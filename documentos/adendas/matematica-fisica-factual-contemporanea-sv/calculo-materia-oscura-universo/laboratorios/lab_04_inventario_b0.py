# -*- coding: utf-8 -*-
"""
================================================================================
LABORATORIO 04 — INVENTARIO INICIAL B₀ DE MATERIALIDAD RETORNADA
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

Banco contemporáneo de contraste:
    Planck Collaboration (2020). Planck 2018 results. VI. Cosmological parameters.
    Astronomy & Astrophysics, 641, A6.
    https://doi.org/10.1051/0004-6361/201833910

PROPÓSITO
---------
Construye el inventario inicial conservador B₀ de materialidad retornada del
dominio físico realizado, separando la salida en la tupla canónica:

    Ret_M^SV(Ω_T;B₀) = (ρ_A^SV, ρ_U^SV, ρ_E^SV, ρ_X^SV)

donde:
    ρ_A^SV  — materialidad admitida (bariones cosmológicos + neutrinos mínimos)
    ρ_U^SV  — materialidad candidata no clausurada (bariones difusos, gas
              caliente, remanentes compactos no identificados, baja luminosidad)
    ρ_E^SV  — retorno energético separado (radiación, fondos radiativos)
    ρ_X^SV  — exclusiones (ρ_DM contemporánea, estimadores gravitatorios puros,
              parámetros cosmológicos absorbidos como sustancia)

La materialidad retornada NO se calcula por resta contra ρ_DM contemporánea.
Se construye por admisión positiva con las restricciones canónicas del corpus
(identidad material, magnitud, unidad, frontera, traza, retorno propio,
ausencia de doble cómputo).

ATENCIÓN
--------
Este código forma parte de la obra protegida intelectualmente bajo licencia
CC BY-NC-ND 4.0. Cualquier referencia académica debe citar la sede canónica
original con DOI cuando esté disponible. Uso no comercial y sin obras derivadas.

================================================================================
"""

from decimal import Decimal, getcontext

getcontext().prec = 50


# ==============================================================================
# COMPONENTES DEL INVENTARIO INICIAL B₀
# ==============================================================================

# ρ_A^SV — MATERIALIDAD ADMITIDA
# ------------------------------
# Entrada bariónica derivada del banco contemporáneo Planck Collaboration (2020)
# con Ω_b·h² = 0.0224 y H₀ = 67.4 km·s⁻¹·Mpc⁻¹.
# Estatuto: referencia material declarada, contraste externo bariónico.
RHO_BARIONES_PLANCK = Decimal("4.2E-28")  # kg/m³

# Término mínimo de neutrinos masivos en reposo bajo cota declarada
# Σm_ν ≲ 0.12 eV (combinación cosmológica + oscilaciones).
# Estatuto: materialidad no bariónica admitida con cota.
RHO_NEUTRINOS_MIN = Decimal("1.0E-29")  # kg/m³

# Materialidad admitida inicial total
RHO_A_B0 = RHO_BARIONES_PLANCK + RHO_NEUTRINOS_MIN


# ρ_U^SV — MATERIALIDAD CANDIDATA NO CLAUSURADA
# ---------------------------------------------
# Entradas físicamente plausibles cuyo cierre escalar el inventario inicial
# no autoriza; se conservan como U(causa; B) con causa declarada.
RHO_U_COMPONENTES = {
    "bariones_difusos": {
        "estatuto": "U(no clausurado; B₀)",
        "causa": "frontera observacional imprecisa en medio intergaláctico",
    },
    "gas_caliente_intergalactico": {
        "estatuto": "U(no clausurado; B₀)",
        "causa": "dependencia residual de modelo termodinámico",
    },
    "remanentes_compactos_no_identificados": {
        "estatuto": "U(no clausurado; B₀)",
        "causa": "control de doble cómputo con progenitores estelares",
    },
    "materialidad_baja_luminosidad": {
        "estatuto": "U(no clausurado; B₀)",
        "causa": "sin frontera operativa precisa",
    },
}


# ρ_E^SV — RETORNO ENERGÉTICO SEPARADO
# ------------------------------------
# Fondo cósmico de microondas y otros fondos radiativos.
# Estatuto: retorno energético, no materialidad. NO entra en ρ_ret^SV.
RHO_E_COMPONENTES = {
    "fondo_cosmico_microondas": {
        "T_caracteristica": Decimal("2.725"),  # K
        "estatuto": "ρ_E^SV; no materialidad",
        "criterio": "equivalencia masa-energía no altera naturaleza ontológica",
    },
    "fondos_radiativos_galacticos": {
        "estatuto": "ρ_E^SV; no materialidad",
        "criterio": "retorno radiativo distinto de masa retornada",
    },
}


