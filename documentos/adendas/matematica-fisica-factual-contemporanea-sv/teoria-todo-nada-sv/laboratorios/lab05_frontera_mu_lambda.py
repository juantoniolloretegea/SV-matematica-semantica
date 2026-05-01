"""
Laboratorio 05 — Frontera común de colapso cíclico (μ, λ) = (0, 0)

Documento canónico vinculado:
  Teoría del TODO y de la NADA en el Sistema Vectorial SV
  https://github.com/juantoniolloretegea/SV-matematica-semantica/tree/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/teoria-todo-nada-sv

Sección doctrinal: §10
Criterio de aptitud: nulidad simultánea estricta (μ, λ) = (0, 0).

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


def mu_close(trayectoria):
    """
    Magnitud de cierre interno μ del §10.
    Cuenta U remanentes (no clausurados) en el último estado de la trayectoria.
    """
    last = trayectoria[-1]
    return sum(1 for x in last if x == 'U')


def lambda_border(trayectoria):
    """
    Magnitud de borde λ del §10.
    Cuenta posiciones con cambio respecto al primer estado que no acaban en
    valor canónico fuerte (0 o 1) en el último estado.
    """
    first = trayectoria[0]
    last = trayectoria[-1]
    cambios_no_resueltos = 0
    for i in range(len(first)):
        if first[i] != last[i] and last[i] not in (0, 1):
            cambios_no_resueltos += 1
    return cambios_no_resueltos


def run() -> SV_TODO_NADA_RESULT:
    result = SV_TODO_NADA_RESULT(
        lab_id="lab05",
        section="§10",
        verdict=None,
        components=[],
        trace=[],
        passes_E7=False,
    )

    # Trayectoria canónica del ciclo q sobre SV(9, 3) que cierra completamente:
    # parte de inscripción inicial con U honestas y termina con todas resueltas.
    trayectoria = [
        ('U', 'U', 'U', 'U', 'U', 'U', 'U', 'U', 'U'),
        (0,   'U', 'U', 'U', 'U', 'U', 'U', 'U', 'U'),
        (0,   0,   'U', 'U', 'U', 'U', 'U', 'U', 'U'),
        (0,   0,   0,   'U', 'U', 'U', 'U', 'U', 'U'),
        (0,   0,   0,   0,   'U', 'U', 'U', 'U', 'U'),
        (0,   0,   0,   0,   0,   'U', 'U', 'U', 'U'),
        (0,   0,   0,   0,   0,   0,   'U', 'U', 'U'),
        (0,   0,   0,   0,   0,   0,   0,   'U', 'U'),
        (0,   0,   0,   0,   0,   0,   0,   0,   'U'),
        (0,   0,   0,   0,   0,   0,   0,   0,   0),
    ]

    mu = mu_close(trayectoria)
    lam = lambda_border(trayectoria)

    result.trace.append(f"μ (cierre interno) = {mu}")
    result.trace.append(f"λ (borde) = {lam}")

    # Nulidad simultánea estricta (μ, λ) = (0, 0)
    if mu == 0 and lam == 0:
        result.trace.append("(μ, λ) = (0, 0) verificado: frontera común.")
        result.components.append(0)
    else:
        result.trace.append("E6 — (μ, λ) ≠ (0, 0).")
        result.components.append(1)

    # 𝓒_q = ζ_SV(μ + λ) = ζ_SV(0) = 0
    C_q = zeta_SV(mu + lam)
    result.trace.append(f"𝓒_q = ζ_SV(μ + λ) = ζ_SV({mu + lam}) = {C_q}")
    result.components.append(C_q)

    # Verificación de nulidad simultánea por componente
    result.components.append(zeta_SV(mu))
    result.components.append(zeta_SV(lam))

    result.passes_E7 = passes_E7(result.components)
    result.verdict = 0 if result.passes_E7 else 1
    return result


if __name__ == "__main__":
    print(header("lab05", "Frontera común de colapso cíclico (μ, λ) = (0, 0)", "§10"))
    r = run()
    print(r.render())
    print()
