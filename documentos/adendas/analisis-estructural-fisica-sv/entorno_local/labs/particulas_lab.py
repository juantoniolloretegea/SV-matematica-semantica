"""
Laboratorio de física de partículas — cinco casos del Sistema Vectorial SV.
"""
from pathlib import Path
import sys, json

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from runner.sv_runner import run_sv_analysis

CASOS = {
    'identificacion_univoca': {
        'estados': [1, 1],
        'transforms': ['identificacion'],
        'descripcion': 'La identidad física queda determinada sin ambigüedad.',
        'dictamen_esperado': 'APTO',
    },
    'ambiguedad_estructural': {
        'estados': [1, 'U', 'U'],
        'transforms': ['hipotesis_A', 'hipotesis_B'],
        'descripcion': 'Dos hipótesis permanecen compatibles: la ambigüedad se preserva.',
        'dictamen_esperado': 'INDETERMINADO',
    },
    'hipotesis_dominante': {
        'estados': [1, 1, 'U'],
        'transforms': ['hipotesis_principal', 'hipotesis_residual'],
        'descripcion': 'Una hipótesis domina pero una alternativa residual permanece abierta.',
        'dictamen_esperado': 'INDETERMINADO',
    },
    'conflicto_estructural': {
        'estados': [1, 0, 'U'],
        'transforms': ['hipotesis_A', 'hipotesis_incompatible'],
        'descripcion': 'Hipótesis mutuamente incompatibles: conflicto estructural.',
        'dictamen_esperado': 'NO APTO',
    },
    'no_clausura_ambiguedad': {
        'estados': ['U', 'U'],
        'transforms': ['ambiguedad_irreductible'],
        'descripcion': 'La ambigüedad no puede resolverse: no clausura bajo ambigüedad.',
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
