# Autoría: Juan Antonio Lloret Egea | ORCID: 0000-0002-6634-3351 | Institución: Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA) | Publicación: IA eñ™ — La Biblia de la IA™ | ISSN: 2695-6411 | Licencia: CC BY-NC-ND 4.0 | Lugar y fecha: Madrid, 2026
"""
LAB 10 — TVMTPA y extremos locales.

Estado esperado: CONFIRMA.
"""
from __future__ import annotations
from core.sv_lab_core import (
    LabResult,
    find_crossings_piecewise_linear,
    local_extrema,
    mean_trapezoidal,
    tpa_example_director,
    assert_equal,
)

LAB_ID = "LAB-10"
TITLE = "TPA — TVMTPA y criterio factual de extremos"

def run() -> LabResult:
    phi = list(tpa_example_director())
    mean_val = mean_trapezoidal(phi)
    crossings = find_crossings_piecewise_linear(phi, mean_val)
    extrema = local_extrema(phi)

    assert_equal(min(phi) <= mean_val <= max(phi), True)
    assert_equal(len(crossings) >= 1, True)
    assert_equal(extrema["maxima"], [4, 5])
    assert_equal(extrema["minima"], [9])

    return LabResult(
        lab_id=LAB_ID,
        title=TITLE,
        status="CONFIRMA",
        passed=True,
        summary="La media factual cae dentro del rango observable y la curva lineal a trozos la alcanza; los extremos se detectan por el cambio de signo de M.",
        details={"phi": phi, "mean": mean_val, "crossings": crossings, "extrema": extrema},
    )

if __name__ == "__main__":
    print(run().to_dict())
