# -*- coding: utf-8 -*-
# © 2026. Todos los derechos reservados. | Juan Antonio Lloret Egea | ORCID: 0000-0002-6634-3351
# Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA)
# IA eñ™ — La Biblia de la IA™ | ISSN 2695-6411 | Licencia CC BY-NC-ND 4.0 | Madrid, 08/05/2026
# Advertencia: esta publicación está protegida por CEDRO. Uso comercial prohibido sin autorización.
#
# Runner de verificación del catálogo SV-443
# Ejecutar desde la carpeta laboratorios/: python3 runner.py
# El CSV debe encontrarse en ../elementos-materiales-nueva-generacion.csv
# o bien pasar la ruta como argumento: python3 runner.py /ruta/al/csv

import sys
import json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / "src"))
from sv_443 import verificar_todo, N_ELEMENTOS, N_COLUMNAS

# ── Localización del CSV ───────────────────────────────────────────────────────
if len(sys.argv) > 1:
    ruta_csv = Path(sys.argv[1])
else:
    # Por defecto: una carpeta por encima del laboratorio
    ruta_csv = Path(__file__).parent.parent.parent / "elementos_sv_443.csv"
    if not ruta_csv.exists():
        # Intentar en la carpeta hermana del laboratorio
        ruta_csv = Path(__file__).parent.parent / "elementos_sv_443.csv"

if not ruta_csv.exists():
    print(json.dumps({
        "error": "SV-443-LOAD: CSV no encontrado. "
                 "Pasar la ruta como argumento: python3 runner.py /ruta/csv",
        "estado": "FALLO"
    }, indent=2, ensure_ascii=False))
    sys.exit(1)

# ── Verificación ───────────────────────────────────────────────────────────────
errores = verificar_todo(ruta_csv)

# Clasificar errores por tipo
formulas = [e for e in errores if any(
    c in e for c in ["-Z-", "-A-", "-P-", "-G-", "-ORDEN"])]
rangos   = [e for e in errores if any(
    c in e for c in ["-DENS-", "-CONDUCT-", "-EN-", "-EI-", "-RADIO-",
                     "-AFIN-", "-METAL-", "-KTERM-", "-MUR-", "-MOHS-",
                     "-RES-", "-ROZ-", "-FLEX-", "-MALE-", "-OXID-",
                     "-CORR-", "-TMAX-", "-VOL-", "-RAD-", "-ISO-",
                     "-FLOAT-"])]
textos   = [e for e in errores if any(
    c in e for c in ["-ESTADO-", "-VACIO-", "-FUNC-", "-APLIC-"])]
otros    = [e for e in errores
            if e not in formulas and e not in rangos and e not in textos]

resultado = {
    "csv_verificado":      str(ruta_csv),
    "elementos_esperados": N_ELEMENTOS,
    "columnas_esperadas":  N_COLUMNAS,
    "errores_totales":     len(errores),
    "errores_formula":     len(formulas),
    "errores_rango":       len(rangos),
    "errores_texto":       len(textos),
    "errores_otros":       len(otros),
    "estado":              "APTO" if not errores else "FALLO",
}

if errores:
    resultado["detalle_errores"] = errores  # TODOS, sin excepción
    print(json.dumps(resultado, indent=2, ensure_ascii=False))
    sys.exit(1)
else:
    resultado["elementos_verificados"] = f"{N_ELEMENTOS}/{N_ELEMENTOS}"
    print(json.dumps(resultado, indent=2, ensure_ascii=False))
