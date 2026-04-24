#!/usr/bin/env python3
"""
runner.py — Ejecutor maestro de los 22 laboratorios L-LUZ-01 a L-LUZ-22 del
régimen luminoso factual en el Sistema Vectorial SV.

Fuente canónica: Lloret Egea, J. A. (2026). Teoría general factual de la luz
en el Sistema Vectorial SV. ISSN 2695-6411.

Política estricta (idéntica al patrón del bloque termodinámico 2026l):

  1. Carga el catálogo canónico de errores y verifica unicidad de códigos
     (LUZ-CFG-002 si hay duplicados).
  2. Carga la configuración `runner_config.json` y verifica:
     — el orden declarado contiene exactamente 22 laboratorios
     — cada archivo existe físicamente
     — no hay ids duplicados
     (LUZ-CFG-003 si cualquiera falla).
  3. Ejecuta cada laboratorio vía subprocess, separando stdout/stderr.
  4. NO captura excepciones con `except:` genérico. Cada fallo de subprocess
     se reporta con su returncode y el último fragmento útil de stdout/stderr.
  5. Al primer laboratorio que falla, detiene la ejecución y reporta código.
  6. exit(0) SOLO si los 22 laboratorios pasan íntegramente.
  7. Detección de pases silenciosos:
     — si 'FALLO' aparece en stdout pese a exit=0 → LUZ-LAB-002
     — si la última línea no contiene 'PASADO' → LUZ-LAB-002
     — si stdout está vacío → LUZ-LAB-001
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


# ---------------------------------------------------------------------------
# UTILIDADES
# ---------------------------------------------------------------------------

def fatal(codigo: str, mensaje: str) -> None:
    """Termina el runner con código específico del catálogo. Sin except silencioso."""
    print(f"\n{'=' * 74}")
    print(f"[RUNNER] FALLO FATAL — código = {codigo}")
    print(f"         mensaje: {mensaje}")
    print(f"{'=' * 74}")
    sys.exit(1)


def cargar_json(path: Path, codigo_io: str) -> dict:
    """Carga un JSON levantando código específico si falla."""
    if not path.is_file():
        fatal("LUZ-CFG-001", f"Archivo requerido no encontrado: {path}")
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        fatal(codigo_io, f"JSON inválido en {path}: {e}")
    except UnicodeDecodeError as e:
        fatal("LUZ-IO-003", f"Encoding distinto de UTF-8 en {path}: {e}")


# ---------------------------------------------------------------------------
# VERIFICACIÓN DEL CATÁLOGO
# ---------------------------------------------------------------------------

def verificar_unicidad_codigos(catalogo: dict) -> int:
    """Comprueba que todos los códigos del catálogo son únicos y no triviales."""
    codigos = catalogo.get("codigos", {})
    if not isinstance(codigos, dict):
        fatal("LUZ-CFG-001", "La clave 'codigos' del catálogo debe ser un diccionario.")
    if len(codigos) == 0:
        fatal("LUZ-CFG-001", "Catálogo vacío.")
    if len(codigos) != len(set(codigos.keys())):
        fatal("LUZ-CFG-002", "Catálogo contiene códigos duplicados.")
    for cod, mensaje in codigos.items():
        if not mensaje or not isinstance(mensaje, str):
            fatal("LUZ-CFG-001", f"Código {cod} sin mensaje válido.")
        if not cod.startswith("LUZ-"):
            fatal("LUZ-CFG-002",
                  f"Código {cod} sin prefijo canónico 'LUZ-'. "
                  "Todos los códigos deben empezar por LUZ-.")
    print(f"  [CFG OK] Catálogo con {len(codigos)} códigos únicos, todos con prefijo LUZ-.")
    return len(codigos)


# ---------------------------------------------------------------------------
# VERIFICACIÓN DE LA CONFIGURACIÓN DE LABORATORIOS
# ---------------------------------------------------------------------------

def verificar_orden_laboratorios(config: dict) -> list:
    """Comprueba que los 22 laboratorios declarados existen y son únicos."""
    orden = config.get("orden_laboratorios", [])
    if len(orden) != 22:
        fatal("LUZ-CFG-003",
              f"Se esperaban 22 laboratorios; se declaran {len(orden)}.")
    ids_vistos = set()
    archivos_vistos = set()
    for entrada in orden:
        lab_id = entrada.get("id")
        archivo = entrada.get("archivo")
        if not lab_id or not archivo:
            fatal("LUZ-CFG-003",
                  f"Entrada sin id o archivo: {entrada}")
        if lab_id in ids_vistos:
            fatal("LUZ-CFG-003", f"Laboratorio con id duplicado: {lab_id}")
        if archivo in archivos_vistos:
            fatal("LUZ-CFG-003", f"Archivo duplicado en configuración: {archivo}")
        ids_vistos.add(lab_id)
        archivos_vistos.add(archivo)
        ruta = AQUI / archivo
        if not ruta.is_file():
            fatal("LUZ-CFG-003",
                  f"Laboratorio {lab_id}: archivo '{archivo}' no encontrado en {AQUI}.")
    print(f"  [CFG OK] 22 laboratorios declarados, todos presentes, sin duplicados.")
    return orden


# ---------------------------------------------------------------------------
# EJECUCIÓN DE UN LABORATORIO
# ---------------------------------------------------------------------------

def extraer_codigo_del_stdout(stdout: str) -> str:
    """
    Extrae el código de error del stdout del laboratorio. El formato canónico
    es 'FALLO código=LUZ-XXX-NNN'. Si no aparece, devuelve LUZ-LAB-001 como
    código genérico (sólo se usa cuando el laboratorio falla sin emitir código).
    """
    for line in stdout.splitlines():
        if "FALLO código=" in line:
            try:
                codigo = line.split("FALLO código=")[1].strip().split()[0].rstrip(",")
                return codigo
            except IndexError:
                return "LUZ-LAB-001"
    return "LUZ-LAB-001"


def ejecutar_lab(lab: dict, idx_total: int, total_labs: int) -> None:
    """
    Ejecuta un laboratorio vía subprocess. Política estricta:
      — si returncode != 0 → fatal(código_del_stdout)
      — si stdout contiene 'FALLO' sin 'PASADO' al final → LUZ-LAB-002
      — si última línea no contiene 'PASADO' → LUZ-LAB-002
      — si stdout está vacío → LUZ-LAB-001
    """
    archivo = lab["archivo"]
    lab_id  = lab["id"]
    tema    = lab["tema"]
    teorema = lab["teorema"]
    ruta = AQUI / archivo

    print(f"\n  ─── {idx_total:02d}/{total_labs} — {lab_id} — Teorema {teorema}")
    print(f"       tema:    {tema}")
    print(f"       archivo: {archivo}")

    t0 = time.time()
    try:
        proc = subprocess.run(
            [sys.executable, str(ruta)],
            cwd=str(AQUI),
            capture_output=True,
            text=True,
            timeout=180,
        )
    except subprocess.TimeoutExpired:
        fatal("LUZ-LAB-001",
              f"Laboratorio {lab_id}: timeout superado (>180s). Ejecución abortada.")
    elapsed = time.time() - t0

    stdout = proc.stdout or ""
    stderr = proc.stderr or ""

    # Caso 1: returncode ≠ 0
    if proc.returncode != 0:
        codigo = extraer_codigo_del_stdout(stdout)
        print(f"\n  [RUNNER] {lab_id} terminó con exit={proc.returncode}")
        print(f"  ─── stdout (últimas 12 líneas) ───")
        for l in stdout.splitlines()[-12:]:
            print(f"    {l}")
        if stderr.strip():
            print(f"  ─── stderr (últimas 8 líneas) ───")
            for l in stderr.splitlines()[-8:]:
                print(f"    {l}")
        fatal(codigo, f"Laboratorio {lab_id} falló (exit={proc.returncode}).")

    # Caso 2: returncode 0 pero stdout vacío
    lineas_utiles = [l for l in stdout.splitlines() if l.strip()]
    if not lineas_utiles:
        fatal("LUZ-LAB-001",
              f"Laboratorio {lab_id}: stdout vacío pese a exit=0 (ejecución sospechosa).")

    # Caso 3: 'FALLO código=' aparece en stdout (pase silencioso)
    if "FALLO código=" in stdout:
        codigo = extraer_codigo_del_stdout(stdout)
        fatal("LUZ-LAB-002",
              f"Laboratorio {lab_id}: 'FALLO código={codigo}' detectado en stdout "
              f"pese a exit=0. Pase silencioso.")

    # Caso 4: la última línea no contiene 'PASADO'
    ultima = lineas_utiles[-1]
    if "PASADO" not in ultima:
        fatal("LUZ-LAB-002",
              f"Laboratorio {lab_id}: última línea no contiene 'PASADO': "
              f"'{ultima[:120]}'")

    # Éxito
    print(f"       ✓ {ultima}  ({elapsed:.2f}s)")


# ---------------------------------------------------------------------------
# PUNTO DE ENTRADA
# ---------------------------------------------------------------------------

def main() -> int:
    print("=" * 74)
    print("RUNNER — Régimen luminoso factual en el Sistema Vectorial SV")
    print("Fuente: Lloret Egea (2026). Teoría general factual de la luz.")
    print("=" * 74)

    print("\n[1/3] Verificación de prerrequisitos:")
    catalogo = cargar_json(CATALOGO_PATH, "LUZ-IO-001")
    n_cod = verificar_unicidad_codigos(catalogo)
    config = cargar_json(CONFIG_PATH, "LUZ-IO-001")
    orden = verificar_orden_laboratorios(config)

    print(f"\n[2/3] Ejecución secuencial de los {len(orden)} laboratorios:")
    t0_total = time.time()
    for idx, lab in enumerate(orden, start=1):
        ejecutar_lab(lab, idx, len(orden))
    elapsed_total = time.time() - t0_total

    print("\n[3/3] Resumen final:")
    print("=" * 74)
    print(f"  RUNNER COMPLETADO — {len(orden)}/{len(orden)} laboratorios pasados en {elapsed_total:.2f}s.")
    print(f"  Ningún código de error activado sobre {n_cod} códigos canónicos.")
    print(f"  El régimen luminoso factual SV queda verificado ejecutablemente.")
    print("=" * 74)
    return 0


if __name__ == "__main__":
    sys.exit(main())
