"""
Lab 02 — Ejemplo director: los 7 planos sobre la célula SV(9,3)
Corresponde a la sección XII §7 del documento.

Verifica TODOS los valores declarados en el documento:
  - f(νj) = [3, 2, 1, 0]
  - Derivadas = [-1, -1, -1]   (descenso uniforme)
  - Acumulación = -3 = f(ν₃)-f(ν₀)   (relación fundamental)
  - Clasificación final: APTO
  - Jacobiano en APTO: [0, 0]   (insensible a parámetros del horizonte)

Autor:     Juan Antonio Lloret Egea | ORCID 0000-0002-6634-3351
Sello:     ITVIA — IA eñ™ | ISSN 2695-6411 | CC BY-NC-ND 4.0
"""

import json, sys
import os
# Importamos funciones del lab 01 (mismo directorio)
import importlib.util, os
_spec = importlib.util.spec_from_file_location(
    "lab01", os.path.join(os.path.dirname(__file__), "lab_01_calculo_suceso.py"))
_mod = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(_mod)
make_cell = _mod.make_cell
observable_compatible = _mod.observable_compatible
deriv_event = _mod.deriv_event
deriv_order2 = _mod.deriv_order2
accumulate = _mod.accumulate
telescopy_check = _mod.telescopy_check
sensitivity = _mod.sensitivity
jacobian_traj = _mod.jacobian_traj
check_no_favorable_closure = _mod.check_no_favorable_closure
K3_U = _mod.K3_U; K3_0 = _mod.K3_0; K3_1 = _mod.K3_1

# ── Datos exactos del ejemplo director (XII §7) ──────────────────────────────
# v₀ = (U,0,0,U,0,0,U,0,0) → P1=U, P4=U, P7=U
# v₁ = (0,0,0,U,0,0,U,0,0) → P4=U, P7=U
# v₂ = (0,0,0,0,0,0,U,0,0) → P7=U
# v₃ = (0,0,0,0,0,0,0,0,0) → APTO

TRAYECTORIA = [
    make_cell([K3_U,K3_0,K3_0,K3_U,K3_0,K3_0,K3_U,K3_0,K3_0]),  # ν₀
    make_cell([K3_0,K3_0,K3_0,K3_U,K3_0,K3_0,K3_U,K3_0,K3_0]),  # ν₁
    make_cell([K3_0,K3_0,K3_0,K3_0,K3_0,K3_0,K3_U,K3_0,K3_0]),  # ν₂
    make_cell([K3_0,K3_0,K3_0,K3_0,K3_0,K3_0,K3_0,K3_0,K3_0]),  # ν₃
]
OMEGA = [1, 1, 1, 1]  # pesos por frame (4 frames)

# Horizonte ℋ_NLP: los parámetros que gobiernan la apertura de P4 y P7
# Para la sensibilidad: si a1 baja el umbral de P4, un suceso adicional resuelve P4
# Simulamos f con un suceso extra activado:
TRAY_a1_perturbed = [   # a1 activado en ν₀: P4 ya resuelta desde el inicio
    make_cell([K3_U,K3_0,K3_0,K3_0,K3_0,K3_0,K3_U,K3_0,K3_0]),  # ν₀ con P4=0
    make_cell([K3_0,K3_0,K3_0,K3_0,K3_0,K3_0,K3_U,K3_0,K3_0]),  # ν₁
    make_cell([K3_0,K3_0,K3_0,K3_0,K3_0,K3_0,K3_U,K3_0,K3_0]),  # ν₂
    make_cell([K3_0,K3_0,K3_0,K3_0,K3_0,K3_0,K3_0,K3_0,K3_0]),  # ν₃
]

