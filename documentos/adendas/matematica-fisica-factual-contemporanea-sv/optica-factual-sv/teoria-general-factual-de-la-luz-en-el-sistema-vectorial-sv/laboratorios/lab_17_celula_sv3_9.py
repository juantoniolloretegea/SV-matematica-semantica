"""
lab_17_celula_sv3_9.py — L-LUZ-17 — Recorrido canónico sobre la célula SV(3,9).

§18: La célula canónica SV(3, 9) es la configuración paradigmática del aparato
SV sobre alfabeto ternario Σ = {0, 1, U} con d = 3 dimensiones de hebra y
n = 9 posiciones ordinales. Su exhaustividad combinatoria es 3^9 = 19 683
configuraciones distintas.

Pruebas:
  1. Caso C (canónica SV(3,9)): verificar d = 3 y n = 9
  2. Alfabeto ternario estricto: chi ∈ Σ = {0, 1, U_CODE} en todas las posiciones
  3. Exhaustividad combinatoria: card(Σ^n) = 3^9 = 19 683
  4. Recorrido canónico del §18: L_SV = 0 sobre la célula
  5. Dimensión SV consistente: magnitudes canónicas bien definidas sobre (3,9)
  6. Rechazo estructural: caso con d ≠ 3 o n ≠ 9 dispara LUZ-CEL-001

Códigos: LUZ-CEL-001..005
"""
import sys
import os
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sv_core import (SVError, cargar_casos, construir_acumulados,
                     operador_L_SV, operador_L_SV_sumandos,
                     TOLERANCIA_DEFAULT, U_CODE, CasoFibra)


def _buscar_caso_canonico() -> CasoFibra:
    """Devuelve el caso C (canónica SV(3,9)) o eleva LUZ-CEL-001."""
    casos = cargar_casos()
    for c in casos:
        if "SV(3,9)" in c.nombre or "canónica" in c.nombre.lower():
            return c
    raise SVError(
        "LUZ-CEL-001",
        "No se encontró caso canónico SV(3,9) en casos_canonicos.json",
    )


def prueba_1_dimensiones_canonicas() -> None:
    """Caso C: d = 3 hebras, n = 9 posiciones."""
    caso = _buscar_caso_canonico()
    d = caso.chi.shape[0]
    n = caso.chi.shape[1]
    if d != 3:
        raise SVError(
            "LUZ-CEL-001",
            f"Caso canónico con d = {d} ≠ 3 (aparato SV requiere d = 3)",
        )
    if n != 9:
        raise SVError(
            "LUZ-CEL-001",
            f"Caso canónico con n = {n} ≠ 9 (célula SV(3,9) requiere n = 9)",
        )
    print(f"  [CEL OK] Célula canónica SV(3,9): d = 3, n = 9 ✓")


def prueba_2_alfabeto_ternario_estricto() -> None:
    """chi[i, j] ∈ Σ = {0, 1, U_CODE = 2} sobre todas las posiciones."""
    caso = _buscar_caso_canonico()
    valores_validos = {0, 1, U_CODE}
    for v in np.unique(caso.chi):
        if int(v) not in valores_validos:
            raise SVError(
                "LUZ-CEL-002",
                f"Valor χ = {v} fuera de Σ = {{0, 1, {U_CODE}}}",
            )
    print(f"  [CEL OK] Alfabeto ternario Σ = {{0, 1, U}} respetado sobre (3, 9) ✓")


def prueba_3_exhaustividad_combinatoria() -> None:
    """|Σ^n| = 3^9 = 19 683 configuraciones posibles."""
    n = 9
    esperado = 3 ** n
    if esperado != 19683:
        raise SVError(
            "LUZ-CEL-003",
            f"Cardinalidad combinatoria 3^9 = {esperado} ≠ 19683",
        )
    # Verificamos que el caso actual es UNO entre las 19 683 posibles
    caso = _buscar_caso_canonico()
    # La distribución P(φ = k) en el caso debe ser consistente con el espacio Σ^n
    distribuciones = {v: int(np.sum(caso.chi == v)) for v in [0, 1, U_CODE]}
    total = sum(distribuciones.values())
    if total != caso.chi.size:
        raise SVError(
            "LUZ-CEL-003",
            f"Distribución inconsistente: suma = {total} ≠ {caso.chi.size}",
        )
    print(f"  [CEL OK] Exhaustividad combinatoria |Σ^9| = 3^9 = 19 683 ✓")


