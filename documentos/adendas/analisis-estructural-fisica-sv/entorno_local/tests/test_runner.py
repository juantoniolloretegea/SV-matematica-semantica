from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from runner.sv_runner import run_sv_analysis


def test_apto_exacto():
    r = run_sv_analysis([1, 1])
    assert r['verdict'] == 'APTO'
    assert r['boundary'] == 'CERRABLE'
    assert r['residuals'] == [0]


def test_no_apto_residual():
    r = run_sv_analysis([1, 0.8])
    assert r['verdict'] == 'NO APTO'
    assert r['boundary'] == 'NO_CERRABLE'
    assert r['residuals'] == [1]


def test_indeterminado_U():
    r = run_sv_analysis(['U', 'U'])
    assert r['verdict'] == 'INDETERMINADO'
    assert r['boundary'] == 'ABIERTA'
    assert r['residuals'] == ['U']


def test_mixto_1_U():
    r = run_sv_analysis([1, 1, 'U'])
    assert r['verdict'] == 'INDETERMINADO'
    assert r['residuals'] == [0, 'U']
    assert r['classification'] == [1, 'U']


def test_conflicto_con_U():
    r = run_sv_analysis([1, 0, 'U'])
    assert r['verdict'] == 'NO APTO'
    assert 0 in r['classification']


def test_tres_estados_apto():
    r = run_sv_analysis([1, 1, 1])
    assert r['verdict'] == 'APTO'
    assert r['residuals'] == [0, 0]
