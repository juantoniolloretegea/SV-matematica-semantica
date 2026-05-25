# -*- coding: utf-8 -*-
"""
================================================================================
LABORATORIO 02 — CURVATURA CICLO-DISTANCIAL ESTRUCTURAL Λ_SV,puro
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

Sede canónica de Λ_SV,puro:
    Lloret Egea, J. A. (2026h). Teorema de resolución física de la constante
    cosmológica: transducción ciclo-distancial SV de Λ, energía oscura y
    expansión cosmológica. ITVIA — IA eñ — La Biblia de la IA.

PROPÓSITO
---------
Calcula y verifica la curvatura ciclo-distancial estructural pura del corpus,
Λ_SV,puro = 3 / (c² · T_obs²), magnitud canónica establecida en el Teorema de
resolución física de la constante cosmológica y precedente formal sobre el que
descansa la presente demostración para la materia oscura.

El cálculo es exacto: ningún parámetro se importa de la cosmología contemporánea;
todos los valores provienen del corpus del Sistema Vectorial SV.

ATENCIÓN
--------
Este código forma parte de la obra protegida intelectualmente bajo licencia
CC BY-NC-ND 4.0. Cualquier referencia académica debe citar la sede canónica
original con DOI cuando esté disponible. Uso no comercial y sin obras derivadas.

================================================================================
"""

from decimal import Decimal, getcontext
from lab_01_constantes_fundamentales_sv import T_OBS, C

getcontext().prec = 50


# ==============================================================================
# CÁLCULO DE LA CURVATURA CICLO-DISTANCIAL ESTRUCTURAL Λ_SV,puro
# ==============================================================================

def calcular_lambda_sv_puro():
    """
    Calcula Λ_SV,puro = 3 / (c² · T_obs²).

    Retorna:
        Decimal: valor en m⁻² con precisión decimal extendida.
    """
    return Decimal(3) / (C ** 2 * T_OBS ** 2)


LAMBDA_SV_PURO = calcular_lambda_sv_puro()


# Cifra canónica establecida en el corpus (Lloret Egea, 2026h):
#   Λ_SV,puro = 1.7600043527547774 × 10⁻⁵² m⁻²
LAMBDA_SV_PURO_CANONICA = Decimal("1.7600043527547774E-52")


def verificar_lambda_sv_puro():
    """
    Verifica que el cálculo coincide con la cifra canónica del corpus dentro de
    la precisión declarada. Comparación a 14 cifras significativas.
    """
    calculado = LAMBDA_SV_PURO
    canonico = LAMBDA_SV_PURO_CANONICA

    diferencia_relativa = abs((calculado - canonico) / canonico)
    tolerancia = Decimal("1E-14")

    coincide = diferencia_relativa < tolerancia

    return {
        "calculado": calculado,
        "canonico": canonico,
        "diferencia_relativa": diferencia_relativa,
        "tolerancia": tolerancia,
        "coincide": coincide,
    }


def imprimir_resultado():
    """Imprime el resultado del cálculo con verificación canónica."""
    print("=" * 80)
    print("Λ_SV,puro — CURVATURA CICLO-DISTANCIAL ESTRUCTURAL")
    print("=" * 80)
    print(f"\n  Fórmula:    Λ_SV,puro = 3 / (c² · T_obs²)")
    print(f"\n  Entradas canónicas del corpus:")
    print(f"      T_obs = {T_OBS} s")
    print(f"      c     = {C} m·s⁻¹")
    print(f"\n  Resultado calculado:")
    print(f"      Λ_SV,puro = {LAMBDA_SV_PURO:.20E} m⁻²")
    print(f"\n  Cifra canónica del corpus (Lloret Egea, 2026h):")
    print(f"      Λ_SV,puro = {LAMBDA_SV_PURO_CANONICA:.20E} m⁻²")
    print(f"\n  Verificación:")
    v = verificar_lambda_sv_puro()
    print(f"      diferencia relativa: {v['diferencia_relativa']:.2E}")
    print(f"      tolerancia exigida : {v['tolerancia']:.2E}")
    print(f"      coincide           : {v['coincide']}")
    print("\n" + "=" * 80)


if __name__ == "__main__":
    imprimir_resultado()
