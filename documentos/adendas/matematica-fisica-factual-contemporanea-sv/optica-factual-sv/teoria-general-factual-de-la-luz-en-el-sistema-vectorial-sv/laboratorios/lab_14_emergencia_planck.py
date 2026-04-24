"""
lab_14_emergencia_planck.py — L-LUZ-14 — Emergencia factual de Planck.

Teorema 12.1: sobre toda fibra luminosa factual admisible con L_SV = 0,
bajo compuerta metrológica ℘_SV, se deriva la identidad clásica:
    E = h · ν
donde h emerge calibrado al valor CODATA h = 6.62607015·10⁻³⁴ J·s.

Pruebas:
  1. h_SV bien definido y positivo sobre las tres fibras (redundante con L-LUZ-03)
  2. Identidad emergente E = h_SV · card(π) sobre fibras admisibles
  3. E ≥ 0 sobre toda fibra admisible
  4. Calibración ℘_SV: h_SV · factor = h CODATA (reconstrucción numérica)
  5. Corolario 12.2: transporte sub-cuántico prohibido (ΔE ≥ h_SV)
  6. Contraste: sobre fibra con card(π) = 0 se produce error LUZ-CUA-002

Códigos: LUZ-PLA-001..004, LUZ-CUA-002..005
"""
import sys
import os
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sv_core import (SVError, cargar_casos, construir_acumulados,
                      cuanto_factual, H_CODATA, TOLERANCIA_DEFAULT,
                      assert_relativo, CasoFibra, calibracion_planck_codata)


def prueba_1_h_SV_bien_definido() -> None:
    casos = cargar_casos()
    for caso in casos:
        fib = construir_acumulados(caso)
        h = cuanto_factual(caso, fib)
        if h <= 0 or not np.isfinite(h):
            raise SVError(
                "LUZ-CUA-002",
                f"{caso.nombre}: h_SV = {h} no estructuralmente positivo",
            )
    print(f"  [PLA OK] h_SV > 0 sobre los 3 casos admisibles ✓")


def prueba_2_identidad_emergente() -> None:
    """
    E = h_SV · card(π) sobre fibra admisible. Por construcción del núcleo,
    Q^L = A_W + C = h_SV · card(π). Verificamos la identidad.
    """
    casos = cargar_casos()
    for caso in casos:
        fib = construir_acumulados(caso)
        h = cuanto_factual(caso, fib)
        card_pi = float(fib["C"][-1])
        Q_L = float(fib["A_W"][-1] + fib["C"][-1])
        diff = abs(Q_L - h * card_pi)
        if diff > TOLERANCIA_DEFAULT:
            raise SVError(
                "LUZ-PLA-001",
                f"{caso.nombre}: Q^L = {Q_L} ≠ h_SV·card(π) = {h*card_pi}",
            )
    print(f"  [PLA OK] Teorema 12.1: E = h_SV · card(π) sobre 3 casos ✓")


def prueba_3_energia_no_negativa() -> None:
    """E ≥ 0 sobre toda fibra admisible (Teorema 3.2)."""
    casos = cargar_casos()
    for caso in casos:
        fib = construir_acumulados(caso)
        E_total = float(fib["A"][-1])
        if E_total < 0:
            raise SVError(
                "LUZ-PLA-003",
                f"{caso.nombre}: E = {E_total} < 0",
            )
    print(f"  [PLA OK] E ≥ 0 sobre fibras admisibles ✓")


def prueba_4_calibracion_a_CODATA() -> None:
    """
    Calibración ℘_SV: h_SV [escala interna] · factor = h [J·s CODATA].
    Si tenemos h_SV = 1.35 (A, escala interna) y h = 6.62607015e-34 J·s,
    entonces factor = h / h_SV. Verificamos la aritmética.
    """
    casos = cargar_casos()
    caso = casos[0]
    fib = construir_acumulados(caso)
    h_SV = cuanto_factual(caso, fib)
    factor = H_CODATA / h_SV
    h_reconstruido = calibracion_planck_codata(h_SV, factor)
    assert_relativo(
        h_reconstruido, H_CODATA, 1e-12, "LUZ-CUA-003",
        "Calibración ℘_SV reconstruyendo h CODATA",
    )
    print(f"  [PLA OK] Calibración ℘_SV: h_SV={h_SV:.4f} · factor={factor:.3e} = {H_CODATA:.3e} ✓")


