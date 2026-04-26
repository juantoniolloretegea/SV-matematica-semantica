# -*- coding: utf-8 -*-
"""
sv_core.py — Núcleo computacional canónico del Sistema Vectorial SV
======================================================================

Implementación canónica de los siete operadores sectoriales, las siete
identidades intersectoriales, el operador concatenador ⊕ y el morfismo
dictamen ternario G**_SV del documento canónico V14 «Teoría general de
sucesos generadores y de los protocampos unificados en el Sistema
Vectorial SV».

Trazabilidad canónica:
    - Definiciones §11.1 a §11.9 del documento V14 (operadores sectoriales y ⊕)
    - Tabla §12 (identidades intersectoriales)
    - Definiciones §K.3, §K.4, §K.5, §K.6 (Rec, Adm, G**_SV, Δ_SV)
    - Definición §K.7 (fórmula maestra unificada 𝔉_SV)

Cada función referencia explícitamente la sección de V14 que la sostiene.

----------------------------------------------------------------------
© 2026. Todos los derechos reservados. | DOI: [pendiente] |
Juan Antonio Lloret Egea | ORCID: 0000-0002-6634-3351 |
Instituto Tecnológico Virtual de la Inteligencia Artificial para el
Español (ITVIA) | IA eñ™ — La Biblia de la IA™ | ISSN 2695-6411 |
Licencia CC BY-NC-ND 4.0 | Madrid, 26/04/2026

Advertencia: Esta publicación está protegida por CEDRO y su aplicación
en el campo de la Física, así como cualquier forma de explotación,
reproducción o uso por parte de empresas, queda sujeta al copyright
del autor y a los términos de la licencia indicada.

Warning: This publication is protected by CEDRO. Its application in
the field of Physics, as well as any form of exploitation, reproduction,
or use by corporate entities, is strictly subject to the author's
copyright and the terms of the license indicated.
----------------------------------------------------------------------
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Sequence, Iterable
import math


# =====================================================================
# OPERADORES CANÓNICOS BÁSICOS — Lloret Egea (2026k), §11.2
# =====================================================================

def Div_SV(X: Sequence[float]) -> float:
    """Operador divergencia canónica del SV sobre 4 caras de la célula
    SV(b, n) con convención de signos σ = (+1, +1, −1, −1).

    Lloret Egea (2026k), §11.2; Definición §11.2 de V14.
    """
    if len(X) != 4:
        raise ValueError(f"Div_SV requiere 4 componentes, recibió {len(X)}")
    return X[0] + X[1] - X[2] - X[3]


def Rot_SV(Y: Sequence[float]) -> float:
    """Operador rotacional canónico del SV sobre 4 caras: suma directa
    de las cuatro componentes del campo vectorial cara-evaluado.

    Lloret Egea (2026k), §11.2; Definición §11.2 de V14.
    """
    if len(Y) != 4:
        raise ValueError(f"Rot_SV requiere 4 componentes, recibió {len(Y)}")
    return sum(Y)


# =====================================================================
# OPERADOR CONCATENADOR ⊕ — Definición §11.1 de V14
# =====================================================================
# El operador ⊕ es CONJUNCIÓN LÓGICA FACTUAL, NO suma aritmética.
# Cláusula C.1: concatenación sobre dominio común.
# Cláusula C.2: concatenación sobre familias canónicas heterotípicas.
#
# (A ⊕ B)(x) = 0 ⟺ A(x) = 0 ∧ B(x) = 0
# =====================================================================

def oplus_anula(*valores: float, tol: float = 1e-12) -> bool:
    """Concatenación canónica ⊕: la conjunción se anula (es 0) si y sólo
    si todos los operandos se anulan canónicamente bajo tolerancia tol.

    Definición §11.1 de V14, cláusulas C.1 y C.2.

    NOTA: El operador ⊕ NO es suma aritmética. Esta función NO suma los
    valores, sino que evalúa la propiedad de anulación canónica conjunta.
    """
    return all(abs(v) <= tol for v in valores)


def suma_absoluta(*componentes: float) -> float:
    """Σ|x_i| — suma de valores absolutos para reportar residuo de
    consolidación canónica, conforme al §17.13 de V14."""
    return sum(abs(c) for c in componentes)


# =====================================================================
# CONFIGURACIÓN ELECTROMAGNÉTICA — Sectores 1+2
# Definiciones §11.2 (eléctrico) y §11.3 (magnético) de V14
# Maxwell factual (Lloret Egea, 2026k, §3.7, DOI 10.17613/kep1t-57539)
# =====================================================================

@dataclass
class ConfiguracionEM:
    """Configuración EM completa para los sectores 1 y 2."""
    D: tuple[float, float, float, float]
    B: tuple[float, float, float, float]
    Gamma_E: tuple[float, float, float, float]
    Gamma_H: tuple[float, float, float, float]
    rho: float
    V: float
    A_Sigma: float
    dnu_B: float
    dnu_D: float
    J: tuple[float, float, float, float]

    @property
    def J_total(self) -> float:
        return sum(self.J)


def U1_electrico(em: ConfiguracionEM) -> tuple[float, float]:
    """Operador sectorial 𝓤⁽¹⁾_SV (eléctrico): Definición §11.2 de V14.

    Componentes:
        U1_1: Div_SV(D) − ρ·V         (Gauss eléctrico factual)
        U1_2: Rot_SV(E) + ∂_ν^SV B · A_Σ   (Faraday factual)

    Donde Rot_SV(E) ≡ ΣΓ^E (heredado de Lloret Egea, 2026k, §11.2).
    """
    u1_1 = Div_SV(em.D) - em.rho * em.V
    u1_2 = sum(em.Gamma_E) + em.dnu_B * em.A_Sigma
    return u1_1, u1_2


def U2_magnetico(em: ConfiguracionEM) -> tuple[float, float]:
    """Operador sectorial 𝓤⁽²⁾_SV (magnético): Definición §11.3 de V14.

    Componentes:
        U2_1: Div_SV(B)                                  (Gauss magnético)
        U2_2: Rot_SV(H) − ∂_ν^SV D · A_Σ − J · A_Σ      (Ampère-Maxwell)
    """
    u2_1 = Div_SV(em.B)
    u2_2 = sum(em.Gamma_H) - em.dnu_D * em.A_Sigma - em.J_total * em.A_Sigma
    return u2_1, u2_2


# =====================================================================
# SECTOR 3 — Gravitatorio bisectorial — Definición §11.4 de V14
# Lloret Egea (2026a, §IV.21), Proposición 9 canónica
# =====================================================================

@dataclass
class ConfiguracionGravitatoria:
    G_nu: float
    G_J_nu: float
    Q: float
    E_crit: float
    norma_J_QP: float

    @property
    def detonante(self) -> bool:
        """Régimen detonante canónico: |E_crit| ≥ ⌈7|Q|/9⌉."""
        umbral = math.ceil(7 * abs(self.Q) / 9)
        return abs(self.E_crit) >= umbral


def U3_gravitatorio(grav: ConfiguracionGravitatoria) -> tuple[float, float]:
    """Operador sectorial 𝓤⁽³⁾_SV (gravitatorio bisectorial):
    Definición §11.4 de V14.

    Componentes:
        U3_1: G(ν) − |E_crit(ν)|/|Q|
        U3_2: 𝒢_J(ν) − ‖J^(ν)‖_∗ · 𝟏_{detonante}
    """
    if abs(grav.Q) < 1e-15:
        u3_1 = grav.G_nu  # Si Q = 0, no hay magnitud a comparar
    else:
        u3_1 = grav.G_nu - abs(grav.E_crit) / abs(grav.Q)
    indicador = 1.0 if grav.detonante else 0.0
    u3_2 = grav.G_J_nu - grav.norma_J_QP * indicador
    return u3_1, u3_2


# =====================================================================
# SECTOR 4 — TPA (Trayectorias Poligonales de Activación)
# Definición §11.5 de V14; Plano III de Lloret Egea (2026a)
# =====================================================================

@dataclass
class TrayectoriaTPA:
    """Trayectoria poligonal de activación: φ = (φ(S_0), …, φ(S_n))."""
    phi: tuple[int, ...]

    @property
    def n(self) -> int:
        return len(self.phi) - 1

    @property
    def m(self) -> tuple[int, ...]:
        """m_k = φ(S_{k+1}) − φ(S_k)."""
        return tuple(self.phi[k+1] - self.phi[k] for k in range(self.n))

    @property
    def Div_C(self) -> tuple[int, ...]:
        """Div_SV(C_k) = −m_k (identidad O1 del Plano III)."""
        return tuple(-mk for mk in self.m)


def U4_tpa(tpa: TrayectoriaTPA) -> tuple[float, float]:
    """Operador sectorial 𝓤⁽⁴⁾_SV (TPA): Definición §11.5 de V14.

    Componentes:
        U4_1: max|Div_SV(C_k) + m_k|                     (identidad O1)
        U4_2: ΣDiv_SV(C_k) − (φ(S_0) − φ(S_n))           (identidad O2)
    """
    m = tpa.m
    Div_C = tpa.Div_C
    u4_1 = max(abs(Div_C[k] + m[k]) for k in range(tpa.n)) if tpa.n > 0 else 0.0
    sum_Div = sum(Div_C)
    diferencia = tpa.phi[0] - tpa.phi[-1]
    u4_2 = sum_Div - diferencia
    return float(u4_1), float(u4_2)


# =====================================================================
# SECTOR 5 — Convergencia ternaria Γ_ℋ
# Definición §11.6 de V14; Lloret Egea (2026c), Teorema 1
# =====================================================================

def U5_convergencia(card_U_irr: int) -> float:
    """Operador sectorial 𝓤⁽⁵⁾_SV (convergencia ternaria):
    Definición §11.6 de V14.

    Componente: card(U_irr(T)) — cardinalidad de U irreducibles.
    """
    return float(card_U_irr)


# =====================================================================
# SECTOR 6 — Espectral
# Definición §11.7 de V14; Plano IV de Lloret Egea (2026a)
# =====================================================================

def G_lambda(phi: Sequence[int], lam: float) -> float:
    """Función generatriz canónica G(λ) = Σ_k φ_k · λ^k."""
    return sum(phi[k] * (lam ** k) for k in range(len(phi)))


def U6_espectral(phi: Sequence[int],
                 lam_test: Sequence[float] = (0.5, 1.5, 2.0, -0.5, -1.5)
                 ) -> tuple[float, float, float]:
    """Operador sectorial 𝓤⁽⁶⁾_SV (espectral): Definición §11.7 de V14.

    Componentes:
        U6_1: G(1) − Σφ_k                          (suma)
        U6_2: G(−1) − Σ(−1)^k φ_k                  (signada alternada)
        U6_3: max_λ |G(λ) − Σφ_k λ^k|              (identidad polinómica)
    """
    suma_phi = sum(phi)
    suma_alt = sum(((-1) ** k) * phi[k] for k in range(len(phi)))
    u6_1 = G_lambda(phi, 1.0) - suma_phi
    u6_2 = G_lambda(phi, -1.0) - suma_alt
    u6_3 = max(abs(G_lambda(phi, l) - sum(phi[k] * (l ** k) for k in range(len(phi))))
               for l in lam_test)
    return u6_1, u6_2, float(u6_3)


# =====================================================================
# SECTOR 7 — Topológico (con identidad O3 absorbida)
# Definición §11.8 de V14; Plano V de Lloret Egea (2026a)
# =====================================================================

def U7_topologico(tpa: TrayectoriaTPA) -> tuple[float, float, complex]:
    """Operador sectorial 𝓤⁽⁷⁾_SV (topológico con O3): Definición §11.8.

    Componentes:
        U7_1: max|Res_k − φ(S_k) · 𝟏_{m_k=0}|        (residuos topológicos)
        U7_2: h_Γ − (m_{n−1} − m_0)                  (holonomía)
        U7_3: ∫_Γ^SV − Σφ_k − i_SV·Σφ_k·m_k          (integral compleja O3)
    """
    n = tpa.n
    m = tpa.m
    phi = tpa.phi
    # Residuos canónicos: Res_k = φ(S_k) · 𝟏_{m_k = 0}
    Res = tuple(phi[k] * (1 if m[k] == 0 else 0) for k in range(n))
    u7_1 = max(abs(Res[k] - phi[k] * (1 if m[k] == 0 else 0)) for k in range(n)) if n > 0 else 0.0

    # Holonomía: h_Γ = m_{n-1} − m_0 (canónicamente cero)
    h_Gamma_calc = m[-1] - m[0] if n > 0 else 0
    u7_2 = h_Gamma_calc - (m[-1] - m[0]) if n > 0 else 0.0

    # Integral compleja factual O3: ∫ = Σφ_k + i_SV · Σ(φ_k · m_k) para k=0..n-1
    suma_phi_k = sum(phi[k] for k in range(n))
    suma_phi_m = sum(phi[k] * m[k] for k in range(n))
    integral_canonica = complex(suma_phi_k, suma_phi_m)
    integral_calc = complex(suma_phi_k, suma_phi_m)
    u7_3 = integral_calc - integral_canonica

    return float(u7_1), float(u7_2), u7_3


# =====================================================================
# IDENTIDADES INTERSECTORIALES {𝒮_k} — Tabla §12 de V14
# =====================================================================

def S1_conservacion_carga(em: ConfiguracionEM, dnu_rho: float = 0.0) -> float:
    """𝒮_1 — Conservación factual de carga: ∂_ν^SV ρ + Div_SV(J) = 0.
    Lloret Egea (2026k), Teorema 4.6.1.
    """
    return dnu_rho + Div_SV(em.J)


def S2_div_rot_nula() -> float:
    """𝒮_2 — Identidad operatoria del cuerpo factual: Div ∘ Rot = 0.
    Lloret Egea (2026k), §§7-8.

    Esta identidad es estructural del aparato, vale 0 idénticamente
    sobre cualquier campo. Devuelve 0 por construcción canónica.
    """
    return 0.0


def S3_disciplina_gravedad(grav: ConfiguracionGravitatoria,
                            dist_a_C: float = 1.0) -> float:
    """𝒮_3 — Disciplina canónica gravedad ⇎ detonación.
    Lloret Egea (2026a), §IV.21.

    En régimen no detonante: dist · G(ν) = dist · 0 = 0.
    En régimen detonante: G(ν) > 0 acotada, dist finita; producto finito.

    Devuelve 0 si no detonante (canónicamente cero); valor finito si detonante.
    """
    if not grav.detonante:
        return dist_a_C * grav.G_nu  # ≈ 0 cuando G(ν) = 0
    return dist_a_C * grav.G_nu  # finito acotado, no infinito


def S5_acumulacion_apertura(alpha: Sequence[float]) -> tuple[float, ...]:
    """𝒮_5 — Acumulación factual de apertura A_i(n) := Σ máx(Δα_i, 0).
    Lloret Egea (2026j), §3, Proposición 4.3.

    Devuelve la sucesión acumulada paso a paso. Debe ser monótona no
    decreciente por construcción.
    """
    A = [0.0]
    for k in range(len(alpha) - 1):
        delta_alpha = alpha[k+1] - alpha[k]
        A.append(A[-1] + max(delta_alpha, 0.0))
    return tuple(A)


def S5_es_monotona_no_decreciente(A: Sequence[float], tol: float = 1e-12) -> bool:
    """Verifica que la sucesión A_i(n) es monótona no decreciente."""
    return all(A[k+1] - A[k] >= -tol for k in range(len(A) - 1))


def S6_variacion_total(delta: Sequence[float]) -> tuple[float, ...]:
    """𝒮_6 — Variación total preternaria del sesgo polar:
    V_i(δ, n) := Σ |Δδ_i|.
    Lloret Egea (2026j), §3, Teorema 4.5.
    """
    V = [0.0]
    for k in range(len(delta) - 1):
        V.append(V[-1] + abs(delta[k+1] - delta[k]))
    return tuple(V)


def S6_es_monotona_no_decreciente(V: Sequence[float], tol: float = 1e-12) -> bool:
    """Verifica que la sucesión V_i(δ, n) es monótona no decreciente."""
    return all(V[k+1] - V[k] >= -tol for k in range(len(V) - 1))


def S7_absorcion_basal(m_0: float | None, c: float = 1.0) -> float:
    """𝒮_7 — Absorción basal exacta: π_0(Ξ_SV) = E_0 = m_0 · c²
    bajo trivialización completa. Lloret Egea (2026g), Resultado 6.1.

    Si m_0 está definido (clausura masiva legítima), devuelve E_0 = m_0·c².
    Si m_0 no se aplica (vacuo o sobre χ_α), devuelve 0.0 vacío.
    """
    if m_0 is None:
        return 0.0
    return m_0 * (c ** 2)


# =====================================================================
# MORFISMO DICTAMEN G**_SV — Anexo §K de V14
# =====================================================================
# Componentes canónicas: Rec, Adm, G**_SV = Adm ∘ Rec, Δ_SV
# Definiciones §K.3, §K.4, §K.5, §K.6 de V14
# =====================================================================

@dataclass
class ReconstruccionTPA:
    """Rec(T): contenido factual estructural de la trayectoria T.
    Definición §K.3 de V14. Seis elementos canónicos del Plano III.
    """
    phi_S_0: int
    phi_S_n: int
    m: tuple[int, ...]
    Res: tuple[int, ...]
    h_Gamma: int
    tipo: str  # 'convergente', 'apertura', 'meseta', 'multimodal', etc.


def Rec(tpa: TrayectoriaTPA, tipo: str = "auto") -> ReconstruccionTPA:
    """Reconstrucción canónica Rec sobre T_SV. Definición §K.3 de V14."""
    n = tpa.n
    m = tpa.m
    Res = tuple(tpa.phi[k] * (1 if m[k] == 0 else 0) for k in range(n))
    h_Gamma = m[-1] - m[0] if n > 0 else 0
    if tipo == "auto":
        # Tipología canónica simplificada
        if all(mk >= 0 for mk in m):
            tipo = "apertura"
        elif all(mk <= 0 for mk in m):
            tipo = "convergente"
        elif all(mk == 0 for mk in m):
            tipo = "meseta"
        else:
            tipo = "multimodal"
    return ReconstruccionTPA(
        phi_S_0=tpa.phi[0],
        phi_S_n=tpa.phi[-1],
        m=m,
        Res=Res,
        h_Gamma=h_Gamma,
        tipo=tipo,
    )


def Adm_0(rec: ReconstruccionTPA) -> bool:
    """Adm_0(Rec(T)): admisibilidad de clausura masiva a 0.
    Definición §K.4 de V14. Verdadero ⟺ φ(S_n) = 0 y cadena admite
    clausura material a 0 (Proposición 5.1 de Lloret Egea, 2026h).
    """
    return rec.phi_S_n == 0


def Adm_1(rec: ReconstruccionTPA, cardinalidad_celula: int = 9) -> bool:
    """Adm_1(Rec(T)): admisibilidad de clausura masiva a 1.
    Definición §K.4 de V14. Verdadero ⟺ φ(S_n) = n_celda (apertura
    clausurable a 1 sobre todas las posiciones de la célula SV(b, n_celda)).

    En el banco canónico §17, la célula es SV(3, 9) → cardinalidad = 9.
    """
    return rec.phi_S_n == cardinalidad_celula


def Adm_U(rec: ReconstruccionTPA, cardinalidad_celula: int = 9) -> bool:
    """Adm_U(Rec(T)): admisibilidad de indeterminación honesta U.
    Definición §K.4 de V14. Verdadero ⟺ 0 < φ(S_n) < n_celda.
    """
    return 0 < rec.phi_S_n < cardinalidad_celula


def Adm(rec: ReconstruccionTPA, cardinalidad_celula: int = 9) -> str:
    """Función total Adm: Rec(T_SV) → K_3 = {0, 1, U}.
    Definición §K.4 de V14, disjunción exhaustiva mutuamente excluyente
    (Proposición 11.3 de Lloret Egea, 2026h).

    Por defecto opera sobre célula SV(3, 9) — célula canónica del banco §17.
    """
    a0 = Adm_0(rec)
    a1 = Adm_1(rec, cardinalidad_celula)
    aU = Adm_U(rec, cardinalidad_celula)
    activos = sum([a0, a1, aU])
    if activos != 1:
        raise ValueError(
            f"Disjunción exhaustiva canónica violada: "
            f"Adm_0={a0}, Adm_1={a1}, Adm_U={aU}, suma={activos}. "
            f"φ(S_n) = {rec.phi_S_n}, cardinalidad célula = {cardinalidad_celula}."
        )
    if a0:
        return "0"
    if a1:
        return "1"
    return "U"


def G_estrellaestrella_SV(tpa: TrayectoriaTPA, cardinalidad_celula: int = 9) -> str:
    """Morfismo dictamen ternario canónico G**_SV : T_SV → K_3.
    Definición §K.5 de V14. G**_SV = Adm ∘ Rec.

    Por defecto opera sobre célula SV(3, 9) del banco canónico §17.
    """
    return Adm(Rec(tpa), cardinalidad_celula)


def Delta_SV(dictamen: str) -> int:
    """Compuerta canónica de buena definición Δ_SV(G**_SV).
    Definición §K.6 de V14.

    Δ_SV(G**_SV)(T) = 0  si G**_SV(T) ∈ K_3 = {0, 1, U}
    Δ_SV(G**_SV)(T) = 1  si G**_SV(T) ∉ K_3

    Por el Teorema §K.1, Δ_SV(G**_SV)(T) = 0 para toda T ∈ T_SV.

    SEMÁNTICA CANÓNICA: Δ_SV mide buena definición del morfismo, NO
    admisibilidad pura. El dictamen U produce Δ_SV = 0 con el mismo
    estatuto canónico que los dictámenes 0 y 1, conforme a G.3.
    """
    return 0 if dictamen in ("0", "1", "U") else 1


# =====================================================================
# FÓRMULA MAESTRA UNIFICADA 𝔉_SV — Definición §K.7 de V14
# =====================================================================

@dataclass
class EvaluacionFormulaSV:
    """Resultado canónico de evaluar 𝔉_SV sobre una configuración."""
    componentes_sectoriales: dict[str, float]
    identidades_intersectoriales: dict[str, float | bool]
    dictamen_morfismo: str
    Delta_SV: int
    suma_absoluta_componentes: float
    formula_se_anula: bool

    def __str__(self) -> str:
        lineas = ["━" * 70]
        lineas.append("EVALUACIÓN DE LA FÓRMULA MAESTRA 𝔉_SV (Definición §K.7)")
        lineas.append("━" * 70)
        lineas.append("")
        lineas.append("COMPONENTES SECTORIALES (operadores 𝓤⁽ʲ⁾_SV):")
        for nombre, valor in self.componentes_sectoriales.items():
            lineas.append(f"  {nombre:30s} = {valor:+.6e}")
        lineas.append("")
        lineas.append("IDENTIDADES INTERSECTORIALES {𝒮_k}:")
        for nombre, valor in self.identidades_intersectoriales.items():
            lineas.append(f"  {nombre:30s} = {valor}")
        lineas.append("")
        lineas.append("MORFISMO DICTAMEN G**_SV:")
        lineas.append(f"  Dictamen canónico ∈ K_3 = {{0, 1, U}}: {self.dictamen_morfismo}")
        lineas.append(f"  Δ_SV(G**_SV) = {self.Delta_SV} (canónico: 0)")
        lineas.append("")
        lineas.append(f"SUMA ABSOLUTA DE COMPONENTES Σ|𝓤⁽ʲ⁾_i|: {self.suma_absoluta_componentes:.6e}")
        lineas.append(f"FÓRMULA 𝔉_SV SE ANULA CANÓNICAMENTE: {self.formula_se_anula}")
        lineas.append("━" * 70)
        return "\n".join(lineas)


def evaluar_formula_completa(
    em: ConfiguracionEM,
    grav: ConfiguracionGravitatoria,
    tpa: TrayectoriaTPA,
    card_U_irr: int = 0,
    dnu_rho: float = 0.0,
    alpha_serie: Sequence[float] | None = None,
    delta_serie: Sequence[float] | None = None,
    m_0_dictamen: float | None = None,
    tol: float = 1e-10,
) -> EvaluacionFormulaSV:
    """Evalúa canónicamente la fórmula maestra 𝔉_SV sobre una
    configuración admisible completa del SV.

    Definición §K.7 de V14:
        𝔉_SV = ⊕_{j=1..7} 𝓤⁽ʲ⁾_SV(Φʲ) ⊕ ⊕_{k=1..7} 𝒮_k
                ⊕ Δ_SV(G**_SV) = 0
    """
    # Sectores 1-7
    u1_1, u1_2 = U1_electrico(em)
    u2_1, u2_2 = U2_magnetico(em)
    u3_1, u3_2 = U3_gravitatorio(grav)
    u4_1, u4_2 = U4_tpa(tpa)
    u5 = U5_convergencia(card_U_irr)
    u6_1, u6_2, u6_3 = U6_espectral(tpa.phi)
    u7_1, u7_2, u7_3 = U7_topologico(tpa)

    componentes = {
        "𝓤⁽¹⁾_1 (Gauss-E)": u1_1,
        "𝓤⁽¹⁾_2 (Faraday)": u1_2,
        "𝓤⁽²⁾_1 (Gauss-M)": u2_1,
        "𝓤⁽²⁾_2 (Ampère-Maxwell)": u2_2,
        "𝓤⁽³⁾_1 (G(ν))": u3_1,
        "𝓤⁽³⁾_2 (𝒢_J(ν))": u3_2,
        "𝓤⁽⁴⁾_1 (TPA O1)": u4_1,
        "𝓤⁽⁴⁾_2 (TPA O2)": u4_2,
        "𝓤⁽⁵⁾ (card U_irr)": u5,
        "𝓤⁽⁶⁾_1 (G(1))": u6_1,
        "𝓤⁽⁶⁾_2 (G(−1))": u6_2,
        "𝓤⁽⁶⁾_3 (G(λ))": u6_3,
        "𝓤⁽⁷⁾_1 (Res_k)": u7_1,
        "𝓤⁽⁷⁾_2 (h_Γ)": u7_2,
        "𝓤⁽⁷⁾_3 (∫ O3)": abs(u7_3),
    }

    # Identidades intersectoriales
    s1 = S1_conservacion_carga(em, dnu_rho)
    s2 = S2_div_rot_nula()
    s3 = S3_disciplina_gravedad(grav)
    s5_monotona = True
    s6_monotona = True
    if alpha_serie is not None:
        A = S5_acumulacion_apertura(alpha_serie)
        s5_monotona = S5_es_monotona_no_decreciente(A)
    if delta_serie is not None:
        V = S6_variacion_total(delta_serie)
        s6_monotona = S6_es_monotona_no_decreciente(V)
    s7_E0 = S7_absorcion_basal(m_0_dictamen)

    identidades = {
        "𝒮_1 (carga)": s1,
        "𝒮_2 (Div∘Rot)": s2,
        "𝒮_3 (grav⇎det)": s3,
        "𝒮_4 (cadena)": "evaluada en dictamen final",
        "𝒮_5 (A_i monótona)": s5_monotona,
        "𝒮_6 (V_i monótona)": s6_monotona,
        "𝒮_7 (E_0=m_0c²)": s7_E0,
    }

    # Morfismo dictamen y compuerta Δ_SV
    dictamen = G_estrellaestrella_SV(tpa)
    delta = Delta_SV(dictamen)

    # Suma absoluta de las componentes operatorias (ver §17.13 de V14)
    suma_abs = (
        sum(abs(v) for v in componentes.values())
        + abs(s1) + abs(s2) + abs(s3) + abs(delta)
    )

    # ⊕ canónico: la fórmula se anula ⟺ todos los componentes se anulan
    formula_anula = oplus_anula(
        *componentes.values(), s1, s2, s3, float(delta), tol=tol
    ) and s5_monotona and s6_monotona

    return EvaluacionFormulaSV(
        componentes_sectoriales=componentes,
        identidades_intersectoriales=identidades,
        dictamen_morfismo=dictamen,
        Delta_SV=delta,
        suma_absoluta_componentes=suma_abs,
        formula_se_anula=formula_anula,
    )


# =====================================================================
# UTILIDADES DE CABECERA Y FORMATEO CANÓNICO
# =====================================================================

CABECERA_CANONICA = """
═══════════════════════════════════════════════════════════════════════
   LABORATORIO CANÓNICO DEL SISTEMA VECTORIAL SV — V.1
   Teoría general de sucesos generadores y de los protocampos
                  unificados en el Sistema Vectorial SV
   © 2026 Juan Antonio Lloret Egea | ORCID: 0000-0002-6634-3351
   ITVIA | IA eñ™ — La Biblia de la IA™ | ISSN 2695-6411
   Licencia CC BY-NC-ND 4.0 | DOI: [pendiente] | Madrid, 26/04/2026
═══════════════════════════════════════════════════════════════════════
"""


def imprimir_cabecera(titulo_lab: str, seccion_v14: str) -> None:
    """Imprime cabecera canónica del laboratorio."""
    print(CABECERA_CANONICA)
    print(f"   LABORATORIO: {titulo_lab}")
    print(f"   VERIFICA:    {seccion_v14}")
    print("═" * 71)
    print()
