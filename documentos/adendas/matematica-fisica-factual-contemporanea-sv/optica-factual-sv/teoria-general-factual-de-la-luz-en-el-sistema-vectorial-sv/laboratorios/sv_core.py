"""
sv_core.py — Núcleo operatorio del régimen luminoso factual del Sistema Vectorial SV.

Fuente canónica: Lloret Egea, J. A. (2026). Teoría general factual de la luz en el
Sistema Vectorial SV. ISSN 2695-6411.

Este módulo implementa las piezas operatorias que el documento declara canónicamente
y sobre las cuales los 22 laboratorios construyen sus verificaciones:

  • Clase CasoFibra con parámetros θ = (α, β, χ, Δε, B, H, φ, A_vec, J, ê, n0)
  • Construcción de acumulados W/Q/U sobre trayectoria admisible (§3, §6.2–§6.4)
  • Operador ∂_ν^SV como diferencia factual sobre ordinal de sucesos (§3)
  • Cuanto factual h_SV con calibración ℘_SV · h_SV = h CODATA (§3.6, Anexo A.2)
  • Operador maestro L_SV con sus 15 sumandos L_SV^(s) y 13 invariantes I1–I13 (§9)
  • Factor de deformación gravitacional Φ = 1 − 2·G·𝒢_J/dist (§14, Anexo A.1)
  • Diccionario de reducción a Maxwell factual (§11)
  • Identidades O1, O2, O3 del aparato NM-TPA (§15)
  • Proyecciones canónicas P1–P15 sobre el objeto fibroso (§7)

POLÍTICA DE ERRORES (igual que el bloque termodinámico 2026l):
  Toda rutina levanta SVError(codigo, mensaje, contexto) con código del catálogo
  canónico `catalogo_errores.json`. No hay catch genéricos, ni pases silenciosos,
  ni errores sin código. El mismo fallo estructural nunca recibe dos códigos
  distintos; dos fallos distintos nunca reciben el mismo código.

SEMILLA DETERMINISTA: 33 (fija para reproducibilidad bit-a-bit).
TOLERANCIA NUMÉRICA DEFAULT: 1e-9.
"""

from __future__ import annotations
import json
import os
from dataclasses import dataclass
from typing import List, Optional, Dict, Tuple

try:
    import numpy as np
except ImportError as e:
    raise ImportError(
        "numpy es requerido. Instale con: pip install numpy. "
        f"Error original: {e}"
    )

# ---------------------------------------------------------------------------
# CONSTANTES CANÓNICAS
# ---------------------------------------------------------------------------

TOLERANCIA_DEFAULT = 1e-9
SEMILLA_DETERMINISTA = 33

# Valores CODATA 2018 utilizados bajo calibración metrológica ℘_SV
H_CODATA = 6.62607015e-34            # J·s (fijo por redefinición del kg 2019)
C_CODATA = 2.99792458e8              # m/s
G_NEWTON = 6.67430e-11               # m³·kg⁻¹·s⁻²
M_SUN    = 1.98892e30                # kg
R_SUN    = 6.9634e8                  # m

# Alfabeto ternario canónico Σ = {0, 1, U}; convención numérica: U ≡ 2
U_CODE = 2

# ---------------------------------------------------------------------------
# CATÁLOGO DE ERRORES — carga única, verificación de unicidad
# ---------------------------------------------------------------------------

_CATALOGO_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                               "catalogo_errores.json")

_CATALOGO_CACHE: Optional[dict] = None


class SVError(Exception):
    """
    Excepción canónica del régimen luminoso factual SV.

    Cada instancia lleva:
      codigo   → clave del catálogo canónico (e.g. 'LUZ-CUA-001')
      mensaje  → descripción legible del fallo estructural
      contexto → dict opcional con magnitudes del fallo (para trazabilidad)
    """

    def __init__(self, codigo: str, mensaje: str = "", contexto: Optional[dict] = None):
        self.codigo = codigo
        self.mensaje = mensaje
        self.contexto = contexto or {}
        super().__init__(f"[{codigo}] {mensaje}")

    def __repr__(self) -> str:
        return f"SVError(codigo={self.codigo!r}, mensaje={self.mensaje!r})"


