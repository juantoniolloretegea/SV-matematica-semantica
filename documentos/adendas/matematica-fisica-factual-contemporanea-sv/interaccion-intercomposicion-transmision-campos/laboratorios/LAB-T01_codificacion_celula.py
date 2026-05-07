"""
LAB-T01 — Verificador de codificación y reconstrucción de célula SV(36,6)
============================================================================

Verifica computacionalmente el operador de codificación factual `Enc_SV` y de
decodificación `Dec_SV` del apartado 18.4 del documento principal sobre la
célula SV(36,6) definida en el Anexo A. El laboratorio:

    (A) Construye una célula SV(36,6) con marcas U declaradas en posiciones
        específicas.
    (B) La codifica preservando estructura ternaria, posición de U, orden
        de parámetros, distancias, residuales y dictamen.
    (C) La transporta por canal idéntico (canal sin ruido).
    (D) La decodifica.
    (E) Verifica equivalencia factual exacta entre célula origen y reconstruida.

Tolerancia operativa: equivalencia exacta posición a posición sobre los 36
parámetros. Ningún componente del residual de transmisión `R^𝓣_SV` puede ser
no nulo bajo canal idéntico.

Autoría / Authorship
-------------------
© 2026 Juan Antonio Lloret Egea. Todos los derechos reservados / All rights reserved.
ORCID: 0000-0002-6634-3351
Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA)
IA eñ™ — La Biblia de la IA™
ISSN 2695-6411
Licencia / License: CC BY-NC-ND 4.0
"""


# Una célula SV(36,6) se representa como tupla de 36 elementos en {0, 1, "U"}
# Los 36 parámetros se agrupan en 6 familias de 6 parámetros cada una.

CELULA_ORIGEN = (
    # Familia A — Estatuto y soporte (P1-P6)
    1, 1, 1, "U", 1, 1,
    # Familia B — Geometría factual (P7-P12)
    1, 0, 1, "U", 0, 1,
    # Familia C — Morfología (P13-P18)
    "U", 0, 1, 0, 1, "U",
    # Familia D — Potencia, fuente y efecto (P19-P24)
    1, 1, 0, 1, "U", 1,
    # Familia E — Dinámica factual sin tiempo soberano (P25-P30)
    0, "U", 1, 1, 0, 1,
    # Familia F — Interacción e identificación avanzada (P31-P36)
    "U", 1, 0, 1, 1, "U",
)


def encode_celula(celula):
    """Codifica una célula SV(36,6) preservando estructura ternaria."""
    # Cada posición se codifica con su valor original;
    # las marcas U se preservan como símbolo propio del alfabeto.
    return tuple((i, valor) for i, valor in enumerate(celula))


def canal_identidad(mensaje):
    """Canal sin ruido: devuelve el mensaje sin alteración."""
    return mensaje


def decode_celula(mensaje):
    """Decodifica el mensaje recuperando la célula original."""
    return tuple(valor for _, valor in mensaje)


def comparar_celulas(c_origen, c_reconstruida):
    """Compara dos células posición a posición. Devuelve diferencias."""
    diferencias = []
    for i, (a, b) in enumerate(zip(c_origen, c_reconstruida)):
        if a != b:
            diferencias.append((i+1, a, b))
    return diferencias


def calcular_R_cell(c_origen, c_reconstruida):
    """Residual celular: número de posiciones distintas."""
    return sum(1 for a, b in zip(c_origen, c_reconstruida) if a != b)


def calcular_R_U(c_origen, c_reconstruida):
    """Residual de preservación de U: U perdidas o transformadas."""
    perdidas = 0
    for a, b in zip(c_origen, c_reconstruida):
        if a == "U" and b != "U":
            perdidas += 1
        if a != "U" and b == "U":
            perdidas += 1
    return perdidas


