"""
LAB-18 — Equivalencia de distancia global con divergencia de perfil local
=============================================================================
Potencia operativa de d^{SV}_Φ respecto al tiempo soberano

Este laboratorio verifica computacionalmente el caso extremo que articula
la potencia estructural de la distancia factual fibrosa local sobre el
tiempo: dos cadenas distintas con la misma distancia global D^{SV}_Φ(Γ)
pero con perfiles locales d^{SV}_Φ operativamente distintos.

Este caso es la firma diferencial entre el aparato del Sistema Vectorial
SV y la práctica heredada del tiempo soberano:

    - El tiempo trataría las dos cadenas como equivalentes por igualdad
      de variación neta extremo a extremo.
    - La distancia factual fibrosa las distingue como operativamente
      distintas por divergencia del perfil local de cambio.

El laboratorio:

    (A) Construye dos cadenas con D^{SV}_Φ idéntica pero perfiles distintos.
    (B) Verifica que D^{SV}_Φ coincide en ambas (insuficiencia del tiempo
        para distinguirlas).
    (C) Verifica que los perfiles locales son operativamente distintos
        (capacidad estructural de d^{SV}_Φ).
    (D) Calcula la distancia intercampo entre los perfiles para cuantificar
        la divergencia.
    (E) Calcula los defectos telescópicos para verificar que la firma
        estructural es captada.
    (F) Verifica un tercer caso con perfil aún más divergente con la
        misma D^{SV}_Φ.

Tolerancia operativa: D^{SV}_Φ idéntica + perfiles distintos + DistInter > 0.

Autoría / Authorship
-------------------
© 2026 Juan Antonio Lloret Egea. Todos los derechos reservados / All rights reserved.
ORCID: 0000-0002-6634-3351
Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA)
IA eñ™ — La Biblia de la IA™
ISSN 2695-6411
Licencia / License: CC BY-NC-ND 4.0
"""


def perfil_local(valores):
    """Perfil local d^{SV}_Φ sobre la cadena."""
    return [abs(valores[k+1] - valores[k]) for k in range(len(valores) - 1)]


def D_global(valores):
    """D^{SV}_Φ(Γ) = |Φ(S_r) − Φ(S_l)|."""
    return abs(valores[-1] - valores[0])


def DistInter(perfil_a, perfil_b):
    """DistInter sobre dos perfiles de igual longitud."""
    if len(perfil_a) != len(perfil_b):
        return float('inf')
    return sum(abs(a - b) for a, b in zip(perfil_a, perfil_b))


def defecto_telescopico(valores):
    """|D − Σd|. Cuando es 0, la cadena es telescópicamente coherente."""
    D = D_global(valores)
    suma = sum(perfil_local(valores))
    return abs(D - suma)


