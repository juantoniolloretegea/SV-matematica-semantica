"""
Laboratorio de coincidencia multidetector — cinco casos del Sistema Vectorial SV.
"""
from pathlib import Path
import sys, json

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from runner.sv_runner import run_sv_analysis

CASOS = {
    'coincidencia_completa': {
        'estados': [1, 1, 1],
        'transforms': ['detector_A', 'detector_B'],
        'descripcion': 'Tres detectores coinciden plenamente: clausura estructural legítima.',
        'dictamen_esperado': 'APTO',
    },
    'coincidencia_parcial': {
        'estados': [1, 1, 'U'],
        'transforms': ['detector_A', 'detector_B_parcial'],
        'descripcion': 'Dos detectores coinciden; el tercero es indeterminado.',
        'dictamen_esperado': 'INDETERMINADO',
    },
    'correlacion_aparente': {
        'estados': [1, 1, 0],
        'transforms': ['detector_A', 'detector_B', 'detector_C_conflicto'],
        'descripcion': 'Detectores A y B coinciden numéricamente pero C los contradice: '
                       'la coincidencia aparente queda expuesta como no estructural.',
        'dictamen_esperado': 'NO APTO',
    },
    'conflicto_estructural': {
        'estados': [1, 0, 'U'],
        'transforms': ['detector_A', 'detector_B_conflicto'],
        'descripcion': 'Un detector contradice al otro: conflicto estructural irresuelto.',
        'dictamen_esperado': 'NO APTO',
    },
    'no_clausura_multidetector': {
        'estados': ['U', 'U', 'U'],
        'transforms': ['detector_A_U', 'detector_B_U'],
        'descripcion': 'Ningún detector cierra: no clausura multidetector.',
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