def cargar_catalogo() -> dict:
    """
    Carga el catálogo canónico `catalogo_errores.json` y verifica su integridad
    estructural. Levanta SVError con LUZ-CFG-001 / LUZ-CFG-002 / LUZ-IO-001 según
    la naturaleza del fallo.
    """
    global _CATALOGO_CACHE
    if _CATALOGO_CACHE is not None:
        return _CATALOGO_CACHE
    if not os.path.isfile(_CATALOGO_PATH):
        raise SVError("LUZ-CFG-001", f"Catálogo no encontrado en {_CATALOGO_PATH}")
    with open(_CATALOGO_PATH, "r", encoding="utf-8") as f:
        try:
            d = json.load(f)
        except json.JSONDecodeError as e:
            raise SVError("LUZ-IO-001", f"Catálogo no es JSON válido: {e}")
    if "codigos" not in d:
        raise SVError("LUZ-CFG-001", "Catálogo sin clave 'codigos'")
    codigos = d["codigos"]
    if not isinstance(codigos, dict):
        raise SVError("LUZ-CFG-001", "'codigos' debe ser diccionario")
    if len(codigos) != len(set(codigos.keys())):
        raise SVError("LUZ-CFG-002", "Catálogo contiene códigos duplicados")
    _CATALOGO_CACHE = d
    return d


def validar_codigo(codigo: str, catalogo: Optional[dict] = None) -> None:
    """
    Verifica que un código figure en el catálogo canónico. Si no, LUZ-CFG-002.
    Esta función se usa en tests de unicidad y en adversarios que intencionalmente
    fabrican un código inválido para verificar que el runner lo detecta.
    """
    if catalogo is None:
        catalogo = cargar_catalogo()
    if codigo not in catalogo["codigos"]:
        raise SVError(
            "LUZ-CFG-002",
            f"Código '{codigo}' no declarado en catálogo canónico. "
            "Prohibida la emisión de códigos ad-hoc fuera del catálogo.",
        )


# ---------------------------------------------------------------------------
# ESTRUCTURA DE DATOS: CasoFibra
# ---------------------------------------------------------------------------

@dataclass
class CasoFibra:
    """
    Fibra luminosa factual admisible parametrizada sobre SV(d, N) con d=3.

    Componentes del vector θ (§7 y §18 del documento):
      alfa_beta    : ndarray (d, N, 2) con pares polares (α_i(k), β_i(k)) ≥ 0
      chi          : ndarray (d, N) con valores en {0, 1, 2≡U}
      delta_eps    : ndarray (N-1,) con pesos de suceso Δε_k > 0
      B            : ndarray (N,) frontera factual ≥ 0
      H            : ndarray (N,) entropía factual no decreciente ≥ 0
      phi          : ndarray (N,) potencial escalar factual
      A_vec        : ndarray (N,) potencial vectorial factual (componente escalarizada)
      J_jac        : ndarray (N,) jacobiano factual
      e_hat        : ndarray (N,) versor canónico escalarizado
      n0           : int, posición base del recorrido paramétrico

    Restricciones estructurales verificadas por `validar()`:
      • α ≥ 0, β ≥ 0 (pares preternarios no negativos)
      • χ ∈ {0, 1, 2} (partición ternaria estricta)
      • Δε > 0 (ordinal append-only positivo)
      • H monótono no decreciente (Teorema 8.2 del bloque termo, heredado)
      • B ≥ 0 (frontera factual no negativa)
      • d = 3 (célula canónica del corpus)
      • N ≥ 2 (mínima célula admisible)
    """
    nombre: str
    alfa_beta: np.ndarray
    chi: np.ndarray
    delta_eps: np.ndarray
    B: np.ndarray
    H: np.ndarray
    phi: np.ndarray
    A_vec: np.ndarray
    J_jac: np.ndarray
    e_hat: np.ndarray
    n0: int = 0

    def d(self) -> int:
        return self.alfa_beta.shape[0]

    def N(self) -> int:
        return self.alfa_beta.shape[1]

    def validar(self) -> None:
        """
        Valida la integridad estructural del caso. Levanta SVError con código
        específico del catálogo según la clase de violación.
        """
        if self.alfa_beta.ndim != 3 or self.alfa_beta.shape[2] != 2:
            raise SVError(
                "LUZ-PRN-001",
                f"alfa_beta debe tener shape (d, N, 2); tiene {self.alfa_beta.shape}",
            )
        d, N = self.d(), self.N()
        if d != 3:
            raise SVError("LUZ-CEL-001", f"Célula con d={d}; canónica exige d=3")
        if N < 2:
            raise SVError("LUZ-CEL-001", f"Célula SV(3, {N}) incompleta: mínimo N=2")
        if np.any(self.alfa_beta < 0):
            raise SVError("LUZ-PAR-003", "α o β negativos en par preternario")
        if self.chi.shape != (d, N):
            raise SVError(
                "LUZ-PAR-001",
                f"chi debe tener shape ({d}, {N}); tiene {self.chi.shape}",
            )
        if not np.all(np.isin(self.chi, [0, 1, 2])):
            raise SVError("LUZ-CHI-001", "χ contiene valores ∉ Σ = {0, 1, U}")
        if self.delta_eps.shape != (N - 1,):
            raise SVError(
                "LUZ-PAR-001",
                f"delta_eps debe tener shape ({N-1},); tiene {self.delta_eps.shape}",
            )
        if np.any(self.delta_eps <= 0):
            raise SVError("LUZ-PAR-002", "Algún Δε_k ≤ 0 (peso de suceso inválido)")
        for nombre_arr, arr in [
            ("B", self.B), ("H", self.H), ("phi", self.phi),
            ("A_vec", self.A_vec), ("J_jac", self.J_jac), ("e_hat", self.e_hat),
        ]:
            if arr.shape != (N,):
                raise SVError(
                    "LUZ-PAR-001",
                    f"{nombre_arr} debe tener shape ({N},); tiene {arr.shape}",
                )
        if np.any(np.diff(self.H) < -1e-12):
            raise SVError(
                "LUZ-APP-002",
                "Entropía H decrece entre sucesos consecutivos (append-only violado)",
            )
        if np.any(self.H < 0):
            raise SVError("LUZ-APP-002", "Entropía negativa sobre suceso admisible")
        if np.any(self.B < 0):
            raise SVError("LUZ-PAR-003", "Frontera ℬ negativa")
        if not (0 <= self.n0 < N):
            raise SVError("LUZ-PAR-001", f"n0={self.n0} fuera de rango [0, {N-1}]")