# ρ_X^SV — EXCLUSIONES
# --------------------
# Magnitudes excluidas de materialidad por inferencia gravitatoria sin retorno
# material, doble cómputo, dependencia de modelo o sustancialización oscura.
RHO_X_COMPONENTES = {
    "rho_DM_contemporanea": {
        "estatuto": "ρ_X^SV; rechazado como materialidad",
        "criterio": "comparece solo como diferencia gravitatoria, sin retorno "
                    "material directo identificado",
    },
    "masas_por_lente": {
        "estatuto": "ρ_X^SV; rechazado como materialidad",
        "criterio": "mide efecto gravitatorio, no identidad material",
    },
    "masas_dinamicas_virial": {
        "estatuto": "ρ_X^SV; rechazado como materialidad",
        "criterio": "estimador gravitatorio dependiente de modelo dinámico",
    },
    "Omega_c_como_sustancia": {
        "estatuto": "ρ_X^SV; rechazado como materialidad",
        "criterio": "parámetro de modelo ΛCDM, no contenido material auditable",
    },
}


def construir_inventario_B0():
    """
    Construye la tupla canónica Ret_M^SV(Ω_T;B₀) con los cuatro componentes
    auditados según las restricciones canónicas del corpus.
    """
    return {
        "rho_A_SV": {
            "valor": RHO_A_B0,
            "unidades": "kg·m⁻³",
            "componentes": {
                "bariones_cosmologicos": RHO_BARIONES_PLANCK,
                "neutrinos_masivos_min": RHO_NEUTRINOS_MIN,
            },
            "estatuto": "materialidad admitida (escalar cerrado)",
        },
        "rho_U_SV": {
            "valor": "U(no clausurado; B₀)",
            "unidades": "kg·m⁻³ (rango no escalado)",
            "componentes": RHO_U_COMPONENTES,
            "estatuto": "materialidad candidata no clausurada",
        },
        "rho_E_SV": {
            "valor": "separado de ρ_ret^SV",
            "unidades": "no aplicable a materialidad",
            "componentes": RHO_E_COMPONENTES,
            "estatuto": "retorno energético separado",
        },
        "rho_X_SV": {
            "valor": "excluido de materialidad",
            "unidades": "no aplicable",
            "componentes": RHO_X_COMPONENTES,
            "estatuto": "exclusiones por restricción canónica",
        },
    }


def imprimir_inventario():
    """Imprime el inventario inicial completo con cuatro componentes."""
    inv = construir_inventario_B0()

    print("=" * 80)
    print("INVENTARIO INICIAL B₀ DE MATERIALIDAD RETORNADA")
    print("Ret_M^SV(Ω_T;B₀) = (ρ_A^SV, ρ_U^SV, ρ_E^SV, ρ_X^SV)")
    print("=" * 80)

    print("\n[ρ_A^SV] MATERIALIDAD ADMITIDA")
    print(f"    Bariones cosmológicos (Planck 2020): {RHO_BARIONES_PLANCK} kg·m⁻³")
    print(f"    Neutrinos masivos mínimos:           {RHO_NEUTRINOS_MIN} kg·m⁻³")
    print(f"    TOTAL ρ_A^SV(Ω_T;B₀) =               {RHO_A_B0} kg·m⁻³")
    print(f"    ≈ 4.3 × 10⁻²⁸ kg·m⁻³")

    print("\n[ρ_U^SV] MATERIALIDAD CANDIDATA NO CLAUSURADA")
    for nombre, datos in RHO_U_COMPONENTES.items():
        print(f"    {nombre}")
        print(f"        estatuto: {datos['estatuto']}")
        print(f"        causa   : {datos['causa']}")

    print("\n[ρ_E^SV] RETORNO ENERGÉTICO SEPARADO")
    for nombre, datos in RHO_E_COMPONENTES.items():
        print(f"    {nombre}")
        print(f"        estatuto: {datos['estatuto']}")
        print(f"        criterio: {datos['criterio']}")

    print("\n[ρ_X^SV] EXCLUSIONES POR RESTRICCIÓN CANÓNICA")
    for nombre, datos in RHO_X_COMPONENTES.items():
        print(f"    {nombre}")
        print(f"        estatuto: {datos['estatuto']}")
        print(f"        criterio: {datos['criterio']}")

    print("\n" + "=" * 80)
    print("OBSERVACIÓN DOCTRINAL:")
    print("La materialidad retornada se construye por admisión positiva")
    print("bajo restricciones canónicas, NUNCA por resta contra ρ_DM")
    print("contemporánea. La cifra de ρ_A^SV no es totalidad material del")
    print("dominio: es salida auditada inicial del banco conservador B₀,")
    print("escalable mediante refinamientos sucesivos en publicaciones")
    print("específicas del corpus.")
    print("=" * 80)


if __name__ == "__main__":
    imprimir_inventario()
