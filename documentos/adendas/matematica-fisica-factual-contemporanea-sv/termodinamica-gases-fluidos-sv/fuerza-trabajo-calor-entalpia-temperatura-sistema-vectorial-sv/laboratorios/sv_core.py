"""
sv_core.py — Núcleo operatorio del fibrado soberano Ω_SV para el dominio termodinámico factual.

Implementa fielmente las definiciones canónicas del corpus:
  - §6.2 A^W_i, §6.3 A^Q_i, §6.4 A^U_i por trapecio canónico
  - Contador de clausura C_i en canal W
  - Proyecciones canónicas π_W, π_Q, π_U, π_F, π_Θ, π_Λ (§6)
  - Operador 𝔇_Γ como diferencia factual
  - Identidad canónica Θ·𝔇𝓗 = 𝔇𝒬 (§10.4)
  - Vector director u⃗_SV = 𝔇_Γ Ω_SV (§15.4.b)
  - Generador 𝖦_SV y ecuación escalar nula (§5.1, §5.2)

Política de errores: todas las rutinas levantan SVError(codigo, mensaje) con códigos
del catálogo. No hay catch genéricos ni pases silenciosos.
"""

from __future__ import annotations
import json
import os
from dataclasses import dataclass, field
from typing import List, Tuple, Optional

try:
    import numpy as np
except ImportError as e:
    raise ImportError(
        "numpy es requerido. Instale con: pip install numpy. "
        f"Error original: {e}"
    )

# ---------------------------------------------------------------------------
# CATÁLOGO DE ERRORES — carga única, códigos indexados
# ---------------------------------------------------------------------------

_CATALOGO_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "catalogo_errores.json")

def cargar_catalogo() -> dict:
    """Carga el catálogo maestro. Código IO-001/002 si algo falla."""
    if not os.path.isfile(_CATALOGO_PATH):
        raise SVError("CFG-001", f"Catálogo no encontrado en {_CATALOGO_PATH}")
    with open(_CATALOGO_PATH, "r", encoding="utf-8") as f:
        try:
            d = json.load(f)
        except json.JSONDecodeError as e:
            raise SVError("IO-001", f"Catálogo no es JSON válido: {e}")
    if "codigos" not in d:
        raise SVError("CFG-001", "Catálogo sin clave 'codigos'")
    codigos = d["codigos"]
    # Verificar unicidad de códigos
    if len(codigos) != len(set(codigos.keys())):
        raise SVError("CFG-002", "Catálogo contiene códigos duplicados")
    return d


class SVError(Exception):
    """Excepción del Sistema Vectorial SV. Cada instancia lleva un código del catálogo."""

    def __init__(self, codigo: str, mensaje: str = "", contexto: Optional[dict] = None):
        self.codigo = codigo
        self.mensaje = mensaje
        self.contexto = contexto or {}
        super().__init__(f"[{codigo}] {mensaje}")

    def __repr__(self):
        return f"SVError(codigo={self.codigo!r}, mensaje={self.mensaje!r})"


def validar_codigo(codigo: str, catalogo: Optional[dict] = None) -> None:
    """Verifica que un código exista en el catálogo. Si no, CFG-002."""
    if catalogo is None:
        catalogo = cargar_catalogo()
    if codigo not in catalogo["codigos"]:
        raise SVError(
            "CFG-002",
            f"Código '{codigo}' no declarado en catálogo. "
            f"Prohibido emitir códigos ad-hoc.",
        )


# ---------------------------------------------------------------------------
# ESTRUCTURA DE DATOS: caso canónico
# ---------------------------------------------------------------------------

