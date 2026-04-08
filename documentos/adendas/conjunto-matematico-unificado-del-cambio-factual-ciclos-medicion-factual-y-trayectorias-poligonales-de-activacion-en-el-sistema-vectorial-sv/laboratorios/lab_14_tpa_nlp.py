# Autoría: Juan Antonio Lloret Egea | ORCID: 0000-0002-6634-3351 | Institución: Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA) | Publicación: IA eñ™ — La Biblia de la IA™ | ISSN: 2695-6411 | Licencia: CC BY-NC-ND 4.0 | Lugar y fecha: Madrid, 2026
"""
LAB 14 — Proyección TPA sobre un caso conversacional tipo NLP.

Estado esperado: CONFIRMA.
Se construye una trayectoria conversacional compacta y un fork.
"""
from __future__ import annotations
from core.sv_lab_core import (
    LabResult,
    affine_reference_area,
    local_extrema,
    mean_trapezoidal,
    trapezoid_area,
    assert_equal,
)

LAB_ID = "LAB-14"
TITLE = "TPA — proyección aplicada al agente NLP"

def run() -> LabResult:
    # Trayectoria conversacional compacta de 9 turnos.
    conv = [5, 6, 7, 7, 5, 4, 3, 2, 1, 0]
    n_turns = len(conv) - 1
    A = trapezoid_area(conv)
    phi_bar = mean_trapezoidal(conv)
    A_af = affine_reference_area(conv[0], conv[-1], n_turns)
    delta_af = A - A_af
    extrema = local_extrema(conv)

    # Fork desde k*=3
    base_tail = conv[3:]
    fork_tail = [7, 8, 7, 5, 3, 1, 0]
    A_fork_extra = trapezoid_area(fork_tail) - trapezoid_area(base_tail)
    grad_k3 = n_turns - 3 - 0.5

    assert_equal(max(conv), 7)
    assert_equal(phi_bar > 0, True)
    assert_equal(delta_af > 0, True)
    assert_equal(A_fork_extra > 0, True)
    assert_equal(grad_k3, 5.5)
    assert_equal(extrema["maxima"], [2, 3])

    return LabResult(
        lab_id=LAB_ID,
        title=TITLE,
        status="CONFIRMA",
        passed=True,
        summary="La proyección NLP produce densidad de ambigüedad, pico conversacional y coste adicional de fork coherentes con el documento.",
        details={
            "conversation_phi": conv,
            "A_conv": A,
            "phi_bar": phi_bar,
            "A_af": A_af,
            "delta_af": delta_af,
            "extrema": extrema,
            "fork_tail": fork_tail,
            "A_fork_extra": A_fork_extra,
            "grad_at_k3": grad_k3,
        },
    )

if __name__ == "__main__":
    print(run().to_dict())
