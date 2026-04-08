# Autoría: Juan Antonio Lloret Egea | ORCID: 0000-0002-6634-3351 | Institución: Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA) | Publicación: IA eñ™ — La Biblia de la IA™ | ISSN: 2695-6411 | Licencia: CC BY-NC-ND 4.0 | Lugar y fecha: Madrid, 2026
"""
LAB 03 — Propiedades básicas del Ciclo de Suceso.

Estado esperado: CONFIRMA.
Audita:
- CS-1: Σm_k = 0 en ciclo.
- CS-2: conservatividad del observable director.
- CS-0: misma área no implica misma trayectoria ni mismo polígono.
"""
from __future__ import annotations
from core.sv_lab_core import (
    LabResult,
    area_partition,
    balance,
    cycle_descriptor_first_order,
    descriptor_quadruple,
    divergence,
    eq_cost_first_order,
    is_cycle,
    slopes,
    tpa_cycle_counterexample_same_area,
    assert_close,
    assert_equal,
)

LAB_ID = "LAB-03"
TITLE = "Ciclo de Suceso — propiedades básicas y contraejemplo de misma área"

def run() -> LabResult:
    phi_a, phi_b = tpa_cycle_counterexample_same_area()
    m_a = slopes(phi_a)
    m_b = slopes(phi_b)
    assert_equal(is_cycle(phi_a), True)
    assert_equal(is_cycle(phi_b), True)
    assert_equal(sum(m_a), 0)
    assert_equal(sum(m_b), 0)
    assert_equal(balance(phi_a), 0)
    assert_equal(balance(phi_b), 0)

    area_a = descriptor_quadruple(phi_a)[0]
    area_b = descriptor_quadruple(phi_b)[0]
    assert_close(area_a, 20.0)
    assert_close(area_b, 20.0)
    assert_equal(phi_a != phi_b, True)
    assert_equal(max(phi_a) != max(phi_b), True)
    assert_equal(eq_cost_first_order(phi_a, phi_b), False)

    return LabResult(
        lab_id=LAB_ID,
        title=TITLE,
        status="CONFIRMA",
        passed=True,
        summary="Se confirma Σm_k=0 y el balance nulo en ciclos; se refuta que igual área implique misma trayectoria.",
        details={
            "phi_a": phi_a,
            "phi_b": phi_b,
            "m_a": m_a,
            "m_b": m_b,
            "area_a": area_a,
            "area_b": area_b,
            "balance_a": balance(phi_a),
            "balance_b": balance(phi_b),
            "descriptor_a": cycle_descriptor_first_order(phi_a),
            "descriptor_b": cycle_descriptor_first_order(phi_b),
        },
    )

if __name__ == "__main__":
    print(run().to_dict())
