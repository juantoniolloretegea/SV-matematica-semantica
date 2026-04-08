# Autoría: Juan Antonio Lloret Egea | ORCID: 0000-0002-6634-3351 | Institución: Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA) | Publicación: IA eñ™ — La Biblia de la IA™ | ISSN: 2695-6411 | Licencia: CC BY-NC-ND 4.0 | Lugar y fecha: Madrid, 2026
"""
LAB 08 — Identidades emergentes O1, O2 y O3.

Estado esperado: CONFIRMA.
"""
from __future__ import annotations
from core.sv_lab_core import (
    LabResult,
    balance,
    complex_integral_sv,
    divergence,
    slopes,
    tpa_example_director,
    assert_equal,
)

LAB_ID = "LAB-08"
TITLE = "TPA — identidades emergentes O1, O2 y O3"

def run() -> LabResult:
    phi = list(tpa_example_director())
    m = slopes(phi)
    div = divergence(phi)

    # O1
    assert_equal(div, [-x for x in m])

    # O2
    lhs = sum(div)
    rhs = phi[0] - phi[-1]
    rhs2 = -sum(m)
    assert_equal(lhs, rhs)
    assert_equal(lhs, rhs2)

    # O3
    cint = complex_integral_sv(phi)
    assert_equal(cint, complex(55, -15))

    return LabResult(
        lab_id=LAB_ID,
        title=TITLE,
        status="CONFIRMA",
        passed=True,
        summary="Las identidades O1, O2 y O3 se verifican exactamente sobre el ejemplo director.",
        details={
            "M": m,
            "Div": div,
            "O2": {"sum_div": lhs, "phi0_minus_phin": rhs, "minus_sum_m": rhs2},
            "O3": {"integral": {"real": cint.real, "imag": cint.imag}},
        },
    )

if __name__ == "__main__":
    print(run().to_dict())
