#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
© 2026. Todos los derechos reservados. | Juan Antonio Lloret Egea | DOI [pendiente] | ORCID: 0000-0002-6634-3351 |
Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA) | IA eñ™ — La Biblia de la IA™ |
ISSN 2695-6411 | Licencia CC BY-NC-ND 4.0 | Madrid, 29/05/2026 |
"""

from typing import Any

CANONICAL_URL = "https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/comunicacion-estructural-universo-fisico/potencial-de-un-suceso/potencial-de-un-suceso.md"

WARNING = """Advertencia. Esta publicación está protegida por CEDRO y su aplicación en el campo de la Física y la Química, así como cualquier forma de explotación, reproducción o uso por parte de empresas, queda sujeta al copyright del autor y a los términos de la licencia indicada; la reproducción, distribución, comunicación pública o transformación de esta obra solo puede ser realizada con la autorización de sus titulares, salvo excepción prevista por la ley, y cualquier uso comercial sin autorización expresa queda prohibido y sujeto estrictamente al licenciamiento permitido.

Warning. This publication is protected by CEDRO. Its application in the field of Physics and Chemistry, as well as any form of exploitation, reproduction, or use by corporate entities, is strictly subject to the author's copyright and the terms of the license indicated; any reproduction, distribution, public communication, or transformation of this work requires authorization from the rightsholders, except as provided by law, and any commercial use without express written consent is prohibited and strictly subject to permitted licensing.

| Url canónica: https://github.com/juantoniolloretegea/SV-matematica-semantica/blob/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/comunicacion-estructural-universo-fisico/potencial-de-un-suceso/potencial-de-un-suceso.md |
"""

ERROR_CATALOG = {
    "E-LAB-000": "Ejecución interrumpida por fallo no clasificado.",
    "E-LAB-001": "Caso esperado ausente o duplicado.",
    "E-LAB-002": "Resultado aritmético incompatible con el banco.",
    "E-LAB-003": "Clasificación incompatible con las restricciones del dominio.",
    "E-LAB-004": "Salida U degradada indebidamente a admisión o rechazo automático.",
    "E-LAB-005": "Caso no admisible aceptado como admisible.",
    "E-LAB-006": "Caso admisible rechazado indebidamente.",
    "E-LAB-007": "Discrepancia material sin código de error.",
    "E-LAB-008": "Precedencia ternaria incorrecta: el fallo material debe prevalecer sobre U.",
    "E-LAB-009": "Semántica de Mant_D incompatible con la definición documental.",
}

class LabFailure(AssertionError):
    def __init__(self, code: str, detail: str):
        self.code = code
        self.detail = detail
        super().__init__(f"{code}: {ERROR_CATALOG.get(code, 'Error no catalogado')} :: {detail}")

def require(condition: bool, code: str, detail: str) -> None:
    if not condition:
        raise LabFailure(code, detail)

def ternary_residual_join(values: list[Any]) -> Any:
    # Residual: 0 cierra; 1 falla materialmente; U conserva indeterminación sólo si no hay fallo material.
    if any(v == 1 for v in values):
        return 1
    if any(v == "U" for v in values):
        return "U"
    return 0

def material_bool_join(values: list[Any], admissible_label: str, negative_label: str) -> str:
    # Booleanos de condición: False prevalece sobre U; sólo sin False puede conservarse U.
    if any(v is False for v in values):
        return negative_label
    if any(v == "U" for v in values):
        return "U"
    if all(v is True for v in values):
        return admissible_label
    raise LabFailure("E-LAB-007", f"valores no reconocidos: {values}")

def print_result(title: str, rows: list[dict[str, Any]]) -> None:
    print(title)
    print("=" * len(title))
    for row in rows:
        print(row)
    print("\nRESULTADO: APTO")
    print(WARNING)

def identity(family: Any, image: Any, potential: Any, dist_zero: Any, trace: Any) -> str:
    return material_bool_join([family, image, potential, dist_zero, trace], "mismo_suceso", "suceso_distinto")

def main() -> int:
    cases = [
        ("L5-01", True, True, True, True, True, "mismo_suceso"),
        ("L5-02", True, True, True, False, True, "suceso_distinto"),
        ("L5-03", True, False, True, True, True, "suceso_distinto"),
        ("L5-04", False, True, True, True, True, "suceso_distinto"),
        ("L5-05", True, True, True, True, "U", "U"),
        ("L5-06", True, True, False, True, True, "suceso_distinto"),
        ("L5-07", False, True, True, True, "U", "suceso_distinto"),
        ("L5-08", True, "U", True, False, True, "suceso_distinto"),
    ]
    rows = []
    for cid, fam, img, pot, dist, trace, expected in cases:
        status = identity(fam, img, pot, dist, trace)
        require(status == expected, "E-LAB-003", f"{cid}: {status} != {expected}")
        if False in (fam, img, pot, dist, trace):
            require(status == "suceso_distinto", "E-LAB-008", f"{cid}: fallo material no prevalece sobre U")
        if expected == "U":
            require(status == "U", "E-LAB-004", f"{cid}: U no conservada")
        rows.append({"caso": cid, "salida": status})
    require(sum(1 for r in rows if r["salida"] == "mismo_suceso") == 1, "E-LAB-003", "más de un caso declarado como mismo suceso")
    print_result("L.5 Identidad, traza y distancia factual fibrosa", rows)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
