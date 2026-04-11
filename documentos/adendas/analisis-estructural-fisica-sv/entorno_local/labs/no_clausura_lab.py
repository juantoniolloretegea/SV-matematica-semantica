"""
Laboratorio de no clausura — cinco casos del Sistema Vectorial SV.
El quinto caso emplea reapertura factual explícita.
"""
from pathlib import Path
import sys, json

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from runner.sv_runner import run_sv_analysis
from core.reopen import reopen
from core.trajectory import build_trajectory
from core.residuals import compute_residuals
from core.boundary import evaluate_boundary
from core.verdict import compute_verdict

CASOS = {
    'determinacion_parcial': {
        'estados': [1, 'U'],
        'transforms': ['medicion_parcial'],
        'descripcion': 'Un estado queda indeterminado: la clausura no puede completarse.',
        'dictamen_esperado': 'INDETERMINADO',
    },
    'dependencia_orden': {
        'estados': ['U', 1, 'U'],
        'transforms': ['orden_A', 'orden_B'],
        'descripcion': 'El resultado depende del orden de medición: indeterminación estructural.',
        'dictamen_esperado': 'INDETERMINADO',
    },
    'no_clausura_irreductible': {
        'estados': ['U', 'U'],
        'transforms': ['limite_observabilidad'],
        'descripcion': 'La no clausura es constitutiva del fenómeno, no instrumental.',
        'dictamen_esperado': 'INDETERMINADO',
    },
    'clausura_forzada': {
        'estados': [1, 0],
        'transforms': ['cierre_forzado'],
        'descripcion': 'Intento de clausura forzada sobre estados incompatibles: NO APTO.',
        'dictamen_esperado': 'NO APTO',
    },
    'reapertura': {
        'estados_iniciales': ['U', 'U'],
        'transforms_iniciales': ['medicion_inicial'],
        'nuevos_estados': [1],
        'descripcion': 'Trayectoria abierta que se reabre con nueva información. '
                       'La reapertura no reescribe el pasado: extiende la trayectoria.',
        'dictamen_esperado_inicial': 'INDETERMINADO',
        'dictamen_esperado_final': 'INDETERMINADO',
    },
}


def run_all():
    resultados = {}
    fallos = []

    for nombre, caso in CASOS.items():
        if nombre == 'reapertura':
            # Caso de reapertura: construir trayectoria inicial y luego extender
            trayectoria_inicial = build_trajectory(
                caso['estados_iniciales'],
                caso['transforms_iniciales'],
            )
            res_i = compute_residuals(trayectoria_inicial)
            from runner.sv_runner import classify
            cls_i = classify(res_i)
            frontera_i = evaluate_boundary(cls_i)
            dictamen_inicial = compute_verdict(frontera_i)

            # Reapertura: extender la trayectoria sin borrar el pasado
            trayectoria_extendida = reopen(trayectoria_inicial, caso['nuevos_estados'])
            res_f = compute_residuals(trayectoria_extendida)
            cls_f = classify(res_f)
            frontera_f = evaluate_boundary(cls_f)
            dictamen_final = compute_verdict(frontera_f)

            ok_i = dictamen_inicial == caso['dictamen_esperado_inicial']
            ok_f = dictamen_final == caso['dictamen_esperado_final']
            ok = ok_i and ok_f
            if not ok:
                fallos.append(
                    f"{nombre}: inicial={dictamen_inicial!r} "
                    f"(esp={caso['dictamen_esperado_inicial']!r}), "
                    f"final={dictamen_final!r} "
                    f"(esp={caso['dictamen_esperado_final']!r})"
                )
            resultados[nombre] = {
                'descripcion': caso['descripcion'],
                'trayectoria_inicial': trayectoria_inicial,
                'trayectoria_extendida': trayectoria_extendida,
                'dictamen_inicial': dictamen_inicial,
                'dictamen_final': dictamen_final,
                'dictamen_esperado_inicial': caso['dictamen_esperado_inicial'],
                'dictamen_esperado_final': caso['dictamen_esperado_final'],
                'pasos_iniciales': len(trayectoria_inicial),
                'pasos_tras_reapertura': len(trayectoria_extendida),
                'ok': ok,
            }
        else:
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