@dataclass
class CasoCanonico:
    """Caso canónico SV(d, N) con parámetros θ completos."""
    nombre: str
    alfa_beta: np.ndarray   # shape (d, N, 2)
    chi: np.ndarray          # shape (d, N), valores en {0, 1, 2} con 2 == U
    delta_eps: np.ndarray    # shape (N-1,), pesos > 0
    B: np.ndarray            # shape (N,), frontera factual
    H: np.ndarray            # shape (N,), entropía factual creciente
    phi: np.ndarray          # shape (N,), potencial escalar factual
    A_vec: np.ndarray        # shape (N,), potencial vectorial factual (componente)
    J_jac: np.ndarray        # shape (N,), jacobiano factual escalar
    e_hat: np.ndarray        # shape (N,), versor canónico escalar
    n0: int = 0

    def d(self) -> int:
        return self.alfa_beta.shape[0]

    def N(self) -> int:
        return self.alfa_beta.shape[1]

    def validar(self) -> None:
        """Valida θ completo. Levanta SVError con códigos PAR/PRN/CHI/CEL si falla."""
        if self.alfa_beta.ndim != 3 or self.alfa_beta.shape[2] != 2:
            raise SVError("PRN-001", f"alfa_beta debe tener shape (d, N, 2); tiene {self.alfa_beta.shape}")
        d, N = self.d(), self.N()
        if d != 3:
            raise SVError("CEL-002", f"Célula con dimensión d={d}; se requiere d=3 en células canónicas del documento")
        if N < 2:
            raise SVError("CEL-001", f"Célula SV(3, {N}) incompleta: mínimo N=2")
        if np.any(self.alfa_beta < 0):
            raise SVError("PAR-003", "α o β negativos en algún par preternario")
        if self.chi.shape != (d, N):
            raise SVError("PAR-001", f"chi debe tener shape ({d}, {N}); tiene {self.chi.shape}")
        if not np.all(np.isin(self.chi, [0, 1, 2])):
            raise SVError("CHI-001", "χ contiene valores ∉ {0, 1, 2=U}")
        if self.delta_eps.shape != (N - 1,):
            raise SVError("PAR-001", f"delta_eps debe tener shape ({N-1},); tiene {self.delta_eps.shape}")
        if np.any(self.delta_eps <= 0):
            raise SVError("PAR-002", "Algún Δε_k ≤ 0 (peso de suceso inválido)")
        for nombre_arr, arr in [("B", self.B), ("H", self.H), ("phi", self.phi),
                                 ("A_vec", self.A_vec), ("J_jac", self.J_jac), ("e_hat", self.e_hat)]:
            if arr.shape != (N,):
                raise SVError("PAR-001", f"{nombre_arr} debe tener shape ({N},); tiene {arr.shape}")
        if np.any(np.diff(self.H) < -1e-12):
            raise SVError("IRR-002", "Entropía H decrece entre sucesos consecutivos (Teorema 8.2 violado)")
        if np.any(self.H < 0):
            raise SVError("H-002", "Entropía negativa en algún suceso")
        if np.any(self.B < 0):
            raise SVError("B-002", "Frontera ℬ negativa")
        if not (0 <= self.n0 < N):
            raise SVError("PAR-001", f"n0={self.n0} fuera de rango [0, {N-1}]")


# ---------------------------------------------------------------------------
# CONSTRUCCIÓN DEL FIBRADO desde θ — forma EXPLÍCITA
# ---------------------------------------------------------------------------

def construir_acumulados(caso: CasoCanonico) -> dict:
    """
    Forma explícita desde θ. Devuelve diccionario con:
      A_W, A_Q, A_U, C_count, A_total, A_SV, TW (= A_W + C_count), TQ, TU, Lambda
    y los incrementos por paso W_inc, Q_inc, U_inc, DA.
    
    La activación por coordenada es a_i(k) = |β_i(k) − α_i(k)|. Se filtra por canal
    según χ_i(k). Las acumulaciones son trapezoidales canónicas (§6.2, §6.3, §6.4).
    El contador C_i cuenta sucesos con χ_i(k)=0 y se agrega al canal W (§6.2).
    """
    caso.validar()
    d, N = caso.d(), caso.N()
    a = np.abs(caso.alfa_beta[:, :, 1] - caso.alfa_beta[:, :, 0])   # (d, N), ≥ 0
    if np.any(a < 0):
        # Redundante, pero protege contra fallos aritméticos de platform
        raise SVError("PRN-001", "Activación a_i(k) < 0 detectada (imposible por construcción)")
    a_W = np.where(caso.chi == 0, a, 0.0)
    a_Q = np.where(caso.chi == 1, a, 0.0)
    a_U = np.where(caso.chi == 2, a, 0.0)
    # Verificar partición ternaria estricta (no solapamientos)
    suma_canales = a_W + a_Q + a_U
    if not np.allclose(suma_canales, a):
        raise SVError("CHI-003", "Solapamiento de canales: a ≠ a_W + a_Q + a_U")

    A_W = np.zeros(N); A_Q = np.zeros(N); A_U = np.zeros(N); C = np.zeros(N)
    for n in range(1, N):
        inc_W = inc_Q = inc_U = inc_C = 0.0
        for i in range(d):
            inc_W += 0.5 * (a_W[i, n-1] + a_W[i, n]) * caso.delta_eps[n-1]
            inc_Q += 0.5 * (a_Q[i, n-1] + a_Q[i, n]) * caso.delta_eps[n-1]
            inc_U += 0.5 * (a_U[i, n-1] + a_U[i, n]) * caso.delta_eps[n-1]
            inc_C += 1.0 if caso.chi[i, n] == 0 else 0.0
        A_W[n] = A_W[n-1] + inc_W
        A_Q[n] = A_Q[n-1] + inc_Q
        A_U[n] = A_U[n-1] + inc_U
        C[n]   = C[n-1]   + inc_C
    # Monotonía estricta
    if np.any(np.diff(A_W) < -1e-12): raise SVError("W-001", "A^W decrece")
    if np.any(np.diff(A_Q) < -1e-12): raise SVError("Q-001", "A^Q decrece")
    if np.any(np.diff(A_U) < -1e-12): raise SVError("U-001", "A^U decrece")

    TW = A_W + C   # trabajo acumulado = activación W + contador de clausura
    TQ = A_Q.copy()
    TU = A_U.copy()
    A_total = TW + TQ + TU   # 𝒜_SV
    Lambda = A_total + caso.B   # Λ = 𝒜 + ℬ

    # Incrementos por paso (magnitudes puntuales 𝒲, 𝒬, 𝒰 = componentes del vector director)
    W_inc = np.zeros(N); Q_inc = np.zeros(N); U_inc = np.zeros(N); DA = np.zeros(N)
    W_inc[:-1] = np.diff(TW)
    Q_inc[:-1] = np.diff(TQ)
    U_inc[:-1] = np.diff(TU)
    DA[:-1]    = np.diff(A_total)

    # Monotonía de 𝒜 (append-only)
    if np.any(DA[:-1] < -1e-12):
        raise SVError("A-001", "𝒜_SV decrece (viola append-only)")

    return dict(
        a=a, a_W=a_W, a_Q=a_Q, a_U=a_U,
        A_W=A_W, A_Q=A_Q, A_U=A_U, C=C,
        TW=TW, TQ=TQ, TU=TU, A=A_total, Lambda=Lambda,
        W_inc=W_inc, Q_inc=Q_inc, U_inc=U_inc, DA=DA,
    )


