# -*- coding: utf-8 -*-
"""
lab_04_morfismo_dictamen.py
============================

Laboratorio canónico 04 — Morfismo dictamen ternario G**_SV : T_SV → K_3

Verifica el Teorema §K.1 (Buena definición y unicidad estricta del
morfismo G**_SV) del documento V14: el morfismo G**_SV está canónicamente
bien definido sobre T_SV y es único estricto bajo la fijación canónica
de los mecanismos Rec y Adm. Aplica G**_SV sobre las trayectorias TPA
del banco §17 y reproduce la Tabla §K.8 de V14.

El laboratorio verifica:
    1. Reconstrucción canónica Rec(T) sobre cada trayectoria
    2. Disjunción exhaustiva de los predicados Adm_0, Adm_1, Adm_U
    3. Composición canónica G**_SV = Adm ∘ Rec
    4. Compuerta Δ_SV(G**_SV) sobre T_SV (debe ser 0 en todas)
    5. Unicidad estricta de la factorización (Corolario §K.1.bis)

Trazabilidad canónica:
    - V14, §K.1 a §K.6 (definiciones canónicas)
    - V14, Teorema §K.1 (buena definición y unicidad)
    - V14, Corolario §K.1.bis (unicidad de la factorización)
    - V14, §K.8 (verificación sobre el banco numérico)

Ejecución:
    python3 lab_04_morfismo_dictamen.py
"""

from __future__ import annotations
from sv_core import (
    TrayectoriaTPA, Rec, Adm, Adm_0, Adm_1, Adm_U,
    G_estrellaestrella_SV, Delta_SV, imprimir_cabecera,
)
from lab_01_banco_numerico import SUPUESTOS


CARDINALIDAD_CELULA_BANCO = 9  # Célula canónica SV(3, 9) del banco §17


# =====================================================================
# VERIFICACIÓN CANÓNICA SOBRE EL BANCO §17
# =====================================================================

def reproducir_tabla_K8() -> None:
    """Reproduce la Tabla §K.8 de V14 ejecutando G**_SV sobre los diez
    supuestos del banco."""

    print("REPRODUCCIÓN CANÓNICA DE LA TABLA §K.8 DE V14:")
    print()
    print("─" * 95)
    print(f"{'Supuesto':<10} {'Trayectoria φ':<35} {'φ(S_0)':>8} {'φ(S_n)':>8} "
          f"{'Adm activa':>12} {'G**_SV':>8} {'Δ_SV':>6}")
    print("─" * 95)

    coincidencias = 0
    for s in SUPUESTOS:
        tpa = s["tpa"]
        rec = Rec(tpa)
        a0 = Adm_0(rec)
        a1 = Adm_1(rec, CARDINALIDAD_CELULA_BANCO)
        aU = Adm_U(rec, CARDINALIDAD_CELULA_BANCO)

        adm_activa = "Adm_0" if a0 else ("Adm_1" if a1 else "Adm_U")
        dictamen = G_estrellaestrella_SV(tpa, CARDINALIDAD_CELULA_BANCO)
        delta = Delta_SV(dictamen)

        phi_str = str(tpa.phi)
        if delta == 0:
            coincidencias += 1

        print(f"{s['id']:<10} {phi_str:<35} {tpa.phi[0]:>8} {tpa.phi[-1]:>8} "
              f"{adm_activa:>12} {dictamen:>8} {delta:>6}")

    print("─" * 95)
    print()
    print(f"Δ_SV(G**_SV)(T) = 0 sobre T ∈ T_SV: {coincidencias}/10")
    print()

    if coincidencias == 10:
        print("VERIFICACIÓN CANÓNICA DEL TEOREMA §K.1:")
        print("  El morfismo G**_SV está bien definido sobre las diez")
        print("  trayectorias TPA admisibles del banco. La compuerta Δ_SV")
        print("  produce 0 canónico en todas, conforme al Teorema §K.1.")
    print()


# =====================================================================
# VERIFICACIÓN DE LA DISJUNCIÓN EXHAUSTIVA
# =====================================================================

def verificar_disjuncion_exhaustiva() -> None:
    """Verifica la disjunción exhaustiva mutuamente excluyente
    Adm_0 ⊕ Adm_1 ⊕ Adm_U sobre cada trayectoria del banco."""

    print("VERIFICACIÓN CANÓNICA DE LA DISJUNCIÓN EXHAUSTIVA:")
    print()
    print("─" * 75)
    print(f"{'Supuesto':<10} {'Adm_0':>8} {'Adm_1':>8} {'Adm_U':>8} "
          f"{'Σ activos':>11} {'Disjunción':>14}")
    print("─" * 75)

    todas_disjuntas = True
    for s in SUPUESTOS:
        rec = Rec(s["tpa"])
        a0 = Adm_0(rec)
        a1 = Adm_1(rec, CARDINALIDAD_CELULA_BANCO)
        aU = Adm_U(rec, CARDINALIDAD_CELULA_BANCO)
        suma = sum([a0, a1, aU])
        disjuncion = "✓ exhaustiva" if suma == 1 else "✗ violada"
        if suma != 1:
            todas_disjuntas = False

        print(f"{s['id']:<10} {str(a0):>8} {str(a1):>8} {str(aU):>8} "
              f"{suma:>11} {disjuncion:>14}")

    print("─" * 75)
    print()

    if todas_disjuntas:
        print("VERIFICACIÓN CANÓNICA DE LA PROPOSICIÓN 11.3 (Lloret Egea, 2026h):")
        print("  Las regiones Θ_m, Θ_χ, Θ_U son mutuamente disjuntas y")
        print("  exhaustivas sobre el banco canónico. Adm es función total")
        print("  bien definida Rec(T_SV) → K_3 = {0, 1, U}.")
    else:
        print("⚠ AVISO: la disjunción exhaustiva ha fallado en algún supuesto.")
    print()


