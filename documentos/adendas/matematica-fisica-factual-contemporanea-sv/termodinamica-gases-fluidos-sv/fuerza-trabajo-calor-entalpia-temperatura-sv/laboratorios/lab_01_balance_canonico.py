"""
lab_01_balance_canonico.py — Verificación del Teorema 8.1 (balance canónico).

Teorema 8.1:   𝔇_Γ 𝒜_SV(Γ,n) = 𝒲_SV(Γ,n) + 𝒬_SV(Γ,n) + 𝒰_SV(Γ,n)

Pruebas:
  1. Residuo |𝔇𝒜 − 𝒲 − 𝒬 − 𝒰| sobre los tres casos canónicos A, B, C.
  2. Régimen adiabático factual (𝒬 = 0) degenerado: balance se reduce a 𝔇𝒜 = 𝒲 + 𝒰.
  3. Régimen de clausura total (𝒰 = 0): balance se reduce a 𝔇𝒜 = 𝒲 + 𝒬.
  4. Contraste por contradicción: insertar un cuarto término ficticio y verificar que
     el residuo se hace no nulo (BAL-003).
  5. Tolerancia estricta: 1e-9 absoluto. Cualquier residuo mayor dispara BAL-001.

Códigos: BAL-001..005, CHI-001..004 (si los casos generados violan χ)
"""
import sys
import os
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sv_core import (cargar_casos, construir_acumulados, SVError,
                     TOLERANCIA_DEFAULT, CasoCanonico)


def verificar_balance_caso(fib: dict, nombre: str) -> None:
    """
    Teorema 8.1 estricto: 𝔇𝒜 = 𝒲 + 𝒬 + 𝒰 sobre cada paso.
    """
    DA = fib["DA"][:-1]
    suma = fib["W_inc"][:-1] + fib["Q_inc"][:-1] + fib["U_inc"][:-1]
    residuo = DA - suma
    max_res = float(np.max(np.abs(residuo)))
    if max_res > TOLERANCIA_DEFAULT:
        raise SVError("BAL-001",
                      f"Caso '{nombre}': residuo máximo |𝔇𝒜−𝒲−𝒬−𝒰| = {max_res:.3e} "
                      f"supera tolerancia {TOLERANCIA_DEFAULT}")
    print(f"  [BAL OK] {nombre}: residuo máx = {max_res:.2e}")


def verificar_contraste_cuarto_termino(fib: dict, nombre: str) -> None:
    """
    Contraste por contradicción §3.2: 𝔇𝒜 − 𝒲 − 𝒬 − 𝒰 − X = 0 sólo si X ≡ 0.
    Insertamos X = 0.1 artificial y verificamos que el residuo se hace no nulo.
    Si a pesar de ello el residuo fuera nulo, hay un cuarto canal oculto: BAL-003.
    """
    DA = fib["DA"][:-1]
    suma = fib["W_inc"][:-1] + fib["Q_inc"][:-1] + fib["U_inc"][:-1]
    X_ficticio = 0.1
    residuo_con_X = DA - suma - X_ficticio
    if np.allclose(residuo_con_X, 0.0, atol=TOLERANCIA_DEFAULT):
        raise SVError("BAL-003",
                      f"Caso '{nombre}': un cuarto término X={X_ficticio} cancela el balance; "
                      f"imposible por §3.2. Hay canal oculto.")
    # En el régimen correcto, residuo ≈ -0.1 en cada paso
    if not np.allclose(residuo_con_X, -X_ficticio, atol=TOLERANCIA_DEFAULT):
        # El residuo no es constantemente -0.1: hay otra inconsistencia
        raise SVError("BAL-001",
                      f"Caso '{nombre}': residuo con cuarto término no coincide con -X; "
                      f"valores: {residuo_con_X}")
    print(f"  [BAL-003 OK] {nombre}: cuarto término rechazado correctamente.")


