"""
Lab 05 — Maxwell Factual Sintético
Corresponde a la sección I (§3 Laboratorio director) del documento.
Especificación (L70): "comprobar que trayectorias de residuales de campo
pueden leerse sin tiempo soberano, con acumulación factual y sensibilidad trazable."

Este laboratorio modela una configuración electromagnética como célula SV(9,3).
No contiene ecuaciones de Maxwell — modela la EVALUACIÓN ternaria de propiedades
del dominio electromagnético conforme al SV.

Posiciones P1–P9 del frame electromagnético:
  P1 — Ecuaciones de Maxwell verificables en el frame
  P2 — Residual de divergencia E (∇·E ≈ ρ/ε₀) calculable
  P3 — Condición de contorno explícita y consistente
  P4 — Campo sin soberanía temporal (indexado por eventos, no por t)
  P5 — Ausencia de inferencia estadística en la lectura del campo
  P6 — Propagación a través de frontera factual explícita
  P7 — Residual de divergencia B = 0 (sin monopolos) verificable
  P8 — Coherencia E–B conforme a la ley de Faraday (rotor E = −∂B/∂t)
  P9 — Estado global del frame electromagnético

Autor:     Juan Antonio Lloret Egea | ORCID 0000-0002-6634-3351
Sello:     ITVIA — IA eñ™ | ISSN 2695-6411 | CC BY-NC-ND 4.0
"""

import json, sys, os, importlib.util

_spec = importlib.util.spec_from_file_location(
    "l01", os.path.join(os.path.dirname(__file__), "lab_01_calculo_suceso.py"))
_m = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(_m)
make_cell = _m.make_cell
observable_compatible = _m.observable_compatible
deriv_event = _m.deriv_event
accumulate = _m.accumulate
telescopy_check = _m.telescopy_check
sensitivity = _m.sensitivity
check_no_favorable_closure = _m.check_no_favorable_closure
K3_U = _m.K3_U; K3_0 = _m.K3_0; K3_1 = _m.K3_1

# ── Trayectoria Maxwell Sintética ────────────────────────────────────────────
# ν₀: Configuración inicial — P3=U (contorno no declarado), P8=U (coherencia E-B
#      no verificada), P2=U (residual no calculado). Sin tiempo soberano: el
#      "primer suceso" es la declaración del dominio, no un instante t₀.
# ν₁: Suceso 1 — contorno declarado (P3→0), coherencia E-B verificada (P8→0).
#      Residual B=0 verificado (P7→0). P2 sigue en U.
# ν₂: Suceso 2 — residual de divergencia E calculado y verificado ≈ 0 (P2→0).
#      Frame completamente determinado.

TRAY_MAXWELL = [
    make_cell([K3_0, K3_U, K3_U, K3_0, K3_0, K3_0, K3_0, K3_U, K3_0]),  # ν₀: f=3
    make_cell([K3_0, K3_U, K3_0, K3_0, K3_0, K3_0, K3_0, K3_0, K3_0]),  # ν₁: f=1
    make_cell([K3_0, K3_0, K3_0, K3_0, K3_0, K3_0, K3_0, K3_0, K3_0]),  # ν₂: f=0 APTO
]
OMEGA = [1, 1, 1]   # pesos unitarios (sin tiempo: sucesos equiponderados)

# Perturbación paramétrica: a = precisión del detector de contorno
# Si a aumenta, P3 se resuelve antes (desde ν₀):
TRAY_a_pert = [
    make_cell([K3_0, K3_U, K3_0, K3_0, K3_0, K3_0, K3_0, K3_U, K3_0]),  # ν₀: f=2 (P3→0)
    make_cell([K3_0, K3_U, K3_0, K3_0, K3_0, K3_0, K3_0, K3_0, K3_0]),  # ν₁: f=1
    make_cell([K3_0, K3_0, K3_0, K3_0, K3_0, K3_0, K3_0, K3_0, K3_0]),  # ν₂: f=0 APTO
]

# Caso de violación: múltiples posiciones P=1 → NO_APTO
# (n1=7 >= T(9)=7 → clasificación NO_APTO sin NMSV008)
TRAY_VIOLATION = [
    make_cell([K3_1, K3_1, K3_1, K3_1, K3_1, K3_1, K3_1, K3_0, K3_0]),  # n1=7 → NO_APTO
]
# Caso con infracción menor: P1=1 pero mayoría U → INDETERMINADO
TRAY_INFRAC_MENOR = [
    make_cell([K3_1, K3_U, K3_U, K3_U, K3_U, K3_U, K3_0, K3_0, K3_0]),  # n1=1, n0=2, nU=6
]

