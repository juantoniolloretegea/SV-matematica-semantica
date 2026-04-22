"""
sv_core.py — Primitivas del Sistema Vectorial SV para laboratorios de
entropía factual (2026l).

Implementa las definiciones formales del documento:
- Variación total preternaria del sesgo polar (Def 4.1)
- Acumulación factual de apertura (Def 4.2)
- Dispersión factual preternaria H_pre (Def 4.2)
- Dispersión ternaria inducida H_K3 (Def 5.2)
- Dispersión canónica factual H_Xi (Def 6.1)
- Dispersiones H_Sigma_c, H_Sigma_k, H_fin (Defs 7.2-7.4)
- Entropía factual H_SV (Def 8.1)

Todas las primitivas son Python estándar puro. Sin dependencias externas.
No se introduce probabilidad, estadística fundante, tiempo soberano
ni coordenadas externas: la magnitud se deriva exclusivamente de
acumulaciones append-only y variaciones totales del sesgo polar.

Autor: Juan Antonio Lloret Egea — ITVIA — 2026
Licencia: CC BY-NC-ND 4.0
"""

from math import inf
from typing import Sequence


# ═══════════════════════════════════════════════════════════════════════
# Primitivas estrato preternario (§4)
# ═══════════════════════════════════════════════════════════════════════

def V_i(deltas: Sequence[float], n: int, k_star: float) -> float:
    """Variación total preternaria del sesgo polar de la posición i.

    V_i(δ, n) = Σ_{k=0}^{min(n, k_i*) - 1} |δ_i(k+1) - δ_i(k)|  (Def 4.1)

    Parámetros
    ----------
    deltas : secuencia [δ_i(0), δ_i(1), ..., δ_i(k_i*)]
        Valores declarados del sesgo polar hasta el paso de activación inclusive.
    n : int
        Paso del cálculo.
    k_star : int o inf
        Paso de activación k_i*(Γ). Si la posición no cruza en Γ, usar inf.

    Retorna
    -------
    float
        Variación total acumulada. Suma vacía devuelve 0.
    """
    if k_star == inf:
        k_max = n
    else:
        k_max = min(n, int(k_star))
    s = 0.0
    for k in range(k_max):
        if k + 1 < len(deltas):
            s += abs(deltas[k + 1] - deltas[k])
    return s


def A_i(n: int, k_star: float, delta_eps: float = 1.0) -> float:
    """Acumulación factual de apertura de la posición i.

    A_i(n) = Σ_{k=0}^{n-1} (1/2)(a_i(k) + a_i(k+1)) · Δε_k

    con a_i(k) = 1 si k ≤ k_i*, 0 si k > k_i* (Def 4.2, convenio §5.1).

    Parámetros
    ----------
    n : int
    k_star : int o inf
    delta_eps : float
        Incremento del índice factual. Por defecto 1 (caso didáctico).

    Retorna
    -------
    float
    """
    s = 0.0
    for k in range(n):
        a_k = 1 if k <= k_star else 0
        a_k1 = 1 if k + 1 <= k_star else 0
        s += 0.5 * (a_k + a_k1) * delta_eps
    return s


def H_pre(deltas_by_pos: dict, k_stars: dict, n: int,
          delta_eps: float = 1.0) -> tuple:
    """Dispersión factual preternaria (Def 4.2).

    H_pre(Γ, n) = Σ_i [A_i(n) + V_i(δ, n)]

    Retorna
    -------
    (H_pre, A_Γ, V_Γ) : tupla
        H_pre total, acumulación agregada y variación agregada.
    """
    A_total = 0.0
    V_total = 0.0
    for i in deltas_by_pos:
        A_total += A_i(n, k_stars[i], delta_eps)
        V_total += V_i(deltas_by_pos[i], n, k_stars[i])
    return A_total + V_total, A_total, V_total


