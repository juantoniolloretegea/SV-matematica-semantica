# Autoría: Juan Antonio Lloret Egea | ORCID: 0000-0002-6634-3351 | Institución: Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA) | Publicación: IA eñ™ — La Biblia de la IA™ | ISSN: 2695-6411 | Licencia: CC BY-NC-ND 4.0 | Lugar y fecha: Madrid, 2026
"""
LAB 02 — Umbral rector, gravedad y gravedad detonante.

Estado esperado: CONFIRMA.
Audita:
- T(n)=floor(7n/9),
- inclusión E_det ⊆ E_sens ∩ E_crit,
- G_det <= G.
"""
from __future__ import annotations
import math
from core.sv_lab_core import LabResult, assert_equal

LAB_ID = "LAB-02"
TITLE = "CMODCF-SV — umbral rector y gravedad modulada"

def run() -> LabResult:
    Q = list(range(9))
    E_crit = {0, 1, 2, 3, 4, 5, 6}
    E_sens = {0, 1, 2, 3, 4, 5, 7}
    E_det = {0, 1, 2, 3, 4, 5}
    Tn = math.floor(7 * len(Q) / 9)
    G = len(E_crit) / len(Q)
    G_det = len(E_det) / len(Q)

    assert_equal(Tn, 7)
    assert_equal(E_det.issubset(E_sens.intersection(E_crit)), True)
    assert_equal(G_det <= G, True)
    assert_equal(len(E_crit) >= Tn, True)

    return LabResult(
        lab_id=LAB_ID,
        title=TITLE,
        status="CONFIRMA",
        passed=True,
        summary="Se confirma el umbral rector y la inclusión detonante de la gravedad.",
        details={
            "Q": len(Q),
            "Tn": Tn,
            "E_crit": sorted(E_crit),
            "E_sens": sorted(E_sens),
            "E_det": sorted(E_det),
            "G": G,
            "G_det": G_det,
        },
    )

if __name__ == "__main__":
    print(run().to_dict())
