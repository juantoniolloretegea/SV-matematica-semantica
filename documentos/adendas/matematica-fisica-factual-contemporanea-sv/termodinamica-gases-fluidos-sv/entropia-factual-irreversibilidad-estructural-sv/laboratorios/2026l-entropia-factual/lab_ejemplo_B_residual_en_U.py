"""
lab_ejemplo_B_residual_en_U.py — Ejemplo de principio a fin B.

Dictamen factual: 𝔗_SV(Γ) = U (residual estructural persistente).

Dos posiciones. ξ_1 cruza con cierre determinado (δ = -0.4, |δ| ≥ θ_0 = 0.3);
ξ_2 cruza con |δ| = 0.3 < θ_U = 0.4 y base insuficiente, produciendo
clausura a U.

Esperado: H_SV(Γ, 5) = 15.0 con δ_U = 0.5 contribuyendo al dictamen.
Monotonía Δ[3,5] = 4.70 > 0.

Ejecución:
    python3 lab_ejemplo_B_residual_en_U.py
"""

from sv_core import H_pre, cadena_completa, print_cadena, project_Pi3H


def main():
    print("═" * 70)
    print("EJEMPLO B — Residual en U {U}")
    print("═" * 70)

    deltas = {
        1: [0.0, -0.1, -0.2, -0.4],                   # k*=3, δ=-0.4 → v=0
        2: [0.2, 0.3, 0.1, 0.2, 0.2, 0.3],            # k*=5, δ=0.3, |δ|<θ_U
    }
    k_stars = {1: 3, 2: 5}
    theta_U = 0.4

    print("\n--- Configuración ---")
    print(f"  2 posiciones, Δε = 1, θ_U = {theta_U}")
    print(f"  Pasos de activación: k_1* = 3, k_2* = 5")

    print("\n--- Tabla δ_i(k) ---")
    max_k = 5
    print(f"  k | {'δ_1':>6} | {'δ_2':>6}")
    for k in range(max_k + 1):
        d1 = f"{deltas[1][k]:+.1f}" if k <= k_stars[1] else "—"
        d2 = f"{deltas[2][k]:+.1f}" if k <= k_stars[2] else "—"
        print(f"  {k} | {d1:>6} | {d2:>6}")

    print("\n--- Proyección Π_3^H en el paso de cruce ---")
    d1_final = deltas[1][k_stars[1]]
    v1 = project_Pi3H(d1_final, theta_U=theta_U, base_suficiente=True)
    print(f"  ξ_1: δ_1(3) = {d1_final:+.1f}, base suficiente → v_1 = {v1}")

    d2_final = deltas[2][k_stars[2]]
    # ξ_2 tiene |δ| = 0.3 < θ_U = 0.4 → proyección a U por insuficiencia
    v2 = project_Pi3H(d2_final, theta_U=theta_U, base_suficiente=False)
    print(f"  ξ_2: δ_2(5) = {d2_final:+.1f}, |δ| = {abs(d2_final):.1f} < θ_U = {theta_U}")
    print(f"       base insuficiente → v_2 = {v2}")

    n = 5
    h_pre, A, V = H_pre(deltas, k_stars, n)
    print(f"\n--- Evaluación n = {n} ---")
    print(f"  A_Γ({n}) = {A:.1f}")
    print(f"  V_Γ(B, {n}) = {V:.1f}")
    print(f"  H_pre({n}) = {h_pre:.1f}")

    # Parámetros admisibles: el cierre en U genera residual estructural mayor
    cad5 = cadena_completa(
        h_pre,
        J_norm=1.8, R_gamma=1.2,
        contribuciones_conc=[0.4, 0.3],
        contribuciones_canal=[0.3, 0.6, 0.5],
        contribuciones_trans=[0, 0, 0.5],     # δ_U = 0.5 contribuye
    )
    print()
    print_cadena(cad5, f"n={n}")

    # Verificación monotonía [3, 5]
    h_pre_3, _, _ = H_pre(deltas, k_stars, 3)
    cad3 = cadena_completa(
        h_pre_3,
        J_norm=1.3, R_gamma=0.8,
        contribuciones_conc=[0.2, 0.1],
        contribuciones_canal=[0.2, 0.5, 0.4],
        contribuciones_trans=[0, 0, 0],
    )
    delta_H = cad5['H_SV'] - cad3['H_SV']
    print(f"\n--- Verificación monotonía [3, 5] ---")
    print(f"  H_SV(3) = {cad3['H_SV']:.1f}")
    print(f"  H_SV(5) = {cad5['H_SV']:.1f}")
    print(f"  Δ = {delta_H:.2f} > 0  ✓")

    assert delta_H > 0
    assert abs(cad5['H_SV'] - 15.0) < 1e-9

    print("\n--- Dictamen factual ---")
    print("  𝔗_SV(Γ, 5) = U")
    print("  La posición ξ_2 clausura a U por insuficiencia de base compatible.")
    print("  δ_U(Γ, 5) = 0.5 contribuye al dictamen final.")
    print("  H_SV registra residual estructural persistente: 15.0 unidades.")

    print("\n" + "═" * 70)


if __name__ == '__main__':
    main()
