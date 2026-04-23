"""
lab_06_absorcion_limite_clasica.py — Verificación de la absorción límite (§10).

Teorema de absorción: en régimen de clausura total (χ ∈ {0,1}, 𝒰=0) el aparato
factual recupera:
  1. Primer principio:    dU = δW + δQ   ⇔   𝔇_Γ 𝒜 = 𝒲 + 𝒬
  2. Identidad de Gibbs:  T·dS = δQ      ⇔   Θ·𝔇_Γ 𝓗 = 𝔇_Γ 𝒬

Pruebas:
  1. Forzar χ=U → χ=0 en los tres casos. Verificar 𝔇𝒜 = 𝒲+𝒬 estricto.
  2. Verificar Θ · 𝔇𝓗 = 𝔇𝒬 en el régimen reducido.
  3. Verificar que el "límite clásico" del SV es 𝒰 ≡ 0 (no hay término residual).

Códigos: BAL-005, T-003, U-008 (en caso de contaminación residual de U).
"""
import sys
import os
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sv_core import (cargar_casos, CasoCanonico, construir_acumulados,
                     temperatura, SVError, TOLERANCIA_DEFAULT)


def regimen_clausura_total(caso: CasoCanonico) -> CasoCanonico:
    chi_cerr = np.where(caso.chi == 2, 0, caso.chi)
    return CasoCanonico(
        nombre=f"{caso.nombre} [clausura→clásico]",
        alfa_beta=caso.alfa_beta, chi=chi_cerr, delta_eps=caso.delta_eps,
        B=caso.B, H=caso.H, phi=caso.phi, A_vec=caso.A_vec,
        J_jac=caso.J_jac, e_hat=caso.e_hat, n0=caso.n0,
    )


def verificar_primer_principio(caso_mod: CasoCanonico) -> None:
    """𝔇𝒜 = 𝒲 + 𝒬 (sin 𝒰)"""
    fib = construir_acumulados(caso_mod)
    if not np.allclose(fib["U_inc"], 0.0, atol=TOLERANCIA_DEFAULT):
        raise SVError("U-008", f"{caso_mod.nombre}: 𝒰 ≠ 0 en régimen clausura")
    DA = fib["DA"][:-1]
    suma = fib["W_inc"][:-1] + fib["Q_inc"][:-1]
    res = float(np.max(np.abs(DA - suma)))
    if res > TOLERANCIA_DEFAULT:
        raise SVError("BAL-005", f"{caso_mod.nombre}: primer principio violado; res={res:.3e}")
    print(f"  [1er ppio OK] {caso_mod.nombre}: 𝔇𝒜 = 𝒲+𝒬 residuo {res:.2e}  ←→  dU = δW+δQ")


def verificar_identidad_Gibbs(caso_mod: CasoCanonico) -> None:
    """Θ · 𝔇𝓗 = 𝔇𝒬 en régimen clausura (equivalencia T·dS = δQ)"""
    fib = construir_acumulados(caso_mod)
    Theta = temperatura(fib, caso_mod)
    DH = np.diff(caso_mod.H)
    DQ = fib["Q_inc"][:-1]
    term = DH > 1e-12
    if term.sum() == 0:
        print(f"  [Gibbs SK] {caso_mod.nombre}: régimen no térmico, identidad trivial")
        return
    producto = Theta[:-1][term] * DH[term]
    res = float(np.max(np.abs(producto - DQ[term])))
    if res > TOLERANCIA_DEFAULT:
        raise SVError("T-003", f"{caso_mod.nombre}: Θ·𝔇𝓗 ≠ 𝔇𝒬; residuo {res:.3e}")
    print(f"  [Gibbs OK] {caso_mod.nombre}: Θ·𝔇𝓗 = 𝔇𝒬 residuo {res:.2e}  ←→  T·dS = δQ")


def verificar_no_residuo_U(caso_mod: CasoCanonico) -> None:
    """Verifica que el canal U no deja residuo fantasma en caso de clausura."""
    fib = construir_acumulados(caso_mod)
    if not np.allclose(fib["A_U"], 0.0, atol=TOLERANCIA_DEFAULT):
        raise SVError("U-001", f"{caso_mod.nombre}: A^U ≠ 0 pese a clausura total")
    if not np.allclose(fib["a_U"], 0.0, atol=TOLERANCIA_DEFAULT):
        raise SVError("U-002", f"{caso_mod.nombre}: a_U ≠ 0 pese a clausura")
    print(f"  [U≡0 OK] {caso_mod.nombre}: canal U totalmente vacío.")


def run():
    print("=" * 70)
    print("LAB 06 — ABSORCIÓN LÍMITE CLÁSICA (§10)")
    print("=" * 70)
    casos = cargar_casos()
    for caso in casos:
        caso_mod = regimen_clausura_total(caso)
        verificar_primer_principio(caso_mod)
        verificar_identidad_Gibbs(caso_mod)
        verificar_no_residuo_U(caso_mod)
    print("-" * 70)
    print("LAB 06 — PASADO. Primer principio y Gibbs recuperados en régimen clausura.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(run())
    except SVError as e:
        print(f"\n[LAB 06] FALLO código={e.codigo} — {e.mensaje}")
        sys.exit(1)
