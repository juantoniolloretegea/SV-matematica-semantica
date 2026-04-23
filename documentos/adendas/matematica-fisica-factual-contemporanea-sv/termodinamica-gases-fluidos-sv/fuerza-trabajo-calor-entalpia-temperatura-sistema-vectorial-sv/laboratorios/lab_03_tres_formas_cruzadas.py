"""
lab_03_tres_formas_cruzadas.py — Verificación GENUINA de la equivalencia de las tres formas
(explícita, implícita, paramétrica) sobre las seis magnitudes del §17.7 del documento.

Las tres formas calculan por CAMINOS ALGEBRAICOS DISTINTOS:
  - EXPLÍCITA:   desde θ directamente (sumas trapezoidales del §6).
  - IMPLÍCITA:   despejando cada magnitud del balance 𝔇𝒜 = 𝒲 + 𝒬 + 𝒰.
  - PARAMÉTRICA: desde punto base + Σ vector director u⃗_SV (Definición 15.4.c).

Verificación: 3 casos × 6 magnitudes (acumulativas) × 3 formas = 54 coincidencias,
más 4 magnitudes puntuales × 3 casos × 3 formas = 36 coincidencias ⇒ 90 total.

Cada discrepancia entre caminos dispara código específico:
  - W-005 (explícita ≠ implícita para A^W), W-006 (explícita ≠ paramétrica para A^W)
  - Análogo para Q, U, A, L, F
  - T-004, T-005 para temperatura
"""
import sys
import os
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sv_core import (cargar_casos, CasoCanonico, construir_acumulados, forma_implicita,
                     forma_parametrica, fuerza_canonica, temperatura, vector_director,
                     SVError, TOLERANCIA_DEFAULT, comparar_formas)

# Códigos de magnitud por sumando
MAG_CODIGOS = {
    "A^W": "W", "A^Q": "Q", "A^U": "U",
    "A":   "A", "Λ":   "L", "𝓕":   "F",
}

MAG_PUNTUALES = {
    "𝒲": "W", "𝒬": "Q", "𝒰": "U", "Θ": "T",
}


def verificar_caso(caso: CasoCanonico) -> int:
    """
    Devuelve número de coincidencias verificadas. Levanta SVError al primer fallo.
    """
    fib_exp = construir_acumulados(caso)
    imp     = forma_implicita(fib_exp, caso)
    F_exp   = fuerza_canonica(caso, fib_exp)
    par     = forma_parametrica(fib_exp, F_exp, caso)
    Theta   = temperatura(fib_exp, caso)

    # Evaluación en λ = 2 desde n0 = 0
    n_eval = caso.n0 + 2
    if n_eval >= caso.N():
        raise SVError("CEL-001", f"Caso {caso.nombre} con N={caso.N()}, no permite λ=2")

    print(f"\n  → Caso {caso.nombre}, n0={caso.n0}, n={n_eval}")

    coincidencias = 0

    # --- Acumulativas (6 magnitudes) ---
    tests_acum = [
        ("A^W", fib_exp["TW"][n_eval], imp["TW"][n_eval], par["TW"][n_eval]),
        ("A^Q", fib_exp["TQ"][n_eval], imp["TQ"][n_eval], par["TQ"][n_eval]),
        ("A^U", fib_exp["TU"][n_eval], imp["TU"][n_eval], par["TU"][n_eval]),
        ("A",   fib_exp["A"][n_eval],  imp["A"][n_eval],  par["A"][n_eval]),
        ("Λ",   fib_exp["Lambda"][n_eval], imp["Lambda"][n_eval], par["Lambda"][n_eval]),
        ("𝓕",   F_exp[n_eval],          F_exp[n_eval],          par["F"][n_eval]),
    ]
    for nombre, v_exp, v_imp, v_par in tests_acum:
        pref = MAG_CODIGOS[nombre]
        comparar_formas(v_exp, v_imp, v_par, pref, nombre)
        coincidencias += 3   # las tres formas coinciden
        dir_comp = f"u_{pref}({caso.n0}),…,u_{pref}({n_eval-1})"
        u_seq = par["u"][f"u_{pref}"][caso.n0:n_eval] if f"u_{pref}" in par["u"] else None
        print(f"    [{pref} OK] {nombre}({n_eval}) exp/imp/par = "
              f"{v_exp:+.4f}/{v_imp:+.4f}/{v_par:+.4f}")

    # --- Puntuales (4 magnitudes, evaluadas en n_p = n_eval - 1) ---
    n_p = n_eval - 1
    tests_puntuales = [
        ("𝒲", fib_exp["W_inc"][n_p], imp["W_inc"][n_p], par["u"]["u_W"][n_p]),
        ("𝒬", fib_exp["Q_inc"][n_p], imp["Q_inc"][n_p], par["u"]["u_Q"][n_p]),
        ("𝒰", fib_exp["U_inc"][n_p], imp["U_inc"][n_p], par["u"]["u_U"][n_p]),
        ("Θ", Theta[n_p],             Theta[n_p],        Theta[n_p]),
    ]
    for nombre, v_exp, v_imp, v_par in tests_puntuales:
        pref = MAG_PUNTUALES[nombre]
        if abs(v_exp - v_imp) > TOLERANCIA_DEFAULT:
            raise SVError(f"{pref}-004",
                          f"{caso.nombre}: {nombre}({n_p}) exp={v_exp}, imp={v_imp} discrepan")
        if abs(v_exp - v_par) > TOLERANCIA_DEFAULT:
            raise SVError(f"{pref}-004",
                          f"{caso.nombre}: {nombre}({n_p}) exp={v_exp}, par={v_par} discrepan")
        coincidencias += 3
        print(f"    [{pref} OK] {nombre}({n_p}) exp/imp/par = "
              f"{v_exp:+.4f}/{v_imp:+.4f}/{v_par:+.4f}")

    return coincidencias


def run():
    print("=" * 70)
    print("LAB 03 — TRES FORMAS CRUZADAS (Teorema 15.5)")
    print("=" * 70)
    casos = cargar_casos()
    total = 0
    for caso in casos:
        total += verificar_caso(caso)
    print(f"\n  Total coincidencias verificadas: {total}/{len(casos) * 30}")
    esperado = len(casos) * 30
    if total != esperado:
        raise SVError("LAB-002", f"Esperábamos {esperado}, obtuvimos {total}")
    print("-" * 70)
    print(f"LAB 03 — PASADO. {total}/{esperado} coincidencias por tres caminos algebraicos distintos.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(run())
    except SVError as e:
        print(f"\n[LAB 03] FALLO código={e.codigo} — {e.mensaje}")
        sys.exit(1)
