# -*- coding: utf-8 -*-
"""
================================================================================
LABORATORIO 01 — CONSTANTES FUNDAMENTALES DEL SISTEMA VECTORIAL SV
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

Sedes canónicas del corpus relevantes:
    Lloret Egea, J. A. (2026c). Primitivos metrológicos del Sistema Vectorial SV.
        https://doi.org/10.21428/39829d0b.c8ec692e
    Lloret Egea, J. A. (2026i). Edades relativas del universo observable.

PROPÓSITO
---------
Fija las constantes fundamentales canónicas del Sistema Vectorial SV con
precisión auditable y declara su estatuto metrológico (primitivo, transductor,
constante de contraste). Sirve como módulo común importado por el resto de
laboratorios de la suite.

ATENCIÓN
--------
Este código forma parte de la obra protegida intelectualmente bajo licencia
CC BY-NC-ND 4.0. Cualquier referencia académica debe citar la sede canónica
original con DOI cuando esté disponible. Uso no comercial y sin obras derivadas.

================================================================================
"""

from decimal import Decimal, getcontext

# Precisión decimal alta para cálculos auditables
getcontext().prec = 50


# ==============================================================================
# CONSTANTES CANÓNICAS DEL CORPUS DEL SISTEMA VECTORIAL SV
# ==============================================================================

# Régimen de retorno ciclo-distancial del dominio observable (parámetro
# estructural canónico del corpus, no tiempo soberano transcurrido).
# Sede: Lloret Egea (2026i), Edades relativas del universo observable.
T_OBS = Decimal("4.354948800E17")  # segundos
T_OBS_ANIOS_JULIANOS = Decimal("13.800E9")  # años julianos equivalentes

# Velocidad de la luz en el vacío.
# Estatuto: constante SI exacta absorbida como primitivo del Sistema Vectorial.
# Sede: Lloret Egea (2026c), Primitivos metrológicos del SV.
C = Decimal("299792458")  # metros por segundo

# Constante de gravitación universal.
# Estatuto: constante de contraste con absorción parcial declarada; opera como
# conversor metrológico de retorno hacia unidades másicas del Sistema
# Internacional, no como fundamento sustancial del cálculo.
G = Decimal("6.67430E-11")  # metros cúbicos por kilogramo por segundo cuadrado

# Constante pi con precisión decimal extendida.
PI = Decimal("3.14159265358979323846264338327950288419716939937510")


# ==============================================================================
# IDENTIFICACIÓN OPERATIVA DE LAS CONSTANTES
# ==============================================================================

CONSTANTES = {
    "T_obs": {
        "valor": T_OBS,
        "unidades": "s",
        "estatuto": "régimen estructural canónico del corpus",
        "sede": "Lloret Egea (2026i)",
        "equivalente": f"{T_OBS_ANIOS_JULIANOS} años julianos",
    },
    "c": {
        "valor": C,
        "unidades": "m·s⁻¹",
        "estatuto": "constante SI exacta absorbida como primitivo SV",
        "sede": "Lloret Egea (2026c)",
        "equivalente": None,
    },
    "G": {
        "valor": G,
        "unidades": "m³·kg⁻¹·s⁻²",
        "estatuto": "transductor metrológico con absorción parcial declarada",
        "sede": "Lloret Egea (2026c)",
        "equivalente": None,
    },
}


def imprimir_tabla_constantes():
    """
    Imprime las constantes fundamentales del corpus con su estatuto metrológico
    declarado, conforme a la disciplina de no interiorización.
    """
    print("=" * 80)
    print("CONSTANTES FUNDAMENTALES — SISTEMA VECTORIAL SV")
    print("=" * 80)
    for nombre, datos in CONSTANTES.items():
        print(f"\n  {nombre}")
        print(f"      valor      : {datos['valor']} {datos['unidades']}")
        print(f"      estatuto   : {datos['estatuto']}")
        print(f"      sede       : {datos['sede']}")
        if datos['equivalente']:
            print(f"      equivalente: {datos['equivalente']}")
    print("\n" + "=" * 80)


if __name__ == "__main__":
    imprimir_tabla_constantes()
