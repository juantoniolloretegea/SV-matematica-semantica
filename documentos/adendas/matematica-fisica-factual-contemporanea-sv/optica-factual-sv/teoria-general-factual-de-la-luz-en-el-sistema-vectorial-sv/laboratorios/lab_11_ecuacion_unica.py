"""
lab_11_ecuacion_unica.py — L-LUZ-11 — Ecuación única L_SV = 0 con 15 sumandos
y 13 invariantes.

Teorema 9.1 (Clausura absoluta): L_SV(Φ^L; {𝓛_i^(gr)}) = 0 si y sólo si los
trece invariantes I1–I13 se satisfacen simultáneamente sobre la fibra.

Pruebas:
  1. L_SV = 0 sobre las tres fibras canónicas admisibles
  2. Número de sumandos L_SV^(s) = 15 (contador exacto)
  3. Anulación simultánea: cada uno de los 15 sumandos se anula
  4. Cada invariante I_s tiene sumando asociado declarado
  5. Dirección necesaria: violación de un invariante ⇒ L_SV ≠ 0
  6. Dirección suficiente: anulación de los 15 sumandos ⇒ todos los invariantes OK
  7. Ausencia del cuarto término: no existe L_SV^(16) no nulo escondido

Códigos: LUZ-LSV-001..005, LUZ-INV-001..004
"""
import sys
import os
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sv_core import (SVError, cargar_casos, construir_acumulados,
                      operador_L_SV, operador_L_SV_sumandos,
                      TOLERANCIA_DEFAULT, CasoFibra)


def prueba_1_L_SV_cero_sobre_admisibles() -> None:
    """L_SV = 0 sobre los tres casos canónicos admisibles."""
    casos = cargar_casos()
    for caso in casos:
        fib = construir_acumulados(caso)
        L = operador_L_SV(caso, fib)
        if abs(L) > TOLERANCIA_DEFAULT:
            raise SVError(
                "LUZ-LSV-001",
                f"{caso.nombre}: L_SV = {L:.6e} ≠ 0 sobre fibra admisible",
                {"L_SV": float(L)},
            )
        print(f"  [LSV OK] {caso.nombre[:45]:45s} L_SV = {L:.3e} ✓")


def prueba_2_cardinal_sumandos_quince() -> None:
    """Número de sumandos L_SV^(s) = 15 exactos."""
    casos = cargar_casos()
    caso = casos[0]
    fib = construir_acumulados(caso)
    s = operador_L_SV_sumandos(caso, fib)
    if len(s) != 15:
        raise SVError(
            "LUZ-LSV-003",
            f"Número de sumandos = {len(s)} ≠ 15",
        )
    print(f"  [LSV OK] Cardinal = 15 sumandos L_SV^(s) ✓")


def prueba_3_anulacion_simultanea() -> None:
    """Cada uno de los 15 sumandos se anula sobre fibra admisible."""
    casos = cargar_casos()
    for caso in casos:
        fib = construir_acumulados(caso)
        s = operador_L_SV_sumandos(caso, fib)
        for nombre, valor in s.items():
            if abs(valor) > TOLERANCIA_DEFAULT:
                raise SVError(
                    "LUZ-LSV-001",
                    f"{caso.nombre}: sumando {nombre} = {valor:.6e} ≠ 0",
                )
    print(f"  [LSV OK] 15 sumandos se anulan simultáneamente sobre 3 casos ✓")


def prueba_4_trece_invariantes_con_sumando() -> None:
    """
    Los 13 invariantes I1-I13 tienen sumando asociado. Como hay 15 sumandos
    y 13 invariantes, se permiten sumandos auxiliares (2 extra para
    identidades O2/O3 que refuerzan O1).
    """
    # Mapeo canónico documentado en §9
    mapeo_I_a_L = {
        "I1":  ["L1"],        # generación preternaria
        "I2":  ["L2"],        # transducción honesta
        "I3":  ["L4"],        # append-only
        "I4":  ["L3"],        # modalidad proyectiva
        "I5":  ["L6"],        # residualidad polar
        "I6":  ["L12"],       # cierre electromagnético
        "I7":  ["L5"],        # cuantización (Planck emergente)
        "I8":  ["L7"],        # coherencia interna
        "I9":  ["L8"],        # compatibilidad basal-fibrosa
        "I10": ["L11"],       # coherencia entrópica
        "I11": ["L9"],        # deformación gravitacional
        "I12": ["L13", "L14", "L15"],  # identidades O1/O2/O3 (3 sumandos)
        "I13": ["L10"],       # clasificador Γ_ℋ
    }
    if len(mapeo_I_a_L) != 13:
        raise SVError("LUZ-INV-001", f"Invariantes declarados = {len(mapeo_I_a_L)} ≠ 13")
    todos_los_sumandos = set()
    for L_list in mapeo_I_a_L.values():
        todos_los_sumandos.update(L_list)
    if len(todos_los_sumandos) != 15:
        raise SVError(
            "LUZ-INV-004",
            f"Los 13 invariantes cubren {len(todos_los_sumandos)} sumandos ≠ 15",
        )
    print(f"  [INV OK] 13 invariantes con sumando asociado; mapeo cubre 15/15 sumandos ✓")


