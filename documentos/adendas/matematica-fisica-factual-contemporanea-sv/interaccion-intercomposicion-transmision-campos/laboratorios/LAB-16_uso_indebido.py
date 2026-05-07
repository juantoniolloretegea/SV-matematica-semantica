"""
LAB-16 — Verificador adversarial de uso indebido de d^{SV}_Φ
================================================================

Verifica computacionalmente las cinco prevenciones del apartado A.9 del
Anexo A, articuladas con los códigos de error E-11 a E-16:

    E-11: d^{SV}_Φ interpretada como tiempo (segundos, ms, etc.).
    E-12: d^{SV}_Φ interpretada como distancia espacial (metros).
    E-13: distancia factual calculada sin observable Φ declarado.
    E-14: distancia factual calculada sin trayectoria Γ declarada.
    E-15: distancia intercampo calculada sin trayectoria común.
    E-16: Fourier factual usado antes de cerrar distancia, residual y ciclo.

El laboratorio implementa seis intentos adversariales de violación, uno por
cada código de error, y verifica que cada uno es rechazado correctamente.

Tolerancia operativa: exacta sobre verificación booleana de las prevenciones.

Autoría / Authorship
-------------------
© 2026 Juan Antonio Lloret Egea. Todos los derechos reservados / All rights reserved.
ORCID: 0000-0002-6634-3351
Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA)
IA eñ™ — La Biblia de la IA™
ISSN 2695-6411
Licencia / License: CC BY-NC-ND 4.0
"""


# Unidades temporales y espaciales del SI (no admisibles para d^{SV}_Φ)
UNIDADES_TEMPORALES = ["s", "ms", "μs", "ns", "min", "h", "día", "año"]
UNIDADES_ESPACIALES = ["m", "cm", "mm", "km", "Å", "fm", "AU", "pc"]

# Cadena de cierre operativo previo al uso de Fourier factual
PASOS_CIERRE_PREVIO = [
    "campo_definido",
    "funcion_ordinal_construida",
    "trayectoria_verificada",
    "frontera_declarada",
    "residual_calculado",
    "ciclo_evaluado",
]


def E11_rechazo_temporal(unidad):
    """E-11: rechaza si la unidad es temporal."""
    if unidad in UNIDADES_TEMPORALES:
        return ("RECHAZADO", f"unidad '{unidad}' es temporal del SI")
    return ("ADMITIDO", "no temporal")


def E12_rechazo_espacial(unidad):
    """E-12: rechaza si la unidad es espacial."""
    if unidad in UNIDADES_ESPACIALES:
        return ("RECHAZADO", f"unidad '{unidad}' es espacial del SI")
    return ("ADMITIDO", "no espacial")


def E13_rechazo_sin_observable(observable_declarado):
    """E-13: rechaza si no hay observable declarado."""
    if observable_declarado is None:
        return ("RECHAZADO", "no hay observable Φ declarado por el horizonte")
    return ("ADMITIDO", f"observable declarado: {observable_declarado}")


def E14_rechazo_sin_trayectoria(trayectoria_declarada):
    """E-14: rechaza si no hay trayectoria declarada."""
    if trayectoria_declarada is None or len(trayectoria_declarada) == 0:
        return ("RECHAZADO", "no hay trayectoria Γ declarada")
    return ("ADMITIDO", f"trayectoria con {len(trayectoria_declarada)} sucesos")


def E15_rechazo_sin_trayectoria_comun(traj_a, traj_b):
    """E-15: rechaza si las trayectorias de los dos campos son distintas."""
    if traj_a != traj_b:
        return ("RECHAZADO", "trayectorias distintas: no admiten DistInter")
    return ("ADMITIDO", "trayectoria común")


def E16_rechazo_Fourier_prematuro(estado_cierre):
    """E-16: rechaza si Fourier factual se aplica sin cierre operativo previo."""
    pasos_completos = all(estado_cierre.get(paso, False) for paso in PASOS_CIERRE_PREVIO)
    if not pasos_completos:
        faltantes = [paso for paso in PASOS_CIERRE_PREVIO
                     if not estado_cierre.get(paso, False)]
        return ("RECHAZADO", f"faltan pasos previos: {faltantes}")
    return ("ADMITIDO", "cierre operativo completo, Fourier admisible")