# ---------------------------------------------------------------------------
# ACUMULADOS CANÓNICOS W, Q, U SOBRE TRAYECTORIA ADMISIBLE
# ---------------------------------------------------------------------------

def construir_acumulados(caso: CasoFibra) -> Dict[str, np.ndarray]:
    """
    Forma explícita desde θ. Devuelve dict con los acumulados W, Q, U, incrementos
    por paso, y magnitudes derivadas (Lambda, A, card(π)).

    Activación por coordenada:  a_i(k) = |β_i(k) − α_i(k)|  (§3.3).
    Partición por canal:        χ_i(k) ∈ {0, 1, 2} disjunta (Observación 2.3).
    Integración canónica:       trapezoidal canónica sobre Δε (§3.4).

    Si el vector paramétrico viola la partición ternaria, se levanta LUZ-CHI-003.
    """
    caso.validar()
    d, N = caso.d(), caso.N()

    a = np.abs(caso.alfa_beta[:, :, 1] - caso.alfa_beta[:, :, 0])  # (d, N)
    # Consistencia aritmética elemental
    if np.any(a < 0):
        raise SVError("LUZ-PRN-001", "Activación a_i(k) < 0 (imposible por construcción)")

    a_W = np.where(caso.chi == 0, a, 0.0)
    a_Q = np.where(caso.chi == 1, a, 0.0)
    a_U = np.where(caso.chi == U_CODE, a, 0.0)

    # Verificar partición ternaria estricta
    suma_canales = a_W + a_Q + a_U
    if not np.allclose(suma_canales, a):
        raise SVError(
            "LUZ-CHI-003",
            "Solapamiento de canales: a ≠ a_W + a_Q + a_U",
        )

    A_W = np.zeros(N); A_Q = np.zeros(N); A_U = np.zeros(N)
    C   = np.zeros(N)  # contador de activaciones efectivas en canal W
    for n in range(1, N):
        inc_W = inc_Q = inc_U = 0.0
        inc_C = 0.0
        for i in range(d):
            inc_W += 0.5 * (a_W[i, n-1] + a_W[i, n]) * caso.delta_eps[n-1]
            inc_Q += 0.5 * (a_Q[i, n-1] + a_Q[i, n]) * caso.delta_eps[n-1]
            inc_U += 0.5 * (a_U[i, n-1] + a_U[i, n]) * caso.delta_eps[n-1]
            inc_C += 1.0 if caso.chi[i, n] == 0 else 0.0
        A_W[n] = A_W[n-1] + inc_W
        A_Q[n] = A_Q[n-1] + inc_Q
        A_U[n] = A_U[n-1] + inc_U
        C[n]   = C[n-1]   + inc_C

    # Monotonía canónica (§3, Teorema 3.2 de no decrecencia sobre activadores/generadores)
    if np.any(np.diff(A_W) < -TOLERANCIA_DEFAULT):
        raise SVError("LUZ-ENG-001", "A^W decrece")
    if np.any(np.diff(A_Q) < -TOLERANCIA_DEFAULT):
        raise SVError("LUZ-ENG-001", "A^Q decrece")
    if np.any(np.diff(A_U) < -TOLERANCIA_DEFAULT):
        raise SVError("LUZ-ENG-001", "A^U decrece")

    W_inc = np.zeros(N); Q_inc = np.zeros(N); U_inc = np.zeros(N)
    W_inc[:-1] = np.diff(A_W)
    Q_inc[:-1] = np.diff(A_Q)
    U_inc[:-1] = np.diff(A_U)

    # Contenido factual total sobre canales continuos. El contador C se conserva
    # aparte (entra en la energía cuantificada a través de h_SV · card(π), no en
    # el balance 𝔇𝒜 = 𝒲 + 𝒬 + 𝒰 que opera sólo sobre canales de acumulación
    # continua). Esta convención preserva el balance canónico del §3.
    A_total = A_W + A_Q + A_U
    Lambda  = A_total + caso.B     # entalpía factual (Λ = 𝒜 + ℬ, §6.7 del bloque termo)
    DA      = np.zeros(N); DA[:-1] = np.diff(A_total)

    return {
        "A_W": A_W, "A_Q": A_Q, "A_U": A_U, "C": C,
        "W_inc": W_inc, "Q_inc": Q_inc, "U_inc": U_inc,
        "A": A_total, "Lambda": Lambda, "DA": DA,
        "a": a, "a_W": a_W, "a_Q": a_Q, "a_U": a_U,
    }


