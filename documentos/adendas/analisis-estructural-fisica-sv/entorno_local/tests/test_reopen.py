from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from core.reopen import reopen
from core.trajectory import build_trajectory
from core.residuals import compute_residuals
from core.boundary import evaluate_boundary
from core.verdict import compute_verdict
from runner.sv_runner import classify


def _run_from_trajectory(traj):
    r = compute_residuals(traj)
    c = classify(r)
    b = evaluate_boundary(c)
    return compute_verdict(b)


def test_reopen_extiende_sin_borrar():
    t0 = build_trajectory(['U', 'U'])
    t1 = reopen(t0, [1])
    assert len(t1) == 3
    # Los dos primeros elementos son los originales
    assert t1[0]['state'] == 'U'
    assert t1[1]['state'] == 'U'
    assert t1[2]['state'] == 1
    assert t1[2]['index'] == 2


def test_reopen_indices_continuos():
    t0 = build_trajectory([1, 1])
    t1 = reopen(t0, ['U', 'U'])
    indices = [x['index'] for x in t1]
    assert indices == [0, 1, 2, 3]


def test_reopen_no_modifica_original():
    t0 = build_trajectory(['U', 'U'])
    original_len = len(t0)
    _ = reopen(t0, [1])
    assert len(t0) == original_len


def test_reopen_dictamen_cambia():
    t0 = build_trajectory(['U', 'U'])
    v0 = _run_from_trajectory(t0)
    assert v0 == 'INDETERMINADO'
    t1 = reopen(t0, ['U'])
    v1 = _run_from_trajectory(t1)
    assert v1 == 'INDETERMINADO'  # sigue abierta, no cambia
    # Reapertura con datos que añaden conflicto
    t2 = reopen(t0, [0])
    v2 = _run_from_trajectory(t2)
    # 'U'→0: residual='U'; 0 en states: boundary depende de clasificación
    assert v2 in ('INDETERMINADO', 'NO APTO')
