# Prueba test_postfrontier.py
# Autor: Juan Antonio Lloret Egea
# ORCID: 0000-0002-6634-3351
# Derechos: © 2026. Todos los derechos reservados.
# Licencia: CC BY-NC-ND 4.0
# Fecha: Madrid, 10/05/2026
from src.sv_core import postfrontier, mn2_is_not_u

def test_postfrontier_mn2():
    assert postfrontier(0,0,0,'M_N2-SV')['dictamen'] == 'APTO'
    assert postfrontier(0,0,0,'U')['error'] == 'BH-UPOST-001'
    assert mn2_is_not_u()
