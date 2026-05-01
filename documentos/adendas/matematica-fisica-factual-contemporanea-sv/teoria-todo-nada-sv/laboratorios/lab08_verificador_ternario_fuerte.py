"""
Laboratorio 08 — Verificador ternario fuerte 𝓝★_SV

Documento canónico vinculado:
  Teoría del TODO y de la NADA en el Sistema Vectorial SV
  https://github.com/juantoniolloretegea/SV-matematica-semantica/tree/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/teoria-todo-nada-sv

Sección doctrinal: §§13.3-13.5
Criterio de aptitud: tabla exhaustiva de las 27 entradas con cardinal canónico
(1 entrada → 0, 19 entradas → 1, 7 entradas → U).

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
from sv_lib import SIGMA, SV_TODO_NADA_RESULT, header, N_star_SV, passes_E7


def run() -> SV_TODO_NADA_RESULT:
    result = SV_TODO_NADA_RESULT(
        lab_id="lab08",
        section="§§13.3-13.5",
        verdict=None,
        components=[],
        trace=[],
        passes_E7=False,
    )

    # Tabla exhaustiva del verificador 𝓝★_SV para m = 3 (Tabla 13.5.1).
    # 3³ = 27 entradas posibles sobre Σ³.
    cuenta_0 = 0
    cuenta_1 = 0
    cuenta_U = 0
    tabla = []

    for entrada in product(SIGMA, repeat=3):
        salida = N_star_SV(*entrada)
        tabla.append((entrada, salida))
        if salida == 0:
            cuenta_0 += 1
        elif salida == 1:
            cuenta_1 += 1
        elif salida == 'U':
            cuenta_U += 1

    # Cardinal canónico esperado sobre las 27 entradas:
    #   1 entrada con salida 0 (la única tupla (0, 0, 0))
    #   19 entradas con salida 1 (todas las que contienen al menos un 1)
    #   7 entradas con salida U (las que no tienen 1 pero sí al menos un U)
    total = cuenta_0 + cuenta_1 + cuenta_U
    result.trace.append(f"Total entradas computadas = {total} (esperado 27)")
    result.trace.append(f"Cardinal de salidas:")
    result.trace.append(f"  · 0 → {cuenta_0}  (esperado 1)")
    result.trace.append(f"  · 1 → {cuenta_1}  (esperado 19)")
    result.trace.append(f"  · U → {cuenta_U}  (esperado 7)")

    if total == 27:
        result.components.append(0)
    else:
        result.trace.append("E6 — total ≠ 27.")
        result.components.append(1)

    if cuenta_0 == 1:
        result.components.append(0)
    else:
        result.trace.append(f"E6 — cuenta_0 = {cuenta_0} ≠ 1.")
        result.components.append(1)

    if cuenta_1 == 19:
        result.components.append(0)
    else:
        result.trace.append(f"E6 — cuenta_1 = {cuenta_1} ≠ 19.")
        result.components.append(1)

    if cuenta_U == 7:
        result.components.append(0)
    else:
        result.trace.append(f"E6 — cuenta_U = {cuenta_U} ≠ 7.")
        result.components.append(1)

    # Verificación de la prelación 1 ≻ U ≻ 0:
    # (i) cualquier entrada con un 1 da salida 1
    for entrada, salida in tabla:
        if 1 in entrada and salida != 1:
            result.trace.append(f"E6 — prelación rota: {entrada} → {salida}")
            result.components.append(1)
            break
    else:
        result.trace.append("Prelación 1 ≻ U ≻ 0: todas las entradas con 1 dan salida 1 ✓")
        result.components.append(0)

    # (ii) entrada (0, 0, 0) da salida 0
    if N_star_SV(0, 0, 0) == 0:
        result.components.append(0)
    else:
        result.components.append(1)

    result.passes_E7 = passes_E7(result.components)
    result.verdict = 0 if result.passes_E7 else 1
    return result


if __name__ == "__main__":
    print(header("lab08", "Verificador ternario fuerte 𝓝★_SV", "§§13.3-13.5"))
    r = run()
    print(r.render())
    print()
