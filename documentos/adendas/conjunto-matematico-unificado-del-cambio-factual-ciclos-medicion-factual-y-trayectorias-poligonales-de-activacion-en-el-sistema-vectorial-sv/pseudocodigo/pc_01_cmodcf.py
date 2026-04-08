# Autoría: Juan Antonio Lloret Egea | ORCID: 0000-0002-6634-3351 | Institución: Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA) | Publicación: IA eñ™ — La Biblia de la IA™ | ISSN: 2695-6411 | Licencia: CC BY-NC-ND 4.0 | Lugar y fecha: Madrid, 2026
"""
Pseudocódigo Python — CMODCF-SV.

Objetivo:
- decidir directriz mínima,
- decidir detonación mínima,
- clasificar el tramo: act / neu / ago / 0.

def evaluar_tramo(alpha, delta, beta, rho, estatuto_detonante):
    D = -alpha*delta + beta*rho
    E = alpha*delta - beta*rho

    if not estatuto_detonante:
        if D == 0 and delta == 0 and rho == 0:
            return "neutralidad_trivial"
        return "no_detonante"

    if delta > 0 and E > 0:
        return "act"
    if delta > 0 and rho > 0 and E == 0:
        return "neu"
    if delta == 0 and rho == 0 and D == 0:
        return "ago"
    return "no_clausurado"
"""
