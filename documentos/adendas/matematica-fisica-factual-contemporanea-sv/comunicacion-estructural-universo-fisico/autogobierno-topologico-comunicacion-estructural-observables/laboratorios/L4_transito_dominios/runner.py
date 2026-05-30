# -*- coding: utf-8 -*-
"""
L.4 — Ley general del tránsito por dominios

Laboratorio de consistencia formal. No usa estadística, probabilidad,
inferencia opaca ni cierre favorable por ausencia de contradicción.
"""

LAB_ID = "L.4"
OBJETO = "Ley general del tránsito por dominios"
ENTRADAS = {'R_D^SV': ['r_dom', 'r_id', 'r_est', 'r_front', 'r_canal', 'r_traza', 'r_ret'], 'T_D^SV': '0 ⇔ R_D^SV=0', 'Id_trans^SV': '1 ⇔ residual compuesto nulo'}
RESTRICCIONES = ['El tránsito cierra sólo si todas las restricciones locales anulan residual.', 'La identidad de tránsito exige cierre de la cadena completa.', 'Un componente U conserva indeterminación honesta y no se fuerza a 0.']
SALIDA_ESPERADA = 'Cierre sólo si todas las restricciones locales anulan residual.'

def format_value(value):
    if isinstance(value, dict):
        return "; ".join(f"{k}={v}" for k, v in value.items())
    if isinstance(value, list):
        return "; ".join(str(x) for x in value)
    return str(value)

def emit(label, value):
    print(f"{label}: {format_value(value)}")

def main():
    def residual_compuesto(componentes):
        if any(v == 1 for v in componentes):
            return 1
        if any(v == "U" for v in componentes):
            return "U"
        return 0

    casos = {
        "cerrado": [0, 0, 0, 0, 0, 0, 0],
        "contradictorio": [0, 0, 1, 0, 0, 0, 0],
        "indeterminado": [0, 0, "U", 0, 0, 0, 0],
    }
    salidas = {}
    for nombre, componentes in casos.items():
        R = residual_compuesto(componentes)
        T = 0 if R == 0 else R
        Id = 1 if R == 0 else R
        salidas[nombre] = {"R_D^SV": R, "T_D^SV": T, "Id_trans^SV": Id}

    condicion = (
        salidas["cerrado"] == {"R_D^SV": 0, "T_D^SV": 0, "Id_trans^SV": 1}
        and salidas["contradictorio"]["R_D^SV"] == 1
        and salidas["indeterminado"]["R_D^SV"] == "U"
    )
    residual = 0 if condicion else 1
    resultado = "APTO" if residual == 0 else "NO_APTO"

    emit("LAB_ID", LAB_ID)
    emit("OBJETO", OBJETO)
    emit("ENTRADAS", ENTRADAS)
    emit("RESTRICCIONES", RESTRICCIONES)
    emit("SALIDA_ESPERADA", SALIDA_ESPERADA)
    emit("SALIDA_OBTENIDA", salidas)
    emit("RESIDUAL", residual)
    emit("CONDICION_ACEPTACION", "cerrado→R=0,T=0,Id=1; contradictorio→R=1; indeterminado→R=U")
    emit("RESULTADO", resultado)

if __name__ == "__main__":
    main()
