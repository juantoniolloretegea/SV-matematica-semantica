"""
lab_04_4_verificacion_preternaria.py — Verificación numérica del §4.4
del documento 2026l: H_pre(Γ, 3) = 10,2 sobre configuración de 3 posiciones
con tabla de sesgos polares declarada.

Ejecución:
    python3 lab_04_4_verificacion_preternaria.py
"""

from sv_core import V_i, A_i, H_pre


def main():
    print("═" * 70)
    print("LAB §4.4 — Verificación visible de H_pre sobre 3 posiciones")
    print("═" * 70)

    # Tabla de sesgos polares declarada en §4.4
    deltas = {
        1: [0.0,  0.0, -0.4, -0.8],
        2: [-0.6, -0.6, -0.7, -0.6],
        3: [0.4,  0.3,  0.3,  0.2],
    }
    # Ninguna posición cruza en el tramo [0, 3]: k_i* >= 3
    # Para simplicidad usamos k_star = 3 (frontera: contribuyen los 3 pasos)
    k_stars = {1: 3, 2: 3, 3: 3}

    print("\nTabla δ_i(k):")
    print(f"  k | δ_1   | δ_2   | δ_3")
    for k in range(4):
        print(f"  {k} | {deltas[1][k]:+.1f}  | {deltas[2][k]:+.1f}  | {deltas[3][k]:+.1f}")

    print("\nCálculo V_i(δ, 3):")
    V_tot = 0.0
    for i in (1, 2, 3):
        v = V_i(deltas[i], 3, k_stars[i])
        V_tot += v
        print(f"  V_{i}(δ, 3) = {v:.1f}")
    print(f"  V_Γ(B, 3) = {V_tot:.1f}")

    print("\nCálculo A_i(3) con a_i(k) = 1 uniforme en el tramo preternario:")
    A_tot = 0.0
    for i in (1, 2, 3):
        a = A_i(3, k_stars[i])
        A_tot += a
        print(f"  A_{i}(3) = {a:.1f}")
    print(f"  A_Γ(3) = {A_tot:.1f}")

    h, _, _ = H_pre(deltas, k_stars, 3)
    print(f"\nH_pre(Γ, 3) = A_Γ(3) + V_Γ(B, 3) = {A_tot:.1f} + {V_tot:.1f} = {h:.1f}")

    assert abs(h - 10.2) < 1e-9, f"H_pre(3) = {h}, esperado 10.2"
    print("\n✓ Verificación OK: H_pre(Γ, 3) = 10.2 coincide con §4.4 del documento.")

    # Contraste sin oscilación
    deltas_sin_osc = {1: [0.0]*4, 2: [-0.6]*4, 3: [0.4]*4}
    h_sin, _, V_sin = H_pre(deltas_sin_osc, k_stars, 3)
    print(f"\nContraste sin oscilación: V_Γ = {V_sin:.1f}, H_pre = {h_sin:.1f}")
    print(f"Diferencia por oscilación: {h - h_sin:.1f} unidades factuales.")
    assert abs(h_sin - 9.0) < 1e-9


if __name__ == '__main__':
    main()
