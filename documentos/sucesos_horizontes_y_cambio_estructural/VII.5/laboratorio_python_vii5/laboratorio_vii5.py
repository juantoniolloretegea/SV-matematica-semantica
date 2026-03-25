=============================================================================
Laboratorio mínimo reproducible — VII.5
Enlace formal entre acumulaciones sucesivas en el Sistema Vectorial SV

Autor: Juan Antonio Lloret Egea
ORCID: 0000-0002-6634-3351
Serie doctrinal: Sistema Vectorial SV
ITVIA / IA eñ™ — La Biblia de la IA™
ISSN: 2695-6411 | Madrid, 25 de marzo de 2026
=============================================================================

Este laboratorio cubre los problemas propios de VII.5:

  - Problema 1: formalización mínima del dato de enlace Λ como triple
                (J_Λ, Θ_Λ, Π_Λ) entre acumulación previa y acumulación
                sucesiva.
  - Problema 2: tipificación operativa de los cinco dictámenes básicos:
                separación, enlace débil, reinicialización pura,
                reinicialización con memoria y enlace fuerte.
  - Problema 3: verificación de condiciones mínimas de existencia y
                no existencia del enlace formal entre acumulaciones
                sucesivas.
  - Problema 4: reproducción del ejemplo canónico sobre SV(9,3),
                con junta tipada, transporte parcial y proyección
                aceptable hacia la acumulación sucesiva.
  - Problema 5: validación operativa básica mediante aserciones, para
                asegurar que el dictamen obtenido coincide con la
                tipología declarada en el manuscrito.

El laboratorio NO pretende:
  - cerrar una teoría general de memoria estructural;
  - constituir backend soberano ni IR;
  - formalizar aún una semántica completa de herencia entre regímenes;
  - ni sustituir la futura disciplina algebraica más fuerte del enlace.

Sí ilustra con SV(9,3) el núcleo tipado del enlace formal entre
acumulaciones sucesivas en el Sistema Vectorial SV.
=============================================================================
from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List, Optional, Sequence, Set

SIGMA = {0, 1, 'U'}


@dataclass(frozen=True)
class CeldaSV:
    """Célula canónica SV(9,3) para el laboratorio acompañante de VII.5."""

    valores: Sequence[object]
    b: int = 3

    def __post_init__(self) -> None:
        if len(self.valores) != 9:
            raise ValueError('Este laboratorio se restringe a SV(9,3).')
        if any(v not in SIGMA for v in self.valores):
            raise ValueError('Los valores admisibles son 0, 1 y U.')

    @property
    def soporte(self) -> List[str]:
        return [f'P{i}' for i in range(1, 10)]


@dataclass(frozen=True)
class DatoEnlace:
    dominio: Set[str]
    transporte: Dict[str, str]
    proyeccion: Dict[str, object]

    def validar(self, soporte_a: Set[str], soporte_b: Set[str], herederos_validos: Set[object]) -> None:
        if not self.dominio.issubset(soporte_a):
            raise ValueError('J_Lambda contiene posiciones fuera del soporte de A.')
        if set(self.transporte.keys()) - self.dominio:
            raise ValueError('Theta_Lambda sólo puede operar sobre el dominio declarado.')
        if any(destino not in soporte_b for destino in self.transporte.values()):
            raise ValueError('Theta_Lambda apunta a posiciones no válidas de B.')
        if set(self.proyeccion.keys()) - self.dominio:
            raise ValueError('Pi_Lambda sólo puede proyectar elementos del dominio declarado.')
        for valor in self.proyeccion.values():
            if valor != 0 and valor not in herederos_validos:
                raise ValueError(f'Valor de herencia no aceptable por R_B: {valor!r}')


