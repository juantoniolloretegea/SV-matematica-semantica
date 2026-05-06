# -*- coding: utf-8 -*-
# © 2026. Todos los derechos reservados. | Juan Antonio Lloret Egea | ORCID: 0000-0002-6634-3351 | Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español (ITVIA) | IA eñ™ — La Biblia de la IA™ | ISSN 2695-6411 | Licencia CC BY-NC-ND 4.0 | Madrid, 06/05/2026
# Advertencia. Esta publicación está protegida por CEDRO y su aplicación en el campo de la Física, así como cualquier forma de explotación, reproducción o uso por parte de empresas, queda sujeta al copyright del autor y a los términos de la licencia indicada; la reproducción, distribución, comunicación pública o transformación de esta obra solo puede ser realizada con la autorización de sus titulares, salvo excepción prevista por la ley, y cualquier uso comercial sin autorización expresa queda prohibido y sujeto estrictamente al licenciamiento permitido.
# Warning. This publication is protected by CEDRO. Its application in the field of Physics, as well as any form of exploitation, reproduction, or use by corporate entities, is strictly subject to the author's copyright and the terms of the license indicated; any reproduction, distribution, public communication, or transformation of this work requires authorization from the rightsholders, except as provided by law, and any commercial use without express written consent is prohibited and strictly subject to permitted licensing.

from dataclasses import dataclass
from enum import Enum
from typing import Dict, Iterable, List

class Dictamen(str, Enum):
    ELEMENTO_ADMISIBLE = "ELEMENTO_ADMISIBLE"
    MOLECULA_ADMISIBLE = "MOLECULA_ADMISIBLE"
    ATMOSFERA_ADMISIBLE = "ATMOSFERA_ADMISIBLE"
    NO_ADMISIBLE = "NO_ADMISIBLE"
    U = "U"

@dataclass(frozen=True)
class Estado:
    F_boundary: float
    Q_transfer: float
    residual: float
    boundary_var: float
    lambda_umbral: float
    discrete_exchange: bool
    identity: bool
    e_star_ok: bool
    known: bool = True


def p_min(e: Estado) -> float:
    vals = [e.F_boundary, e.Q_transfer, e.residual, e.boundary_var, e.lambda_umbral]
    if any(v < 0 for v in vals):
        raise ValueError("SV-GH-INPUT-001: magnitud negativa no admisible")
    if e.lambda_umbral <= 0:
        raise ValueError("SV-GH-BOUNDARY-001: umbral de frontera inválido")
    return e.F_boundary - e.Q_transfer - e.residual


def condicion_base(e: Estado) -> bool:
    return (p_min(e) > 0 and e.boundary_var < e.lambda_umbral and e.residual < e.lambda_umbral
            and e.discrete_exchange and e.identity and e.e_star_ok)


def dictaminar_elemento(e: Estado, Z: int) -> Dictamen:
    if Z > 118 and not e.known:
        return Dictamen.U
    return Dictamen.ELEMENTO_ADMISIBLE if condicion_base(e) else Dictamen.NO_ADMISIBLE


def dictaminar_molecula(componentes: Iterable[Dictamen], e: Estado) -> Dictamen:
    if not all(c == Dictamen.ELEMENTO_ADMISIBLE for c in componentes):
        return Dictamen.NO_ADMISIBLE
    return Dictamen.MOLECULA_ADMISIBLE if condicion_base(e) else Dictamen.NO_ADMISIBLE


def dictaminar_atmosfera(componentes: Iterable[Dictamen], e: Estado, retencion_grav: bool) -> Dictamen:
    if not all(c in (Dictamen.MOLECULA_ADMISIBLE, Dictamen.ELEMENTO_ADMISIBLE) for c in componentes):
        return Dictamen.NO_ADMISIBLE
    if not retencion_grav:
        return Dictamen.NO_ADMISIBLE
    return Dictamen.ATMOSFERA_ADMISIBLE if condicion_base(e) else Dictamen.NO_ADMISIBLE


def estado_elemento(Z: int, known: bool = True) -> Estado:
    if Z > 118:
        return Estado(0, 0, 0, 1, 1, False, False, True, False)
    # Secuencia determinista: garantiza prueba estructural común para 1..118 sin parametrización manual elemento a elemento.
    F = 20.0 + (Z % 17) * 0.73 + Z * 0.015
    Q = 3.0 + (Z % 7) * 0.19
    R = 0.45 + (Z % 11) * 0.031
    L = 2.0 + (Z % 5) * 0.07
    B = 0.25 + (Z % 13) * 0.021
    return Estado(F, Q, R, B, L, True, True, True, known)


def estado_molecular(intensidad: float = 1.0) -> Estado:
    return Estado(18.0 * intensidad, 4.0 * intensidad, 0.8 * intensidad, 0.35, 1.2, True, True, True, True)


def estado_atmosferico(retencion: bool = True) -> Estado:
    if retencion:
        return Estado(32.0, 9.0, 2.0, 0.6, 3.0, True, True, True, True)
    return Estado(4.0, 9.0, 3.0, 3.2, 3.0, True, True, True, True)
