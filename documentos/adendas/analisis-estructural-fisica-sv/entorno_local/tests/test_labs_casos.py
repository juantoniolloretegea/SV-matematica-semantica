"""
Verificación de que todos los labs producen los 5 dictámenes esperados.
"""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import labs.metrologia_lab as met
import labs.electromagnetismo_lab as em
import labs.multidetector_lab as mul
import labs.particulas_lab as par
import labs.no_clausura_lab as nc


def _check(nombre, resultados, fallos):
    assert not fallos, f"Fallos en {nombre}: {fallos}"
    for caso, r in resultados.items():
        assert r['ok'], f"{nombre}/{caso}: {r}"


def test_metrologia_5_casos():
    resultados, fallos = met.run_all()
    assert len(resultados) == 5
    _check('metrologia', resultados, fallos)


def test_electromagnetismo_5_casos():
    resultados, fallos = em.run_all()
    assert len(resultados) == 5
    _check('electromagnetismo', resultados, fallos)


def test_multidetector_5_casos():
    resultados, fallos = mul.run_all()
    assert len(resultados) == 5
    _check('multidetector', resultados, fallos)


def test_particulas_5_casos():
    resultados, fallos = par.run_all()
    assert len(resultados) == 5
    _check('particulas', resultados, fallos)


def test_no_clausura_5_casos():
    resultados, fallos = nc.run_all()
    assert len(resultados) == 5
    _check('no_clausura', resultados, fallos)


def test_multidetector_casos_distintos():
    """Coincidencia parcial (INDETERMINADO) y correlacion aparente (NO APTO) deben diferir."""
    resultados, _ = mul.run_all()
    v_parcial = resultados['coincidencia_parcial']['dictamen_obtenido']
    v_correlacion = resultados['correlacion_aparente']['dictamen_obtenido']
    assert v_parcial != v_correlacion, (
        f"coincidencia_parcial ({v_parcial}) y "
        f"correlacion_aparente ({v_correlacion}) deben ser distintos"
    )
    assert v_parcial == 'INDETERMINADO'
    assert v_correlacion == 'NO APTO'
