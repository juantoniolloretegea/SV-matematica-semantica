# -*- coding: utf-8 -*-
"""
lab_01_banco_numerico.py
========================

Laboratorio canónico 01 — Banco numérico de los diez supuestos del §17

Verifica el Teorema §17.1 (Cumplimiento canónico del banco numérico) del
documento V14: los diez supuestos del banco satisfacen 𝓤ᵘⁿⁱᶠ_SV = 0 con
verificación trazable componente a componente sobre los siete operadores
sectoriales y las siete identidades intersectoriales.

Salida: tabla numérica con residuo por componente y residuo total por
supuesto. Bajo construcción canónica, los residuos deben ser del orden
de la precisión de máquina (ε_máquina ≈ 1e-16).

Trazabilidad canónica:
    - V14, §17.1 a §17.11 (los diez supuestos)
    - V14, §17.12 (tabla canónica consolidada de dictámenes)
    - V14, §17.13 (verificación de identidad sintáctica entre formas)
    - V14, Teorema §17.1

Ejecución:
    python3 lab_01_banco_numerico.py
"""

from __future__ import annotations
from sv_core import (
    ConfiguracionEM, ConfiguracionGravitatoria, TrayectoriaTPA,
    evaluar_formula_completa, suma_absoluta, imprimir_cabecera,
)


# =====================================================================
# DATOS CANÓNICOS DE LOS DIEZ SUPUESTOS DEL BANCO §17
# Reproducidos literalmente de las subsecciones §17.2–§17.11 de V14
# =====================================================================

# Sector gravitatorio: régimen no detonante en todo el banco
GRAV_NO_DETONANTE = ConfiguracionGravitatoria(
    G_nu=0.0, G_J_nu=0.0, Q=0.0, E_crit=0.0, norma_J_QP=0.0
)

