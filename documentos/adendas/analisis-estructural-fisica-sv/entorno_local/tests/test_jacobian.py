from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from core.jacobian import compute_jacobian


def test_jacobian_estado_sensible():
    # [1, 0.95] → residual=1 → NO APTO. Perturbando index=1 a 0.95+0.1=1.05
    # sigue siendo NO APTO. Perturbando a 0.85 sigue NO APTO.
    # [1, 1] → APTO. Perturbando a [1, 1.1] → 1 ≠ 1.1 → residual=1 → NO APTO → sensible
    r = compute_jacobian([1, 1], epsilon=0.1)
    assert r['dictamen_base'] == 'APTO'
    assert 1 in r['estados_sensibles']  # el estado 1 es sensible


def test_jacobian_estado_U_no_perturbable():
    r = compute_jacobian(['U', 'U'])
    assert r['dictamen_base'] == 'INDETERMINADO'
    assert r['estados_sensibles'] == []
    for s in r['sensibilidades']:
        assert s['sensible'] is False


def test_jacobian_estructura():
    r = compute_jacobian([1, 1, 'U'])
    assert 'dictamen_base' in r
    assert 'estados_sensibles' in r
    assert 'sensibilidades' in r
    assert len(r['sensibilidades']) == 3


def test_jacobian_no_apto_estable():
    # [1, 0] → NO APTO. Perturbar index=0 a 1.1 → sigue NO APTO. Insensible.
    r = compute_jacobian([1, 0], epsilon=0.1)
    assert r['dictamen_base'] == 'NO APTO'
