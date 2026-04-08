# Autoría: Juan Antonio Lloret Egea | ORCID: 0000-0002-6634-3351 | Institución: Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA) | Publicación: IA eñ™ — La Biblia de la IA™ | ISSN: 2695-6411 | Licencia: CC BY-NC-ND 4.0 | Lugar y fecha: Madrid, 2026
"""
Pseudocódigo Python — Medidor factual de ciclo.

def unidad_elemental_mfc(total_referencia, n):
    q, r = divmod(total_referencia, n)
    return q, r

def trayectoria_referencia(phi0, n):
    return [phi0] * (n + 1)

def contraste_no_universal(phi_ref, phi_alt):
    return area(phi_alt) < area(phi_ref)
"""