def main():
    print("=" * 78)
    print(" LAB-16 — Verificador adversarial de uso indebido de d^{SV}_Φ")
    print("=" * 78)
    print()
    print(" Cinco prevenciones del apartado A.9 del Anexo A, con códigos E-11 a E-16.")
    print()

    # Seis escenarios adversariales
    escenarios = [
        # E-11: temporalización
        {
            "codigo": "E-11",
            "etiqueta": "Intento de expresar d^{SV}_Φ en segundos",
            "test": lambda: E11_rechazo_temporal("s"),
            "esperado": "RECHAZADO",
        },
        # E-12: espacialización
        {
            "codigo": "E-12",
            "etiqueta": "Intento de expresar d^{SV}_Φ en metros",
            "test": lambda: E12_rechazo_espacial("m"),
            "esperado": "RECHAZADO",
        },
        # E-13: sin observable
        {
            "codigo": "E-13",
            "etiqueta": "Cálculo sin observable Φ declarado",
            "test": lambda: E13_rechazo_sin_observable(None),
            "esperado": "RECHAZADO",
        },
        # E-14: sin trayectoria
        {
            "codigo": "E-14",
            "etiqueta": "Cálculo sin trayectoria Γ declarada",
            "test": lambda: E14_rechazo_sin_trayectoria(None),
            "esperado": "RECHAZADO",
        },
        # E-15: distancia intercampo sin trayectoria común
        {
            "codigo": "E-15",
            "etiqueta": "DistInter sobre trayectorias distintas",
            "test": lambda: E15_rechazo_sin_trayectoria_comun(
                ["S1", "S2", "S3"], ["S1", "S2", "S4"]),
            "esperado": "RECHAZADO",
        },
        # E-16: Fourier prematuro
        {
            "codigo": "E-16",
            "etiqueta": "Fourier factual antes del cierre operativo",
            "test": lambda: E16_rechazo_Fourier_prematuro({
                "campo_definido": True,
                "funcion_ordinal_construida": True,
                "trayectoria_verificada": False,  # falta este paso
                "frontera_declarada": False,
                "residual_calculado": False,
                "ciclo_evaluado": False,
            }),
            "esperado": "RECHAZADO",
        },
    ]

    # Tres escenarios de control: lecturas correctas que deben ser admitidas
    escenarios_control = [
        {
            "codigo": "control E-11",
            "etiqueta": "d^{SV}_Φ sin unidad SI (uso correcto)",
            "test": lambda: E11_rechazo_temporal("adimensional"),
            "esperado": "ADMITIDO",
        },
        {
            "codigo": "control E-13",
            "etiqueta": "Cálculo con observable F_uno declarado",
            "test": lambda: E13_rechazo_sin_observable("F_uno"),
            "esperado": "ADMITIDO",
        },
        {
            "codigo": "control E-15",
            "etiqueta": "DistInter sobre trayectoria común",
            "test": lambda: E15_rechazo_sin_trayectoria_comun(
                ["S1", "S2", "S3"], ["S1", "S2", "S3"]),
            "esperado": "ADMITIDO",
        },
    ]

    print(f" {'Código':<13} | {'Escenario':<48} | {'Esperado':<10} | {'OK':<3}")
    print(" " + "-" * 80)

    aciertos = 0
    total = len(escenarios) + len(escenarios_control)

    for esc in escenarios + escenarios_control:
        resultado, motivo = esc["test"]()
        ok = (resultado == esc["esperado"])
        if ok:
            aciertos += 1
        marca = "✓" if ok else "✗"
        print(f" {esc['codigo']:<13} | {esc['etiqueta']:<48} | "
              f"{esc['esperado']:<10} | {marca:<3}")
        if not ok:
            print(f"     · {motivo}")

    print()
    print(" Análisis estructural:")
    print(" - d^{SV}_Φ no se expresa en unidades SI (E-11, E-12).")
    print(" - El cálculo exige observable y trayectoria declarados (E-13, E-14).")
    print(" - DistInter exige trayectoria común (E-15).")
    print(" - Fourier factual sólo opera tras el cierre operativo completo (E-16).")
    print(" - Los tres controles confirman que las admisiones legítimas no son rechazadas.")
    print()

    if aciertos == total:
        print("✓ LAB-16 SUPERADO:")
        print(f"  - Las 6 prevenciones (E-11 a E-16) son rechazadas correctamente.")
        print(f"  - Los 3 controles legítimos son admitidos correctamente.")
        print("  - Apartado A.9 del Anexo A verificado operativamente.")
        return 0
    else:
        print(f"✗ LAB-16 FALLA: {total - aciertos} verificaciones incorrectas.")
        return 1


if __name__ == "__main__":
    import sys
    sys.exit(main())
