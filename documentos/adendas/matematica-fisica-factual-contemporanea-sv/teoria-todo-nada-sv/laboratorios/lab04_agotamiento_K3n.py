"""
Laboratorio 04 — Agotamiento configuracional Im(v) = K₃ⁿ

Documento canónico vinculado:
  Teoría del TODO y de la NADA en el Sistema Vectorial SV
  https://github.com/juantoniolloretegea/SV-matematica-semantica/tree/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/teoria-todo-nada-sv

Sección doctrinal: §9
Criterio de aptitud: diferencia simétrica vacía entre imagen acumulada y
codominio K₃². 𝓐_q = ζ_SV(|∅|) = 0.

Author:    Juan Antonio Lloret Egea
ORCID:     https://orcid.org/0000-0002-6634-3351
ISSN:      2695-6411
Editor:    IA eñ™ — La Biblia de la IA™ (Instituto Tecnológico Virtual de la
           Inteligencia Artificial para el Español, ITVIA)
License:   CC BY-NC-ND 4.0
Copyright: © 2026 Juan Antonio Lloret Egea. Todos los derechos reservados.
Protected: CEDRO — https://www.cedro.org/english?lng=en
"""

from itertools import product
from sv_lib import SIGMA, SV_TODO_NADA_RESULT, header, zeta_SV, passes_E7


def run() -> SV_TODO_NADA_RESULT:
    result = SV_TODO_NADA_RESULT(
        lab_id="lab04",
        section="§9",
        verdict=None,
        components=[],
        trace=[],
        passes_E7=False,
    )

    # Codominio K₃² = Σ²: nueve configuraciones canónicas del ejemplo 9.4.
    K3_2 = set(product(SIGMA, repeat=2))
    if len(K3_2) != 9:
        result.trace.append(f"E6 — |K₃²| = {len(K3_2)} ≠ 9 (esperado 3²).")
        result.components.append(1)
    else:
        result.trace.append(f"|K₃²| = 9 verificado.")
        result.components.append(0)

    # Trayectoria canónica de longitud 9 sobre K₃² del ejemplo 9.4 que recorre
    # exactamente todas las configuraciones del codominio (agotamiento).
    trayectoria = [
        (0, 0), (0, 1), (0, 'U'),
        (1, 0), (1, 1), (1, 'U'),
        ('U', 0), ('U', 1), ('U', 'U'),
    ]

    # Imagen acumulada
    Im_v = set(trayectoria)

    # Diferencia simétrica entre imagen acumulada y codominio
    diff_sim = Im_v.symmetric_difference(K3_2)
    result.trace.append(f"Im(v) ∩ K₃² = {len(Im_v & K3_2)} / 9 configuraciones.")
    result.trace.append(f"Diferencia simétrica = {diff_sim}")

    if diff_sim == set():
        result.trace.append("Im(v) = K₃² verificado: agotamiento configuracional.")
        result.components.append(0)
    else:
        result.trace.append("E6 — Im(v) ≠ K₃² (diferencia simétrica no vacía).")
        result.components.append(1)

    # 𝓐_q = ζ_SV(|diferencia simétrica|) = ζ_SV(0) = 0
    A_q = zeta_SV(len(diff_sim))
    result.trace.append(f"𝓐_q = ζ_SV(|{diff_sim}|) = ζ_SV({len(diff_sim)}) = {A_q}")
    result.components.append(A_q)

    result.passes_E7 = passes_E7(result.components)
    result.verdict = 0 if result.passes_E7 else 1
    return result


if __name__ == "__main__":
    print(header("lab04", "Agotamiento configuracional Im(v) = K₃ⁿ", "§9"))
    r = run()
    print(r.render())
    print()
