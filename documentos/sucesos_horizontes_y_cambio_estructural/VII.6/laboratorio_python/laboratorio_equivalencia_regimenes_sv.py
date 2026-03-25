#!/usr/bin/env python3
"""
Laboratorio acompañante para el manuscrito:
Equivalencia parcial, preservación e invariancia local entre regímenes
en el Sistema Vectorial SV.

Carácter: subordinado, ilustrativo y verificable.
Ámbito: SV(9,3).
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Dict, Iterable, List, Optional, Sequence, Tuple

SIGMA = {0, 1, 'U'}


@dataclass(frozen=True)
class CeldaSV:
    valores: Tuple[object, ...]

    def __post_init__(self) -> None:
        if len(self.valores) != 9:
            raise ValueError('Este laboratorio se restringe a SV(9,3).')
        if any(v not in SIGMA for v in self.valores):
            raise ValueError(f'Valores no admitidos: {self.valores}')

    def valor_en(self, pos: str) -> object:
        idx = int(pos[1:]) - 1
        return self.valores[idx]

    def restriccion(self, posiciones: Sequence[str]) -> Tuple[object, ...]:
        return tuple(self.valor_en(p) for p in posiciones)

    def distribucion_alfabeto(self) -> Dict[object, int]:
        d: Dict[object, int] = {0: 0, 1: 0, 'U': 0}
        for v in self.valores:
            d[v] += 1
        return d


@dataclass(frozen=True)
class PropiedadRelevante:
    """
    Observable local tipado sobre un subdominio declarado.
    El evaluador recibe la restricción ordenada de la célula a dicho subdominio.
    """

    nombre: str
    subdominio: Tuple[str, ...]
    codominio: str
    evaluador: Callable[[Tuple[object, ...]], object]

    def evaluar(self, celda: CeldaSV, posiciones: Optional[Sequence[str]] = None) -> object:
        dominio = tuple(posiciones) if posiciones is not None else self.subdominio
        return self.evaluador(celda.restriccion(dominio))


@dataclass(frozen=True)
class DatoEnlace:
    dominio: Tuple[str, ...]
    transporte: Dict[str, str]
    proyeccion: Dict[str, object]


@dataclass
class ConfiguracionTriada:
    celda_a: CeldaSV
    celda_b: CeldaSV
    familia_propiedades: List[Tuple[PropiedadRelevante, PropiedadRelevante]]
    transporte: Dict[str, str]
    perdida_declarada: bool = False
    lambda_dato: Optional[DatoEnlace] = None
    comparabilidad_independiente: Optional[Callable[[CeldaSV, CeldaSV], bool]] = None


TRIADA = {
    'no_equivalencia': 'R_A ≁ R_B',
    'comparabilidad': 'R_A ⋈ R_B',
    'equivalencia_parcial': 'R_A ~_par R_B',
}


def _dominio_transportado(subdominio: Sequence[str], transporte: Dict[str, str]) -> Tuple[Tuple[str, ...], Tuple[str, ...]]:
    origen = tuple(p for p in subdominio if p in transporte)
    destino = tuple(transporte[p] for p in origen)
    return origen, destino


def transporte_coherente(prop_a: PropiedadRelevante, prop_b: PropiedadRelevante, transporte: Dict[str, str]) -> bool:
    origen, destino = _dominio_transportado(prop_a.subdominio, transporte)
    if not origen:
        return False
    return set(destino).issubset(set(prop_b.subdominio))


def preservacion(
    prop_a: PropiedadRelevante,
    celda_a: CeldaSV,
    prop_b: PropiedadRelevante,
    celda_b: CeldaSV,
    transporte: Dict[str, str],
) -> bool:
    """Compara valores de propiedades tipadas bajo transporte declarado."""
    if not transporte_coherente(prop_a, prop_b, transporte):
        return False
    origen, destino = _dominio_transportado(prop_a.subdominio, transporte)
    valor_a = prop_a.evaluar(celda_a, origen)
    valor_b = prop_b.evaluar(celda_b, destino)
    return valor_a == valor_b


def _cobertura_no_trivial(familia: List[Tuple[PropiedadRelevante, PropiedadRelevante]]) -> bool:
    union: set[str] = set()
    for prop_a, _ in familia:
        union.update(prop_a.subdominio)
    return len(union) >= 2


def invariancia_local(
    familia: List[Tuple[PropiedadRelevante, PropiedadRelevante]],
    celda_a: CeldaSV,
    celda_b: CeldaSV,
    transporte: Dict[str, str],
) -> bool:
    if not familia:
        return False
    if not _cobertura_no_trivial(familia):
        return False
    return all(
        preservacion(prop_a, celda_a, prop_b, celda_b, transporte)
        for prop_a, prop_b in familia
    )


def clasificar_triada(cfg: ConfiguracionTriada) -> str:
    hay_invariancia_local = invariancia_local(
        cfg.familia_propiedades,
        cfg.celda_a,
        cfg.celda_b,
        cfg.transporte,
    )

    if hay_invariancia_local and cfg.perdida_declarada:
        return 'equivalencia_parcial'

    alguna_preservada = any(
        preservacion(prop_a, cfg.celda_a, prop_b, cfg.celda_b, cfg.transporte)
        for prop_a, prop_b in cfg.familia_propiedades
    )

    comparabilidad_independiente = (
        cfg.comparabilidad_independiente is not None
        and cfg.comparabilidad_independiente(cfg.celda_a, cfg.celda_b)
    )

    if alguna_preservada or comparabilidad_independiente:
        return 'comparabilidad'

    return 'no_equivalencia'


# ─────────────────────────────────────────────
# Constructores de propiedades
# ─────────────────────────────────────────────


def prop_vector_igual(nombre: str, subdominio: Sequence[str]) -> PropiedadRelevante:
    return PropiedadRelevante(
        nombre=nombre,
        subdominio=tuple(subdominio),
        codominio='tupla_sigma',
        evaluador=lambda vals: tuple(vals),
    )


def prop_todo_uno(nombre: str, subdominio: Sequence[str]) -> PropiedadRelevante:
    return PropiedadRelevante(
        nombre=nombre,
        subdominio=tuple(subdominio),
        codominio='bool',
        evaluador=lambda vals: all(v == 1 for v in vals),
    )


def prop_sin_u(nombre: str, subdominio: Sequence[str]) -> PropiedadRelevante:
    return PropiedadRelevante(
        nombre=nombre,
        subdominio=tuple(subdominio),
        codominio='bool',
        evaluador=lambda vals: all(v != 'U' for v in vals),
    )


def prop_patron_exacto(nombre: str, subdominio: Sequence[str], patron: Tuple[object, ...]) -> PropiedadRelevante:
    return PropiedadRelevante(
        nombre=nombre,
        subdominio=tuple(subdominio),
        codominio='bool',
        evaluador=lambda vals: tuple(vals) == patron,
    )


# ─────────────────────────────────────────────
# Ejemplos canónicos del manuscrito
# ─────────────────────────────────────────────


def ejemplo_e1_comparabilidad_sin_lambda() -> str:
    a = CeldaSV((1, 1, 0, 0, 0, 0, 'U', 'U', 'U'))
    b = CeldaSV((0, 0, 'U', 1, 1, 0, 'U', 'U', 0))

    def comp_distribucion(ca: CeldaSV, cb: CeldaSV) -> bool:
        return ca.distribucion_alfabeto() == cb.distribucion_alfabeto()

    cfg = ConfiguracionTriada(
        celda_a=a,
        celda_b=b,
        familia_propiedades=[],
        transporte={},
        comparabilidad_independiente=comp_distribucion,
    )
    return clasificar_triada(cfg)


def ejemplo_e2_comparabilidad_puntual() -> str:
    a = CeldaSV((0, 1, 0, 'U', 1, 0, 0, 'U', 0))
    b = CeldaSV((0, 'U', 0, 0, 1, 0, 0, 0, 1))

    prop_a = prop_patron_exacto('P5_es_1_en_A', ('P5',), (1,))
    prop_b = prop_patron_exacto('P5_es_1_en_B', ('P5',), (1,))

    lmbd = DatoEnlace(
        dominio=('P2', 'P5', 'P8'),
        transporte={'P2': 'P2', 'P5': 'P5', 'P8': 'P9'},
        proyeccion={'P2': 0, 'P5': 1, 'P8': 'mu'},
    )

    cfg = ConfiguracionTriada(
        celda_a=a,
        celda_b=b,
        familia_propiedades=[(prop_a, prop_b)],
        transporte={'P5': 'P5'},
        perdida_declarada=False,
        lambda_dato=lmbd,
    )
    return clasificar_triada(cfg)


def ejemplo_e3_equivalencia_parcial() -> str:
    a = CeldaSV((1, 1, 1, 0, 0, 0, 'U', 'U', 'U'))
    b = CeldaSV((1, 1, 1, 'U', 'U', 'U', 0, 0, 0))

    prop_a1 = prop_todo_uno('bloque_superior_todo_1_en_A', ('P1', 'P2', 'P3'))
    prop_b1 = prop_todo_uno('bloque_superior_todo_1_en_B', ('P1', 'P2', 'P3'))
    prop_a2 = prop_sin_u('bloque_superior_sin_U_en_A', ('P1', 'P2', 'P3'))
    prop_b2 = prop_sin_u('bloque_superior_sin_U_en_B', ('P1', 'P2', 'P3'))

    cfg = ConfiguracionTriada(
        celda_a=a,
        celda_b=b,
        familia_propiedades=[(prop_a1, prop_b1), (prop_a2, prop_b2)],
        transporte={'P1': 'P1', 'P2': 'P2', 'P3': 'P3'},
        perdida_declarada=True,
    )
    return clasificar_triada(cfg)


def ejemplo_e4_identidad_vectorial_sin_identidad_regimen() -> str:
    a = CeldaSV((1, 0, 'U', 1, 0, 'U', 1, 0, 'U'))
    b = CeldaSV((1, 0, 'U', 1, 0, 'U', 1, 0, 'U'))

    cfg = ConfiguracionTriada(
        celda_a=a,
        celda_b=b,
        familia_propiedades=[],
        transporte={},
        perdida_declarada=False,
    )
    return clasificar_triada(cfg)


def ejemplo_e5_comparabilidad_independiente() -> str:
    a = CeldaSV(('U', 'U', 'U', 0, 0, 0, 1, 1, 1))
    b = CeldaSV(('U', 'U', 'U', 1, 1, 1, 0, 0, 0))

    def comp_distribucion(ca: CeldaSV, cb: CeldaSV) -> bool:
        return ca.distribucion_alfabeto() == cb.distribucion_alfabeto()

    cfg = ConfiguracionTriada(
        celda_a=a,
        celda_b=b,
        familia_propiedades=[],
        transporte={},
        comparabilidad_independiente=comp_distribucion,
    )
    return clasificar_triada(cfg)


# ─────────────────────────────────────────────
# Casos de borde
# ─────────────────────────────────────────────


def tesauro_t1_lambda_fuerte_no_basta() -> str:
    a = CeldaSV((1, 1, 1, 0, 0, 0, 'U', 'U', 'U'))
    b = CeldaSV((1, 1, 1, 0, 0, 0, 0, 0, 0))

    lmbd = DatoEnlace(
        dominio=('P1', 'P2', 'P3'),
        transporte={'P1': 'P1', 'P2': 'P2', 'P3': 'P3'},
        proyeccion={'P1': 1, 'P2': 1, 'P3': 1},
    )

    cfg = ConfiguracionTriada(
        celda_a=a,
        celda_b=b,
        familia_propiedades=[],
        transporte={},
        perdida_declarada=False,
        lambda_dato=lmbd,
    )
    return clasificar_triada(cfg)


def tesauro_t2_equivalencia_parcial_minima() -> str:
    a = CeldaSV((1, 1, 0, 0, 0, 0, 0, 0, 0))
    b = CeldaSV((1, 1, 'U', 'U', 'U', 'U', 'U', 'U', 'U'))

    prop_a = prop_vector_igual('bloque_P1P2_en_A', ('P1', 'P2'))
    prop_b = prop_vector_igual('bloque_P1P2_en_B', ('P1', 'P2'))

    cfg = ConfiguracionTriada(
        celda_a=a,
        celda_b=b,
        familia_propiedades=[(prop_a, prop_b)],
        transporte={'P1': 'P1', 'P2': 'P2'},
        perdida_declarada=True,
    )
    return clasificar_triada(cfg)


def tesauro_t3_no_equivalencia_pura() -> str:
    a = CeldaSV((1, 0, 0, 1, 0, 0, 1, 0, 0))
    b = CeldaSV((0, 0, 1, 0, 0, 1, 0, 0, 1))

    cfg = ConfiguracionTriada(
        celda_a=a,
        celda_b=b,
        familia_propiedades=[],
        transporte={},
    )
    return clasificar_triada(cfg)


def tesauro_t4_comparabilidad_por_propiedad_local() -> str:
    a = CeldaSV((0, 1, 0, 'U', 1, 0, 0, 'U', 0))
    b = CeldaSV((0, 'U', 0, 0, 1, 0, 0, 0, 1))

    prop_a = prop_patron_exacto('P5_igual_1_en_A', ('P5',), (1,))
    prop_b = prop_patron_exacto('P5_igual_1_en_B', ('P5',), (1,))

    cfg = ConfiguracionTriada(
        celda_a=a,
        celda_b=b,
        familia_propiedades=[(prop_a, prop_b)],
        transporte={'P5': 'P5'},
    )
    return clasificar_triada(cfg)


def tesauro_t5_equivalencia_parcial_con_u() -> str:
    a = CeldaSV(('U', 'U', 0, 0, 0, 0, 0, 0, 0))
    b = CeldaSV(('U', 'U', 1, 1, 1, 1, 1, 1, 1))

    prop_a = prop_vector_igual('par_inicial_U_en_A', ('P1', 'P2'))
    prop_b = prop_vector_igual('par_inicial_U_en_B', ('P1', 'P2'))

    cfg = ConfiguracionTriada(
        celda_a=a,
        celda_b=b,
        familia_propiedades=[(prop_a, prop_b)],
        transporte={'P1': 'P1', 'P2': 'P2'},
        perdida_declarada=True,
    )
    return clasificar_triada(cfg)


def pruebas_canonicas() -> None:
    assert ejemplo_e1_comparabilidad_sin_lambda() == 'comparabilidad'
    assert ejemplo_e2_comparabilidad_puntual() == 'comparabilidad'
    assert ejemplo_e3_equivalencia_parcial() == 'equivalencia_parcial'
    assert ejemplo_e4_identidad_vectorial_sin_identidad_regimen() == 'no_equivalencia'
    assert ejemplo_e5_comparabilidad_independiente() == 'comparabilidad'

    assert tesauro_t1_lambda_fuerte_no_basta() == 'no_equivalencia'
    assert tesauro_t2_equivalencia_parcial_minima() == 'equivalencia_parcial'
    assert tesauro_t3_no_equivalencia_pura() == 'no_equivalencia'
    assert tesauro_t4_comparabilidad_por_propiedad_local() == 'comparabilidad'
    assert tesauro_t5_equivalencia_parcial_con_u() == 'equivalencia_parcial'

    print('Laboratorio: verificación canónica completada correctamente.')


def informe_completo() -> None:
    casos = [
        ('E1 — Comparabilidad sin dato de enlace', ejemplo_e1_comparabilidad_sin_lambda),
        ('E2 — Comparabilidad con preservación puntual', ejemplo_e2_comparabilidad_puntual),
        ('E3 — Equivalencia parcial genuina', ejemplo_e3_equivalencia_parcial),
        ('E4 — Identidad vectorial sin identidad de régimen', ejemplo_e4_identidad_vectorial_sin_identidad_regimen),
        ('E5 — Comparabilidad independiente del enlace', ejemplo_e5_comparabilidad_independiente),
        ('T1 — Lambda fuerte no basta', tesauro_t1_lambda_fuerte_no_basta),
        ('T2 — Equivalencia parcial mínima', tesauro_t2_equivalencia_parcial_minima),
        ('T3 — No equivalencia pura', tesauro_t3_no_equivalencia_pura),
        ('T4 — Comparabilidad por propiedad local', tesauro_t4_comparabilidad_por_propiedad_local),
        ('T5 — Equivalencia parcial con U', tesauro_t5_equivalencia_parcial_con_u),
    ]
    print('\n─── Informe de clasificación del laboratorio ───\n')
    for nombre, fn in casos:
        resultado = fn()
        print(f'{nombre}\n  → {resultado}  [{TRIADA[resultado]}]\n')


if __name__ == '__main__':
    pruebas_canonicas()
    informe_completo()
