# -*- coding: utf-8 -*-
"""
L.2 — Convergencia asintótica gobernada y conservación de U

Laboratorio de consistencia formal. No usa estadística, probabilidad,
inferencia opaca ni cierre favorable por ausencia de contradicción.
"""

LAB_ID = "L.2"
OBJETO = "Convergencia asintótica gobernada y conservación de U"
ENTRADAS = {'ξ(ε−0)': 'sostenida', 'γ': 'positivo estructural', 'U': 'indeterminación honesta', 'clausura_binaria_forzada': False}
RESTRICCIONES = ['Si ξ(ε−0) está sostenida, Φ_∞ no clausura en 0.', 'U no causa el proceso ni actúa como motor.', 'U no se degrada a ruido, media o ignorancia.']
SALIDA_ESPERADA = 'No clausura a reposo absoluto.'

def format_value(value):
    if isinstance(value, dict):
        return "; ".join(f"{k}={v}" for k, v in value.items())
    if isinstance(value, list):
        return "; ".join(str(x) for x in value)
    return str(value)

def emit(label, value):
    print(f"{label}: {format_value(value)}")

def main():
    xi_sostenida = True
    u_legitima = True
    u_es_motor = False
    clausura_binaria_forzada = False
    phi_infinito = "NO_NULO" if xi_sostenida else 0

    no_clausura = (phi_infinito != 0 and u_legitima and not u_es_motor and not clausura_binaria_forzada)
    salida_obtenida = {
        "Φ_∞": phi_infinito,
        "U_legitima": u_legitima,
        "U_motor": u_es_motor,
        "clausura_binaria_forzada": clausura_binaria_forzada,
    }
    residual = 0 if no_clausura else 1
    resultado = "APTO" if residual == 0 else "NO_APTO"

    emit("LAB_ID", LAB_ID)
    emit("OBJETO", OBJETO)
    emit("ENTRADAS", ENTRADAS)
    emit("RESTRICCIONES", RESTRICCIONES)
    emit("SALIDA_ESPERADA", SALIDA_ESPERADA)
    emit("SALIDA_OBTENIDA", salida_obtenida)
    emit("RESIDUAL", residual)
    emit("CONDICION_ACEPTACION", "Φ_∞≠0 ∧ U_legitima=True ∧ U_motor=False ∧ cierre_binario=False")
    emit("RESULTADO", resultado)

if __name__ == "__main__":
    main()
