# -*- coding: utf-8 -*-
"""
lab_05_configuracion_propia.py
==============================

Laboratorio canónico 05 — Interfaz de configuración propia del usuario

Permite a un tercero introducir su propia configuración (EM + TPA +
datos preternarios) y obtener el dictamen canónico de la fórmula
maestra 𝔉_SV sobre dicha configuración.

Este laboratorio es la pieza de uso operativo del aparato del SV V.1
más allá del banco canónico cerrado §17. Permite que un revisor
académico, físico computacional o equipo de trabajo aplique la fórmula
sobre configuraciones nuevas con trazabilidad completa al documento V14.

Trazabilidad canónica:
    - V14, Definición §K.7 (fórmula maestra unificada 𝔉_SV)
    - V14, §17.1 (notación canónica del banco)
    - Núcleo computacional: sv_core.py

Uso:
    1. Modo interactivo:
        python3 lab_05_configuracion_propia.py
    2. Modo programático:
        Importar evaluar_configuracion_usuario() y pasar parámetros.

Configuración requerida:
    - Sectores 1+2 (EM): D, B, Γ^E, Γ^H, ρ, V, A_Σ, ∂_ν^SV B, ∂_ν^SV D, J
    - Sector 3 (Grav): G(ν), 𝒢_J(ν), Q, E_crit, ‖J^(ν)_{Q,P}‖_∗
    - Sector 4 (TPA): φ = (φ(S_0), …, φ(S_n))
    - Sector 5: card(U_irr(T))
    - Datos preternarios opcionales: α_1(k), δ_1(k)
    - Dictamen 𝒮_4 opcional: m_0 ∈ ℕ ∪ {None} para U/χ_α
"""

from __future__ import annotations
from sv_core import (
    ConfiguracionEM, ConfiguracionGravitatoria, TrayectoriaTPA,
    evaluar_formula_completa, imprimir_cabecera,
)


# =====================================================================
# EJEMPLO DE CONFIGURACIÓN PROPIA — punto de partida para el usuario
# =====================================================================

def ejemplo_configuracion_admisible() -> dict:
    """Devuelve un ejemplo canónicamente admisible del que el usuario
    puede partir para construir su propia configuración."""

    return {
        "id": "Configuración-propia-ejemplo-A",
        "descripcion": "Configuración admisible de ejemplo (régimen estacionario)",
        "em": ConfiguracionEM(
            D=(0.10, 0.10, 0.10, 0.10),
            B=(0.05, 0.05, 0.05, 0.05),
            Gamma_E=(0.060, 0.060, 0.060, -0.180),
            Gamma_H=(0.100, 0.100, 0.100, -0.100),
            rho=0.000, V=1.000, A_Sigma=0.400,
            dnu_B=0.000, dnu_D=0.000,
            J=(0.125, 0.125, 0.125, 0.125),
        ),
        "grav": ConfiguracionGravitatoria(
            G_nu=0.0, G_J_nu=0.0, Q=0.0, E_crit=0.0, norma_J_QP=0.0
        ),
        "tpa": TrayectoriaTPA(phi=(2, 2, 2, 2)),
        "card_U_irr": 0,
        "dnu_rho": 0.0,
        "alpha": (0.5, 0.5, 0.5, 0.5),
        "delta": (0.0, 0.0, 0.0, 0.0),
        "m_0_dictamen": None,  # U sostenida (Adm_U activa: 0 < 2 < 9)
    }


def ejemplo_configuracion_violadora() -> dict:
    """Configuración que VIOLA canonicidad para demostrar que la
    fórmula DETECTA configuraciones inadmisibles."""

    return {
        "id": "Configuración-propia-ejemplo-B (viola Gauss eléctrico)",
        "descripcion": "Configuración con Gauss eléctrico violado (Div_SV(D) ≠ ρV)",
        "em": ConfiguracionEM(
            D=(0.30, 0.30, 0.30, 0.30),  # Div_SV(D) = 0
            B=(0.0, 0.0, 0.0, 0.0),
            Gamma_E=(0.0, 0.0, 0.0, 0.0),
            Gamma_H=(0.0, 0.0, 0.0, 0.0),
            rho=0.50, V=1.000, A_Sigma=0.400,  # ρV = 0.50 ≠ 0
            dnu_B=0.000, dnu_D=0.000,
            J=(0.0, 0.0, 0.0, 0.0),
        ),
        "grav": ConfiguracionGravitatoria(
            G_nu=0.0, G_J_nu=0.0, Q=0.0, E_crit=0.0, norma_J_QP=0.0
        ),
        "tpa": TrayectoriaTPA(phi=(2, 2, 2, 2)),
        "card_U_irr": 0,
        "dnu_rho": 0.0,
        "alpha": (0.5, 0.5, 0.5, 0.5),
        "delta": (0.0, 0.0, 0.0, 0.0),
        "m_0_dictamen": None,
    }


# =====================================================================
# EVALUACIÓN CANÓNICA DE UNA CONFIGURACIÓN PROPIA
# =====================================================================

