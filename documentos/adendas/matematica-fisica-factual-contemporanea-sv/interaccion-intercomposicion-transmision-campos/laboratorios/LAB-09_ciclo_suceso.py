"""
LAB-09 — Verificador de Ciclo de Suceso
==========================================

Verifica computacionalmente la condición de Ciclo de Suceso definida en el
apartado 13 del documento principal:

    CS(Φ) = 1  ⟺  ∃ p > 0 : ∀ n admisible, f_Φ(n+p) ≡_SV f_Φ(n)

bajo equivalencia factual declarada y residual de ciclo controlado:

    R^CS_{a→b, F}(Γ) ≤ L_CS

El laboratorio implementa cuatro escenarios:

    C1 — campo con Ciclo de Suceso cerrado (período p).
    C2 — campo sin Ciclo de Suceso (función monótona).
    C3 — campo con ciclo aparente pero residual fuera de tolerancia.
    C4 — interacción dirigida con ciclo asimétrico
          (CS(a→b) ≠ CS(b→a)).

Tolerancia operativa: L_CS = 1e-3 sobre el residual de ciclo.

Autoría / Authorship
-------------------
© 2026 Juan Antonio Lloret Egea. Todos los derechos reservados / All rights reserved.
ORCID: 0000-0002-6634-3351
Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA)
IA eñ™ — La Biblia de la IA™
ISSN 2695-6411
Licencia / License: CC BY-NC-ND 4.0
"""

import numpy as np


L_CS = 1e-3  # umbral declarado del residual de ciclo


def residual_ciclo(secuencia, p):
    """
    Calcula el residual de ciclo R^CS sobre una secuencia ordinal y un
    período candidato p como la máxima distancia |f(n+p) - f(n)| sobre
    los n admisibles.
    """
    if p <= 0 or p >= len(secuencia):
        return float("inf")
    distancias = [abs(secuencia[n+p] - secuencia[n])
                  for n in range(len(secuencia) - p)]
    return max(distancias) if distancias else float("inf")


def detecta_ciclo(secuencia, p_max=None):
    """
    Busca el período p más pequeño tal que el residual de ciclo está bajo L_CS.
    Devuelve (CS, p_detectado, R) donde CS ∈ {0, 1, U}.
    """
    n = len(secuencia)
    if p_max is None:
        p_max = n // 2
    mejor_p = None
    mejor_R = float("inf")
    for p in range(1, p_max + 1):
        R = residual_ciclo(secuencia, p)
        if R < mejor_R:
            mejor_R = R
            mejor_p = p
        if R < L_CS:
            return ("1", p, R)
    if mejor_R < L_CS * 100:  # cerca pero fuera de tolerancia
        return ("U", mejor_p, mejor_R)
    return ("0", None, mejor_R)


# Cuatro escenarios estructurales
ESCENARIOS = [
    {
        "etiqueta": "C1 — campo con CS cerrado (p = 4)",
        # Período exacto 4: [a, b, c, d, a, b, c, d, ...]
        "secuencia": [1.0, 2.0, 3.0, 2.0] * 3,
        "esperado_CS": "1",
    },
    {
        "etiqueta": "C2 — campo sin CS (monótono)",
        # Función estrictamente creciente: no hay ciclo
        "secuencia": [float(i) for i in range(1, 13)],
        "esperado_CS": "0",
    },
    {
        "etiqueta": "C3 — ciclo aparente con residual fuera de tolerancia",
        # Casi periódico pero con desviación de 0.05 (mayor que L_CS)
        "secuencia": [1.0, 2.0, 3.0, 2.0, 1.05, 2.05, 3.05, 2.05, 1.10, 2.10, 3.10, 2.10],
        "esperado_CS": "U",  # ni cierre limpio ni rechazo total
    },
    {
        "etiqueta": "C4 — interacción asimétrica direccional",
        # No es estrictamente CS de campo; se evalúa en el bloque B
        "secuencia": None,
        "esperado_CS": None,
    },
]


def main():
    print("=" * 78)
    print(" LAB-09 — Verificador de Ciclo de Suceso")
    print("=" * 78)
    print()
    print(f" Umbral declarado del residual de ciclo: L_CS = {L_CS}")
    print()

    # ---- Bloque A: tres escenarios de CS de campo ----
    print(" BLOQUE A — Ciclo de Suceso de campo.")
    print()
    print(f" {'Escenario':<48} | {'Esperado':<10} | {'Detectado':<10} | "
          f"{'p':<3} | {'R':<10}")
    print(" " + "-" * 90)

    aciertos_A = 0
    for esc in ESCENARIOS[:3]:
        CS, p, R = detecta_ciclo(esc["secuencia"])
        ok = (CS == esc["esperado_CS"])
        if ok:
            aciertos_A += 1
        marca = "✓" if ok else "✗"
        p_str = str(p) if p is not None else "—"
        R_str = f"{R:.5f}" if R != float("inf") else "inf"
        print(f" {esc['etiqueta']:<48} | "
              f"{esc['esperado_CS']:<10} | {CS:<10} | {p_str:<3} | {R_str:<10} {marca}")

    print()

    # ---- Bloque B: ciclo de interacción asimétrico ----
    print(" BLOQUE B — Ciclo de Suceso de interacción asimétrico.")
    print()
    # Dos secuencias que representan la dirección a→b y la dirección b→a
    secuencia_a_to_b = [1.0, 2.0, 3.0, 2.0] * 3   # CS cerrado p = 4
    secuencia_b_to_a = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0]  # sin CS

    CS_ab, p_ab, R_ab = detecta_ciclo(secuencia_a_to_b)
    CS_ba, p_ba, R_ba = detecta_ciclo(secuencia_b_to_a)

    print(f"   Dirección a → b: CS = {CS_ab}, p = {p_ab}, R = {R_ab:.5f}")
    print(f"   Dirección b → a: CS = {CS_ba}, p = {p_ba}, R = {R_ba:.5f}")

    asimetria_ciclo = (CS_ab != CS_ba)
    print(f"   ¿Asimetría direccional del ciclo? {'sí' if asimetria_ciclo else 'no'}")

    aciertos_B = 1 if asimetria_ciclo else 0

    print()
    print(" Análisis estructural:")
    print(" - El Ciclo de Suceso no es periodicidad temporal.")
    print(" - Es recurrencia estructural sobre el ordinal de cadena.")
    print(" - La detección requiere residual bajo umbral declarado L_CS.")
    print(" - El ciclo hereda la asimetría direccional del operador 𝓘_SV.")
    print()

    total_aciertos = aciertos_A + aciertos_B
    total = 3 + 1

    if total_aciertos == total:
        print("✓ LAB-09 SUPERADO:")
        print(f"  - {aciertos_A}/3 escenarios de CS de campo verificados.")
        print(f"  - Asimetría direccional del ciclo de interacción detectada.")
        print("  - Ciclo de Suceso verificado operativamente.")
        return 0
    else:
        print(f"✗ LAB-09 FALLA: {total - total_aciertos} verificaciones incorrectas.")
        return 1


if __name__ == "__main__":
    import sys
    sys.exit(main())
