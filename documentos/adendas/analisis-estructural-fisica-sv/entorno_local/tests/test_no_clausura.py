from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from runner.sv_runner import run_sv_analysis


def test_no_clausura_irreductible():
    r = run_sv_analysis(['U', 'U'])
    assert r['verdict'] == 'INDETERMINADO'


def test_determinacion_parcial():
    r = run_sv_analysis([1, 'U'])
    assert r['verdict'] == 'INDETERMINADO'
    assert r['residuals'] == ['U']


def test_dependencia_orden():
    r = run_sv_analysis(['U', 1, 'U'])
    assert r['verdict'] == 'INDETERMINADO'
    assert r['residuals'] == ['U', 'U']


def test_clausura_forzada():
    r = run_sv_analysis([1, 0])
    assert r['verdict'] == 'NO APTO'


def test_no_clausura_multiestado():
    r = run_sv_analysis(['U', 'U', 'U'])
    assert r['verdict'] == 'INDETERMINADO'
    assert all(x == 'U' for x in r['residuals'])
