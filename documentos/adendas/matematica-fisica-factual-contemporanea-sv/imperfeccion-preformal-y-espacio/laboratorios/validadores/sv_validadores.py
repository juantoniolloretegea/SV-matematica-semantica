# -*- coding: utf-8 -*-
"""
Validadores de laboratorios — Imperfección preformal y espacio.
Autor: Juan Antonio Lloret Egea | ORCID: 0000-0002-6634-3351
© 2026. Todos los derechos reservados. Licencia CC BY-NC-ND 4.0.
"""
from __future__ import annotations

import csv
import hashlib
import json
from pathlib import Path
from typing import Dict, Iterable, List, Tuple

REQUIRED_METADATA = {
    "autor": "Juan Antonio Lloret Egea",
    "orcid": "0000-0002-6634-3351",
    "copyright": "© 2026. Todos los derechos reservados.",
    "licencia": "CC BY-NC-ND 4.0",
}

CASE_FILES = [
    "casos_origen_cosmologico.csv",
    "casos_espacio.csv",
    "casos_transparencia.csv",
    "casos_materia_oscura.csv",
    "casos_energia_oscura.csv",
    "casos_dm_de_bh.csv",
    "casos_agujero_negro.csv",
    "casos_falsos_fundamentos.csv",
]
CRITICAL_FLAGS = ["delta_domM", "delta_domSV", "delta_unidad_sv", "delta_proj", "delta_ret", "delta_inv", "delta_fund"]
PARTIAL_FLAGS = ["delta_mod"]
SUPPORT_FLAGS = ["delta_sup"]
VALID_DICTAMEN = {"admisible", "admisible_parcial", "no_admisible", "U"}
FORBIDDEN_SILENT_EQUIVALENCES = {
    ("Big Bang", "ε₋₀"),
    ("vacío cuántico", "NADA"),
    ("nothing", "NADA"),
    ("materia oscura", "agujero negro"),
    ("energía oscura", "materia oscura"),
    ("trayectoria", "crea espacio"),
    ("métrica", "funda espacio"),
}

class LabFailure(Exception):
    pass

def read_csv(path: Path) -> List[Dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))

def as_int(row: Dict[str, str], key: str) -> int:
    try:
        value = int(str(row.get(key, "0")).strip() or "0")
    except ValueError as exc:
        raise LabFailure(f"{row.get('id_caso','SIN_ID')}: {key} no es entero 0/1") from exc
    if value not in (0, 1):
        raise LabFailure(f"{row.get('id_caso','SIN_ID')}: {key} no pertenece a {{0,1}}")
    return value

def expected_from_flags(row: Dict[str, str]) -> str:
    if any(as_int(row, key) == 1 for key in CRITICAL_FLAGS):
        return "no_admisible"
    if any(as_int(row, key) == 1 for key in PARTIAL_FLAGS):
        return "admisible_parcial"
    if any(as_int(row, key) == 1 for key in SUPPORT_FLAGS):
        return "U"
    return "admisible"

def validate_metadata(rows: Iterable[Dict[str, str]], source: str) -> List[str]:
    errors: List[str] = []
    for idx, row in enumerate(rows, 1):
        for key, expected in REQUIRED_METADATA.items():
            if row.get(key) != expected:
                errors.append(f"{source}:{idx}: metadato {key} inválido o ausente")
    return errors

