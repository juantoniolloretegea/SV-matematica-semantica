from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from runner.sv_runner import run_from_json


def test_all_datasets_smoke():
    base = ROOT / 'datasets'
    for path in sorted(base.glob('*_minimo.json')):
        result = run_from_json(path)
        assert 'verdict' in result
        assert 'boundary' in result
        assert result['verdict'] in ('APTO', 'NO APTO', 'INDETERMINADO')
