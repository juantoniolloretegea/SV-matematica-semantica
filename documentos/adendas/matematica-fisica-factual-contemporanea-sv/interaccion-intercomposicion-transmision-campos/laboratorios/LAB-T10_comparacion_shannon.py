"""
LAB-T10 — Comparación con canal Shannon clásico sin atribución semántica
==========================================================================

Verifica adversarialmente la frontera del apartado 18.1 entre la teoría
matemática de la comunicación de Shannon (1948) y la transmisión factual
del Sistema Vectorial SV.

El laboratorio:

    (A) Aplica un canal binario simétrico de Shannon sobre un estado X_SV
        con marcas U declaradas, mostrando que el canal NO preserva U
        por construcción (las degrada a 0 o 1 estocásticamente).

    (B) Verifica que sin codificación adicional que preserve U como símbolo
        propio, el canal Shannon NO es canal factual apto del Sistema
        Vectorial SV: viola el Teorema 7.

    (C) Verifica que con codificación factual que mapea U a un símbolo
        propio del alfabeto extendido y un canal Shannon ternario sobre
        ese alfabeto, la transmisión sí preserva U y queda apta.

    (D) Confirma operativamente que la teoría de la información entra
        SOLO como ingeniería de transmisión, no como semántica.

Tolerancia operativa: cero tolerancia a la pérdida de U bajo canal Shannon
clásico binario sin codificación factual.

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


# Estado origen con tres marcas U
ESTADO_ORIGEN = (1, 0, "U", 1, "U", 0, 1, "U", 0)


def canal_shannon_binario(estado, semilla=42):
    """
    Canal binario simétrico de Shannon: entrada en {0,1}, salida en {0,1}.
    NO admite U: cualquier U de la entrada es resuelta arbitrariamente.
    Esto demuestra adversarialmente que el canal Shannon clásico no preserva U.
    """
    rng = random.Random(semilla)
    salida = []
    for v in estado:
        if v == "U":
            # Canal Shannon binario fuerza la elección: U → {0, 1}
            salida.append(rng.choice([0, 1]))
        else:
            salida.append(v)
    return tuple(salida)


def canal_shannon_ternario_factual(estado):
    """
    Canal Shannon ternario sobre alfabeto {0, 1, U} extendido.
    Preserva U como símbolo propio, conforme a la disciplina del SV.
    """
    return tuple(estado)  # canal idéntico ternario sin ruido


def calcular_R_U(origen, recon):
    """Residual de preservación de U."""
    return sum(1 for a, b in zip(origen, recon)
               if (a == "U" and b != "U") or (a != "U" and b == "U"))


def main():
    print("=" * 78)
    print(" LAB-T10 — Comparación con canal Shannon sin atribución semántica")
    print("=" * 78)
    print()
    print(" Frontera operativa del apartado 18.1:")
    print("   Shannon = canal / transmisión / codificación / reconstrucción")
    print("   SV      = semántica factual / suceso / campo / U / dictamen")
    print()
    print(f" Estado origen: {ESTADO_ORIGEN}")
    n_U = sum(1 for v in ESTADO_ORIGEN if v == "U")
    print(f" Marcas U en origen: {n_U}")
    print()

    # Bloque A: canal Shannon binario clásico
    print(" BLOQUE A — Canal Shannon binario clásico aplicado a estado con U.")
    print()
    estado_recon_shannon = canal_shannon_binario(ESTADO_ORIGEN)
    print(f"   Estado reconstruido: {estado_recon_shannon}")
    R_U_shannon = calcular_R_U(ESTADO_ORIGEN, estado_recon_shannon)
    print(f"   R_U (preservación de U): {R_U_shannon}")
    print(f"   Marcas U restantes: {sum(1 for v in estado_recon_shannon if v == 'U')}")
    apto_shannon = (R_U_shannon == 0)
    print(f"   {'✓' if not apto_shannon else '✗'} Canal Shannon clásico NO preserva U: viola Teorema 7.")
    print()

    # Bloque B: confirmación adversarial
    print(" BLOQUE B — Confirmación adversarial: canal Shannon clásico no apto.")
    print()
    no_apto_correcto = (R_U_shannon > 0)
    print(f"   R_U > 0: {R_U_shannon > 0} → canal NO apto bajo disciplina SV.")
    print(f"   {'✓' if no_apto_correcto else '✗'} Frontera del apartado 18.1 verificada operativamente.")
    print()

    # Bloque C: canal Shannon ternario con alfabeto factual extendido
    print(" BLOQUE C — Canal Shannon ternario sobre alfabeto {0, 1, U}.")
    print()
    estado_recon_ternario = canal_shannon_ternario_factual(ESTADO_ORIGEN)
    print(f"   Estado reconstruido: {estado_recon_ternario}")
    R_U_ternario = calcular_R_U(ESTADO_ORIGEN, estado_recon_ternario)
    print(f"   R_U (preservación de U): {R_U_ternario}")
    apto_ternario = (R_U_ternario == 0)
    print(f"   {'✓' if apto_ternario else '✗'} Canal ternario factual SÍ preserva U: respeta Teorema 7.")
    print()

    # Bloque D: confirmación de la frontera operativa
    print(" BLOQUE D — Frontera entre Shannon clásico y Shannon factual SV.")
    print()
    print("   Shannon clásico binario: canal sobre {0, 1}; U se degrada por construcción.")
    print("   Shannon factual ternario SV: canal sobre {0, 1, U}; U preservada como símbolo.")
    print("   La teoría de la información es UTIL como ingeniería del canal,")
    print("   pero NO sustituye la semántica factual del corpus.")
    print()

    todo_OK = (not apto_shannon) and apto_ternario and no_apto_correcto

    print(" Análisis estructural:")
    print(" - Shannon clásico binario no preserva U: viola disciplina SV.")
    print(" - Shannon ternario sobre {0, 1, U} sí preserva U: respeta disciplina SV.")
    print(" - La frontera del apartado 18.1 distingue uso clásico (no apto) de")
    print("   uso factual SV (apto bajo extensión ternaria del alfabeto).")
    print(" - Información ≠ verdad factual; canal ≠ semántica.")
    print()

    if todo_OK:
        print("✓ LAB-T10 SUPERADO:")
        print("  - Canal Shannon clásico rechazado por violación del Teorema 7.")
        print("  - Canal Shannon ternario factual aceptado.")
        print("  - Frontera del apartado 18.1 verificada operativamente.")
        return 0
    else:
        print("✗ LAB-T10 FALLA: alguna verificación incorrecta.")
        return 1


if __name__ == "__main__":
    import sys
    sys.exit(main())
