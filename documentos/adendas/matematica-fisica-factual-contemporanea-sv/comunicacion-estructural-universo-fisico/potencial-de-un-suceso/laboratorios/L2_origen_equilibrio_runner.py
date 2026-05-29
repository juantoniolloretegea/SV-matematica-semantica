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

def classify(mu: int, lam: int) -> str:
    require(mu >= 0 and lam >= 0, "E-LAB-003", f"polos negativos: {(mu, lam)}")
    p, intensity = mu - lam, mu + lam
    if p == 0 and intensity == 0:
        return "origen_formal"
    if p == 0 and intensity > 0:
        return "equilibrio_realizado"
    return "predominio_polo_uno" if p > 0 else "predominio_polo_cero"

def main() -> int:
    cases = [
        ("L2-01", 0, 0, "origen_formal"),
        ("L2-02", 1, 1, "equilibrio_realizado"),
        ("L2-03", 12, 12, "equilibrio_realizado"),
        ("L2-04", 3, 0, "predominio_polo_uno"),
        ("L2-05", 0, 3, "predominio_polo_cero"),
        ("L2-06", 7, 7, "equilibrio_realizado"),
    ]
    rows, origins = [], 0
    for cid, mu, lam, expected in cases:
        label = classify(mu, lam)
        origins += 1 if label == "origen_formal" else 0
        require(label == expected, "E-LAB-003", f"{cid}: {label} != {expected}")
        rows.append({"caso": cid, "par": (mu, lam), "P": mu-lam, "I": mu+lam, "salida": label})
    require(origins == 1, "E-LAB-003", f"orígenes formales detectados: {origins}")
    print_result("L.2 Origen formal y equilibrio realizado", rows)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
