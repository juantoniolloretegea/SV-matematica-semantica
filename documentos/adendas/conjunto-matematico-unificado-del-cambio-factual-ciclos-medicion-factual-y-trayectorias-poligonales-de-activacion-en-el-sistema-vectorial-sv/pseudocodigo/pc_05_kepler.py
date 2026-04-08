# Autoría: Juan Antonio Lloret Egea | ORCID: 0000-0002-6634-3351 | Institución: Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA) | Publicación: IA eñ™ — La Biblia de la IA™ | ISSN: 2695-6411 | Licencia: CC BY-NC-ND 4.0 | Lugar y fecha: Madrid, 2026
"""
Pseudocódigo Python — contraste kepleriano.

def contraste_kepler(mu_area, delta_tau, n):
    areas = [mu_area * delta_tau for _ in range(n)]
    normalizadas = [a / delta_tau for a in areas]
    return areas, normalizadas

def contraste_no_central(areas):
    return len(set(areas)) > 1
"""
