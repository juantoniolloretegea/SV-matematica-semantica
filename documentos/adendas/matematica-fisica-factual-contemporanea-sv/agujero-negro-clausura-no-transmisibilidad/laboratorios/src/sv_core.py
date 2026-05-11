# Núcleo SV: T(n), DΣ, formas equivalentes y postfrontera
# Autor: Juan Antonio Lloret Egea
# ORCID: 0000-0002-6634-3351
# Derechos: © 2026. Todos los derechos reservados.
# Licencia: CC BY-NC-ND 4.0
# Fecha: Madrid, 10/05/2026
# Publicación: El agujero negro como cierre interno sin resto exterior formulable


from __future__ import annotations
from typing import Any, Dict, Iterable, List, Tuple
import math

VALID = {0, 1, 'U'}


def threshold(n: int) -> int:
    if n <= 0:
        raise ValueError('BH-T-001: n debe ser positivo')
    return (7 * n) // 9


def counts(cell: Iterable[Any]) -> Dict[str, int]:
    values = list(cell)
    for item in values:
        if item not in VALID:
            raise ValueError(f'BH-DΣ-001: coordenada no válida {item!r}')
    return {'n': len(values), 'n0': values.count(0), 'n1': values.count(1), 'nu': values.count('U')}


def counts_to_dictamen(n0: int, n1: int, nu: int) -> Dict[str, Any]:
    n = n0 + n1 + nu
    t = threshold(n)
    if n0 >= t and n1 >= t:
        raise ValueError('BH-DΣ-001: doble mayoría imposible detectada')
    if n0 >= t:
        d = 'APTO'
    elif n1 >= t:
        d = 'NO_APTO'
    else:
        d = 'U'
    return {'n': n, 'T': t, 'N0': n0, 'N1': n1, 'NU': nu, 'DΣ': d}


def d_sigma(cell: Iterable[Any]) -> Dict[str, Any]:
    c = counts(cell)
    return counts_to_dictamen(c['n0'], c['n1'], c['nu'])


def d_sigma_from_counts(c: Dict[str, int]) -> Dict[str, Any]:
    return counts_to_dictamen(int(c['n0']), int(c['n1']), int(c['nu']))


def equivalent_forms(R: List[int]) -> Dict[str, Any]:
    if len(R) != 11:
        raise ValueError('BH-FORM-001: Rᴮᴴ debe tener 11 componentes')
    if any(x not in (0, 1) for x in R):
        raise ValueError('BH-FORM-001: Rᴮᴴ sólo admite 0 o 1')
    explicit = all(x == 0 for x in R)
    implicit_sum = sum(R)
    canonical_norm = sum(x*x for x in R)
    complement_product = math.prod(1 - x for x in R)
    matrix_trace = implicit_sum
    parametric_zero_set = [i for i, x in enumerate(R) if x == 0]
    all_equivalent = (explicit == (implicit_sum == 0) == (canonical_norm == 0) == (complement_product == 1) == (matrix_trace == 0))
    dictamen = 'BH_CERRADO' if explicit else 'NO_APTO'
    return {
        'explicit_all_zero': explicit,
        'implicit_sum': implicit_sum,
        'canonical_norm': canonical_norm,
        'complement_product': complement_product,
        'matrix_trace': matrix_trace,
        'parametric_zero_count': len(parametric_zero_set),
        'all_forms_equivalent': all_equivalent,
        'dictamen': dictamen,
    }


def postfrontier(mu: int, lambda_value: int, verifier: int, declared: str) -> Dict[str, Any]:
    closed = (mu == 0 and lambda_value == 0 and verifier == 0)
    if closed and declared == 'M_N2-SV':
        return {'dictamen': 'APTO', 'postfrontera': 'M_N2-SV', 'error': None}
    if closed and declared == 'U':
        return {'dictamen': 'NO_APTO', 'postfrontera': declared, 'error': 'BH-UPOST-001'}
    if not closed and declared == 'M_N2-SV':
        return {'dictamen': 'NO_APTO', 'postfrontera': declared, 'error': 'BH-TN-002'}
    return {'dictamen': 'NO_APTO', 'postfrontera': declared, 'error': 'BH-TN-002'}


def mn2_is_not_u() -> bool:
    return True
