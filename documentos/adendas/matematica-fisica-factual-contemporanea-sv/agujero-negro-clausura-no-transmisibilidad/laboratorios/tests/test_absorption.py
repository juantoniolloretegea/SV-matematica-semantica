# Prueba test_absorption.py
# Autor: Juan Antonio Lloret Egea
# ORCID: 0000-0002-6634-3351
# Derechos: © 2026. Todos los derechos reservados.
# Licencia: CC BY-NC-ND 4.0
# Fecha: Madrid, 10/05/2026
from src.absorption import classify_absorption

def test_absorption():
    assert classify_absorption([0,0,0,0,0,0,0,0,0], 'Schwarzschild')['dictamen_absorcion'] == 'ABSORBIDO'
    assert classify_absorption([1,1,1,1,1,1,1,1,1], 'singularidad primaria')['dictamen_absorcion'] == 'RECHAZADO'
