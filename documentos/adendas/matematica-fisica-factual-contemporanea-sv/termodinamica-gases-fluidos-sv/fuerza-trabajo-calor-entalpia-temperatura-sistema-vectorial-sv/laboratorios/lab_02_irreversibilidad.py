"""
lab_02_irreversibilidad.py — Verificación del Teorema 8.2 (irreversibilidad factual).

Teorema 8.2:  𝔇_Γ 𝓗_SV(Γ, n) ≥ 0     sobre toda Γ admisible.

Pruebas:
  1. Sobre los tres casos A, B, C: 𝔇_Γ 𝓗 ≥ 0 en cada paso.
  2. Verificación de 𝓗 ≥ 0 absolutamente (no puede haber entropía negativa).
  3. Contraste por contradicción: perturbación decreciente inyectada. Se genera
     caso con H(n+1) < H(n) en un punto; se verifica que IRR-001 se dispara.
  4. Verificación de que el append-only del documento (Lema 5.5 Lloret Egea 2026j)
     es condición suficiente para 𝓗 no decreciente.

Códigos: IRR-001..003, H-001..003.
"""
import sys
import os
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sv_core import (cargar_casos, CasoCanonico, construir_acumulados,
                     SVError, TOLERANCIA_DEFAULT)


def verificar_monotonia(caso: CasoCanonico) -> None:
    """𝔇_Γ 𝓗 ≥ 0 estricto."""
    DH = np.diff(caso.H)
    min_DH = float(DH.min()) if DH.size else 0.0
    # Tolerancia: DH puede ser exactamente cero; negativo significativo no admitido
    if min_DH < -TOLERANCIA_DEFAULT:
        raise SVError("IRR-001",
                      f"{caso.nombre}: 𝔇_Γ 𝓗 mínimo = {min_DH:.3e} < 0 en algún paso")
    # 𝓗 ≥ 0 en cada suceso
    if float(caso.H.min()) < -TOLERANCIA_DEFAULT:
        raise SVError("H-002", f"{caso.nombre}: entropía mínima = {caso.H.min()} < 0")
    print(f"  [IRR OK] {caso.nombre}: min 𝔇𝓗 = {min_DH:.3e} ≥ 0;  min 𝓗 = {caso.H.min():.3e} ≥ 0")


def contraste_por_contradiccion(caso: CasoCanonico) -> None:
    """
    Generamos un caso contrafáctico con entropía decreciente y verificamos que la
    validación del caso dispara IRR-002 (vía validar() de CasoCanonico).
    """
    H_mala = caso.H.copy()
    # Forzar H(1) < H(0) insertando un decremento visible
    H_mala[1] = caso.H[0] - 0.01
    caso_malo = CasoCanonico(
        nombre=f"{caso.nombre} [H-decreciente artificial]",
        alfa_beta=caso.alfa_beta, chi=caso.chi, delta_eps=caso.delta_eps,
        B=caso.B, H=H_mala, phi=caso.phi, A_vec=caso.A_vec,
        J_jac=caso.J_jac, e_hat=caso.e_hat, n0=caso.n0,
    )
    try:
        caso_malo.validar()
    except SVError as e:
        if e.codigo == "IRR-002":
            print(f"  [IRR-002 OK] {caso.nombre}: decremento artificial rechazado correctamente.")
            return
        # Otro código: eso es problema — esperábamos IRR-002 exacto
        raise SVError("LAB-002",
                      f"Esperábamos IRR-002 al validar H decreciente, "
                      f"pero se obtuvo '{e.codigo}'. Contraste adversarial no discriminó.")
    # Si no levantó excepción, la validación es permisiva: LAB-002
    raise SVError("LAB-002",
                  f"{caso.nombre}: validación aceptó H decreciente sin levantar IRR-002. "
                  f"Pase silencioso detectado.")


def verificar_acoplamiento_append_only(caso: CasoCanonico) -> None:
    """
    Append-only + activación ≥ 0 ⇒ 𝒜 no decrece ⇒ 𝓗 construido como
    función de 𝒜, 𝓥, ℛ, 𝒥, ℬ no puede decrecer.
    Verificamos 𝒜 no decreciente como condición estructural.
    """
    fib = construir_acumulados(caso)
    A = fib["A"]
    if np.any(np.diff(A) < -TOLERANCIA_DEFAULT):
        raise SVError("A-001", f"{caso.nombre}: 𝒜_SV decreciente (append-only violado)")
    # 𝓗 debe ser compatible: no decrece sobre trayectorias admisibles
    DH = np.diff(caso.H)
    if np.any(DH < -TOLERANCIA_DEFAULT):
        raise SVError("IRR-003", f"{caso.nombre}: incompatibilidad entre append-only (𝒜↑) y 𝓗↓")
    print(f"  [append-only OK] {caso.nombre}: 𝒜 no decrece y 𝓗 no decrece.")


def run():
    print("=" * 70)
    print("LAB 02 — IRREVERSIBILIDAD FACTUAL (Teorema 8.2)")
    print("=" * 70)
    casos = cargar_casos()
    for caso in casos:
        verificar_monotonia(caso)
    for caso in casos:
        contraste_por_contradiccion(caso)
    for caso in casos:
        verificar_acoplamiento_append_only(caso)
    print("-" * 70)
    print("LAB 02 — PASADO. Teorema 8.2 verificado; contraste adversarial discrimina IRR-002.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(run())
    except SVError as e:
        print(f"\n[LAB 02] FALLO código={e.codigo} — {e.mensaje}")
        sys.exit(1)
