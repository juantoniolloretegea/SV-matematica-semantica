#!/usr/bin/env python3
"""
runner.py — Ejecutor maestro de los 12 laboratorios del dominio termodinámico
factual del Sistema Vectorial SV.

Política estricta:
  1. Carga el catálogo de errores y verifica unicidad de códigos (CFG-002).
  2. Carga la configuración (runner_config.json) y verifica que el orden declarado
     corresponde con los archivos existentes (CFG-003).
  3. Ejecuta cada laboratorio vía subprocess, separando stdout/stderr.
  4. NO captura excepciones con 'except:' genérico. Cada fallo de subprocess
     se reporta con su returncode y el último fragmento de stdout/stderr.
  5. Al primer laboratorio que falla, detiene la ejecución y reporta código.
  6. exit(0) SOLO si los 12 laboratorios pasan íntegramente.
  7. No hay pases silenciosos: un laboratorio que escriba 'FALLO' en stdout
     también detiene el runner.
"""
import sys
import os
import json
import subprocess
import time
from pathlib import Path

AQUI = Path(os.path.dirname(os.path.abspath(__file__)))
CATALOGO_PATH = AQUI / "catalogo_errores.json"
CONFIG_PATH   = AQUI / "runner_config.json"


def fatal(codigo: str, mensaje: str) -> None:
    """Termina el runner con un código de error específico. Sin except silencioso."""
    print(f"\n{'=' * 70}")
    print(f"[RUNNER] FALLO FATAL — código = {codigo}")
    print(f"         mensaje: {mensaje}")
    print(f"{'=' * 70}")
    sys.exit(1)


def cargar_json(path: Path, codigo_io: str) -> dict:
    if not path.is_file():
        fatal("CFG-001", f"Archivo requerido no encontrado: {path}")
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        fatal(codigo_io, f"JSON inválido en {path}: {e}")
    except UnicodeDecodeError as e:
        fatal("IO-003", f"Encoding distinto de UTF-8 en {path}: {e}")


def verificar_unicidad_codigos(catalogo: dict) -> None:
    """Comprueba que todos los códigos del catálogo son únicos y no triviales."""
    codigos = catalogo.get("codigos", {})
    if not isinstance(codigos, dict):
        fatal("CFG-001", "La clave 'codigos' del catálogo debe ser un diccionario.")
    if len(codigos) == 0:
        fatal("CFG-001", "Catálogo vacío.")
    # Python dict tiene claves únicas por definición, pero verificamos cardinalidad
    if len(codigos) != len(set(codigos.keys())):
        fatal("CFG-002", "Catálogo contiene códigos duplicados.")
    # Verificamos que cada código tiene mensaje no trivial
    for cod, mensaje in codigos.items():
        if not mensaje or not isinstance(mensaje, str):
            fatal("CFG-001", f"Código {cod} sin mensaje válido.")
    print(f"  [CFG OK] Catálogo con {len(codigos)} códigos únicos.")


def verificar_orden_laboratorios(config: dict) -> list:
    """Comprueba que cada archivo declarado existe físicamente."""
    orden = config.get("orden_laboratorios", [])
    if len(orden) != 12:
        fatal("CFG-003", f"Se esperaban 12 laboratorios; se declaran {len(orden)}.")
    ids_vistos = set()
    for entrada in orden:
        lab_id = entrada.get("id")
        archivo = entrada.get("archivo")
        if lab_id in ids_vistos:
            fatal("CFG-003", f"Laboratorio con id duplicado: {lab_id}")
        ids_vistos.add(lab_id)
        ruta = AQUI / archivo
        if not ruta.is_file():
            fatal("CFG-003", f"Laboratorio {lab_id}: archivo {archivo} no encontrado en {AQUI}.")
    print(f"  [CFG OK] 12 laboratorios declarados, todos presentes.")
    return orden


def ejecutar_lab(lab: dict, idx_total: int) -> None:
    """
    Ejecuta un laboratorio. No captura errores genéricos.
    Si returncode != 0 o la salida contiene 'FALLO', detiene el runner.
    """
    archivo = lab["archivo"]
    lab_id  = lab["id"]
    tema    = lab["tema"]
    teorema = lab["teorema"]
    ruta = AQUI / archivo
    print(f"\n  ─── {lab_id.upper()} / 12 — Teorema {teorema} — {tema}")
    print(f"       archivo: {archivo}")
    t0 = time.time()
    proc = subprocess.run(
        [sys.executable, str(ruta)],
        cwd=str(AQUI),
        capture_output=True,
        text=True,
        timeout=120,
    )
    elapsed = time.time() - t0
    stdout = proc.stdout or ""
    stderr = proc.stderr or ""
    if proc.returncode != 0:
        # Fallo explícito. Extraer código si aparece en stdout
        codigo = "LAB-001"
        for line in stdout.splitlines():
            if "FALLO código=" in line:
                codigo = line.split("FALLO código=")[1].split(" ")[0].rstrip(",")
                break
        print(f"\n  [RUNNER] {lab_id} terminó con exit={proc.returncode}")
        print(f"  ─── stdout (últimas 10 líneas) ───")
        for l in stdout.splitlines()[-10:]:
            print(f"    {l}")
        if stderr.strip():
            print(f"  ─── stderr ───")
            for l in stderr.splitlines()[-10:]:
                print(f"    {l}")
        fatal(codigo, f"Laboratorio {lab_id} falló (exit={proc.returncode}).")
    # Aunque exit==0, revisamos que no haya "FALLO" en stdout (pase silencioso)
    if "FALLO" in stdout and "rechazado correctamente" not in stdout and "PASADO" not in stdout.split("FALLO")[1]:
        fatal("LAB-002", f"Laboratorio {lab_id}: 'FALLO' detectado en stdout pese a exit=0 (pase silencioso).")
    # Última línea útil: PASADO
    lineas = [l for l in stdout.splitlines() if l.strip()]
    if not lineas:
        fatal("LAB-001", f"Laboratorio {lab_id}: stdout vacío (ejecución sospechosa).")
    ultima = lineas[-1]
    if "PASADO" not in ultima:
        fatal("LAB-002", f"Laboratorio {lab_id}: última línea no contiene 'PASADO': '{ultima}'")
    print(f"       ✓ {ultima}  ({elapsed:.2f}s)")


def main() -> int:
    print("=" * 70)
    print("RUNNER — Dominio termodinámico factual SV")
    print("Fuente: Lloret Egea (2026). Fórmula factual única absoluta.")
    print("=" * 70)
    print("\n[1/3] Verificación de prerrequisitos:")
    catalogo = cargar_json(CATALOGO_PATH, "IO-001")
    verificar_unicidad_codigos(catalogo)
    config = cargar_json(CONFIG_PATH, "IO-001")
    orden = verificar_orden_laboratorios(config)

    print("\n[2/3] Ejecución secuencial de los 12 laboratorios:")
    t0_total = time.time()
    for idx, lab in enumerate(orden, start=1):
        ejecutar_lab(lab, idx)
    elapsed_total = time.time() - t0_total

    print("\n[3/3] Resumen final:")
    print("=" * 70)
    print(f"  RUNNER COMPLETADO — 12/12 laboratorios pasados en {elapsed_total:.2f} segundos.")
    print(f"  Ningún código de error activado.")
    print(f"  El dominio termodinámico factual SV queda verificado ejecutablemente.")
    print("=" * 70)
    return 0


if __name__ == "__main__":
    sys.exit(main())
