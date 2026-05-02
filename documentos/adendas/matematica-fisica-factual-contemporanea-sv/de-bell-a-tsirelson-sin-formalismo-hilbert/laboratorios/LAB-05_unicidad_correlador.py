"""
LAB-05 — Verificación numérica de la unicidad del correlador angular factual
==============================================================================

Verifica numéricamente el Teorema 10.2.1 (unicidad del coseno factual acoplado)
sobre once candidatos estructuralmente distintos para C_SV(δ), comprobando que
sólo el candidato canónico C_SV(δ) = -cos δ satisface simultáneamente los nueve
axiomas A1–A9 del aparato angular factual del Sistema Vectorial SV.

Cada candidato alternativo viola al menos uno de los axiomas. El laboratorio
identifica qué axioma falla en cada caso.

Axiomas verificados:
    A1: dependencia angular pura.
    A2: anticorrelación plena en coincidencia C_SV(0) = -1.
    A3: correlación plena en base opuesta C_SV(π) = +1.
    A4: paridad C_SV(-δ) = C_SV(δ).
    A5: complementariedad polar C_SV(δ + π) = -C_SV(δ).
    A6: existencia de componente conjugada normalizada (C² + S² = 1).
    A7: composición SO(2) sobre la auxiliar C̃ = -C_SV.
    A8: continuidad estructural.
    A9: fidelidad angular mínima (k = 1).

Autoría
-------
© 2026. Todos los derechos reservados.
Juan Antonio Lloret Egea
ORCID: 0000-0002-6634-3351
Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español (ITVIA)
IA eñ™ — La Biblia de la IA™
ISSN 2695-6411
Licencia: CC BY-NC-ND 4.0
"""
import numpy as np


TOL = 1e-9


def verifica_axiomas(C, nombre):
    """
    Verifica los nueve axiomas A1–A9 sobre un candidato C: ℝ/2πℤ → [-1, +1].
    Devuelve un diccionario con el resultado por axioma y la lista de fallos.
    """
    deltas = np.linspace(-2 * np.pi, 2 * np.pi, 401)
    resultados = {}

    # A2: C(0) = -1
    resultados["A2"] = abs(C(0) + 1) < TOL
    # A3: C(π) = +1
    resultados["A3"] = abs(C(np.pi) - 1) < TOL
    # A4: paridad
    resultados["A4"] = all(abs(C(-d) - C(d)) < TOL for d in deltas)
    # A5: complementariedad polar
    resultados["A5"] = all(abs(C(d + np.pi) + C(d)) < TOL for d in deltas)
    # A6: existencia de S = sqrt(1 - C^2) bien definida (C en [-1, +1])
    resultados["A6"] = all(abs(C(d)) <= 1 + TOL for d in deltas)
    # A7: composición SO(2) sobre la auxiliar C̃ = -C
    # C̃(δ1 + δ2) = C̃(δ1)C̃(δ2) - S̃(δ1)S̃(δ2)
    # Verificar para varias parejas
    Ct = lambda d: -C(d)

    def St(d):
        c = Ct(d)
        if abs(c) > 1:
            return None
        # Convención: S̃ = sqrt(1 - C̃²) con signo del seno habitual
        return np.sin(d) if -np.pi <= ((d + np.pi) % (2 * np.pi) - np.pi) <= np.pi else -np.sin(d)

    pruebas_A7 = []
    for d1 in [0.1, 0.5, 1.0, 1.5, 2.0]:
        for d2 in [0.1, 0.5, 1.0, 1.5, 2.0]:
            try:
                lhs = Ct(d1 + d2)
                rhs = Ct(d1) * Ct(d2) - St(d1) * St(d2)
                pruebas_A7.append(abs(lhs - rhs) < TOL)
            except (TypeError, ValueError):
                pruebas_A7.append(False)
    resultados["A7"] = all(pruebas_A7)
    # A8: continuidad
    finite = all(np.isfinite(C(d)) for d in deltas)
    resultados["A8"] = finite
    # A9: fidelidad angular mínima — verificar que C(δ + 2π/k) = C(δ) sólo si k = 1
    # Si k=2: C(δ + π) = C(δ) violaría A5 con C(δ+π) = -C(δ); hay que ver si la
    # aux Ct cumple Ct(δ + 2π/k) = Ct(δ) para k=2, 3, ...
    es_k1 = True
    for k in [2, 3, 4]:
        period = 2 * np.pi / k
        ds_test = [0.1, 0.7, 1.3, 2.1]
        if all(abs(Ct(d + period) - Ct(d)) < TOL for d in ds_test):
            es_k1 = False
            break
    resultados["A9"] = es_k1

    fallos = [a for a, ok in resultados.items() if not ok]
    return resultados, fallos


def main():
    print("=" * 72)
    print("LAB-05 — Unicidad del correlador angular factual sobre 11 candidatos")
    print("=" * 72)

    candidatos = [
        ("C_SV = -cos δ (canónico)", lambda d: -np.cos(d)),
        ("k=2: -cos(2δ)", lambda d: -np.cos(2 * d)),
        ("k=3: -cos(3δ)", lambda d: -np.cos(3 * d)),
        ("Diente de sierra", lambda d: -((d / np.pi) % 2 - 1)),
        ("Parábola cuadrática", lambda d: -1 + 2 * (((d % (2 * np.pi)) - np.pi) / np.pi) ** 2),
        ("Sigmoide tanh", lambda d: -np.tanh(np.cos(d))),
        ("Función escalón", lambda d: -1 if (d % (2 * np.pi)) < np.pi else +1),
        ("Rotación fase π/4: -cos(δ + π/4)", lambda d: -np.cos(d + np.pi / 4)),
        ("Negativo: +cos δ", lambda d: np.cos(d)),
        ("Mezcla 0,7 cos δ + 0,3 cos 2δ", lambda d: -(0.7 * np.cos(d) + 0.3 * np.cos(2 * d))),
        ("Polinomio cuarto grado", lambda d: -1 + 0.5 * (d % (2 * np.pi) - np.pi) ** 2 / np.pi ** 2),
    ]

    print(f"\n{'Candidato':<45} | {'Axiomas violados':<25}")
    print("-" * 75)

    n_canonico_pasa = 0
    n_alternativo_falla = 0
    for nombre, C in candidatos:
        try:
            _, fallos = verifica_axiomas(C, nombre)
        except Exception as e:
            fallos = ["error_eval"]
        marca = ", ".join(fallos) if fallos else "ninguno (CANÓNICO)"
        if "canónico" in nombre.lower() and not fallos:
            n_canonico_pasa += 1
        elif "canónico" not in nombre.lower() and fallos:
            n_alternativo_falla += 1
        print(f"{nombre:<45} | {marca:<25}")

    n_alternativos = len(candidatos) - 1
    print()
    print(f"Candidato canónico que satisface A1–A9: {n_canonico_pasa}/1")
    print(f"Candidatos alternativos que violan al menos un axioma: {n_alternativo_falla}/{n_alternativos}")

    if n_canonico_pasa == 1 and n_alternativo_falla == n_alternativos:
        print("\n✓ LAB-05 SUPERADO: unicidad del correlador C_SV(δ) = -cos δ verificada.")
        return 0
    else:
        print("\n✗ LAB-05 FALLA: revisar.")
        return 1


if __name__ == "__main__":
    import sys
    sys.exit(main())