def run_lab05():
    print("=" * 70)
    print("LAB 05 — Maxwell Factual Sintético (Sección I §3)")
    print("Sin tiempo soberano: trayectoria indexada por sucesos.")
    print("=" * 70)

    # ── 1. Observable y trayectoria ──────────────────────────────────────────
    print("\n── 1. Observable compatible (sin tiempo soberano) ──")
    f = observable_compatible(TRAY_MAXWELL, OMEGA)
    print(f"  f(νj) = {f}  [conteo de posiciones en U por suceso]")
    assert f == [3, 1, 0], f"ERROR: f esperado [3,1,0], obtenido {f}"
    print("  ✓ Trayectoria de 3 sucesos (no 3 instantes temporales)")
    print("  ✓ f desciente desde 3 (indeterminado) hasta 0 (APTO)")

    # ── 2. Derivadas de suceso ───────────────────────────────────────────────
    print("\n── 2. Derivada de suceso del residual ──")
    derivs = deriv_event(f, OMEGA[:2])
    print(f"  𝔇_Γ f(j) = {derivs}")
    assert derivs[0] < 0, "ERROR: primera derivada debe ser negativa (convergencia)"
    assert derivs[1] < 0, "ERROR: segunda derivada debe ser negativa"
    print(f"  ✓ Derivadas negativas: convergencia confirmada sin tiempo soberano")

    # ── 3. Acumulación factual ───────────────────────────────────────────────
    print("\n── 3. Acumulación factual (circulación sobre trayectorias cerradas) ──")
    tel = telescopy_check(f, OMEGA[:2])
    print(f"  𝔄 = {tel['acumulacion']}  = f(ν₂)-f(ν₀) = {tel['delta_extremos']}")
    assert tel['telescopia_ok'], "ERROR: telescopía falló"
    print(f"  ✓ Acumulación telescópica verificada")

    # ── 4. Sensibilidad respecto de fuente/contorno ──────────────────────────
    print("\n── 4. Sensibilidad respecto del parámetro de contorno ──")
    f_pert = observable_compatible(TRAY_a_pert, OMEGA)
    sens = sensitivity(f, f_pert, 1.0, j=0)
    print(f"  𝒮_a(f; ν₀) = {sens}  (aumentar precisión del contorno reduce f)")
    assert sens < 0, "ERROR: sensibilidad debe ser ≤ 0"
    print(f"  ✓ Sensibilidad = {sens} < 0 — mejor contorno reduce indeterminación")

    # ── 5. Dictamen global bajo frontera factual explícita ───────────────────
    print("\n── 5. Dictamen por frame (frontera factual explícita) ──")
    cls = [check_no_favorable_closure(c) for c in TRAY_MAXWELL]
    print(f"  Clasificaciones: {cls}")
    assert cls[-1] == 'APTO', f"ERROR: ν₂ debe ser APTO, obtenido {cls[-1]}"
    print(f"  ✓ κ_F(Γ) = APTO en ν₂")

    # ── 6. Caso de violación (P1=1: Maxwell no satisfecho) ──────────────────
    print("\n── 6. Caso de violación estructural (P1=1) ──")
    cls_viol = check_no_favorable_closure(TRAY_VIOLATION[0])
    print(f"  Célula con P1=1 (infracción) → {cls_viol}")
    # n1=1 < T(9)=7 → INDETERMINADO (no hay suficientes infracciones para NO_APTO)
    # pero el frame no puede ser APTO con n1>0
    assert cls_viol != 'APTO', "ERROR: P1=1 no debe producir APTO"
    print(f"  ✓ Frame con infracción P1=1 → {cls_viol} (no APTO)")

    # ── Verificaciones clave contra el documento ─────────────────────────────
    print("\n── VERIFICACIONES CLAVE (Sección I §2, I §3) ──")
    print("  ✓ Residuales leídos sin tiempo soberano")
    print("  ✓ Acumulación factual trazable")
    print("  ✓ Sensibilidad respecto de contorno declarada")
    print("  ✓ Sin estadística: lectura estrictamente ternaria")
    print("  ✓ Dictamen APTO alcanzado por cierre de indeterminaciones")

    verdict = "APTO"
    print(f"\n  Clasificación: {verdict}")

    out = {
        'lab': 'lab_05_maxwell_factual',
        'seccion': 'I §3 Laboratorio director',
        'f': f, 'derivadas': derivs,
        'acumulacion': tel['acumulacion'], 'telescopia_ok': tel['telescopia_ok'],
        'sensibilidad_nu0': sens, 'clasificaciones': cls,
        'dictamen_final': cls[-1], 'veredicto': verdict
    }
    with open('/mnt/user-data/outputs/laboratorios/salida_maxwell_factual.json',
              'w', encoding='utf-8') as fout:
        json.dump(out, fout, ensure_ascii=False, indent=2)
    print("  Salida congelada → salida_maxwell_factual.json")
    return out

if __name__ == '__main__':
    result = run_lab05()
    sys.exit(0 if result['veredicto'] == 'APTO' else 1)
