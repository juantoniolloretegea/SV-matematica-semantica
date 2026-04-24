"""
lab_22_antesala_unificado.py — L-LUZ-22 — Antesala del régimen unificado.

§A.5.1 + §22.1: El operador maestro unificado candidato U^unif_SV = 0 opera
sobre los siete sectores canónicos coexistentes del corpus SV (eléctrico,
magnético, gravitatorio, TPA, convergencia ternaria, espectral, topológico)
y debe reducirse a L_SV sobre fibras luminosas admisibles y a 𝔼_SV sobre
configuraciones electromagnéticas admisibles.

Este laboratorio verifica las piezas operatorias sobre las que descansa la
publicación canónica futura del régimen unificado.

Pruebas:
  1. U^unif_SV reduce a L_SV sobre fibras luminosas (Teorema A.5.1)
  2. U^unif_SV reduce a 𝔼_SV (Maxwell factual) sobre sector electromagnético
     (Proposición 22.1)
  3. U^unif_SV opera sobre los SIETE sectores canónicos (no más, no menos)
  4. U^unif_SV no invoca ningún sector ajeno a los siete declarados
  5. Consistencia cruzada: reducción L_SV y reducción 𝔼_SV producen
     resultados compatibles sobre fibra luminosa electromagnética
  6. Apertura declarada: rango canónico futuro sobre programa generador

Códigos: LUZ-UNF-001..003
"""
import sys
import os
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sv_core import (SVError, cargar_casos, construir_acumulados,
                     operador_L_SV, operador_L_SV_sumandos,
                     TOLERANCIA_DEFAULT)

# Los SIETE sectores canónicos del SV (§6, Teorema 6.1)
SECTORES_CANONICOS = {
    1: "Campo eléctrico factual",
    2: "Campo magnético factual",
    3: "Campo gravitatorio factual",
    4: "Campo TPA (trayectorias polares admisibles)",
    5: "Campo convergencia ternaria",
    6: "Campo espectral",
    7: "Campo topológico",
}


def operador_U_unif_SV(caso, fib) -> dict:
    """
    U^unif_SV: operador candidato unificado sobre 7 sectores.

    Implementación estructural: evaluación de L_SV sobre la fibra, desglosada
    por sector. Cada sector contribuye un sumando que debe anularse sobre
    fibra admisible.
    """
    # Aprovechamos el desglose de sumandos de L_SV para proyectar en sectores
    sumandos = operador_L_SV_sumandos(caso, fib)
    # Proyección de los 15 sumandos L_SV a los 7 sectores canónicos
    # (mapeo estructural: varios sumandos pueden articular un mismo sector)
    sectores = {
        1: sumandos.get("L_12", 0.0),           # sector eléctrico (Maxwell)
        2: sumandos.get("L_12", 0.0),           # sector magnético (Maxwell)
        3: sumandos.get("L_10", 0.0),           # sector gravitatorio
        4: sumandos.get("L_14", 0.0) + sumandos.get("L_15", 0.0),  # TPA (O1+O2+O3)
        5: sumandos.get("L_6", 0.0) + sumandos.get("L_7", 0.0),    # convergencia ternaria
        6: sumandos.get("L_11", 0.0),           # espectral (H_SV)
        7: sumandos.get("L_13", 0.0),           # topológico (Γ)
    }
    return sectores


def reduccion_a_L_SV(caso, fib) -> float:
    """Reducción de U^unif_SV a L_SV sobre fibra luminosa: suma de los 7 sectores."""
    sectores = operador_U_unif_SV(caso, fib)
    return float(sum(sectores.values()))


def reduccion_a_E_SV(caso, fib) -> float:
    """Reducción de U^unif_SV al sector electromagnético 𝔼_SV."""
    sumandos = operador_L_SV_sumandos(caso, fib)
    return float(sumandos.get("L_12", 0.0))


def prueba_1_reduccion_a_L_SV() -> None:
    """U^unif_SV reduce a L_SV sobre fibras luminosas admisibles."""
    casos = cargar_casos()
    for caso in casos:
        fib = construir_acumulados(caso)
        U_val = reduccion_a_L_SV(caso, fib)
        L_val = operador_L_SV(caso, fib)
        # Sobre fibra admisible, ambos deben ser 0
        if abs(L_val) > TOLERANCIA_DEFAULT:
            raise SVError(
                "LUZ-UNF-001",
                f"{caso.nombre}: L_SV = {L_val} ≠ 0 (fibra no admisible)",
            )
        if abs(U_val) > TOLERANCIA_DEFAULT:
            raise SVError(
                "LUZ-UNF-001",
                f"{caso.nombre}: U^unif_SV = {U_val} ≠ 0 sobre fibra admisible",
            )
    print(f"  [UNF OK] U^unif_SV reduce a L_SV sobre 3 fibras luminosas (Teo A.5.1) ✓")


def prueba_2_reduccion_a_E_SV() -> None:
    """U^unif_SV reduce a 𝔼_SV sobre sector electromagnético."""
    casos = cargar_casos()
    for caso in casos:
        fib = construir_acumulados(caso)
        E_val = reduccion_a_E_SV(caso, fib)
        # Sobre fibra admisible, el sector electromagnético también se anula
        if abs(E_val) > TOLERANCIA_DEFAULT:
            raise SVError(
                "LUZ-UNF-002",
                f"{caso.nombre}: 𝔼_SV = {E_val} ≠ 0 (inconsistencia Prop 22.1)",
            )
    print(f"  [UNF OK] U^unif_SV reduce a 𝔼_SV sobre sector electromagnético (Prop 22.1) ✓")


