# Cálculos físicos externos absorbidos por SV-BH9
# Autor: Juan Antonio Lloret Egea
# ORCID: 0000-0002-6634-3351
# Derechos: © 2026. Todos los derechos reservados.
# Licencia: CC BY-NC-ND 4.0
# Fecha: Madrid, 10/05/2026
# Publicación: El agujero negro como cierre interno sin resto exterior formulable


from __future__ import annotations
import math
from typing import Dict, Any

G = 6.67430e-11
c = 299792458.0
hbar = 1.054571817e-34
k_B = 1.380649e-23
M_solar = 1.98847e30


def schwarzschild_radius(mass_kg: float) -> float:
    return 2 * G * mass_kg / (c ** 2)


def horizon_area(rs: float) -> float:
    return 4 * math.pi * rs * rs


def planck_length() -> float:
    return math.sqrt(hbar * G / (c ** 3))


def entropy_dimensionless(area: float) -> float:
    lp = planck_length()
    return area / (4 * lp * lp)


def hawking_temperature(mass_kg: float) -> float:
    return hbar * c**3 / (8 * math.pi * G * mass_kg * k_B)


def thermo_row(solar_masses: float) -> Dict[str, float]:
    m = solar_masses * M_solar
    rs = schwarzschild_radius(m)
    area = horizon_area(rs)
    return {
        'mass_kg': m,
        'r_s_m': rs,
        'r_s_km': rs / 1000,
        'r_s_AU': rs / 1.495978707e11,
        'area_m2': area,
        'S_BH_over_kB': entropy_dimensionless(area),
        'T_H_K': hawking_temperature(m),
    }


def escape_ratio(q: float) -> float:
    if q <= 0:
        return float('inf')
    return math.sqrt(1 / q)


def schwarzschild_cell(q: float) -> list:
    if q <= 1:
        return [1,1,1,1,1,1,1,1,0] if q < 1 else [1,1,1,1,1,1,1,0,0]
    return [0,0,0,0,0,0,0,1,1]


def kerr_r_plus_over_rg(chi: float) -> Any:
    if abs(chi) > 1:
        return None
    return 1 + math.sqrt(1 - chi*chi)


def kretschmann_ratio(q: float) -> Any:
    if q == 0:
        return None
    if q < 0:
        raise ValueError('radio normalizado negativo')
    return (1 / q) ** 6
