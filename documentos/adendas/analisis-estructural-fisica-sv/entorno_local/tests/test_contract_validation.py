from pathlib import Path
import json
import sys
import pytest

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from core.errors import FFSVError
from runner.sv_runner import run_cases_from_json, run_from_data


def test_error_horizon_obligatorio():
    with pytest.raises(FFSVError) as exc:
        run_from_data({"states": [1, 1], "transforms": ["paso_1"]})
    assert exc.value.code == 'FFSV-006'


def test_error_longitud_transforms_incompatible():
    with pytest.raises(FFSVError) as exc:
        run_from_data({
            "states": [1, 1, 1],
            "transforms": ["a", "b", "c", "d"],
            "horizon": {"domain": "manual"},
        })
    assert exc.value.code == 'FFSV-002'


def test_error_estado_invalido():
    with pytest.raises(FFSVError) as exc:
        run_from_data({
            "states": [1, "cerrado"],
            "transforms": ["paso_1"],
            "horizon": {"domain": "manual"},
        })
    assert exc.value.code == 'FFSV-004'


def test_reapertura_dataset_se_ejecuta_en_runner():
    resultados = run_cases_from_json(ROOT / 'datasets' / 'no_clausura_casos.json')
    caso = next(item for item in resultados if item['name'] == 'reapertura')
    assert [step['state'] for step in caso['trajectory']] == ['U', 'U', 1]
    assert caso['verdict'] == 'INDETERMINADO'