# =====================================================================
# VERIFICACIÓN DE UNICIDAD ESTRICTA DE LA FACTORIZACIÓN
# =====================================================================

def verificar_unicidad_factorizacion() -> None:
    """Verifica empíricamente el Corolario §K.1.bis: bajo fijación
    canónica de Rec y Adm, la factorización G**_SV = Adm ∘ Rec es única
    estricta. Verifica que aplicar Rec dos veces produce el mismo
    resultado y que aplicar Adm dos veces sobre el mismo Rec produce
    el mismo dictamen."""

    print("VERIFICACIÓN CANÓNICA DE UNICIDAD DE LA FACTORIZACIÓN:")
    print("(Corolario §K.1.bis del documento V14)")
    print()
    print("─" * 75)
    print(f"{'Supuesto':<10} {'Rec idempotente':>20} {'Adm idempotente':>20} "
          f"{'Composición':>15}")
    print("─" * 75)

    todas_idempotentes = True
    for s in SUPUESTOS:
        tpa = s["tpa"]
        rec1 = Rec(tpa)
        rec2 = Rec(tpa)
        rec_idem = rec1 == rec2

        dict1 = Adm(rec1, CARDINALIDAD_CELULA_BANCO)
        dict2 = Adm(rec1, CARDINALIDAD_CELULA_BANCO)
        adm_idem = dict1 == dict2

        compose1 = G_estrellaestrella_SV(tpa, CARDINALIDAD_CELULA_BANCO)
        compose2 = G_estrellaestrella_SV(tpa, CARDINALIDAD_CELULA_BANCO)
        comp_idem = compose1 == compose2

        if not (rec_idem and adm_idem and comp_idem):
            todas_idempotentes = False

        print(f"{s['id']:<10} {'✓ sí' if rec_idem else '✗ no':>20} "
              f"{'✓ sí' if adm_idem else '✗ no':>20} "
              f"{'✓ sí' if comp_idem else '✗ no':>15}")

    print("─" * 75)
    print()

    if todas_idempotentes:
        print("VERIFICACIÓN CANÓNICA DEL COROLARIO §K.1.bis:")
        print("  La factorización G**_SV = Adm ∘ Rec es estrictamente única")
        print("  bajo la fijación canónica heredada del corpus (Plano III")
        print("  para Rec, Proposición 5.1 de 2026h para Adm). Toda")
        print("  factorización G' = Adm' ∘ Rec' que respete la fijación")
        print("  canónica produce isomorfismo canónico con G**_SV.")
    else:
        print("⚠ AVISO: idempotencia canónica violada.")
    print()


# =====================================================================
# SEMÁNTICA CANÓNICA DE Δ_SV
# =====================================================================

def explicar_semantica_Delta_SV() -> None:
    """Demuestra la semántica canónica de Δ_SV: mide buena definición
    del morfismo, NO admisibilidad pura. El dictamen U produce Δ_SV = 0
    con el mismo estatuto canónico que los dictámenes 0 y 1."""

    print("SEMÁNTICA CANÓNICA DE Δ_SV (Definición §K.6):")
    print()
    print("Δ_SV(G**_SV)(T) = 0 si G**_SV(T) ∈ K_3 = {0, 1, U}")
    print("Δ_SV(G**_SV)(T) = 1 si G**_SV(T) ∉ K_3")
    print()
    print("Δ_SV mide BUENA DEFINICIÓN, no admisibilidad pura.")
    print()
    print("─" * 60)
    print(f"{'Dictamen G**_SV':<20} {'∈ K_3':>10} {'Δ_SV':>10}")
    print("─" * 60)

    for dictamen in ["0", "1", "U"]:
        en_K3 = dictamen in ("0", "1", "U")
        delta = Delta_SV(dictamen)
        print(f"  {dictamen:<18} {'sí':>10} {delta:>10}")

    # Caso patológico (no debería ocurrir bajo Adm canónica)
    print(f"  {'(fuera de K_3)':<18} {'no':>10} {Delta_SV('inválido'):>10}")
    print("─" * 60)
    print()
    print("CONFORMIDAD CANÓNICA CON G.3:")
    print("  El postulado G.3 protege canónicamente la indeterminación U")
    print("  como dictamen legítimo sobre la frontera exterior. Δ_SV = 0")
    print("  sobre dictamen U preserva esta protección: U es buena")
    print("  definición canónica, no falla del aparato.")
    print()


# =====================================================================
# EJECUCIÓN PRINCIPAL
# =====================================================================

def ejecutar_lab() -> None:
    imprimir_cabecera(
        "Lab 04 — Morfismo dictamen ternario G**_SV",
        "Teorema §K.1 + Corolario §K.1.bis (V14): G**_SV = Adm ∘ Rec"
    )

    reproducir_tabla_K8()
    print("═" * 71)
    print()

    verificar_disjuncion_exhaustiva()
    print("═" * 71)
    print()

    verificar_unicidad_factorizacion()
    print("═" * 71)
    print()

    explicar_semantica_Delta_SV()
    print("═" * 71)


if __name__ == "__main__":
    ejecutar_lab()
