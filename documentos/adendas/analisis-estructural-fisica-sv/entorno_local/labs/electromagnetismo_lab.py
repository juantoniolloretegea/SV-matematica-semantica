"""
Laboratorio electromagnético — cinco casos del Sistema Vectorial SV.
"""
from pathlib import Path
import sys, json

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from runner.sv_runner import run_sv_analysis

CASOS = {
    'reconstruccion_completa': {
        'estados': [1, 1],
        'transforms': ['reconstruccion_modal'],
        'descripcion': 'Reconstrucción sin residual: el campo se recupera íntegramente.',
        'dictamen_esperado': 'APTO',
    },
    'truncacion_controlada': {
        'estados': [1, 0.8],
        'transforms': ['truncacion'],
        'descripcion': 'Truncación modal con pérdida declarada: residual presente.',
        'dictamen_esperado': 'NO APTO',
    },
    'residual_de_borde': {
        'estados': [1, 1, 'U'],
        'transforms': ['reconstruccion_modal', 'borde'],
        'descripcion': 'La mayor parte del campo se reconstruye, pero el borde queda '
                       'irresuelto: la clausura permanece abierta.',
        'dictamen_esperado': 'INDETERMINADO',
    },
    'conflicto_estructural': {
        'estados': [1, 0],
        'transforms': ['conflicto'],
        'descripcion': 'Conflicto entre campo medido y reconstruido: incompatibilidad.',
        'dictamen_esperado': 'NO APTO',
    },
    'no_clausura_em': {
        'estados': ['U', 'U'],
        'transforms': ['limite_representacion'],
        'descripcion': 'Borde irreductible que impide la clausura: no clausura estructural.',
        'dictamen_esperado': 'INDETERMINADO',
    },
}


def run_all():
    resultados = {}
    fallos = []
    for nombre, caso in CASOS.items():
        resultado = run_sv_analysis(caso['estados'], transforms=caso['transforms'])
        ok = resultado['verdict'] == caso['dictamen_esperado']
        if not ok:
            fallos.append(
                f"{nombre}: esperado {caso['dictamen_esperado']!r}, "
                f"obtenido {resultado['verdict']!r}"
            )
        resultados[nombre] = {
            'descripcion': caso['descripcion'],
            'estados': caso['estados'],
            'dictamen_esperado': caso['dictamen_esperado'],
            'dictamen_obtenido': resultado['verdict'],
            'frontera': resultado['boundary'],
            'residuales': resultado['residuals'],
            'clasificacion': resultado['classification'],
            'ok': ok,
        }
    return resultados, fallos


if __name__ == '__main__':
    resultados, fallos = run_all()
    print(json.dumps(resultados, indent=2, ensure_ascii=False))
    if fallos:
        print('\nFALLOS:', fallos, file=sys.stderr)
        sys.exit(1)
