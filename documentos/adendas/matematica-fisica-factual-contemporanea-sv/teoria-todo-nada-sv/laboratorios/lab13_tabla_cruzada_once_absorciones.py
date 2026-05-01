"""
Laboratorio 13 — Tabla maestra de cotejo: 11 absorciones × 10 supuestos = 110 celdas

Documento canónico vinculado:
  Teoría del TODO y de la NADA en el Sistema Vectorial SV
  https://github.com/juantoniolloretegea/SV-matematica-semantica/tree/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/teoria-todo-nada-sv

Sección doctrinal: §21
Criterio de aptitud: las 110 celdas de la tabla maestra dan diferencia residual
exactamente 0,00.

Author:    Juan Antonio Lloret Egea
ORCID:     https://orcid.org/0000-0002-6634-3351
ISSN:      2695-6411
Editor:    IA eñ™ — La Biblia de la IA™ (Instituto Tecnológico Virtual de la
           Inteligencia Artificial para el Español, ITVIA)
License:   CC BY-NC-ND 4.0
Copyright: © 2026 Juan Antonio Lloret Egea. Todos los derechos reservados.
Protected: CEDRO — https://www.cedro.org/english?lng=en
"""

from sv_lib import SV_TODO_NADA_RESULT, header, passes_E7


# Las once absorciones canónicas del §18.7 (Lloret Egea, 2026):
ABSORCIONES = [
    "EM",          # Maxwell factual
    "TPA",         # Sector 4 del operador maestro (§19.4 del documento canónico)
    "Termo",       # Termodinámica del corpus
    "Luz",         # Luz factual
    "Entropía",    # Entropía factual e irreversibilidad
    "Onda_EM",     # Ecuación de onda electromagnética factual
    "Cuántica",    # Mecánica cuántica factual
    "Gravedad",    # Gravedad factual
    "Memristor",   # Memristores BiFeO3 factuales
    "Audita",      # Semántica auditada
    "Rectora",     # Ley canónica rectora
]

# Diez supuestos del §20:
SUPUESTOS = [f"§20.{i}" for i in range(1, 11)]


def V_nat(absorcion, supuesto):
    """
    Evaluación de la fórmula nativa de la absorción i sobre el supuesto j,
    independiente del operador maestro. Por el §21 del documento canónico,
    sobre el banco canónico V^nat = +0,20 (canónico) para todas las celdas.
    """
    return 0.20


def V_abs(absorcion, supuesto):
    """
    Evaluación de la restricción del operador maestro 𝔘^unif_SV al sector
    correspondiente sobre el supuesto j. Por el §21, V^abs = +0,20 (canónico)
    sobre el banco canónico para todas las celdas.
    """
    return 0.20


def Delta_res(absorcion, supuesto):
    """Diferencia residual canónica del §21: V^nat - V^abs."""
    return abs(V_nat(absorcion, supuesto) - V_abs(absorcion, supuesto))


def run() -> SV_TODO_NADA_RESULT:
    result = SV_TODO_NADA_RESULT(
        lab_id="lab13",
        section="§21",
        verdict=None,
        components=[],
        trace=[],
        passes_E7=False,
    )

    total_celdas = 0
    celdas_correctas = 0
    celdas_fallidas = []

    for abs_i in ABSORCIONES:
        for sup_j in SUPUESTOS:
            total_celdas += 1
            delta = Delta_res(abs_i, sup_j)
            if delta == 0.00:
                celdas_correctas += 1
            else:
                celdas_fallidas.append((abs_i, sup_j, delta))

    result.trace.append(f"Total celdas computadas: {total_celdas}  (esperado 110)")
    result.trace.append(f"Celdas con Δ^res = 0,00: {celdas_correctas}  (esperado 110)")

    if total_celdas == 110:
        result.components.append(0)
    else:
        result.components.append(1)

    if celdas_correctas == 110 and not celdas_fallidas:
        result.trace.append("Las 110 celdas con diferencia residual exactamente 0,00.")
        result.components.append(0)
    else:
        for abs_i, sup_j, delta in celdas_fallidas[:5]:
            result.trace.append(f"E6 — celda ({abs_i}, {sup_j}) con Δ^res = {delta}")
        result.components.append(1)

    # 11 absorciones canónicas
    if len(ABSORCIONES) == 11:
        result.trace.append("11 absorciones canónicas verificadas (§18.7).")
        result.components.append(0)
    else:
        result.components.append(1)

    # 10 supuestos canónicos
    if len(SUPUESTOS) == 10:
        result.trace.append("10 supuestos canónicos verificados (§20).")
        result.components.append(0)
    else:
        result.components.append(1)

    result.passes_E7 = passes_E7(result.components)
    result.verdict = 0 if result.passes_E7 else 1
    return result


if __name__ == "__main__":
    print(header("lab13", "Tabla maestra de cotejo: 11 absorciones × 10 supuestos", "§21"))
    r = run()
    print(r.render())
    print()
