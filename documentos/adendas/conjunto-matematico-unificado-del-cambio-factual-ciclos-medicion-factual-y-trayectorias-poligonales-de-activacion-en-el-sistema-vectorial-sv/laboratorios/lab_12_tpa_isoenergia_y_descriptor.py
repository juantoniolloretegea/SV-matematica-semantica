# Autoría: Juan Antonio Lloret Egea | ORCID: 0000-0002-6634-3351 | Institución: Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA) | Publicación: IA eñ™ — La Biblia de la IA™ | ISSN: 2695-6411 | Licencia: CC BY-NC-ND 4.0 | Lugar y fecha: Madrid, 2026
"""
LAB 12 — Isoenergía y no completitud del descriptor cuádruplo.

Estado esperado: CONFIRMA.
"""
from __future__ import annotations
from core.sv_lab_core import (
    LabResult,
    descriptor_quadruple,
    generating_function_coefficients,
    tpa_descriptor_collision_pair,
    assert_equal,
)

LAB_ID = "LAB-12"
TITLE = "TPA — isoenergía y descriptor cuádruplo de primer orden"

def run() -> LabResult:
    phi_a, phi_b = tpa_descriptor_collision_pair()
    q_a = descriptor_quadruple(phi_a)
    q_b = descriptor_quadruple(phi_b)

    assert_equal(q_a, q_b)
    assert_equal(phi_a != phi_b, True)
    assert_equal(generating_function_coefficients(phi_a) != generating_function_coefficients(phi_b), True)

    return LabResult(
        lab_id=LAB_ID,
        title=TITLE,
        status="CONFIRMA",
        passed=True,
        summary="Se confirma que el descriptor cuádruplo es de primer orden y no determina por sí solo la TPA completa.",
        details={
            "phi_a": phi_a,
            "phi_b": phi_b,
            "quadruple": q_a,
            "G_coeffs_a": generating_function_coefficients(phi_a),
            "G_coeffs_b": generating_function_coefficients(phi_b),
        },
    )

if __name__ == "__main__":
    print(run().to_dict())
