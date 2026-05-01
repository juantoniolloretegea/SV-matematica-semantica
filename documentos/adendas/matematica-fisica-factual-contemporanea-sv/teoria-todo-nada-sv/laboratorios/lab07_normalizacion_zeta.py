"""
Laboratorio 07 — Normalización ζ_SV

Documento canónico vinculado:
  Teoría del TODO y de la NADA en el Sistema Vectorial SV
  https://github.com/juantoniolloretegea/SV-matematica-semantica/tree/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/teoria-todo-nada-sv

Sección doctrinal: §13.1
Criterio de aptitud: las tres ramas de la regla por casos de ζ_SV evaluadas
correctamente sobre los casos de borde: x = 0, x ∈ (0, ∞), x = U.

Author:    Juan Antonio Lloret Egea
ORCID:     https://orcid.org/0000-0002-6634-3351
ISSN:      2695-6411
Editor:    IA eñ™ — La Biblia de la IA™ (Instituto Tecnológico Virtual de la
           Inteligencia Artificial para el Español, ITVIA)
License:   CC BY-NC-ND 4.0
Copyright: © 2026 Juan Antonio Lloret Egea. Todos los derechos reservados.
Protected: CEDRO — https://www.cedro.org/english?lng=en
"""

import math
from sv_lib import SV_TODO_NADA_RESULT, header, zeta_SV, passes_E7


def run() -> SV_TODO_NADA_RESULT:
    result = SV_TODO_NADA_RESULT(
        lab_id="lab07",
        section="§13.1",
        verdict=None,
        components=[],
        trace=[],
        passes_E7=False,
    )

    # Casos canónicos de borde por el §13.1 del documento canónico.
    casos = [
        # (entrada, salida_esperada, descripción)
        (0,            0,    "rama 1: x = 0 → ζ_SV(0) = 0"),
        (1,            1,    "rama 2: x = 1 ∈ (0, ∞) → ζ_SV(1) = 1"),
        (0.5,          1,    "rama 2: x = 0.5 ∈ (0, ∞) → ζ_SV(0.5) = 1"),
        (1e-12,        1,    "rama 2: x = 10⁻¹² ∈ (0, ∞) → ζ_SV(ε) = 1"),
        (1000,         1,    "rama 2: x = 1000 ∈ (0, ∞) → ζ_SV(1000) = 1"),
        (math.inf,     1,    "rama 2: x = ∞ → ζ_SV(∞) = 1"),
        ('U',          'U',  "rama 3: x = U → ζ_SV(U) = U"),
    ]

    for entrada, esperado, descripcion in casos:
        try:
            obtenido = zeta_SV(entrada)
            if obtenido == esperado:
                result.trace.append(f"✓ {descripcion} | obtenido = {obtenido}")
                result.components.append(0)
            else:
                result.trace.append(
                    f"✗ E6 — {descripcion} | esperado = {esperado}, obtenido = {obtenido}"
                )
                result.components.append(1)
        except Exception as e:
            result.trace.append(f"✗ E6 — {descripcion} | excepción: {e}")
            result.components.append(1)

    result.passes_E7 = passes_E7(result.components)
    result.verdict = 0 if result.passes_E7 else 1
    return result


if __name__ == "__main__":
    print(header("lab07", "Normalización ζ_SV", "§13.1"))
    r = run()
    print(r.render())
    print()