def run_lab02():
    print("=" * 70)
    print("LAB 02 — Ejemplo director: célula SV(9,3) bajo los 7 planos (XII §7)")
    print("=" * 70)

    results = {}

    # ── Plano I — Dominio compatible ────────────────────────────────────────
    print("\n── Plano I — Dominio compatible (VII §1) ──")
    f_vals = observable_compatible(TRAYECTORIA, OMEGA)
    print(f"  f(νj) = {f_vals}")
    assert f_vals == [3,2,1,0], f"ERROR: f esperado [3,2,1,0], obtenido {f_vals}"
    print("  ✓ Observable compatible f ∈ ℕ₀; valores verificados")
    results['plano_I'] = {'f': f_vals, 'ok': True}

    # ── Plano II — Equivalente clásico ──────────────────────────────────────
    print("\n── Plano II — Equivalente clásico (VIII §2) ──")
    delta_N = sum(1 for x in f_vals if x > 0)
    print(f"  Descenso f(ν₀)=3 → f(ν₃)=0 — análogo función convergente")
    print(f"  ΔN = {delta_N}  (profundidad de convergencia)")
    assert delta_N == 3, f"ERROR: ΔN esperado 3, obtenido {delta_N}"
    print("  ✓ ΔN = 3")
    results['plano_II'] = {'delta_N': delta_N, 'ok': True}

    # ── Plano III — U, residual y límite ────────────────────────────────────
    print("\n── Plano III — U, residual y límite (IX) ──")
    cls_frames = [check_no_favorable_closure(c) for c in TRAYECTORIA]
    n_irr = 0  # 𝒰_irr = ∅ por construcción del ejemplo (todas U son resolubles)
    residual_nu0 = f_vals[0]
    print(f"  𝒰_irr(ν₀) = ∅  (P1, P4, P7 son U-resolubles)")
    print(f"  Residual R(ν₀) = {residual_nu0}")
    print(f"  Clasificaciones por frame: {cls_frames}")
    print(f"  κ_F(Γ) = APTO en ν₃ (f(ν₃)=0)")
    assert cls_frames[-1] == 'APTO', f"ERROR: ν₃ debe ser APTO, obtenido {cls_frames[-1]}"
    print("  ✓ Límite estructural APTO alcanzado en ν₃")
    results['plano_III'] = {
        'U_irr': n_irr, 'residual_nu0': residual_nu0,
        'clasificaciones': cls_frames, 'limite': 'APTO', 'ok': True
    }

    # ── Plano IV — Derivada de suceso ────────────────────────────────────────
    print("\n── Plano IV — Derivada de suceso (X §2) ──")
    derivs = deriv_event(f_vals, OMEGA[:3])
    d2 = deriv_order2(derivs, [1,1])
    print(f"  𝔇_Γ f(j) = {derivs}")
    print(f"  Segunda derivada 𝔇²_Γ f = {d2}")
    assert derivs == [-1.0,-1.0,-1.0], \
        f"ERROR: derivadas esperadas [-1,-1,-1], obtenidas {derivs}"
    assert d2 == [0.0,0.0], f"ERROR: 𝔇² esperada [0,0] (variación lineal), obtenida {d2}"
    print("  ✓ Derivada constante = -1  (una U por suceso)")
    print("  ✓ Segunda derivada = 0  (variación lineal)")
    results['plano_IV'] = {'derivadas': derivs, 'segunda_derivada': d2, 'ok': True}

    # ── Plano V — Acumulación factual ────────────────────────────────────────
    print("\n── Plano V — Acumulación factual (XI §4) ──")
    tel = telescopy_check(f_vals, OMEGA[:3])
    print(f"  𝔄_Γ[0,3](𝔇_Γ f) = {tel['acumulacion']}")
    print(f"  f(ν₃) - f(ν₀) = {tel['delta_extremos']}")
    print(f"  |diferencia| = {tel['diferencia']:.2e}")
    assert tel['telescopia_ok'], "ERROR: relación fundamental falló"
    assert abs(tel['acumulacion'] - (-3.0)) < 1e-9, \
        f"ERROR: acumulación esperada -3, obtenida {tel['acumulacion']}"
    print("  ✓ 𝔄 = -3 = f(ν₃)-f(ν₀)  (relación fundamental)")
    results['plano_V'] = {'acumulacion': tel['acumulacion'],
                          'delta': tel['delta_extremos'], 'ok': True}

    # ── Plano VI — Sensibilidad factual ──────────────────────────────────────
    print("\n── Plano VI — Sensibilidad factual (XII §1) ──")
    f_a1 = observable_compatible(TRAY_a1_perturbed, [1,1,1,1])
    delta_a = 1.0  # variación unitaria del parámetro
    sens_j0 = sensitivity(f_vals, f_a1, delta_a, j=0)
    print(f"  f base en ν₀ = {f_vals[0]}, f perturbada en ν₀ = {f_a1[0]}")
    print(f"  𝒮_a1(f; ν₀) = ({f_a1[0]} - {f_vals[0]}) / {delta_a} = {sens_j0}")
    assert sens_j0 < 0, "ERROR: sensibilidad debe ser < 0 (activar suceso reduce f)"
    print(f"  ✓ Sensibilidad = {sens_j0} < 0  (activar suceso adicional reduce f)")
    results['plano_VI'] = {'sensibilidad_nu0': sens_j0, 'ok': True}

    # ── Plano VII — Jacobiano estructural ─────────────────────────────────────
    print("\n── Plano VII — Jacobiano estructural (XII §2) ──")
    # Para ν₃ (APTO), f(ν₃)=0 en todos los parámetros → Jacobiano = 0
    # f perturbada en ν₃: si a1 activa suceso extra, P4 ya cerrada → f(ν₃)=0 siempre
    f_a1_nu3 = f_a1[3]
    f_base_nu3 = f_vals[3]
    J_nu3 = (f_a1_nu3 - f_base_nu3) / delta_a
    print(f"  J_SV(ν₃)[a1] = ({f_a1_nu3} - {f_base_nu3}) / {delta_a} = {J_nu3}")
    assert J_nu3 == 0.0, f"ERROR: Jacobiano en APTO debe ser 0, obtenido {J_nu3}"
    print("  ✓ J_SV(ν₃) = 0  (punto de convergencia insensible a variaciones)")
    results['plano_VII'] = {'jacobiano_nu3': J_nu3, 'ok': True}

    # ── Cierre ────────────────────────────────────────────────────────────────
    print("\n── CIERRE DEL RECORRIDO ──")
    all_ok = all(v.get('ok', False) for v in results.values())
    verdict = "APTO" if all_ok else "NO_APTO"
    print(f"  Todos los planos verificados: {'SÍ' if all_ok else 'NO'}")
    print(f"  Clasificación: {verdict}")
    print(f"  ΔN=3, derivada uniforme, acumulación telescópica ✓")
    print(f"  residual monotónico, jacobiano nulo en cierre ✓")

    output = {
        'lab': 'lab_02_ejemplo_director',
        'seccion': 'XII §7',
        'datos': {'f': f_vals, 'omega': OMEGA, 'n_posiciones': 9, 'base': 3},
        'planos': results,
        'veredicto': verdict
    }
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'salida_ejemplo_director.json'),
              'w', encoding='utf-8') as fout:
        json.dump(output, fout, ensure_ascii=False, indent=2)
    print("  Salida congelada → salida_ejemplo_director.json")
    return output

if __name__ == '__main__':
    result = run_lab02()
    sys.exit(0 if result['veredicto'] == 'APTO' else 1)