def evaluar_configuracion_usuario(config: dict, tol: float = 1e-10) -> None:
    """Evalúa canónicamente la fórmula maestra 𝔉_SV sobre la
    configuración proporcionada por el usuario y emite dictamen
    canónico con trazabilidad completa."""

    print()
    print("─" * 71)
    print(f"CONFIGURACIÓN: {config['id']}")
    print(f"Descripción:   {config['descripcion']}")
    print("─" * 71)
    print()
    print("DATOS DECLARADOS POR EL USUARIO:")
    print(f"  Sector 1+2 (EM):")
    print(f"    D       = {config['em'].D}")
    print(f"    B       = {config['em'].B}")
    print(f"    Γ^E     = {config['em'].Gamma_E}")
    print(f"    Γ^H     = {config['em'].Gamma_H}")
    print(f"    ρ       = {config['em'].rho}")
    print(f"    V       = {config['em'].V}")
    print(f"    A_Σ     = {config['em'].A_Sigma}")
    print(f"    ∂_ν^SV B = {config['em'].dnu_B}")
    print(f"    ∂_ν^SV D = {config['em'].dnu_D}")
    print(f"    J       = {config['em'].J} (J_total = {config['em'].J_total})")
    print(f"  Sector 3 (Grav):")
    print(f"    G(ν)    = {config['grav'].G_nu}")
    print(f"    𝒢_J(ν)  = {config['grav'].G_J_nu}")
    print(f"    Q       = {config['grav'].Q}")
    print(f"    E_crit  = {config['grav'].E_crit}")
    print(f"  Sector 4 (TPA):")
    print(f"    φ       = {config['tpa'].phi}")
    print(f"    m       = {config['tpa'].m}")
    print(f"  Sector 5: card(U_irr) = {config['card_U_irr']}")
    print(f"  Datos preternarios:")
    print(f"    α_1(k)  = {config['alpha']}")
    print(f"    δ_1(k)  = {config['delta']}")
    print(f"  Dictamen 𝒮_4 declarado: m_0 = {config['m_0_dictamen']}")
    print()

    ev = evaluar_formula_completa(
        em=config["em"],
        grav=config["grav"],
        tpa=config["tpa"],
        card_U_irr=config["card_U_irr"],
        dnu_rho=config["dnu_rho"],
        alpha_serie=config["alpha"],
        delta_serie=config["delta"],
        m_0_dictamen=config["m_0_dictamen"],
        tol=tol,
    )

    print(ev)
    print()

    if ev.formula_se_anula:
        print("DICTAMEN CANÓNICO: configuración ADMISIBLE.")
        print("  La fórmula maestra 𝔉_SV se anula canónicamente sobre")
        print("  la configuración. Conforme al documento V14, esta")
        print("  configuración respeta los siete sectores primarios, las")
        print("  siete identidades intersectoriales, y la compuerta del")
        print("  morfismo dictamen ternario.")
    else:
        print("DICTAMEN CANÓNICO: configuración INADMISIBLE.")
        print("  La fórmula maestra 𝔉_SV NO se anula sobre la configuración.")
        print("  El aparato detecta una o más violaciones canónicas. Revise")
        print("  los componentes con valor distinto de cero en la salida")
        print("  anterior; cada uno corresponde a una identidad canónica")
        print("  del corpus que la configuración no satisface.")
    print()


# =====================================================================
# EJECUCIÓN PRINCIPAL
# =====================================================================

def ejecutar_lab() -> None:
    imprimir_cabecera(
        "Lab 05 — Configuración propia del usuario",
        "Aplicación canónica de 𝔉_SV (Definición §K.7) a configuraciones nuevas"
    )

    print("Este laboratorio aplica la fórmula maestra 𝔉_SV sobre")
    print("configuraciones canónicas DECLARADAS POR EL USUARIO, obteniendo")
    print("dictamen canónico de admisibilidad bajo el aparato del SV V.1.")
    print()
    print("Se demuestra con dos configuraciones de ejemplo:")
    print()
    print("EJEMPLO A — Configuración admisible canónicamente.")
    print("EJEMPLO B — Configuración violadora (Gauss eléctrico).")
    print()
    print("═" * 71)

    print("\n┃ EJEMPLO A ┃")
    config_A = ejemplo_configuracion_admisible()
    evaluar_configuracion_usuario(config_A)

    print("═" * 71)

    print("\n┃ EJEMPLO B ┃")
    config_B = ejemplo_configuracion_violadora()
    evaluar_configuracion_usuario(config_B)

    print("═" * 71)
    print()
    print("USO PROGRAMÁTICO:")
    print()
    print("  Para evaluar tu propia configuración, importa este módulo")
    print("  y construye un diccionario con la misma estructura que")
    print("  ejemplo_configuracion_admisible(). Llama después a")
    print("  evaluar_configuracion_usuario(tu_configuracion).")
    print()
    print("  Ejemplo:")
    print()
    print("    from lab_05_configuracion_propia import evaluar_configuracion_usuario")
    print("    from sv_core import ConfiguracionEM, ConfiguracionGravitatoria, TrayectoriaTPA")
    print()
    print("    mi_config = {")
    print("        'id': 'Mi configuración',")
    print("        'descripcion': 'Régimen experimental propio',")
    print("        'em': ConfiguracionEM(...),")
    print("        'grav': ConfiguracionGravitatoria(...),")
    print("        'tpa': TrayectoriaTPA(phi=(...)),")
    print("        'card_U_irr': 0,")
    print("        'dnu_rho': 0.0,")
    print("        'alpha': (...),")
    print("        'delta': (...),")
    print("        'm_0_dictamen': None,  # o un m_0 si Adm_0/Adm_1 aplica")
    print("    }")
    print("    evaluar_configuracion_usuario(mi_config)")
    print()
    print("═" * 71)


if __name__ == "__main__":
    ejecutar_lab()
