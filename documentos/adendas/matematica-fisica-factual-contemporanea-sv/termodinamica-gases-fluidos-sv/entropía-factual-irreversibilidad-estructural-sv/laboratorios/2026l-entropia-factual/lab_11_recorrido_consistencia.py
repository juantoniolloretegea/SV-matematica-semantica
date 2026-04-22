"""
lab_11_recorrido_consistencia.py — Recorrido de consistencia del §11
del documento 2026l: caso patrón sobre SV(3,9) con 5 posiciones
preternarias, tramo [0, 6], verificación de monotonía [5, 6].

Números esperados (§11):
    A_Γ(6) = 28      V_Γ(B, 6) = 3.0     H_pre(6) = 31.0
    H_Ξ(6) = 35.3    H_Σc(6) = 36.3     H_Σk(6) = 38.3    H_SV(6) = 38.6
    A_Γ(5) = 24.5    V_Γ(B, 5) = 2.7     H_pre(5) = 27.2
    H_Ξ(5) = 30.9    H_Σc(5) = 31.7     H_Σk(5) = 33.4    H_SV(5) = 33.4
    Monotonía: H_SV(6) - H_SV(5) = 5.2 > 0

Ejecución:
    python3 lab_11_recorrido_consistencia.py
"""

from math import inf
from sv_core import (H_pre, H_K3, cadena_completa, print_cadena,
                     verify_monotonia, project_Pi3H, RHO)


def caso_patron():
    """Devuelve la configuración completa del caso patrón §11."""
    deltas = {
        1: [0.0, 0.1, -0.1, -0.3, -0.4, -0.5, -0.6],   # k*=6
        2: [-0.2, -0.3, -0.4, -0.5, -0.6, -0.7],        # k*=5
        3: [0.1, 0.0, 0.2, 0.1, 0.3, 0.4, 0.3],         # k*=6
        4: [0.4, 0.5, 0.6, 0.5, 0.5],                   # k*=4
        5: [-0.1, -0.2, -0.1, 0.0, 0.1, 0.2, 0.3],      # no cruza
    }
    k_stars = {1: 6, 2: 5, 3: 6, 4: 4, 5: inf}
    return deltas, k_stars


def contribuciones(n):
    """Parámetros admisibles declarados en §11.7-§11.8 y §11.9."""
    if n == 6:
        return dict(J_norm=2.5, R_gamma=1.8,
                    conc=[0.6, 0.4],
                    canal=[0.5, 0.8, 0.7],
                    trans=[0, 0, 0.3])  # [δ_m0, δ_χ, δ_U]
    elif n == 5:
        return dict(J_norm=2.2, R_gamma=1.5,
                    conc=[0.5, 0.3],
                    canal=[0.4, 0.7, 0.6],
                    trans=[0, 0, 0])


def evaluar_caso(n, deltas, k_stars):
    h_pre, A, V = H_pre(deltas, k_stars, n)
    c = contribuciones(n)
    cadena = cadena_completa(h_pre, c['J_norm'], c['R_gamma'],
                             c['conc'], c['canal'], c['trans'])
    cadena['A_Gamma'] = A
    cadena['V_Gamma'] = V
    return cadena


def main():
    print("═" * 70)
    print("LAB §11 — Recorrido de consistencia sobre SV(3,9), 5 posiciones")
    print("═" * 70)

    deltas, k_stars = caso_patron()

    print("\nPasos de activación:")
    for i, k in k_stars.items():
        k_str = "∞" if k == inf else str(k)
        print(f"  k_{i}* = {k_str}")

    print("\nProyección Π_3^H en el paso de cruce (con θ_U = 0.4):")
    # ξ_4 en k=4 con δ=0.5 → v_4=1
    # ξ_2 en k=5 con δ=-0.7 → v_2=0
    # ξ_1 en k=6 con δ=-0.6 → v_1=0
    # ξ_3 en k=6 con δ=0.3, |δ|<0.4 → v_3=U
    print(f"  ξ_1: δ={deltas[1][6]:+.1f} → v_1 = {project_Pi3H(deltas[1][6], theta_U=0.4)}")
    print(f"  ξ_2: δ={deltas[2][5]:+.1f} → v_2 = {project_Pi3H(deltas[2][5], theta_U=0.4)}")
    print(f"  ξ_3: δ={deltas[3][6]:+.1f} → v_3 = {project_Pi3H(deltas[3][6], theta_U=0.4, base_suficiente=False)}")
    print(f"  ξ_4: δ={deltas[4][4]:+.1f} → v_4 = {project_Pi3H(deltas[4][4], theta_U=0.4)}")

    # --- Evaluación en n = 5 y n = 6 ---
    print("\n" + "─" * 70)
    print("Evaluación n = 5")
    print("─" * 70)
    r5 = evaluar_caso(5, deltas, k_stars)
    print(f"  A_Γ(5)    = {r5['A_Gamma']:.1f}   (esperado: 24.5)")
    print(f"  V_Γ(B, 5) = {r5['V_Gamma']:.1f}   (esperado: 2.7)")
    print()
    print_cadena(r5, "n=5")

    print("\n" + "─" * 70)
    print("Evaluación n = 6")
    print("─" * 70)
    r6 = evaluar_caso(6, deltas, k_stars)
    print(f"  A_Γ(6)    = {r6['A_Gamma']:.1f}   (esperado: 28.0)")
    print(f"  V_Γ(B, 6) = {r6['V_Gamma']:.1f}   (esperado: 3.0)")
    print()
    print_cadena(r6, "n=6")

    # --- Verificación de monotonía ---
    print("\n" + "─" * 70)
    print("Verificación Teorema 8.2 (monotonía)")
    print("─" * 70)
    delta_H = r6['H_SV'] - r5['H_SV']
    print(f"  H_SV(6) - H_SV(5) = {r6['H_SV']:.1f} - {r5['H_SV']:.1f} = {delta_H:.2f}")
    assert delta_H > 0, "Violación de monotonía"
    print(f"  ✓ Δ = {delta_H:.2f} > 0 — Teorema 8.2 verificado sobre [5, 6].")

    # --- Assertions contra valores del documento ---
    esperados_6 = {'A_Gamma': 28.0, 'V_Gamma': 3.0,
                   'H_pre': 31.0, 'H_Xi': 35.3, 'H_Sigma_c': 36.3,
                   'H_Sigma_k': 38.3, 'H_SV': 38.6}
    esperados_5 = {'A_Gamma': 24.5, 'V_Gamma': 2.7,
                   'H_pre': 27.2, 'H_Xi': 30.9, 'H_Sigma_c': 31.7,
                   'H_Sigma_k': 33.4, 'H_SV': 33.4}

    print("\n" + "─" * 70)
    print("Assertions contra valores declarados en el documento")
    print("─" * 70)
    for key, expected in esperados_6.items():
        actual = r6[key]
        status = "✓" if abs(actual - expected) < 1e-9 else "✗"
        print(f"  {status} {key}(6) = {actual:.1f} (esperado: {expected})")
        assert abs(actual - expected) < 1e-9
    for key, expected in esperados_5.items():
        actual = r5[key]
        status = "✓" if abs(actual - expected) < 1e-9 else "✗"
        print(f"  {status} {key}(5) = {actual:.1f} (esperado: {expected})")
        assert abs(actual - expected) < 1e-9

    print("\n" + "═" * 70)
    print("Todos los valores del caso patrón §11 verificados.")
    print("═" * 70)


if __name__ == '__main__':
    main()