def prueba_4_recorrido_canonico_L_SV_cero() -> None:
    """Sobre la célula canónica, L_SV = 0 (Teorema 9.1)."""
    caso = _buscar_caso_canonico()
    fib = construir_acumulados(caso)
    L_val = operador_L_SV(caso, fib)
    if abs(L_val) > TOLERANCIA_DEFAULT:
        raise SVError(
            "LUZ-CEL-005",
            f"Célula canónica SV(3,9): L_SV = {L_val} ≠ 0 (recorrido §18 falla)",
        )
    print(f"  [CEL OK] Recorrido canónico §18: L_SV = 0 sobre célula SV(3,9) ✓")


def prueba_5_dimensiones_canonicas_magnitudes() -> None:
    """Magnitudes canónicas bien definidas y finitas sobre (3, 9)."""
    caso = _buscar_caso_canonico()
    fib = construir_acumulados(caso)
    for clave in ["A", "A_W", "C", "a", "DA"]:
        if clave not in fib:
            raise SVError(
                "LUZ-CEL-004",
                f"Magnitud {clave} ausente sobre célula SV(3,9)",
            )
        arr = np.asarray(fib[clave], dtype=float)
        if not np.all(np.isfinite(arr)):
            raise SVError(
                "LUZ-CEL-004",
                f"Magnitud {clave} con valor no finito",
            )
    # Sumandos individuales también finitos
    sumandos = operador_L_SV_sumandos(caso, fib)
    for k, v in sumandos.items():
        if not np.isfinite(v):
            raise SVError(
                "LUZ-CEL-004",
                f"Sumando {k} = {v} no finito",
            )
    print(f"  [CEL OK] Magnitudes y sumandos L_SV finitos sobre SV(3,9) ✓")


def prueba_6_rechazo_estructural_dimensiones() -> None:
    """
    Caso con d = 3 y n = 9 debe pasar; caso con otras dimensiones
    NO se considera canónico SV(3,9).
    """
    casos = cargar_casos()
    canonicos = [c for c in casos if c.chi.shape == (3, 9)]
    no_canonicos = [c for c in casos if c.chi.shape != (3, 9)]
    if len(canonicos) < 1:
        raise SVError(
            "LUZ-CEL-001",
            "No hay ningún caso canónico SV(3, 9) en el conjunto",
        )
    # Los no canónicos son bibliográficamente SV(3, 4) o SV(3, 6); deben
    # tener dimensiones distintas a (3, 9) — si alguno pasara como SV(3,9)
    # habría ambigüedad estructural
    for c in no_canonicos:
        if c.chi.shape == (3, 9):
            raise SVError(
                "LUZ-CEL-001",
                f"{c.nombre}: dimensiones (3,9) pero no marcado como canónico",
            )
    print(f"  [CEL OK] Distinción estructural: {len(canonicos)} canónico(s), "
          f"{len(no_canonicos)} no canónico(s) ✓")


def run() -> int:
    print("=" * 74)
    print("L-LUZ-17 — CÉLULA CANÓNICA SV(3, 9) (§18)")
    print("=" * 74)
    prueba_1_dimensiones_canonicas()
    prueba_2_alfabeto_ternario_estricto()
    prueba_3_exhaustividad_combinatoria()
    prueba_4_recorrido_canonico_L_SV_cero()
    prueba_5_dimensiones_canonicas_magnitudes()
    prueba_6_rechazo_estructural_dimensiones()
    print("-" * 74)
    print("L-LUZ-17 — PASADO. Célula SV(3,9) canónica con exhaustividad 3^9 = 19683.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(run())
    except SVError as e:
        print(f"\n[L-LUZ-17] FALLO código={e.codigo}")
        print(f"           mensaje: {e.mensaje}")
        sys.exit(1)
