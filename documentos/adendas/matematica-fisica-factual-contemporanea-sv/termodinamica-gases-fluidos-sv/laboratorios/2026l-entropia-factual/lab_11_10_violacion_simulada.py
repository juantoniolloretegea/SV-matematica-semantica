"""
lab_11_10_violacion_simulada.py — Contraste con violación simulada (§11.10).

Demuestra que la reescritura retroactiva del sesgo polar declarado
δ_3(2) = 0.2 → 0.1 sin aportar nueva base compatible produce decremento
estricto de V_3(δ, 3): V_3 = 0.4 original → V_3_viol = 0.2.

Consecuencia: H_pre decrece en 0.2 unidades, violación directa del Teorema 4.5.

Ejecución:
    python3 lab_11_10_violacion_simulada.py
"""

from sv_core import V_i


def main():
    print("═" * 70)
    print("LAB §11.10 — Violación simulada por reescritura retroactiva")
    print("═" * 70)

    # Trayectoria original: δ_3 declarado en §11.2
    delta_3_orig = [0.1, 0.0, 0.2, 0.1]   # k = 0, 1, 2, 3
    V_3_orig = V_i(delta_3_orig, n=3, k_star=6)
    print(f"\nTrayectoria original: δ_3 = {delta_3_orig}")
    print(f"V_3(δ, 3) = |0.0-0.1| + |0.2-0.0| + |0.1-0.2|")
    print(f"         = 0.1 + 0.2 + 0.1 = {V_3_orig:.1f}")
    assert abs(V_3_orig - 0.4) < 1e-9

    # Violación: δ_3(2) cambiado de 0.2 a 0.1, aplanando el zigzag
    delta_3_viol = [0.1, 0.0, 0.1, 0.1]
    V_3_viol = V_i(delta_3_viol, n=3, k_star=6)
    print(f"\nViolación: δ_3(2) = 0.2 → 0.1 (aplanamiento retroactivo)")
    print(f"δ_3_viol = {delta_3_viol}")
    print(f"V_3_viol(δ, 3) = |0.0-0.1| + |0.1-0.0| + |0.1-0.1|")
    print(f"              = 0.1 + 0.1 + 0.0 = {V_3_viol:.1f}")
    assert abs(V_3_viol - 0.2) < 1e-9

    delta_H = V_3_orig - V_3_viol
    print(f"\nDecremento de V_3: {V_3_orig:.1f} - {V_3_viol:.1f} = {delta_H:.1f}")
    print(f"Por la Definición 4.2, H_pre(Γ, 3) decrece en {delta_H:.1f} unidades.")
    print(f"Por el Teorema 8.2 y transporte estratificado, H_SV también decrece.")

    assert V_3_viol < V_3_orig, "La violación no produce decremento"
    print(f"\n✓ Violación confirmada: V_3_viol({V_3_viol:.1f}) < V_3({V_3_orig:.1f})")
    print(f"✓ Violación directa del Teorema 4.5 (monotonía preternaria).")
    print(f"✓ Reescritura retroactiva excluida por Proposición 4.7.")

    print("\n" + "═" * 70)
    print("Consecuencia operativa:")
    print("  La disciplina append-only, junto con la honestidad coordenada,")
    print("  excluye toda operación que modifique sesgos polares declarados")
    print("  sin aportar nueva base compatible. El aparato entrópico es")
    print("  estructuralmente protegido contra reescritura retroactiva.")
    print("═" * 70)


if __name__ == '__main__':
    main()