def fuerza_canonica(caso: CasoCanonico, fib: dict) -> np.ndarray:
    """
    Fuerza factual 𝓕 según §6.5: 𝓕 = −∇^SV φ + ⋆d 𝒜^vec + 𝒥·ê.
    Representación escalar proyectada: los operadores ∇ y ⋆d se implementan como
    diferencias factuales 𝔇_Γ φ y 𝔇_Γ 𝒜^vec sobre índice de suceso.
    """
    N = caso.N()
    F = np.zeros(N)
    # 𝔇_Γ φ y 𝔇_Γ 𝒜^vec
    for n in range(N - 1):
        grad_phi = caso.phi[n+1] - caso.phi[n]
        rot_Avec = caso.A_vec[n+1] - caso.A_vec[n]
        F[n] = -grad_phi + rot_Avec + caso.J_jac[n] * caso.e_hat[n]
    # F[N-1] se define como el acumulado: F[n-1] = F[0] + Σ ΔF_j
    # Aquí F se interpreta como "fuerza acumulada en paso n→n+1"; el valor final
    # se completa por suma del director:
    for n in range(1, N):
        F[n] = F[0]
        for j in range(n):
            F[n] += (caso.phi[j] - caso.phi[j+1]) + (caso.A_vec[j+1] - caso.A_vec[j]) \
                  + caso.J_jac[j] * caso.e_hat[j]
    # Simplificación: usamos el valor acumulativo canónico en cada n
    F_acum = np.zeros(N)
    F_acum[0] = -caso.phi[0] + caso.A_vec[0] + caso.J_jac[0] * caso.e_hat[0]
    for n in range(1, N):
        grad = caso.phi[n] - caso.phi[n-1]
        rot  = caso.A_vec[n] - caso.A_vec[n-1]
        F_acum[n] = F_acum[n-1] + (-grad) + rot + caso.J_jac[n-1] * caso.e_hat[n-1]
    return F_acum


def temperatura(fib: dict, caso: CasoCanonico) -> np.ndarray:
    """Θ_SV(n) = UFT(𝔇𝒬 / 𝔇𝓗). Sobre régimen 𝔇𝓗 ≤ 1e-12, Θ = 0 convencional."""
    N = caso.N()
    DH = np.zeros(N); DH[:-1] = np.diff(caso.H)
    Theta = np.zeros(N)
    for n in range(N - 1):
        if DH[n] > 1e-12:
            Theta[n] = fib["Q_inc"][n] / DH[n]
        else:
            # Régimen no-térmico: Θ por convención del documento, no se emite error
            Theta[n] = 0.0
    return Theta


