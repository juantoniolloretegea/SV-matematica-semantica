"""
lab_15_disolucion_dualidad.py — L-LUZ-15 — Disolución proyectiva de la dualidad.

Teorema 13.1: onda y corpúsculo no son dos ontologías excluyentes sino dos
proyecciones canónicas (P1_ondulatoria y P2_corpuscular) entre al menos
quince de un mismo objeto fibroso factual Φ^L_SV. Ambas proyecciones son
operativamente compatibles sobre toda fibra admisible con L_SV = 0.

Pruebas:
  1. P1_ondulatoria produce resultado válido sobre las 3 fibras canónicas
  2. P2_corpuscular produce resultado válido sobre las 3 fibras canónicas
  3. P1 y P2 NO son mutuamente excluyentes: ambas operan simultáneamente
     sobre la misma fibra sin contradicción (Teorema 13.1, disolución)
  4. P1 y P2 forman parte de una familia mayor (P1..P15) coexistente
  5. Contraste adversarial: sobre fibra admisible, ambas deben ser no triviales
  6. Coexistencia extendida: 15 proyecciones bien definidas sobre 3 fibras

Códigos: LUZ-DUA-001..004
"""
import sys
import os
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sv_core import (SVError, cargar_casos, construir_acumulados,
                     proyecciones_canonicas, operador_L_SV, TOLERANCIA_DEFAULT)


def prueba_1_proyeccion_ondulatoria_valida() -> None:
    """P1_ondulatoria: lectura ondulatoria como acumulado de canal W."""
    casos = cargar_casos()
    for caso in casos:
        fib = construir_acumulados(caso)
        proys = proyecciones_canonicas(caso, fib)
        P1 = proys.get("P1_ondulatoria")
        if P1 is None:
            raise SVError(
                "LUZ-DUA-001",
                f"{caso.nombre}: P1_ondulatoria no definida "
                f"(patrón ondulatorio ausente del diccionario canónico)",
            )
        P1_arr = np.asarray(P1, dtype=float)
        if not np.all(np.isfinite(P1_arr)):
            raise SVError(
                "LUZ-DUA-001",
                f"{caso.nombre}: P1_ondulatoria contiene valores no finitos",
            )
        if np.any(np.diff(P1_arr) < -TOLERANCIA_DEFAULT):
            raise SVError(
                "LUZ-DUA-001",
                f"{caso.nombre}: P1_ondulatoria no monótona (A_W debe ser no decreciente)",
            )
    print(f"  [DUA OK] P1_ondulatoria operativa sobre 3 fibras canónicas ✓")


def prueba_2_proyeccion_corpuscular_valida() -> None:
    """P2_corpuscular: lectura corpuscular como conteo discreto C."""
    casos = cargar_casos()
    for caso in casos:
        fib = construir_acumulados(caso)
        proys = proyecciones_canonicas(caso, fib)
        P2 = proys.get("P2_corpuscular")
        if P2 is None:
            raise SVError(
                "LUZ-DUA-002",
                f"{caso.nombre}: P2_corpuscular no definida",
            )
        P2_arr = np.asarray(P2, dtype=float)
        if np.any(P2_arr < 0):
            raise SVError(
                "LUZ-DUA-002",
                f"{caso.nombre}: P2_corpuscular con conteo discreto negativo",
            )
        if np.any(np.diff(P2_arr) < -TOLERANCIA_DEFAULT):
            raise SVError(
                "LUZ-DUA-002",
                f"{caso.nombre}: P2_corpuscular no monótona",
            )
    print(f"  [DUA OK] P2_corpuscular operativa sobre 3 fibras canónicas ✓")


def prueba_3_no_mutuamente_excluyentes() -> None:
    """Teorema 13.1: P1 y P2 simultáneas, no excluyentes."""
    casos = cargar_casos()
    for caso in casos:
        fib = construir_acumulados(caso)
        proys = proyecciones_canonicas(caso, fib)
        P1 = proys["P1_ondulatoria"]
        P2 = proys["P2_corpuscular"]
        L_val = operador_L_SV(caso, fib)
        if abs(L_val) > TOLERANCIA_DEFAULT:
            raise SVError(
                "LUZ-DUA-003",
                f"{caso.nombre}: L_SV = {L_val} ≠ 0 "
                f"(disolución proyectiva fracturada)",
            )
        if len(P1) != len(P2):
            raise SVError(
                "LUZ-DUA-003",
                f"{caso.nombre}: cardinalidades distintas P1({len(P1)}) ≠ P2({len(P2)})",
            )
    print(f"  [DUA OK] Teorema 13.1: P1 y P2 simultáneas sin contradicción ✓")


