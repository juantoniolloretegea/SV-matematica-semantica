# Autoría: Juan Antonio Lloret Egea | ORCID: 0000-0002-6634-3351 | Institución: Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA) | Publicación: IA eñ™ — La Biblia de la IA™ | ISSN: 2695-6411 | Licencia: CC BY-NC-ND 4.0 | Lugar y fecha: Madrid, 2026
"""
LAB 11 — Refutación de la isoperimetría lineal universal.

Estado esperado: CONFIRMA la refutación.
"""
from __future__ import annotations
from core.sv_lab_core import (
    LabResult,
    affine_reference_area,
    affine_deviation,
    check_no_collinearity,
    in_domain,
    slopes,
    tpa_isoperimetric_counterexample,
    trapezoid_area,
    assert_equal,
)

LAB_ID = "LAB-11"
TITLE = "TPA — refutación de la cota lineal universal y referencia afín"

def run() -> LabResult:
    phi = list(tpa_isoperimetric_counterexample())
    m = slopes(phi)
    A = trapezoid_area(phi)
    A_af = affine_reference_area(phi[0], phi[-1], len(phi) - 1)
    delta_af = affine_deviation(phi)

    assert_equal(sum(m), phi[-1] - phi[0])
    assert_equal(check_no_collinearity(phi), True)
    assert_equal(in_domain(phi, 0, 9), True)
    assert_equal(A < A_af, True)

    return LabResult(
        lab_id=LAB_ID,
        title=TITLE,
        status="CONFIRMA",
        passed=True,
        summary="Se confirma la refutación de la cota lineal universal; la referencia afín queda como funcional comparativo, no como mínimo general.",
        details={
            "phi": phi,
            "M": m,
            "A": A,
            "A_af": A_af,
            "delta_af": delta_af,
        },
    )

if __name__ == "__main__":
    print(run().to_dict())