# ---------------------------------------------------------------------------
# FORMA IMPLÍCITA — despeje del balance
# ---------------------------------------------------------------------------

def forma_implicita(fib_exp: dict, caso: CasoCanonico) -> dict:
    """
    Despeja cada magnitud usando la ecuación escalar nula 𝔇𝒜 − 𝒲 − 𝒬 − 𝒰 = 0.
    Devuelve los valores reconstruidos por camino algebraico distinto.
    """
    DA = fib_exp["DA"]
    W_imp = DA - fib_exp["Q_inc"] - fib_exp["U_inc"]
    Q_imp = DA - fib_exp["W_inc"] - fib_exp["U_inc"]
    U_imp = DA - fib_exp["W_inc"] - fib_exp["Q_inc"]
    # Reintegrar acumulados desde punto base
    N = caso.N()
    TW_imp = np.zeros(N); TQ_imp = np.zeros(N); TU_imp = np.zeros(N); A_imp = np.zeros(N)
    TW_imp[0] = fib_exp["TW"][0]; TQ_imp[0] = fib_exp["TQ"][0]
    TU_imp[0] = fib_exp["TU"][0]; A_imp[0]  = fib_exp["A"][0]
    for n in range(1, N):
        TW_imp[n] = TW_imp[n-1] + W_imp[n-1]
        TQ_imp[n] = TQ_imp[n-1] + Q_imp[n-1]
        TU_imp[n] = TU_imp[n-1] + U_imp[n-1]
        A_imp[n]  = A_imp[n-1]  + DA[n-1]
    Lambda_imp = A_imp + caso.B
    return dict(TW=TW_imp, TQ=TQ_imp, TU=TU_imp, A=A_imp, Lambda=Lambda_imp,
                W_inc=W_imp, Q_inc=Q_imp, U_inc=U_imp, DA=DA)


# ---------------------------------------------------------------------------
# FORMA PARAMÉTRICA — punto base + Σ vector director
# ---------------------------------------------------------------------------

def vector_director(fib_exp: dict, F_acum: np.ndarray, caso: CasoCanonico) -> dict:
    """
    Vector director u⃗_SV = 𝔇_Γ Ω_SV. Devuelve sus componentes canónicas por paso.
    u_A, u_W, u_Q, u_U, u_Lambda, u_F, u_H.
    """
    N = caso.N()
    u_W = fib_exp["W_inc"].copy()
    u_Q = fib_exp["Q_inc"].copy()
    u_U = fib_exp["U_inc"].copy()
    u_A = u_W + u_Q + u_U   # por balance
    u_Lambda = np.zeros(N); u_Lambda[:-1] = np.diff(fib_exp["Lambda"])
    u_F      = np.zeros(N); u_F[:-1]      = np.diff(F_acum)
    u_H      = np.zeros(N); u_H[:-1]      = np.diff(caso.H)
    return dict(u_W=u_W, u_Q=u_Q, u_U=u_U, u_A=u_A, u_Lambda=u_Lambda, u_F=u_F, u_H=u_H)


def forma_parametrica(fib_exp: dict, F_acum: np.ndarray, caso: CasoCanonico) -> dict:
    """Reconstruye cada magnitud como base + Σ u_M desde n0."""
    u = vector_director(fib_exp, F_acum, caso)
    N = caso.N(); n0 = caso.n0
    TW_p = np.zeros(N); TQ_p = np.zeros(N); TU_p = np.zeros(N)
    A_p  = np.zeros(N); L_p  = np.zeros(N); F_p  = np.zeros(N)
    TW_p[n0] = fib_exp["TW"][n0]; TQ_p[n0] = fib_exp["TQ"][n0]
    TU_p[n0] = fib_exp["TU"][n0]; A_p[n0]  = fib_exp["A"][n0]
    L_p[n0]  = fib_exp["Lambda"][n0]; F_p[n0] = F_acum[n0]
    for lam in range(1, N - n0):
        i = n0 + lam
        TW_p[i] = TW_p[i-1] + u["u_W"][i-1]
        TQ_p[i] = TQ_p[i-1] + u["u_Q"][i-1]
        TU_p[i] = TU_p[i-1] + u["u_U"][i-1]
        A_p[i]  = A_p[i-1]  + u["u_A"][i-1]
        L_p[i]  = L_p[i-1]  + u["u_Lambda"][i-1]
        F_p[i]  = F_p[i-1]  + u["u_F"][i-1]
    return dict(TW=TW_p, TQ=TQ_p, TU=TU_p, A=A_p, Lambda=L_p, F=F_p, u=u)


