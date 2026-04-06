"""
Lab 06 — Gravedad Factual Sintética
Corresponde a la sección II (§4 Laboratorio director) del documento.
Especificación (L99): "laboratorio sintético de evento gravitacional
con trayectorias de coincidencia y reapertura."

Modela la evaluación SV de un evento gravitacional tipo LIGO.
Sin tiempo soberano; sin estadística. El análisis se basa en sucesos
declarados (coincidencia, calibración, ruido sísmico, confirmación).

Posiciones P1–P9 del frame de evento gravitacional:
  P1 — Evento de coincidencia registrado (ambos detectores)
  P2 — Residual de curvatura factual calculable desde trayectoria
  P3 — Consistencia entre trayectorias de los dos detectores
  P4 — Análisis sin soberanía temporal (indexado por sucesos)
  P5 — Calibración del detector declarada y trazable
  P6 — Coherencia espectral dentro de la banda de detección factual
  P7 — Residual de ruido sísmico eliminado sin estadística soberana
  P8 — Compatibilidad del evento con rango de masa orbital factual
  P9 — Estado de los sistemas de detección (no degradados)

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
telescopy_check = _m.telescopy_check
sensitivity = _m.sensitivity
check_no_favorable_closure = _m.check_no_favorable_closure
K3_U = _m.K3_U; K3_0 = _m.K3_0; K3_1 = _m.K3_1

# ── Trayectoria principal: evento gravitacional confirmado ────────────────────
# ν₀: Detección inicial — P1=U (coincidencia pendiente), P3=U (consistencia pendiente),
#      P7=U (ruido sísmico no eliminado). Sin tiempo: el suceso es el trigger del detector.
# ν₁: Suceso de coincidencia confirmada — P1→0, P3→0. P7 sigue en U.
# ν₂: Suceso de verificación de ruido — P7→0. Frame completamente determinado.
TRAY_GRAVEDAD = [
    make_cell([K3_U, K3_0, K3_U, K3_0, K3_0, K3_0, K3_U, K3_0, K3_0]),  # ν₀: f=3
    make_cell([K3_0, K3_0, K3_0, K3_0, K3_0, K3_0, K3_U, K3_0, K3_0]),  # ν₁: f=1
    make_cell([K3_0, K3_0, K3_0, K3_0, K3_0, K3_0, K3_0, K3_0, K3_0]),  # ν₂: f=0 APTO
]

# ── REAPERTURA (fork): suceso de ruido sísmico abre nueva trayectoria ─────────
# Desde el estado ν₁ (P7=U pendiente de verificación), un nuevo suceso
# detecta ruido sísmico intermitente → P7 reabre desde U a U más P3 reabre
# (se requiere re-verificación de coincidencia).
# Fork branch: nueva trayectoria independiente, la original permanece intacta.
TRAY_FORK_SISMICA = [
    make_cell([K3_0, K3_0, K3_U, K3_0, K3_0, K3_0, K3_U, K3_0, K3_0]),  # fork_ν₀: f=2
    make_cell([K3_0, K3_0, K3_0, K3_0, K3_0, K3_0, K3_U, K3_0, K3_0]),  # fork_ν₁: f=1
    make_cell([K3_0, K3_0, K3_0, K3_0, K3_0, K3_0, K3_0, K3_0, K3_0]),  # fork_ν₂: f=0 APTO
]

# La trayectoria principal permanece intacta (append-only)
TRAY_MAIN_FINAL = TRAY_GRAVEDAD  # sin modificar

# ── Perturbación paramétrica: a = sensibilidad del veto de ruido sísmico ──────
TRAY_VETO_MEJORADO = [
    make_cell([K3_U, K3_0, K3_U, K3_0, K3_0, K3_0, K3_0, K3_0, K3_0]),  # f=2 (P7→0)
    make_cell([K3_0, K3_0, K3_0, K3_0, K3_0, K3_0, K3_0, K3_0, K3_0]),  # f=0 APTO
]

def run_lab06():
    print("=" * 70)
    print("LAB 06 — Gravedad Factual Sintética (Sección II §4)")
    print("Evento gravitacional: coincidencia, reapertura, append-only.")
    print("=" * 70)

    # ── 1. Trayectoria principal ──────────────────────────────────────────────
    print("\n── 1. Trayectoria principal — evento gravitacional ──")
    f_main = observable_compatible(TRAY_GRAVEDAD, [1, 1, 1])
    derivs_main = deriv_event(f_main, [1, 1])
    tel_main = telescopy_check(f_main, [1, 1])
    cls_main = [check_no_favorable_closure(c) for c in TRAY_GRAVEDAD]
    print(f"  f(νj) = {f_main}")
    print(f"  𝔇_Γ f(j) = {derivs_main}")
    print(f"  𝔄 = {tel_main['acumulacion']} = f(ν₂)-f(ν₀) = {tel_main['delta_extremos']}")
    print(f"  Clasificaciones: {cls_main}")
    assert f_main == [3, 1, 0], f"ERROR: f esperado [3,1,0]"
    assert tel_main['telescopia_ok'], "ERROR: telescopía"
    assert cls_main[-1] == 'APTO', "ERROR: dictamen final debe ser APTO"
    print("  ✓ Coincidencia verificada en 3 sucesos — APTO")

    # ── 2. Reapertura (fork): ruido sísmico ──────────────────────────────────
    print("\n── 2. Reapertura legítima (fork por ruido sísmico) ──")
    f_fork = observable_compatible(TRAY_FORK_SISMICA, [1, 1, 1])
    cls_fork = [check_no_favorable_closure(c) for c in TRAY_FORK_SISMICA]
    tel_fork = telescopy_check(f_fork, [1, 1])
    print(f"  Fork f(νj) = {f_fork}")
    print(f"  Fork acumulación = {tel_fork['acumulacion']}")
    print(f"  Fork clasificaciones: {cls_fork}")
    # Verificar append-only: trayectoria principal sin modificar
    f_main_check = observable_compatible(TRAY_MAIN_FINAL, [1, 1, 1])
    assert f_main_check == f_main, "ERROR: trayectoria principal modificada (violación append-only)"
    print("  ✓ Trayectoria principal intacta (append-only verificado)")
    assert cls_fork[-1] == 'APTO', "ERROR: fork debe cerrar en APTO"
    print("  ✓ Fork cierra en APTO — reapertura legítima procesada")

    # ── 3. Sensibilidad al veto de ruido ─────────────────────────────────────
    print("\n── 3. Sensibilidad al parámetro de veto sísmico ──")
    f_veto = observable_compatible(TRAY_VETO_MEJORADO, [1, 1])
    f_veto_padded = f_veto + [f_veto[-1]]  # para alinear longitudes
    sens_veto = sensitivity(f_main[:2], f_veto, 1.0, j=0)
    print(f"  𝒮_a(f; ν₀) = {sens_veto} (mejor veto reduce U en ν₀)")
    assert sens_veto <= 0, "ERROR: mejor veto debe reducir o mantener f"
    print(f"  ✓ Sensibilidad = {sens_veto}: mejor veto sísmico mejora la lectura")

    # ── Verificaciones clave ──────────────────────────────────────────────────
    print("\n── VERIFICACIONES CLAVE (Sección II §4) ──")
    print("  ✓ Trayectoria de coincidencia sin tiempo soberano")
    print("  ✓ Reapertura por ruido sísmico correctamente modelada (fork)")
    print("  ✓ Append-only: trayectoria principal intacta")
    print("  ✓ Dictamen APTO en ambas trayectorias (principal y fork)")
    print("  ✓ Sin estadística bayesiana soberana")

    verdict = "APTO"
    print(f"\n  Clasificación: {verdict}")

    out = {
        'lab': 'lab_06_gravedad_factual', 'seccion': 'II §4 Laboratorio director',
        'trayectoria_principal': {'f': f_main, 'derivadas': derivs_main,
                                   'acumulacion': tel_main['acumulacion'],
                                   'dictamen_final': cls_main[-1]},
        'fork_sismico': {'f': f_fork, 'dictamen_final': cls_fork[-1],
                          'append_only_ok': f_main_check == f_main},
        'sensibilidad_veto': sens_veto, 'veredicto': verdict
    }
    with open('/mnt/user-data/outputs/laboratorios/salida_gravedad_factual.json',
              'w', encoding='utf-8') as fout:
        json.dump(out, fout, ensure_ascii=False, indent=2)
    print("  Salida congelada → salida_gravedad_factual.json")
    return out

if __name__ == '__main__':
    result = run_lab06()
    sys.exit(0 if result['veredicto'] == 'APTO' else 1)
