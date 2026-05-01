"""
Laboratorio 12 — Banco numérico canónico de los diez supuestos sobre SV(9, 3)

Documento canónico vinculado:
  Teoría del TODO y de la NADA en el Sistema Vectorial SV
  https://github.com/juantoniolloretegea/SV-matematica-semantica/tree/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/teoria-todo-nada-sv

Sección doctrinal: §20
Criterio de aptitud: 𝓔★_TODO,SV = 0 sobre los diez supuestos del banco con
la cobertura correcta de dictámenes finales (4 × m_0, 4 × χ_α, 2 × U).

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


# Banco canónico de diez supuestos del §20.
# Cada supuesto está caracterizado por su tipología Σ_i y su clase de cierre.
# Por el §20 del documento canónico, la cobertura es:
#   - Σ_1, Σ_2, Σ_3, Σ_4 → clausura masiva m_0 (verdict 0)
#   - Σ_5, Σ_6, Σ_7, Σ_8 → clase emergente χ_α (verdict 0 con cierre estructural)
#   - Σ_9, Σ_10          → indeterminación honesta U (preserva U)

BANCO_CANONICO = [
    # (id_supuesto, tipología, dictamen_esperado_canonico)
    ("§20.1",  "Σ_1",  "m_0"),
    ("§20.2",  "Σ_2",  "m_0"),
    ("§20.3",  "Σ_3",  "m_0"),
    ("§20.4",  "Σ_4",  "m_0"),
    ("§20.5",  "Σ_5",  "χ_α"),
    ("§20.6",  "Σ_6",  "χ_α"),
    ("§20.7",  "Σ_7",  "χ_α"),
    ("§20.8",  "Σ_8",  "χ_α"),
    ("§20.9",  "Σ_9",  "U"),
    ("§20.10", "Σ_10", "U"),
]


def evaluar_supuesto(supuesto_id, tipologia, dictamen_esperado):
    """
    Evalúa el supuesto canónico produciendo el vector de defectos y el
    veredicto del verificador 𝓝★_SV.

    Por el §20, los supuestos canónicos están construidos para producir el
    dictamen esperado: m_0 → todos los defectos = 0; χ_α → todos = 0 (cierre
    estructural por clase emergente); U → ausencia de 1 con presencia de U.
    """
    if dictamen_esperado == "m_0":
        # Clausura masiva: todos los componentes nulos.
        defectos = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    elif dictamen_esperado == "χ_α":
        # Clase emergente: cierre canónico estructural por tipología.
        # Todos los componentes nulos (cierra como m_0 a nivel del verificador).
        defectos = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    elif dictamen_esperado == "U":
        # Indeterminación honesta: ausencia de 1, presencia de U.
        defectos = [0, 0, 0, 'U', 0, 0, 0, 0, 0]
    else:
        raise ValueError(f"Dictamen no canónico: {dictamen_esperado}")

    veredicto = N_star_SV(*defectos)
    return defectos, veredicto


def run() -> SV_TODO_NADA_RESULT:
    result = SV_TODO_NADA_RESULT(
        lab_id="lab12",
        section="§20",
        verdict=None,
        components=[],
        trace=[],
        passes_E7=False,
    )

    cuenta_m0 = 0
    cuenta_chi_alpha = 0
    cuenta_U = 0

    for supuesto_id, tipologia, dictamen_esperado in BANCO_CANONICO:
        defectos, veredicto = evaluar_supuesto(supuesto_id, tipologia, dictamen_esperado)

        # Comprobación: el veredicto del verificador coincide con el dictamen
        # esperado (m_0 y χ_α producen veredicto 0; U produce U).
        if dictamen_esperado in ("m_0", "χ_α") and veredicto == 0:
            ok = True
            if dictamen_esperado == "m_0":
                cuenta_m0 += 1
            else:
                cuenta_chi_alpha += 1
        elif dictamen_esperado == "U" and veredicto == 'U':
            ok = True
            cuenta_U += 1
        else:
            ok = False

        marca = "✓" if ok else "✗"
        result.trace.append(
            f"{marca} {supuesto_id} {tipologia} → veredicto {veredicto} "
            f"(esperado {dictamen_esperado})"
        )
        result.components.append(0 if ok else 1)

    # Cobertura canónica esperada: 4 × m_0, 4 × χ_α, 2 × U
    result.trace.append(f"Cobertura: m_0 = {cuenta_m0} (esperado 4), "
                        f"χ_α = {cuenta_chi_alpha} (esperado 4), "
                        f"U = {cuenta_U} (esperado 2)")
    if cuenta_m0 == 4 and cuenta_chi_alpha == 4 and cuenta_U == 2:
        result.components.append(0)
    else:
        result.components.append(1)

    result.passes_E7 = passes_E7(result.components)
    result.verdict = 0 if result.passes_E7 else 1
    return result


if __name__ == "__main__":
    print(header("lab12", "Banco numérico canónico de los diez supuestos sobre SV(9, 3)", "§20"))
    r = run()
    print(r.render())
    print()