# ---------------------------------------------------------------------------
# GENERADOR 𝖦_SV y PRODUCTO ESCALAR
# ---------------------------------------------------------------------------

# Vector normal 𝖦_SV = (1, 0, 0, 0, 0) − (π_W* + π_Q* + π_U*)
# En representación de proyecciones reducidas (𝒜, 𝓗, 𝒥, ℛ, ℬ; 𝒲; 𝒬; 𝒰):
# 𝖦_SV ≡ (+1, 0, 0, 0, 0 ; −1, −1, −1)
G_SV = np.array([+1.0, 0.0, 0.0, 0.0, 0.0, -1.0, -1.0, -1.0])


def producto_G(u_extendido: np.ndarray) -> float:
    """
    Contrae un vector director extendido (8 componentes) con 𝖦_SV.
    El vector extendido es (u_A, u_H, u_J, u_R, u_B, u_W, u_Q, u_U).
    """
    if u_extendido.shape != (8,):
        raise SVError("ORT-003", f"Vector director extendido debe tener shape (8,); tiene {u_extendido.shape}")
    return float(np.dot(u_extendido, G_SV))


# ---------------------------------------------------------------------------
# UTILIDADES DE COMPARACIÓN
# ---------------------------------------------------------------------------

TOLERANCIA_DEFAULT = 1e-9


def comparar_formas(valor_exp, valor_imp, valor_par, codigo_base: str,
                    nombre_magnitud: str, tolerancia: float = TOLERANCIA_DEFAULT) -> None:
    """
    Compara los valores producidos por las tres formas. Emite SVError con el
    sufijo correspondiente si difieren:
      valor_exp vs valor_imp  →  {codigo_base}-005  "difiere explícita vs implícita"
      valor_exp vs valor_par  →  {codigo_base}-006  "difiere explícita vs paramétrica"
    """
    a = float(valor_exp); b = float(valor_imp); c = float(valor_par)
    if abs(a - b) > tolerancia:
        raise SVError(f"{codigo_base}-005",
                      f"{nombre_magnitud}: forma explícita ({a}) ≠ implícita ({b}), diff={abs(a-b):.3e}")
    if abs(a - c) > tolerancia:
        raise SVError(f"{codigo_base}-006",
                      f"{nombre_magnitud}: forma explícita ({a}) ≠ paramétrica ({c}), diff={abs(a-c):.3e}")


# ---------------------------------------------------------------------------
# Cargador de casos canónicos desde JSON
# ---------------------------------------------------------------------------

_CASOS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "datos", "casos_canonicos.json")


def cargar_casos() -> List[CasoCanonico]:
    """Carga los tres casos A, B, C desde el JSON de datos."""
    if not os.path.isfile(_CASOS_PATH):
        raise SVError("IO-002", f"Archivo de casos no encontrado: {_CASOS_PATH}")
    with open(_CASOS_PATH, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError as e:
            raise SVError("IO-001", f"JSON de casos inválido: {e}")
    if "casos" not in data:
        raise SVError("IO-001", "JSON de casos sin clave 'casos'")
    casos = []
    for c in data["casos"]:
        try:
            caso = CasoCanonico(
                nombre=c["nombre"],
                alfa_beta=np.array(c["alfa_beta"], dtype=float),
                chi=np.array(c["chi"], dtype=int),
                delta_eps=np.array(c["delta_eps"], dtype=float),
                B=np.array(c["B"], dtype=float),
                H=np.array(c["H"], dtype=float),
                phi=np.array(c["phi"], dtype=float),
                A_vec=np.array(c["A_vec"], dtype=float),
                J_jac=np.array(c["J_jac"], dtype=float),
                e_hat=np.array(c["e_hat"], dtype=float),
                n0=int(c.get("n0", 0)),
            )
        except KeyError as e:
            raise SVError("IO-003", f"Caso incompleto, falta clave {e}")
        caso.validar()
        casos.append(caso)
    if len(casos) == 0:
        raise SVError("IO-001", "Ningún caso canónico cargado")
    return casos


if __name__ == "__main__":
    # Self-check mínimo
    cat = cargar_catalogo()
    print(f"[sv_core] Catálogo cargado: {len(cat['codigos'])} códigos.")
    try:
        casos = cargar_casos()
        print(f"[sv_core] Casos cargados: {[c.nombre for c in casos]}")
    except SVError as e:
        print(f"[sv_core] No hay casos cargables todavía ({e.codigo}: {e.mensaje})")
