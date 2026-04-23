"""
lab_11_celula_canonica_sv3_9.py — Verificación del Teorema 11.1 (consistencia
sobre la célula canónica SV(3, 9)).

Teorema 11.1 (§11 del documento): sobre la célula canónica mínima SV(3, 9) — es
decir, sobre 3 coordenadas factuales y 9 sucesos con rotación sistemática de los
tres canales χ ∈ {0, 1, U}, todas las magnitudes del dominio termodinámico factual
del SV son consistentes por tres vías independientes:
  (a) Balance canónico  𝔇_Γ 𝒜 = 𝒲 + 𝒬 + 𝒰
  (b) Irreversibilidad   𝔇_Γ 𝓗 ≥ 0
  (c) Identidad termométrica  Θ · 𝔇_Γ 𝓗 = 𝔇_Γ 𝒬

Construcción de SV(3, 9): matriz χ con rotación estricta de los tres canales
sobre las tres coordenadas y nueve sucesos. Cada canal recibe exactamente 9
activaciones (3 por coordenada). La célula es la unidad mínima que verifica la
partición ternaria completa al activar los tres canales por igual.

Códigos: CEL-001..003, BAL-002, IRR-001, T-003.
"""
import sys
import os
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sv_core import (CasoCanonico, construir_acumulados, temperatura,
                     fuerza_canonica, vector_director, producto_G, G_SV,
                     SVError, TOLERANCIA_DEFAULT)


def construir_celula_canonica() -> CasoCanonico:
    """
    Célula canónica SV(3, 9).
    
    χ matriz 3×9: rotación ternaria sistemática.
      coord 0: 0 1 2 0 1 2 0 1 2
      coord 1: 1 2 0 1 2 0 1 2 0
      coord 2: 2 0 1 2 0 1 2 0 1
    
    Cada canal χ ∈ {0, 1, 2} aparece exactamente 3 veces por coordenada, 9 veces total.
    Las activaciones a_i(k) = |β-α| se diseñan para que cada canal aporte cantidades
    bien definidas sobre el cómputo.
    """
    chi = np.array([
        [0, 1, 2, 0, 1, 2, 0, 1, 2],
        [1, 2, 0, 1, 2, 0, 1, 2, 0],
        [2, 0, 1, 2, 0, 1, 2, 0, 1],
    ], dtype=int)
    # Pares preternarios (α, β) por coordenada y suceso (3×9×2)
    rng = np.random.default_rng(seed=33)
    alfa = rng.uniform(0.0, 0.3, size=(3, 9))
    beta = alfa + rng.uniform(0.2, 0.5, size=(3, 9))
    alfa_beta = np.stack([alfa, beta], axis=-1)   # shape (3, 9, 2)
    delta_eps = np.ones(8)   # N-1 = 8 pesos
    B   = np.linspace(0.0, 4.0, 9)                 # frontera creciente
    H   = np.linspace(0.0, 2.0, 9)                 # entropía creciente
    phi = np.linspace(0.2, 1.8, 9)                 # potencial escalar
    A_vec = np.linspace(0.1, 1.6, 9)               # potencial vectorial escalar
    J_jac = np.linspace(0.1, 0.9, 9)               # jacobiano escalar
    e_hat = np.ones(9)                             # versor canónico
    return CasoCanonico(
        nombre="SV(3, 9) — célula canónica",
        alfa_beta=alfa_beta, chi=chi, delta_eps=delta_eps,
        B=B, H=H, phi=phi, A_vec=A_vec,
        J_jac=J_jac, e_hat=e_hat, n0=0,
    )


def verificar_celula_estructura(celula: CasoCanonico) -> None:
    """Verifica que la célula tiene d=3 y N=9, partición ternaria completa."""
    if celula.d() != 3:
        raise SVError("CEL-002", f"Célula tiene d={celula.d()}, se requiere d=3")
    if celula.N() != 9:
        raise SVError("CEL-001", f"Célula tiene N={celula.N()}, se requiere N=9")
    # Verificar que cada canal aparece 9 veces (3 por coordenada)
    for canal_val, canal_nombre in [(0, "W"), (1, "Q"), (2, "U")]:
        conteos = (celula.chi == canal_val).sum(axis=1)
        if not np.all(conteos == 3):
            raise SVError("CEL-003",
                          f"Canal {canal_nombre} con distribución asimétrica: {conteos} (se esperaban 3 por coord)")
    print(f"  [CEL estructura OK] SV(3, 9) con d=3, N=9, partición ternaria simétrica (9 por canal).")


def verificar_balance_sobre_celula(celula: CasoCanonico) -> dict:
    """Teorema 11.1(a): 𝔇𝒜 = 𝒲 + 𝒬 + 𝒰 sobre los 8 pasos de la célula."""
    fib = construir_acumulados(celula)
    DA = fib["DA"][:-1]
    suma = fib["W_inc"][:-1] + fib["Q_inc"][:-1] + fib["U_inc"][:-1]
    residuo = DA - suma
    max_res = float(np.max(np.abs(residuo)))
    if max_res > TOLERANCIA_DEFAULT:
        raise SVError("BAL-002",
                      f"Célula SV(3,9): residuo max |𝔇𝒜−𝒲−𝒬−𝒰| = {max_res:.3e} > tol")
    print(f"  [CEL balance OK] Residuo máx en 8 pasos = {max_res:.2e}")
    # Totales por canal
    print(f"      A^W(9) = {fib['A_W'][-1]:.4f}")
    print(f"      A^Q(9) = {fib['A_Q'][-1]:.4f}")
    print(f"      A^U(9) = {fib['A_U'][-1]:.4f}")
    print(f"      𝒜(9)   = {fib['A'][-1]:.4f}")
    return fib