def main():
    print("=" * 78)
    print(" LAB-18 — Equivalencia de D^{SV}_Φ con divergencia de perfil local")
    print("=" * 78)
    print()
    print(" Caso extremo articulado por el apartado A.3 del Anexo A:")
    print("   Tiempo: insuficiente para distinguir dos cadenas con igual variación neta.")
    print("   d^{SV}_Φ: distingue por perfil local de cambio.")
    print()

    # Cadena A: monótona estricta. Φ valores: 0, 1, 2, 3, 4, 5
    cadena_A = [0, 1, 2, 3, 4, 5]
    # Cadena B: misma D global, perfil distinto (no monótona, ida y vuelta)
    cadena_B = [0, 3, 1, 4, 2, 5]
    # Cadena C: misma D global, perfil aún más divergente
    cadena_C = [0, 5, 0, 5, 0, 5]

    cadenas = [
        ("Cadena A (monótona)", cadena_A),
        ("Cadena B (no monótona moderada)", cadena_B),
        ("Cadena C (oscilación máxima)", cadena_C),
    ]

    print(" Tres cadenas distintas con la misma distancia global D^{SV}_Φ:")
    print()
    print(f" {'Cadena':<32} | {'Valores':<25} | {'D global':<8} | {'Σ d local':<10}")
    print(" " + "-" * 78)

    perfiles = {}
    D_globales = {}
    sumas_locales = {}

    for nombre, c in cadenas:
        D = D_global(c)
        p = perfil_local(c)
        s = sum(p)
        D_globales[nombre] = D
        perfiles[nombre] = p
        sumas_locales[nombre] = s
        print(f" {nombre:<32} | {str(c):<25} | {D:<8} | {s:<10}")

    print()

    # Bloque B: D global coincide
    D_A = D_globales["Cadena A (monótona)"]
    D_B = D_globales["Cadena B (no monótona moderada)"]
    D_C = D_globales["Cadena C (oscilación máxima)"]
    D_iguales = (D_A == D_B == D_C)
    print(f" BLOQUE B — D^{{SV}}_Φ idéntica en las tres cadenas: D_A = D_B = D_C = {D_A}")
    print(f"   {'✓' if D_iguales else '✗'} El tiempo trataría las tres cadenas como equivalentes.")
    print()

    # Bloque C: perfiles operativamente distintos
    p_A = perfiles["Cadena A (monótona)"]
    p_B = perfiles["Cadena B (no monótona moderada)"]
    p_C = perfiles["Cadena C (oscilación máxima)"]
    perfiles_distintos_AB = (p_A != p_B)
    perfiles_distintos_AC = (p_A != p_C)
    perfiles_distintos_BC = (p_B != p_C)
    todos_distintos = perfiles_distintos_AB and perfiles_distintos_AC and perfiles_distintos_BC

    print(f" BLOQUE C — Perfiles locales d^{{SV}}_Φ operativamente distintos:")
    print(f"   Perfil A: {p_A}")
    print(f"   Perfil B: {p_B}")
    print(f"   Perfil C: {p_C}")
    print(f"   {'✓' if todos_distintos else '✗'} d^{{SV}}_Φ distingue las tres cadenas por perfil local.")
    print()

    # Bloque D: distancia intercampo cuantifica la divergencia
    DI_AB = DistInter(p_A, p_B)
    DI_AC = DistInter(p_A, p_C)
    DI_BC = DistInter(p_B, p_C)
    print(f" BLOQUE D — Distancia intercampo entre perfiles:")
    print(f"   DistInter(A, B) = {DI_AB}")
    print(f"   DistInter(A, C) = {DI_AC}")
    print(f"   DistInter(B, C) = {DI_BC}")
    DI_positivos = (DI_AB > 0 and DI_AC > 0 and DI_BC > 0)
    print(f"   {'✓' if DI_positivos else '✗'} Las tres distancias intercampo son estrictamente positivas.")
    print()

    # Bloque E: defectos telescópicos
    Delta_A = defecto_telescopico(cadena_A)
    Delta_B = defecto_telescopico(cadena_B)
    Delta_C = defecto_telescopico(cadena_C)
    print(f" BLOQUE E — Defecto telescópico Δ^Φ_q de cada cadena:")
    print(f"   Δ^Φ_A = |D − Σd| = |{D_A} − {sumas_locales['Cadena A (monótona)']}| = {Delta_A}")
    print(f"   Δ^Φ_B = |D − Σd| = |{D_B} − {sumas_locales['Cadena B (no monótona moderada)']}| = {Delta_B}")
    print(f"   Δ^Φ_C = |D − Σd| = |{D_C} − {sumas_locales['Cadena C (oscilación máxima)']}| = {Delta_C}")
    print(f"   Cadena monótona A: defecto = 0 (Teorema T1).")
    print(f"   Cadenas no monótonas B, C: defecto > 0 (firma estructural).")
    defectos_correctos = (Delta_A == 0 and Delta_B > 0 and Delta_C > 0)
    print(f"   {'✓' if defectos_correctos else '✗'} La firma estructural del defecto distingue monotonía de no monotonía.")
    print()

    # Bloque F: caso extremo aún más divergente
    print(" BLOQUE F — Verificación del caso extremo (Cadena C):")
    print(f"   Cadena C oscilante: perfil = {p_C}")
    print(f"   Suma del perfil = {sum(p_C)} (mucho mayor que D = {D_C})")
    print(f"   El cambio acumulado es {sum(p_C) // D_C} veces mayor que el cambio neto.")
    extremo_OK = (sum(p_C) > D_C)
    print(f"   {'✓' if extremo_OK else '✗'} El caso extremo articula la potencia diferencial de d^{{SV}}_Φ.")
    print()

    # Síntesis
    todo_OK = (D_iguales and todos_distintos and DI_positivos
               and defectos_correctos and extremo_OK)

    print(" Análisis estructural:")
    print(" - Tres cadenas con la MISMA distancia global pero perfiles distintos.")
    print(" - El tiempo soberano no puede distinguirlas (sólo ve variación neta).")
    print(" - d^{SV}_Φ las distingue operativamente por perfil local.")
    print(" - DistInter cuantifica numéricamente la divergencia entre los perfiles.")
    print(" - El defecto telescópico Δ^Φ_q firma cada cadena por su tipo de cambio.")
    print(" - La tesis fuerte del apartado A.3 queda articulada operativamente:")
    print("   d^{SV}_Φ es estructuralmente más potente que el tiempo para el SV.")
    print()

    if todo_OK:
        print("✓ LAB-18 SUPERADO:")
        print("  - D global idéntica en las tres cadenas.")
        print("  - Perfiles locales operativamente distintos.")
        print("  - Distancias intercampo estrictamente positivas.")
        print("  - Firma del defecto telescópico verifica la diferencia estructural.")
        print("  - Potencia diferencial de d^{SV}_Φ respecto al tiempo confirmada.")
        return 0
    else:
        print("✗ LAB-18 FALLA: alguna verificación incorrecta.")
        return 1


if __name__ == "__main__":
    import sys
    sys.exit(main())