# ═══════════════════════════════════════════════════════════════════════
# Codificación ternaria visible (§5.2, Maxwell §4.1)
# ═══════════════════════════════════════════════════════════════════════

RHO = {0: 1, 1: 2, 'U': 3}


def H_K3(transitions: Sequence[tuple]) -> int:
    """Dispersión ternaria inducida (Def 5.2).

    H_K3(Γ, n) = Σ_i Σ_k 𝟙[v_i(k) ≠ v_i(k+1)] · ρ(v_i(k+1))

    Con convenio operativo v_i(k) = U virtual para k < k_i*.

    Parámetros
    ----------
    transitions : lista de (v_k, v_k1)
        Cada par representa (valor previo, valor siguiente) en una transición.

    Retorna
    -------
    int
        Suma de contribuciones ρ en las transiciones no nulas.
    """
    total = 0
    for v_prev, v_next in transitions:
        if v_prev != v_next:
            total += RHO[v_next]
    return total


# ═══════════════════════════════════════════════════════════════════════
# Dispersión canónica y estratos posteriores (§6, §7)
# ═══════════════════════════════════════════════════════════════════════

def H_Xi(h_pre: float, J_norm: float, R_gamma: float) -> float:
    """Dispersión canónica factual (Def 6.1, Prop 6.2).

    H_Ξ(Γ, n) = H_pre(Γ, n) + ‖J_Γ(n)‖_1 + R_Γ(n)
    """
    return h_pre + J_norm + R_gamma


def H_Sigma_c(h_xi: float, contributions_conc: Sequence[float]) -> float:
    """Dispersión en concentración (Def 7.2).

    H_Σ_c(Γ, n) = H_Ξ(Γ, n) + Σ_𝒞∈𝔠^adm_Σ_conc 𝒞(Γ, n)
    """
    return h_xi + sum(contributions_conc)


def H_Sigma_k(h_sc: float, contributions_canal: Sequence[float]) -> float:
    """Dispersión en canalización (Def 7.3)."""
    return h_sc + sum(contributions_canal)


def H_fin(h_sk: float, contributions_trans: Sequence[float]) -> float:
    """Dispersión final (Def 7.4)."""
    return h_sk + sum(contributions_trans)


# ═══════════════════════════════════════════════════════════════════════
# Entropía factual (Def 8.1)
# ═══════════════════════════════════════════════════════════════════════

def H_SV(h_fin: float) -> float:
    """Entropía factual del Sistema Vectorial SV.

    H_SV(Γ, n) := H_fin(Γ, n)  (Def 8.1)
    """
    return h_fin


# ═══════════════════════════════════════════════════════════════════════
# Proyección Π_3^H y paso de activación
# ═══════════════════════════════════════════════════════════════════════

def project_Pi3H(delta_final: float, theta_0: float = 0.3,
                 theta_1: float = 0.3, theta_U: float = 0.4,
                 base_suficiente: bool = True):
    """Proyección ternaria Π_3^H en el paso de cruce (§5.1, 2026j §5.2).

    Parámetros
    ----------
    delta_final : δ_i(k_i*), el último sesgo polar preternario.
    theta_0, theta_1 : umbrales de clausura determinada.
    theta_U : umbral de insuficiencia de base para |δ| < θ_U.
    base_suficiente : si False, la clausura es a U aunque |δ| ≥ θ_U.

    Retorna
    -------
    int o str : 0, 1, o 'U'
    """
    if not base_suficiente:
        return 'U'
    if delta_final >= theta_1:
        return 1
    if delta_final <= -theta_0:
        return 0
    if abs(delta_final) < theta_U:
        return 'U'
    # Caso borde: |δ| entre θ_U y θ_0/θ_1 con base suficiente
    return 0 if delta_final < 0 else 1


# ═══════════════════════════════════════════════════════════════════════
# Verificación de monotonía (Teorema 8.2)
# ═══════════════════════════════════════════════════════════════════════

