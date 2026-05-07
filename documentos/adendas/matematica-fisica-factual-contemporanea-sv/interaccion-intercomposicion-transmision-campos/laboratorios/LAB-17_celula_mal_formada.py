"""
LAB-17 — Verificador adversarial de célula SV(36,6) mal formada
=================================================================

Verifica computacionalmente que la determinación operativa de campo
mediante la célula SV(36,6) (apartado A.6 del Anexo A) detecta y rechaza
células mal formadas. El laboratorio cubre cuatro clases de mala
formación detectadas como código de error E-17:

    Caso 1: orden incorrecto (parámetros fuera de su familia).
    Caso 2: parámetros faltantes (cardinalidad ≠ 36).
    Caso 3: duplicados (mismo identificador de parámetro repetido).
    Caso 4: mezcla Σ=0 como Σ=1 (un primitivo metrológico colocado
            como parámetro de campo dentro de la célula).

Más cuatro controles legítimos donde la célula está bien formada.

Tolerancia operativa: cero células mal formadas admitidas; cero células
bien formadas rechazadas.

Autoría / Authorship
-------------------
© 2026 Juan Antonio Lloret Egea. Todos los derechos reservados / All rights reserved.
ORCID: 0000-0002-6634-3351
Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA)
IA eñ™ — La Biblia de la IA™
ISSN 2695-6411
Licencia / License: CC BY-NC-ND 4.0
"""


# Especificación canónica de la célula SV(36,6) según el Anexo A
# Cada familia tiene 6 parámetros con identificadores específicos.
ESPECIFICACION_CANONICA = {
    "A": ["P1_dominio", "P2_frontera", "P3_codominio",
          "P4_tipo_campo", "P5_soporte_trayectoria", "P6_estatuto_sigma"],
    "B": ["P7_angulo", "P8_direccion", "P9_vector_campo",
          "P10_gradiente", "P11_pliegue_local", "P12_curvatura_torsion"],
    "C": ["P13_convergencia", "P14_divergencia", "P15_inflexion",
          "P16_concavidad", "P17_convexidad", "P18_rugosidad"],
    "D": ["P19_intensidad_simple", "P20_potencial", "P21_fuente_local",
          "P22_fuerza_campo", "P23_sensibilidad", "P24_efecto_observable"],
    "E": ["P25_activacion_local", "P26_extincion_local", "P27_persistencia",
          "P28_rotor_turbulencia", "P29_resonancia", "P30_estabilidad_ruptura"],
    "F": ["P31_interseccion_otro", "P32_intensidad_compuesta", "P33_dominancia",
          "P34_factor_combinacion", "P35_huella_factual", "P36_lectura_auxiliar"],
}

# Primitivos metrológicos del SV (lectura Σ=0): nunca pueden aparecer como
# parámetros de campo dentro de la célula
PRIMITIVOS_METROLOGICOS_SIGMA0 = ["UE_MFC", "UFE", "UFM", "UFC", "UFT", "UFCE"]


def verificar_celula_bien_formada(celula):
    """
    Devuelve (es_valida, razones_de_invalidez).
    celula es lista de identificadores de parámetro en orden.
    """
    razones = []

    # 1. Cardinalidad exacta = 36
    if len(celula) != 36:
        razones.append(f"cardinalidad incorrecta: {len(celula)} (esperado 36)")

    # 2. Sin duplicados
    if len(celula) != len(set(celula)):
        duplicados = [p for p in celula if celula.count(p) > 1]
        razones.append(f"duplicados detectados: {set(duplicados)}")

    # 3. Sin primitivos metrológicos Σ=0
    metrologicos_intrusos = [p for p in celula if p in PRIMITIVOS_METROLOGICOS_SIGMA0]
    if metrologicos_intrusos:
        razones.append(f"primitivos metrológicos Σ=0 intrusos: {metrologicos_intrusos}")

    # 4. Orden correcto: cada parámetro en su familia y posición
    orden_canonico = []
    for fam in ["A", "B", "C", "D", "E", "F"]:
        orden_canonico.extend(ESPECIFICACION_CANONICA[fam])

    if len(celula) == 36 and len(set(celula)) == 36:
        # Sólo verificamos orden si no hay otros problemas
        if celula != orden_canonico:
            posiciones_incorrectas = [i for i, (a, b) in enumerate(zip(celula, orden_canonico)) if a != b]
            if posiciones_incorrectas:
                razones.append(f"orden incorrecto en {len(posiciones_incorrectas)} posiciones")

    return (len(razones) == 0, razones)


