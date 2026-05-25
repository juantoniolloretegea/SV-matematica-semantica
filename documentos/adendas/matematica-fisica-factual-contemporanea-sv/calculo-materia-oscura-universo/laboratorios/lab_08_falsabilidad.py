# -*- coding: utf-8 -*-
"""
================================================================================
LABORATORIO 08 — TEST DE FALSABILIDAD DE LA IDENTIDAD NULA SUSTANCIAL
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

Instalaciones experimentales de búsqueda directa e indirecta:
    LUX-ZEPLIN:    https://lz.lbl.gov/
    XENONnT:       https://xenonexperiment.org/
    PandaX-4T:     https://pandax.sjtu.edu.cn/
    Fermi-LAT:     https://fermi.gsfc.nasa.gov/
    IceCube:       https://icecube.wisc.edu/
    AMS-02:        https://ams02.space/

PROPÓSITO
---------
Implementa el test de falsabilidad de la identidad ρ_DM,sustancia^SV = 0:
simula una detección hipotética de partícula oscura material y verifica que la
tesis del trabajo CAE en el ámbito cubierto por esa detección, demostrando que
el resultado no se inmuniza contra evidencia experimental futura.

La identidad nula es exacta y formal, pero es falsable en sentido estricto: si
se produjera identificación material directa de una sustancia oscura con
propiedades másicas reproducibles, interacción confirmada experimentalmente
en distintas instalaciones, independencia respecto a inferencias gravitatorias
previas y capacidad cuantitativa suficiente, la tesis quedaría refutada.

ATENCIÓN
--------
Este código forma parte de la obra protegida intelectualmente bajo licencia
CC BY-NC-ND 4.0. Cualquier referencia académica debe citar la sede canónica
original con DOI cuando esté disponible. Uso no comercial y sin obras derivadas.

================================================================================
"""

from lab_06_identidad_nula import evaluar_admision_material, CANDIDATOS


# ==============================================================================
# CRITERIOS DE FALSABILIDAD DE LA IDENTIDAD NULA
# ==============================================================================
# Estos cuatro criterios son condiciones simultáneas: la identidad nula se
# refuta si y solo si todos se cumplen para una sustancia oscura específica.

CRITERIOS_REFUTACION = {
    "propiedades_masicas_reproducibles": {
        "descripcion": "Masa en reposo determinada con precisión y reproducible.",
        "verificacion": "Coincidencia entre experimentos independientes con "
                        "incertidumbre acotada.",
    },
    "interaccion_confirmada_multiples_instalaciones": {
        "descripcion": "Detección confirmada en distintas instalaciones "
                       "experimentales independientes.",
        "verificacion": "No atribución única a artefacto experimental ni a "
                        "calibración de una sola instalación.",
    },
    "independencia_respecto_a_inferencia_gravitatoria": {
        "descripcion": "Identificación material directa, no por balance "
                       "gravitatorio.",
        "verificacion": "Detección por interacción con materia ordinaria, "
                        "no por reconstrucción de potencial.",
    },
    "capacidad_cuantitativa_suficiente": {
        "descripcion": "Capacidad de explicar el componente cosmológico "
                       "atribuido a materia oscura.",
        "verificacion": "Densidad cosmológica de la sustancia detectada "
                        "compatible con Ω_c contemporánea bajo cierre "
                        "experimental.",
    },
}


# ==============================================================================
# SIMULACIONES DE ESCENARIOS HIPOTÉTICOS
# ==============================================================================

ESCENARIOS_HIPOTETICOS = {
    "estado_actual_2026": {
        "descripcion": "Estado a la fecha del trabajo (25 mayo 2026): "
                       "búsquedas acumuladas en LZ, XENONnT, PandaX-4T, "
                       "Fermi-LAT, IceCube, AMS-02 sin identificación positiva.",
        "propiedades_masicas_reproducibles": False,
        "interaccion_confirmada_multiples_instalaciones": False,
        "independencia_respecto_a_inferencia_gravitatoria": False,
        "capacidad_cuantitativa_suficiente": False,
    },
    "deteccion_aislada_no_confirmada": {
        "descripcion": "Hipotética detección en una sola instalación sin "
                       "confirmación independiente.",
        "propiedades_masicas_reproducibles": False,
        "interaccion_confirmada_multiples_instalaciones": False,
        "independencia_respecto_a_inferencia_gravitatoria": True,
        "capacidad_cuantitativa_suficiente": None,
    },
    "deteccion_confirmada_parcial": {
        "descripcion": "Hipotética detección reproducible en varias "
                       "instalaciones pero con densidad cosmológica "
                       "insuficiente para explicar Ω_c.",
        "propiedades_masicas_reproducibles": True,
        "interaccion_confirmada_multiples_instalaciones": True,
        "independencia_respecto_a_inferencia_gravitatoria": True,
        "capacidad_cuantitativa_suficiente": False,
    },
    "deteccion_refutadora_completa": {
        "descripcion": "Hipotética detección que cumple los cuatro criterios "
                       "simultáneamente: refutación efectiva de la identidad "
                       "nula sustancial.",
        "propiedades_masicas_reproducibles": True,
        "interaccion_confirmada_multiples_instalaciones": True,
        "independencia_respecto_a_inferencia_gravitatoria": True,
        "capacidad_cuantitativa_suficiente": True,
    },
}


