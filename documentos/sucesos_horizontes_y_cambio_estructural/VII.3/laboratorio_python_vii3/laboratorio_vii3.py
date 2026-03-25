"""
=============================================================================
Laboratorio mínimo reproducible — VII.3
Cadenas, acumulación y regímenes de paso en el Sistema Vectorial SV

Autor: Juan Antonio Lloret Egea
ORCID: 0000-0002-6634-3351
Serie doctrinal: Sistema Vectorial SV
ITVIA / IA eñ™ — La Biblia de la IA™
ISSN: 2695-6411 | Madrid, 25 de marzo de 2026
=============================================================================

Módulo mínimo reproducible. Cubre los cuatro ejemplos de la sección 8:
  - Ejemplo I   : cadena legítima finita en SV(9,3)
  - Ejemplo II  : pseudoacumulación ilegítima
  - Ejemplo III : paso de régimen estable a singular
  - Ejemplo IV  : respuesta estructural a suceso de horizonte

El laboratorio NO pretende:
  - reconstrucción geométrica completa
  - integración con backend soberano
  - validación lingüística final del Lenguaje SV

Sí permite:
  - declarar una célula SV(9,3) con espacio ternario Σ = {0, 1, U}
  - definir sucesos admisibles tipados
  - verificar si una familia constituye cadena legítima (C1–C4)
  - aplicar regla de actualización y detectar régimen de paso
=============================================================================
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Callable, Any
import textwrap

# ---------------------------------------------------------------------------
# 1. Espacio ternario y célula SV(9,3)
# ---------------------------------------------------------------------------

TERNARIO = {0, 1, "U"}  # Σ = {0, 1, U}
N_POSICIONES = 9        # dimensión de SV(9,3)
N_GRUPOS = 3            # tres grupos estructurales de lectura


def validar_vector(v: tuple) -> bool:
    """Verifica que v sea un vector ternario de longitud 9."""
    if len(v) != N_POSICIONES:
        return False
    return all(x in TERNARIO for x in v)


@dataclass
class CeldaSV:
    """
    Célula SV(n, b).  Por defecto: SV(9, 3).
    El vector de lectura vive en Σ^9 = {0, 1, U}^9.
    """
    n: int = 9
    b: int = 3
    vector: tuple = field(default_factory=lambda: tuple([0] * 9))
    horizonte: str = "H0"

    def __post_init__(self):
        if not validar_vector(self.vector):
            raise ValueError(f"Vector inválido: {self.vector}. Debe ser de longitud 9 con valores en {{0,1,U}}.")

    def grupos(self) -> list[tuple]:
        """Devuelve los b grupos de lectura (partición equitativa)."""
        paso = self.n // self.b
        return [self.vector[i * paso:(i + 1) * paso] for i in range(self.b)]

    def aplicar_reevaluacion(self, pos: int, nuevo_valor) -> "CeldaSV":
        """Devuelve nueva célula con la posición `pos` (0-indexed) actualizada."""
        if nuevo_valor not in TERNARIO:
            raise ValueError(f"Valor {nuevo_valor} no pertenece a Σ.")
        v = list(self.vector)
        v[pos] = nuevo_valor
        return CeldaSV(self.n, self.b, tuple(v), self.horizonte)

    def __repr__(self):
        grps = self.grupos()
        gstr = " | ".join(str(g) for g in grps)
        return f"SV({self.n},{self.b}) [{gstr}]  H={self.horizonte}"


# ---------------------------------------------------------------------------
# 2. Suceso admisible
# ---------------------------------------------------------------------------

@dataclass
class SucesoAdmisible:
    """
    Suceso admisible en el sentido de VII.1.

    Atributos:
      nombre       : etiqueta del suceso (ej. "e1")
      posiciones   : soporte σ(e) ⊆ {0,…,8}  (0-indexed)
      cambios      : dict {pos: nuevo_valor}  para la reevaluación
      horizonte_in : horizonte de partida
      horizonte_out: horizonte resultante
      observable   : etiqueta de la familia de observables relevantes
    """
    nombre: str
    posiciones: frozenset
    cambios: dict
    horizonte_in: str
    horizonte_out: str
    observable: str = "F_default"

    def aplicar(self, celda: CeldaSV) -> CeldaSV:
        """Aplica el suceso a la célula y devuelve la nueva célula."""
        nueva = celda
        for pos, val in self.cambios.items():
            nueva = nueva.aplicar_reevaluacion(pos, val)
        nueva = CeldaSV(nueva.n, nueva.b, nueva.vector, self.horizonte_out)
        return nueva

    def __repr__(self):
        cambios_str = ", ".join(f"P{p+1}:{v}" for p, v in self.cambios.items())
        return (f"Suceso({self.nombre}: σ={{{','.join('P'+str(p+1) for p in sorted(self.posiciones))}}} "
                f"[{cambios_str}]  H:{self.horizonte_in}→{self.horizonte_out}  obs={self.observable})")


# ---------------------------------------------------------------------------
# 3. Verificación de cadena (C1–C4)
# ---------------------------------------------------------------------------

@dataclass
class ResultadoVerificacion:
    es_cadena: bool
    criterio_fallido: Optional[str] = None
    mensaje: str = ""


def verificar_par(ei: SucesoAdmisible, ej: SucesoAdmisible) -> ResultadoVerificacion:
    """
    Verifica los cuatro criterios de cadena para el par consecutivo (eᵢ, eⱼ).

    C1: composición local definible — los soportes no se solapan de forma que
        invalide la composición (aquí: σ(eⱼ) no altera lo que eᵢ dejó en U
        sin resolución posible). Criterio simplificado: intersección de soportes
        no produce conflicto de escritura simultánea sobre mismo parámetro
        en sentidos incompatibles.
    C2: horizonte_out(eᵢ) compatible con horizonte_in(eⱼ).
    C3: observable de eⱼ transportable desde eᵢ (misma familia o traducible).
    C4: criterio acumulativo mantenido (campo observable igual, proxy aquí).
    """
    # C1: composición local
    conflicto = ei.posiciones & ej.posiciones
    if conflicto:
        # Se permite solapamiento si los valores son coherentes (no exigimos disjunción),
        # pero sí exigimos que no haya cambio sobre U no resuelto.
        for pos in conflicto:
            v_ei = ei.cambios.get(pos)
            v_ej = ej.cambios.get(pos)
            if v_ei == "U" and v_ej == "U":
                return ResultadoVerificacion(
                    False, "C1",
                    f"Conflicto en P{pos+1}: ambos sucesos dejan valor U sin resolución."
                )

    # C2: compatibilidad de horizonte
    if ei.horizonte_out != ej.horizonte_in:
        return ResultadoVerificacion(
            False, "C2",
            f"Horizonte incompatible: {ei.nombre}.H_out={ei.horizonte_out} "
            f"!= {ej.nombre}.H_in={ej.horizonte_in}"
        )

    # C3: transporte de observables
    # Criterio proxy: misma familia de observables O existe traducción declarada.
    # Aquí se considera "transportable" si las familias son iguales o si ej.observable
    # está marcado como "_ajena_" (indicador de observable sin traducción).
    if ej.observable.startswith("_ajena_"):
        return ResultadoVerificacion(
            False, "C3",
            f"Observable de {ej.nombre} ({ej.observable}) es ajena al régimen: sin traducción formal."
        )

    # C4: criterio acumulativo
    # Proxy: la familia de observables debe ser la misma o una extensión compatible.
    if ei.observable != ej.observable and not ej.observable.startswith(ei.observable):
        return ResultadoVerificacion(
            False, "C4",
            f"Criterio acumulativo roto: {ei.nombre}.obs={ei.observable} "
            f"vs {ej.nombre}.obs={ej.observable}"
        )

    return ResultadoVerificacion(True, mensaje="Par válido: C1–C4 satisfechos.")


def verificar_cadena(sucesos: list[SucesoAdmisible]) -> tuple[bool, list[ResultadoVerificacion]]:
    """
    Verifica si la familia de sucesos constituye una cadena legítima.
    Devuelve (es_cadena, [ResultadoVerificacion por par]).
    """
    if len(sucesos) < 2:
        return True, []
    resultados = []
    for i in range(len(sucesos) - 1):
        r = verificar_par(sucesos[i], sucesos[i + 1])
        resultados.append(r)
        if not r.es_cadena:
            return False, resultados
    return True, resultados


# ---------------------------------------------------------------------------
# 4. Acumulación eventiva y régimen de paso
# ---------------------------------------------------------------------------

def phi_default(e: SucesoAdmisible, a_n: float) -> float:
    """
    Regla de actualización por defecto Φ:
    incremento proporcional al número de posiciones reevaluadas.
    Φ(e, Aₙ) = |σ(e)| * 0.4 + Aₙ * 0.05
    """
    return len(e.posiciones) * 0.4 + a_n * 0.05


@dataclass
class PasoAcumulacion:
    indice: int
    suceso: SucesoAdmisible
    a_n: float
    regimen: str
    nota: str = ""


def calcular_acumulacion(
    sucesos: list[SucesoAdmisible],
    phi: Callable = phi_default,
    a_inicial: float = 1.0,
) -> list[PasoAcumulacion]:
    """
    Calcula la acumulación eventiva A_n sobre una cadena.
    Si en algún paso el suceso rompe C3 o C4, el régimen pasa a SINGULAR.

    Retorna lista de PasoAcumulacion con A_n y régimen para cada paso.
    """
    pasos = []
    a_n = a_inicial
    regimen_actual = "ESTABLE"

    for i, e in enumerate(sucesos):
        if e.observable.startswith("_ajena_"):
            regimen_actual = "SINGULAR"
            pasos.append(PasoAcumulacion(
                i + 1, e, float("nan"), "SINGULAR",
                nota=f"Observable ajena sin traducción: Φ indefinida."
            ))
            break

        # C4 check: si el observable cambia incompatiblemente, singular
        if i > 0 and sucesos[i - 1].observable != e.observable \
                and not e.observable.startswith(sucesos[i - 1].observable):
            regimen_actual = "SINGULAR"
            pasos.append(PasoAcumulacion(
                i + 1, e, float("nan"), "SINGULAR",
                nota=f"Cambio de observable sin traducción: Φ ilegible."
            ))
            break

        if i == 0:
            # A₁ = Δ_{e₁}F (aquí: número de posiciones reevaluadas)
            a_n = float(len(e.posiciones))
            reg = "FINITO" if len(sucesos) <= 3 else "ESTABLE"
        else:
            delta = phi(e, a_n)
            a_n = a_n + delta
            reg = regimen_actual

        pasos.append(PasoAcumulacion(i + 1, e, round(a_n, 4), reg))

    return pasos


def clasificar_regimen_global(pasos: list[PasoAcumulacion]) -> str:
    """Clasifica el régimen global de la cadena."""
    regimenes = {p.regimen for p in pasos}
    if "SINGULAR" in regimenes:
        return "SINGULAR"
    if "ESTABLE" in regimenes:
        return "ESTABLE"
    return "FINITO"


# ---------------------------------------------------------------------------
# 5. Salida formateada
# ---------------------------------------------------------------------------

def imprimir_tabla(
    titulo: str,
    celda_inicial: CeldaSV,
    sucesos: list[SucesoAdmisible],
    phi: Callable = phi_default,
):
    """
    Imprime la tabla de cadena, magnitud acumulativa y régimen de paso.
    """
    sep = "─" * 72
    print(f"\n{'═'*72}")
    print(f"  {titulo}")
    print(f"{'═'*72}")
    print(f"  Célula inicial : {celda_inicial}")
    print(sep)

    # Verificación de cadena
    es_cadena, verificaciones = verificar_cadena(sucesos)
    print(f"\n  ▶ VERIFICACIÓN DE CADENA (C1–C4)")
    print(sep)
    for i, r in enumerate(verificaciones):
        estado = "✓" if r.es_cadena else "✗"
        print(f"  Par (e{i+1}, e{i+2}): {estado}  {r.mensaje}")
    if not es_cadena:
        print(f"\n  ✗ RESULTADO: No constituye cadena legítima.")
        for r in verificaciones:
            if not r.es_cadena:
                print(f"    Criterio fallido: {r.criterio_fallido} — {r.mensaje}")
        print(sep)
        return

    print(f"\n  ✓ RESULTADO: Cadena legítima. Todos los pares satisfacen C1–C4.")

    # Acumulación
    print(f"\n  ▶ ACUMULACIÓN EVENTIVA")
    print(sep)
    header = f"  {'n':>3}  {'Suceso':<10}  {'σ(e)':<16}  {'H_in→H_out':<20}  {'Obs':<14}  {'Aₙ':>8}  {'Régimen'}"
    print(header)
    print("  " + "·" * 68)

    pasos = calcular_acumulacion(sucesos, phi)
    for p in pasos:
        sigma_str = "{" + ",".join(f"P{pos+1}" for pos in sorted(p.suceso.posiciones)) + "}"
        h_str = f"{p.suceso.horizonte_in}→{p.suceso.horizonte_out}"
        a_str = f"{p.a_n:.4f}" if not (isinstance(p.a_n, float) and p.a_n != p.a_n) else "n/d"
        nota_str = f"  ← {p.nota}" if p.nota else ""
        print(f"  {p.indice:>3}  {p.suceso.nombre:<10}  {sigma_str:<16}  {h_str:<20}  "
              f"{p.suceso.observable:<14}  {a_str:>8}  {p.regimen}{nota_str}")

    regimen_global = clasificar_regimen_global(pasos)
    print(f"\n  ▶ RÉGIMEN GLOBAL: {regimen_global}")
    print(sep)


# ---------------------------------------------------------------------------
# 6. Ejemplos de la sección 8
# ---------------------------------------------------------------------------

def ejemplo_I():
    """
    Ejemplo I — cadena legítima finita en SV(9,3)
    Sección 8.1 de VII.3
    """
    celda = CeldaSV(vector=(0, "U", 0, 0, 0, 0, "U", 0, 0), horizonte="H1")

    e1 = SucesoAdmisible(
        nombre="e1",
        posiciones=frozenset([1]),        # P2 (0-indexed)
        cambios={1: 0},                   # P2: U → 0
        horizonte_in="H1", horizonte_out="H1",
        observable="F_reevaluacion"
    )
    e2 = SucesoAdmisible(
        nombre="e2",
        posiciones=frozenset([6]),        # P7
        cambios={6: 1},                   # P7: U → 1
        horizonte_in="H1", horizonte_out="H1",
        observable="F_reevaluacion"
    )
    e3 = SucesoAdmisible(
        nombre="e3",
        posiciones=frozenset([6]),        # P7
        cambios={6: 1},                   # P7: ajuste local (mismo valor)
        horizonte_in="H1", horizonte_out="H1",
        observable="F_reevaluacion"
    )

    imprimir_tabla("EJEMPLO I — Cadena legítima finita en SV(9,3)", celda, [e1, e2, e3])


def ejemplo_II():
    """
    Ejemplo II — pseudoacumulación ilegítima
    Sección 8.2 de VII.3
    """
    celda = CeldaSV(vector=(0, 0, 0, 0, 0, 0, 0, 0, 0), horizonte="H1")

    e1 = SucesoAdmisible(
        nombre="e1",
        posiciones=frozenset([0, 1]),     # P1, P2
        cambios={0: 1, 1: 0},
        horizonte_in="H1", horizonte_out="H1",
        observable="F_conectividad"
    )
    e2 = SucesoAdmisible(
        nombre="e2",
        posiciones=frozenset([4, 5]),     # P5, P6
        cambios={4: 1, 5: 0},
        horizonte_in="H1", horizonte_out="H1",
        observable="F_conectividad"
    )
    # e3 exige observable ajena de otro régimen — marcado con prefijo "_ajena_"
    e3 = SucesoAdmisible(
        nombre="e3",
        posiciones=frozenset([7]),        # P8
        cambios={7: 1},
        horizonte_in="H1", horizonte_out="H1",
        observable="_ajena_topologia"     # marcador de observable sin traducción
    )

    imprimir_tabla("EJEMPLO II — Pseudoacumulación ilegítima (observable ajena)", celda, [e1, e2, e3])


def ejemplo_III():
    """
    Ejemplo III — paso de régimen estable a singular por cambio de horizonte
    Sección 8.3 de VII.3
    """
    celda = CeldaSV(vector=(0, 0, "U", 0, 0, 0, "U", 0, 0), horizonte="H1")

    e1 = SucesoAdmisible(
        nombre="e1", posiciones=frozenset([2]), cambios={2: 0},
        horizonte_in="H1", horizonte_out="H1", observable="F_local"
    )
    e2 = SucesoAdmisible(
        nombre="e2", posiciones=frozenset([6]), cambios={6: 1},
        horizonte_in="H1", horizonte_out="H1", observable="F_local"
    )
    e3 = SucesoAdmisible(
        nombre="e3", posiciones=frozenset([3]), cambios={3: 1},
        horizonte_in="H1", horizonte_out="H1", observable="F_local"
    )
    # e4 introduce un cambio de horizonte: H1 → H2
    # El suceso de horizonte rompe la compatibilidad H_out(e3) != H_in(e4)
    e4 = SucesoAdmisible(
        nombre="e4", posiciones=frozenset([0, 8]), cambios={0: 1, 8: 1},
        horizonte_in="H2",   # <-- horizonte cambiado, incompatible con H_out(e3)=H1
        horizonte_out="H2",
        observable="F_local"
    )

    imprimir_tabla(
        "EJEMPLO III — Paso de régimen estable a singular (cambio de horizonte)",
        celda, [e1, e2, e3, e4]
    )


def ejemplo_IV():
    """
    Ejemplo IV — respuesta estructural a suceso de horizonte
    Sección 8.4 de VII.3

    Este ejemplo muestra las cuatro respuestas posibles (R1–R4) ante un
    suceso de horizonte e*. VII.3 delimita el problema; no lo cierra.
    La respuesta R4 (reevaluación envolvente) queda reservada para VII.4.
    """
    print(f"\n{'═'*72}")
    print(f"  EJEMPLO IV — Respuesta estructural a suceso de horizonte")
    print(f"{'═'*72}")
    print(textwrap.dedent("""
  Cadena estable inicial bajo H1: e1, e2, e3 (régimen estable verificado).
  Suceso e* altera el horizonte: H1 → H2, sin destruir la legibilidad completa.

  Cuatro respuestas estructurales posibles (sección 8.4 / Figura 4):

  R1 — Prolongar bajo nueva regla Φ′
       La cadena continúa con H2 y Φ′ bien tipada para H2.
       Requiere: Φ′ definida y observable de H2 transportable.

  R2 — Nueva cadena independiente
       e* cierra la cadena previa. A(e1,e2,e3) queda congelada.
       Nueva cadena e′₁, e′₂,… parte de cero bajo H2.

  R3 — Detener acumulación
       A(e1,e2,e3) queda como registro cerrado.
       e* no genera nueva acumulación por falta de Φ bajo H2.

  R4 — Reevaluación envolvente [RESERVADA PARA VII.4]
       e* exige reconsiderar la cadena previa bajo H2.
       No formalizable en VII.3. Apertura estructural hacia VII.4.

  ─────────────────────────────────────────────────────────────────────────
  Nota: VII.3 delimita el problema. No lo cierra.
  Lo decisivo no es el orden temporal de e*, sino su capacidad para
  alterar el horizonte, la comparabilidad y la legitimidad de Φ.
  (Proposición 5 de VII.3)
  ─────────────────────────────────────────────────────────────────────────
    """))

    # Simular la cadena previa estable
    celda = CeldaSV(vector=(0, 0, "U", 0, 0, 0, "U", 0, 0), horizonte="H1")
    e1 = SucesoAdmisible(
        nombre="e1", posiciones=frozenset([2]), cambios={2: 0},
        horizonte_in="H1", horizonte_out="H1", observable="F_local"
    )
    e2 = SucesoAdmisible(
        nombre="e2", posiciones=frozenset([6]), cambios={6: 1},
        horizonte_in="H1", horizonte_out="H1", observable="F_local"
    )
    e3 = SucesoAdmisible(
        nombre="e3", posiciones=frozenset([3]), cambios={3: 1},
        horizonte_in="H1", horizonte_out="H1", observable="F_local"
    )

    print("  ▶ Cadena previa bajo H1:")
    imprimir_tabla("Cadena previa e1,e2,e3 (H1)", celda, [e1, e2, e3])

    print(textwrap.dedent("""
  ▶ Suceso de horizonte e* (H1 → H2):
    σ(e*) = {P1, P5}  ·  H_in=H1  ·  H_out=H2
    La cadena previa queda congelada con A(e1,e2,e3) válida.
    Las respuestas R1–R4 quedan delimitadas, no cerradas en VII.3.
    """))


# ---------------------------------------------------------------------------
# 7. Ejecución principal
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("=" * 72)
    print("  LABORATORIO MÍNIMO REPRODUCIBLE — VII.3")
    print("  Sistema Vectorial SV | ITVIA / IA eñ™")
    print("=" * 72)

    ejemplo_I()
    ejemplo_II()
    ejemplo_III()
    ejemplo_IV()

    print(f"\n{'═'*72}")
    print("  Fin del laboratorio VII.3")
    print(f"{'═'*72}\n")
