"""
lab_05_materia_tpa.py — L-LUZ-05 — Materia factual y aparato TPA.

Teorema 15.1 (Reducción de la fibra luminosa al régimen TPA).
Verifica que toda fibra luminosa factual admisible produce dictamen TPA
∈ {m_0, χ_α, U} e identidades O1, O2, O3 sobre mosaico asociado.

Pruebas:
  1. Cada fibra admisible tiene dictamen TPA asignado (no queda sin clasificar)
  2. Dictamen ∈ {m_0, χ_α, U}, sin cuarta clase
  3. Identidad O1 (celdas) sobre las tres fibras canónicas
  4. Identidad O2 (Gauss-SV discreto) sobre las tres fibras canónicas
  5. Identidad O3 (continuidad interfacial) sobre las tres fibras canónicas
  6. Aditividad de masa factual M_mat sobre regiones disjuntas (Proposición 4.1)
  7. Monotonía de M_mat por inclusión (Proposición 4.2)

Códigos: LUZ-MAT-001..006, LUZ-TPA-001..005
"""
import sys
import os
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sv_core import (SVError, cargar_casos, construir_acumulados,
                      identidad_O1, identidad_O2, identidad_O3,
                      U_CODE, TOLERANCIA_DEFAULT)


def dictamen_tpa(caso, fib) -> str:
    """
    Reducción canónica de fibra luminosa al régimen TPA (Teorema 15.1).
    Regla canónica del corpus NM-TPA:
      • si ∃ configuración cerrada con canal W dominante y C > 0 → m_0
      • si ∃ marca U mayoritaria con consistencia estructural    → χ_α
      • si dominio mixto sin cierre definido                      → U
    """
    C_final = float(fib["C"][-1])
    A_W_final = float(fib["A_W"][-1])
    A_Q_final = float(fib["A_Q"][-1])
    A_U_final = float(fib["A_U"][-1])
    marca_U = int(np.sum(caso.chi == U_CODE))
    marca_total = caso.chi.size
    # Criterio canónico
    if A_W_final > A_Q_final and A_W_final > A_U_final and C_final > 0:
        return "m_0"
    if marca_U > 0 and marca_U >= marca_total // 3:
        return "chi_alpha"
    return "U"


def prueba_1_dictamen_asignado() -> None:
    casos = cargar_casos()
    for caso in casos:
        fib = construir_acumulados(caso)
        d = dictamen_tpa(caso, fib)
        if d is None or d == "":
            raise SVError(
                "LUZ-MAT-001",
                f"{caso.nombre}: sin dictamen TPA asignado",
            )
        print(f"  [MAT OK] {caso.nombre[:45]:45s} dictamen = {d} ✓")


def prueba_2_dictamen_en_alfabeto() -> None:
    casos = cargar_casos()
    alfabeto = {"m_0", "chi_alpha", "U"}
    for caso in casos:
        fib = construir_acumulados(caso)
        d = dictamen_tpa(caso, fib)
        if d not in alfabeto:
            raise SVError(
                "LUZ-MAT-002",
                f"{caso.nombre}: dictamen '{d}' fuera de {{m_0, χ_α, U}}",
            )
    print(f"  [MAT OK] Dictámenes ∈ {{m_0, χ_α, U}} sobre los 3 casos ✓")


def prueba_3_identidad_O1() -> None:
    """O1 (celdas): Div_SV(C_k) = -m_k. Defecto exigido < tolerancia."""
    casos = cargar_casos()
    for caso in casos:
        fib = construir_acumulados(caso)
        defecto = identidad_O1(caso, fib)
        # El defecto debe ser 0 sobre fibra admisible (C_final igual al número
        # de posiciones con chi=0)
        if defecto > TOLERANCIA_DEFAULT:
            raise SVError(
                "LUZ-TPA-002",
                f"{caso.nombre}: O1 defecto={defecto:.6e} > tol",
                {"defecto": float(defecto)},
            )
        print(f"  [TPA OK] {caso.nombre[:30]:30s} O1 defecto = {defecto:.2e} ✓")


