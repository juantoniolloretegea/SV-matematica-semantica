# -*- coding: utf-8 -*-
# © 2026. Todos los derechos reservados. | Juan Antonio Lloret Egea | ORCID: 0000-0002-6634-3351 | Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA) | IA eñ™ — La Biblia de la IA™ | ISSN 2695-6411 | Licencia CC BY-NC-ND 4.0 | Madrid, 06/05/2026
# Advertencia. Esta publicación está protegida por CEDRO y su aplicación en el campo de la Física, así como cualquier forma de explotación, reproducción o uso por parte de empresas, queda sujeta al copyright del autor y a los términos de la licencia indicada; la reproducción, distribución, comunicación pública o transformación de esta obra solo puede ser realizada con la autorización de sus titulares, salvo excepción prevista por la ley, y cualquier uso comercial sin autorización expresa queda prohibido y sujeto estrictamente al licenciamiento permitido.
# Warning. This publication is protected by CEDRO. Its application in the field of Physics, as well as any form of exploitation, reproduction, or use by corporate entities, is strictly subject to the author's copyright and the terms of the license indicated; any reproduction, distribution, public communication, or transformation of this work requires authorization from the rightsholders, except as provided by law, and any commercial use without express written consent is prohibited and strictly subject to permitted licensing.
#
# Módulo: sv_tabla_bis — verificación del §14bis (Teorema de admisibilidad y extensión periódica estructural)
# Referencia doctrinal: Lloret Egea (2026), §14bis; Teoría del TODO y de la NADA §14-15 (Teorema T5)
# Errores de dominio: SV-BIS-INPUT-001 a SV-BIS-EXT-003

from __future__ import annotations
from dataclasses import dataclass
from enum import Enum
from math import floor
from typing import Iterator, List, Tuple


class DictamenBis(str, Enum):
    ADMISIBLE    = "ADMISIBLE_ESTRUCTURAL"
    NO_DETECTADO = "CANDIDATO_SV_NO_DETECTADO"
    U            = "U"
    NO_ADMISIBLE = "NO_ADMISIBLE"
    ARTEFACTO    = "ARTEFACTO_FORMAL"


@dataclass(frozen=True)
class CandidatoSV:
    """Clase atómica candidata al dominio 𝕋_chem^SV (§14bis.1)."""
    nombre: str
    Z_sv: int                # número estructural (>=119 para candidatos)
    p_min_pos: bool          # 𝓟_min > 0
    frontera_ok: bool        # δ(∂Ω) < Λ
    residual_ok: bool        # ℛ < Λ
    intercambio_ok: bool     # Δ𝓗 ∈ 𝓢_disc
    identidad_ok: bool       # Id_chem ≠ ∅
    desc_proto: bool | None  # None = U (§14bis.4)
    no_artificio: bool | None # None = U (§14bis.3)
    e_star_ok: bool          # 𝓔★(Γ_U; τ) = 0 (compuerta rectora)
    detectado_ext: bool = False  # contraste empírico externo


def verifica_admisibilidad(c: CandidatoSV) -> DictamenBis:
    """Aplica la fórmula de pertenencia 𝓝★[...]=1 del §14bis.1.

    Prelación del verificador ternario fuerte: 1 ≻ U ≻ 0.
    """
    # Compuerta rectora — fallo fuerte
    if not c.e_star_ok:
        return DictamenBis.NO_ADMISIBLE

    # Detectar artefacto formal (§14bis.3)
    if c.no_artificio is False:
        return DictamenBis.ARTEFACTO

    # Detectar U en condiciones críticas
    condiciones_criticas = [
        c.p_min_pos,
        c.frontera_ok,
        c.residual_ok,
        c.intercambio_ok,
        c.identidad_ok,
    ]
    if any(v is None for v in condiciones_criticas):
        raise ValueError("SV-BIS-INPUT-001: condición crítica no puede ser U en este nivel")

    if not all(condiciones_criticas):
        return DictamenBis.NO_ADMISIBLE

    # Desc_proto: U → suspensión honesta (§14bis.21)
    if c.desc_proto is None:
        return DictamenBis.U
    if not c.desc_proto:
        return DictamenBis.NO_ADMISIBLE

    # No_artificio: U → suspensión honesta
    if c.no_artificio is None:
        return DictamenBis.U

    # Pasa todas las compuertas
    if c.detectado_ext:
        return DictamenBis.ADMISIBLE
    else:
        return DictamenBis.NO_DETECTADO


# -------------- Teorema de extensión periódica (§14bis.7) ---------------

def nombre_sv(k: int) -> str:
    """Nom_Griego(k): alfabeto griego en vueltas sucesivas (§14bis.6)."""
    alfabeto = [
        "Alfa", "Beta", "Gamma", "Delta", "Epsilon", "Zeta", "Eta", "Theta",
        "Iota", "Kappa", "Lambda", "Mu", "Nu", "Xi", "Omicron", "Pi",
        "Rho", "Sigma", "Tau", "Upsilon", "Phi", "Chi", "Psi", "Omega"
    ]
    vuelta = (k - 1) // 24
    idx    = (k - 1) % 24
    prefijo = "" if vuelta == 0 else f"SV-{['II','III','IV','V','VI'][vuelta-1]}-"
    return f"SV-{prefijo}{alfabeto[idx]}" if vuelta == 0 else f"{prefijo}{alfabeto[idx]}"


def A_sv(k: int) -> int:
    """A_SV(k) = 294 + 3k + ⌊k/2⌋ — masa atómica estructural (§14bis.7)."""
    return 294 + 3 * k + floor(k / 2)


def periodo_sv(k: int) -> int:
    """Periodo_SV(k) = 8 + ⌊(k−1)/18⌋ (§14bis.7)."""
    return 8 + floor((k - 1) / 18)


def grupo_sv(k: int) -> int:
    """Grupo_SV(k) = 1 + ((k−1) mod 18) (§14bis.7)."""
    return 1 + ((k - 1) % 18)


def genera_extension(
    N: int,
    compuertas_fn  # función (k) -> CandidatoSV con compuertas evaluadas
) -> List[Tuple]:
    """Genera la extensión 𝕋_ext^SV(N) y devuelve las N tuplas de salida.

    Cada tupla: (Nº, Nombre, Z_SV, Masa_u, Conf, Periodo, Grupo, Estado_STP, Función)
    Lanza SV-BIS-EXT-001 si algún candidato no supera las compuertas.
    """
    resultados = []
    for k in range(1, N + 1):
        c = compuertas_fn(k)
        dictamen = verifica_admisibilidad(c)
        if dictamen == DictamenBis.NO_ADMISIBLE or dictamen == DictamenBis.ARTEFACTO:
            raise ValueError(
                f"SV-BIS-EXT-001: candidato k={k} ({c.nombre}) "
                f"no supera compuertas — dictamen {dictamen}"
            )
        resultados.append((
            k,
            nombre_sv(k),
            118 + k,          # Z_SV
            A_sv(k),          # masa atómica SV
            f"[Og]_ext_k{k}", # configuración simbólica
            periodo_sv(k),
            grupo_sv(k),
            "U_fis",          # estado STP: no determinado físicamente
            dictamen.value,
        ))
    return resultados