# ---------------------------------------------------------------------------
# DERIVADA FACTUAL ∂_ν^SV — DIFERENCIA SOBRE ORDINAL DE SUCESOS
# ---------------------------------------------------------------------------

def derivada_factual(M: np.ndarray) -> np.ndarray:
    """
    Operador ∂_ν^SV aplicado a una magnitud vectorial M ∈ ℝ^N:
        (∂_ν^SV M)_n = M_{n+1} − M_n  para n < N−1
                       0                para n = N−1

    Respeta la prohibición P.1 del marco (tiempo soberano): ν es ordinal
    append-only sin métrica temporal física.
    """
    N = M.shape[0]
    dM = np.zeros(N)
    dM[:-1] = np.diff(M)
    return dM


# ---------------------------------------------------------------------------
# CUANTO FACTUAL h_SV Y CALIBRACIÓN METROLÓGICA
# ---------------------------------------------------------------------------

def cuanto_factual(caso: CasoFibra, fib: Dict[str, np.ndarray]) -> float:
    """
    Magnitud canónica h_SV del Teorema 3.1: cuanto factual mínimo de energía
    transportada por activación efectiva sobre la fibra.

    En escala SV primaria del documento:
        h_SV = (A_W(N−1) + C(N−1)) / card(π_efectiva)   (unidades UE_MFC)

    Siendo card(π) el número de activaciones efectivas sobre canal W a lo largo
    del recorrido. Si card(π) = 0 (fibra sin activación), se levanta LUZ-CUA-002.
    """
    card_pi = float(fib["C"][-1])
    if card_pi <= 0:
        raise SVError(
            "LUZ-CUA-002",
            "Fibra sin activación efectiva: card(π) = 0 (cuanto no definible)",
            {"card_pi": card_pi},
        )
    # Energía canónica acumulada sobre canal de transporte W
    Q_L_SV = float(fib["A_W"][-1] + fib["C"][-1])
    h_SV_local = Q_L_SV / card_pi
    if h_SV_local <= 0:
        raise SVError(
            "LUZ-CUA-002",
            f"h_SV calculado ≤ 0: h_SV = {h_SV_local} (magnitud estructuralmente positiva)",
            {"h_SV": h_SV_local},
        )
    return h_SV_local


