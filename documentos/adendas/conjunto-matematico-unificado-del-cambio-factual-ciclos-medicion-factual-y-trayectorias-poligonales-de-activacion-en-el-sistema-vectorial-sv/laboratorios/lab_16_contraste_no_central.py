# Autoría: Juan Antonio Lloret Egea | ORCID: 0000-0002-6634-3351 | Institución: Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA) | Publicación: IA eñ™ — La Biblia de la IA™ | ISSN: 2695-6411 | Licencia: CC BY-NC-ND 4.0 | Lugar y fecha: Madrid, 2026
"""
LAB 16 — Contraste negativo: régimen no central o no homogéneo.

Estado esperado: CONFIRMA.
Si la ley areolar no es constante, el paralelismo con Kepler deja de sostenerse.
"""
from __future__ import annotations
from core.sv_lab_core import LabResult, noncentral_sector_areas_example, assert_equal

LAB_ID = "LAB-16"
TITLE = "Contraste SV — caso no central / no homogéneo"

def run() -> LabResult:
    sectors = noncentral_sector_areas_example(8)
    constant_areas = len(set(round(x, 12) for x in sectors)) == 1
    diffs = [round(sectors[i + 1] - sectors[i], 12) for i in range(len(sectors) - 1)]

    assert_equal(constant_areas, False)

    return LabResult(
        lab_id=LAB_ID,
        title=TITLE,
        status="CONFIRMA",
        passed=True,
        summary="Cuando la velocidad areolar no es constante, el contraste kepleriano deja de confirmarse.",
        details={"sector_areas": sectors, "constant_areas": constant_areas, "differences": diffs},
    )

if __name__ == "__main__":
    print(run().to_dict())