def clasificar_enlace(lmbd: Optional[DatoEnlace], soporte_a: Set[str], soporte_b: Set[str], herederos_validos: Set[object]) -> str:
    if lmbd is None:
        return 'separacion_completa'

    lmbd.validar(soporte_a, soporte_b, herederos_validos)

    if not lmbd.dominio:
        return 'separacion_completa'

    transporte_no_vacio = bool(lmbd.transporte)
    proy_no_nula = any(v != 0 for v in lmbd.proyeccion.values())
    proyeccion_sobre_dominio = set(lmbd.proyeccion.keys()) == set(lmbd.dominio)
    transporte_coherente = set(lmbd.transporte.keys()).issubset(lmbd.dominio)
    herencia_no_nula = [v for v in lmbd.proyeccion.values() if v != 0]
    herencia_significativa = len(herencia_no_nula) >= max(2, len(lmbd.dominio) // 2)
    contiene_memoria_resumida = any(v == 'mu' for v in lmbd.proyeccion.values())
    contiene_no_herencia = any(v == 0 for v in lmbd.proyeccion.values())

    if not proy_no_nula:
        return 'reinicializacion_pura'

    if transporte_no_vacio and transporte_coherente and proyeccion_sobre_dominio and herencia_significativa and not contiene_memoria_resumida and not contiene_no_herencia:
        return 'enlace_fuerte'

    # Convención operativa prudencial: una proyección auxiliar no nula sin transporte
    # declarado no se eleva a continuidad ni a enlace fuerte; se rebaja al caso más pobre.
    if not transporte_no_vacio:
        return 'enlace_debil'

    return 'reinicializacion_con_memoria'


def ejemplo_sv93_reinicializacion_con_memoria() -> str:
    a = CeldaSV((0, 1, 0, 'U', 1, 0, 0, 'U', 0))
    b = CeldaSV((0, 'U', 0, 0, 1, 0, 0, 0, 1))
    soporte_a = set(a.soporte)
    soporte_b = set(b.soporte)
    herederos_validos = {0, 1, 'U', 'mu'}

    lmbd = DatoEnlace(
        dominio={'P2', 'P5', 'P8'},
        transporte={'P2': 'P2', 'P5': 'P5', 'P8': 'P9'},
        proyeccion={'P2': 0, 'P5': 1, 'P8': 'mu'},
    )
    return clasificar_enlace(lmbd, soporte_a, soporte_b, herederos_validos)


def pruebas_canonicas() -> None:
    soporte = {f'P{i}' for i in range(1, 10)}
    herederos_validos = {0, 1, 'U', 'mu', 'sigma'}

    # 1. Separación completa
    assert clasificar_enlace(None, soporte, soporte, herederos_validos) == 'separacion_completa'

    # 2. Enlace débil: caso frontera con memoria auxiliar, pero sin transporte declarado.
    enlace_debil = DatoEnlace(dominio={'P1'}, transporte={}, proyeccion={'P1': 'mu'})
    assert clasificar_enlace(enlace_debil, soporte, soporte, herederos_validos) == 'enlace_debil'

    # 3. Reinicialización pura: transporte posible, pero proyección totalmente nula.
    reinicio_puro = DatoEnlace(dominio={'P2', 'P5'}, transporte={'P2': 'P2'}, proyeccion={'P2': 0, 'P5': 0})
    assert clasificar_enlace(reinicio_puro, soporte, soporte, herederos_validos) == 'reinicializacion_pura'

    # 4. Reinicialización con memoria: caso canónico del manuscrito.
    assert ejemplo_sv93_reinicializacion_con_memoria() == 'reinicializacion_con_memoria'

    # 5. Enlace fuerte: transporte parcial estable y herencia significativa sin cobertura total.
    fuerte = DatoEnlace(
        dominio={'P1', 'P2', 'P3', 'P5'},
        transporte={'P1': 'P1', 'P2': 'P2', 'P5': 'P5'},
        proyeccion={'P1': 1, 'P2': 'U', 'P3': 1, 'P5': 1},
    )
    assert clasificar_enlace(fuerte, soporte, soporte, herederos_validos) == 'enlace_fuerte'


if __name__ == '__main__':
    pruebas_canonicas()
    print('Laboratorio VII.5: verificación canónica completada correctamente.')
    print('Caso del manuscrito (SV(9,3)):', ejemplo_sv93_reinicializacion_con_memoria())
