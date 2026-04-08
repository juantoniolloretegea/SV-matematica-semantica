# Autoría: Juan Antonio Lloret Egea | ORCID: 0000-0002-6634-3351 | Institución: Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA) | Publicación: IA eñ™ — La Biblia de la IA™ | ISSN: 2695-6411 | Licencia: CC BY-NC-ND 4.0 | Lugar y fecha: Madrid, 2026
"""
LAB 06 — Alcance no universal del "mínimo" del medidor factual.

Estado esperado: REFUTA una lectura demasiado fuerte:
"la meseta canónica es mínimo universal sobre SV(3,9)".

Método:
- comparar la meseta de referencia con un ciclo válido de igual frontera y menor área.
"""
from __future__ import annotations
from core.sv_lab_core import (
    LabResult,
    check_no_collinearity,
    in_domain,
    mfc_lower_than_plateau_counterexample,
    mfc_reference_cycle,
    trapezoid_area,
    assert_equal,
)

LAB_ID = "LAB-06"
TITLE = "Medidor factual de ciclo — refutación del mínimo universal"

def run() -> LabResult:
    plateau = mfc_reference_cycle(phi0=3, n=9)
    counter = mfc_lower_than_plateau_counterexample(phi0=3, n=9)
    area_plateau = trapezoid_area(plateau)
    area_counter = trapezoid_area(counter)

    assert_equal(check_no_collinearity(counter), True)
    assert_equal(in_domain(counter, 0, 9), True)
    assert_equal(counter[0] == counter[-1], True)
    assert_equal(area_counter < area_plateau, True)

    return LabResult(
        lab_id=LAB_ID,
        title=TITLE,
        status="REFUTA",
        passed=True,
        summary="Se refuta una lectura universal del mínimo: existe un ciclo válido con menor área que la meseta de referencia.",
        details={
            "plateau": {"phi": plateau, "A": area_plateau},
            "counterexample": {"phi": counter, "A": area_counter},
        },
    )

if __name__ == "__main__":
    print(run().to_dict())
