# Autoría: Juan Antonio Lloret Egea | ORCID: 0000-0002-6634-3351 | Institución: Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA) | Publicación: IA eñ™ — La Biblia de la IA™ | ISSN: 2695-6411 | Licencia: CC BY-NC-ND 4.0 | Lugar y fecha: Madrid, 2026

"""
Utilidades de auditoría dura para runners del Hito 3.
"""
from __future__ import annotations

from dataclasses import asdict, is_dataclass
from pathlib import Path
from typing import Iterable, Sequence

from core.error_codes import (
    ERR_INVALID_RESULT,
    ERR_METADATA_MISSING,
    ERR_PASSED_FALSE,
    ERR_REGISTRY_DUPLICATE_ASSERTION_ID,
    ERR_REGISTRY_DUPLICATE_LAB,
    ERR_REGISTRY_MISSING_LAB_FILE,
    ERR_REGISTRY_UNREGISTERED_LAB_FILE,
    ERR_STATUS_MISMATCH,
)

AUTHOR_MARKER = "Juan Antonio Lloret Egea"
ALLOWED_STATUSES = {"CONFIRMA", "REFUTA", "ABIERTO"}
REQUIRED_RESULT_KEYS = {"lab_id", "title", "status", "passed", "summary", "details"}


def collect_python_files(base_dir: Path) -> list[Path]:
    return sorted(p for p in base_dir.rglob('*.py') if '__pycache__' not in p.parts)


def ensure_author_metadata(base_dir: Path) -> tuple[int, dict[str, object]] | None:
    missing = []
    for path in collect_python_files(base_dir):
        text = path.read_text(encoding='utf-8')
        if AUTHOR_MARKER not in text:
            missing.append(str(path.relative_to(base_dir)))
    if missing:
        return ERR_METADATA_MISSING, {"missing_author_metadata": missing}
    return None


def validate_registry(assertions: Sequence[dict[str, object]], base_dir: Path) -> tuple[int, dict[str, object]] | None:
    ids = [str(item['id']) for item in assertions]
    if len(ids) != len(set(ids)):
        duplicates = sorted({x for x in ids if ids.count(x) > 1})
        return ERR_REGISTRY_DUPLICATE_ASSERTION_ID, {"duplicate_assertion_ids": duplicates}

    labs = [str(item['laboratorio']) for item in assertions]
    if len(labs) != len(set(labs)):
        duplicates = sorted({x for x in labs if labs.count(x) > 1})
        return ERR_REGISTRY_DUPLICATE_LAB, {"duplicate_laboratorios": duplicates}

    lab_dir = base_dir / 'laboratorios'
    expected_files = {f"{lab}.py" for lab in labs}
    actual_files = {p.name for p in lab_dir.glob('lab_*.py')}

    missing = sorted(expected_files - actual_files)
    if missing:
        return ERR_REGISTRY_MISSING_LAB_FILE, {"missing_lab_files": missing}

    unregistered = sorted(actual_files - expected_files)
    if unregistered:
        return ERR_REGISTRY_UNREGISTERED_LAB_FILE, {"unregistered_lab_files": unregistered}

    return None


def normalize_result(obj: object) -> dict[str, object]:
    if hasattr(obj, 'to_dict'):
        data = obj.to_dict()  # type: ignore[attr-defined]
    elif is_dataclass(obj):
        data = asdict(obj)
    elif isinstance(obj, dict):
        data = dict(obj)
    else:
        raise ValueError('Resultado no serializable ni normalizable.')
    return data


def validate_result(data: dict[str, object], expected_status: str) -> tuple[int, dict[str, object]] | None:
    keys = set(data.keys())
    if REQUIRED_RESULT_KEYS - keys:
        return ERR_INVALID_RESULT, {
            "missing_result_keys": sorted(REQUIRED_RESULT_KEYS - keys),
            "result_keys": sorted(keys),
        }

    status = data['status']
    if status not in ALLOWED_STATUSES:
        return ERR_INVALID_RESULT, {
            "invalid_status": status,
            "allowed_statuses": sorted(ALLOWED_STATUSES),
        }

    passed = data['passed']
    if not isinstance(passed, bool) or passed is not True:
        return ERR_PASSED_FALSE, {
            "passed": passed,
            "status": status,
            "expected_status": expected_status,
        }

    if status != expected_status:
        return ERR_STATUS_MISMATCH, {
            "expected_status": expected_status,
            "received_status": status,
            "lab_id": data.get('lab_id'),
        }

    return None
