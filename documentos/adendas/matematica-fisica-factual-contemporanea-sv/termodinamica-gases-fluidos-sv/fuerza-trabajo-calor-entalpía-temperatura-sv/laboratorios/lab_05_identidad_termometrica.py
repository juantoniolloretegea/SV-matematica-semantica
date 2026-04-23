"""
lab_05_identidad_termometrica.py — Verificación de la identidad termométrica absoluta
§10.4 del documento:   Θ_SV · 𝔇_Γ 𝓗_SV = 𝔇_Γ 𝒬_SV.

Esta identidad es la absorción límite factual de la identidad clásica T·dS = δQ.
Sobre los tres casos canónicos debe cumplirse con residuo estrictamente nulo en
todo paso con 𝔇𝓗 > 0. En regímenes donde 𝔇𝓗 = 0 (no térmicos), Θ es convencional
y la identidad es trivial.

Códigos: T-001..007.
"""
import sys
import os
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sv_core import (cargar_casos, CasoCanonico, construir_acumulados,
                     temperatura, SVError, TOLERANCIA_DEFAULT)


def verificar_identidad_termometrica(caso: CasoCanonico) -> None:
    fib = construir_acumulados(caso)
    Theta = temperatura(fib, caso)
    DH = np.diff(caso.H)
    DQ = fib["Q_inc"][:-1]
    # Θ · 𝔇𝓗 debe igualar 𝔇𝒬 en régimen DH > 0
    pasos_termicos = DH > 1e-12
    pasos_no_termicos = ~pasos_termicos
    if pasos_termicos.sum() == 0:
        raise SVError("T-002",
                      f"{caso.nombre}: 𝔇𝓗 = 0 en todos los pasos; régimen no térmico total, "
                      f"no se puede evaluar identidad §10.4")
    producto = Theta[:-1][pasos_termicos] * DH[pasos_termicos]
    DQ_term  = DQ[pasos_termicos]
    residuo = producto - DQ_term
    max_res = float(np.max(np.abs(residuo))) if residuo.size else 0.0
    if max_res > TOLERANCIA_DEFAULT:
        raise SVError("T-003",
                      f"{caso.nombre}: Θ·𝔇𝓗 ≠ 𝔇𝒬 en régimen térmico; residuo máx = {max_res:.3e}")
    # Θ debe ser ≥ 0 en pasos térmicos (𝔇𝒬 y 𝔇𝓗 son ambos ≥ 0 por construcción)
    neg = (Theta[:-1] < -TOLERANCIA_DEFAULT).sum()
    if neg > 0:
        raise SVError("T-006", f"{caso.nombre}: Θ negativa en {neg} paso(s)")
    print(f"  [T-003 OK] {caso.nombre}: Θ·𝔇𝓗 = 𝔇𝒬 con residuo {max_res:.2e} sobre {pasos_termicos.sum()} pasos térmicos")
    if pasos_no_termicos.sum() > 0:
        # Θ convencional = 0 en pasos no térmicos
        Theta_noT = Theta[:-1][pasos_no_termicos]
        if not np.allclose(Theta_noT, 0.0, atol=TOLERANCIA_DEFAULT):
            raise SVError("T-005",
                          f"{caso.nombre}: Θ ≠ 0 en pasos no térmicos; valores = {Theta_noT}")
        print(f"    (pasos no térmicos {pasos_no_termicos.sum()}: Θ = 0 por convención)")


def contraste_rival_kB(caso: CasoCanonico) -> None:
    """
    Contraste adversarial: rival introduce constante externa k_B. Se verifica que
    la identidad k_B·Θ·𝔇𝓗 = 𝔇𝒬 falla dimensionalmente. Código P5-001.
    """
    k_B = 1.380649e-23
    fib = construir_acumulados(caso)
    Theta = temperatura(fib, caso)
    DH = np.diff(caso.H)
    DQ = fib["Q_inc"][:-1]
    # Evaluar rival
    termicos = DH > 1e-12
    if termicos.sum() == 0:
        return
    lhs_rival = k_B * Theta[:-1][termicos] * DH[termicos]
    rhs = DQ[termicos]
    # Tiene que fallar con divergencia de orden 10^22
    ratio_mean = float(np.mean(rhs / np.maximum(np.abs(lhs_rival), 1e-300)))
    if abs(ratio_mean) < 1e10:
        # Rival coincide — imposible por dimensional
        raise SVError("T-004",
                      f"{caso.nombre}: rival con k_B coincide con LHS canónica (ratio {ratio_mean}); "
                      f"dimensional broken but not detected")
    print(f"  [P5-001 OK] {caso.nombre}: rival con k_B falla por factor {ratio_mean:.2e}")


def run():
    print("=" * 70)
    print("LAB 05 — IDENTIDAD TERMOMÉTRICA Θ·𝔇𝓗 = 𝔇𝒬 (§10.4)")
    print("=" * 70)
    casos = cargar_casos()
    for caso in casos:
        verificar_identidad_termometrica(caso)
        contraste_rival_kB(caso)
    print("-" * 70)
    print("LAB 05 — PASADO. Identidad verificada; rival con k_B descartada dimensionalmente.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(run())
    except SVError as e:
        print(f"\n[LAB 05] FALLO código={e.codigo} — {e.mensaje}")
        sys.exit(1)