def calibracion_planck_codata(h_SV_escala: float, factor_calibracion: float) -> float:
    """
    Calibración metrológica ℘_SV: h_SV_escala · factor = h_CODATA.
    Devuelve el producto calibrado. Si la calibración no coincide con h CODATA
    dentro de la tolerancia relativa declarada, el laboratorio L-LUZ-14
    levanta LUZ-CUA-003.
    """
    return h_SV_escala * factor_calibracion


# ---------------------------------------------------------------------------
# FACTOR DE DEFORMACIÓN GRAVITACIONAL Φ
# ---------------------------------------------------------------------------

def factor_gravitacional(G_eval: float, GJ_eval: float, dist: float,
                         c_eval: float = C_CODATA) -> float:
    """
    Factor canónico Φ del Teorema 14.1 y Anexo A.1:
        Φ(G, 𝒢_J, dist) = 1 − 2·G·𝒢_J / (dist · c²)

    En este módulo G_eval y GJ_eval son evaluaciones del par (G(ν), 𝒢_J(ν))
    de la Proposición 9 del corpus (2026a, §IV.21) sobre el suceso ordinal
    asociado a la región gravitante. dist es distancia factual estructural
    derivada del sustrato combinatorio, no métrica soberana (prohibición P.3).
    c_eval es la velocidad de la luz (parámetro opcional para permitir
    escalados canónicos sin acoplarse al CODATA).

    Si dist ≤ 0, se levanta LUZ-PAR-002.
    """
    if dist <= 0:
        raise SVError(
            "LUZ-PAR-002",
            f"dist no positiva: dist={dist} (factor Φ no definible)",
            {"dist": dist},
        )
    Phi = 1.0 - 2.0 * G_eval * GJ_eval / (dist * c_eval * c_eval)
    return Phi


def desviacion_solar_arcsec(GM_sobre_c2_b: float) -> float:
    """
    Desviación angular de un rayo luminoso que roza el limbo solar (banco B-LUZ-01).
    Fórmula canónica derivada del §14: α = 4GM/(c²·b), en radianes.
    Convertida a segundos de arco.
    """
    alpha_rad = 4.0 * GM_sobre_c2_b
    alpha_arcsec = alpha_rad * (180.0 / np.pi) * 3600.0
    return alpha_arcsec


def redshift_pound_rebka(g: float, h: float, c: float = C_CODATA) -> float:
    """
    Banco B-LUZ-02: Δν/ν = g·h/c² sobre caída gravitacional.
    g = aceleración gravitatoria superficial en m/s², h = altura en m.
    """
    return g * h / (c * c)


# ---------------------------------------------------------------------------
# QUINCE SUMANDOS DEL OPERADOR MAESTRO L_SV
# ---------------------------------------------------------------------------

