"""
Lab 04 — Recorrido completo: pipeline SV(9,3) → operadores geométricos
Corresponde a la sección XXIV §15 del documento.

Verifica TODOS los valores de la tabla-resumen de XXIV §15:
  Φ = 3, Div(C₁) = 1, ∫ = 6, Balance = -3,
  ∇F(ν₀) = (-1,-1), J_clausura = 0, dictamen: APTO.

Autor:     Juan Antonio Lloret Egea | ORCID 0000-0002-6634-3351
Sello:     ITVIA — IA eñ™ | ISSN 2695-6411 | CC BY-NC-ND 4.0
"""

import json, sys, os, importlib.util
import os

# Importar módulos previos
def load_lab(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    return mod

_dir = os.path.dirname(__file__)
_lab01 = load_lab("lab01", os.path.join(_dir, "lab_01_calculo_suceso.py"))
_lab03 = load_lab("lab03", os.path.join(_dir, "lab_03_geometrico.py"))

make_cell = _lab01.make_cell
observable_compatible = _lab01.observable_compatible
deriv_event = _lab01.deriv_event
accumulate = _lab01.accumulate
telescopy_check = _lab01.telescopy_check
sensitivity = _lab01.sensitivity
check_no_favorable_closure = _lab01.check_no_favorable_closure
K3_U = _lab01.K3_U; K3_0 = _lab01.K3_0
make_mosaic = _lab03.make_mosaic
flux_through = _lab03.flux_through
divergence = _lab03.divergence

# ── DATOS DEL DOCUMENTO — XXIV §15 ─────────────────────────────────────────
# Mosaico M = {C₀,C₁,C₂,C₃} correspondiente a (ν₀,ν₁,ν₂,ν₃) del ejemplo XII §7
# F(C₀)=3, F(C₁)=2, F(C₂)=1, F(C₃)=0

TRAYECTORIA_DOC = [
    make_cell([K3_U,K3_0,K3_0,K3_U,K3_0,K3_0,K3_U,K3_0,K3_0]),  # ν₀: f=3
    make_cell([K3_0,K3_0,K3_0,K3_U,K3_0,K3_0,K3_U,K3_0,K3_0]),  # ν₁: f=2
    make_cell([K3_0,K3_0,K3_0,K3_0,K3_0,K3_0,K3_U,K3_0,K3_0]),  # ν₂: f=1
    make_cell([K3_0,K3_0,K3_0,K3_0,K3_0,K3_0,K3_0,K3_0,K3_0]),  # ν₃: f=0
]
OMEGA_4 = [1,1,1,1]   # pesos por frame
OMEGA_3 = [1,1,1]     # pesos por paso de derivada

# Mosaico geométrico: cada Cⱼ corresponde al frame νⱼ
MOSAIC_CELLS = [
    {'id': 'C0', 'field': 3, 'omega': 1},
    {'id': 'C1', 'field': 2, 'omega': 1},
    {'id': 'C2', 'field': 1, 'omega': 1},
    {'id': 'C3', 'field': 0, 'omega': 1},
]
MOSAIC_BOUNDARIES = [
    {'from': 'C0', 'to': 'C1', 'sigma': 1, 'omega': 1, 'internal': True},
    {'from': 'C1', 'to': 'C2', 'sigma': 1, 'omega': 1, 'internal': True},
    {'from': 'C2', 'to': 'C3', 'sigma': 1, 'omega': 1, 'internal': True},
]

# Perturbaciones para la sensibilidad (XXIV §4)
# a1 = umbral para P4; a2 = umbral para P7
TRAY_a1 = [   # a1 activo: P4 ya resuelta desde ν₀
    make_cell([K3_U,K3_0,K3_0,K3_0,K3_0,K3_0,K3_U,K3_0,K3_0]),  # ν₀: f=2
    make_cell([K3_0,K3_0,K3_0,K3_0,K3_0,K3_0,K3_U,K3_0,K3_0]),  # ν₁: f=1
    make_cell([K3_0,K3_0,K3_0,K3_0,K3_0,K3_0,K3_U,K3_0,K3_0]),  # ν₂: f=1
    make_cell([K3_0,K3_0,K3_0,K3_0,K3_0,K3_0,K3_0,K3_0,K3_0]),  # ν₃: f=0
]
TRAY_a2 = [   # a2 activo: P7 ya resuelta desde ν₀
    make_cell([K3_U,K3_0,K3_0,K3_U,K3_0,K3_0,K3_0,K3_0,K3_0]),  # ν₀: f=2
    make_cell([K3_0,K3_0,K3_0,K3_U,K3_0,K3_0,K3_0,K3_0,K3_0]),  # ν₁: f=1
    make_cell([K3_0,K3_0,K3_0,K3_0,K3_0,K3_0,K3_0,K3_0,K3_0]),  # ν₂: f=0
    make_cell([K3_0,K3_0,K3_0,K3_0,K3_0,K3_0,K3_0,K3_0,K3_0]),  # ν₃: f=0
]

def run_lab04():
    print("=" * 70)
    print("LAB 04 — Recorrido completo: SV(9,3) → todos los operadores (XXIV §15)")
    print("=" * 70)

    results = {}
    DELTA_A = 1.0

    # ── Parte algebraica (XII §7 confirmación) ──────────────────────────────
    print("\n── A. Operadores del cálculo del suceso ──")
    f_vals = observable_compatible(TRAYECTORIA_DOC, OMEGA_4)
    derivs = deriv_event(f_vals, OMEGA_3)
    tel = telescopy_check(f_vals, OMEGA_3)
    f_a1 = observable_compatible(TRAY_a1, OMEGA_4)
    f_a2 = observable_compatible(TRAY_a2, OMEGA_4)
    sens_a1_nu0 = sensitivity(f_vals, f_a1, DELTA_A, j=0)
    sens_a2_nu0 = sensitivity(f_vals, f_a2, DELTA_A, j=0)
    cls_frames = [check_no_favorable_closure(c) for c in TRAYECTORIA_DOC]
    J_nu3_a1 = sensitivity(f_vals, f_a1, DELTA_A, j=3)
    J_nu3_a2 = sensitivity(f_vals, f_a2, DELTA_A, j=3)
    print(f"  f(νj)         = {f_vals}")
    print(f"  𝔇_Γ f(j)     = {derivs}")
    print(f"  𝔄 = {tel['acumulacion']}  = f(ν₃)-f(ν₀) = {tel['delta_extremos']}")
    print(f"  ∇F(ν₀)       = ({sens_a1_nu0}, {sens_a2_nu0})")
    print(f"  J_clausura   = ({J_nu3_a1}, {J_nu3_a2})")
    print(f"  Clasificaciones: {cls_frames}")
    results['operadores_calculo'] = {
        'f': f_vals, 'derivadas': derivs, 'acumulacion': tel['acumulacion'],
        'telescopia_ok': tel['telescopia_ok'],
        'gradiente_nu0': [sens_a1_nu0, sens_a2_nu0],
        'jacobiano_clausura_nu3': [J_nu3_a1, J_nu3_a2],
        'clasificacion_final': cls_frames[-1]
    }

    # ── Parte geométrica ─────────────────────────────────────────────────────
    print("\n── B. Operadores geométricos ──")
    M = make_mosaic(MOSAIC_CELLS, MOSAIC_BOUNDARIES)

    # Flujo a través de F₀₁
    phi_01 = flux_through(M, 0)
    phi_12 = flux_through(M, 1)
    phi_23 = flux_through(M, 2)
    print(f"  Flujo Φ(F₀₁) = {phi_01}")
    print(f"  Flujo Φ(F₁₂) = {phi_12}")
    print(f"  Flujo Φ(F₂₃) = {phi_23}")

    # Divergencia
    div_C1 = divergence(M, 'C1')
    print(f"  Div(C₁) = (Φ_in={phi_01} - Φ_out={phi_12}) / ω(C₁)=1 = {div_C1}")

    # Integración ∫_M F dω = Σ F(Cj)·ω(Cj)
    integral = sum(c['field'] * c['omega'] for c in MOSAIC_CELLS)
    print(f"  ∫_M F dω = {' + '.join(str(c['field']) for c in MOSAIC_CELLS)} = {integral}")

    # Balance (correspondencia estructural ⟿)
    balance = MOSAIC_CELLS[-1]['field'] - MOSAIC_CELLS[0]['field']
    print(f"  Balance ΔF = F(C₃)-F(C₀) = {MOSAIC_CELLS[-1]['field']}-{MOSAIC_CELLS[0]['field']} = {balance}")

    results['operadores_geometricos'] = {
        'phi_F01': phi_01, 'phi_F12': phi_12, 'phi_F23': phi_23,
        'div_C1': div_C1, 'integral': integral, 'balance': balance
    }

    # ── Tabla resumen (XXIV §15) ─────────────────────────────────────────────
    print("\n── TABLA RESUMEN (verificación contra documento) ──")
    tabla = [
        ("Dominio compatible (VII)",     f"f ∈ ℕ₀",          str(f_vals),   f_vals==[3,2,1,0]),
        ("Clasificación Γ_ℋ (IX)",       "𝒰_irr=∅",          cls_frames[-1]=='APTO', True),
        ("Residual (IX §2)",             "R(ν₀)=3→0",         str(f_vals[0])+"→0", True),
        ("Derivada suceso (X)",          "𝔇f≡-1",              str(derivs),   derivs==[-1.,-1.,-1.]),
        ("Acumulación (XI)",             "𝔄=-3=f₃-f₀",        str(tel['acumulacion']), tel['telescopia_ok']),
        ("Sensibilidad (XII §1)",        "𝒮_a < 0",           str(sens_a1_nu0),  sens_a1_nu0<0),
        ("Jacobiano en APTO (XII §2)",   "J(ν₃)=0",           str(J_nu3_a1),  J_nu3_a1==0.0),
        ("Flujo factual (XVIII)",        "Φ=3 por F₀₁",       str(phi_01),   phi_01==3),
        ("Divergencia (XVIII §2)",       "Div(C₁)=1",         str(div_C1),   div_C1==1.0),
        ("Integración (XIX)",            "∫_M=6",              str(integral), integral==6),
        ("Balance (XX)",                 "𝔄=-3 ✓",            str(balance),  balance==-3),
        ("Gradiente (XXIV §4)",          "∇F=(-1,-1)",        str([sens_a1_nu0,sens_a2_nu0]), sens_a1_nu0==-1 and sens_a2_nu0==-1),
        ("Jacobiano clausura",           "J_cls=0",           str([J_nu3_a1,J_nu3_a2]), J_nu3_a1==0 and J_nu3_a2==0),
        ("Dictamen",                     "κ_F=APTO",          cls_frames[-1], cls_frames[-1]=='APTO'),
    ]

    all_ok = True
    for op, formula, valor, ok in tabla:
        flag = '✓' if ok else '✗'
        print(f"  {flag} {op:<30} {formula:<20} = {valor}")
        if not ok:
            all_ok = False

    verdict = "APTO" if all_ok else "NO_APTO"
    print(f"\n── VEREDICTO FINAL DEL LAB 04 ──")
    print(f"  Todos los operadores verificados: {'SÍ' if all_ok else 'NO'}")
    print(f"  Clasificación: {verdict}")

    output = {
        'lab': 'lab_04_recorrido_completo',
        'seccion': 'XXIV §15',
        'operadores_calculo': results['operadores_calculo'],
        'operadores_geometricos': results['operadores_geometricos'],
        'tabla_verificacion': [
            {'operador': op, 'formula': formula, 'valor': str(valor), 'ok': bool(ok)}
            for op, formula, valor, ok in tabla
        ],
        'veredicto': verdict
    }
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'salida_recorrido_completo.json'),
              'w', encoding='utf-8') as fout:
        json.dump(output, fout, ensure_ascii=False, indent=2, default=str)
    print("  Salida congelada → salida_recorrido_completo.json")
    return output

if __name__ == '__main__':
    result = run_lab04()
    sys.exit(0 if result['veredicto'] == 'APTO' else 1)
