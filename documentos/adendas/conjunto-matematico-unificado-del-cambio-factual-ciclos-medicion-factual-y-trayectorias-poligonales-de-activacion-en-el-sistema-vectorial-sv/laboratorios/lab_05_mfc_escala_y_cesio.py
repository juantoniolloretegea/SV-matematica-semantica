# Autoría: Juan Antonio Lloret Egea | ORCID: 0000-0002-6634-3351 | Institución: Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA) | Publicación: IA eñ™ — La Biblia de la IA™ | ISSN: 2695-6411 | Licencia: CC BY-NC-ND 4.0 | Lugar y fecha: Madrid, 2026
"""
LAB 05 — Escala del medidor factual de ciclo y referencia del cesio.

Estado esperado: CONFIRMA.
Audita:
- división exacta 9_192_631_770 / 9,
- trayectoria de referencia de meseta,
- coste factual y descriptor del caso canónico.
"""
from __future__ import annotations
from core.sv_lab_core import LabResult, descriptor_quadruple, mfc_reference_cycle, assert_equal

LAB_ID = "LAB-05"
TITLE = "Medidor factual de ciclo — escala, cesio y trayectoria canónica"

def run() -> LabResult:
    cesio = 9_192_631_770
    ue = cesio // 9
    residuo = cesio % 9
    phi = mfc_reference_cycle(phi0=3, n=9)
    area, sigma_m, phi_max, l1 = descriptor_quadruple(phi)

    assert_equal(ue, 1_021_403_530)
    assert_equal(residuo, 0)
    assert_equal(area, 27.0)
    assert_equal(sigma_m, 0)
    assert_equal(phi_max, 3)
    assert_equal(l1, 0.0)

    return LabResult(
        lab_id=LAB_ID,
        title=TITLE,
        status="CONFIRMA",
        passed=True,
        summary="Se confirma la descomposición exacta del cesio y el descriptor del caso canónico de meseta.",
        details={
            "cesio": cesio,
            "ue_mfc": ue,
            "residuo": residuo,
            "phi_ref": phi,
            "descriptor": {"A": area, "sum_m": sigma_m, "phi_max": phi_max, "l1": l1},
        },
    )

if __name__ == "__main__":
    print(run().to_dict())
