#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
© 2026. Todos los derechos reservados. | Juan Antonio Lloret Egea | DOI [pendiente] | ORCID: 0000-0002-6634-3351 |
Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA) | IA eñ™ — La Biblia de la IA™ |
ISSN 2695-6411 | Licencia CC BY-NC-ND 4.0 | Madrid, 29/05/2026 |
"""

from typing import Any
from math import floor, sqrt, ceil

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
    "E-LAB-010": "Métrica tipada incompatible con IX.",
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
    if any(v == 1 for v in values):
        return 1
    if any(v == "U" for v in values):
        return "U"
    return 0

def material_bool_join(values: list[Any], admissible_label: str, negative_label: str) -> str:
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

def analyze_trajectory(potentials: list[float], coeffs: list[float] | None = None) -> dict[str, object]:
    require(len(potentials) >= 2, "E-LAB-001", "la trayectoria exige al menos dos potenciales")
    deltas = [potentials[i+1] - potentials[i] for i in range(len(potentials)-1)]
    signed = sum(deltas)
    boundary = potentials[-1] - potentials[0]
    walked = sum(abs(d) for d in deltas)
    defect = walked - abs(boundary)
    result: dict[str, object] = {
        "potenciales": potentials,
        "variaciones": deltas,
        "acumulacion_firmada": signed,
        "saldo_frontera": boundary,
        "acumulacion_recorrida": walked,
        "defecto_recorrido": defect,
    }
    if coeffs is not None:
        require(len(coeffs) == len(deltas), "E-LAB-001", "coeficientes incompatibles con el número de tramos")
        require(all(c > 0 for c in coeffs), "E-LAB-003", f"coeficientes no positivos: {coeffs}")
        result["derivadas_normalizadas"] = [d / c for d, c in zip(deltas, coeffs)]
    return result

def main() -> int:
    canonical = analyze_trajectory([1, 4, 2], [1, 2])
    require(canonical["variaciones"] == [3, -2], "E-LAB-002", f"A.2.7 variaciones: {canonical['variaciones']}")
    require(canonical["derivadas_normalizadas"] == [3.0, -1.0], "E-LAB-002", f"A.2.7 derivadas: {canonical['derivadas_normalizadas']}")
    require(canonical["acumulacion_firmada"] == 1, "E-LAB-002", f"A.2.8 suma firmada: {canonical['acumulacion_firmada']}")
    require(canonical["saldo_frontera"] == 1, "E-LAB-002", f"A.2.8 saldo: {canonical['saldo_frontera']}")
    require(canonical["acumulacion_recorrida"] == 5, "E-LAB-002", f"A.2.8 recorrido: {canonical['acumulacion_recorrida']}")
    require(canonical["defecto_recorrido"] == 4, "E-LAB-002", f"A.2.8 defecto: {canonical['defecto_recorrido']}")

    extended = analyze_trajectory([1, 4, 2, 7])
    require(extended["variaciones"] == [3, -2, 5], "E-LAB-002", f"L4-02 variaciones: {extended['variaciones']}")
    require(extended["acumulacion_firmada"] == 6, "E-LAB-002", f"L4-02 suma firmada: {extended['acumulacion_firmada']}")
    require(extended["saldo_frontera"] == 6, "E-LAB-002", f"L4-02 saldo: {extended['saldo_frontera']}")
    require(extended["acumulacion_recorrida"] == 10, "E-LAB-002", f"L4-02 recorrido: {extended['acumulacion_recorrida']}")
    require(extended["defecto_recorrido"] == 4, "E-LAB-002", f"L4-02 defecto: {extended['defecto_recorrido']}")

    rows = [{"caso": "L4-01", **canonical}, {"caso": "L4-02", **extended}]
    print_result("L.4 Trayectoria, acumulación, recorrido y derivada normalizada", rows)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
