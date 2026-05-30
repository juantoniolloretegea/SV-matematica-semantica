# -*- coding: utf-8 -*-
"""
L.5 — Fórmula universal de gobierno de observables

Laboratorio de consistencia formal. No usa estadística, probabilidad,
inferencia opaca ni cierre favorable por ausencia de contradicción.
"""

LAB_ID = "L.5"
OBJETO = "Fórmula universal de gobierno de observables"
ENTRADAS = {'𝓒★ObsU': '𝓝★[ΩM_D, 𝔛, F_D, I_D, C_D, B_D, Δ_D, R_D, Tr_D]', 'salida': '{0,1,U}'}
RESTRICCIONES = ['Todas las restricciones en 0 producen observable fuerte.', 'Cualquier contradicción material produce no admisión.', 'La presencia de U sin contradicción conserva indeterminación honesta.']
SALIDA_ESPERADA = 'Admisión, no admisión o U sin cierre impropio.'

def format_value(value):
    if isinstance(value, dict):
        return "; ".join(f"{k}={v}" for k, v in value.items())
    if isinstance(value, list):
        return "; ".join(str(x) for x in value)
    return str(value)

def emit(label, value):
    print(f"{label}: {format_value(value)}")

def main():
    def C_obsu(restricciones):
        if any(v == 1 for v in restricciones.values()):
            return 1
        if any(v == "U" for v in restricciones.values()):
            return "U"
        return 0

    casos = {
        "observable_fuerte": dict.fromkeys(["ΩM_D", "𝔛", "F_D", "I_D", "C_D", "B_D", "Δ_D", "R_D", "Tr_D"], 0),
        "no_admisible": {"ΩM_D": 0, "𝔛": 0, "F_D": 0, "I_D": 1, "C_D": 0, "B_D": 0, "Δ_D": 0, "R_D": 0, "Tr_D": 0},
        "indeterminado": {"ΩM_D": 0, "𝔛": "U", "F_D": 0, "I_D": 0, "C_D": 0, "B_D": 0, "Δ_D": 0, "R_D": 0, "Tr_D": 0},
    }
    salidas = {nombre: C_obsu(restricciones) for nombre, restricciones in casos.items()}
    condicion = salidas == {"observable_fuerte": 0, "no_admisible": 1, "indeterminado": "U"}
    residual = 0 if condicion else 1
    resultado = "APTO" if residual == 0 else "NO_APTO"

    emit("LAB_ID", LAB_ID)
    emit("OBJETO", OBJETO)
    emit("ENTRADAS", ENTRADAS)
    emit("RESTRICCIONES", RESTRICCIONES)
    emit("SALIDA_ESPERADA", SALIDA_ESPERADA)
    emit("SALIDA_OBTENIDA", salidas)
    emit("RESIDUAL", residual)
    emit("CONDICION_ACEPTACION", "todo 0→0; alguna contradicción→1; U sin contradicción→U")
    emit("RESULTADO", resultado)

if __name__ == "__main__":
    main()
