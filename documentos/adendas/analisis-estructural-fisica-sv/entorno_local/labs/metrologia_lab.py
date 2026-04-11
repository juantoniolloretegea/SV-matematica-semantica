"""
Laboratorio metrológico — cinco casos del Sistema Vectorial SV.
Cada caso fija estados, transformación y dictamen esperado.
El laboratorio verifica que el sistema produce exactamente el dictamen declarado.
"""
from pathlib import Path
import sys, json

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from runner.sv_runner import run_sv_analysis

CASOS = {
    'equivalencia_ideal': {
        'estados': [1, 1],
        'transforms': ['conversion_exacta'],
        'descripcion': 'Conversión sin pérdida de información estructural.',
        'dictamen_esperado': 'APTO',
    },
    'reduccion_con_perdida': {
        'estados': [1, 0.8],
        'transforms': ['reduccion'],
        'descripcion': 'Reducción que destruye información: residual estructural presente.',
        'dictamen_esperado': 'NO APTO',
    },
    'compensacion_aparente': {
        'estados': [1, 1, 'U'],
        'transforms': ['conversion_exacta', 'estimacion'],
        'descripcion': 'Resultado aparentemente cerrado con paso intermedio indeterminado.',
        'dictamen_esperado': 'INDETERMINADO',
    },
    'incompatibilidad_dimensional': {
        'estados': [1, 0],
        'transforms': ['transformacion_incompatible'],
        'descripcion': 'Estados incompatibles: residual máximo, frontera no cerrable.',
        'dictamen_esperado': 'NO APTO',
    },
    'no_clausura_metrologica': {
        'estados': ['U', 'U'],
        'transforms': ['medicion_indeterminada'],
        'descripcion': 'La medición no puede cerrarse: indeterminación estructural.',
        'dictamen_esperado': 'INDETERMINADO',
    },
}


def run_all():
    resultados = {}
    fallos = []
    for nombre, caso in CASOS.items():
        resultado = run_sv_analysis(
            caso['estados'],
            transforms=caso['transforms'],
        )
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
