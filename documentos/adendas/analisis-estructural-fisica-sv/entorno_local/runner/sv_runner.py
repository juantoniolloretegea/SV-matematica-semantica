from pathlib import Path
import json
import sys

# Permite ejecución directa desde runner/, labs/, scripts/ o tests/
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from core.boundary import evaluate_boundary
from core.errors import FFSVError
from core.reopen import reopen
from core.residuals import compute_residuals
from core.trajectory import build_trajectory
from core.verdict import compute_verdict


def classify(residuals):
    return [1 if r == 0 else ('U' if r == 'U' else 0) for r in residuals]


def _is_valid_state(value):
    return value is None or value == 'U' or isinstance(value, (int, float))


def validate_input_payload(payload):
    if not isinstance(payload, dict):
        raise FFSVError('FFSV-001', 'La entrada debe ser un objeto JSON.')

    states = payload.get('states')
    if not isinstance(states, list) or not states:
        raise FFSVError('FFSV-001', 'La clave "states" debe existir y contener una lista no vacía.')
    if any(not _is_valid_state(value) for value in states):
        raise FFSVError('FFSV-004', 'Todos los estados deben ser numéricos, nulos o iguales a "U".')

    transforms = payload.get('transforms', [])
    if not isinstance(transforms, list):
        raise FFSVError('FFSV-002', 'La clave "transforms" debe contener una lista.')
    if len(transforms) not in (0, len(states) - 1, len(states)):
        raise FFSVError(
            'FFSV-002',
            'La longitud de "transforms" debe ser 0, n-1 o n respecto de la trayectoria declarada.'
        )

    horizon = payload.get('horizon')
    if not isinstance(horizon, dict) or not str(horizon.get('domain', '')).strip():
        raise FFSVError('FFSV-006', 'El contrato JSON exige un horizonte declarado con clave "domain" no vacía.')

    nuevos_estados = horizon.get('nuevos_estados')
    if nuevos_estados is not None:
        if not isinstance(nuevos_estados, list) or not nuevos_estados:
            raise FFSVError('FFSV-005', 'La reapertura debe declarar una lista no vacía en "horizon.nuevos_estados".')
        if any(not _is_valid_state(value) for value in nuevos_estados):
            raise FFSVError('FFSV-005', 'Los estados de reapertura deben ser numéricos, nulos o iguales a "U".')

    return payload


def run_sv_analysis(states, transforms=None, horizon=None):
    trajectory = build_trajectory(states, transforms)
    if isinstance(horizon, dict) and horizon.get('nuevos_estados'):
        trajectory = reopen(trajectory, horizon['nuevos_estados'])
    residuals = compute_residuals(trajectory)
    classification = classify(residuals)
    boundary = evaluate_boundary(classification)
    verdict = compute_verdict(boundary)
    return {
        'trajectory': trajectory,
        'residuals': residuals,
        'classification': classification,
        'boundary': boundary,
        'verdict': verdict,
        'horizon': horizon or {}
    }


def _extract_input_payload(data):
    if isinstance(data, dict):
        if 'states' in data:
            return data
        if isinstance(data.get('input'), dict) and 'states' in data['input']:
            return data['input']
    raise FFSVError(
        'FFSV-001',
        'El JSON debe ser un objeto con "states" o un sobre con clave "input" que la contenga.'
    )


def run_from_data(data):
    payload = validate_input_payload(_extract_input_payload(data))
    return run_sv_analysis(
        payload['states'],
        payload.get('transforms', []),
        payload['horizon']
    )


def run_from_json(path):
    data = json.loads(Path(path).read_text(encoding='utf-8'))
    if isinstance(data, list):
        raise FFSVError(
            'FFSV-001',
            'run_from_json() admite un único caso por archivo. Para baterías use run_cases_from_json().'
        )
    return run_from_data(data)


def run_cases_from_json(path):
    data = json.loads(Path(path).read_text(encoding='utf-8'))
    if isinstance(data, list):
        resultados = []
        for idx, item in enumerate(data):
            resultado = run_from_data(item)
            if isinstance(item, dict) and 'name' in item:
                resultado['name'] = item['name']
            else:
                resultado['name'] = f'caso_{idx + 1}'
            resultados.append(resultado)
        return resultados
    resultado = run_from_data(data)
    if isinstance(data, dict) and 'name' in data:
        resultado['name'] = data['name']
    return [resultado]


if __name__ == '__main__':
    sample = run_sv_analysis([1, 1], transforms=['paso_1'], horizon={'domain': 'manual'})
    print(json.dumps(sample, indent=2, ensure_ascii=False))
