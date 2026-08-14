#!/usr/bin/env python3
"""Reproduce el resultado r2 y ejecuta el contrato diagnóstico suplementario.

Modo preferente: si está presente el ZIP congelado, verifica su SHA-256, lo extrae
a un directorio temporal y ejecuta desde esa extracción.

Modo de respaldo: si el ZIP todavía no está alojado en GitHub, verifica uno a uno
los SHA-256 de la copia extraída contra `reports/manifest_contenido_r2.txt` y ejecuta
desde esa copia. Este modo permite reproducibilidad inmediata sin fingir que el
ZIP binario está publicado.

Las 16 pruebas diagnósticas suplementarias se informan aparte y NO se suman a las
78 pruebas congeladas citadas en el artículo.
"""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import zipfile

ROOT = Path(__file__).resolve().parent
ZIP = ROOT / "frozen" / "SV_AUTH_A2_revised_reference_r2_20260813.zip"
EXTRACTED = ROOT / "frozen" / "extracted"
FILE_MANIFEST = ROOT / "reports" / "manifest_contenido_r2.txt"
EXPECTED_SHA256 = "7c18761cf5546c8fdd9ad962c0ea3e0a54a9ddd4a4bf6d43c0ab29c7e4cf794f"
DIAG_TEST = ROOT / "diagnosticos" / "test_contrato_diagnostico.py"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for block in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def verify_extracted_tree(root: Path) -> None:
    """Comprueba que cada fichero extraído coincide con el ZIP r2 original."""
    expected: dict[str, str] = {}
    for line in FILE_MANIFEST.read_text(encoding="utf-8").splitlines():
        digest, rel = line.split("  ", 1)
        expected[rel] = digest
    actual_files = {p.relative_to(root).as_posix() for p in root.rglob("*") if p.is_file()}
    if actual_files != set(expected):
        missing = sorted(set(expected) - actual_files)
        extra = sorted(actual_files - set(expected))
        raise SystemExit(f"ERROR: árbol extraído divergente; faltan={missing}; sobran={extra}")
    for rel, digest in expected.items():
        got = sha256(root / rel)
        if got != digest:
            raise SystemExit(f"ERROR: SHA-256 incorrecto para {rel}: {got}")
    print(f"Integridad por fichero: {len(expected)} ficheros coinciden con el r2 original")


def run(cmd: list[str], *, cwd: Path, env: dict[str, str]) -> subprocess.CompletedProcess[str]:
    print("+", " ".join(cmd), flush=True)
    result = subprocess.run(cmd, cwd=cwd, env=env, text=True, capture_output=True)
    if result.stdout:
        print(result.stdout, end="")
    if result.stderr:
        print(result.stderr, end="", file=sys.stderr)
    if result.returncode != 0:
        raise SystemExit(result.returncode)
    return result


def execute(work: Path) -> None:
    env = os.environ.copy()
    env["PYTHONPATH"] = str(work / "src")

    frozen = run(
        [sys.executable, "-m", "pytest", "-q", "tests/test_authority.py"],
        cwd=work,
        env=env,
    )
    if "78 passed" not in frozen.stdout:
        raise SystemExit("ERROR: la batería congelada no produjo 78 pruebas superadas")

    run([sys.executable, "-m", "coverage", "erase"], cwd=work, env=env)
    run(
        [sys.executable, "-m", "coverage", "run", "-m", "pytest", "-q", "tests/test_authority.py"],
        cwd=work,
        env=env,
    )
    cov_json = work / "coverage-lab.json"
    run(
        [sys.executable, "-m", "coverage", "json", "-o", str(cov_json),
         "--include=src/sv_motor/security/authority_runtime.py,src/sv_motor/security/authority_types.py"],
        cwd=work,
        env=env,
    )
    data = json.loads(cov_json.read_text(encoding="utf-8"))
    totals = data["totals"]
    statements = totals["num_statements"]
    missing = totals["missing_lines"]
    percent = str(totals["percent_covered_display"])
    print(f"Cobertura fuente citada: {statements} sentencias, {missing} no cubiertas, {percent} %")
    if statements != 537 or missing != 24 or percent != "96":
        raise SystemExit("ERROR: la cobertura no coincide con el resultado sellado 537/24/96 %")

    run(
        [sys.executable, "-m", "pytest", "-q", str(DIAG_TEST)],
        cwd=ROOT,
        env=env,
    )


def main() -> None:
    if ZIP.exists():
        actual = sha256(ZIP)
        print(f"SHA-256 ZIP r2: {actual}")
        if actual != EXPECTED_SHA256:
            raise SystemExit("ERROR: el ZIP no coincide con el artefacto r2 sellado")
        with tempfile.TemporaryDirectory(prefix="sv-auth-r2-") as tmp:
            work = Path(tmp)
            with zipfile.ZipFile(ZIP) as zf:
                zf.extractall(work)
            execute(work)
        mode = "ZIP congelado verificado"
    else:
        print("AVISO: ZIP binario no presente; se usa la copia extraída verificada por fichero.")
        verify_extracted_tree(EXTRACTED)
        with tempfile.TemporaryDirectory(prefix="sv-auth-r2-tree-") as tmp:
            work = Path(tmp)
            shutil.copytree(EXTRACTED, work, dirs_exist_ok=True)
            execute(work)
        mode = "árbol extraído verificado por SHA-256 individual"

    print(f"\nRESULTADO: {mode}; 78/78 reproducido; 96 % reproducido; contrato diagnóstico superado.")


if __name__ == "__main__":
    main()
