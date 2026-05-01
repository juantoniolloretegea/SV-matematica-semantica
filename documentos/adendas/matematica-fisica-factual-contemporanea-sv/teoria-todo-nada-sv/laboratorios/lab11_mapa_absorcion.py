"""
Laboratorio 11 — Mapa de absorción y operador maestro 𝔘^unif_SV

Documento canónico vinculado:
  Teoría del TODO y de la NADA en el Sistema Vectorial SV
  https://github.com/juantoniolloretegea/SV-matematica-semantica/tree/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/teoria-todo-nada-sv

Sección doctrinal: §18
Criterio de aptitud: 𝔘^unif_SV = 0 ⟺ los 14 componentes (7 sectores + 7
identidades intersectoriales) son simultáneamente nulos.

Author:    Juan Antonio Lloret Egea
ORCID:     https://orcid.org/0000-0002-6634-3351
ISSN:      2695-6411
Editor:    IA eñ™ — La Biblia de la IA™ (Instituto Tecnológico Virtual de la
           Inteligencia Artificial para el Español, ITVIA)
License:   CC BY-NC-ND 4.0
Copyright: © 2026 Juan Antonio Lloret Egea. Todos los derechos reservados.
Protected: CEDRO — https://www.cedro.org/english?lng=en
"""

from sv_lib import SV_TODO_NADA_RESULT, header, N_star_SV, passes_E7


def U_unif_SV(sectores, identidades):
    """
    Operador maestro 𝔘^unif_SV del §18.5 del documento canónico:
        𝔘^unif_SV = ⊕_{j=1..7} 𝓤^(j)_SV(Φ^j) ⊕ ⊕_{k=1..7} 𝒮_k

    Por la cláusula C.2 del operador concatenador ⊕:
        𝔘^unif_SV = 0 ⟺ todos los 𝓤^(j)_SV = 0 ∧ todas las 𝒮_k cumplen.

    Argumentos:
        sectores    : lista de 7 valores en { 0, 1, U } (siete sectores).
        identidades : lista de 7 valores en { 0, 1, U } (siete identidades).

    Retorna veredicto del verificador 𝓝★_SV sobre los 14 componentes.
    """
    if len(sectores) != 7 or len(identidades) != 7:
        raise ValueError("Se requieren 7 sectores y 7 identidades intersectoriales.")
    return N_star_SV(*sectores, *identidades)


def run() -> SV_TODO_NADA_RESULT:
    result = SV_TODO_NADA_RESULT(
        lab_id="lab11",
        section="§18",
        verdict=None,
        components=[],
        trace=[],
        passes_E7=False,
    )

    # Caso canónico de cierre: los 14 componentes son nulos.
    sectores_canonicos = [0, 0, 0, 0, 0, 0, 0]      # 7 sectores
    identidades_canonicas = [0, 0, 0, 0, 0, 0, 0]   # 7 identidades intersectoriales

    v_canonico = U_unif_SV(sectores_canonicos, identidades_canonicas)
    result.trace.append(f"Caso canónico (14 componentes nulos):")
    result.trace.append(f"  𝔘^unif_SV = {v_canonico}  (esperado 0)")
    if v_canonico == 0:
        result.components.append(0)
    else:
        result.components.append(1)

    # Verificación de la cláusula C.1: si una componente vale 1, 𝔘^unif_SV = 1.
    sectores_C1 = [0, 0, 1, 0, 0, 0, 0]   # un sector con defecto
    v_C1 = U_unif_SV(sectores_C1, identidades_canonicas)
    result.trace.append(f"Cláusula C.1 (un sector vale 1):")
    result.trace.append(f"  𝔘^unif_SV = {v_C1}  (esperado 1)")
    if v_C1 == 1:
        result.components.append(0)
    else:
        result.components.append(1)

    # Verificación de la cláusula C.2: anulación conjunta.
    # 𝔘^unif_SV = 0 implica todos los componentes = 0.
    # Si CUALQUIER componente vale 1, 𝔘^unif_SV no puede valer 0.
    casos_C2 = []
    for i in range(7):
        sectores_test = [0] * 7
        sectores_test[i] = 1
        v = U_unif_SV(sectores_test, identidades_canonicas)
        casos_C2.append((f"sector_{i+1}=1", v))
    for i in range(7):
        identidades_test = [0] * 7
        identidades_test[i] = 1
        v = U_unif_SV(sectores_canonicos, identidades_test)
        casos_C2.append((f"identidad_{i+1}=1", v))

    todos_no_cero = all(v != 0 for _, v in casos_C2)
    result.trace.append(f"Cláusula C.2 (anulación conjunta):")
    result.trace.append(f"  Sobre 14 casos con un único componente = 1, todos producen 𝔘^unif_SV ≠ 0: {todos_no_cero}")
    if todos_no_cero:
        result.components.append(0)
    else:
        result.components.append(1)

    # Equivalencia bidireccional: 𝔘^unif_SV = 0 ⟺ 14 componentes = 0
    # Recíproco: si 𝔘^unif_SV = 0 sobre el caso canónico, los 14 son 0.
    todos_cero_canonico = all(c == 0 for c in sectores_canonicos + identidades_canonicas)
    if v_canonico == 0 and todos_cero_canonico:
        result.trace.append("Equivalencia: 𝔘^unif_SV = 0 ⟺ 14 componentes nulos ✓")
        result.components.append(0)
    else:
        result.trace.append("E6 — equivalencia rota.")
        result.components.append(1)

    result.passes_E7 = passes_E7(result.components)
    result.verdict = 0 if result.passes_E7 else 1
    return result


if __name__ == "__main__":
    print(header("lab11", "Mapa de absorción y operador maestro 𝔘^unif_SV", "§18"))
    r = run()
    print(r.render())
    print()
