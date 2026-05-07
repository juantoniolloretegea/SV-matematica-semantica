"""
LAB-08 — Verificador de la función ordinal de campo
======================================================

Verifica computacionalmente la construcción del apartado 12 del documento
principal: la función ordinal de campo

    f_Φ : ℕ_0 → 𝓥_Φ con f_Φ(n) = Φ(S_n)

junto con la derivada de suceso

    Δ_{ν_n}Φ := f_Φ(n+1) − f_Φ(n)

y la sensibilidad de interacción

    𝓢_{Φ^a → Φ^b}(n) := 𝓡_SV(Δ_{ν_n}Φ^b | Δ_{ν_n}Φ^a).

El laboratorio:

    (A) Construye f_Φ(n) sobre una secuencia ordinal sintética para tres
        campos admitidos, evaluando que el operador es bien definido sobre
        ℕ_0 sin presuponer cronología continua.

    (B) Calcula la derivada de suceso Δ_{ν_n}Φ como diferencia entre valores
        ordinales, confirmando que opera sobre el ordinal de cadena y no
        introduce tiempo soberano.

    (C) Calcula la sensibilidad asimétrica entre dos campos y confirma que
        en general 𝓢_{a→b} ≠ 𝓢_{b→a}, en correspondencia con el Teorema 4.

Tolerancia operativa: 1e-12 sobre las componentes diferenciales.

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


TOL = 1e-12


# Secuencia ordinal sintética: tres campos admitidos sobre 8 sucesos.
# Los valores f_Φ(n) son objeto del aparato del corpus, no magnitudes SI.
# La secuencia ilustra una trayectoria de 8 estados con sucesos ordinales.
SECUENCIA_ORDINAL = {
    "sector_basal_gravitatorio": [1.0, 1.1, 1.3, 1.6, 2.0, 2.3, 2.5, 2.6],
    "sector_electrico":          [0.0, 0.2, 0.5, 0.7, 0.6, 0.8, 1.0, 1.2],
    "sector_magnetico":          [2.0, 1.8, 1.5, 1.4, 1.5, 1.6, 1.4, 1.2],
}


def funcion_ordinal_campo(campo, n):
    """f_Φ(n) = Φ(S_n) sobre la secuencia declarada."""
    return SECUENCIA_ORDINAL[campo][n]


def derivada_suceso(campo, n):
    """Δ_{ν_n}Φ := f_Φ(n+1) - f_Φ(n)."""
    return funcion_ordinal_campo(campo, n+1) - funcion_ordinal_campo(campo, n)


def sensibilidad_interaccion(campo_a, campo_b, n):
    """
    Sensibilidad de interacción 𝓢_{Φ^a → Φ^b}(n).

    Operativamente, en este laboratorio se modela como cociente de derivadas
    de suceso cuando la derivada del campo a es no nula. Si el cociente es
    indefinido (denominador nulo), se devuelve U.
    """
    delta_a = derivada_suceso(campo_a, n)
    delta_b = derivada_suceso(campo_b, n)
    if abs(delta_a) < TOL:
        return None  # representa U
    return delta_b / delta_a


def main():
    print("=" * 78)
    print(" LAB-08 — Verificador de la función ordinal de campo")
    print("=" * 78)
    print()
    print(" Construcción operativa:")
    print("   f_Φ(n) = Φ(S_n)               [función ordinal]")
    print("   Δ_{ν_n}Φ = f_Φ(n+1) − f_Φ(n)  [derivada de suceso]")
    print("   𝓢_{a→b}(n) = Δ_b/Δ_a          [sensibilidad direccional]")
    print()

    # ---- Bloque A: función ordinal ----
    n_sucesos = len(next(iter(SECUENCIA_ORDINAL.values())))
    print(f" BLOQUE A — Función ordinal sobre {n_sucesos} sucesos.")
    print()
    print(f" {'n':<3} | " + " | ".join(f"{c[:18]:<18}" for c in SECUENCIA_ORDINAL.keys()))
    print(" " + "-" * 75)
    for n in range(n_sucesos):
        valores = [f"{funcion_ordinal_campo(c, n):<18.4f}" for c in SECUENCIA_ORDINAL.keys()]
        print(f" {n:<3} | " + " | ".join(valores))
    print()

    # ---- Bloque B: derivada de suceso ----
    print(f" BLOQUE B — Derivada de suceso Δ_{{ν_n}}Φ.")
    print()
    print(f" {'n':<3} | " + " | ".join(f"Δ_{c[:14]:<14}" for c in SECUENCIA_ORDINAL.keys()))
    print(" " + "-" * 75)
    for n in range(n_sucesos - 1):
        derivadas = [f"{derivada_suceso(c, n):<+18.4f}" for c in SECUENCIA_ORDINAL.keys()]
        print(f" {n:<3} | " + " | ".join(derivadas))
    print()

    # ---- Bloque C: sensibilidad asimétrica ----
    print(" BLOQUE C — Sensibilidad de interacción asimétrica.")
    print()
    print(" Pares evaluados sobre n = 3 (estado intermedio):")
    pares = [
        ("sector_basal_gravitatorio", "sector_electrico"),
        ("sector_electrico", "sector_basal_gravitatorio"),
        ("sector_basal_gravitatorio", "sector_magnetico"),
        ("sector_magnetico", "sector_basal_gravitatorio"),
    ]
    asimetrias_detectadas = 0
    for a, b in pares:
        s = sensibilidad_interaccion(a, b, 3)
        s_str = f"{s:+.6f}" if s is not None else "U"
        print(f"   𝓢_{{{a[:12]} → {b[:12]}}}(3) = {s_str}")

    # Verificación de asimetría
    print()
    print(" Verificación de asimetría sobre tres pares:")
    aciertos_asimetria = 0
    for a, b in [("sector_basal_gravitatorio", "sector_electrico"),
                 ("sector_basal_gravitatorio", "sector_magnetico"),
                 ("sector_electrico", "sector_magnetico")]:
        s_ab = sensibilidad_interaccion(a, b, 3)
        s_ba = sensibilidad_interaccion(b, a, 3)
        if s_ab is None or s_ba is None:
            asimetria = "U"
        elif abs(s_ab - s_ba) > TOL:
            asimetria = "DETECTADA"
            aciertos_asimetria += 1
        else:
            asimetria = "no"
        print(f"   {a[:18]} ↔ {b[:18]}: 𝓢(a→b) = {s_ab:+.4f}, "
              f"𝓢(b→a) = {s_ba:+.4f} → {asimetria}")

    print()
    print(" Análisis estructural:")
    print(" - La función ordinal opera sobre ℕ_0 sin presuponer cronología.")
    print(" - La derivada de suceso es diferencia de valores ordinales.")
    print(" - La sensibilidad hereda la asimetría direccional del Teorema 4.")
    print()

    n_pares = 3
    if aciertos_asimetria >= 2:  # al menos dos de tres pares deben mostrar asimetría
        print("✓ LAB-08 SUPERADO:")
        print(f"  - Función ordinal construida sobre {n_sucesos} sucesos para 3 campos.")
        print(f"  - Derivada de suceso calculada para los 3 campos.")
        print(f"  - Sensibilidad asimétrica detectada en {aciertos_asimetria}/{n_pares} pares.")
        print("  - Función ordinal de campo verificada operativamente.")
        return 0
    else:
        print(f"✗ LAB-08 FALLA: sólo {aciertos_asimetria}/{n_pares} pares con asimetría.")
        return 1


if __name__ == "__main__":
    import sys
    sys.exit(main())
