# -*- coding: utf-8 -*-
"""
L.6 — Familia de transductores 𝓖★TrU(D)

Laboratorio de consistencia formal. No usa estadística, probabilidad,
inferencia opaca ni cierre favorable por ausencia de contradicción.
"""

LAB_ID = "L.6"
OBJETO = "Familia de transductores 𝓖★TrU(D)"
ENTRADAS = {'campos_requeridos': ['Ω_D', 'M_D', 'F_D', 'I_D', 'C_D', 'B_D', 'Δ_D', 'R_D', 'Tr_D'], 'derivacion': 'desde 𝓒★ObsU'}
RESTRICCIONES = ['Un transductor legítimo deriva de 𝓒★ObsU.', 'Todo campo requerido debe estar declarado.', 'No se admite puente por analogía libre.']
SALIDA_ESPERADA = 'Transductor legítimo sólo por especialización tipada.'

def format_value(value):
    if isinstance(value, dict):
        return "; ".join(f"{k}={v}" for k, v in value.items())
    if isinstance(value, list):
        return "; ".join(str(x) for x in value)
    return str(value)

def emit(label, value):
    print(f"{label}: {format_value(value)}")

def main():
    campos_requeridos = ["Ω_D", "M_D", "F_D", "I_D", "C_D", "B_D", "Δ_D", "R_D", "Tr_D"]

    def es_transductor_legitimo(candidato):
        return (
            candidato.get("derivado_de_𝓒★ObsU") is True
            and candidato.get("analogía_libre") is False
            and all(candidato.get(campo) == "declarado" for campo in campos_requeridos)
        )

    casos = {
        "legitimo": {"derivado_de_𝓒★ObsU": True, "analogía_libre": False, **{c: "declarado" for c in campos_requeridos}},
        "analogico": {"derivado_de_𝓒★ObsU": False, "analogía_libre": True, **{c: "declarado" for c in campos_requeridos}},
        "incompleto": {"derivado_de_𝓒★ObsU": True, "analogía_libre": False, **{c: "declarado" for c in campos_requeridos[:-1]}},
    }
    salidas = {nombre: es_transductor_legitimo(candidato) for nombre, candidato in casos.items()}
    condicion = salidas == {"legitimo": True, "analogico": False, "incompleto": False}
    residual = 0 if condicion else 1
    resultado = "APTO" if residual == 0 else "NO_APTO"

    emit("LAB_ID", LAB_ID)
    emit("OBJETO", OBJETO)
    emit("ENTRADAS", ENTRADAS)
    emit("RESTRICCIONES", RESTRICCIONES)
    emit("SALIDA_ESPERADA", SALIDA_ESPERADA)
    emit("SALIDA_OBTENIDA", salidas)
    emit("RESIDUAL", residual)
    emit("CONDICION_ACEPTACION", "derivado_de_𝓒★ObsU=True ∧ todos_los_campos_declarados ∧ analogía_libre=False")
    emit("RESULTADO", resultado)

if __name__ == "__main__":
    main()