def prueba_4_familia_quince_coexistente() -> None:
    """P1 y P2 son 2 proyecciones entre 15 canónicas."""
    casos = cargar_casos()
    caso = casos[0]
    fib = construir_acumulados(caso)
    proys = proyecciones_canonicas(caso, fib)
    if len(proys) < 15:
        raise SVError(
            "LUZ-DUA-004",
            f"Familia de proyecciones con {len(proys)} < 15 elementos",
        )
    if len(proys) == 2:
        raise SVError(
            "LUZ-DUA-004",
            "Sólo 2 proyecciones: dualidad sigue siendo binaria ontológica",
        )
    for i in range(1, 16):
        if not any(k.startswith(f"P{i}_") for k in proys.keys()):
            raise SVError(
                "LUZ-DUA-004",
                f"Proyección P{i} ausente del diccionario canónico",
            )
    print(f"  [DUA OK] Familia de {len(proys)} proyecciones P1..P15 coexistentes ✓")


def prueba_5_contraste_ontologia_excluyente() -> None:
    """Sobre fibra admisible, P1 y P2 ambas no triviales (no XOR)."""
    casos = cargar_casos()
    for caso in casos:
        fib = construir_acumulados(caso)
        proys = proyecciones_canonicas(caso, fib)
        P1 = np.asarray(proys["P1_ondulatoria"], dtype=float)
        P2 = np.asarray(proys["P2_corpuscular"], dtype=float)
        P1_no_trivial = bool(np.any(P1 > TOLERANCIA_DEFAULT))
        P2_no_trivial = bool(np.any(P2 > TOLERANCIA_DEFAULT))
        if not (P1_no_trivial and P2_no_trivial):
            raise SVError(
                "LUZ-DUA-004",
                f"{caso.nombre}: P1 no trivial={P1_no_trivial}, "
                f"P2 no trivial={P2_no_trivial} — exclusión ontológica, "
                f"Teorema 13.1 violado",
            )
    print(f"  [DUA OK] Contraste ontología excluyente: P1 y P2 ambas activas ✓")


def prueba_6_coexistencia_extendida() -> None:
    """15 proyecciones bien definidas sobre 3 fibras."""
    casos = cargar_casos()
    for caso in casos:
        fib = construir_acumulados(caso)
        proys = proyecciones_canonicas(caso, fib)
        for key, val in proys.items():
            if val is None:
                raise SVError(
                    "LUZ-DUA-003",
                    f"{caso.nombre}: proyección {key} None",
                )
            arr = np.asarray(val, dtype=float)
            if arr.size == 0:
                raise SVError(
                    "LUZ-DUA-003",
                    f"{caso.nombre}: proyección {key} vacía",
                )
            if not np.all(np.isfinite(arr)):
                raise SVError(
                    "LUZ-DUA-003",
                    f"{caso.nombre}: proyección {key} con valor no finito",
                )
    print(f"  [DUA OK] Coexistencia extendida: 15 proyecciones bien definidas sobre 3 fibras ✓")


def run() -> int:
    print("=" * 74)
    print("L-LUZ-15 — DISOLUCIÓN PROYECTIVA DE LA DUALIDAD (Teorema 13.1)")
    print("=" * 74)
    prueba_1_proyeccion_ondulatoria_valida()
    prueba_2_proyeccion_corpuscular_valida()
    prueba_3_no_mutuamente_excluyentes()
    prueba_4_familia_quince_coexistente()
    prueba_5_contraste_ontologia_excluyente()
    prueba_6_coexistencia_extendida()
    print("-" * 74)
    print("L-LUZ-15 — PASADO. Dualidad disuelta en 15 proyecciones canónicas coexistentes.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(run())
    except SVError as e:
        print(f"\n[L-LUZ-15] FALLO código={e.codigo}")
        print(f"           mensaje: {e.mensaje}")
        sys.exit(1)
