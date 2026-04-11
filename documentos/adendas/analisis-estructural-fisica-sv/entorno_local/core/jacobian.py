"""
Jacobiano estructural del Sistema Vectorial SV.

Mide la sensibilidad del dictamen ante perturbaciones explícitas
de los estados de una trayectoria. Para cada estado numérico,
introduce una perturbación de magnitud epsilon y registra si
el dictamen cambia. Los estados de tipo U no son perturbables.
"""

def compute_jacobian(states, epsilon=0.1):
    from runner.sv_runner import run_sv_analysis

    base = run_sv_analysis(states)
    base_verdict = base['verdict']
    sensitivities = []

    for i, s in enumerate(states):
        if isinstance(s, (int, float)):
            perturbed_up = list(states)
            perturbed_up[i] = s + epsilon
            result_up = run_sv_analysis(perturbed_up)

            perturbed_down = list(states)
            perturbed_down[i] = max(0.0, s - epsilon)
            result_down = run_sv_analysis(perturbed_down)

            sensitive = (
                result_up['verdict'] != base_verdict or
                result_down['verdict'] != base_verdict
            )
            sensitivities.append({
                'index': i,
                'state': s,
                'perturbacion': epsilon,
                'dictamen_base': base_verdict,
                'dictamen_mas': result_up['verdict'],
                'dictamen_menos': result_down['verdict'],
                'sensible': sensitive,
            })
        else:
            sensitivities.append({
                'index': i,
                'state': s,
                'perturbacion': None,
                'dictamen_base': base_verdict,
                'dictamen_mas': None,
                'dictamen_menos': None,
                'sensible': False,
            })

    return {
        'dictamen_base': base_verdict,
        'estados_sensibles': [x['index'] for x in sensitivities if x['sensible']],
        'sensibilidades': sensitivities,
    }
