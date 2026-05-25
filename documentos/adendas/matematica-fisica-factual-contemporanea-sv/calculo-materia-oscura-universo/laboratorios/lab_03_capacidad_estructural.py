# -*- coding: utf-8 -*-
"""
================================================================================
LABORATORIO 03 — CAPACIDAD ESTRUCTURAL DEL DOMINIO FÍSICO REALIZADO
================================================================================

Autor:               Juan Antonio Lloret Egea
ORCID:               https://orcid.org/0000-0002-6634-3351
Sello editorial:     Instituto Tecnológico Virtual de la Inteligencia Artificial
                     para el Español (ITVIA)
Publicación:         IA eñ — La Biblia de la IA
ISSN:                2695-6411  (https://portal.issn.org/resource/ISSN/2695-6411)
Licencia:            Creative Commons Attribution-NonCommercial-NoDerivatives 4.0
                     International (CC BY-NC-ND 4.0)
                     https://creativecommons.org/licenses/by-nc-nd/4.0/
Fecha:               25 de mayo de 2026
Lugar:               Madrid

Trabajo de referencia:
    Lloret Egea, J. A. (2026). La materia oscura no existe como sustancia:
    Demostración formal de nulidad sustancial, densidad gravitatoria efectiva
    de sutura y contraste físico escalable. ITVIA — IA eñ — La Biblia de la IA.

PROPÓSITO
---------
Calcula la capacidad estructural del dominio físico realizado bajo régimen de
retorno ciclo-distancial T_obs:

    ρ_cap^SV(Ω_T) = 3 / (8π · G · T_obs²)   [densidad equivalente]
    m_cap^SV(Ω_T) = c³ · T_obs / (2G)        [capacidad integrada]
    V_T^SV         = (4π/3) · (c · T_obs)³   [volumen operativo]

Estas magnitudes no constituyen inventario de materia escondida. Representan
expresión en unidades del Sistema Internacional de una capacidad estructural,
obtenida mediante transducción metrológica declarada desde Λ_SV,puro con G
como conversor metrológico explícito.

ATENCIÓN
--------
Este código forma parte de la obra protegida intelectualmente bajo licencia
CC BY-NC-ND 4.0. Cualquier referencia académica debe citar la sede canónica
original con DOI cuando esté disponible. Uso no comercial y sin obras derivadas.

================================================================================
"""

from decimal import Decimal, getcontext
from lab_01_constantes_fundamentales_sv import T_OBS, C, G, PI
from lab_02_lambda_sv_puro import LAMBDA_SV_PURO

getcontext().prec = 50


# ==============================================================================
# CÁLCULOS DE CAPACIDAD ESTRUCTURAL
# ==============================================================================

def calcular_volumen_operativo():
    """
    V_T^SV = (4π/3) · (c · T_obs)³

    Retorna:
        Decimal: volumen en m³.
    """
    radio = C * T_OBS
    return (Decimal(4) * PI / Decimal(3)) * radio ** 3


def calcular_densidad_capacidad():
    """
    ρ_cap^SV(Ω_T) = 3 / (8π · G · T_obs²)

    Equivalentemente, por transducción metrológica desde la curvatura:
    ρ_cap^SV = Λ_SV,puro · c² / (8π · G)

    Retorna:
        Decimal: densidad en kg·m⁻³.
    """
    return Decimal(3) / (Decimal(8) * PI * G * T_OBS ** 2)


def calcular_masa_capacidad():
    """
    m_cap^SV(Ω_T) = c³ · T_obs / (2G)

    Capacidad integrada del dominio sobre su volumen operativo.

    Retorna:
        Decimal: masa en kg.
    """
    return C ** 3 * T_OBS / (Decimal(2) * G)


def verificar_consistencia():
    """
    Verifica la consistencia interna del cálculo:

        m_cap^SV = ρ_cap^SV · V_T^SV   (definición integral)
        ρ_cap^SV = Λ_SV,puro · c² / (8π · G)   (transducción desde curvatura)
    """
    rho_cap = calcular_densidad_capacidad()
    m_cap = calcular_masa_capacidad()
    V_T = calcular_volumen_operativo()
    rho_desde_lambda = LAMBDA_SV_PURO * C ** 2 / (Decimal(8) * PI * G)

    # Verificación 1: producto densidad por volumen recupera la masa
    m_desde_rho_y_V = rho_cap * V_T
    error_1 = abs((m_desde_rho_y_V - m_cap) / m_cap)

    # Verificación 2: densidad desde Λ coincide con densidad directa
    error_2 = abs((rho_desde_lambda - rho_cap) / rho_cap)

    return {
        "rho_cap": rho_cap,
        "m_cap": m_cap,
        "V_T": V_T,
        "rho_desde_lambda": rho_desde_lambda,
        "consistencia_masa_volumen": error_1,
        "consistencia_lambda_densidad": error_2,
    }


# Cifras canónicas establecidas en el trabajo:
RHO_CAP_CANONICA = Decimal("9.429953786784435E-27")  # kg/m³
M_CAP_CANONICA = Decimal("8.790416297944350E52")     # kg


def imprimir_resultado():
    """Imprime los resultados con verificación canónica."""
    rho = calcular_densidad_capacidad()
    m = calcular_masa_capacidad()
    V = calcular_volumen_operativo()

    print("=" * 80)
    print("CAPACIDAD ESTRUCTURAL DEL DOMINIO FÍSICO REALIZADO Ω_T")
    print("=" * 80)

    print(f"\n  Volumen operativo del dominio:")
    print(f"      V_T^SV = (4π/3) · (c · T_obs)³")
    print(f"             = {V:.6E} m³")

    print(f"\n  Densidad de capacidad estructural:")
    print(f"      ρ_cap^SV(Ω_T) = 3 / (8π · G · T_obs²)")
    print(f"                    = {rho:.16E} kg·m⁻³")
    print(f"      cifra canónica = {RHO_CAP_CANONICA:.16E} kg·m⁻³")

    print(f"\n  Capacidad integrada:")
    print(f"      m_cap^SV(Ω_T) = c³ · T_obs / (2G)")
    print(f"                    = {m:.16E} kg")
    print(f"      cifra canónica = {M_CAP_CANONICA:.16E} kg")

    v = verificar_consistencia()
    print(f"\n  Verificaciones de consistencia interna:")
    print(f"      m_cap = ρ_cap · V_T :")
    print(f"          error relativo = {v['consistencia_masa_volumen']:.2E}")
    print(f"      ρ_cap = Λ_SV,puro · c² / (8π · G) :")
    print(f"          error relativo = {v['consistencia_lambda_densidad']:.2E}")

    print("\n  Naturaleza ontológica:")
    print("      Estas cifras NO representan inventario de materia.")
    print("      Expresan capacidad estructural del dominio en unidades SI")
    print("      mediante transducción metrológica con G como conversor.")

    print("\n" + "=" * 80)


if __name__ == "__main__":
    imprimir_resultado()