def verify_monotonia(H_serie: Sequence[float], tol: float = 1e-9) -> bool:
    """Teorema 8.2: H_SV(Γ, n+1) >= H_SV(Γ, n) para toda n."""
    for i in range(len(H_serie) - 1):
        if H_serie[i+1] < H_serie[i] - tol:
            return False
    return True


def cadena_completa(h_pre, J_norm, R_gamma,
                    contribuciones_conc, contribuciones_canal,
                    contribuciones_trans):
    """Aplica la cadena entropy completa desde H_pre hasta H_SV.

    Retorna dict con todos los estratos para inspección.
    """
    h_xi = H_Xi(h_pre, J_norm, R_gamma)
    h_sc = H_Sigma_c(h_xi, contribuciones_conc)
    h_sk = H_Sigma_k(h_sc, contribuciones_canal)
    h_fin_val = H_fin(h_sk, contribuciones_trans)
    return {
        'H_pre': h_pre,
        'H_Xi': h_xi,
        'H_Sigma_c': h_sc,
        'H_Sigma_k': h_sk,
        'H_fin': h_fin_val,
        'H_SV': H_SV(h_fin_val),
    }


# ═══════════════════════════════════════════════════════════════════════
# Utilidad de impresión
# ═══════════════════════════════════════════════════════════════════════

def print_cadena(cadena: dict, label: str = "") -> None:
    """Imprime la cadena entrópica de forma legible."""
    prefix = f"[{label}] " if label else ""
    print(f"{prefix}H_pre     = {cadena['H_pre']:>7.2f}")
    print(f"{prefix}H_Xi      = {cadena['H_Xi']:>7.2f}")
    print(f"{prefix}H_Sigma_c = {cadena['H_Sigma_c']:>7.2f}")
    print(f"{prefix}H_Sigma_k = {cadena['H_Sigma_k']:>7.2f}")
    print(f"{prefix}H_fin     = {cadena['H_fin']:>7.2f}")
    print(f"{prefix}H_SV      = {cadena['H_SV']:>7.2f}")


# ═══════════════════════════════════════════════════════════════════════
if __name__ == '__main__':
    # Smoke test: caso patrón del §11 del documento (5 posiciones, n=6)
    print("═" * 60)
    print("Smoke test: caso patrón §11 (5 posiciones, n=6)")
    print("═" * 60)

    deltas_pat = {
        1: [0.0, 0.1, -0.1, -0.3, -0.4, -0.5, -0.6],
        2: [-0.2, -0.3, -0.4, -0.5, -0.6, -0.7],
        3: [0.1, 0.0, 0.2, 0.1, 0.3, 0.4, 0.3],
        4: [0.4, 0.5, 0.6, 0.5, 0.5],
        5: [-0.1, -0.2, -0.1, 0.0, 0.1, 0.2, 0.3],
    }
    k_stars_pat = {1: 6, 2: 5, 3: 6, 4: 4, 5: inf}

    h_pre_6, A_g_6, V_g_6 = H_pre(deltas_pat, k_stars_pat, 6)
    print(f"\nA_Γ(6) = {A_g_6:.1f}   (esperado: 28)")
    print(f"V_Γ(B, 6) = {V_g_6:.1f}   (esperado: 3.0)")
    print(f"H_pre(Γ, 6) = {h_pre_6:.1f}   (esperado: 31.0)")

    cadena = cadena_completa(
        h_pre_6, J_norm=2.5, R_gamma=1.8,
        contribuciones_conc=[0.6, 0.4],
        contribuciones_canal=[0.5, 0.8, 0.7],
        contribuciones_trans=[0, 0, 0.3],
    )
    print()
    print_cadena(cadena, "n=6")
    print(f"\nH_SV(Γ, 6) esperado: 38.6")
    assert abs(cadena['H_SV'] - 38.6) < 1e-9, "H_SV(6) no coincide"
    print("✓ smoke test OK")
