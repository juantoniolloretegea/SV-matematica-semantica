# -*- coding: utf-8 -*-
"""
L.7 — Canal, diccionario semántico estructural y Diag_AB^⊥

Laboratorio de consistencia formal. No usa estadística, probabilidad,
inferencia opaca ni cierre favorable por ausencia de contradicción.
"""

LAB_ID = "L.7"
OBJETO = "Canal, diccionario semántico estructural y Diag_AB^⊥"
ENTRADAS = {'Diag_AB^⊥': '1 ⇔ Canal_AB^Γ=1 ∧ 𝓓_AB^⊥ apto ∧ R_AB trazado ∧ Δ_sem admisible'}
RESTRICCIONES = ['La consolidación positiva exige canal, diccionario, retorno y residual admisible.', 'Sin canal no hay consolidación.', 'Con retorno o diccionario insuficiente se conserva U si no hay contradicción material.']
SALIDA_ESPERADA = 'Consolidación positiva sólo con canal, diccionario, retorno y residual.'

def format_value(value):
    if isinstance(value, dict):
        return "; ".join(f"{k}={v}" for k, v in value.items())
    if isinstance(value, list):
        return "; ".join(str(x) for x in value)
    return str(value)

def emit(label, value):
    print(f"{label}: {format_value(value)}")

def main():
    def diag(canal, diccionario, retorno, delta_admisible):
        if canal == 1 and diccionario == 1 and retorno == 1 and delta_admisible is True:
            return 1
        if canal == 0 or diccionario == 0 or retorno == 0 or delta_admisible is False:
            return 0
        return "U"

    casos = {
        "consolidado": diag(1, 1, 1, True),
        "sin_canal": diag(0, 1, 1, True),
        "indeterminado": diag(1, "U", 1, True),
    }
    condicion = casos == {"consolidado": 1, "sin_canal": 0, "indeterminado": "U"}
    residual = 0 if condicion else 1
    resultado = "APTO" if residual == 0 else "NO_APTO"

    emit("LAB_ID", LAB_ID)
    emit("OBJETO", OBJETO)
    emit("ENTRADAS", ENTRADAS)
    emit("RESTRICCIONES", RESTRICCIONES)
    emit("SALIDA_ESPERADA", SALIDA_ESPERADA)
    emit("SALIDA_OBTENIDA", casos)
    emit("RESIDUAL", residual)
    emit("CONDICION_ACEPTACION", "consolidado→1; falta material→0; incompleto sin contradicción→U")
    emit("RESULTADO", resultado)

if __name__ == "__main__":
    main()
