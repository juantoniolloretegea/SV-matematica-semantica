# Prueba test_core.py
# Autor: Juan Antonio Lloret Egea
# ORCID: 0000-0002-6634-3351
# Derechos: © 2026. Todos los derechos reservados.
# Licencia: CC BY-NC-ND 4.0
# Fecha: Madrid, 10/05/2026
from src.sv_core import threshold, d_sigma

def test_threshold():
    assert threshold(9) == 7
    assert threshold(36) == 28

def test_dsigma():
    assert d_sigma([1,1,1,1,1,1,1,0,0])['DΣ'] == 'NO_APTO'
    assert d_sigma([0,0,0,0,0,0,0,1,1])['DΣ'] == 'APTO'