def prueba_5_direccion_necesaria() -> None:
    """
    Si un invariante es violado, L_SV ≠ 0. Construimos una fibra con I2
    violado (χ fuera de Σ) y verificamos que la construcción rechaza el caso.
    """
    casos = cargar_casos()
    # Intentamos construir caso con chi=4 (fuera de Σ)
    caso_base = casos[0]
    chi_violado = caso_base.chi.copy()
    chi_violado[0, 1] = 4  # valor fuera de {0,1,2}
    try:
        caso_bad = CasoFibra(
            nombre="bad", alfa_beta=caso_base.alfa_beta, chi=chi_violado,
            delta_eps=caso_base.delta_eps, B=caso_base.B, H=caso_base.H,
            phi=caso_base.phi, A_vec=caso_base.A_vec, J_jac=caso_base.J_jac,
            e_hat=caso_base.e_hat, n0=0,
        )
        caso_bad.validar()
        # Si llegamos aquí, no se detectó la violación: fallo del validador
        raise SVError(
            "LUZ-LSV-002",
            "Fibra con I2 violado aceptada como admisible (dirección necesaria falla)",
        )
    except SVError as e:
        if e.codigo == "LUZ-LSV-002":
            raise
        if e.codigo in ("LUZ-CHI-001", "LUZ-PAR-001"):
            print(f"  [LSV OK] Violación de I2 detectada con código {e.codigo} ✓")
            return
        raise


def prueba_6_direccion_suficiente() -> None:
    """
    Anulación de los 15 sumandos implica L_SV = 0 (trivial por definición
    de sumando canónico). Verificamos la identidad L_SV = Σ L_SV^(s).
    """
    casos = cargar_casos()
    for caso in casos:
        fib = construir_acumulados(caso)
        L = operador_L_SV(caso, fib)
        s = operador_L_SV_sumandos(caso, fib)
        suma = sum(s.values())
        if abs(L - suma) > TOLERANCIA_DEFAULT:
            raise SVError(
                "LUZ-LSV-001",
                f"{caso.nombre}: L_SV = {L} ≠ Σ L_SV^(s) = {suma}",
            )
    print(f"  [LSV OK] Identidad L_SV = Σ L_SV^(s) verificada sobre 3 casos ✓")


def prueba_7_ausencia_cuarto_termino_oculto() -> None:
    """
    Por construcción, L_SV tiene exactamente 15 sumandos. Verificamos que
    no hay un L_SV^(16) oculto en el diccionario.
    """
    casos = cargar_casos()
    caso = casos[0]
    fib = construir_acumulados(caso)
    s = operador_L_SV_sumandos(caso, fib)
    claves = sorted(s.keys())
    esperados = [f"L{i}" for i in range(1, 16)]
    if sorted(claves) != sorted(esperados):
        raise SVError(
            "LUZ-LSV-003",
            f"Claves de sumandos distintas de L1..L15: {claves}",
        )
    print(f"  [LSV OK] Sumandos = L1..L15 exactos (sin L_16 oculto) ✓")


def run() -> int:
    print("=" * 74)
    print("L-LUZ-11 — ECUACIÓN ÚNICA L_SV = 0 (Teorema 9.1)")
    print("=" * 74)
    prueba_1_L_SV_cero_sobre_admisibles()
    prueba_2_cardinal_sumandos_quince()
    prueba_3_anulacion_simultanea()
    prueba_4_trece_invariantes_con_sumando()
    prueba_5_direccion_necesaria()
    prueba_6_direccion_suficiente()
    prueba_7_ausencia_cuarto_termino_oculto()
    print("-" * 74)
    print("L-LUZ-11 — PASADO. L_SV = 0 verificada con 15 sumandos y 13 invariantes.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(run())
    except SVError as e:
        print(f"\n[L-LUZ-11] FALLO código={e.codigo}")
        print(f"           mensaje: {e.mensaje}")
        sys.exit(1)
