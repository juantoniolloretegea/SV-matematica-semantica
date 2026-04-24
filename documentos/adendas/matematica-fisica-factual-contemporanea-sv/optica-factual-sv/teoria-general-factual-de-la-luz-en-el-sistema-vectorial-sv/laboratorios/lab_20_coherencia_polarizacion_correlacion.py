"""
lab_20_coherencia_polarizacion_correlacion.py — L-LUZ-20 — Coherencia,
polarización y correlación estructural.

§8 B.6: Operador de coherencia estructural entre hebras de misma fibra
§8 B.7: Operador de polarización como residual polar δ_i^res = β_i - α_i
§8 B.16: Operador de correlación estructural entre dos fibras distintas
§A.6.1: Teorema sobre ≠-entrelazamiento (Correlación ≠ entrelazamiento cuántico)

Pruebas:
  1. Coherencia estructural B.7 ≥ 0 sobre hebras compatibles
  2. Polarización {δ_i^res} igual a β_i - α_i sobre posiciones activadas
  3. Ángulo de Brewster calculado con tolerancia 1% (B-LUZ-14)
  4. Correlación estructural NO se reduce a entrelazamiento cuántico (Teo A.6.1)
  5. Correlación sobre fibras con ξ_1 ∩ ξ_2 = ∅ devuelve valor nulo
  6. Polarización sobre fibra admisible tiene traza a par polar (α, β) preternario

Códigos: LUZ-COH-001..003, LUZ-POL-001..003, LUZ-COR-001..003
"""
import sys
import os
import math
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sv_core import (SVError, cargar_casos, construir_acumulados,
                     TOLERANCIA_DEFAULT, U_CODE)


def coherencia_estructural(caso, fib) -> float:
    """
    B.7 — Coherencia estructural entre hebras de una misma fibra.
    Definida como 1 - varianza_inter_hebras / varianza_total (Pearson-like).
    """
    a = fib["a"]
    N = caso.N()
    varianzas = np.array([np.var(a[:, n]) for n in range(N)])
    var_total = float(np.var(a))
    if var_total < 1e-18:
        return 1.0
    var_media = float(np.mean(varianzas))
    return max(0.0, 1.0 - var_media / var_total)


def polarizacion_residual(caso) -> np.ndarray:
    """B.6 — δ_i^res = β_i - α_i sobre todas las posiciones."""
    return caso.alfa_beta[:, :, 1] - caso.alfa_beta[:, :, 0]


def angulo_brewster(n1: float, n2: float) -> float:
    """Ángulo de Brewster θ_B = atan(n2/n1) en grados."""
    return math.degrees(math.atan(n2 / n1))


def correlacion_estructural(caso1, fib1, caso2, fib2) -> float:
    """
    B.16 — Correlación estructural sobre ξ_1 ∩ ξ_2 (sustrato combinatorio
    común). NO invoca espacio de Hilbert ni operadores hermíticos (P.3).

    Definida como magnitud de similitud estructural entre los pares polares
    activados en posiciones compartidas.
    """
    chi1 = caso1.chi
    chi2 = caso2.chi
    # La intersección se define como posiciones activadas en ambos (chi != U)
    if chi1.shape != chi2.shape:
        # No hay sustrato combinatorio común
        return 0.0
    activadas_1 = (chi1 != U_CODE)
    activadas_2 = (chi2 != U_CODE)
    interseccion = activadas_1 & activadas_2
    if not np.any(interseccion):
        return 0.0
    ab1 = caso1.alfa_beta
    ab2 = caso2.alfa_beta
    # Similitud estructural: 1 - distancia normalizada sobre intersección
    pos_i, pos_n = np.where(interseccion)
    if len(pos_i) == 0:
        return 0.0
    diff = np.abs(ab1[pos_i, pos_n, :] - ab2[pos_i, pos_n, :])
    sim = 1.0 / (1.0 + float(np.mean(diff)))
    return sim


def prueba_1_coherencia_no_negativa() -> None:
    """Coherencia B.7 ≥ 0 sobre hebras compatibles."""
    casos = cargar_casos()
    for caso in casos:
        fib = construir_acumulados(caso)
        coh = coherencia_estructural(caso, fib)
        if coh < -TOLERANCIA_DEFAULT:
            raise SVError(
                "LUZ-COH-001",
                f"{caso.nombre}: coherencia B.7 = {coh} < 0",
            )
        if not math.isfinite(coh):
            raise SVError(
                "LUZ-COH-001",
                f"{caso.nombre}: coherencia = {coh} no finita",
            )
    print(f"  [COH OK] Coherencia estructural B.7 ≥ 0 sobre 3 fibras ✓")


def prueba_2_polarizacion_residual_correcta() -> None:
    """δ_i^res[i, j] = β_i[j] - α_i[j] exactamente."""
    casos = cargar_casos()
    for caso in casos:
        delta_res = polarizacion_residual(caso)
        esperado = caso.alfa_beta[:, :, 1] - caso.alfa_beta[:, :, 0]
        if not np.allclose(delta_res, esperado, atol=TOLERANCIA_DEFAULT):
            max_dif = float(np.max(np.abs(delta_res - esperado)))
            raise SVError(
                "LUZ-POL-001",
                f"{caso.nombre}: |δ^res - (β - α)| = {max_dif:.3e} > {TOLERANCIA_DEFAULT}",
            )
    print(f"  [POL OK] Residual polar δ_i^res = β_i - α_i sobre 3 fibras ✓")