def validate_case_rows(rows: List[Dict[str, str]], source: str) -> Tuple[List[str], Dict[str, int]]:
    errors: List[str] = []
    counts = {"admisible":0, "admisible_parcial":0, "no_admisible":0, "U":0}
    seen = set()
    required = ["id_caso", "familia", "magnitud_fisica", "unidad_sv", "dominio_m", "dominio_sv", "proyeccion_sv", "retorno_fisico", "dictamen_esperado"]
    for row in rows:
        ident = row.get("id_caso", "").strip()
        if not ident:
            errors.append(f"{source}: caso sin id_caso")
            continue
        if ident in seen:
            errors.append(f"{source}: id duplicado {ident}")
        seen.add(ident)
        for key in required:
            if not str(row.get(key, "")).strip():
                errors.append(f"{source}:{ident}: campo crítico vacío: {key}")
        for flag in CRITICAL_FLAGS + PARTIAL_FLAGS + SUPPORT_FLAGS:
            try:
                as_int(row, flag)
            except LabFailure as exc:
                errors.append(str(exc))
        declared = row.get("dictamen_esperado", "").strip()
        if declared not in VALID_DICTAMEN:
            errors.append(f"{source}:{ident}: dictamen no canónico: {declared}")
            continue
        derived = expected_from_flags(row)
        if derived != declared:
            errors.append(f"{source}:{ident}: dictamen esperado {declared} no coincide con derivado {derived}")
        counts[declared] += 1
        # No critical rejection without error code.
        if declared == "no_admisible" and not row.get("codigo_error_esperado", "").strip():
            errors.append(f"{source}:{ident}: no_admisible sin codigo_error_esperado")
        text = " ".join(str(row.get(k, "")) for k in ["magnitud_fisica", "dominio_sv", "proyeccion_sv", "retorno_fisico", "observacion"])
        for left, right in FORBIDDEN_SILENT_EQUIVALENCES:
            if left.lower() in text.lower() and right.lower() in text.lower() and declared != "no_admisible":
                errors.append(f"{source}:{ident}: equivalencia prohibida no rechazada: {left} / {right}")
    return errors, counts

def hash_data_files(data_dir: Path) -> str:
    h = hashlib.sha256()
    for p in sorted(data_dir.glob("*.csv")):
        h.update(p.name.encode("utf-8"))
        h.update(p.read_bytes())
    return h.hexdigest()

def run_all(root: Path) -> Dict[str, object]:
    data_dir = root / "datos"
    all_errors: List[str] = []
    total_counts = {"admisible":0, "admisible_parcial":0, "no_admisible":0, "U":0}
    total_cases = 0
    for filename in CASE_FILES:
        path = data_dir / filename
        if not path.exists():
            all_errors.append(f"falta fichero de casos: {filename}")
            continue
        rows = read_csv(path)
        total_cases += len(rows)
        all_errors.extend(validate_metadata(rows, filename))
        errs, counts = validate_case_rows(rows, filename)
        all_errors.extend(errs)
        for k, v in counts.items():
            total_counts[k] += v
    # Check metadata in non-case CSVs too.
    for filename in ["teorias_externas.csv", "dominios_internos.csv", "magnitudes_unidades_sv.csv"]:
        path = data_dir / filename
        if not path.exists():
            all_errors.append(f"falta fichero de datos: {filename}")
        else:
            all_errors.extend(validate_metadata(read_csv(path), filename))
    # Check catalog metadata.
    catalog = root / "catalogo_errores.csv"
    if not catalog.exists():
        all_errors.append("falta catalogo_errores.csv")
    else:
        catalog_rows = read_csv(catalog)
        all_errors.extend(validate_metadata(catalog_rows, "catalogo_errores.csv"))
        if len(catalog_rows) < 12:
            all_errors.append("catalogo_errores.csv insuficiente: menos de 12 códigos")
    # Anti-silent-pass thresholds.
    minimums = {"admisible":8, "admisible_parcial":6, "no_admisible":10, "U":2}
    for key, minimum in minimums.items():
        if total_counts.get(key, 0) < minimum:
            all_errors.append(f"cobertura insuficiente {key}: {total_counts.get(key,0)} < {minimum}")
    if total_cases < 35:
        all_errors.append(f"cobertura total insuficiente: {total_cases} < 35")
    return {
        "metadata": REQUIRED_METADATA,
        "resultado_global": "NO_APTO" if all_errors else "APTO",
        "total_casos": total_cases,
        "conteo_dictamenes": total_counts,
        "errores_detectados": all_errors,
        "hash_datos": hash_data_files(data_dir),
    }
