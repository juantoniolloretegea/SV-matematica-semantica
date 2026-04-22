"""
lab_ejemplo_C_clase_emergente.py — Ejemplo de principio a fin C.

Dictamen factual: 𝔗_SV(Γ) = χ_α (clase emergente admitida).

Dos posiciones con cruce determinado (ambas con |δ| ≥ umbral). En el paso
n = 5 se activa una clase emergente χ_α bajo el criterio G(χ_α) = 1
del §13 de Lloret Egea (2026j), que aporta contribución transmutativa
δ_χ = 0.6 al dictamen final.

Esperado: H_SV(Γ, 5) = 15.0 con δ_χ = 0.6 capturando la emergencia.
Monotonía Δ[4,5] = 2.00 > 0.

Ejecución:
    python3 lab_ejemplo_C_clase_emergente.py
"""

from sv_core import H_pre, cadena_completa, print_cadena, project_Pi3H


def main():
    print("═" * 70)
    print("EJEMPLO C — Clase emergente {χ_α}")
    print("═" * 70)

    deltas = {
        1: [0.1, 0.2, 0.3, 0.5],                      # k*=3, δ=0.5 → v=1
        2: [-0.1, -0.2, -0.3, -0.4, -0.5],            # k*=4, δ=-0.5 → v=0
    }
    k_stars = {1: 3, 2: 4}

    print("\n--- Configuración ---")
    print("  2 posiciones con cruce determinado en pasos consecutivos.")
    print("  En n = 5 se admite activación de clase emergente χ_α")
    print("  (criterio G(χ_α) = 1, Lloret Egea 2026j §13).")
    print("  Pasos de activación: k_1* = 3, k_2* = 4")

    print("\n--- Tabla δ_i(k) ---")
    max_k = 5
    print(f"  k | {'δ_1':>6} | {'δ_2':>6}")
    for k in range(max_k + 1):
        d1 = f"{deltas[1][k]:+.1f}" if k <= k_stars[1] else "—"
        d2 = f"{deltas[2][k]:+.1f}" if k <= k_stars[2] else "—"
        print(f"  {k} | {d1:>6} | {d2:>6}")
    print("  5 | activación de clase emergente χ_α (G(χ_α) = 1)")

    print("\n--- Proyección Π_3^H en el paso de cruce ---")
    for i in (1, 2):
        d = deltas[i][k_stars[i]]
        v = project_Pi3H(d, base_suficiente=True)
        print(f"  ξ_{i}: δ_{i}(k_{i}*) = {d:+.1f} → v_{i} = {v}")

    # Evaluación en n = 5 (con clase emergente)
    n = 5
    h_pre, A, V = H_pre(deltas, k_stars, n)
    print(f"\n--- Evaluación n = {n} (con clase emergente admitida) ---")
    print(f"  A_Γ({n}) = {A:.1f}")
    print(f"  V_Γ(B, {n}) = {V:.1f}")
    print(f"  H_pre({n}) = {h_pre:.1f}")

    # Contribución δ_χ = 0.6 captura la emergencia
    cad5 = cadena_completa(
        h_pre,
        J_norm=2.0, R_gamma=1.0,
        contribuciones_conc=[0.5, 0.4],
        contribuciones_canal=[0.4, 0.7, 0.6],
        contribuciones_trans=[0, 0.6, 0],     # δ_χ_α = 0.6
    )
    print()
    print_cadena(cad5, f"n={n}")

    # Verificación monotonía [4, 5]
    # En n = 4 la clase emergente aún NO se ha activado: δ_χ = 0
    h_pre_4, _, _ = H_pre(deltas, k_stars, 4)
    cad4 = cadena_completa(
        h_pre_4,
        J_norm=1.7, R_gamma=0.9,
        contribuciones_conc=[0.4, 0.3],
        contribuciones_canal=[0.3, 0.6, 0.5],
        contribuciones_trans=[0, 0, 0],     # δ_χ_α aún no activa
    )
    delta_H = cad5['H_SV'] - cad4['H_SV']
    print(f"\n--- Verificación monotonía [4, 5] ---")
    print(f"  H_SV(4) = {cad4['H_SV']:.1f}   (sin clase emergente)")
    print(f"  H_SV(5) = {cad5['H_SV']:.1f}   (con δ_χ_α = 0.6)")
    print(f"  Δ = {delta_H:.2f} > 0  ✓")

    assert delta_H > 0
    assert abs(cad5['H_SV'] - 15.0) < 1e-9

    print("\n--- Dictamen factual ---")
    print("  𝔗_SV(Γ, 5) = χ_α")
    print("  En n = 5 se admite activación de clase emergente bajo G(χ_α) = 1.")
    print("  La contribución transmutativa δ_χ_α = 0.6 acumula en H_SV,")
    print("  compatible con el régimen de transmutación factual de 𝔠^adm_trans.")
    print("  H_SV = 15.0 unidades factuales.")

    print("\n" + "═" * 70)


if __name__ == '__main__':
    main()
