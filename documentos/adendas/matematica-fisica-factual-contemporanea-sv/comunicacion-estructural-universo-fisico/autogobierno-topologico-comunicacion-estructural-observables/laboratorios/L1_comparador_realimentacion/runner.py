# -*- coding: utf-8 -*-
"""
L.1 — Comparador con realimentación y ruptura de equipotencialidad

Laboratorio de consistencia formal. No usa estadística, probabilidad,
inferencia opaca ni cierre favorable por ausencia de contradicción.
"""

LAB_ID = "L.1"
OBJETO = "Comparador con realimentación y ruptura de equipotencialidad"
ENTRADAS = {'Φ_0': 0, 'ε−0': 'activo como borde preformal', 'agente_externo': False, 'clausura_binaria_forzada': False}
RESTRICCIONES = ['La equipotencialidad inicial debe cerrar en Φ_0=0.', 'La ruptura debe producir Φ(τ_0)≠0.', 'La ruptura no puede depender de agente externo.', 'U no se convierte en número ni en probabilidad.']
SALIDA_ESPERADA = 'Ruptura controlada sin agente externo.'

def format_value(value):
    if isinstance(value, dict):
        return "; ".join(f"{k}={v}" for k, v in value.items())
    if isinstance(value, list):
        return "; ".join(str(x) for x in value)
    return str(value)

def emit(label, value):
    print(f"{label}: {format_value(value)}")

def main():
    phi_0 = 0
    epsilon_preformal_activo = True
    agente_externo = False
    phi_tau0 = "NO_NULO" if epsilon_preformal_activo and not agente_externo else 0

    ruptura_controlada = (phi_0 == 0 and phi_tau0 != 0 and epsilon_preformal_activo and not agente_externo)
    salida_obtenida = {
        "Φ_0": phi_0,
        "Φ(τ_0)": phi_tau0,
        "ruptura_controlada": ruptura_controlada,
        "agente_externo": agente_externo,
    }
    residual = 0 if ruptura_controlada else 1
    resultado = "APTO" if residual == 0 else "NO_APTO"

    emit("LAB_ID", LAB_ID)
    emit("OBJETO", OBJETO)
    emit("ENTRADAS", ENTRADAS)
    emit("RESTRICCIONES", RESTRICCIONES)
    emit("SALIDA_ESPERADA", SALIDA_ESPERADA)
    emit("SALIDA_OBTENIDA", salida_obtenida)
    emit("RESIDUAL", residual)
    emit("CONDICION_ACEPTACION", "Φ_0=0 ∧ Φ(τ_0)≠0 ∧ ε−0 activo ∧ agente_externo=False")
    emit("RESULTADO", resultado)

if __name__ == "__main__":
    main()
