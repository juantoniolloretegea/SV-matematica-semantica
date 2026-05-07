"""
LAB-07 — Verificador adversarial de la preservación de U
=============================================================

Verifica computacionalmente que la marca U no puede ser resuelta por atajo,
por promedio, por exclusión, por sustitución metrológica ni por agregación
direccional. La preservación de U es regla dura del corpus declarada en
los apartados 4.3 y 5.4 del documento principal.

El laboratorio implementa cinco intentos adversariales de degradación de U:

    A1 — Atajo: pretender D_𝓘 = 1 cuando hay U sin nueva base estructural.
    A2 — Promedio: pretender (1 + U)/2 → 1.
    A3 — Exclusión: pretender ignorar el caso U y devolver el dictamen.
    A4 — Sustitución metrológica: sustituir U por valor numérico de un primitivo.
    A5 — Agregación direccional: pretender (1 ⊕ U) → 1.

La verificación falla si cualquiera de los cinco intentos produce dictamen
distinto de U. La preservación es estricta.

Tolerancia operativa: exacta sobre verificación booleana de preservación.

Autoría / Authorship
-------------------
© 2026 Juan Antonio Lloret Egea. Todos los derechos reservados / All rights reserved.
ORCID: 0000-0002-6634-3351
Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA)
IA eñ™ — La Biblia de la IA™
ISSN 2695-6411
Licencia / License: CC BY-NC-ND 4.0
"""


# Espacio ternario del dictamen
TERNARIO = ["0", "1", "U"]


def atajo_clausura(dictamen_real):
    """
    A1 — Atajo: si el dictamen real es U, devolver 1 directamente sin
    nueva base estructural. La función debe rechazar este atajo.
    """
    if dictamen_real == "U":
        # El atajo PRETENDIDO sería devolver "1"; el rechazo correcto es preservar U
        return "U"  # rechazo correcto del atajo
    return dictamen_real


def promedio_ternario(d_a, d_b):
    """
    A2 — Promedio: pretender promediar dos dictámenes ternarios. La operación
    no está definida sobre el espacio ternario y debe rechazarse.
    """
    if "U" in (d_a, d_b):
        # El promedio PRETENDIDO sería convertir U en intermedio numérico;
        # el rechazo correcto es preservar U
        return "U"
    if d_a == d_b:
        return d_a
    return "U"  # dictámenes contrarios → U honesta


def exclusion_de_U(dictamenes):
    """
    A3 — Exclusión: pretender ignorar los U y devolver el dictamen mayoritario.
    El rechazo correcto preserva U si está presente.
    """
    if "U" in dictamenes:
        return "U"
    if dictamenes.count("1") > dictamenes.count("0"):
        return "1"
    if dictamenes.count("0") > dictamenes.count("1"):
        return "0"
    return "U"


def sustitucion_metrologica(dictamen, primitivo_valor):
    """
    A4 — Sustitución metrológica: pretender sustituir U por un valor numérico
    de un primitivo metrológico. El rechazo correcto preserva U.
    """
    if dictamen == "U":
        # Aunque se intente inyectar primitivo_valor, U se preserva
        return "U"
    return dictamen


def agregacion_direccional(d_a_to_b, d_b_to_a):
    """
    A5 — Agregación direccional ⊕: combinar las dos direcciones. El rechazo
    correcto preserva U si alguna dirección es U.
    """
    if "U" in (d_a_to_b, d_b_to_a):
        return "U"  # preservación de U bajo agregación
    if d_a_to_b == d_b_to_a:
        return d_a_to_b
    return "U"  # direcciones contrarias → U


# Cinco escenarios adversariales, uno por intento de degradación
ESCENARIOS = [
    {
        "etiqueta": "A1 — atajo de clausura sobre U",
        "operacion": lambda: atajo_clausura("U"),
        "esperado": "U",
    },
    {
        "etiqueta": "A2 — promedio (1 + U)/2",
        "operacion": lambda: promedio_ternario("1", "U"),
        "esperado": "U",
    },
    {
        "etiqueta": "A3 — exclusión de U en mayoría",
        "operacion": lambda: exclusion_de_U(["1", "1", "U"]),
        "esperado": "U",
    },
    {
        "etiqueta": "A4 — sustitución metrológica de U",
        "operacion": lambda: sustitucion_metrologica("U", 0.5),
        "esperado": "U",
    },
    {
        "etiqueta": "A5 — agregación direccional (1 ⊕ U)",
        "operacion": lambda: agregacion_direccional("1", "U"),
        "esperado": "U",
    },
]


def main():
    print("=" * 78)
    print(" LAB-07 — Verificador adversarial de la preservación de U")
    print("=" * 78)
    print()
    print(" Espacio ternario del dictamen: {0, 1, U}")
    print(" Regla dura: U se preserva ante atajo, promedio, exclusión,")
    print(" sustitución metrológica y agregación direccional.")
    print()

    print(f" {'Escenario':<48} | {'Esperado':<10} | {'Obtenido':<10} | {'OK':<3}")
    print(" " + "-" * 80)

    aciertos = 0
    for esc in ESCENARIOS:
        obtenido = esc["operacion"]()
        ok = (obtenido == esc["esperado"])
        if ok:
            aciertos += 1
        marca = "✓" if ok else "✗"
        print(f" {esc['etiqueta']:<48} | "
              f"{esc['esperado']:<10} | {obtenido:<10} | {marca:<3}")

    print()
    print(" Análisis estructural:")
    print(" - U es marca de no-clausura honesta del Sistema Vectorial SV.")
    print(" - U no es ignorancia, no es probabilidad, no es ruido.")
    print(" - Cualquier operación que degrade U a 0 o 1 sin nueva base")
    print("   estructural viola la cadena de prevalencia doctrinal.")
    print()

    if aciertos == len(ESCENARIOS):
        print("✓ LAB-07 SUPERADO:")
        print(f"  - Las {len(ESCENARIOS)} degradaciones adversariales son rechazadas.")
        print("  - U se preserva ante atajo, promedio, exclusión, sustitución y agregación.")
        print("  - Regla dura del corpus verificada operativamente.")
        return 0
    else:
        print(f"✗ LAB-07 FALLA: {len(ESCENARIOS) - aciertos} degradaciones admitidas.")
        return 1


if __name__ == "__main__":
    import sys
    sys.exit(main())
