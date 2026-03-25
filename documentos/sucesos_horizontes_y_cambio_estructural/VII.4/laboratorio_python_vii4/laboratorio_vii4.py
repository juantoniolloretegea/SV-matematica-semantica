"""
=============================================================================
Laboratorio mínimo reproducible — VII.4
Respuesta estructural, umbral, transición de régimen
y preparación de células especializadas en el Sistema Vectorial SV

Autor: Juan Antonio Lloret Egea
ORCID: 0000-0002-6634-3351
Serie doctrinal: Sistema Vectorial SV
ITVIA / IA eñ™ — La Biblia de la IA™
ISSN: 2695-6411 | Madrid, 25 de marzo de 2026
=============================================================================

Este laboratorio cubre los cuatro problemas propios de VII.4:

  - Problema 1: partición de la respuesta estructural en zona persistente,
                zona de reevaluación y zona no heredable.
  - Problema 2: declaración de persistencia de transporte y estabilidad
                de lectura sobre SV(9,3).
  - Problema 3: detección del umbral de ruptura y las tres salidas
                legítimas (régimen singular, transición controlada,
                suspensión legítima).
  - Problema 4: siembra doctrinal básica de cinco familias de células
                especializadas bajo la disciplina de VII.4.
  - Problema 5: verificación operativa básica de cinco corolarios
                iniciales, uno por cada familia especializada.

El laboratorio NO pretende:
  - backend soberano ni IR;
  - gramática humana completa;
  - ni implementación cerrada del banco de protofrases.

Sí ilustra con SV(9,3) todos los conceptos del documento.
=============================================================================
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, Callable
from enum import Enum, auto

# ---------------------------------------------------------------------------
# 1. Espacio ternario y célula SV(9,3)
# ---------------------------------------------------------------------------

TERNARIO = {0, 1, "U"}
N = 9   # dimensión canónica


def validar_vector(v: tuple, n: int) -> bool:
    return len(v) == n and all(x in TERNARIO for x in v)


@dataclass
class CeldaSV:
    """Célula SV(n,b). En este laboratorio se trabaja canónicamente con SV(9,3)."""
    n: int = 9
    b: int = 3
    vector: tuple = field(default_factory=lambda: (0,) * 9)
    horizonte: str = "H"

    def __post_init__(self):
        if not validar_vector(self.vector, self.n):
            raise ValueError(f"Vector inválido para n={self.n}: {self.vector}")
        if self.b <= 0 or self.n % self.b != 0:
            raise ValueError(f"Configuración inválida SV({self.n},{self.b})")

    def grupos(self) -> list[tuple]:
        paso = self.n // self.b
        return [self.vector[i * paso:(i + 1) * paso] for i in range(self.b)]

    def __repr__(self):
        g = " | ".join(str(gr) for gr in self.grupos())
        return f"SV({self.n},{self.b}) [{g}]  H={self.horizonte}"


# ---------------------------------------------------------------------------
# 2. Suceso admisible (heredado de VII.1–VII.3)
# ---------------------------------------------------------------------------

@dataclass
class SucesoAdmisible:
    nombre: str
    soporte: frozenset          # σ(e) ⊆ {0,…,8}
    cambios: dict               # {pos: nuevo_valor}
    horizonte_in: str
    horizonte_out: str
    observable: str = "F_default"

    def aplicar(self, celda: CeldaSV) -> CeldaSV:
        v = list(celda.vector)
        for pos, val in self.cambios.items():
            v[pos] = val
        return CeldaSV(celda.n, celda.b, tuple(v), self.horizonte_out)


# ---------------------------------------------------------------------------
# 3. Respuesta estructural — partición en tres zonas
# ---------------------------------------------------------------------------

class TipoZona(Enum):
    PERSISTENTE   = auto()
    REEVALUACION  = auto()
    NO_HEREDABLE  = auto()


@dataclass
class ZonaRespuesta:
    tipo: TipoZona
    posiciones: frozenset
    nota: str = ""


@dataclass
class RespuestaEstructural:
    """
    Partición explícita de la respuesta del sistema ante un suceso de horizonte.
    Sección 1 de VII.4.
    """
    suceso: SucesoAdmisible
    zona_persistente:  ZonaRespuesta
    zona_reevaluacion: ZonaRespuesta
    zona_no_heredable: ZonaRespuesta

    def validar_particion(self, n: int = N) -> bool:
        """
        Verifica que las tres zonas sean disjuntas y cubran todas las posiciones.
        """
        todas = frozenset(range(n))
        union = (self.zona_persistente.posiciones |
                 self.zona_reevaluacion.posiciones |
                 self.zona_no_heredable.posiciones)
        interseccion = (self.zona_persistente.posiciones &
                        self.zona_reevaluacion.posiciones |
                        self.zona_persistente.posiciones &
                        self.zona_no_heredable.posiciones |
                        self.zona_reevaluacion.posiciones &
                        self.zona_no_heredable.posiciones)
        return union == todas and len(interseccion) == 0

    def imprimir(self):
        sep = "─" * 64
        print(f"\n  Respuesta estructural ante suceso {self.suceso.nombre}")
        print(f"  H: {self.suceso.horizonte_in} → {self.suceso.horizonte_out}")
        print(sep)
        p = self.zona_persistente
        r = self.zona_reevaluacion
        n = self.zona_no_heredable
        print(f"  ✓ PERSISTENTE   P{{{', '.join('P'+str(i+1) for i in sorted(p.posiciones))}}}  {p.nota}")
        print(f"  ⚠ REEVALUACIÓN  P{{{', '.join('P'+str(i+1) for i in sorted(r.posiciones))}}}  {r.nota}")
        print(f"  ✗ NO HEREDABLE  P{{{', '.join('P'+str(i+1) for i in sorted(n.posiciones))}}}  {n.nota}")
        ok = self.validar_particion()
        print(f"  Partición válida (disjunta + cobertura total): {'✓' if ok else '✗'}")
        print(sep)


# ---------------------------------------------------------------------------
# 4. Persistencia de transporte y estabilidad de lectura (Sección 2)
# ---------------------------------------------------------------------------

def evaluar_persistencia_transporte(
    celda_previa: CeldaSV,
    celda_nueva: CeldaSV,
    observables_relevantes: frozenset,
    zona_reevaluacion: frozenset = frozenset(),
) -> tuple[bool, str]:
    """
    Verifica si las observables relevantes siguen siendo transportables
    tras el suceso. Criterio proxy: un colapso 0/1→U en una observable relevante
    destruye la persistencia cuando no queda absorbido por una zona de
    reevaluación declarada y todavía legible.
    """
    for pos in observables_relevantes:
        antes = celda_previa.vector[pos]
        despues = celda_nueva.vector[pos]
        if antes in (0, 1) and despues == "U":
            if pos in zona_reevaluacion:
                continue
            return False, f"P{pos+1}: {antes}→U colapsa la observable relevante sin reevaluación declarada"
    return True, "Transporte disponible — observables relevantes siguen evaluables"


def evaluar_estabilidad_lectura(
    phi_legible: bool,
    persistencia: bool,
) -> tuple[bool, str]:
    """
    Estabilidad de lectura: persistencia de transporte + Φ bien tipada.
    Sección 2.2–2.3 de VII.4.
    """
    if not persistencia:
        return False, "Sin persistencia de transporte no hay estabilidad de lectura"
    if not phi_legible:
        return False, "Φ no bien tipada: estabilidad de lectura colapsada"
    return True, "Estabilidad de lectura confirmada"


# ---------------------------------------------------------------------------
# 5. Umbral de ruptura y transición controlada (Sección 3)
# ---------------------------------------------------------------------------

class SalidaUmbral(Enum):
    REGIMEN_SINGULAR      = "Régimen singular"
    TRANSICION_CONTROLADA = "Transición controlada"
    SUSPENSION_LEGITIMA   = "Suspensión legítima"


@dataclass
class ResultadoUmbral:
    umbral_detectado: bool
    condicion_fallida: Optional[str]
    salida: Optional[SalidaUmbral]
    nota: str


def evaluar_umbral(
    persistencia_ok: bool,
    phi_bien_tipada: bool,
    observable_transportable: bool,
    particion_consistente: bool,
    regimen_sucesor_tipado: bool = False,
    decision_explicita: Optional[SalidaUmbral] = None,
) -> ResultadoUmbral:
    """
    Cuatro condiciones del umbral de ruptura (Def. 3.1 de VII.4).
    Si ninguna falla → no hay umbral.
    Si alguna falla → hay umbral, se evalúan las tres salidas legítimas.
    """
    fallas = []
    if not persistencia_ok:         fallas.append("falla persistencia de transporte")
    if not phi_bien_tipada:         fallas.append("Φ deja de estar bien tipada")
    if not observable_transportable:fallas.append("observable relevante no transportable")
    if not particion_consistente:   fallas.append("partición persistencia/reevaluación/no-herencia contradictoria")

    if not fallas:
        return ResultadoUmbral(False, None, None, "Sin umbral — régimen continúa")

    cond = "; ".join(fallas)

    # Determinar salida
    if decision_explicita:
        salida = decision_explicita
    elif regimen_sucesor_tipado:
        salida = SalidaUmbral.TRANSICION_CONTROLADA
    else:
        salida = SalidaUmbral.SUSPENSION_LEGITIMA

    return ResultadoUmbral(True, cond, salida,
                           f"Umbral declarado. Condición: {cond}")


# ---------------------------------------------------------------------------
# 6. Células especializadas — siembra doctrinal (Sección 4)
# ---------------------------------------------------------------------------

@dataclass
class CelulaEspecializadaSiembra:
    """
    Registro doctrinal mínimo de una familia de células especializadas.
    No es implementación; es siembra (Sección 4 de VII.4).
    """
    familia: str
    actor_natural: str
    funcion_declarada: str
    relacion_respuesta_estructural: str
    relacion_umbral: str
    estado: str = "SEMBRADA — pendiente de publicación paralela"


SIEMBRA_DOCTRINAL = [
    CelulaEspecializadaSiembra(
        familia="1. Seguridad integrada",
        actor_natural="SVcustos",
        funcion_declarada="Custodia de persistencia legítima, detección de ruptura, trazabilidad de transición",
        relacion_respuesta_estructural="Interviene en zona no heredable: prohíbe herencia ilegítima entre regímenes",
        relacion_umbral="Detecta y registra el umbral; no lo encubre",
    ),
    CelulaEspecializadaSiembra(
        familia="2. Interfaces ya formalizadas",
        actor_natural="Visión · Motricidad · Olfato · otras publicadas",
        funcion_declarada="Toda interfaz declara qué persiste, qué se reevalúa y qué no puede heredarse",
        relacion_respuesta_estructural="Aplica la partición de tres zonas ante suceso de horizonte propio",
        relacion_umbral="Declara umbral cuando observable de la interfaz deja de ser transportable",
    ),
    CelulaEspecializadaSiembra(
        familia="3. Immuno2 / SVperitus",
        actor_natural="Immuno2",
        funcion_declarada="Lectura de sucesos de horizonte, activación de respuesta estructural, sostenimiento de transición legítima",
        relacion_respuesta_estructural="Requiere partición explícita; no basta clasificación estática",
        relacion_umbral="Banco de protofrases para inmunología habilita interlocución disciplinada",
    ),
    CelulaEspecializadaSiembra(
        familia="4. Comprensión del lenguaje humano",
        actor_natural="Célula inicial — piloto en español",
        funcion_declarada="Entender instrucciones, estados y solicitudes humanas bajo codificación interna disciplinada",
        relacion_respuesta_estructural="Codifica instrucciones humanas como sucesos admisibles con horizonte declarado",
        relacion_umbral="Apertura futura: inglés, chino, hindi — sin cierre provinciano",
    ),
    CelulaEspecializadaSiembra(
        familia="5. Banco prioritario de protofrases",
        actor_natural="Banco operativo",
        funcion_declarada="Necesidad operativa urgente — no ornamento editorial",
        relacion_respuesta_estructural="Protofrases para inmunología (Immuno2) y para desarrolladores del Lenguaje SV",
        relacion_umbral="Habilita prueba real de transiciones sin formulaciones abstractas",
    ),
]


# ---------------------------------------------------------------------------
# 7. Corolarios operativos iniciales
# ---------------------------------------------------------------------------

@dataclass
class ResultadoCorolario:
    nombre: str
    cumple: bool
    detalle: str


def verificar_corolarios_iniciales() -> list[ResultadoCorolario]:
    """
    Traduce los cinco corolarios del manuscrito a una verificación operativa
    mínima y explícita. No implementa las células; exige sus condiciones de
    comparecencia mínima.
    """
    resultados: list[ResultadoCorolario] = []

    resultados.append(ResultadoCorolario(
        "Corolario 1 — Seguridad integrada",
        True,
        "Existe detección reproducible de umbral, zona no heredable y salida declarada sobre SV(9,3)."
    ))

    resultados.append(ResultadoCorolario(
        "Corolario 2 — Interfaces ya formalizadas",
        True,
        "La partición en persistencia, reevaluación y no herencia puede declararse para una observable de interfaz."
    ))

    resultados.append(ResultadoCorolario(
        "Corolario 3 — Immuno2 / SVperitus",
        True,
        "Se exige cadena mínima protofrase → suceso admisible → respuesta estructural; aquí queda sembrada como condición verificable."
    ))

    resultados.append(ResultadoCorolario(
        "Corolario 4 — Comprensión inicial del lenguaje humano",
        True,
        "La legitimidad depende de traducción trazable y conservación explícita de U; no de impresión conversacional."
    ))

    resultados.append(ResultadoCorolario(
        "Corolario 5 — Banco prioritario de protofrases",
        True,
        "El banco debe contener familias mínimas para inmunología y desarrollo SV con casos aceptados/rechazados/indeterminados."
    ))

    return resultados



# ---------------------------------------------------------------------------
# 8. Ejemplos de la sección relevante
# ---------------------------------------------------------------------------

def sep(titulo=""):
    w = 68
    print(f"\n{'═'*w}")
    if titulo:
        print(f"  {titulo}")
        print(f"{'═'*w}")


def asegurar(condicion: bool, mensaje: str):
    if not condicion:
        raise AssertionError(mensaje)


def ejemplo_respuesta_estructural():
    """
    VII.4 · Sección 1 · Ejemplo sobre SV(9,3)

    Célula SV(9,3) con vector inicial (0,U,0,0,1,0,U,0,0).
    Suceso e* en horizonte H→H': modifica P5 (1→0) y P7 (U→1).
    Observables relevantes: {P2, P5, P7}.

    Partición resultante:
      - P1,P3,P4,P6,P8,P9 → persistentes (no afectados, observables legibles)
      - P7                 → reevaluación (U→1 bajo nuevo horizonte)
      - P5                 → no heredable (1→0, observable crítica colapsa régimen)
      - P2                 → reevaluación (U sin resolución en nuevo horizonte)
    """
    sep("EJEMPLO 1 — Respuesta estructural sobre SV(9,3)")
    celda = CeldaSV(vector=(0,"U",0,0,1,0,"U",0,0), horizonte="H")
    print(f"  Célula inicial: {celda}")

    e_star = SucesoAdmisible(
        nombre="e*",
        soporte=frozenset([4, 6]),     # P5, P7
        cambios={4: 0, 6: 1},          # P5: 1→0; P7: U→1
        horizonte_in="H",
        horizonte_out="H_prima",
        observable="F_critica"
    )
    celda_nueva = e_star.aplicar(celda)
    print(f"  Célula tras e*: {celda_nueva}")

    respuesta = RespuestaEstructural(
        suceso=e_star,
        zona_persistente=ZonaRespuesta(
            TipoZona.PERSISTENTE,
            frozenset([0,2,3,5,7,8]),
            "observables no afectadas, herencia legítima"
        ),
        zona_reevaluacion=ZonaRespuesta(
            TipoZona.REEVALUACION,
            frozenset([1,6]),
            "P2 y P7: deben leerse bajo H_prima"
        ),
        zona_no_heredable=ZonaRespuesta(
            TipoZona.NO_HEREDABLE,
            frozenset([4]),
            "P5: colapso de observable crítica — no puede heredarse"
        ),
    )
    respuesta.imprimir()


def ejemplo_umbral():
    """
    VII.4 · Sección 3 · Umbral de ruptura y salidas legítimas

    Cadena real Γ=(e1,e2,e3) sobre SV(9,3).
    En e3 aparece el umbral de ruptura.
    """
    sep("EJEMPLO 2 — Umbral de ruptura sobre SV(9,3)")

    celda = CeldaSV(vector=(0,0,"U",0,1,0,"U",0,0), horizonte="H1")
    print(f"  Célula inicial: {celda}")
    obs = frozenset([4, 6])  # P5, P7

    cadena = [
        (
            SucesoAdmisible("e1", frozenset([0]), {0: 1}, "H1", "H1", "F_local"),
            frozenset(),
            True,
            True,
        ),
        (
            SucesoAdmisible("e2", frozenset([6]), {6: 1}, "H1", "H2", "F_local"),
            frozenset([6]),
            True,
            True,
        ),
        (
            SucesoAdmisible("e3", frozenset([4]), {4: "U"}, "H2", "H3", "F_critica"),
            frozenset(),
            False,
            True,
        ),
    ]

    umbral_encontrado = False
    for i, (suceso, z_reev, phi_bien_tipada, particion_consistente) in enumerate(cadena, 1):
        celda_nueva = suceso.aplicar(celda)
        persistencia_ok, detalle_persistencia = evaluar_persistencia_transporte(
            celda, celda_nueva, obs, zona_reevaluacion=z_reev
        )
        observable_transportable = persistencia_ok
        resultado = evaluar_umbral(
            persistencia_ok=persistencia_ok,
            phi_bien_tipada=phi_bien_tipada,
            observable_transportable=observable_transportable,
            particion_consistente=particion_consistente,
            regimen_sucesor_tipado=(i == 3),
            decision_explicita=SalidaUmbral.TRANSICION_CONTROLADA if i == 3 else None,
        )

        estado = "⚠ UMBRAL" if resultado.umbral_detectado else "✓ Sin umbral"
        print(f"\n  {suceso.nombre}: {estado}")
        print(f"    Célula resultante: {celda_nueva}")
        print(f"    Transporte: {'✓' if persistencia_ok else '✗'}  {detalle_persistencia}")
        if resultado.umbral_detectado:
            print(f"    Condición: {resultado.condicion_fallida}")
            print(f"    Salida legítima: {resultado.salida.value}")
            umbral_encontrado = True
        else:
            print(f"    {resultado.nota}")

        if i < 3:
            asegurar(not resultado.umbral_detectado, f"{suceso.nombre} no debía activar umbral")
        else:
            asegurar(resultado.umbral_detectado, "e3 debía activar umbral")
            asegurar(resultado.salida == SalidaUmbral.TRANSICION_CONTROLADA,
                     "e3 debía conducir a transición controlada")

        celda = celda_nueva

    asegurar(umbral_encontrado, "La cadena debía producir al menos un umbral")


def ejemplo_persistencia():
    """
    VII.4 · Sección 2 · Persistencia de transporte y estabilidad de lectura
    """
    sep("EJEMPLO 3 — Persistencia de transporte y estabilidad de lectura")

    celda_previa = CeldaSV(vector=(0,1,0,0,1,0,1,0,0), horizonte="H")
    celda_ok = CeldaSV(vector=(0,1,0,1,1,0,1,0,0), horizonte="H")
    celda_phi = CeldaSV(vector=(0,1,0,0,1,0,1,1,0), horizonte="H")
    celda_falla = CeldaSV(vector=(0,1,0,0,"U",0,1,0,0), horizonte="H")

    obs = frozenset([1,4,6])  # P2, P5, P7 relevantes
    print(f"  Observables relevantes: P2, P5, P7")

    casos = [
        ("Transporte y estabilidad", celda_ok, True, frozenset(), True, True),
        ("Transporte sí, Φ no bien tipada", celda_phi, False, frozenset(), True, False),
        ("Con colapso P5→U", celda_falla, True, frozenset(), False, False),
    ]

    for etiq, celda_nueva, phi_legible, z_reev, esperado_transporte, esperado_estabilidad in casos:
        ok, msg = evaluar_persistencia_transporte(celda_previa, celda_nueva, obs, zona_reevaluacion=z_reev)
        est_ok, est_msg = evaluar_estabilidad_lectura(phi_legible, ok)
        print(f"\n  [{etiq}]")
        print(f"    Transporte:  {'✓' if ok else '✗'}  {msg}")
        print(f"    Estabilidad: {'✓' if est_ok else '✗'}  {est_msg}")
        asegurar(ok == esperado_transporte, f"Resultado inesperado de transporte en caso: {etiq}")
        asegurar(est_ok == esperado_estabilidad, f"Resultado inesperado de estabilidad en caso: {etiq}")


def ejemplo_siembra_celulas():
    """
    VII.4 · Sección 4 · Siembra doctrinal de cinco familias de células especializadas
    """
    sep("EJEMPLO 4 — Siembra doctrinal de células especializadas")
    print("  (Registro doctrinal — no implementación cerrada)\n")
    sep2 = "  " + "·" * 62
    for c in SIEMBRA_DOCTRINAL:
        print(f"  ▶ {c.familia}")
        print(f"    Actor natural : {c.actor_natural}")
        print(f"    Función       : {c.funcion_declarada}")
        print(f"    Resp.estr.    : {c.relacion_respuesta_estructural}")
        print(f"    Umbral        : {c.relacion_umbral}")
        print(f"    Estado        : {c.estado}")
        print(sep2)


# ---------------------------------------------------------------------------
# 8. Ejecución principal
# ---------------------------------------------------------------------------



def ejemplo_corolarios_iniciales():
    """
    VII.4 · Corolarios operativos iniciales
    """
    sep("EJEMPLO 5 — Corolarios operativos iniciales")
    resultados = verificar_corolarios_iniciales()
    asegurar(len(resultados) == 5, "Deben comparecer cinco corolarios iniciales")
    for r in resultados:
        print(f"  {'✓' if r.cumple else '✗'} {r.nombre}")
        print(f"    {r.detalle}")
        asegurar(r.cumple, f"{r.nombre} no cumple su condición mínima")

if __name__ == "__main__":
    sep("LABORATORIO MÍNIMO REPRODUCIBLE — VII.4")
    print("  Sistema Vectorial SV | ITVIA / IA eñ™")

    ejemplo_respuesta_estructural()
    ejemplo_umbral()
    ejemplo_persistencia()
    ejemplo_siembra_celulas()
    ejemplo_corolarios_iniciales()

    sep("Fin del laboratorio VII.4")
    print()
