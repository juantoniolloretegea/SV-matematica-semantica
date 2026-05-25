# -*- coding: utf-8 -*-
"""
================================================================================
LABORATORIO 05 — DENSIDAD GRAVITATORIA EFECTIVA DE SUTURA EN BANCO INICIAL B₀
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

Articulación canónica de la sutura (corpus previo):
    Lloret Egea, J. A. (2026a). Imperfección preformal y espacio.
        https://doi.org/10.21428/39829d0b.9c57c046
    Lloret Egea, J. A. (2026b). Teoría general de sucesos generadores.
        https://doi.org/10.17613/177nb-v2465

PROPÓSITO
---------
Calcula la densidad gravitatoria efectiva de sutura para el banco inicial B₀,
por diferencia estructural:

    ρ_sut,grav^SV(Ω_T;B₀) = ρ_cap^SV(Ω_T) − ρ_ret^SV(Ω_T;B₀) − ρ_C^SV(Ω_T;B₀)

La sutura NO es materia oscura renombrada bajo otra etiqueta técnica. Es
construcción canónica derivada de la articulación entre raigal Ξ_SV,
imperfección preformal ε−0 y operación de clausura, según las sedes canónicas
previas del corpus. Su cifra es indexada por inventario: cambia con cada banco
material auditado, pero el resultado nuclear ρ_DM,sustancia^SV = 0 no depende
del banco material concreto.

ATENCIÓN
--------
Este código forma parte de la obra protegida intelectualmente bajo licencia
CC BY-NC-ND 4.0. Cualquier referencia académica debe citar la sede canónica
original con DOI cuando esté disponible. Uso no comercial y sin obras derivadas.

================================================================================
"""

from decimal import Decimal, getcontext
from lab_03_capacidad_estructural import calcular_densidad_capacidad
from lab_04_inventario_b0 import RHO_A_B0

getcontext().prec = 50


# ==============================================================================
# CÁLCULO DE LA SUTURA EN BANCO INICIAL B₀
# ==============================================================================

# Residual de no clausura para banco inicial.
# En B₀ se conserva como U (no clausurado) por la frontera del inventario;
# para cálculo del auxiliar escalar se toma RHO_C_B0 = 0 con declaración
# explícita de los términos vivos que permanecen en U.
RHO_C_B0 = Decimal(0)


def calcular_sutura_inicial():
    """
    Calcula la sutura inicial bajo materialidad admitida conservadora:

        ρ_sut,grav^SV(Ω_T;B₀) = ρ_cap^SV(Ω_T) − ρ_A^SV(Ω_T;B₀) − ρ_C^SV(Ω_T;B₀)

    El término U(ρ_U^SV) se conserva vivo y NO se descuenta del auxiliar
    escalar; su presencia se declara explícitamente en la salida.

    Retorna:
        dict con los componentes y la sutura resultante.
    """
    rho_cap = calcular_densidad_capacidad()
    rho_A = RHO_A_B0
    rho_C = RHO_C_B0

    sutura = rho_cap - rho_A - rho_C

    return {
        "rho_cap_SV": rho_cap,
        "rho_A_SV_B0": rho_A,
        "rho_U_SV_B0": "U(causa; B₀) — vivo, no clausurado en B₀",
        "rho_C_SV_B0": rho_C,
        "sutura": sutura,
    }


def cifras_contemporaneas_contraste():
    """
    Cifras del banco contemporáneo Planck Collaboration (2020) para contraste
    posterior con la sutura. NO entran en el cálculo: son referencias externas
    de comparación final tras el resultado del banco SV.
    """
    return {
        "rho_crit_contemporanea": Decimal("8.5E-27"),    # kg/m³
        "rho_DM_contemporanea":   Decimal("2.3E-27"),    # kg/m³
        "rho_Lambda_contemporanea": Decimal("5.8E-27"),  # kg/m³
        "rho_bar_contemporanea":  Decimal("4.2E-28"),    # kg/m³
    }


def imprimir_resultado():
    """Imprime la sutura del banco inicial con todas sus declaraciones."""
    r = calcular_sutura_inicial()
    contemp = cifras_contemporaneas_contraste()

    print("=" * 80)
    print("DENSIDAD GRAVITATORIA EFECTIVA DE SUTURA — BANCO INICIAL B₀")
    print("=" * 80)

    print("\n  Fórmula rectora:")
    print("      ρ_sut,grav^SV(Ω_T;B) = ρ_cap^SV(Ω_T) − ρ_ret^SV(Ω_T;B)")
    print("                            − ρ_C^SV(Ω_T;B)")

    print("\n  Componentes con banco inicial B₀:")
    print(f"      ρ_cap^SV(Ω_T)         = {r['rho_cap_SV']:.6E} kg·m⁻³")
    print(f"      ρ_A^SV(Ω_T;B₀)        = {r['rho_A_SV_B0']:.6E} kg·m⁻³")
    print(f"      ρ_U^SV(Ω_T;B₀)        = {r['rho_U_SV_B0']}")
    print(f"      ρ_C^SV(Ω_T;B₀)        = {r['rho_C_SV_B0']}")

    print("\n  Sutura inicial (auxiliar escalar):")
    print(f"      ρ_sut,grav^SV(Ω_T;B₀) = {r['sutura']:.6E} kg·m⁻³")
    print(f"      ≈ 8.99 × 10⁻²⁷ kg·m⁻³")

    print("\n  Contraste con banco contemporáneo (referencias externas):")
    print(f"      ρ_crit (Planck 2020)  = {contemp['rho_crit_contemporanea']:.2E} kg·m⁻³")
    print(f"      ρ_DM (Planck 2020)    = {contemp['rho_DM_contemporanea']:.2E} kg·m⁻³")
    print(f"      ρ_Λ (Planck 2020)     = {contemp['rho_Lambda_contemporanea']:.2E} kg·m⁻³")

    print("\n  Lecturas operativas:")
    print("      • La sutura del banco inicial NO se compara puntualmente con")
    print("        ρ_DM aislada. El contraste correcto exige transducción por")
    print("        subdominios físicos (curvas, lentes, cúmulos, CMB).")
    print("      • La cifra 8.99 × 10⁻²⁷ kg·m⁻³ es salida de banco inicial bajo")
    print("        materialidad admitida conservadora. NO es cifra universal")
    print("        final ni densidad de sustancia oscura renombrada.")
    print("      • La articulación interna Λ_SV,puro / ρ_sut,grav^SV constituye")
    print("        zona de desarrollo doctrinal posterior del corpus.")

    print("\n" + "=" * 80)


if __name__ == "__main__":
    imprimir_resultado()