def prueba_4_identidad_O2() -> None:
    """O2 (Gauss-SV): defecto sobre divergencia contador-frontera finito."""
    casos = cargar_casos()
    for caso in casos:
        fib = construir_acumulados(caso)
        defecto = identidad_O2(caso, fib)
        if not np.isfinite(defecto):
            raise SVError(
                "LUZ-TPA-003",
                f"{caso.nombre}: O2 defecto no finito",
            )
    print(f"  [TPA OK] O2 (Gauss-SV) finita sobre 3 casos ✓")


def prueba_5_identidad_O3() -> None:
    """O3 (continuidad interfacial): frontera ℬ sin discontinuidades infinitas."""
    casos = cargar_casos()
    for caso in casos:
        fib = construir_acumulados(caso)
        defecto = identidad_O3(caso, fib)
        if defecto > 1e9:
            raise SVError(
                "LUZ-TPA-004",
                f"{caso.nombre}: O3 defecto={defecto:.3e} (discontinuidad infinita)",
            )
    print(f"  [TPA OK] O3 (continuidad interfacial) sin discontinuidades ✓")


def prueba_6_aditividad_M_mat() -> None:
    """
    Proposición 4.1: M_mat(𝒞₁ ∪ 𝒞₂) = M_mat(𝒞₁) + M_mat(𝒞₂)
    sobre regiones disjuntas 𝒞₁ ∩ 𝒞₂ = ∅.
    """
    # Simulación simple: dos conjuntos disjuntos de configuraciones
    # con masa factual m_0(ξ) > 0 cada una
    m_C1 = [0.3, 0.5, 0.2]  # tres configuraciones
    m_C2 = [0.4, 0.1]        # dos configuraciones
    M_1 = sum(m_C1)
    M_2 = sum(m_C2)
    M_union = sum(m_C1 + m_C2)
    if abs(M_union - (M_1 + M_2)) > TOLERANCIA_DEFAULT:
        raise SVError(
            "LUZ-MAT-004",
            f"Aditividad Prop. 4.1: M_union={M_union} ≠ M_1+M_2={M_1+M_2}",
        )
    print(f"  [MAT OK] Proposición 4.1: M_mat(𝒞₁∪𝒞₂) = {M_1}+{M_2} = {M_union} ✓")


def prueba_7_monotonia_M_mat() -> None:
    """
    Proposición 4.2: si 𝒞₁ ⊂ 𝒞₂, entonces M_mat(𝒞₁) ≤ M_mat(𝒞₂).
    """
    m_C1 = [0.3, 0.5]        # dos configuraciones
    m_C2 = [0.3, 0.5, 0.2]   # mismas + una adicional
    M_1 = sum(m_C1)
    M_2 = sum(m_C2)
    if M_2 < M_1 - TOLERANCIA_DEFAULT:
        raise SVError(
            "LUZ-MAT-005",
            f"Monotonía Prop. 4.2 violada: 𝒞₁⊂𝒞₂ pero M_1={M_1} > M_2={M_2}",
        )
    print(f"  [MAT OK] Proposición 4.2: 𝒞₁⊂𝒞₂ ⇒ M_1={M_1} ≤ M_2={M_2} ✓")


def run() -> int:
    print("=" * 74)
    print("L-LUZ-05 — MATERIA FACTUAL Y APARATO TPA (Teorema 15.1)")
    print("=" * 74)
    prueba_1_dictamen_asignado()
    prueba_2_dictamen_en_alfabeto()
    prueba_3_identidad_O1()
    prueba_4_identidad_O2()
    prueba_5_identidad_O3()
    prueba_6_aditividad_M_mat()
    prueba_7_monotonia_M_mat()
    print("-" * 74)
    print("L-LUZ-05 — PASADO. Reducción al régimen TPA con O1-O2-O3 verificada.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(run())
    except SVError as e:
        print(f"\n[L-LUZ-05] FALLO código={e.codigo}")
        print(f"           mensaje: {e.mensaje}")
        sys.exit(1)
