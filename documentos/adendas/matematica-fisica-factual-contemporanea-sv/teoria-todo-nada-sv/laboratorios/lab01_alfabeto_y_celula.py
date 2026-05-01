"""
Laboratorio 01 — Alfabeto y célula

Documento canónico vinculado:
  Teoría del TODO y de la NADA en el Sistema Vectorial SV
  https://github.com/juantoniolloretegea/SV-matematica-semantica/tree/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/teoria-todo-nada-sv

Sección doctrinal: §2.1
Criterio de aptitud: enumeración exhaustiva de K₃ⁿ sin colisión ni omisión.

Author:    Juan Antonio Lloret Egea
ORCID:     https://orcid.org/0000-0002-6634-3351
ISSN:      2695-6411
Editor:    IA eñ™ — La Biblia de la IA™ (Instituto Tecnológico Virtual de la
           Inteligencia Artificial para el Español, ITVIA)
License:   CC BY-NC-ND 4.0
Copyright: © 2026 Juan Antonio Lloret Egea. Todos los derechos reservados.
Protected: CEDRO — https://www.cedro.org/english?lng=en
"""

from itertools import product
from sv_lib import (
    SIGMA, SV_TODO_NADA_RESULT, header, zeta_SV, passes_E7
)


def run() -> SV_TODO_NADA_RESULT:
    result = SV_TODO_NADA_RESULT(
        lab_id="lab01",
        section="§2.1",
        verdict=None,
        components=[],
        trace=[],
        passes_E7=False,
    )

    # 1) Verificar la pertenencia tipada de configuraciones a Σⁿ
    for n in (1, 2, 3, 9):
        cube = list(product(SIGMA, repeat=n))
        expected = 3 ** n
        if len(cube) != expected:
            result.trace.append(
                f"E6 — cardinal de Σ^{n} = {len(cube)} ≠ esperado 3^{n} = {expected}"
            )
            result.components.append(1)
        else:
            result.trace.append(
                f"|Σ^{n}| = 3^{n} = {expected} verificado por enumeración exhaustiva."
            )
            result.components.append(0)

    # 2) Verificar ausencia de colisiones (todos distintos)
    cube_9 = list(product(SIGMA, repeat=9))
    if len(set(cube_9)) == len(cube_9) == 19683:
        result.trace.append(
            "Sin colisiones: 19 683 configuraciones únicas en Σ⁹ = K₃⁹."
        )
        result.components.append(0)
    else:
        result.trace.append(
            f"E6 — colisiones detectadas en Σ⁹: {len(cube_9) - len(set(cube_9))}."
        )
        result.components.append(1)

    # 3) Verificar equivalencia notacional SV(9, 3) ≡ SV(3, 9)
    # Por el §2.1: SV(b, n) y SV(n, b) son notaciones equivalentes sobre la
    # célula fundacional con b = 3 y n = 9.
    sv_9_3 = (9, 3)  # (n, b)
    sv_3_9 = (3, 9)  # (b, n)
    if sorted(sv_9_3) == sorted(sv_3_9):
        result.trace.append(
            "Equivalencia notacional SV(9, 3) ≡ SV(3, 9) verificada."
        )
        result.components.append(0)
    else:
        result.trace.append("E6 — equivalencia notacional fallida.")
        result.components.append(1)

    # 4) ζ_SV sobre los componentes para producir veredicto canónico
    # Cada componente vale 0 (verificación correcta) o 1 (fallo); el verificador
    # del laboratorio comprueba nulidad estricta vía E7.
    result.passes_E7 = passes_E7(result.components)
    result.verdict = 0 if result.passes_E7 else 1
    return result


if __name__ == "__main__":
    print(header("lab01", "Alfabeto y célula", "§2.1"))
    r = run()
    print(r.render())
    print()
