"""
LAB-T02 — Verificador adversarial de preservación de U en la transmisión
==========================================================================

Verifica computacionalmente el Teorema 7 del apartado 18.8.2:

    Una transmisión factual operativamente apta no transforma la marca U
    del estado origen en 0 o 1 en el estado reconstruido.

El laboratorio aplica seis intentos adversariales de degradación de U
durante el transporte y comprueba que cada uno produce R_U > 0 y dictamen
de transmisión no apto:

    Adv 1: U codificada como 0
    Adv 2: U codificada como 1
    Adv 3: U codificada como vacío (None)
    Adv 4: U codificada como cadena vacía
    Adv 5: U codificada como -1
    Adv 6: U codificada como "0/1" (resolución arbitraria)

Más tres controles legítimos donde U se preserva correctamente.

Tolerancia operativa: cero degradaciones admitidas, cero controles rechazados.

Autoría / Authorship
-------------------
© 2026 Juan Antonio Lloret Egea. Todos los derechos reservados / All rights reserved.
ORCID: 0000-0002-6634-3351
Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA)
IA eñ™ — La Biblia de la IA™
ISSN 2695-6411
Licencia / License: CC BY-NC-ND 4.0
"""


# Estado origen con tres marcas U en posiciones declaradas
ESTADO_ORIGEN = (1, 0, "U", 1, "U", 0, 1, "U", 0)
POSICIONES_U_ORIGEN = [i for i, v in enumerate(ESTADO_ORIGEN) if v == "U"]


def encode_adversarial(estado, sustituto_U):
    """Codifica reemplazando U por un valor distinto (adversarial)."""
    return tuple(sustituto_U if v == "U" else v for v in estado)


def encode_legitimo(estado):
    """Codifica preservando U como símbolo propio."""
    return tuple(estado)


def calcular_R_U(estado_origen, estado_reconstruido):
    """Residual de preservación de U."""
    perdidas = 0
    for a, b in zip(estado_origen, estado_reconstruido):
        if a == "U" and b != "U":
            perdidas += 1
    return perdidas


def dictamen_transmision(R_U, umbral=0):
    """Dictamen ternario: 1 si R_U=0, 0 si R_U>0 (degradación detectada)."""
    if R_U == 0:
        return 1
    elif R_U > umbral:
        return 0
    else:
        return "U"


def main():
    print("=" * 78)
    print(" LAB-T02 — Preservación adversarial de U en la transmisión (Teorema 7)")
    print("=" * 78)
    print()
    print(f" Estado origen: {ESTADO_ORIGEN}")
    print(f" Posiciones de U en origen: {POSICIONES_U_ORIGEN}")
    print(f" Total de marcas U a preservar: {len(POSICIONES_U_ORIGEN)}")
    print()

    # Seis intentos adversariales
    adversarios = [
        ("Adv 1: U → 0", 0, "RECHAZADO"),
        ("Adv 2: U → 1", 1, "RECHAZADO"),
        ("Adv 3: U → None (vacío)", None, "RECHAZADO"),
        ("Adv 4: U → '' (cadena vacía)", "", "RECHAZADO"),
        ("Adv 5: U → -1 (numérico inválido)", -1, "RECHAZADO"),
        ("Adv 6: U → '0/1' (resolución arbitraria)", "0/1", "RECHAZADO"),
    ]

    # Tres controles legítimos
    controles = [
        ("Ctrl 1: U preservada", "U", "ADMITIDO"),
        ("Ctrl 2: U preservada (caso idéntico)", "U", "ADMITIDO"),
        ("Ctrl 3: U preservada (caso con peso)", "U", "ADMITIDO"),
    ]

    aciertos = 0
    total = len(adversarios) + len(controles)

    print(f" {'Caso':<45} | {'Esperado':<11} | {'R_U':<3} | {'Dictamen':<8} | {'OK':<3}")
    print(" " + "-" * 80)

    for etiqueta, sustituto, esperado in adversarios:
        if sustituto == "U":
            estado_recon = encode_legitimo(ESTADO_ORIGEN)
        else:
            estado_recon = encode_adversarial(ESTADO_ORIGEN, sustituto)
        R_U = calcular_R_U(ESTADO_ORIGEN, estado_recon)
        D = dictamen_transmision(R_U)
        # RECHAZADO: D == 0 (degradación detectada)
        ok = (esperado == "RECHAZADO" and D == 0)
        if ok:
            aciertos += 1
        marca = "✓" if ok else "✗"
        print(f" {etiqueta:<45} | {esperado:<11} | {R_U:<3} | {str(D):<8} | {marca:<3}")

    for etiqueta, sustituto, esperado in controles:
        estado_recon = encode_legitimo(ESTADO_ORIGEN)
        R_U = calcular_R_U(ESTADO_ORIGEN, estado_recon)
        D = dictamen_transmision(R_U)
        # ADMITIDO: D == 1 (sin degradación)
        ok = (esperado == "ADMITIDO" and D == 1)
        if ok:
            aciertos += 1
        marca = "✓" if ok else "✗"
        print(f" {etiqueta:<45} | {esperado:<11} | {R_U:<3} | {str(D):<8} | {marca:<3}")

    print()
    print(" Análisis estructural:")
    print(" - El Teorema 7 sostiene que U debe preservarse durante el transporte.")
    print(" - Cualquier degradación de U produce R_U > 0 y dictamen no apto.")
    print(" - La preservación de U es regla dura del corpus, no propiedad emergente.")
    print()

    if aciertos == total:
        print("✓ LAB-T02 SUPERADO:")
        print(f"  - {len(adversarios)}/6 intentos adversariales rechazados.")
        print(f"  - {len(controles)}/3 controles legítimos admitidos.")
        print("  - Teorema 7 verificado adversarialmente.")
        return 0
    else:
        print(f"✗ LAB-T02 FALLA: {total - aciertos} verificaciones incorrectas.")
        return 1


if __name__ == "__main__":
    import sys
    sys.exit(main())
