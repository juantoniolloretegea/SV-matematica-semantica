# Autoría: Juan Antonio Lloret Egea | ORCID: 0000-0002-6634-3351 | Institución: Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA) | Publicación: IA eñ™ — La Biblia de la IA™ | ISSN: 2695-6411 | Licencia: CC BY-NC-ND 4.0 | Lugar y fecha: Madrid, 2026

"""
Códigos de salida y fallo previstos para la suite laboratorial del Hito 3.
"""
from __future__ import annotations

OK = 0
ERR_REGISTRY_DUPLICATE_ASSERTION_ID = 10
ERR_REGISTRY_DUPLICATE_LAB = 11
ERR_REGISTRY_MISSING_LAB_FILE = 12
ERR_REGISTRY_UNREGISTERED_LAB_FILE = 13
ERR_METADATA_MISSING = 20
ERR_IMPORT = 30
ERR_RUN_EXCEPTION = 31
ERR_INVALID_RESULT = 32
ERR_STATUS_MISMATCH = 33
ERR_PASSED_FALSE = 34
ERR_REPORT_WRITE = 35

DESCRIPTIONS = {
    OK: "Ejecución íntegra sin incidencias.",
    ERR_REGISTRY_DUPLICATE_ASSERTION_ID: "Hay identificadores de afirmación duplicados en el registro.",
    ERR_REGISTRY_DUPLICATE_LAB: "Hay laboratorios duplicados en el registro.",
    ERR_REGISTRY_MISSING_LAB_FILE: "El registro apunta a un laboratorio inexistente.",
    ERR_REGISTRY_UNREGISTERED_LAB_FILE: "Existe un laboratorio físico no registrado.",
    ERR_METADATA_MISSING: "Falta la línea obligatoria de autoría en uno o más archivos Python.",
    ERR_IMPORT: "No se pudo importar un módulo de laboratorio.",
    ERR_RUN_EXCEPTION: "El laboratorio lanzó una excepción no controlada.",
    ERR_INVALID_RESULT: "El laboratorio devolvió un resultado inválido o incompleto.",
    ERR_STATUS_MISMATCH: "El estado devuelto no coincide con el estado esperado por el registro.",
    ERR_PASSED_FALSE: "El laboratorio devolvió passed=False o un booleano inválido.",
    ERR_REPORT_WRITE: "No se pudo escribir el informe JSON de salida.",
}


def describe(code: int) -> str:
    return DESCRIPTIONS.get(code, "Código de salida no documentado.")
