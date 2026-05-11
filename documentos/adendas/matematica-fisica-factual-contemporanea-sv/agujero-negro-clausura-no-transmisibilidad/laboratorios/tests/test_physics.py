# Prueba test_physics.py
# Autor: Juan Antonio Lloret Egea
# ORCID: 0000-0002-6634-3351
# Derechos: © 2026. Todos los derechos reservados.
# Licencia: CC BY-NC-ND 4.0
# Fecha: Madrid, 10/05/2026
from src.bh_physics import schwarzschild_radius, M_solar, kerr_r_plus_over_rg

def test_schwarzschild_radius():
    rs = schwarzschild_radius(M_solar) / 1000
    assert 2.95 < rs < 2.96

def test_kerr():
    assert kerr_r_plus_over_rg(1.1) is None
    assert kerr_r_plus_over_rg(0.0) == 2.0
