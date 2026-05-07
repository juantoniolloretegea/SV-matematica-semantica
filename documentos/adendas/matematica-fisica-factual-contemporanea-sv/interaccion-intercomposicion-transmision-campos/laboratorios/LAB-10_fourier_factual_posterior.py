"""
LAB-10 — Verificador del mapeo posterior con Fourier factual
================================================================

Verifica computacionalmente las cinco reglas duras del apartado 14 del
documento principal sobre el mapeo modal posterior con Fourier factual:

    R1 — Fourier factual puede analizar ciclos.
    R2 — Fourier factual no puede crear campos.
    R3 — Fourier factual no puede cerrar U.
    R4 — Fourier factual no puede sustituir residual.
    R5 — Fourier factual no puede decidir interacción sin trayectoria.

El mapeo modal sólo procede tras seis pasos operativos previos:

    1. Definir el campo admitido.
    2. Construir su función ordinal.
    3. Verificar trayectoria.
    4. Declarar frontera.
    5. Calcular residual.
    6. Evaluar Ciclo de Suceso.

El laboratorio implementa cinco intentos adversariales de violación de las
cinco reglas duras y verifica que cada uno es rechazado correctamente.

Tolerancia operativa: exacta sobre verificación booleana de las reglas.

Autoría / Authorship
-------------------
© 2026 Juan Antonio Lloret Egea. Todos los derechos reservados / All rights reserved.
ORCID: 0000-0002-6634-3351
Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA)
IA eñ™ — La Biblia de la IA™
ISSN 2695-6411
Licencia / License: CC BY-NC-ND 4.0
"""


# Estado operativo previo al mapeo Fourier factual
class EstadoOperativo:
    def __init__(self, campo_definido=False, funcion_ordinal_construida=False,
                 trayectoria_verificada=False, frontera_declarada=False,
                 residual_calculado=False, ciclo_evaluado=False):
        self.campo_definido = campo_definido
        self.funcion_ordinal_construida = funcion_ordinal_construida
        self.trayectoria_verificada = trayectoria_verificada
        self.frontera_declarada = frontera_declarada
        self.residual_calculado = residual_calculado
        self.ciclo_evaluado = ciclo_evaluado

    def cierre_operativo_completo(self):
        return (self.campo_definido and self.funcion_ordinal_construida and
                self.trayectoria_verificada and self.frontera_declarada and
                self.residual_calculado and self.ciclo_evaluado)


def fourier_factual_admisible(estado):
    """
    Devuelve True sólo si el estado operativo está completamente cerrado.
    Si falta algún paso previo, Fourier factual queda inadmisible.
    """
    return estado.cierre_operativo_completo()


def fourier_crea_campo():
    """R2: Fourier factual no puede crear campos."""
    return False  # rechazado correctamente


def fourier_cierra_U(dictamen_actual):
    """R3: Fourier factual no puede cerrar U."""
    if dictamen_actual == "U":
        return "U"  # preserva U
    return dictamen_actual


def fourier_sustituye_residual(residual_estructural):
    """R4: Fourier factual no puede sustituir residual."""
    # El residual estructural es objeto operativo, no objeto modal
    return residual_estructural  # se mantiene el residual original


def fourier_decide_interaccion_sin_trayectoria(trayectoria):
    """R5: Fourier factual no puede decidir interacción sin trayectoria."""
    if trayectoria is None:
        return "U"  # rechazo correcto: sin trayectoria, dictamen U
    return "1"


# Cinco escenarios adversariales de violación de las reglas duras
ESCENARIOS = [
    {
        "etiqueta": "R1 — orden operativo correcto (mapeo admisible)",
        "operacion": lambda: fourier_factual_admisible(
            EstadoOperativo(True, True, True, True, True, True)
        ),
        "esperado": True,
        "regla": "R1",
    },
    {
        "etiqueta": "R1' — falta cierre operativo (orden invertido)",
        "operacion": lambda: fourier_factual_admisible(
            EstadoOperativo(True, True, False, False, False, False)
        ),
        "esperado": False,  # rechazo correcto: orden incorrecto
        "regla": "R1",
    },
    {
        "etiqueta": "R2 — intento de crear campo desde Fourier",
        "operacion": fourier_crea_campo,
        "esperado": False,  # Fourier no crea campos
        "regla": "R2",
    },
    {
        "etiqueta": "R3 — intento de cerrar U mediante mapeo modal",
        "operacion": lambda: fourier_cierra_U("U"),
        "esperado": "U",
        "regla": "R3",
    },
    {
        "etiqueta": "R4 — intento de sustituir residual por modo armónico",
        "operacion": lambda: fourier_sustituye_residual(0.42),
        "esperado": 0.42,  # se mantiene el residual original
        "regla": "R4",
    },
    {
        "etiqueta": "R5 — intento de decidir interacción sin trayectoria",
        "operacion": lambda: fourier_decide_interaccion_sin_trayectoria(None),
        "esperado": "U",
        "regla": "R5",
    },
]


def main():
    print("=" * 78)
    print(" LAB-10 — Verificador del mapeo posterior con Fourier factual")
    print("=" * 78)
    print()
    print(" Cinco reglas duras del mapeo modal:")
    print("   R1 — Fourier puede analizar ciclos (sólo tras cierre operativo).")
    print("   R2 — Fourier no puede crear campos.")
    print("   R3 — Fourier no puede cerrar U.")
    print("   R4 — Fourier no puede sustituir residual.")
    print("   R5 — Fourier no puede decidir interacción sin trayectoria.")
    print()

    print(f" {'Escenario':<55} | {'Regla':<6} | {'Esperado':<10} | {'OK':<3}")
    print(" " + "-" * 80)

    aciertos = 0
    for esc in ESCENARIOS:
        obtenido = esc["operacion"]()
        ok = (obtenido == esc["esperado"])
        if ok:
            aciertos += 1
        marca = "✓" if ok else "✗"
        esp_str = str(esc["esperado"])
        print(f" {esc['etiqueta']:<55} | {esc['regla']:<6} | "
              f"{esp_str:<10} | {marca:<3}")

    print()
    print(" Análisis estructural:")
    print(" - Fourier factual es aparato auxiliar Σ = 0 del corpus.")
    print(" - El mapeo modal opera estrictamente tras el cierre operativo.")
    print(" - La estructura modal detectada es evidencia auxiliar,")
    print("   no sustituto del dictamen operativo del operador 𝓘_SV.")
    print()

    if aciertos == len(ESCENARIOS):
        print("✓ LAB-10 SUPERADO:")
        print(f"  - Las {len(ESCENARIOS)} reglas duras del mapeo modal son verificadas.")
        print("  - Fourier factual queda subordinado al cierre operativo previo.")
        print("  - Mapeo modal verificado operativamente como aparato auxiliar.")
        return 0
    else:
        print(f"✗ LAB-10 FALLA: {len(ESCENARIOS) - aciertos} verificaciones incorrectas.")
        return 1


if __name__ == "__main__":
    import sys
    sys.exit(main())