SUPUESTOS = [
    # ----- §17.1 — Tipología Σ_6: convergente con meseta inicial -----
    {
        "id": "§17.1",
        "tipologia": "Σ_6 convergente con meseta inicial",
        "em": ConfiguracionEM(
            D=(0.025, 0.025, 0.000, 0.000),
            B=(0.180, 0.120, 0.180, 0.120),
            Gamma_E=(0.067500, 0.067500, 0.067500, 0.067500),
            Gamma_H=(0.097500, 0.097500, 0.097500, 0.097500),
            rho=0.050/1.000,  # ρ tal que Div_SV(D) − ρV = 0
            V=1.000,
            A_Sigma=0.300,
            dnu_B=-0.900,
            dnu_D=0.500,
            J=(0.200, 0.200, 0.200, 0.200),
        ),
        "tpa": TrayectoriaTPA(phi=(5, 3, 3, 3)),
        "dictamen_S4": 3.0,  # m_0 = 3 UFM
        "alpha": (1.20, 1.50, 1.50, 1.50),
        "delta": (0.30, -0.20, -0.20, -0.20),
        "card_U_irr": 0,
        "dnu_rho": 0.0,
    },

    # ----- §17.2 — Tipología Σ_5: meseta integral -----
    {
        "id": "§17.2",
        "tipologia": "Σ_5 meseta integral",
        "em": ConfiguracionEM(
            D=(0.100, 0.100, 0.100, 0.100),
            B=(0.050, 0.050, 0.050, 0.050),
            Gamma_E=(0.060, 0.060, 0.060, -0.180),
            Gamma_H=(0.100, 0.100, 0.100, -0.100),
            rho=0.000, V=1.000, A_Sigma=0.400,
            dnu_B=0.000, dnu_D=0.000,
            J=(0.125, 0.125, 0.125, 0.125),
        ),
        "tpa": TrayectoriaTPA(phi=(1, 1, 1, 1)),
        "dictamen_S4": None,  # U sostenida
        "alpha": (0.80, 0.80, 0.80, 0.80),
        "delta": (0.20, 0.20, 0.20, 0.20),
        "card_U_irr": 0,
        "dnu_rho": 0.0,
    },

    # ----- §17.3 — Tipología Σ_2: exploratoria pura -----
    {
        "id": "§17.3",
        "tipologia": "Σ_2 exploratoria pura",
        "em": ConfiguracionEM(
            D=(0.300, 0.250, 0.300, 0.250),
            B=(0.400, 0.300, 0.400, 0.300),
            Gamma_E=(0.150, 0.200, 0.100, -0.450),
            Gamma_H=(0.500, 0.400, 0.300, -0.200),
            rho=0.000, V=1.000, A_Sigma=0.500,
            dnu_B=0.000, dnu_D=0.000,
            J=(0.500, 0.500, 0.500, 0.500),
        ),
        "tpa": TrayectoriaTPA(phi=(0, 1, 2, 3)),
        "dictamen_S4": None,  # χ_α
        "alpha": (0.10, 0.30, 0.50, 0.70),
        "delta": (0.10, 0.10, 0.10, 0.10),
        "card_U_irr": 0,
        "dnu_rho": 0.0,
    },

    # ----- §17.4 — Tipología Σ_3: bimodal apertura-cierre -----
    {
        "id": "§17.4",
        "tipologia": "Σ_3 bimodal apertura-cierre",
        "em": ConfiguracionEM(
            D=(0.400, 0.300, 0.360, 0.240),
            B=(0.360, 0.240, 0.360, 0.240),
            Gamma_E=(0.200, 0.240, 0.180, -0.080),
            Gamma_H=(0.400, 0.300, 0.360, -0.280),
            rho=0.100, V=1.000, A_Sigma=0.300,
            dnu_B=-1.800, dnu_D=1.000,
            J=(0.400, 0.400, 0.400, 0.400),
        ),
        "tpa": TrayectoriaTPA(phi=(5, 6, 5, 4)),
        "dictamen_S4": 4.0,
        "alpha": (1.00, 1.20, 1.40, 1.60),
        "delta": (0.20, 0.10, -0.30, -0.70),
        "card_U_irr": 0,
        "dnu_rho": 0.0,
    },

    # ----- §17.5 — Tipología Σ_4: bimodal cierre-apertura -----
    {
        "id": "§17.5",
        "tipologia": "Σ_4 bimodal cierre-apertura",
        "em": ConfiguracionEM(
            D=(0.500, 0.400, 0.200, 0.200),
            B=(0.250, 0.250, 0.250, 0.250),
            Gamma_E=(0.050, 0.100, 0.100, -0.250),
            Gamma_H=(0.300, 0.300, 0.200, -0.100),
            rho=0.500, V=1.000, A_Sigma=0.200,
            dnu_B=0.000, dnu_D=0.000,
            J=(0.875, 0.875, 0.875, 0.875),
        ),
        "tpa": TrayectoriaTPA(phi=(3, 2, 4, 5)),
        "dictamen_S4": None,  # χ_α
        "alpha": (0.90, 0.90, 1.10, 1.30),
        "delta": (0.20, 0.00, 0.00, 0.00),
        "card_U_irr": 0,
        "dnu_rho": 0.0,
    },

    # ----- §17.6 — Tipología Σ_1: convergente pura -----
    {
        "id": "§17.6",
        "tipologia": "Σ_1 convergente pura",
        "em": ConfiguracionEM(
            D=(0.800, 0.600, 0.500, 0.400),
            B=(0.300, 0.200, 0.300, 0.200),
            Gamma_E=(0.120, 0.180, 0.140, -0.440),
            Gamma_H=(0.600, 0.500, 0.400, -0.200),
            rho=0.500, V=1.000, A_Sigma=0.500,
            dnu_B=0.000, dnu_D=0.000,
            J=(0.650, 0.650, 0.650, 0.650),
        ),
        "tpa": TrayectoriaTPA(phi=(8, 6, 4, 2)),
        "dictamen_S4": 2.0,
        "alpha": (1.80, 2.00, 2.20, 2.40),
        "delta": (0.40, -0.20, -0.80, -1.40),
        "card_U_irr": 0,
        "dnu_rho": 0.0,
    },

    # ----- §17.7 — Tipología Σ_8: exploratoria con saturación -----
    {
        "id": "§17.7",
        "tipologia": "Σ_8 exploratoria con saturación",
        "em": ConfiguracionEM(
            D=(0.250, 0.250, 0.250, 0.250),
            B=(0.100, 0.100, 0.100, 0.100),
            Gamma_E=(0.050, 0.100, 0.100, -1.450),
            Gamma_H=(0.200, 0.150, 0.100, -0.050),
            rho=0.000, V=1.000, A_Sigma=0.400,
            dnu_B=3.000, dnu_D=0.200,
            J=(0.200, 0.200, 0.200, 0.200),
        ),
        "tpa": TrayectoriaTPA(phi=(2, 5, 5, 5, 5)),
        "dictamen_S4": None,
        "alpha": (0.40, 0.70, 0.70, 0.70, 0.70),
        "delta": (0.20, 0.20, 0.20, 0.20, 0.20),
        "card_U_irr": 0,
        "dnu_rho": 0.0,
    },

    # ----- §17.8 — Tipología Σ_7: convergente con meseta intercalada -----
    {
        "id": "§17.8",
        "tipologia": "Σ_7 convergente con meseta intercalada (irracionales)",
        "em": ConfiguracionEM(
            D=(__import__("math").sqrt(2)/4, __import__("math").sqrt(2)/4,
               __import__("math").sqrt(2)/8, __import__("math").sqrt(2)/8),
            B=(__import__("math").sqrt(3)/4, __import__("math").sqrt(3)/4,
               __import__("math").sqrt(3)/4, __import__("math").sqrt(3)/4),
            Gamma_E=(0.100, 0.150, 0.050, -0.300),
            Gamma_H=(0.400, 0.300, 0.200, -0.100),
            rho=__import__("math").sqrt(2)/4, V=1.000, A_Sigma=0.300,
            dnu_B=0.000, dnu_D=0.000,
            J=(2/3, 2/3, 2/3, 2/3),
        ),
        "tpa": TrayectoriaTPA(phi=(1, 4, 4, 7)),
        "dictamen_S4": 7.0,
        "alpha": (0.20, 0.50, 0.50, 0.80),
        "delta": (0.20, 0.20, 0.20, 0.20),
        "card_U_irr": 0,
        "dnu_rho": 0.0,
    },

    # ----- §17.9 — Tipología Σ_10: umbral tardío -----
    {
        "id": "§17.9",
        "tipologia": "Σ_10 umbral tardío",
        "em": ConfiguracionEM(
            D=(0.050, 0.040, 0.050, 0.040),
            B=(0.020, 0.020, 0.020, 0.020),
            Gamma_E=(0.020, 0.040, 0.020, -0.080),
            Gamma_H=(0.100, 0.080, 0.060, -0.040),
            rho=0.000, V=1.000, A_Sigma=0.500,
            dnu_B=0.000, dnu_D=0.000,
            J=(0.100, 0.100, 0.100, 0.100),
        ),
        "tpa": TrayectoriaTPA(phi=(5, 9, 9, 9, 9)),
        "dictamen_S4": None,
        "alpha": (0.80, 1.20, 1.20, 1.20, 1.20),
        "delta": (0.40, 0.60, 0.60, 0.60, 0.60),
        "card_U_irr": 0,
        "dnu_rho": 0.0,
    },

    # ----- §17.10 — Tipología Σ_9: multimodal compleja -----
    {
        "id": "§17.10",
        "tipologia": "Σ_9 multimodal compleja",
        "em": ConfiguracionEM(
            D=(1.000, 0.800, 1.000, 0.800),
            B=(0.500, 0.400, 0.500, 0.400),
            Gamma_E=(0.200, 0.300, 0.100, -0.600),
            Gamma_H=(0.800, 0.600, 0.500, -0.300),
            rho=0.000, V=1.000, A_Sigma=0.500,
            dnu_B=0.000, dnu_D=0.000,
            J=(0.800, 0.800, 0.800, 0.800),
        ),
        "tpa": TrayectoriaTPA(phi=(4, 5, 6, 5, 4, 3, 4, 5)),
        "dictamen_S4": None,
        "alpha": (0.80, 1.00, 1.20, 1.20, 1.20, 1.20, 1.40, 1.60),
        "delta": (0.40, 0.30, 0.20, 0.10, 0.00, -0.10, -0.20, -0.30),
        "card_U_irr": 0,
        "dnu_rho": 0.0,
    },
]


