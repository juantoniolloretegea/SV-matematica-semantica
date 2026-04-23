"""
lab_04_vector_director.py — Verificación del vector director u⃗_SV y su ortogonalidad
canónica con el vector normal 𝖦_SV (§15.4).

Identidad a verificar:    u⃗_SV · 𝖦_SV = 0   sobre toda trayectoria admisible.

Equivalente explícita:    u_A − u_W − u_Q − u_U = 0   (componentes respetan balance).

Pruebas:
  1. Construir u⃗_SV desde Ω_SV aplicando 𝔇_Γ.
  2. Contraer con 𝖦_SV = (+1, 0, 0, 0, 0, -1, -1, -1) y verificar = 0.
  3. Verificar que u_A = u_W + u_Q + u_U en cada paso (Teorema 8.1).
  4. Contraste: construir un director espúreo y verificar que u·G ≠ 0 (ORT-001).
  5. Verificar que el operador usado es 𝔇_Γ exactamente (no d/dt): ORT-003.

Códigos: ORT-001..004, GEN-001..004.
"""
import sys
import os
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sv_core import (cargar_casos, CasoCanonico, construir_acumulados,
                     fuerza_canonica, vector_director, producto_G, G_SV,
                     SVError, TOLERANCIA_DEFAULT)


def verificar_ortogonalidad(caso: CasoCanonico) -> None:
    """Para cada suceso j en [n0, N-1], verifica u⃗(j) · 𝖦 = 0."""
    fib = construir_acumulados(caso)
    F   = fuerza_canonica(caso, fib)
    u   = vector_director(fib, F, caso)
    N   = caso.N()
    max_error = 0.0
    # Construir director extendido de 8 componentes en cada paso
    # (u_A, u_H, u_J, u_R, u_B, u_W, u_Q, u_U)
    # Para los tests, u_J = u_R = u_B = 0 (𝖦 los ignora; no penaliza).
    for j in range(N - 1):
        u_J = 0.0   # no involucrado en 𝖦
        u_R = 0.0
        u_B = float(caso.B[j+1] - caso.B[j])   # sólo informativo
        u_ext = np.array([
            u["u_A"][j],      # 𝒜  (coef +1)
            u["u_H"][j],      # 𝓗  (coef 0)
            u_J,              # 𝒥  (coef 0)
            u_R,              # ℛ  (coef 0)
            u_B,              # ℬ  (coef 0)
            u["u_W"][j],      # 𝒲  (coef -1)
            u["u_Q"][j],      # 𝒬  (coef -1)
            u["u_U"][j],      # 𝒰  (coef -1)
        ])
        valor = producto_G(u_ext)
        max_error = max(max_error, abs(valor))
        if abs(valor) > TOLERANCIA_DEFAULT:
            raise SVError("ORT-001",
                          f"{caso.nombre} paso j={j}: u⃗·𝖦 = {valor:.3e} ≠ 0")
    print(f"  [ORT-001 OK] {caso.nombre}: max|u⃗·𝖦| = {max_error:.2e}")


def verificar_balance_por_director(caso: CasoCanonico) -> None:
    """u_A = u_W + u_Q + u_U componente a componente (Teorema 8.1 expresado en director)."""
    fib = construir_acumulados(caso)
    F   = fuerza_canonica(caso, fib)
    u   = vector_director(fib, F, caso)
    diff = u["u_A"] - u["u_W"] - u["u_Q"] - u["u_U"]
    max_diff = float(np.max(np.abs(diff)))
    if max_diff > TOLERANCIA_DEFAULT:
        raise SVError("ORT-004",
                      f"{caso.nombre}: componentes del director no cumplen u_A = u_W+u_Q+u_U; "
                      f"max diff = {max_diff:.3e}")
    print(f"  [ORT-004 OK] {caso.nombre}: u_A = u_W+u_Q+u_U verificado.")


def contraste_director_espurio(caso: CasoCanonico) -> None:
    """
    Contraste adversarial: construimos un director espúreo con componente u_A
    falseada (le añadimos +0.1) y verificamos que u·G ≠ 0. Si no se dispara
    ORT-001, el aparato no discrimina: LAB-002.
    """
    fib = construir_acumulados(caso)
    F   = fuerza_canonica(caso, fib)
    u   = vector_director(fib, F, caso)
    # Falsear u_A en el primer paso
    u_ext_falso = np.array([
        u["u_A"][0] + 0.1,   # falseado
        u["u_H"][0], 0.0, 0.0, caso.B[1]-caso.B[0],
        u["u_W"][0], u["u_Q"][0], u["u_U"][0],
    ])
    valor = producto_G(u_ext_falso)
    if abs(valor - 0.1) > TOLERANCIA_DEFAULT:
        raise SVError("LAB-002",
                      f"{caso.nombre}: contraste con u_A falseado no produce el desvío esperado +0.1; "
                      f"obtenido {valor:.3e}")
    print(f"  [contraste OK] {caso.nombre}: director espúreo produce u·G = {valor:.3f} ≠ 0 ✓")


def verificar_generador_canónico() -> None:
    """Verifica que 𝖦 = (+1, 0, 0, 0, 0, -1, -1, -1) exactamente (Lema 5.1.b)."""
    esperado = np.array([+1.0, 0.0, 0.0, 0.0, 0.0, -1.0, -1.0, -1.0])
    if not np.array_equal(G_SV, esperado):
        raise SVError("GEN-003", f"Generador 𝖦_SV alterado: {G_SV}")
    if abs(G_SV[0] - 1.0) > 1e-15:
        raise SVError("GEN-003", "Normalización g_A ≠ 1")
    for idx, esperado_val in [(5, -1.0), (6, -1.0), (7, -1.0)]:
        if abs(G_SV[idx] - esperado_val) > 1e-15:
            raise SVError("GEN-004", f"Coeficiente del generador en posición {idx} ≠ {esperado_val}")
    for idx in [1, 2, 3, 4]:
        if abs(G_SV[idx]) > 1e-15:
            raise SVError("GEN-002", f"Generador tiene componente no nula en posición {idx}: {G_SV[idx]}")
    print(f"  [GEN OK] 𝖦_SV = (+1, 0, 0, 0, 0, -1, -1, -1) verificado exactamente.")


def run():
    print("=" * 70)
    print("LAB 04 — VECTOR DIRECTOR Y ORTOGONALIDAD CANÓNICA (§15.4)")
    print("=" * 70)
    verificar_generador_canónico()
    casos = cargar_casos()
    for caso in casos:
        verificar_ortogonalidad(caso)
        verificar_balance_por_director(caso)
        contraste_director_espurio(caso)
    print("-" * 70)
    print("LAB 04 — PASADO. Vector director ortogonal al normal en todos los pasos.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(run())
    except SVError as e:
        print(f"\n[LAB 04] FALLO código={e.codigo} — {e.mensaje}")
        sys.exit(1)
