# -*- coding: utf-8 -*-
"""
L.8 — Predominancia compatible y predominancia lesiva

Laboratorio de consistencia formal. No usa estadística, probabilidad,
inferencia opaca ni cierre favorable por ausencia de contradicción.
"""

LAB_ID = "L.8"
OBJETO = "Predominancia compatible y predominancia lesiva"
ENTRADAS = {'Pred_AB^compat': 'Φ_AB≠0 ∧ R_polo_A trazado ∧ R_polo_B trazado ∧ Δ_AB absorbido', 'Pred_AB^lesiva': 'Canal_AB^Γ capturado ∧ 𝓓_AB^⊥ usado contra retorno de Ω_rector ∧ Δ no absorbido'}
RESTRICCIONES = ['La predominancia compatible conserva función de ambos polos.', 'La predominancia lesiva captura canal y deja residual no absorbido.', 'La distinción es estructural, no moral.']
SALIDA_ESPERADA = 'Distinción estructural entre asimetría gobernada y captura lesiva.'

def format_value(value):
    if isinstance(value, dict):
        return "; ".join(f"{k}={v}" for k, v in value.items())
    if isinstance(value, list):
        return "; ".join(str(x) for x in value)
    return str(value)

def emit(label, value):
    print(f"{label}: {format_value(value)}")

def main():
    def clasificar(caso):
        compatible = (
            caso["Φ_AB"] != 0
            and caso["R_polo_A"] == "trazado"
            and caso["R_polo_B"] == "trazado"
            and caso["Δ_AB"] == "absorbido"
            and not caso["canal_capturado_lesivo"]
        )
        lesiva = (
            caso["canal_capturado_lesivo"]
            and caso["diccionario_contra_retorno_rector"]
            and caso["Δ_AB"] == "no_absorbido"
        )
        if compatible:
            return "compatible"
        if lesiva:
            return "lesiva"
        return "U"

    casos = {
        "simetria_gobernada": {"Φ_AB": 3, "R_polo_A": "trazado", "R_polo_B": "trazado", "Δ_AB": "absorbido", "canal_capturado_lesivo": False, "diccionario_contra_retorno_rector": False},
        "captura_lesiva": {"Φ_AB": 5, "R_polo_A": "trazado", "R_polo_B": "perdido", "Δ_AB": "no_absorbido", "canal_capturado_lesivo": True, "diccionario_contra_retorno_rector": True},
        "incompleto": {"Φ_AB": 1, "R_polo_A": "trazado", "R_polo_B": "U", "Δ_AB": "U", "canal_capturado_lesivo": False, "diccionario_contra_retorno_rector": False},
    }
    salidas = {nombre: clasificar(caso) for nombre, caso in casos.items()}
    condicion = salidas == {"simetria_gobernada": "compatible", "captura_lesiva": "lesiva", "incompleto": "U"}
    residual = 0 if condicion else 1
    resultado = "APTO" if residual == 0 else "NO_APTO"

    emit("LAB_ID", LAB_ID)
    emit("OBJETO", OBJETO)
    emit("ENTRADAS", ENTRADAS)
    emit("RESTRICCIONES", RESTRICCIONES)
    emit("SALIDA_ESPERADA", SALIDA_ESPERADA)
    emit("SALIDA_OBTENIDA", salidas)
    emit("RESIDUAL", residual)
    emit("CONDICION_ACEPTACION", "compatible, lesiva e indeterminada quedan separadas sin juicio moral")
    emit("RESULTADO", resultado)

if __name__ == "__main__":
    main()