def verificar_irreversibilidad_sobre_celula(celula: CasoCanonico) -> None:
    """Teorema 11.1(b): 𝓗 no decrece en la célula."""
    DH = np.diff(celula.H)
    min_DH = float(DH.min())
    if min_DH < -TOLERANCIA_DEFAULT:
        raise SVError("IRR-001",
                      f"Célula SV(3,9): 𝔇𝓗 mínimo = {min_DH:.3e} < 0")
    print(f"  [CEL irrev OK] 𝔇𝓗 ≥ 0 en los 8 pasos (min = {min_DH:.4f})")


def verificar_identidad_Theta_sobre_celula(celula: CasoCanonico, fib: dict) -> None:
    """Teorema 11.1(c): Θ·𝔇𝓗 = 𝔇𝒬 sobre cada paso térmico."""
    Theta = temperatura(fib, celula)
    DH = np.diff(celula.H)
    DQ = fib["Q_inc"][:-1]
    termicos = DH > 1e-12
    if termicos.sum() == 0:
        raise SVError("T-002",
                      f"Célula SV(3,9) sin pasos térmicos; régimen degenerado")
    producto = Theta[:-1][termicos] * DH[termicos]
    residuo = producto - DQ[termicos]
    max_res = float(np.max(np.abs(residuo)))
    if max_res > TOLERANCIA_DEFAULT:
        raise SVError("T-003",
                      f"Célula SV(3,9): Θ·𝔇𝓗 ≠ 𝔇𝒬 en paso térmico; residuo {max_res:.3e}")
    print(f"  [CEL identidad Θ OK] Θ·𝔇𝓗 = 𝔇𝒬 en {termicos.sum()} pasos térmicos; residuo {max_res:.2e}")


def verificar_ortogonalidad_sobre_celula(celula: CasoCanonico, fib: dict) -> None:
    """Ortogonalidad u⃗·𝖦 = 0 en cada uno de los 8 pasos."""
    F = fuerza_canonica(celula, fib)
    u = vector_director(fib, F, celula)
    max_err = 0.0
    for j in range(celula.N() - 1):
        u_B = float(celula.B[j+1] - celula.B[j])
        u_ext = np.array([
            u["u_A"][j], u["u_H"][j], 0.0, 0.0, u_B,
            u["u_W"][j], u["u_Q"][j], u["u_U"][j],
        ])
        valor = producto_G(u_ext)
        max_err = max(max_err, abs(valor))
        if abs(valor) > TOLERANCIA_DEFAULT:
            raise SVError("ORT-001",
                          f"Célula SV(3,9) paso j={j}: u·𝖦 = {valor:.3e}")
    print(f"  [CEL ortogonalidad OK] max|u⃗·𝖦| = {max_err:.2e} sobre los 8 pasos")


def contraste_con_celula_truncada() -> None:
    """Contraste: una célula SV(3, 7) debería fallar el test CEL-001 del §17.4."""
    chi = np.array([
        [0, 1, 2, 0, 1, 2, 0],
        [1, 2, 0, 1, 2, 0, 1],
        [2, 0, 1, 2, 0, 1, 2],
    ], dtype=int)
    alfa = np.full((3, 7), 0.1)
    beta = np.full((3, 7), 0.4)
    alfa_beta = np.stack([alfa, beta], axis=-1)
    trunc = CasoCanonico(
        nombre="SV(3, 7) — truncada",
        alfa_beta=alfa_beta, chi=chi, delta_eps=np.ones(6),
        B=np.linspace(0, 3, 7), H=np.linspace(0, 1.5, 7),
        phi=np.linspace(0.1, 1.5, 7), A_vec=np.linspace(0.1, 1.3, 7),
        J_jac=np.ones(7)*0.3, e_hat=np.ones(7), n0=0,
    )
    if trunc.N() >= 9:
        raise SVError("LAB-002", "Célula de contraste tiene N=9, debería ser truncada")
    # Verificar que esta célula no satisface el conteo 3 por coordenada por canal:
    for canal_val in [0, 1, 2]:
        conteos = (trunc.chi == canal_val).sum(axis=1)
        if np.all(conteos == 3):
            raise SVError("LAB-002",
                          f"Célula truncada presenta conteos perfectos (imposible con N=7)")
    print(f"  [Contraste OK] SV(3, 7) no cumple conteo canónico 3 por canal; "
          f"condición CEL-001 identifica la diferencia estructural.")


def run():
    print("=" * 70)
    print("LAB 11 — CÉLULA CANÓNICA SV(3, 9) (Teorema 11.1)")
    print("=" * 70)
    celula = construir_celula_canonica()
    verificar_celula_estructura(celula)
    fib = verificar_balance_sobre_celula(celula)
    verificar_irreversibilidad_sobre_celula(celula)
    verificar_identidad_Theta_sobre_celula(celula, fib)
    verificar_ortogonalidad_sobre_celula(celula, fib)
    contraste_con_celula_truncada()
    print("-" * 70)
    print("LAB 11 — PASADO. SV(3, 9) consistente por tres vías (balance, irrev, Θ).")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(run())
    except SVError as e:
        print(f"\n[LAB 11] FALLO código={e.codigo} — {e.mensaje}")
        sys.exit(1)
