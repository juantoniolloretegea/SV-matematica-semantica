# Autoría: Juan Antonio Lloret Egea | ORCID: 0000-0002-6634-3351 | Institución: Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA) | Publicación: IA eñ™ — La Biblia de la IA™ | ISSN: 2695-6411 | Licencia: CC BY-NC-ND 4.0 | Lugar y fecha: Madrid, 2026

"""Núcleo común para laboratorios de primitivos metrológicos del SV."""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
import json
import math
from typing import Dict

DELTA_NU_CS = 9_192_631_770
N_CELDA = 9
UE_MFC_SAR = DELTA_NU_CS // N_CELDA
C_LUZ = 299_792_458
H_PLANCK = 6.626_070_15e-34
E_ELEM = 1.602_176_634e-19
K_BOLT = 1.380_649e-23
N_AVG = 6.022_140_76e23


def to_pretty_json(data: object) -> str:
    return json.dumps(data, ensure_ascii=False, indent=2)


@dataclass
class LabResult:
    lab_id: str
    title: str
    status: str
    passed: bool
    summary: str
    details: Dict[str, object]

    def to_dict(self) -> Dict[str, object]:
        return {
            'lab_id': self.lab_id,
            'title': self.title,
            'status': self.status,
            'passed': self.passed,
            'summary': self.summary,
            'details': self.details,
        }


def ue_mfc_seconds_fraction() -> Fraction:
    return Fraction(1, 9)


def ufe_interval_ue_mfc() -> Fraction:
    return Fraction(N_CELDA, C_LUZ)


def reduced_cs_over_c() -> tuple[int, int]:
    g = math.gcd(DELTA_NU_CS, C_LUZ)
    return DELTA_NU_CS // g, C_LUZ // g


def cs_photon_rest_mass() -> float:
    return H_PLANCK * DELTA_NU_CS / (C_LUZ ** 2)


def gas_constant() -> float:
    return N_AVG * K_BOLT