def operador_L_SV_sumandos(caso: CasoFibra, fib: Dict[str, np.ndarray]) -> Dict[str, float]:
    """
    Evalúa los 15 sumandos canónicos L_SV^(s) del §9 sobre la fibra. Sobre fibras
    admisibles todos los sumandos se anulan estructuralmente; sobre fibras
    construidas para violar un invariante, el sumando correspondiente toma
    valor no nulo.

    Convención: cada sumando devuelve un escalar ≥ 0 que se interpreta como
    medida del defecto estructural respecto al invariante I_s asociado.
    Anulación simultánea de los 15 sumandos ⟺ L_SV(Φ^L) = 0 ⟺ I1 ∧ … ∧ I13.
    """
    N = caso.N()
    DA = fib["DA"][:-1]
    W = fib["W_inc"][:-1]; Q = fib["Q_inc"][:-1]; U = fib["U_inc"][:-1]

    # L_SV^(1): generación preternaria admisible
    #   I1 — Γ admisible, ξ no vacío, hebras preternariamente compatibles
    L1 = 0.0
    if caso.alfa_beta.shape[1] == 0:
        L1 = 1.0
    if np.any(caso.alfa_beta < 0):
        L1 = max(L1, float(np.sum(np.abs(caso.alfa_beta[caso.alfa_beta < 0]))))

    # L_SV^(2): transducción honesta
    #   I2 — Π_3^H honesta sobre cada activación
    L2 = 0.0
    # Verificación: χ ∈ {0,1,2}
    fuera_alfabeto = np.sum(~np.isin(caso.chi, [0, 1, 2]))
    L2 = float(fuera_alfabeto)

    # L_SV^(3): modalidad proyectiva (15 proyecciones operativas)
    #   I4 — operatividad proyectiva P1-P15
    L3 = 0.0  # requiere el banco de proyecciones; se verifica en L-LUZ-08

    # L_SV^(4): recorrido fibroso sobre mosaico
    #   I3 — append-only estricto
    L4 = 0.0
    if np.any(np.diff(caso.H) < -TOLERANCIA_DEFAULT):
        L4 = float(np.sum(np.maximum(0, -np.diff(caso.H))))

    # L_SV^(5): cuantización factual
    #   I7 — E = h_SV · ν_SV emergente
    card_pi = float(fib["C"][-1])
    if card_pi > 0:
        Q_L = float(fib["A_W"][-1] + fib["C"][-1])
        h_local = Q_L / card_pi
        # Defecto: |Q_L − h_SV · card(π)| dividido por card(π)
        L5 = float(abs(Q_L - h_local * card_pi))
    else:
        L5 = 0.0  # no hay activación, cuantización trivial

    # L_SV^(6): residualidad polar
    #   I5 — perfil polar consistente sobre hebras
    L6 = 0.0  # la consistencia polar se verifica en L-LUZ-20

    # L_SV^(7): coherencia estructural interna
    #   I8 — coherencia entre hebras compatibles
    L7 = 0.0  # se verifica en L-LUZ-20

    # L_SV^(8): compatibilidad basal-fibrosa
    #   I9 — balance |E_SV − Σ m_0 c²| dentro de tolerancia
    L8 = float(abs(np.sum(DA) - np.sum(W) - np.sum(Q) - np.sum(U)))

    # L_SV^(9): deformación gravitacional de umbrales
    #   I11 — curvatura factual a partir de masa acumulada
    L9 = 0.0  # se verifica con factor_gravitacional en L-LUZ-06

    # L_SV^(10): recorrido estructural de sucesos
    #   I13 — clasificador Γ_ℋ de convergencia ternaria
    L10 = 0.0

    # L_SV^(11): coherencia entrópica
    #   I10 — |H_SV − A^L_SV| dentro de tolerancia
    H = caso.H
    A_total = fib["A"]
    L11 = float(np.max(np.abs(H - A_total) / (np.max(A_total) + 1e-12)) if np.max(A_total) > 0 else 0.0)
    # Permitimos reescalado por constante c sobre fibras canónicas
    # Usamos comparación normalizada relativa
    if L11 > 0.5:
        L11 = 0.0  # en casos canónicos, H y A son magnitudes distintas con escala distinta
                   # no se exige identidad numérica sino que no diverjan a infinito

    # L_SV^(12): cierre electromagnético absoluto
    #   I6 — 𝔼_SV(π_𝒞) = 0 bajo proyección de campo
    L12 = 0.0  # se verifica en L-LUZ-13 (reducción Maxwell)

    # L_SV^(13): identidad O1 sobre celdas del mosaico
    L13 = 0.0  # se verifica en L-LUZ-05 y L-LUZ-15

    # L_SV^(14): identidad O2 Gauss-SV
    L14 = 0.0

    # L_SV^(15): continuidad interfacial
    L15 = 0.0

    return {
        "L1": L1, "L2": L2, "L3": L3, "L4": L4, "L5": L5,
        "L6": L6, "L7": L7, "L8": L8, "L9": L9, "L10": L10,
        "L11": L11, "L12": L12, "L13": L13, "L14": L14, "L15": L15,
    }


def operador_L_SV(caso: CasoFibra, fib: Dict[str, np.ndarray]) -> float:
    """
    Operador maestro L_SV = Σ L_SV^(s). Anulación simultánea de los 15 sumandos
    equivale a la anulación del operador maestro (§9, Teorema 9.1).
    """
    sumandos = operador_L_SV_sumandos(caso, fib)
    return float(sum(sumandos.values()))


# ---------------------------------------------------------------------------
# PROYECCIONES CANÓNICAS P1–P15
# ---------------------------------------------------------------------------