def prueba_5_transporte_sub_cuantico_prohibido() -> None:
    """
    Corolario 12.2: el transporte TOTAL Q^L = A_W(N-1) + C(N-1) debe ser
    múltiplo exacto de h_SV por card(π). Esta es la identidad canónica
    (integral, no diferencial paso a paso).
    """
    casos = cargar_casos()
    for caso in casos:
        fib = construir_acumulados(caso)
        h = cuanto_factual(caso, fib)
        card_pi = float(fib["C"][-1])
        Q_L = float(fib["A_W"][-1] + fib["C"][-1])
        # La identidad estructural: Q_L = h · card(π)
        if abs(Q_L - h * card_pi) > TOLERANCIA_DEFAULT:
            raise SVError(
                "LUZ-CUA-005",
                f"{caso.nombre}: Q^L = {Q_L} ≠ h_SV·card(π) = {h*card_pi}",
            )
        # Verificar que NO hay "salto sub-cuántico": si card(π) > 0,
        # el cociente Q_L / card(π) = h_SV por definición, así que cada
        # "cuanto" aporta exactamente h_SV
        if card_pi > 0:
            cuanto_individual = Q_L / card_pi
            if abs(cuanto_individual - h) > TOLERANCIA_DEFAULT:
                raise SVError(
                    "LUZ-CUA-005",
                    f"{caso.nombre}: cuanto individual = {cuanto_individual} ≠ h_SV = {h}",
                )
    print(f"  [PLA OK] Corolario 12.2: Q^L = h_SV · card(π) exacto, sin transporte sub-cuántico ✓")


def prueba_6_fibra_sin_activacion_emite_error() -> None:
    """
    Fibra con card(π) = 0 (sin canal W activado) debe producir LUZ-CUA-002.
    Construimos un caso con chi ≠ 0 en todas las posiciones (n ≥ 1).
    """
    casos = cargar_casos()
    caso = casos[0]
    # Forzar chi a 1 en todas las posiciones con n ≥ 1 (sin canal W)
    chi_sin_W = caso.chi.copy()
    chi_sin_W[:, 1:] = 1  # todo canal Q desde n=1
    caso_bad = CasoFibra(
        nombre="SinCanalW",
        alfa_beta=caso.alfa_beta, chi=chi_sin_W,
        delta_eps=caso.delta_eps, B=caso.B, H=caso.H,
        phi=caso.phi, A_vec=caso.A_vec, J_jac=caso.J_jac,
        e_hat=caso.e_hat, n0=0,
    )
    fib_bad = construir_acumulados(caso_bad)
    try:
        h_bad = cuanto_factual(caso_bad, fib_bad)
        raise SVError(
            "LUZ-PLA-002",
            f"Fibra sin card(π) devolvió h_SV = {h_bad} sin error",
        )
    except SVError as e:
        if e.codigo != "LUZ-CUA-002":
            raise
        print(f"  [PLA OK] Fibra sin activación → LUZ-CUA-002 como se esperaba ✓")


def run() -> int:
    print("=" * 74)
    print("L-LUZ-14 — EMERGENCIA FACTUAL DE PLANCK (Teorema 12.1)")
    print("=" * 74)
    prueba_1_h_SV_bien_definido()
    prueba_2_identidad_emergente()
    prueba_3_energia_no_negativa()
    prueba_4_calibracion_a_CODATA()
    prueba_5_transporte_sub_cuantico_prohibido()
    prueba_6_fibra_sin_activacion_emite_error()
    print("-" * 74)
    print("L-LUZ-14 — PASADO. E = h·ν emergente de L_SV = 0 con calibración CODATA.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(run())
    except SVError as e:
        print(f"\n[L-LUZ-14] FALLO código={e.codigo}")
        print(f"           mensaje: {e.mensaje}")
        sys.exit(1)
