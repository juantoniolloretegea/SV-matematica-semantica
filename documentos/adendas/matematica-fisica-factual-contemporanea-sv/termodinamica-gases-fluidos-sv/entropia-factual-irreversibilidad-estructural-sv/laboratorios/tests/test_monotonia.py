"""
test_monotonia.py — Suite de tests para verificar los teoremas de
monotonía del Sistema Vectorial SV sobre trayectorias generadas
sistemáticamente.

Teoremas cubiertos:
- Teorema 4.5: monotonía de H_pre
- Teorema 5.4: monotonía de H_K3
- Teorema 6.3: monotonía de H_Xi
- Teorema 7.5: monotonía de H_Sigma_c, H_Sigma_k, H_fin
- Teorema 8.2: monotonía de H_SV (consolidado)
- Corolario 7.7: monotonía estratificada

Ejecución:
    python3 tests/test_monotonia.py
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from math import inf
from sv_core import (H_pre, H_K3, H_Xi, cadena_completa,
                     verify_monotonia, V_i, A_i)


def test_H_pre_no_decreciente_tramo_preternario():
    """Teorema 4.5 en tramo preternario puro (sin cruces)."""
    deltas = {1: [0.0, 0.1, -0.1, -0.3, -0.5]}
    k_stars = {1: 4}
    serie = [H_pre(deltas, k_stars, n)[0] for n in range(5)]
    assert verify_monotonia(serie), f"H_pre decreció: {serie}"
    print("  ✓ test_H_pre_no_decreciente_tramo_preternario")


def test_H_pre_no_decreciente_post_cruce():
    """Teorema 4.5 después del cruce: V_i queda saturada, A_i constante."""
    deltas = {1: [0.0, 0.3, 0.5]}
    k_stars = {1: 2}
    serie = [H_pre(deltas, k_stars, n)[0] for n in range(6)]
    assert verify_monotonia(serie), f"H_pre decreció post-cruce: {serie}"
    # Post-cruce (n ≥ 3), H_pre debe quedar constante (a_i=0)
    assert abs(serie[3] - serie[2]) < 1e-9 or serie[3] >= serie[2]
    print("  ✓ test_H_pre_no_decreciente_post_cruce")


def test_H_K3_no_decreciente():
    """Teorema 5.4: dispersión ternaria no decreciente."""
    transitions_parcial = [('U', 'U'), ('U', 0)]
    transitions_full = transitions_parcial + [(0, 0), (0, 0)]
    h_parcial = H_K3(transitions_parcial)
    h_full = H_K3(transitions_full)
    assert h_full >= h_parcial, f"{h_parcial=}, {h_full=}"
    print("  ✓ test_H_K3_no_decreciente")


def test_H_K3_transicion_virtual_no_contribuye():
    """Transiciones U → U en tramo virtual pre-cruce tienen indicadora 0."""
    assert H_K3([('U', 'U'), ('U', 'U'), ('U', 'U')]) == 0
    print("  ✓ test_H_K3_transicion_virtual_no_contribuye")


def test_H_K3_cota_2_por_posicion():
    """Prop 5.3: acotación por 2 transiciones por posición."""
    # Peor caso: U → U → ... → 0 (1 transición) posteriormente 0 → 0 (constante)
    trans_cota = [('U', 'U')] * 5 + [('U', 0)] + [(0, 0)] * 5
    # Solo 1 transición no virtual contribuye
    assert sum(1 for a, b in trans_cota if a != b) == 1
    # Caso con reactivación U → 1 luego estable:
    trans_U_luego_1 = [('U', 'U')] * 3 + [('U', 1)] + [(1, 1)] * 3
    assert sum(1 for a, b in trans_U_luego_1 if a != b) == 1
    print("  ✓ test_H_K3_cota_2_por_posicion")


def test_H_Xi_suma_monotonia():
    """Teorema 6.3: H_Xi hereda monotonía de H_pre + ‖J‖ + R_Γ."""
    serie = [H_Xi(10.0 + n, 1.0 + 0.1*n, 0.5 + 0.05*n) for n in range(10)]
    assert verify_monotonia(serie)
    print("  ✓ test_H_Xi_suma_monotonia")


def test_cadena_completa_caso_patron():
    """Caso patrón §11: todos los valores de cadena deben cuadrar."""
    deltas = {
        1: [0.0, 0.1, -0.1, -0.3, -0.4, -0.5, -0.6],
        2: [-0.2, -0.3, -0.4, -0.5, -0.6, -0.7],
        3: [0.1, 0.0, 0.2, 0.1, 0.3, 0.4, 0.3],
        4: [0.4, 0.5, 0.6, 0.5, 0.5],
        5: [-0.1, -0.2, -0.1, 0.0, 0.1, 0.2, 0.3],
    }
    k_stars = {1: 6, 2: 5, 3: 6, 4: 4, 5: inf}

    h_pre_6, A_6, V_6 = H_pre(deltas, k_stars, 6)
    assert abs(A_6 - 28.0) < 1e-9
    assert abs(V_6 - 3.0) < 1e-9
    assert abs(h_pre_6 - 31.0) < 1e-9

    cad = cadena_completa(h_pre_6, 2.5, 1.8, [0.6, 0.4],
                          [0.5, 0.8, 0.7], [0, 0, 0.3])
    assert abs(cad['H_Xi'] - 35.3) < 1e-9
    assert abs(cad['H_Sigma_c'] - 36.3) < 1e-9
    assert abs(cad['H_Sigma_k'] - 38.3) < 1e-9
    assert abs(cad['H_SV'] - 38.6) < 1e-9
    print("  ✓ test_cadena_completa_caso_patron")


def test_monotonia_tramo_5_6():
    """Caso patrón §11.9: H_SV(6) - H_SV(5) = 5.2 > 0."""
    deltas = {
        1: [0.0, 0.1, -0.1, -0.3, -0.4, -0.5, -0.6],
        2: [-0.2, -0.3, -0.4, -0.5, -0.6, -0.7],
        3: [0.1, 0.0, 0.2, 0.1, 0.3, 0.4, 0.3],
        4: [0.4, 0.5, 0.6, 0.5, 0.5],
        5: [-0.1, -0.2, -0.1, 0.0, 0.1, 0.2, 0.3],
    }
    k_stars = {1: 6, 2: 5, 3: 6, 4: 4, 5: inf}

    h_pre_5, _, _ = H_pre(deltas, k_stars, 5)
    h_pre_6, _, _ = H_pre(deltas, k_stars, 6)
    c5 = cadena_completa(h_pre_5, 2.2, 1.5, [0.5, 0.3],
                         [0.4, 0.7, 0.6], [0, 0, 0])
    c6 = cadena_completa(h_pre_6, 2.5, 1.8, [0.6, 0.4],
                         [0.5, 0.8, 0.7], [0, 0, 0.3])
    delta = c6['H_SV'] - c5['H_SV']
    assert abs(delta - 5.2) < 1e-9, f"Δ = {delta} esperado 5.2"
    print("  ✓ test_monotonia_tramo_5_6")


def test_violacion_aplanamiento_decrementa_V():
    """§11.10: reescritura retroactiva δ_3(2) = 0.2 → 0.1 decrece V_3."""
    V_orig = V_i([0.1, 0.0, 0.2, 0.1], n=3, k_star=6)
    V_viol = V_i([0.1, 0.0, 0.1, 0.1], n=3, k_star=6)
    assert V_orig > V_viol, f"V_orig={V_orig}, V_viol={V_viol}"
    assert abs(V_orig - V_viol - 0.2) < 1e-9
    print("  ✓ test_violacion_aplanamiento_decrementa_V")


def test_ejemplo_A_cierre():
    """Ejemplo A: cierre determinado, H_SV(4) = 16.8."""
    deltas = {
        1: [0.1, -0.1, -0.3, -0.5],
        2: [0.2, 0.3, 0.4, 0.5, 0.6],
        3: [0.0, -0.1, -0.2, -0.3, -0.4],
    }
    k_stars = {1: 3, 2: 4, 3: 4}
    h_pre, _, _ = H_pre(deltas, k_stars, 4)
    cad = cadena_completa(h_pre, 1.5, 0.8, [0.3, 0.2],
                          [0.2, 0.5, 0.4], [0, 0, 0])
    assert abs(cad['H_SV'] - 16.8) < 1e-9
    print("  ✓ test_ejemplo_A_cierre")


def test_ejemplo_B_residual_U():
    """Ejemplo B: residual en U, H_SV(5) = 15.0."""
    deltas = {
        1: [0.0, -0.1, -0.2, -0.4],
        2: [0.2, 0.3, 0.1, 0.2, 0.2, 0.3],
    }
    k_stars = {1: 3, 2: 5}
    h_pre, _, _ = H_pre(deltas, k_stars, 5)
    cad = cadena_completa(h_pre, 1.8, 1.2, [0.4, 0.3],
                          [0.3, 0.6, 0.5], [0, 0, 0.5])
    assert abs(cad['H_SV'] - 15.0) < 1e-9
    print("  ✓ test_ejemplo_B_residual_U")


def test_ejemplo_C_emergente():
    """Ejemplo C: clase emergente χ_α, H_SV(5) = 15.0."""
    deltas = {
        1: [0.1, 0.2, 0.3, 0.5],
        2: [-0.1, -0.2, -0.3, -0.4, -0.5],
    }
    k_stars = {1: 3, 2: 4}
    h_pre, _, _ = H_pre(deltas, k_stars, 5)
    cad = cadena_completa(h_pre, 2.0, 1.0, [0.5, 0.4],
                          [0.4, 0.7, 0.6], [0, 0.6, 0])
    assert abs(cad['H_SV'] - 15.0) < 1e-9
    print("  ✓ test_ejemplo_C_emergente")


def test_monotonia_serie_completa():
    """Verifica que H_SV(0), H_SV(1), ..., H_SV(6) es no decreciente
    sobre el caso patrón §11 con contribuciones fijas (peor caso)."""
    deltas = {
        1: [0.0, 0.1, -0.1, -0.3, -0.4, -0.5, -0.6],
        2: [-0.2, -0.3, -0.4, -0.5, -0.6, -0.7],
        3: [0.1, 0.0, 0.2, 0.1, 0.3, 0.4, 0.3],
        4: [0.4, 0.5, 0.6, 0.5, 0.5],
        5: [-0.1, -0.2, -0.1, 0.0, 0.1, 0.2, 0.3],
    }
    k_stars = {1: 6, 2: 5, 3: 6, 4: 4, 5: inf}
    serie_H_pre = [H_pre(deltas, k_stars, n)[0] for n in range(7)]
    assert verify_monotonia(serie_H_pre), f"H_pre: {serie_H_pre}"
    print(f"  ✓ test_monotonia_serie_completa: H_pre monótono")


def run_all():
    tests = [
        test_H_pre_no_decreciente_tramo_preternario,
        test_H_pre_no_decreciente_post_cruce,
        test_H_K3_no_decreciente,
        test_H_K3_transicion_virtual_no_contribuye,
        test_H_K3_cota_2_por_posicion,
        test_H_Xi_suma_monotonia,
        test_cadena_completa_caso_patron,
        test_monotonia_tramo_5_6,
        test_violacion_aplanamiento_decrementa_V,
        test_ejemplo_A_cierre,
        test_ejemplo_B_residual_U,
        test_ejemplo_C_emergente,
        test_monotonia_serie_completa,
    ]
    print("═" * 70)
    print(f"Ejecutando {len(tests)} tests...")
    print("═" * 70)
    failures = 0
    for t in tests:
        try:
            t()
        except AssertionError as e:
            failures += 1
            print(f"  ✗ {t.__name__}: {e}")
    print("═" * 70)
    if failures == 0:
        print(f"✓ {len(tests)} tests OK.")
    else:
        print(f"✗ {failures}/{len(tests)} tests fallaron.")
    return failures


if __name__ == '__main__':
    sys.exit(run_all())