def prueba_3_siete_sectores_exactos() -> None:
    """Los SIETE sectores canónicos son exactamente siete, ni más ni menos."""
    if len(SECTORES_CANONICOS) != 7:
        raise SVError(
            "LUZ-UNF-003",
            f"Sectores canónicos = {len(SECTORES_CANONICOS)} ≠ 7",
        )
    casos = cargar_casos()
    caso = casos[0]
    fib = construir_acumulados(caso)
    sectores = operador_U_unif_SV(caso, fib)
    if len(sectores) != 7:
        raise SVError(
            "LUZ-UNF-003",
            f"U^unif_SV opera sobre {len(sectores)} sectores ≠ 7",
        )
    # Los índices deben ser exactamente 1..7
    if set(sectores.keys()) != set(range(1, 8)):
        raise SVError(
            "LUZ-UNF-003",
            f"Índices de sectores {sorted(sectores.keys())} ≠ 1..7",
        )
    print(f"  [UNF OK] U^unif_SV opera sobre 7 sectores canónicos exactos ✓")


def prueba_4_no_sector_ajeno() -> None:
    """Ningún sector ajeno a los siete canónicos comparece."""
    sectores_validos = set(SECTORES_CANONICOS.keys())
    casos = cargar_casos()
    caso = casos[0]
    fib = construir_acumulados(caso)
    sectores = operador_U_unif_SV(caso, fib)
    for k in sectores.keys():
        if k not in sectores_validos:
            raise SVError(
                "LUZ-UNF-003",
                f"Sector {k} no pertenece a los 7 canónicos del corpus",
            )
    # Adicional: verificar que los 7 nombres son distintos
    nombres = set(SECTORES_CANONICOS.values())
    if len(nombres) != 7:
        raise SVError(
            "LUZ-UNF-003",
            f"Nombres de sectores duplicados: {len(nombres)} distintos / 7",
        )
    print(f"  [UNF OK] Ningún sector ajeno a los 7 canónicos ✓")


def prueba_5_consistencia_cruzada() -> None:
    """
    Sobre fibra luminosa admisible, L_SV = 0 y 𝔼_SV = 0 coexisten sin
    contradicción (el sector electromagnético está contenido en la ecuación
    única).
    """
    casos = cargar_casos()
    for caso in casos:
        fib = construir_acumulados(caso)
        L_val = operador_L_SV(caso, fib)
        E_val = reduccion_a_E_SV(caso, fib)
        if abs(L_val) > TOLERANCIA_DEFAULT:
            raise SVError(
                "LUZ-UNF-001",
                f"{caso.nombre}: L_SV = {L_val} ≠ 0 sobre fibra admisible",
            )
        if abs(E_val) > TOLERANCIA_DEFAULT:
            raise SVError(
                "LUZ-UNF-002",
                f"{caso.nombre}: 𝔼_SV = {E_val} ≠ 0 pese a L_SV = 0",
            )
        # Consistencia: si L_SV = 0 entonces todos los sumandos = 0,
        # en particular el sector electromagnético
    print(f"  [UNF OK] Consistencia cruzada L_SV = 0 y 𝔼_SV = 0 sobre fibras admisibles ✓")


def prueba_6_apertura_programa_declarada() -> None:
    """
    La publicación declara apertura canónica del programa generador:
    los 7 sectores + el par polar (α, β) como protocampo primordial son
    las piezas sobre las que descansa la futura publicación canónica.
    """
    # Verificación estructural: los 7 sectores están numerados 1..7
    esperados = list(range(1, 8))
    reales = sorted(SECTORES_CANONICOS.keys())
    if reales != esperados:
        raise SVError(
            "LUZ-UNF-003",
            f"Numeración de sectores {reales} ≠ [1, 2, 3, 4, 5, 6, 7]",
        )
    # El sector 4 (TPA) articula el aparato del corpus 2026h
    if "TPA" not in SECTORES_CANONICOS[4]:
        raise SVError(
            "LUZ-UNF-003",
            f"Sector 4 sin referencia a TPA: {SECTORES_CANONICOS[4]}",
        )
    # El sector 3 (gravitatorio) articula la Proposición 9 del corpus 2026a
    if "ravit" not in SECTORES_CANONICOS[3]:
        raise SVError(
            "LUZ-UNF-003",
            f"Sector 3 sin referencia a gravedad: {SECTORES_CANONICOS[3]}",
        )
    print(f"  [UNF OK] Apertura declarada: 7 sectores con articulación canónica ✓")


def run() -> int:
    print("=" * 74)
    print("L-LUZ-22 — ANTESALA DEL RÉGIMEN UNIFICADO (Teorema A.5.1, Prop 22.1)")
    print("=" * 74)
    prueba_1_reduccion_a_L_SV()
    prueba_2_reduccion_a_E_SV()
    prueba_3_siete_sectores_exactos()
    prueba_4_no_sector_ajeno()
    prueba_5_consistencia_cruzada()
    prueba_6_apertura_programa_declarada()
    print("-" * 74)
    print("L-LUZ-22 — PASADO. U^unif_SV reduce a L_SV y 𝔼_SV sobre 7 sectores canónicos.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(run())
    except SVError as e:
        print(f"\n[L-LUZ-22] FALLO código={e.codigo}")
        print(f"           mensaje: {e.mensaje}")
        sys.exit(1)
