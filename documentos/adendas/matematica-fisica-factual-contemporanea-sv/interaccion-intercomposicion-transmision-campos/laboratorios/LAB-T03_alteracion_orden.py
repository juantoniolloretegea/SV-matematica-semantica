"""
LAB-T03 — Verificador de alteración deliberada de orden de parámetros
========================================================================

Verifica computacionalmente que el residual de orden R_order detecta
alteraciones del orden de los 36 parámetros de la célula SV(36,6) durante
el transporte. El laboratorio aplica cuatro permutaciones controladas y
una identidad como control:

    Perm 1: intercambio de dos parámetros adyacentes (P1 ↔ P2).
    Perm 2: intercambio de dos familias enteras (Familia A ↔ Familia B).
    Perm 3: rotación de seis posiciones dentro de una familia.
    Perm 4: permutación aleatoria global.
    Ctrl  : permutación identidad (debe pasar sin residual).

Tolerancia operativa: R_order = 0 sólo bajo permutación identidad.
Cualquier permutación no identidad debe producir R_order > 0.

Autoría / Authorship
-------------------
© 2026 Juan Antonio Lloret Egea. Todos los derechos reservados / All rights reserved.
ORCID: 0000-0002-6634-3351
Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA)
IA eñ™ — La Biblia de la IA™
ISSN 2695-6411
Licencia / License: CC BY-NC-ND 4.0
"""

import random


# Célula SV(36,6) origen con valores distinguibles por posición
CELULA_ORIGEN = tuple(range(1, 37))  # P1=1, P2=2, ..., P36=36


def aplicar_permutacion(celula, permutacion):
    """Aplica una permutación a la célula. permutacion[i] es el nuevo índice del parámetro original i."""
    n = len(celula)
    resultado = [None] * n
    for i, p in enumerate(permutacion):
        resultado[p] = celula[i]
    return tuple(resultado)


def calcular_R_order(celula_origen, celula_reconstruida):
    """Residual de orden: número de posiciones donde el orden difiere."""
    return sum(1 for a, b in zip(celula_origen, celula_reconstruida) if a != b)


def main():
    print("=" * 78)
    print(" LAB-T03 — Alteración deliberada de orden de parámetros")
    print("=" * 78)
    print()
    print(f" Célula SV(36,6) origen: {CELULA_ORIGEN[:6]}... (36 parámetros)")
    print()

    # Identidad
    perm_id = list(range(36))

    # Perm 1: intercambio P1 ↔ P2
    perm_1 = perm_id.copy()
    perm_1[0], perm_1[1] = perm_1[1], perm_1[0]

    # Perm 2: intercambio de familias A (P1-P6) ↔ B (P7-P12)
    perm_2 = perm_id.copy()
    for i in range(6):
        perm_2[i], perm_2[i+6] = perm_2[i+6], perm_2[i]

    # Perm 3: rotación dentro de familia C (P13-P18)
    perm_3 = perm_id.copy()
    fam_C = [12, 13, 14, 15, 16, 17]
    rot = [13, 14, 15, 16, 17, 12]  # rotación de un paso
    for i, idx in enumerate(fam_C):
        perm_3[idx] = rot[i]

    # Perm 4: permutación aleatoria global con semilla fija
    rng = random.Random(42)
    perm_4 = perm_id.copy()
    rng.shuffle(perm_4)

    casos = [
        ("Ctrl: permutación identidad", perm_id, 0),  # esperado R_order = 0
        ("Perm 1: intercambio P1 ↔ P2", perm_1, "> 0"),
        ("Perm 2: intercambio Familia A ↔ Familia B", perm_2, "> 0"),
        ("Perm 3: rotación dentro de Familia C", perm_3, "> 0"),
        ("Perm 4: permutación aleatoria global", perm_4, "> 0"),
    ]

    print(f" {'Caso':<48} | {'R_order':<8} | {'Esperado':<10} | {'OK':<3}")
    print(" " + "-" * 80)

    aciertos = 0
    for etiqueta, perm, esperado in casos:
        celula_recon = aplicar_permutacion(CELULA_ORIGEN, perm)
        R_order = calcular_R_order(CELULA_ORIGEN, celula_recon)
        if esperado == 0:
            ok = (R_order == 0)
        else:
            ok = (R_order > 0)
        if ok:
            aciertos += 1
        marca = "✓" if ok else "✗"
        print(f" {etiqueta:<48} | {R_order:<8} | {str(esperado):<10} | {marca:<3}")

    print()
    print(" Análisis estructural:")
    print(" - El residual R_order detecta cualquier alteración del orden de parámetros.")
    print(" - Bajo permutación identidad, R_order = 0 (orden preservado).")
    print(" - Bajo cualquier permutación no trivial, R_order > 0.")
    print(" - El orden de los 36 parámetros es información estructural del corpus.")
    print()

    if aciertos == len(casos):
        print("✓ LAB-T03 SUPERADO:")
        print("  - Identidad → R_order = 0 (sin alteración).")
        print("  - 4/4 permutaciones detectadas con R_order > 0.")
        return 0
    else:
        print(f"✗ LAB-T03 FALLA: {len(casos) - aciertos} verificaciones incorrectas.")
        return 1


if __name__ == "__main__":
    import sys
    sys.exit(main())
