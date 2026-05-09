# -*- coding: utf-8 -*-
# © 2026. Todos los derechos reservados. | Juan Antonio Lloret Egea | ORCID: 0000-0002-6634-3351
# Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA)
# IA eñ™ — La Biblia de la IA™ | ISSN 2695-6411 | Licencia CC BY-NC-ND 4.0 | Madrid, 2026
# Advertencia: esta publicación está protegida por CEDRO. Uso comercial prohibido sin autorización.
#
# Runner maestro — Catálogo de Pares Estructurales SV (CPS-SV)
# Referencia doctrinal: §4 (enumeración), §6 (invariantes)
#
# Uso:
#   python3 runner_cps.py                          # CSV por defecto en ./tabla2_sv443.csv
#   python3 runner_cps.py /ruta/tabla2_sv443.csv   # CSV explícito
#   python3 runner_cps.py --tabla2 /ruta/t2.csv --salida /ruta/cps.csv
#
# Salida: JSON con estado APTO/FALLO + recuento de pares por dictamen + errores

import sys, json, time, argparse
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from sv_cps import (cargar_tabla2, enumerar_cps, verificar_invariantes,
                    escribir_csv, N_ELEMENTOS, N_PARES,
                    LAMBDA_M, LAMBDA_C, LAMBDA_RHO, LAMBDA_Mj, LAMBDA_IP)

# ── Argumentos ────────────────────────────────────────────────────────────────
parser = argparse.ArgumentParser(
    description="Runner CPS-SV — genera y verifica el Catálogo de Pares Estructurales SV")
parser.add_argument('--tabla2', default='tabla2_sv443.csv',
                    help='Ruta al CSV de Tabla 2 (default: tabla2_sv443.csv)')
parser.add_argument('--salida', default='catalogo_pares_sv443.csv',
                    help='Ruta de salida del CPS-SV (default: catalogo_pares_sv443.csv)')
parser.add_argument('positional', nargs='?',
                    help='Ruta al CSV de Tabla 2 (argumento posicional alternativo)')
args = parser.parse_args()

ruta_t2  = Path(args.positional if args.positional else args.tabla2)
ruta_out = Path(args.salida)

resultado = {
    "corpus":     "Sistema Vectorial SV",
    "laboratorio":"CPS-SV — Catálogo de Pares Estructurales SV",
    "referencia": "§4, §6 — DOI pendiente de asignación",
    "tabla2":     str(ruta_t2),
    "salida":     str(ruta_out),
    "umbrales": {
        "Lambda_M":   LAMBDA_M,
        "Lambda_C":   LAMBDA_C,
        "Lambda_rho": LAMBDA_RHO,
        "Lambda_Mj":  LAMBDA_Mj,
        "Lambda_IP":  LAMBDA_IP,
    },
    "errores": []
}

# ── Fase 1: Carga y validación de Tabla 2 ─────────────────────────────────────
t0 = time.time()
datos, errores_carga = cargar_tabla2(ruta_t2)
resultado["errores"].extend(errores_carga)

if errores_carga:
    resultado["estado"] = "FALLO"
    resultado["fase_fallo"] = "CARGA"
    print(json.dumps(resultado, indent=2, ensure_ascii=False))
    sys.exit(1)

resultado["elementos_cargados"] = len(datos)

# ── Fase 2: Enumeración del dominio completo ───────────────────────────────────
filas = enumerar_cps(datos)
t1 = time.time()
resultado["pares_enumerados"] = len(filas)
resultado["tiempo_enumeracion_s"] = round(t1 - t0, 2)

# Recuento exacto por dictamen
conteo = {"APTO-M": 0, "APTO-C": 0, "APTO-I": 0, "NO-APTO": 0}
for f in filas:
    conteo[f[4]] += 1
resultado["recuento_exacto"] = conteo
resultado["apto_total"] = conteo["APTO-M"] + conteo["APTO-C"] + conteo["APTO-I"]

# ── Fase 3: Verificación de invariantes (§6.4) ────────────────────────────────
errores_inv = verificar_invariantes(filas)
resultado["errores"].extend(errores_inv)

# ── Fase 4: Escritura y verificación del CSV de salida ────────────────────────
errores_csv = escribir_csv(filas, ruta_out)
resultado["errores"].extend(errores_csv)

# ── Resultado final ────────────────────────────────────────────────────────────
resultado["errores_totales"] = len(resultado["errores"])
resultado["estado"] = "APTO" if not resultado["errores"] else "FALLO"

if resultado["estado"] == "APTO":
    resultado["dictamen_laboratorio"] = (
        f"CPS-SV generado y verificado: {N_PARES} pares, "
        f"{conteo['APTO-M']} APTO-M, {conteo['APTO-C']} APTO-C, "
        f"{conteo['APTO-I']} APTO-I, {conteo['NO-APTO']} NO-APTO. "
        f"Todos los invariantes de §6.4 verificados."
    )

print(json.dumps(resultado, indent=2, ensure_ascii=False))
sys.exit(0 if resultado["estado"] == "APTO" else 1)
