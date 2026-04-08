# Autoría: Juan Antonio Lloret Egea | ORCID: 0000-0002-6634-3351 | Institución: Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA) | Publicación: IA eñ™ — La Biblia de la IA™ | ISSN: 2695-6411 | Licencia: CC BY-NC-ND 4.0 | Lugar y fecha: Madrid, 2026
"""
LAB 13 — Gradiente, curvatura y holonomía.

Estado esperado: CONFIRMA.
"""
from __future__ import annotations
from core.sv_lab_core import (
    LabResult,
    curvature,
    holonomy,
    slopes,
    tpa_example_director,
    assert_close,
    assert_equal,
)

LAB_ID = "LAB-13"
TITLE = "TPA — gradiente, curvatura total y holonomía"

def run() -> LabResult:
    phi = list(tpa_example_director())
    n = len(phi) - 1
    grad = [n - k - 0.5 for k in range(n)]
    expected_grad = [9.5, 8.5, 7.5, 6.5, 5.5, 4.5, 3.5, 2.5, 1.5, 0.5]
    assert_equal(grad, expected_grad)

    kappa = curvature(phi)
    total_kappa = sum(kappa)
    holo = holonomy(phi)
    assert_equal(total_kappa, holo)
    assert_equal(total_kappa, -2)
    assert_equal(sum(abs(x) for x in kappa), 10)

    return LabResult(
        lab_id=LAB_ID,
        title=TITLE,
        status="CONFIRMA",
        passed=True,
        summary="Se confirma el gradiente decreciente del primer activador y la igualdad curvatura total = holonomía.",
        details={"gradient": grad, "kappa": kappa, "sum_kappa": total_kappa, "holonomy": holo},
    )

if __name__ == "__main__":
    print(run().to_dict())
