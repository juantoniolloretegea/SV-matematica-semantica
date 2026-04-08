# Autoría: Juan Antonio Lloret Egea | ORCID: 0000-0002-6634-3351 | Institución: Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA) | Publicación: IA eñ™ — La Biblia de la IA™ | ISSN: 2695-6411 | Licencia: CC BY-NC-ND 4.0 | Lugar y fecha: Madrid, 2026
"""
LAB 04 — Cota condicionada de coste del CS.

Estado esperado: CONFIRMA.
Audita:
- validez de CS-3 bajo la hipótesis φ_k >= φ_0,
- igualdad sólo en meseta,
- caso negativo fuera de la hipótesis.
"""
from __future__ import annotations
from core.sv_lab_core import (
    LabResult,
    cs_conditioned_lower_bound,
    mfc_reference_cycle,
    slopes,
    trapezoid_area,
    assert_equal,
)

LAB_ID = "LAB-04"
TITLE = "Ciclo de Suceso — cota condicionada y caso fuera de hipótesis"

def run() -> LabResult:
    plateau = mfc_reference_cycle(phi0=3, n=9)
    applies_p, area_p, bound_p = cs_conditioned_lower_bound(plateau)
    assert_equal(applies_p, True)
    assert_equal(area_p, bound_p)

    cycle_positive = [3, 4, 5, 4, 3]
    applies_c, area_c, bound_c = cs_conditioned_lower_bound(cycle_positive)
    assert_equal(applies_c, True)
    assert_equal(area_c >= bound_c, True)

    cycle_negative = [3, 2, 0, 1, 0, 3]
    applies_n, area_n, bound_n = cs_conditioned_lower_bound(cycle_negative)
    assert_equal(applies_n, False)
    # fuera de hipótesis no se impone la cota
    counterexample_outside = area_n < bound_n

    return LabResult(
        lab_id=LAB_ID,
        title=TITLE,
        status="CONFIRMA",
        passed=True,
        summary="La cota se confirma sólo bajo la hipótesis explicitada; fuera de ella no procede afirmarla.",
        details={
            "plateau": {"phi": plateau, "area": area_p, "bound": bound_p},
            "cycle_positive": {"phi": cycle_positive, "area": area_c, "bound": bound_c},
            "cycle_negative": {"phi": cycle_negative, "area": area_n, "bound": bound_n, "outside_hypothesis_refutes_universal_reading": counterexample_outside},
        },
    )

if __name__ == "__main__":
    print(run().to_dict())