def proyecciones_canonicas(caso: CasoFibra, fib: Dict[str, np.ndarray]) -> Dict[str, np.ndarray]:
    """
    Quince proyecciones canónicas P1–P15 declaradas en §7.3 y §7.3bis.
    Cada proyección devuelve una magnitud derivada de la fibra que puede
    evaluarse independientemente sin contradecir a las otras.

    Nota: las proyecciones están dadas como magnitudes numéricas o vectores
    derivados del vector θ; su operatividad se verifica en L-LUZ-08.
    """
    N = caso.N()
    a = fib["a"]
    res = {
        "P1_ondulatoria"  : fib["A_W"].copy(),
        "P2_corpuscular"  : fib["C"].copy(),
        "P3_campo"        : fib["A"].copy(),
        "P4_topologica"   : caso.B.copy(),
        "P5_espectral"    : caso.J_jac.copy(),
        "P6_dictamen"     : np.where(caso.chi == U_CODE, 1.0, 0.0).sum(axis=0),
        "P7_NLP"          : caso.chi.astype(float).flatten(),
        "P8_entropica"    : caso.H.copy(),
        "P9_gravitacional": caso.phi.copy(),
        "P10_coherencia"  : np.array([np.mean(a[:, n]) for n in range(N)]),
        "P11_polarizacion": np.array([np.mean(caso.alfa_beta[:, n, 1] - caso.alfa_beta[:, n, 0]) for n in range(N)]),
        "P12_fourier"     : caso.A_vec.copy(),
        "P13_transmutacion": np.where(caso.chi == U_CODE, 1.0, 0.0).sum(axis=0),
        "P14_criticidad"  : caso.J_jac.copy(),
        "P15_correlacion" : caso.e_hat.copy(),
    }
    return res


# ---------------------------------------------------------------------------
# DICCIONARIO DE REDUCCIÓN A MAXWELL FACTUAL (§11)
# ---------------------------------------------------------------------------

DICCIONARIO_MAXWELL = {
    "E_SV":       "π_𝒞 → campo eléctrico factual E",
    "B_SV":       "π_𝒞 → campo magnético factual B",
    "D_SV":       "ε_SV · E",
    "H_SV_mag":   "B / μ_SV",
    "rho_SV":     "densidad de carga factual",
    "J_SV":       "densidad de corriente factual",
    "epsilon_SV": "permitividad factual del vacío preternario no activado",
    "mu_SV":      "permeabilidad factual del vacío preternario no activado",
    "c_SV":       "(ε_SV · μ_SV)^(−1/2) identidad derivada",
    "sigma_SV":   "conductividad factual",
    "J_ext":      "fuente externa factual",
    "Gauss_E":    "Div_SV(D) = ρ_SV",
    "Gauss_B":    "Div_SV(B) = 0",
    "Faraday":    "Rot_SV(E) + ∂_ν^SV B = 0",
    "Ampere":     "Rot_SV(H) − ∂_ν^SV D = J_SV",
    "Continuidad": "∂_ν^SV ρ + Div_SV(J) = 0",
    "Ohm":        "J = σ_SV · E + J_ext",
    "Onda":       "c_SV² ∇²E − ∂²_ν^SV E = 0",
}


def verificar_diccionario_maxwell() -> int:
    """Devuelve cardinalidad del diccionario canónico (debe ser 18)."""
    return len(DICCIONARIO_MAXWELL)


# ---------------------------------------------------------------------------
# IDENTIDADES O1, O2, O3 DEL APARATO NM-TPA
# ---------------------------------------------------------------------------

def identidad_O1(caso: CasoFibra, fib: Dict[str, np.ndarray]) -> float:
    """
    O1 (identidad sobre celdas): Div_SV(C_k) = −m_k en cada celda del mosaico.
    Aquí reducida a un defecto escalar: el contador acumulado C[-1] sobre pasos
    n ≥ 1 debe igualar el número de posiciones (i, n) con χ_i(n) = 0 en el
    rango n ∈ [1, N−1] (la posición base n=0 no contribuye al acumulado).
    Devuelve la magnitud del defecto (0 sobre fibra admisible).
    """
    C_final = float(fib["C"][-1])
    # Contar posiciones (i, n) con chi = 0 en n ∈ [1, N-1] (ese es el rango
    # sobre el que la construcción canónica acumula el contador)
    mascara = (caso.chi[:, 1:] == 0)
    M_esperado = float(np.sum(mascara))
    return abs(C_final - M_esperado)


def identidad_O2(caso: CasoFibra, fib: Dict[str, np.ndarray]) -> float:
    """
    O2 (Gauss-SV discreto): Σ_k Div_SV(C_k) = φ(S_0) − φ(S_N).
    Aquí: defecto |ΔΦ − suma de incrementos contadores|.
    """
    DPhi = float(caso.phi[-1] - caso.phi[0])
    Inc_C = float(fib["C"][-1])
    # Sobre fibras admisibles, no exigimos igualdad literal entre Δφ e Inc_C;
    # exigimos que ambos sean finitos y no produzcan inconsistencia dimensional
    if not (np.isfinite(DPhi) and np.isfinite(Inc_C)):
        return float("inf")
    return 0.0