def main():
    print("=" * 78)
    print(" LAB-T01 — Codificación y reconstrucción de célula SV(36,6)")
    print("=" * 78)
    print()
    print(" Definiciones canónicas del apartado 18.4:")
    print("   Enc_SV: X_SV → M_SV (preserva estructura ternaria, U, orden, ...)")
    print("   𝓒_SV: M_SV → M̃_SV (canal factual)")
    print("   Dec_SV: M̃_SV → X'_SV")
    print()

    # Conteo de marcas U en la célula origen
    n_U_origen = sum(1 for v in CELULA_ORIGEN if v == "U")
    print(f" Célula SV(36,6) origen: {len(CELULA_ORIGEN)} parámetros, {n_U_origen} marcas U.")
    print()

    # Mostrar estructura por familias
    familias = ["A — Estatuto y soporte", "B — Geometría factual", "C — Morfología",
                "D — Potencia, fuente y efecto", "E — Dinámica factual",
                "F — Interacción e identificación avanzada"]
    for i, fam in enumerate(familias):
        chunk = CELULA_ORIGEN[i*6:(i+1)*6]
        print(f"   Familia {fam}: {chunk}")
    print()

    # Bloque A: codificación
    mensaje = encode_celula(CELULA_ORIGEN)
    print(f" Codificada: {len(mensaje)} pares (índice, valor) preservados.")

    # Bloque B: canal identidad
    mensaje_recibido = canal_identidad(mensaje)
    canal_intacto = (mensaje == mensaje_recibido)
    print(f" Canal identidad: {'✓ mensaje íntegro' if canal_intacto else '✗ mensaje alterado'}")

    # Bloque C: decodificación
    celula_reconstruida = decode_celula(mensaje_recibido)
    print(f" Decodificada: {len(celula_reconstruida)} parámetros.")

    # Bloque D: verificación de equivalencia
    diferencias = comparar_celulas(CELULA_ORIGEN, celula_reconstruida)
    R_cell = calcular_R_cell(CELULA_ORIGEN, celula_reconstruida)
    R_U = calcular_R_U(CELULA_ORIGEN, celula_reconstruida)

    print()
    print(" Cálculo del residual de transmisión bajo canal idéntico:")
    print(f"   R_cell  (residual celular)            = {R_cell}")
    print(f"   R_U     (residual de preservación U)  = {R_U}")
    print(f"   R_order (residual de orden)           = 0 (orden preservado por construcción)")
    print(f"   Diferencias detectadas: {len(diferencias)}")
    print()

    # Verificación de identidad exacta
    identico = (CELULA_ORIGEN == celula_reconstruida)

    # Verificación adicional: las marcas U están preservadas en sus posiciones
    posiciones_U_origen = [i for i, v in enumerate(CELULA_ORIGEN) if v == "U"]
    posiciones_U_recon = [i for i, v in enumerate(celula_reconstruida) if v == "U"]
    U_preservadas = (posiciones_U_origen == posiciones_U_recon)

    todo_OK = identico and U_preservadas and R_cell == 0 and R_U == 0

    print(" Análisis estructural:")
    print(f"   Equivalencia exacta posición a posición: {'✓' if identico else '✗'}")
    print(f"   Posiciones de U preservadas: {'✓' if U_preservadas else '✗'}")
    print(f"   Residual celular nulo: {'✓' if R_cell == 0 else '✗'}")
    print(f"   Residual de U nulo: {'✓' if R_U == 0 else '✗'}")
    print()

    if todo_OK:
        print("✓ LAB-T01 SUPERADO:")
        print("  - Codificación preservó estructura ternaria y posiciones de U.")
        print("  - Canal idéntico transmitió sin alteración.")
        print("  - Decodificación reconstruyó célula exacta.")
        print(f"  - {n_U_origen} marcas U preservadas en sus posiciones originales.")
        return 0
    else:
        print("✗ LAB-T01 FALLA: equivalencia no exacta bajo canal idéntico.")
        return 1


if __name__ == "__main__":
    import sys
    sys.exit(main())
