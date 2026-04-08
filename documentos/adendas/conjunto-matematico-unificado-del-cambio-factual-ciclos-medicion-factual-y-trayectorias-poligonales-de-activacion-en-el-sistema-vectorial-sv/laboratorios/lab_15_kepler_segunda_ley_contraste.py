# Autoría: Juan Antonio Lloret Egea | ORCID: 0000-0002-6634-3351 | Institución: Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA) | Publicación: IA eñ™ — La Biblia de la IA™ | ISSN: 2695-6411 | Licencia: CC BY-NC-ND 4.0 | Lugar y fecha: Madrid, 2026
"""
LAB 15 — Contraste con la segunda ley de Kepler.

Estado esperado: CONFIRMA.
Se usa una simulación sobria: si la velocidad areolar es constante y la activación
de referencia es homogénea, las áreas por tramo resultan iguales.
"""
from __future__ import annotations
from core.sv_lab_core import LabResult, kepler_sector_areas_from_areal_velocity, assert_equal

LAB_ID = "LAB-15"
TITLE = "Contraste SV — segunda ley de Kepler bajo velocidad areolar constante"

def run() -> LabResult:
    mu_area = 2.75
    delta_tau = 0.5
    n = 8
    sectors = kepler_sector_areas_from_areal_velocity(mu_area, delta_tau, n)
    normalized = [area / delta_tau for area in sectors]

    assert_equal(len(set(round(x, 12) for x in sectors)) == 1, True)
    assert_equal(len(set(round(x, 12) for x in normalized)) == 1, True)

    return LabResult(
        lab_id=LAB_ID,
        title=TITLE,
        status="CONFIRMA",
        passed=True,
        summary="Bajo velocidad areolar constante y escala homogénea, las áreas sectoriales y sus normalizaciones permanecen invariantes por tramo.",
        details={
            "mu_area": mu_area,
            "delta_tau": delta_tau,
            "sector_areas": sectors,
            "normalized_areas": normalized,
        },
    )

if __name__ == "__main__":
    print(run().to_dict())
