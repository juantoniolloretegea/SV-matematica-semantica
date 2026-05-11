# Clasificación de absorción de modelos contemporáneos
# Autor: Juan Antonio Lloret Egea
# ORCID: 0000-0002-6634-3351
# Derechos: © 2026. Todos los derechos reservados.
# Licencia: CC BY-NC-ND 4.0
# Fecha: Madrid, 10/05/2026
# Publicación: El agujero negro como cierre interno sin resto exterior formulable


from __future__ import annotations
from typing import Dict, Any, Iterable
from .sv_core import d_sigma


def classify_absorption(cell: Iterable[Any], model: str = '') -> Dict[str, Any]:
    d = d_sigma(cell)
    n0, n1, nu = d['N0'], d['N1'], d['NU']
    if d['DΣ'] == 'NO_APTO':
        if 'singularidad' in model.lower():
            label = 'RECHAZADO'
            error = 'BH-SING-001'
        elif 'salida luminosa' in model.lower():
            label = 'RECHAZADO'
            error = 'BH-LUZ-002'
        else:
            label = 'RECHAZADO'
            error = 'BH-ABS-001'
    elif d['DΣ'] == 'APTO' and nu <= 2:
        label = 'ABSORBIDO'
        error = None
    else:
        label = 'ABSORBIDO_PARCIALMENTE'
        error = None
    return {**d, 'modelo': model, 'dictamen_absorcion': label, 'error': error}