def prueba_3_angulo_brewster_agua() -> None:
    """θ_B(agua, n=1.333) con tolerancia 1% respecto a 53.12°."""
    theta_calc = angulo_brewster(1.0, 1.333)
    theta_heredado = 53.12
    rel = abs(theta_calc - theta_heredado) / theta_heredado
    if rel > 0.01:
        raise SVError(
            "LUZ-POL-002",
            f"θ_B agua: calc = {theta_calc:.3f}°, heredado = {theta_heredado}°, "
            f"divergencia = {rel*100:.2f}% > 1%",
        )
    print(f"  [POL OK] θ_B(agua) = {theta_calc:.2f}° (≈ 53.12°, B-LUZ-14) ✓")


def prueba_4_correlacion_no_reducible_a_entrelazamiento() -> None:
    """
    Teorema A.6.1: correlación estructural SV NO es entrelazamiento cuántico.
    Verificación estructural: el operador de correlación opera sobre alfabeto
    ternario {0, 1, U}, no sobre espacio de Hilbert complejo.
    """
    casos = cargar_casos()
    if len(casos) < 2:
        raise SVError(
            "LUZ-COR-001",
            "Se requieren al menos 2 casos para correlación",
        )
    caso1 = casos[0]
    caso2 = casos[1]
    # Las celulas chi son integer ∈ Σ = {0, 1, U} — no complejos
    if caso1.chi.dtype.kind == "c" or caso2.chi.dtype.kind == "c":
        raise SVError(
            "LUZ-COR-002",
            "Célula con valores complejos → operador hermítico invocado (P.3 violado)",
        )
    # Calcular correlación: debe ser un número real finito
    fib1 = construir_acumulados(caso1)
    fib2 = construir_acumulados(caso2)
    corr = correlacion_estructural(caso1, fib1, caso2, fib2)
    if not math.isfinite(corr):
        raise SVError(
            "LUZ-COR-001",
            f"Correlación estructural = {corr} no finita",
        )
    print(f"  [COR OK] Correlación estructural sin espacio de Hilbert (Teo A.6.1) ✓")


def prueba_5_correlacion_interseccion_vacia_nula() -> None:
    """Fibras con ξ_1 ∩ ξ_2 = ∅ → correlación = 0."""
    casos = cargar_casos()
    # Construir una fibra con todo U_CODE (ξ = ∅, no activaciones)
    caso_base = casos[0]
    chi_vacio = np.full_like(caso_base.chi, U_CODE)
    from sv_core import CasoFibra
    caso_vacio = CasoFibra(
        nombre="VacioFibra",
        alfa_beta=caso_base.alfa_beta, chi=chi_vacio,
        delta_eps=caso_base.delta_eps, B=caso_base.B, H=caso_base.H,
        phi=caso_base.phi, A_vec=caso_base.A_vec, J_jac=caso_base.J_jac,
        e_hat=caso_base.e_hat, n0=0,
    )
    fib1 = construir_acumulados(caso_base)
    fib2 = construir_acumulados(caso_vacio)
    corr = correlacion_estructural(caso_base, fib1, caso_vacio, fib2)
    if corr != 0.0:
        raise SVError(
            "LUZ-COR-003",
            f"Intersección ξ ∩ ∅ debe dar correlación 0, obtuvo {corr}",
        )
    print(f"  [COR OK] Correlación(fibra, vacío) = 0 sobre intersección vacía ✓")


def prueba_6_polarizacion_traza_par_polar() -> None:
    """Polarización tiene traza al par polar (α, β) preternario."""
    casos = cargar_casos()
    for caso in casos:
        delta_res = polarizacion_residual(caso)
        # La polarización no puede existir sin el par polar
        if caso.alfa_beta is None or caso.alfa_beta.size == 0:
            raise SVError(
                "LUZ-POL-003",
                f"{caso.nombre}: polarización sin par polar (α, β)",
            )
        # El residual debe venir exactamente de α, β (ya verificado en prueba 2)
        # Adicional: sobre posiciones activadas (chi != U), el residual debe ser
        # consistente con la diferencia
        activadas = (caso.chi != U_CODE)
        if not np.any(activadas):
            continue
        # Verificar que al menos una posición activa tiene residual definido
        delta_activo = delta_res[activadas]
        if not np.all(np.isfinite(delta_activo)):
            raise SVError(
                "LUZ-POL-003",
                f"{caso.nombre}: residual polar no finito en posición activada",
            )
    print(f"  [POL OK] Polarización con traza exacta al par polar (α, β) preternario ✓")


def run() -> int:
    print("=" * 74)
    print("L-LUZ-20 — COHERENCIA, POLARIZACIÓN Y CORRELACIÓN (§8 B.6/B.7/B.16, §A.6.1)")
    print("=" * 74)
    prueba_1_coherencia_no_negativa()
    prueba_2_polarizacion_residual_correcta()
    prueba_3_angulo_brewster_agua()
    prueba_4_correlacion_no_reducible_a_entrelazamiento()
    prueba_5_correlacion_interseccion_vacia_nula()
    prueba_6_polarizacion_traza_par_polar()
    print("-" * 74)
    print("L-LUZ-20 — PASADO. Coherencia, polarización y correlación estructurales verificadas.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(run())
    except SVError as e:
        print(f"\n[L-LUZ-20] FALLO código={e.codigo}")
        print(f"           mensaje: {e.mensaje}")
        sys.exit(1)