def evaluar_escenario(escenario):
    """
    Evalúa si un escenario hipotético refuta la identidad nula sustancial.

    Argumentos:
        escenario (dict): contiene la descripción y los cuatro criterios con
            valores True/False/None.

    Retorna:
        tuple: (refuta, cumplidos, indeterminados, no_cumplidos)
    """
    cumplidos = []
    no_cumplidos = []
    indeterminados = []

    for criterio in CRITERIOS_REFUTACION.keys():
        valor = escenario.get(criterio)
        if valor is True:
            cumplidos.append(criterio)
        elif valor is False:
            no_cumplidos.append(criterio)
        else:
            indeterminados.append(criterio)

    # Refutación efectiva: los cuatro criterios deben cumplirse
    refuta = len(cumplidos) == 4 and len(no_cumplidos) == 0 and len(indeterminados) == 0

    return refuta, cumplidos, indeterminados, no_cumplidos


def aplicar_a_inventario_si_detectado(escenario):
    """
    Si un escenario refuta la identidad nula, simula cómo cambiaría la
    admisión local μ_i^M de la sustancia oscura: de μ_i^M = 0 (excluida) a
    μ_i^M = 1 (admitida en ρ_A^SV) en el ámbito cubierto por la detección.
    """
    refuta, _, _, _ = evaluar_escenario(escenario)

    if refuta:
        # Atributos canónicos que la sustancia detectada satisfaría
        sustancia_detectada = {
            "identidad material": True,
            "magnitud": True,
            "unidad": True,
            "frontera operativa": True,
            "traza identificable": True,
            "retorno material propio": True,
            "ausencia de doble cómputo": True,
        }
        mu, justificacion = evaluar_admision_material(sustancia_detectada)
        return {
            "mu_i_M_actualizado": mu,
            "justificacion": justificacion,
            "consecuencia": "La identidad ρ_DM,sustancia^SV = 0 quedaría "
                            "refutada en el ámbito cubierto por la detección.",
        }
    else:
        return {
            "mu_i_M_actualizado": 0,
            "justificacion": "La materia oscura ΛCDM mantiene exclusión "
                             "canónica del inventario.",
            "consecuencia": "La identidad ρ_DM,sustancia^SV = 0 se sostiene.",
        }


# ==============================================================================
# EJECUCIÓN
# ==============================================================================

def imprimir_test_falsabilidad():
    """Imprime la evaluación de los escenarios hipotéticos."""
    print("=" * 80)
    print("TEST DE FALSABILIDAD DE LA IDENTIDAD NULA SUSTANCIAL")
    print("=" * 80)

    print("\nCriterios de refutación (condiciones simultáneas):")
    for i, (criterio, datos) in enumerate(CRITERIOS_REFUTACION.items(), 1):
        print(f"\n  {i}. {criterio}")
        print(f"     {datos['descripcion']}")
        print(f"     Verificación: {datos['verificacion']}")

    print("\n" + "=" * 80)
    print("EVALUACIÓN DE ESCENARIOS HIPOTÉTICOS")
    print("=" * 80)

    for nombre, escenario in ESCENARIOS_HIPOTETICOS.items():
        refuta, cumplidos, indeterminados, no_cumplidos = evaluar_escenario(escenario)
        consecuencia = aplicar_a_inventario_si_detectado(escenario)

        print(f"\n>> ESCENARIO: {nombre}")
        print(f"   {escenario['descripcion']}")
        print(f"   Criterios cumplidos     : {len(cumplidos)}/4")
        print(f"   Criterios no cumplidos  : {len(no_cumplidos)}/4")
        print(f"   Criterios indeterminados: {len(indeterminados)}/4")
        veredicto = "REFUTACIÓN EFECTIVA" if refuta else "TESIS SE SOSTIENE"
        print(f"   Veredicto               : {veredicto}")
        print(f"   Consecuencia            : {consecuencia['consecuencia']}")

    print("\n" + "=" * 80)
    print("LECTURA DOCTRINAL DEL TEST")
    print("=" * 80)
    print("""
  La identidad ρ_DM,sustancia^SV = 0 es exacta y formal, pero es FALSABLE en
  sentido estricto. El laboratorio demuestra computacionalmente que:

    1. A la fecha del trabajo, ningún experimento ha producido detección que
       satisfaga los cuatro criterios simultáneamente.

    2. Una hipotética detección aislada no refutaría la tesis (insuficiente).

    3. Una hipotética detección confirmada pero con capacidad cuantitativa
       insuficiente para explicar Ω_c tampoco refutaría la tesis en su
       totalidad (refutación parcial circunscrita al ámbito detectado).

    4. Una hipotética detección que cumpla los cuatro criterios refutaría
       efectivamente la identidad en el ámbito cubierto.

  La tesis NO se inmuniza contra evidencia experimental futura. Se compromete
  con una afirmación exacta sometida a contraste empírico. Esta falsabilidad
  es propiedad estructural del aparato, no concesión retórica.
""")
    print("=" * 80)


if __name__ == "__main__":
    imprimir_test_falsabilidad()