# =====================================================================
# EJECUCIÓN CANÓNICA DEL BANCO
# =====================================================================

def ejecutar_banco(tol: float = 1e-10) -> None:
    """Ejecuta los diez supuestos canónicamente y produce tabla."""
    imprimir_cabecera(
        "Lab 01 — Banco numérico canónico",
        "Teorema §17.1 (V14): cumplimiento del banco de diez supuestos"
    )

    print("Tolerancia canónica de anulación: ε = {:.2e}".format(tol))
    print()
    print("─" * 80)
    print(f"{'ID':<8} {'Tipología':<42} {'Σ|comp|':>14} {'𝔉_SV':>10}")
    print("─" * 80)

    pasados = 0
    for s in SUPUESTOS:
        ev = evaluar_formula_completa(
            em=s["em"], grav=GRAV_NO_DETONANTE, tpa=s["tpa"],
            card_U_irr=s["card_U_irr"], dnu_rho=s["dnu_rho"],
            alpha_serie=s["alpha"], delta_serie=s["delta"],
            m_0_dictamen=s["dictamen_S4"], tol=tol,
        )
        anula = ev.formula_se_anula
        marca = "= 0" if anula else "≠ 0 ⚠"
        if anula:
            pasados += 1
        print(f"{s['id']:<8} {s['tipologia']:<42} "
              f"{ev.suma_absoluta_componentes:>14.6e} {marca:>10}")

    print("─" * 80)
    print()
    print(f"Supuestos canónicamente anulados: {pasados}/10")
    print()

    if pasados == 10:
        print("VERIFICACIÓN CANÓNICA DEL TEOREMA §17.1:")
        print("  Los diez supuestos del banco §17 satisfacen 𝓤ᵘⁿⁱᶠ_SV = 0")
        print("  componente a componente, con residuos del orden de la")
        print("  precisión de máquina. Teorema §17.1 verificado.")
    else:
        print(f"⚠ AVISO: {10 - pasados} supuestos no anulan canónicamente.")
        print("  Revisar configuración o tolerancia.")

    print()
    print("═" * 71)


def detalle_supuesto(id_supuesto: str = "§17.1") -> None:
    """Muestra detalle componente a componente de un supuesto específico."""
    for s in SUPUESTOS:
        if s["id"] == id_supuesto:
            ev = evaluar_formula_completa(
                em=s["em"], grav=GRAV_NO_DETONANTE, tpa=s["tpa"],
                card_U_irr=s["card_U_irr"], dnu_rho=s["dnu_rho"],
                alpha_serie=s["alpha"], delta_serie=s["delta"],
                m_0_dictamen=s["dictamen_S4"],
            )
            print(f"\nDETALLE CANÓNICO — Supuesto {id_supuesto}: {s['tipologia']}\n")
            print(ev)
            return
    print(f"Supuesto {id_supuesto} no encontrado.")


if __name__ == "__main__":
    ejecutar_banco()
    print()
    detalle_supuesto("§17.1")
