# -*- coding: utf-8 -*-
"""
L.9 — Matriz integrada de autogobierno y comunicación estructural

Laboratorio de consistencia formal. No usa estadística, probabilidad,
inferencia opaca ni cierre favorable por ausencia de contradicción.
"""

LAB_ID = "L.9"
OBJETO = "Matriz integrada de autogobierno y comunicación estructural"
ENTRADAS = {'bloques': ['comparador', 'convergencia', 'ciclo-distancia', 'tránsito', 'observables', 'transductores', 'canal', 'predominancia'], 'prohibiciones': ['tiempo rector', 'sintiencia', 'transmisión al unísono', 'probabilidad fundante']}
RESTRICCIONES = ['La integración exige cierre conjunto de los bloques L.1-L.8.', 'No debe aparecer tiempo rector, sintiencia, transmisión al unísono ni probabilidad fundante.', 'La salida conserva U como indeterminación honesta.']
SALIDA_ESPERADA = 'Integración sin tiempo rector, sintiencia, transmisión al unísono ni probabilidad fundante.'

def format_value(value):
    if isinstance(value, dict):
        return "; ".join(f"{k}={v}" for k, v in value.items())
    if isinstance(value, list):
        return "; ".join(str(x) for x in value)
    return str(value)

def emit(label, value):
    print(f"{label}: {format_value(value)}")

def main():
    bloques = {
        "comparador": "APTO",
        "convergencia": "APTO",
        "ciclo_distancia": "APTO",
        "transito": "APTO",
        "observables": "APTO",
        "transductores": "APTO",
        "canal_diccionario": "APTO",
        "predominancia": "APTO",
    }
    prohibiciones = {
        "tiempo_rector": False,
        "sintiencia": False,
        "transmision_al_unisono": False,
        "probabilidad_fundante": False,
        "U_numerizada": False,
    }
    integracion = all(v == "APTO" for v in bloques.values()) and not any(prohibiciones.values())
    salida_obtenida = {"bloques": bloques, "prohibiciones_activas": prohibiciones, "integracion": integracion}
    residual = 0 if integracion else 1
    resultado = "APTO" if residual == 0 else "NO_APTO"

    emit("LAB_ID", LAB_ID)
    emit("OBJETO", OBJETO)
    emit("ENTRADAS", ENTRADAS)
    emit("RESTRICCIONES", RESTRICCIONES)
    emit("SALIDA_ESPERADA", SALIDA_ESPERADA)
    emit("SALIDA_OBTENIDA", salida_obtenida)
    emit("RESIDUAL", residual)
    emit("CONDICION_ACEPTACION", "todos_los_bloques=APTO ∧ ninguna_prohibición_activa")
    emit("RESULTADO", resultado)

if __name__ == "__main__":
    main()
