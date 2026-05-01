"""
Laboratorio 03 — Distancia factual fibrosa

Documento canónico vinculado:
  Teoría del TODO y de la NADA en el Sistema Vectorial SV
  https://github.com/juantoniolloretegea/SV-matematica-semantica/tree/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/teoria-todo-nada-sv

Sección doctrinal: §§2.7-2.8 y §8
Criterio de aptitud: igualdad estricta entre la suma local y la distancia
global con observable monótono (coherencia telescópica del §8.5).

Author:    Juan Antonio Lloret Egea
ORCID:     https://orcid.org/0000-0002-6634-3351
ISSN:      2695-6411
Editor:    IA eñ™ — La Biblia de la IA™ (Instituto Tecnológico Virtual de la
           Inteligencia Artificial para el Español, ITVIA)
License:   CC BY-NC-ND 4.0
Copyright: © 2026 Juan Antonio Lloret Egea. Todos los derechos reservados.
Protected: CEDRO — https://www.cedro.org/english?lng=en
"""

from sv_lib import SV_TODO_NADA_RESULT, header, zeta_SV, passes_E7


def Phi(state):
    """
    Observable monótono Φ del §2.7.2 del documento canónico.
    Cuenta el número de posiciones con valor 0 (verificadas) en la inscripción
    factual. Esta es una función estructural monótona no decreciente sobre la
    cadena de inscripciones que despliegan el suceso.
    """
    return sum(1 for x in state if x == 0)


def d_local(s_k, s_k_plus_1):
    """
    Distancia factual fibrosa local 𝑑^SV_Φ(S_{k+1}, S_k) del §2.8 / §8.
    Diferencia absoluta del observable monótono entre estados consecutivos.
    """
    return abs(Phi(s_k_plus_1) - Phi(s_k))


def D_global(chain):
    """
    Distancia factual fibrosa global 𝐷^SV_Φ(Γ) del §8.
    Distancia entre extremos del despliegue del fenómeno.
    """
    return abs(Phi(chain[-1]) - Phi(chain[0]))


def run() -> SV_TODO_NADA_RESULT:
    result = SV_TODO_NADA_RESULT(
        lab_id="lab03",
        section="§§2.7-2.8, 8",
        verdict=None,
        components=[],
        trace=[],
        passes_E7=False,
    )

    # Cadena canónica del ejemplo 2.7.2 sobre SV(9, 3): despliegue progresivo
    # de un fenómeno con observable monótono Φ no decreciente.
    chain = [
        ('U', 'U', 'U', 'U', 'U', 'U', 'U', 'U', 'U'),
        (0,   'U', 'U', 'U', 'U', 'U', 'U', 'U', 'U'),
        (0,   0,   'U', 'U', 'U', 'U', 'U', 'U', 'U'),
        (0,   0,   0,   'U', 'U', 'U', 'U', 'U', 'U'),
        (0,   0,   0,   0,   'U', 'U', 'U', 'U', 'U'),
        (0,   0,   0,   0,   0,   'U', 'U', 'U', 'U'),
    ]

    # 1) Coherencia telescópica: suma local = distancia global
    suma_local = sum(d_local(chain[k], chain[k + 1]) for k in range(len(chain) - 1))
    dist_global = D_global(chain)
    result.trace.append(f"Suma local de distancias = {suma_local}")
    result.trace.append(f"Distancia global Γ      = {dist_global}")

    if suma_local == dist_global:
        result.trace.append("Coherencia telescópica verificada (§8.5).")
        result.components.append(0)
    else:
        result.trace.append("E6 — coherencia telescópica fallida.")
        result.components.append(1)

    # 2) Monotonía no decreciente del observable Φ
    phi_values = [Phi(s) for s in chain]
    is_monotone = all(phi_values[k] <= phi_values[k + 1] for k in range(len(phi_values) - 1))
    result.trace.append(f"Φ(chain) = {phi_values}")
    if is_monotone:
        result.trace.append("Monotonía no decreciente verificada.")
        result.components.append(0)
    else:
        result.trace.append("E6 — monotonía fallida.")
        result.components.append(1)

    # 3) Δ^Φ_q canónico = ζ_SV(suma_local - dist_global) = ζ_SV(0) = 0
    delta_phi_q = zeta_SV(suma_local - dist_global)
    result.trace.append(f"Δ^Φ_q = ζ_SV({suma_local - dist_global}) = {delta_phi_q}")
    result.components.append(delta_phi_q)

    result.passes_E7 = passes_E7(result.components)
    result.verdict = 0 if result.passes_E7 else 1
    return result


if __name__ == "__main__":
    print(header("lab03", "Distancia factual fibrosa", "§§2.7-2.8, 8"))
    r = run()
    print(r.render())
    print()
