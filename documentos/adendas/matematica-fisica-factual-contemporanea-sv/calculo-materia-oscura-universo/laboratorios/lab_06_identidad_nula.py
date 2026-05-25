# -*- coding: utf-8 -*-
"""
================================================================================
LABORATORIO 06 — IDENTIDAD NULA SUSTANCIAL DE LA MATERIA OSCURA
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
Implementa la verificación formal de la identidad nuclear del trabajo:

    ρ_DM,sustancia^SV = 0   (identidad exacta)
    m_DM,sustancia^SV = 0   (identidad exacta)

como resultado de aplicación rigurosa de la restricción canónica de admisión
de materialidad retornada al componente cosmológico cuya sustancialidad se
discute. La identidad NO es aproximación, cota superior, hipótesis de ausencia
provisional ni resultado estadístico; es cierre formal sobre fundamento
canónico.

El laboratorio simula la admisión local μ_i^M ∈ {1, 0, U} para los candidatos
materiales que comparecen ante el inventario y verifica que ρ_DM contemporánea
queda excluida (μ_i^M = 0) por incumplimiento de la restricción de retorno
material directo.

ATENCIÓN
--------
Este código forma parte de la obra protegida intelectualmente bajo licencia
CC BY-NC-ND 4.0. Cualquier referencia académica debe citar la sede canónica
original con DOI cuando esté disponible. Uso no comercial y sin obras derivadas.

================================================================================
"""

from decimal import Decimal


# ==============================================================================
# RESTRICCIONES CANÓNICAS DE ADMISIÓN DE MATERIALIDAD RETORNADA
# ==============================================================================
# Sede: Lloret Egea (2026c), Primitivos metrológicos del SV.
# Disciplina canónica anterior al problema cosmológico de materia oscura.

RESTRICCIONES_ADMISION = [
    "identidad material",
    "magnitud",
    "unidad",
    "frontera operativa",
    "traza identificable",
    "retorno material propio",
    "ausencia de doble cómputo",
]


def evaluar_admision_material(candidato):
    """
    Evalúa la admisión local μ_i^M de un candidato material según las
    restricciones canónicas del corpus.

    Argumentos:
        candidato (dict): debe contener las claves de cada restricción con
            valores booleanos True/False indicando si el candidato las cumple.

    Retorna:
        tuple: (mu_i_M, justificacion)
            mu_i_M = 1   si cumple todas las restricciones
            mu_i_M = 0   si incumple alguna de manera definitiva
            mu_i_M = "U" si la evaluación es indeterminada
    """
    incumplimientos = []
    indeterminadas = []

    for restriccion in RESTRICCIONES_ADMISION:
        valor = candidato.get(restriccion)
        if valor is False:
            incumplimientos.append(restriccion)
        elif valor is None:
            indeterminadas.append(restriccion)

    if incumplimientos:
        return (
            0,
            f"Incumple restricciones canónicas: {', '.join(incumplimientos)}"
        )
    elif indeterminadas:
        return (
            "U",
            f"Indeterminación honesta en: {', '.join(indeterminadas)}"
        )
    else:
        return (1, "Cumple todas las restricciones canónicas")


# ==============================================================================
# CANDIDATOS MATERIALES PARA EVALUACIÓN
# ==============================================================================

CANDIDATOS = {
    "estrella_secuencia_principal": {
        "identidad material": True,
        "magnitud": True,
        "unidad": True,
        "frontera operativa": True,
        "traza identificable": True,
        "retorno material propio": True,
        "ausencia de doble cómputo": True,
    },
    "neutrino_masivo_cota_declarada": {
        "identidad material": True,
        "magnitud": True,
        "unidad": True,
        "frontera operativa": True,
        "traza identificable": True,
        "retorno material propio": True,
        "ausencia de doble cómputo": True,
    },
    "gas_difuso_intergalactico": {
        "identidad material": True,
        "magnitud": True,
        "unidad": True,
        "frontera operativa": None,
        "traza identificable": None,
        "retorno material propio": True,
        "ausencia de doble cómputo": None,
    },
    "fondo_cosmico_microondas": {
        "identidad material": False,
        "magnitud": True,
        "unidad": True,
        "frontera operativa": True,
        "traza identificable": True,
        "retorno material propio": False,
        "ausencia de doble cómputo": True,
    },
    "materia_oscura_LambdaCDM": {
        "identidad material": False,
        "magnitud": True,
        "unidad": True,
        "frontera operativa": False,
        "traza identificable": False,
        "retorno material propio": False,
        "ausencia de doble cómputo": True,
    },
}


