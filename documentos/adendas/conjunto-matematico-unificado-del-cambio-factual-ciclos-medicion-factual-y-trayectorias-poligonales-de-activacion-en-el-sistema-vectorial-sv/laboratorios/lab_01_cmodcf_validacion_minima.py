# Autoría: Juan Antonio Lloret Egea | ORCID: 0000-0002-6634-3351 | Institución: Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA) | Publicación: IA eñ™ — La Biblia de la IA™ | ISSN: 2695-6411 | Licencia: CC BY-NC-ND 4.0 | Lugar y fecha: Madrid, 2026
"""
LAB 01 — Validación mínima CMODCF-SV.

Estado esperado: CONFIRMA.
Audita:
- discriminación directriz mínima,
- criterio mínimo de detonación explícita,
- separación entre neutralidad trivial y equilibrio estructural.

Pseudocódigo:
1. Construir un caso positivo con reducción factual de irreducibilidad.
2. Calcular D_Gamma(u_irr), E_j y T(nu).
3. Confirmar que el caso positivo es directriz y detonante activo.
4. Construir un caso adversarial negativo con mera modificación local.
5. Confirmar que no hay directriz suficiente ni detonación.
"""
from __future__ import annotations
from core.sv_lab_core import LabResult, assert_equal

LAB_ID = "LAB-01"
TITLE = "CMODCF-SV — validación mínima positiva y adversarial"

def run() -> LabResult:
    # Caso positivo del documento.
    u0_pos, u1_pos = 3, 0
    alpha_pos, delta_pos, beta_pos, rho_pos = 1, 3, 1, 0
    d_pos = -alpha_pos * delta_pos + beta_pos * rho_pos
    e_pos = alpha_pos * delta_pos - beta_pos * rho_pos
    directriz_pos = d_pos < 0
    detonante_pos = (e_pos > 0 and delta_pos > 0 and directriz_pos)

    assert_equal(d_pos, -3)
    assert_equal(e_pos, 3)
    assert_equal(directriz_pos, True)
    assert_equal(detonante_pos, True)

    # Caso adversarial negativo del documento.
    u0_neg, u1_neg = 1, 1
    alpha_neg, delta_neg, beta_neg, rho_neg = 1, 0, 1, 0
    d_neg = -alpha_neg * delta_neg + beta_neg * rho_neg
    e_neg = alpha_neg * delta_neg - beta_neg * rho_neg
    directriz_neg = d_neg < 0
    detonante_neg = (e_neg > 0 and delta_neg > 0 and directriz_neg)
    neutralidad_trivial = (d_neg == 0 and delta_neg == 0 and rho_neg == 0)

    assert_equal(d_neg, 0)
    assert_equal(e_neg, 0)
    assert_equal(directriz_neg, False)
    assert_equal(detonante_neg, False)
    assert_equal(neutralidad_trivial, True)

    return LabResult(
        lab_id=LAB_ID,
        title=TITLE,
        status="CONFIRMA",
        passed=True,
        summary="El caso positivo satisface directriz y detonación; el caso adversarial cae en neutralidad trivial.",
        details={
            "caso_positivo": {"u0": u0_pos, "u1": u1_pos, "D": d_pos, "E": e_pos, "directriz": directriz_pos, "detonante": detonante_pos},
            "caso_negativo": {"u0": u0_neg, "u1": u1_neg, "D": d_neg, "E": e_neg, "directriz": directriz_neg, "detonante": detonante_neg, "neutralidad_trivial": neutralidad_trivial},
        },
    )

if __name__ == "__main__":
    print(run().to_dict())