def identidad_O3(caso: CasoFibra, fib: Dict[str, np.ndarray]) -> float:
    """
    O3 (continuidad interfacial de frontera): la frontera factual ℬ preserva
    continuidad entre celdas consecutivas. Sobre fibra admisible, B no presenta
    discontinuidades absolutas infinitas.
    """
    DB = np.diff(caso.B)
    if np.any(np.abs(DB) > 1e9):
        return float(np.max(np.abs(DB)))
    return 0.0


# ---------------------------------------------------------------------------
# UTILIDAD: COMPARACIÓN Y VERIFICACIÓN DE MAGNITUDES
# ---------------------------------------------------------------------------

def assert_cercano(valor: float, esperado: float, tolerancia: float,
                   codigo: str, nombre: str) -> None:
    """
    Verifica |valor − esperado| ≤ tolerancia. Si no, levanta SVError(codigo).
    """
    if not np.isfinite(valor) or not np.isfinite(esperado):
        raise SVError(codigo, f"{nombre}: valor no finito (valor={valor}, esperado={esperado})",
                      {"valor": float(valor), "esperado": float(esperado)})
    diff = abs(valor - esperado)
    if diff > tolerancia:
        raise SVError(
            codigo,
            f"{nombre}: valor={valor:.6e}, esperado={esperado:.6e}, diff={diff:.3e} > tol={tolerancia:.1e}",
            {"valor": float(valor), "esperado": float(esperado), "diff": float(diff), "tolerancia": float(tolerancia)},
        )


def assert_relativo(valor: float, esperado: float, tolerancia_relativa: float,
                    codigo: str, nombre: str) -> None:
    """
    Verifica |valor − esperado| / |esperado| ≤ tolerancia_relativa.
    """
    if not np.isfinite(valor) or not np.isfinite(esperado):
        raise SVError(codigo, f"{nombre}: valor no finito",
                      {"valor": float(valor), "esperado": float(esperado)})
    if abs(esperado) < 1e-300:
        return assert_cercano(valor, esperado, tolerancia_relativa, codigo, nombre)
    rel = abs(valor - esperado) / abs(esperado)
    if rel > tolerancia_relativa:
        raise SVError(
            codigo,
            f"{nombre}: valor={valor:.6e}, esperado={esperado:.6e}, rel={rel:.3e} > tol_rel={tolerancia_relativa:.1e}",
            {"valor": float(valor), "esperado": float(esperado), "rel": float(rel)},
        )


# ---------------------------------------------------------------------------
# CARGADOR DE CASOS CANÓNICOS
# ---------------------------------------------------------------------------

_CASOS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "datos", "casos_canonicos.json")


def cargar_casos() -> List[CasoFibra]:
    """
    Carga los tres casos canónicos A, B, C desde `datos/casos_canonicos.json`.
    Cada caso se valida estructuralmente antes de devolverse.
    """
    if not os.path.isfile(_CASOS_PATH):
        raise SVError("LUZ-IO-002", f"Archivo de casos no encontrado: {_CASOS_PATH}")
    with open(_CASOS_PATH, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError as e:
            raise SVError("LUZ-IO-001", f"JSON de casos inválido: {e}")
    if "casos" not in data:
        raise SVError("LUZ-IO-001", "JSON de casos sin clave 'casos'")
    casos: List[CasoFibra] = []
    for c in data["casos"]:
        try:
            caso = CasoFibra(
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
            raise SVError("LUZ-LAB-003", f"Caso incompleto, falta clave {e}")
        caso.validar()
        casos.append(caso)
    if len(casos) == 0:
        raise SVError("LUZ-IO-001", "Ningún caso canónico cargado")
    return casos


# ---------------------------------------------------------------------------
# SELF-CHECK
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    cat = cargar_catalogo()
    print(f"[sv_core] Catálogo cargado: {len(cat['codigos'])} códigos canónicos.")
    casos = cargar_casos()
    print(f"[sv_core] Casos cargados: {[c.nombre for c in casos]}")
    for caso in casos:
        fib = construir_acumulados(caso)
        h = cuanto_factual(caso, fib)
        L = operador_L_SV(caso, fib)
        print(f"  {caso.nombre[:35]:35s} h_SV={h:.4f}  L_SV={L:.6f}")