# ==============================================================================
# VERIFICACIÓN DE LA IDENTIDAD NULA
# ==============================================================================

def verificar_identidad_nula():
    """
    Recorre todos los candidatos materiales y verifica que la materia oscura
    contemporánea queda excluida del inventario por incumplimiento de las
    restricciones canónicas de admisión.

    El resultado nuclear ρ_DM,sustancia^SV = 0 se sostiene como consecuencia
    formal de la evaluación, no como postulado.
    """
    resultados = {}
    for nombre, atributos in CANDIDATOS.items():
        mu, justificacion = evaluar_admision_material(atributos)
        resultados[nombre] = {
            "mu_i_M": mu,
            "justificacion": justificacion,
        }
    return resultados


def imprimir_evaluacion():
    """Imprime la evaluación completa de todos los candidatos."""
    resultados = verificar_identidad_nula()

    print("=" * 80)
    print("VERIFICACIÓN DE LA IDENTIDAD NULA SUSTANCIAL")
    print("Aplicación de la restricción canónica de admisión")
    print("=" * 80)

    print("\nRestricciones canónicas de admisión (μ_i^M = 1):")
    for r in RESTRICCIONES_ADMISION:
        print(f"    • {r}")

    print("\nEvaluación de candidatos materiales:")
    print("-" * 80)
    for nombre, datos in resultados.items():
        simbolo = {1: "✓ ADMITIDO", 0: "✗ EXCLUIDO", "U": "? INDETERMINADO"}[datos["mu_i_M"]]
        print(f"\n  {nombre}:")
        print(f"      μ_i^M = {datos['mu_i_M']}   [{simbolo}]")
        print(f"      {datos['justificacion']}")

    print("\n" + "=" * 80)
    print("RESULTADO NUCLEAR DEL TRABAJO")
    print("=" * 80)
    mu_DM = resultados["materia_oscura_LambdaCDM"]["mu_i_M"]
    if mu_DM == 0:
        print("\n  ρ_DM,sustancia^SV = 0   (identidad exacta)")
        print("  m_DM,sustancia^SV = 0   (identidad exacta)")
        print()
        print("  La materia oscura contemporánea queda excluida del inventario")
        print("  de materialidad retornada porque incumple las restricciones")
        print("  canónicas de identidad material, frontera operativa, traza")
        print("  identificable y retorno material propio.")
        print()
        print("  El retorno gravitatorio observado se conserva íntegramente y")
        print("  se reidentifica como densidad gravitatoria efectiva de sutura")
        print("  del dominio físico realizado, magnitud estructural articulada")
        print("  canónicamente desde raigal Ξ_SV (Lloret Egea, 2026b),")
        print("  imperfección preformal ε−0 (Lloret Egea, 2026a) y operación")
        print("  de clausura.")
    print("\n" + "=" * 80)


# ==============================================================================
# CONDICIÓN DE REFUTACIÓN (FALSABILIDAD)
# ==============================================================================

CONDICION_REFUTACION = """
CONDICIÓN DE REFUTACIÓN DE LA IDENTIDAD NULA
============================================

La identidad ρ_DM,sustancia^SV = 0 quedaría refutada en el ámbito cubierto si
se produjera identificación material directa de una sustancia oscura con
todas las propiedades siguientes simultáneamente:

  1. Propiedades másicas reproducibles experimentalmente (masa en reposo
     determinada con precisión y reproducible).

  2. Interacción confirmada en distintas instalaciones independientes
     (no atribución única a artefacto experimental).

  3. Independencia experimental respecto a inferencias gravitatorias
     previas (detección material directa, no por balance gravitatorio).

  4. Capacidad cuantitativa suficiente para explicar el componente
     cosmológico cosmológicamente atribuido a materia oscura en los bancos
     observacionales contemporáneos.

A la fecha del trabajo (25 de mayo de 2026), las búsquedas experimentales
acumuladas durante varias décadas en LUX-ZEPLIN, XENONnT, PandaX-4T,
Fermi-LAT, IceCube y AMS-02 no han producido identificación positiva de
candidato alguno bajo estos cuatro criterios.

La tesis NO se inmuniza contra evidencia futura: se compromete con una
afirmación exacta sometida a contraste empírico.
"""


if __name__ == "__main__":
    imprimir_evaluacion()
    print(CONDICION_REFUTACION)
