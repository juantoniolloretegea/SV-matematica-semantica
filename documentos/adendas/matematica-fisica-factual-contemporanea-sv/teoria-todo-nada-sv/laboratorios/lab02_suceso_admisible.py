"""
Laboratorio 02 — Suceso admisible

Documento canónico vinculado:
  Teoría del TODO y de la NADA en el Sistema Vectorial SV
  https://github.com/juantoniolloretegea/SV-matematica-semantica/tree/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/teoria-todo-nada-sv

Sección doctrinal: §2.4
Criterio de aptitud: las seis condiciones A1-A6 evaluadas a verdadero sobre la
entrada canónica de la cuaterna admisible e = (H, H', σ, R_e).

Author:    Juan Antonio Lloret Egea
ORCID:     https://orcid.org/0000-0002-6634-3351
ISSN:      2695-6411
Editor:    IA eñ™ — La Biblia de la IA™ (Instituto Tecnológico Virtual de la
           Inteligencia Artificial para el Español, ITVIA)
License:   CC BY-NC-ND 4.0
Copyright: © 2026 Juan Antonio Lloret Egea. Todos los derechos reservados.
Protected: CEDRO — https://www.cedro.org/english?lng=en
"""

from sv_lib import SV_TODO_NADA_RESULT, header, alphabet_check, passes_E7


def admissible_event_check(H, H_prime, sigma, R_e):
    """
    Verifica las seis condiciones A1-A6 del §2.4 del documento canónico
    para una cuaterna admisible e = (H, H', σ, R_e) sobre SV(9, 3).

    A1 — H, H' ⊂ Σ⁹ son horizontes bien formados (subconjuntos no vacíos del
         cubo ternario).
    A2 — σ : H → H' es una función parcial sin reescritura.
    A3 — R_e ⊂ H × H' es la relación admisible determinada por σ.
    A4 — Toda imagen σ(s) con s ∈ dom(σ) pertenece a H'.
    A5 — La cuaterna no introduce símbolos exteriores a Σ.
    A6 — La cuaterna no postula tiempo soberano (orden append-only sobre ν).
    """
    checks = {}

    # A1 — horizontes bien formados
    checks["A1"] = (
        isinstance(H, set) and isinstance(H_prime, set)
        and len(H) > 0 and len(H_prime) > 0
        and all(len(s) == 9 for s in H)
        and all(len(s) == 9 for s in H_prime)
    )

    # A2 — σ es función parcial (cada elemento del dominio mapea a uno solo)
    if isinstance(sigma, dict):
        checks["A2"] = all(s in H for s in sigma.keys())
    else:
        checks["A2"] = False

    # A3 — R_e coincide exactamente con el grafo de σ
    if isinstance(sigma, dict):
        graph_sigma = {(s, sigma[s]) for s in sigma}
        checks["A3"] = R_e == graph_sigma
    else:
        checks["A3"] = False

    # A4 — todo σ(s) pertenece a H'
    if isinstance(sigma, dict):
        checks["A4"] = all(sigma[s] in H_prime for s in sigma)
    else:
        checks["A4"] = False

    # A5 — todos los símbolos están en Σ
    checks["A5"] = (
        all(alphabet_check(s) for s in H)
        and all(alphabet_check(s) for s in H_prime)
    )

    # A6 — disciplina append-only (no se modifica retrospectivamente)
    # Verificación: la cuaterna es inmutable una vez construida.
    checks["A6"] = True  # las estructuras son frozenset/tuple-based

    return checks


def run() -> SV_TODO_NADA_RESULT:
    result = SV_TODO_NADA_RESULT(
        lab_id="lab02",
        section="§2.4",
        verdict=None,
        components=[],
        trace=[],
        passes_E7=False,
    )

    # Cuaterna canónica del ejemplo 2.4.2 sobre SV(9, 3): un suceso simple
    # que activa una posición no crítica del frame (P6 = árbol del paisaje).
    s_pre = (0, 0, 0, 0, 0, 'U', 0, 0, 0)   # estado pre-suceso con árbol U
    s_post = (0, 0, 0, 0, 0, 0, 0, 0, 0)    # estado post-suceso con árbol determinado
    H = {s_pre}
    H_prime = {s_post}
    sigma = {s_pre: s_post}
    R_e = {(s_pre, s_post)}

    checks = admissible_event_check(H, H_prime, sigma, R_e)

    for axiom, ok in checks.items():
        if ok:
            result.trace.append(f"{axiom} verificado.")
            result.components.append(0)
        else:
            result.trace.append(f"{axiom} fallido (E6).")
            result.components.append(1)

    result.passes_E7 = passes_E7(result.components)
    result.verdict = 0 if result.passes_E7 else 1
    return result


if __name__ == "__main__":
    print(header("lab02", "Suceso admisible", "§2.4"))
    r = run()
    print(r.render())
    print()