def verificar_adiabatico(caso: CasoCanonico) -> None:
    """
    Régimen adiabático factual: forzamos χ = U donde había χ = 1.
    Entonces 𝒬 debería ser 0 y el balance 𝔇𝒜 = 𝒲 + 𝒰.
    BAL-004 si no se cumple.
    """
    chi_adiabatico = np.where(caso.chi == 1, 2, caso.chi)
    caso_mod = CasoCanonico(
        nombre=f"{caso.nombre} [adiabático]",
        alfa_beta=caso.alfa_beta, chi=chi_adiabatico, delta_eps=caso.delta_eps,
        B=caso.B, H=caso.H, phi=caso.phi, A_vec=caso.A_vec,
        J_jac=caso.J_jac, e_hat=caso.e_hat, n0=caso.n0,
    )
    fib = construir_acumulados(caso_mod)
    if not np.allclose(fib["Q_inc"], 0.0, atol=TOLERANCIA_DEFAULT):
        raise SVError("Q-008", f"{caso_mod.nombre}: 𝒬 no nula pese a χ=1 reemplazado por U")
    DA = fib["DA"][:-1]
    suma = fib["W_inc"][:-1] + fib["U_inc"][:-1]
    res = float(np.max(np.abs(DA - suma)))
    if res > TOLERANCIA_DEFAULT:
        raise SVError("BAL-004", f"{caso_mod.nombre}: balance adiabático 𝔇𝒜 = 𝒲+𝒰 falla, residuo {res:.3e}")
    print(f"  [BAL-004 OK] {caso_mod.nombre}: 𝔇𝒜 = 𝒲 + 𝒰 verificado.")


def verificar_clausura_total(caso: CasoCanonico) -> None:
    """
    Régimen de clausura total: forzamos χ=U a χ=0 (cualquier canal no-U a W).
    Entonces 𝒰 = 0 y el balance se reduce a 𝔇𝒜 = 𝒲 + 𝒬.
    BAL-005 si no se cumple.
    """
    chi_cerr = np.where(caso.chi == 2, 0, caso.chi)
    caso_mod = CasoCanonico(
        nombre=f"{caso.nombre} [clausura total]",
        alfa_beta=caso.alfa_beta, chi=chi_cerr, delta_eps=caso.delta_eps,
        B=caso.B, H=caso.H, phi=caso.phi, A_vec=caso.A_vec,
        J_jac=caso.J_jac, e_hat=caso.e_hat, n0=caso.n0,
    )
    fib = construir_acumulados(caso_mod)
    if not np.allclose(fib["U_inc"], 0.0, atol=TOLERANCIA_DEFAULT):
        raise SVError("U-008", f"{caso_mod.nombre}: 𝒰 no nula pese a ausencia de χ=U")
    DA = fib["DA"][:-1]
    suma = fib["W_inc"][:-1] + fib["Q_inc"][:-1]
    res = float(np.max(np.abs(DA - suma)))
    if res > TOLERANCIA_DEFAULT:
        raise SVError("BAL-005", f"{caso_mod.nombre}: balance clausura total 𝔇𝒜 = 𝒲+𝒬 falla, residuo {res:.3e}")
    print(f"  [BAL-005 OK] {caso_mod.nombre}: 𝔇𝒜 = 𝒲 + 𝒬 verificado.")


def run():
    print("=" * 70)
    print("LAB 01 — BALANCE CANÓNICO (Teorema 8.1)")
    print("=" * 70)
    casos = cargar_casos()
    # Verificación primaria sobre cada caso
    for caso in casos:
        fib = construir_acumulados(caso)
        verificar_balance_caso(fib, caso.nombre)
        verificar_contraste_cuarto_termino(fib, caso.nombre)
    # Regímenes derivados
    for caso in casos:
        verificar_adiabatico(caso)
        verificar_clausura_total(caso)
    print("-" * 70)
    print("LAB 01 — PASADO sin grietas. Teorema 8.1 verificado sobre 3 casos × 3 regímenes.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(run())
    except SVError as e:
        print(f"\n[LAB 01] FALLO código={e.codigo}")
        print(f"         mensaje: {e.mensaje}")
        sys.exit(1)
