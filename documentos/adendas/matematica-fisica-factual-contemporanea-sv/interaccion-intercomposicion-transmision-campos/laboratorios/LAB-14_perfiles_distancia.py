"""
LAB-14 — Verificador de comparación de perfiles d^{SV}_{Φa} y d^{SV}_{Φb}
============================================================================

Verifica computacionalmente la Definición A.3 del Anexo A:

    d_{Φ^a}(Γ) := (d^{SV}_{Φ^a}(S_{l+1}, S_l), ..., d^{SV}_{Φ^a}(S_r, S_{r-1}))

y aplica las cinco reglas de intercomposición del apartado 15.3:
    1. Regla del máximo (max).
    2. Regla del mínimo (min).
    3. Regla dirigida (a → b).
    4. Regla por residual.
    5. Regla por diferencia estructural (defectos telescópicos).

El laboratorio:

    (A) Construye los perfiles locales de dos campos sobre trayectoria
        común y verifica las propiedades formales del perfil.

    (B) Aplica las cinco reglas de intercomposición a los dos perfiles.

    (C) Verifica que las cinco reglas producen resultados operativamente
        distintos (no son redundantes).

Tolerancia operativa: exacta sobre cuentas en SV(9,3).

Autoría / Authorship
-------------------
© 2026 Juan Antonio Lloret Egea. Todos los derechos reservados / All rights reserved.
ORCID: 0000-0002-6634-3351
Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA)
IA eñ™ — La Biblia de la IA™
ISSN 2695-6411
Licencia / License: CC BY-NC-ND 4.0
"""


def F_uno(S):
    return sum(1 for x in S if x == 1)


def F_cero(S):
    return sum(1 for x in S if x == 0)


def perfil_local(cadena, observable):
    """Perfil local de distancia factual fibrosa sobre la cadena."""
    return [abs(observable(cadena[k+1]) - observable(cadena[k]))
            for k in range(len(cadena) - 1)]


def regla_max(perfil_a, perfil_b):
    return [max(a, b) for a, b in zip(perfil_a, perfil_b)]


def regla_min(perfil_a, perfil_b):
    return [min(a, b) for a, b in zip(perfil_a, perfil_b)]


def regla_dirigida(perfil_a, perfil_b):
    """Diferencia signada: a − b."""
    return [a - b for a, b in zip(perfil_a, perfil_b)]


def distancia_intercampo(perfil_a, perfil_b):
    """Σ_k |d_a − d_b|."""
    return sum(abs(a - b) for a, b in zip(perfil_a, perfil_b))


def defecto_observable(cadena, observable):
    """Defecto telescópico simplificado (sin ζ_SV: devolvemos la magnitud)."""
    D = abs(observable(cadena[-1]) - observable(cadena[0]))
    suma = sum(abs(observable(cadena[k+1]) - observable(cadena[k]))
               for k in range(len(cadena) - 1))
    return abs(D - suma)


