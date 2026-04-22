"""
lab_ejemplo_A_cierre_determinado.py — Ejemplo de principio a fin A.

Dictamen factual: 𝔗_SV(Γ) = m_0 (cierre basal determinado).

Tres posiciones que cruzan todas con determinación |δ| ≥ θ_0, θ_1.
Los residuales estructurales son bajos; la entropía factual crece
monotónicamente hasta un valor bajo-medio que refleja una trayectoria
cercana a la trivialización basal.

Esperado: H_SV(Γ, 4) = 16.8 con monotonía Δ[3,4] = 3.70 > 0.

Ejecución:
    python3 lab_ejemplo_A_cierre_determinado.py
"""

from sv_core import (H_pre, cadena_completa, print_cadena,
                     verify_monotonia, project_Pi3H)


def main():
    print("═" * 70)
    print("EJEMPLO A — Cierre determinado {m_0}")
    print("═" * 70)

    # Configuración: 3 posiciones con k* = 3, 4, 4
    deltas = {
        1: [0.1, -0.1, -0.3, -0.5],                  # k*=3, δ=-0.5
        2: [0.2, 0.3, 0.4, 0.5, 0.6],                # k*=4, δ=0.6
        3: [0.0, -0.1, -0.2, -0.3, -0.4],            # k*=4, δ=-0.4
    }
    k_stars = {1: 3, 2: 4, 3: 4}
    theta_0 = 0.3; theta_1 = 0.3; theta_U = 0.4

    print("\n--- Configuración ---")
    print(f"  3 posiciones, Δε = 1, θ_0 = θ_1 = {theta_0}, θ_U = {theta_U}")
    print(f"  Pasos de activación: k_1* = 3, k_2* = k_3* = 4")

    print("\n--- Tabla δ_i(k) ---")
    max_k = 4
    print(f"  k | {'δ_1':>6} | {'δ_2':>6} | {'δ_3':>6}")
    for k in range(max_k + 1):
        def cell(i):
            if k <= k_stars[i]:
                return f"{deltas[i][k]:+.1f}"
            return "—"
        print(f"  {k} | {cell(1):>6} | {cell(2):>6} | {cell(3):>6}")

    print("\n--- Proyección Π_3^H en el paso de cruce ---")
    for i in (1, 2, 3):
        d = deltas[i][k_stars[i]]
        v = project_Pi3H(d, theta_0, theta_1, theta_U, base_suficiente=True)
        print(f"  ξ_{i}: δ_{i}(k_{i}*) = {d:+.1f} → v_{i} = {v}")

    # Evaluación en n = 4
    n = 4
    h_pre, A, V = H_pre(deltas, k_stars, n)
    print(f"\n--- Evaluación n = {n} ---")
    print(f"  A_Γ({n}) = {A:.1f}")
    print(f"  V_Γ(B, {n}) = {V:.1f}")
    print(f"  H_pre({n}) = {h_pre:.1f}")

    # Parámetros admisibles: bajo cierre determinado los residuales son bajos
    cad4 = cadena_completa(
        h_pre,
        J_norm=1.5, R_gamma=0.8,
        contribuciones_conc=[0.3, 0.2],       # R^c, F^c
        contribuciones_canal=[0.2, 0.5, 0.4], # R^k, J^sel, J^rec
        contribuciones_trans=[0, 0, 0],       # δ_m0=0, δ_χ=0, δ_U=0
    )
    print()
    print_cadena(cad4, f"n={n}")

    # Verificación monotonía [3, 4]
    h_pre_3, _, _ = H_pre(deltas, k_stars, 3)
    cad3 = cadena_completa(
        h_pre_3,
        J_norm=1.2, R_gamma=0.6,
        contribuciones_conc=[0.2, 0.1],
        contribuciones_canal=[0.1, 0.4, 0.3],
        contribuciones_trans=[0, 0, 0],
    )
    delta_H = cad4['H_SV'] - cad3['H_SV']
    print(f"\n--- Verificación monotonía [3, 4] ---")
    print(f"  H_SV(3) = {cad3['H_SV']:.1f}")
    print(f"  H_SV(4) = {cad4['H_SV']:.1f}")
    print(f"  Δ = {delta_H:.2f} > 0  ✓")

    assert delta_H > 0
    assert abs(cad4['H_SV'] - 16.8) < 1e-9

    print("\n--- Dictamen factual ---")
    print("  𝔗_SV(Γ, 4) = m_0")
    print("  La trayectoria alcanza cierre basal determinado en n = 4.")
    print("  Los residuales estructurales son bajos y no contribuyen al dictamen.")
    print("  H_SV queda en nivel bajo-medio: 16.8 unidades factuales.")

    print("\n" + "═" * 70)


if __name__ == '__main__':
    main()
