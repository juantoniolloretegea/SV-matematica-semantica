# Autoría: Juan Antonio Lloret Egea | ORCID: 0000-0002-6634-3351 | Institución: Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA) | Publicación: IA eñ™ — La Biblia de la IA™ | ISSN: 2695-6411 | Licencia: CC BY-NC-ND 4.0 | Lugar y fecha: Madrid, 2026
"""
LAB 07 — Ejemplo director TPA.

Estado esperado: CONFIRMA.
Audita los cálculos numéricos principales del ejemplo director del documento.
"""
from __future__ import annotations
from core.sv_lab_core import (
    LabResult,
    area_partition,
    balance,
    complex_integral_sv,
    curvature,
    descriptor_quadruple,
    divergence,
    generating_function_value,
    holonomy,
    local_extrema,
    mean_trapezoidal,
    slopes,
    tpa_example_director,
    trapezoid_area,
    left_area,
    assert_close,
    assert_equal,
)

LAB_ID = "LAB-07"
TITLE = "TPA — ejemplo director numérico"

def run() -> LabResult:
    phi = list(tpa_example_director())
    m = slopes(phi)
    kappa = curvature(phi)
    A = trapezoid_area(phi)
    A_left = left_area(phi)
    parts = area_partition(phi, [0, 4, 5, 10])
    quad = descriptor_quadruple(phi)
    div = divergence(phi)
    gint = complex_integral_sv(phi)
    extrema = local_extrema(phi)

    assert_equal(sum(phi), 57)
    assert_equal(sum(m), 1)
    assert_close(A, 55.5)
    assert_close(A_left, 55.0)
    assert_equal(parts, [22.0, 9.0, 24.5])
    assert_equal(max(phi), 9)
    assert_equal(quad, (55.5, 1, 9, 15.0))
    assert_equal(div, [-2, -3, -2, -1, 0, 1, 2, 3, 1, 0])
    assert_equal(balance(phi), -1)
    assert_equal(generating_function_value(phi, 1), 57)
    assert_equal(generating_function_value(phi, -1), 1)
    assert_equal(gint, complex(55, -15))
    assert_close(mean_trapezoidal(phi), 5.55)
    assert_equal(holonomy(phi), -2)
    assert_equal(kappa, [1, -1, -1, -1, -1, -1, -1, 2, 1])
    assert_equal(extrema["maxima"], [4, 5])
    assert_equal(extrema["minima"], [9])

    return LabResult(
        lab_id=LAB_ID,
        title=TITLE,
        status="CONFIRMA",
        passed=True,
        summary="El ejemplo director del documento queda reproducido sin discrepancias numéricas.",
        details={
            "phi": phi,
            "M": m,
            "kappa": kappa,
            "A_trap": A,
            "A_left": A_left,
            "parts": parts,
            "quadruple": quad,
            "div": div,
            "balance": balance(phi),
            "G(1)": generating_function_value(phi, 1).real,
            "G(-1)": generating_function_value(phi, -1).real,
            "integral_compleja": {"real": gint.real, "imag": gint.imag},
            "extrema": extrema,
        },
    )

if __name__ == "__main__":
    print(run().to_dict())