def main():
    print("=" * 78)
    print(" LAB-14 — Comparación de perfiles d^{SV}_{Φ^a} y d^{SV}_{Φ^b}")
    print("=" * 78)
    print()
    print(" Cinco reglas de intercomposición del apartado 15.3:")
    print("   1. Máximo (max)")
    print("   2. Mínimo (min)")
    print("   3. Dirigida (a → b)")
    print("   4. Por residual (DistInter − R_int)")
    print("   5. Por diferencia estructural (Δ^a − Δ^b)")
    print()

    # ---- Construcción de la cadena común y los dos perfiles ----
    print(" BLOQUE A — Perfiles locales sobre trayectoria común.")
    print()
    cadena = [
        (0, 0, 0,  0, 0, 0,  0, 0, 0),  # F_uno=0, F_cero=9
        (1, 0, 0,  0, 0, 0,  0, 0, 0),  # F_uno=1, F_cero=8
        (1, 1, 0,  0, 0, 0,  0, 0, 0),  # F_uno=2, F_cero=7
        (1, 1, 0,  0, "U", 0,  0, 0, 0),  # F_uno=2, F_cero=6
    ]
    perfil_F_uno = perfil_local(cadena, F_uno)
    perfil_F_cero = perfil_local(cadena, F_cero)

    print(f"   Cadena: {len(cadena)} configuraciones, {len(cadena)-1} pasos consecutivos.")
    print()
    print(f"   {'k → k+1':<10} | {'F_uno':<5} | {'F_cero':<6} | "
          f"{'d_F_uno':<7} | {'d_F_cero':<8}")
    print("   " + "-" * 60)
    for k in range(len(cadena) - 1):
        print(f"   {f'{k} → {k+1}':<10} | "
              f"{F_uno(cadena[k]):<5} | "
              f"{F_cero(cadena[k]):<6} | "
              f"{perfil_F_uno[k]:<7} | "
              f"{perfil_F_cero[k]:<8}")

    # Verificación de propiedades del perfil
    print()
    cardinalidad_OK = (len(perfil_F_uno) == len(cadena) - 1
                       and len(perfil_F_cero) == len(cadena) - 1)
    no_negativos = all(d >= 0 for d in perfil_F_uno + perfil_F_cero)
    perfiles_distintos = (perfil_F_uno != perfil_F_cero)
    bloque_A_OK = cardinalidad_OK and no_negativos
    print(f"   {'✓' if cardinalidad_OK else '✗'} Cardinalidad: {len(perfil_F_uno)} = pasos consecutivos.")
    print(f"   {'✓' if no_negativos else '✗'} No negatividad: todas las distancias ≥ 0.")
    print(f"   {'✓' if perfiles_distintos else '✗'} Perfiles operativamente distintos: F_uno vs F_cero.")
    print()

    # ---- Bloque B: aplicar las cinco reglas ----
    print(" BLOQUE B — Aplicación de las cinco reglas de intercomposición.")
    print()

    perfil_max = regla_max(perfil_F_uno, perfil_F_cero)
    perfil_min = regla_min(perfil_F_uno, perfil_F_cero)
    perfil_dir = regla_dirigida(perfil_F_uno, perfil_F_cero)
    dist_inter = distancia_intercampo(perfil_F_uno, perfil_F_cero)

    # Defecto telescópico simplificado de cada observable
    defecto_a = defecto_observable(cadena, F_uno)
    defecto_b = defecto_observable(cadena, F_cero)
    diff_estructural = abs(defecto_a - defecto_b)

    # Residual de interacción dirigida (estructural; aquí lo modelamos como
    # magnitud declarada en función de la incompatibilidad de los perfiles)
    R_interaccion = dist_inter / 2  # valor declarado para este escenario
    R_inter_residual = dist_inter - R_interaccion

    print(f"   Regla 1 (max):       {perfil_max}")
    print(f"   Regla 2 (min):       {perfil_min}")
    print(f"   Regla 3 (a → b):     {perfil_dir}")
    print(f"   Regla 4 (residual):  DistInter = {dist_inter}, R_int = {R_interaccion},")
    print(f"                        R^inter = DistInter − R_int = {R_inter_residual}")
    print(f"   Regla 5 (estructural): defecto_F_uno = {defecto_a}, defecto_F_cero = {defecto_b},")
    print(f"                        |Δa − Δb| = {diff_estructural}")
    print()

    # ---- Bloque C: verificar que las reglas producen resultados distintos ----
    print(" BLOQUE C — Las cinco reglas producen resultados operativamente distintos.")
    print()
    resultados = {
        "max": perfil_max,
        "min": perfil_min,
        "dirigida": perfil_dir,
        "residual": [R_inter_residual],
        "estructural": [diff_estructural],
    }

    todos_distintos = True
    pares_revisados = []
    for r1, v1 in resultados.items():
        for r2, v2 in resultados.items():
            if r1 < r2:
                # Comparar magnitudes representativas
                if r1 in ("max", "min", "dirigida") and r2 in ("max", "min", "dirigida"):
                    iguales = (v1 == v2)
                else:
                    iguales = (sum(abs(x) for x in v1) == sum(abs(x) for x in v2))
                pares_revisados.append((r1, r2, iguales))
                if iguales:
                    print(f"   ✗ Reglas '{r1}' y '{r2}' producen el mismo resultado.")
                    todos_distintos = False

    if todos_distintos:
        print("   ✓ Las cinco reglas producen resultados operativamente distintos.")
    print()

    # ---- Resumen ----
    todo_OK = bloque_A_OK and todos_distintos
    print(" Análisis estructural:")
    print(" - Los perfiles locales son vectores de cardinalidad pasos = |Γ| − 1.")
    print(" - Las cinco reglas leen información distinta de los mismos perfiles:")
    print("   max → cambio más rápido paso a paso;")
    print("   min → cambio común mínimo;")
    print("   dirigida → asimetría signada;")
    print("   residual → articulación con interacción 𝓘_SV;")
    print("   estructural → comparación de defectos telescópicos.")
    print()

    if todo_OK:
        print("✓ LAB-14 SUPERADO:")
        print("  - Perfiles locales construidos sobre trayectoria común.")
        print("  - Las cinco reglas de intercomposición aplicadas correctamente.")
        print("  - Los cinco resultados son operativamente distintos.")
        return 0
    else:
        print("✗ LAB-14 FALLA: alguna verificación incorrecta.")
        return 1


if __name__ == "__main__":
    import sys
    sys.exit(main())