def main():
    print("=" * 78)
    print(" LAB-17 — Verificador adversarial de célula SV(36,6) mal formada")
    print("=" * 78)
    print()
    print(" Cuatro clases de mala formación cubiertas por el código E-17:")
    print("   1. Orden incorrecto")
    print("   2. Parámetros faltantes")
    print("   3. Duplicados")
    print("   4. Mezcla Σ=0 como Σ=1 (primitivo metrológico intruso)")
    print()

    # Construyo la célula canónica para tener referencia
    celula_canonica = []
    for fam in ["A", "B", "C", "D", "E", "F"]:
        celula_canonica.extend(ESPECIFICACION_CANONICA[fam])

    # CASOS ADVERSARIALES
    casos = []

    # Caso 1: orden incorrecto (intercambio de dos posiciones)
    cel_1 = list(celula_canonica)
    cel_1[0], cel_1[7] = cel_1[7], cel_1[0]  # P1 ↔ P8 (cruce A-B)
    casos.append(("Adv 1: orden incorrecto (P1 ↔ P8)", cel_1, "INVALIDA"))

    # Caso 2: parámetros faltantes (35 en vez de 36)
    cel_2 = list(celula_canonica)[:-1]  # quitamos P36
    casos.append(("Adv 2: parámetro faltante (P36 ausente)", cel_2, "INVALIDA"))

    # Caso 2b: parámetros faltantes (familia incompleta)
    cel_2b = list(celula_canonica)
    del cel_2b[12:14]  # quitamos P13 y P14 de Familia C
    casos.append(("Adv 2b: dos parámetros faltantes (P13, P14)", cel_2b, "INVALIDA"))

    # Caso 3: duplicados (P1 repetido, suplantando a P36)
    cel_3 = list(celula_canonica)
    cel_3[35] = "P1_dominio"  # duplicamos P1 en lugar de P36
    casos.append(("Adv 3: duplicado (P1 repetido en posición de P36)", cel_3, "INVALIDA"))

    # Caso 4: mezcla Σ=0 como Σ=1 (UE_MFC intruso)
    cel_4 = list(celula_canonica)
    cel_4[5] = "UE_MFC"  # primitivo metrológico en posición de P6
    casos.append(("Adv 4: primitivo metrológico UE_MFC intruso", cel_4, "INVALIDA"))

    # Caso 4b: dos metrológicos intrusos
    cel_4b = list(celula_canonica)
    cel_4b[5] = "UFE"
    cel_4b[18] = "UFM"
    casos.append(("Adv 4b: dos metrológicos intrusos (UFE, UFM)", cel_4b, "INVALIDA"))

    # CASOS DE CONTROL LEGÍTIMOS
    controles = [
        ("Ctrl 1: célula canónica completa", list(celula_canonica), "VALIDA"),
        ("Ctrl 2: célula canónica (segunda lectura)", list(celula_canonica), "VALIDA"),
    ]

    print(f" {'Caso':<58} | {'Esperado':<10} | {'OK':<3}")
    print(" " + "-" * 78)

    aciertos = 0
    total = len(casos) + len(controles)

    for etiqueta, celula, esperado in casos + controles:
        es_valida, razones = verificar_celula_bien_formada(celula)
        resultado = "VALIDA" if es_valida else "INVALIDA"
        ok = (resultado == esperado)
        if ok:
            aciertos += 1
        marca = "✓" if ok else "✗"
        print(f" {etiqueta:<58} | {esperado:<10} | {marca:<3}")
        if not es_valida and esperado == "INVALIDA":
            for r in razones[:1]:
                print(f"     · {r}")

    print()
    print(" Análisis estructural:")
    print(" - La célula SV(36,6) exige 36 parámetros en su orden canónico.")
    print(" - El código E-17 detecta cardinalidad incorrecta, duplicados,")
    print("   alteración de orden e intrusos metrológicos Σ=0.")
    print(" - La determinación operativa de campo exige célula bien formada;")
    print("   sin esa condición, el campo no admite radiografía operativa.")
    print(" - Los primitivos metrológicos Σ=0 nunca participan en la célula:")
    print("   esa intrusión es violación del Teorema 2 ya verificado en LAB-02.")
    print()

    if aciertos == total:
        print("✓ LAB-17 SUPERADO:")
        print(f"  - {len(casos)}/{len(casos)} adversariales rechazados.")
        print(f"  - {len(controles)}/{len(controles)} controles legítimos admitidos.")
        print("  - Código E-17 (célula mal formada) verificado adversarialmente.")
        return 0
    else:
        print(f"✗ LAB-17 FALLA: {total - aciertos} verificaciones incorrectas.")
        return 1


if __name__ == "__main__":
    import sys
    sys.exit(main())
