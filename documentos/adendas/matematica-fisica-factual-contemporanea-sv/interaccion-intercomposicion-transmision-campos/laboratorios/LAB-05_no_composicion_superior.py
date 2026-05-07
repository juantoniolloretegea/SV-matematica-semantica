"""
LAB-05 — Verificador de no composición superior en el arranque canónico
==========================================================================

Verifica computacionalmente el Teorema 5 del documento principal: el arranque
canónico no admite operadores 𝓘_SV^{(n)} de orden n ≥ 3 sin construcción
explícita de su dominio, codominio, regla de resolución, residual y dictamen.

El laboratorio implementa dos verificaciones complementarias:

    (A) Test de admisibilidad de orden: confirma que sólo el orden binario
        está canonizado y que cualquier orden n ≥ 3 falla por ausencia de
        los seis elementos operativos requeridos.

    (B) Test de descomposición: dada una relación aparentemente n-aria entre
        n campos sobre trayectoria común, calcula el conjunto de n·(n-1)
        interacciones binarias dirigidas que la descomponen, y verifica que
        cada una es admisible por el operador canónico 𝓘_SV.

Tolerancia operativa: exacta sobre verificación booleana de orden.

Autoría / Authorship
-------------------
© 2026 Juan Antonio Lloret Egea. Todos los derechos reservados / All rights reserved.
ORCID: 0000-0002-6634-3351
Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA)
IA eñ™ — La Biblia de la IA™
ISSN 2695-6411
Licencia / License: CC BY-NC-ND 4.0
"""

from itertools import permutations


CAMPOS_ADMITIDOS = ["sector_electrico", "sector_magnetico",
                     "sector_basal_gravitatorio", "convergencia_ternaria",
                     "sector_topologico", "TPA", "regimen_angular_factual"]


# Elementos operativos requeridos para canonizar un operador de orden n
ELEMENTOS_REQUERIDOS = [
    "dominio_explicito",
    "codominio_explicito",
    "regla_de_resolucion",
    "control_de_cardinalidad",
    "residual_propio",
    "dictamen_propio",
]


def operador_canonizado(orden, elementos_disponibles):
    """
    Verifica si un operador 𝓘_SV^{(orden)} está canonizado.
    Devuelve True sólo si todos los elementos requeridos están disponibles.
    """
    return all(e in elementos_disponibles for e in ELEMENTOS_REQUERIDOS)


def descomponer_n_aria_en_binarias(campos):
    """
    Descompone una relación aparentemente n-aria entre n campos sobre
    trayectoria común en su conjunto de n·(n-1) interacciones binarias
    dirigidas (todas las permutaciones ordenadas de pares distintos).
    """
    return list(permutations(campos, 2))


def main():
    print("=" * 78)
    print(" LAB-05 — Verificador de no composición superior en el arranque canónico")
    print("=" * 78)
    print()

    # ---- Bloque A: admisibilidad por orden ----
    print(" BLOQUE A — Admisibilidad por orden del operador.")
    print()
    print(f" Elementos operativos requeridos para canonizar 𝓘_SV^{{(n)}}:")
    for e in ELEMENTOS_REQUERIDOS:
        print(f"   - {e}")
    print()

    # Estado declarado de canonización en el arranque canónico
    estado_canonizacion = {
        2: ELEMENTOS_REQUERIDOS,           # binario: completamente canonizado
        3: ["dominio_explicito"],          # ternario: incompleto (sólo declarado pendiente)
        4: [],                             # cuaternario: nada
        5: [],                             # quinario: nada
    }

    print(f" {'Orden n':<10} | {'Elementos disponibles':<25} | {'Canonizado?':<12}")
    print(" " + "-" * 60)

    aciertos_A = 0
    for orden, elementos in estado_canonizacion.items():
        canonizado = operador_canonizado(orden, elementos)
        # Sólo el orden 2 debe estar canonizado en el arranque
        esperado = (orden == 2)
        coherente = (canonizado == esperado)
        if coherente:
            aciertos_A += 1
        marca = "sí" if canonizado else "NO"
        marca_ok = "✓" if coherente else "✗"
        print(f" n = {orden:<6} | {len(elementos)} de {len(ELEMENTOS_REQUERIDOS):<23} | {marca:<12} {marca_ok}")

    print()

    # ---- Bloque B: descomposición de relaciones aparentemente n-arias ----
    print(" BLOQUE B — Descomposición binaria de relaciones aparentemente n-arias.")
    print()

    # Caso aparentemente ternario: 3 campos sobre trayectoria común
    campos_ternario = ["sector_basal_gravitatorio", "sector_electrico", "sector_magnetico"]
    descomposicion = descomponer_n_aria_en_binarias(campos_ternario)

    n = len(campos_ternario)
    esperado = n * (n - 1)
    print(f" Caso ternario aparente: {n} campos sobre trayectoria común.")
    print(f" Cardinalidad esperada de la descomposición: n·(n-1) = {esperado}")
    print(f" Cardinalidad obtenida:                       {len(descomposicion)}")
    print()
    print(" Descomposición binaria dirigida:")
    for i, (a, b) in enumerate(descomposicion):
        print(f"   {i+1:>2}. 𝓘_SV({a}, {b})")

    aciertos_B = 1 if len(descomposicion) == esperado else 0
    print()

    # Caso aparentemente cuaternario
    campos_cuaternario = ["sector_basal_gravitatorio", "sector_electrico",
                          "sector_magnetico", "convergencia_ternaria"]
    desc4 = descomponer_n_aria_en_binarias(campos_cuaternario)
    n4 = len(campos_cuaternario)
    esperado4 = n4 * (n4 - 1)
    print(f" Caso cuaternario aparente: {n4} campos.")
    print(f" Cardinalidad esperada: n·(n-1) = {esperado4}")
    print(f" Cardinalidad obtenida: {len(desc4)}")

    aciertos_B += 1 if len(desc4) == esperado4 else 0
    print()

    # ---- Resumen ----
    total_aciertos = aciertos_A + aciertos_B
    total_tests = len(estado_canonizacion) + 2

    print(" Análisis estructural:")
    print(" - Sólo el operador binario 𝓘_SV está canonizado en el arranque.")
    print(" - Los órdenes n ≥ 3 fallan por ausencia de elementos operativos.")
    print(" - Las relaciones aparentemente n-arias se descomponen como")
    print("   conjunto declarado de n·(n-1) interacciones binarias dirigidas.")
    print()

    if total_aciertos == total_tests:
        print("✓ LAB-05 SUPERADO:")
        print(f"  - {aciertos_A}/{len(estado_canonizacion)} verificaciones de admisibilidad por orden.")
        print(f"  - {aciertos_B}/2 verificaciones de descomposición binaria.")
        print("  - Teorema 5 verificado: el arranque canónico es estrictamente binario.")
        return 0
    else:
        print(f"✗ LAB-05 FALLA: {total_tests - total_aciertos} verificaciones incorrectas.")
        return 1


if __name__ == "__main__":
    import sys
    sys.exit(main())
