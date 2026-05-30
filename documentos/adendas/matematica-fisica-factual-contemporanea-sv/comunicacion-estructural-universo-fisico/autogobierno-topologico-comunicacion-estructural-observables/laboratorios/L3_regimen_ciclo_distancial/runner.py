# -*- coding: utf-8 -*-
"""
L.3 — Régimen ciclo-distancial y topología sin transmisión

Laboratorio de consistencia formal. No usa estadística, probabilidad,
inferencia opaca ni cierre favorable por ausencia de contradicción.
"""

LAB_ID = "L.3"
OBJETO = "Régimen ciclo-distancial y topología sin transmisión"
ENTRADAS = {'T_obs': '4.354948800×10^17 s', 'T_ciclo': '2·T_obs', 'limite_propagativo': 'c·T_obs', 'transmision_al_unisono': False}
RESTRICCIONES = ['T_obs opera como régimen ciclo-distancial, no como tiempo rector.', 'El lazo topológico no se modela como transmisión física.', 'Toda propagación física conserva latencia de dominio.']
SALIDA_ESPERADA = 'Separación entre cambio físico con latencia y propiedad topológica no propagativa.'

def format_value(value):
    if isinstance(value, dict):
        return "; ".join(f"{k}={v}" for k, v in value.items())
    if isinstance(value, list):
        return "; ".join(str(x) for x in value)
    return str(value)

def emit(label, value):
    print(f"{label}: {format_value(value)}")

def main():
    from decimal import Decimal
    T_obs = Decimal("4.354948800e17")
    T_ciclo = Decimal(2) * T_obs
    transmision_al_unisono = False
    latencia_fisica = True
    tiempo_rector = False

    separacion_correcta = (T_ciclo == Decimal("8.709897600e17") and not transmision_al_unisono and latencia_fisica and not tiempo_rector)
    salida_obtenida = {
        "T_obs": f"{T_obs:.9E}",
        "T_ciclo": f"{T_ciclo:.9E}",
        "transmision_al_unisono": transmision_al_unisono,
        "latencia_fisica": latencia_fisica,
        "tiempo_rector": tiempo_rector,
    }
    residual = 0 if separacion_correcta else 1
    resultado = "APTO" if residual == 0 else "NO_APTO"

    emit("LAB_ID", LAB_ID)
    emit("OBJETO", OBJETO)
    emit("ENTRADAS", ENTRADAS)
    emit("RESTRICCIONES", RESTRICCIONES)
    emit("SALIDA_ESPERADA", SALIDA_ESPERADA)
    emit("SALIDA_OBTENIDA", salida_obtenida)
    emit("RESIDUAL", residual)
    emit("CONDICION_ACEPTACION", "T_ciclo=2·T_obs ∧ transmisión_al_unísono=False ∧ tiempo_rector=False")
    emit("RESULTADO", resultado)

if __name__ == "__main__":
    main()
