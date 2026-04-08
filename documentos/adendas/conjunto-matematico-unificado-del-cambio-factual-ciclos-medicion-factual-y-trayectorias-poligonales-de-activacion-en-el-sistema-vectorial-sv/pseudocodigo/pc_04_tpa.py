# Autoría: Juan Antonio Lloret Egea | ORCID: 0000-0002-6634-3351 | Institución: Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA) | Publicación: IA eñ™ — La Biblia de la IA™ | ISSN: 2695-6411 | Licencia: CC BY-NC-ND 4.0 | Lugar y fecha: Madrid, 2026
"""
Pseudocódigo Python — TPA.

def construir_tpa(phi):
    M = diferencias(phi)
    kappa = diferencias(M)
    A = area_trapezoidal(phi)
    Div = [-m for m in M]
    return {"phi": phi, "M": M, "kappa": kappa, "A": A, "Div": Div}

def auditar_tpa(phi):
    datos = construir_tpa(phi)
    comprobar_telescopia(datos)
    comprobar_gauss_sv(datos)
    comprobar_integral_compleja(datos)
    comprobar_tvmtpa(datos)
    return datos
"""
