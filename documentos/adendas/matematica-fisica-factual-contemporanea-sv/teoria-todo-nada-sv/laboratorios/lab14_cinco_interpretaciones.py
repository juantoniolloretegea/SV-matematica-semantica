"""
Laboratorio 14 — Cinco interpretaciones canónicas de la rectora

Documento canónico vinculado:
  Teoría del TODO y de la NADA en el Sistema Vectorial SV
  https://github.com/juantoniolloretegea/SV-matematica-semantica/tree/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/teoria-todo-nada-sv

Sección doctrinal: §22
Criterio de aptitud: los cinco veredictos coinciden exactamente con los
enunciados en la Tabla 22.6.1 bajo la prelación 1 ≻ U ≻ 0.

Author:    Juan Antonio Lloret Egea
ORCID:     https://orcid.org/0000-0002-6634-3351
ISSN:      2695-6411
Editor:    IA eñ™ — La Biblia de la IA™ (Instituto Tecnológico Virtual de la
           Inteligencia Artificial para el Español, ITVIA)
License:   CC BY-NC-ND 4.0
Copyright: © 2026 Juan Antonio Lloret Egea. Todos los derechos reservados.
Protected: CEDRO — https://www.cedro.org/english?lng=en
"""

from sv_lib import SV_TODO_NADA_RESULT, header, N_star_SV, passes_E7


# Tabla 22.6.1 del documento canónico — cinco interpretaciones:
INTERPRETACIONES = [
    {
        "id": "I1",
        "nombre": "Convergente plena",
        "defectos": [0, 0, 0, 0, 0, 0, 0, 0, 0],
        "veredicto_esperado": 0,
    },
    {
        "id": "I2",
        "nombre": "Refutación local",
        "defectos": [0, 0, 1, 0, 0, 0, 0, 0, 0],
        "veredicto_esperado": 1,
    },
    {
        "id": "I3",
        "nombre": "No clausura honesta",
        "defectos": [0, 0, 'U', 0, 0, 0, 0, 0, 0],
        "veredicto_esperado": 'U',
    },
    {
        "id": "I4",
        "nombre": "Refutación con no clausura paralela",
        "defectos": [0, 0, 1, 0, 'U', 0, 0, 0, 0],
        "veredicto_esperado": 1,   # prelación 1 ≻ U ≻ 0
    },
    {
        "id": "I5",
        "nombre": "Inadmisibilidad por estado corpus τ",
        "defectos": [0, 0, 0, 1, 0, 'U', 0, 0, 0],
        "veredicto_esperado": 1,   # prelación 1 ≻ U ≻ 0
    },
]


def run() -> SV_TODO_NADA_RESULT:
    result = SV_TODO_NADA_RESULT(
        lab_id="lab14",
        section="§22",
        verdict=None,
        components=[],
        trace=[],
        passes_E7=False,
    )

    for interp in INTERPRETACIONES:
        veredicto = N_star_SV(*interp["defectos"])
        ok = veredicto == interp["veredicto_esperado"]
        marca = "✓" if ok else "✗"
        result.trace.append(
            f"{marca} {interp['id']} {interp['nombre']:38s} "
            f"→ veredicto {veredicto} (esperado {interp['veredicto_esperado']})"
        )
        result.components.append(0 if ok else 1)

    # Verificación de la prelación 1 ≻ U ≻ 0 sobre las 5 interpretaciones
    prelacion_ok = True
    for interp in INTERPRETACIONES:
        defectos = interp["defectos"]
        veredicto = N_star_SV(*defectos)
        if 1 in defectos and veredicto != 1:
            prelacion_ok = False
        elif 1 not in defectos and 'U' in defectos and veredicto != 'U':
            prelacion_ok = False
        elif 1 not in defectos and 'U' not in defectos and veredicto != 0:
            prelacion_ok = False

    if prelacion_ok:
        result.trace.append("Prelación canónica 1 ≻ U ≻ 0 preservada en las 5 interpretaciones.")
        result.components.append(0)
    else:
        result.trace.append("E6 — prelación rota.")
        result.components.append(1)

    result.passes_E7 = passes_E7(result.components)
    result.verdict = 0 if result.passes_E7 else 1
    return result


if __name__ == "__main__":
    print(header("lab14", "Cinco interpretaciones canónicas de la rectora", "§22"))
    r = run()
    print(r.render())
    print()
