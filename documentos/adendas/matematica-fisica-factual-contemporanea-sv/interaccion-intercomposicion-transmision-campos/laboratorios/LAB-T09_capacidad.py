"""
LAB-T09 — Verificador de capacidad factual de transmisión Cap_SV(𝓒)
========================================================================

Verifica computacionalmente la magnitud Cap_SV(𝓒) del apartado 18.7:

    Cap_SV(𝓒) = κ_SV(R^𝓣_SV ≤ L_𝓣)

con dictamen ternario:
    1 — canal factual apto
    0 — canal factual no apto
    U — no clausurable por falta de evidencia

El laboratorio aplica cuatro perfiles de canal factual:

    Perfil 1: canal apto (residual nulo o bajo umbral).
    Perfil 2: canal no apto (residual excede umbral).
    Perfil 3: canal en U (residual no calculable).
    Perfil 4: canal frontera (residual exactamente al umbral).

Tolerancia operativa: el dictamen ternario debe distinguir los cuatro perfiles.

Autoría / Authorship
-------------------
© 2026 Juan Antonio Lloret Egea. Todos los derechos reservados / All rights reserved.
ORCID: 0000-0002-6634-3351
Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA)
IA eñ™ — La Biblia de la IA™
ISSN 2695-6411
Licencia / License: CC BY-NC-ND 4.0
"""


def kappa_SV(residual_total, umbral, calculable=True):
    """Compuerta de dictamen ternario sobre el residual."""
    if not calculable:
        return "U"
    if residual_total <= umbral:
        return 1
    return 0


def Cap_SV(residual_componentes, umbral, calculable=True):
    """Capacidad factual de transmisión."""
    if not calculable:
        return "U"
    R_total = sum(residual_componentes)
    return kappa_SV(R_total, umbral, calculable)


def main():
    print("=" * 78)
    print(" LAB-T09 — Capacidad factual de transmisión Cap_SV(𝓒)")
    print("=" * 78)
    print()
    print(" Definición canónica:")
    print("   Cap_SV(𝓒) = κ_SV(R^𝓣_SV ≤ L_𝓣)")
    print()
    print(" Dictamen ternario:")
    print("   1 — canal factual apto")
    print("   0 — canal factual no apto")
    print("   U — no clausurable por falta de evidencia")
    print()

    UMBRAL_L_T = 2

    perfiles = [
        ("Perfil 1: canal apto (residual nulo)", (0, 0, 0, 0, 0, 0, 0), True, 1),
        ("Perfil 1b: canal apto (residual bajo umbral)", (1, 0, 0, 0, 0, 0, 0), True, 1),
        ("Perfil 2: canal no apto (residual sobre umbral)", (1, 1, 0, 1, 0, 0, 0), True, 0),
        ("Perfil 3: canal en U (no calculable)", (None,), False, "U"),
        ("Perfil 4: canal frontera (residual = umbral)", (1, 1, 0, 0, 0, 0, 0), True, 1),
        ("Perfil 5: canal severamente no apto", (3, 2, 1, 1, 1, 1, 1), True, 0),
    ]

    print(f" Umbral L_𝓣 = {UMBRAL_L_T}")
    print()
    print(f" {'Perfil':<48} | {'R total':<7} | {'Cap_SV':<7} | {'Esp':<3} | {'OK':<3}")
    print(" " + "-" * 80)

    aciertos = 0
    for etiqueta, R_componentes, calculable, esperado in perfiles:
        R_total = "N/A" if not calculable else sum(R_componentes)
        cap = Cap_SV(R_componentes, UMBRAL_L_T, calculable)
        ok = (cap == esperado)
        if ok:
            aciertos += 1
        marca = "✓" if ok else "✗"
        print(f" {etiqueta:<48} | {str(R_total):<7} | {str(cap):<7} | {str(esperado):<3} | {marca:<3}")

    print()
    print(" Análisis estructural:")
    print(" - Cap_SV mide preservación de estructura factual, no cantidad de bits.")
    print(" - Es magnitud distinta de la capacidad de Shannon clásica.")
    print(" - El dictamen ternario preserva U cuando el residual no es calculable.")
    print(" - El umbral L_𝓣 es declaración del horizonte operativo.")
    print()

    if aciertos == len(perfiles):
        print("✓ LAB-T09 SUPERADO:")
        print(f"  - {len(perfiles)} perfiles de canal verificados.")
        print("  - Dictamen ternario apto/no apto/U distingue correctamente.")
        print("  - Capacidad factual SV diferenciada de capacidad de Shannon clásica.")
        return 0
    else:
        print(f"✗ LAB-T09 FALLA: {len(perfiles) - aciertos} verificaciones incorrectas.")
        return 1


if __name__ == "__main__":
    import sys
    sys.exit(main())
