from pathlib import Path
import json
import sys

BASE_DIR = Path(__file__).resolve().parents[1]
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from runner.sv_runner import run_cases_from_json


if __name__ == '__main__':
    base = BASE_DIR / 'datasets'
    for path in sorted(base.glob('*.json')):
        print(path.name)
        resultados = run_cases_from_json(path)
        for resultado in resultados:
            nombre = resultado.get('name', 'caso')
            resumen = {
                'name': nombre,
                'boundary': resultado['boundary'],
                'verdict': resultado['verdict'],
                'classification': resultado['classification'],
                'residuals': resultado['residuals'],
            }
            print(json.dumps(resumen, indent=2, ensure_ascii=False))
        print('-' * 60)
