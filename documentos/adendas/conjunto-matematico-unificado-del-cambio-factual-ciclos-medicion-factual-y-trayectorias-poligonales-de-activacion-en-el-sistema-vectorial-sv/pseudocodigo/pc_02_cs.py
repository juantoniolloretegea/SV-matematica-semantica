# Autoría: Juan Antonio Lloret Egea | ORCID: 0000-0002-6634-3351 | Institución: Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA) | Publicación: IA eñ™ — La Biblia de la IA™ | ISSN: 2695-6411 | Licencia: CC BY-NC-ND 4.0 | Lugar y fecha: Madrid, 2026
"""
Pseudocódigo Python — Ciclo de Suceso.

def es_ciclo(phi):
    return phi[0] == phi[-1]

def condicion_necesaria_cs(phi):
    M = diferencias(phi)
    return sum(M) == 0

def descriptor_ciclico(phi):
    if not es_ciclo(phi):
        raise ValueError("No es ciclo")
    return area(phi), max(phi), norma1(diferencias(phi))

def cota_condicionada(phi):
    phi0 = phi[0]
    if all(v >= phi0 for v in phi):
        return area(phi) >= (len(phi)-1)*phi0
    return "fuera_de_hipotesis"
"""
