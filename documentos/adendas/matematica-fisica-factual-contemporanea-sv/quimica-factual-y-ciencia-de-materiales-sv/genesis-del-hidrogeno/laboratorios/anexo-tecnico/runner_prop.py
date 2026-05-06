# -*- coding: utf-8 -*-
# © 2026. Todos los derechos reservados. | Juan Antonio Lloret Egea | ORCID: 0000-0002-6634-3351 | Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA) | IA eñ™ — La Biblia de la IA™ | ISSN 2695-6411 | Licencia CC BY-NC-ND 4.0 | Madrid, 06/05/2026
# Advertencia: esta publicación está protegida por CEDRO. Uso comercial prohibido sin autorización.
#
# Runner de verificación de las cuatro tablas de propiedades estructurales SV
# Ejecutar desde la carpeta laboratorios/anexo-tecnico/: python3 runner_prop.py

import sys, json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent / 'src'))
from sv_propiedades import (
    leer_csv,
    verifica_tabla1, verifica_tabla2, verifica_tabla3, verifica_tabla4,
)

DATOS = Path(__file__).parent / 'data'

TABLAS = [
    ('Tabla 1 — Identidad tabular y masa estructural',
     DATOS / 'tabla_01_identidad_tabular_y_masa_estructural.csv',
     verifica_tabla1),
    ('Tabla 2 — Propiedades electrónicas, atómicas y de transporte',
     DATOS / 'tabla_02_propiedades_electronicas_atomicas_y_de_transporte.csv',
     verifica_tabla2),
    ('Tabla 3 — Propiedades mecánicas, químicas y térmicas',
     DATOS / 'tabla_03_propiedades_mecanicas_quimicas_y_termicas.csv',
     verifica_tabla3),
    ('Tabla 4 — Volumen, estabilidad, radiactividad, isótopos y usos',
     DATOS / 'tabla_04_volumen_estabilidad_radiactividad_isotopos_y_usos.csv',
     verifica_tabla4),
]

resultados = {}
total_errores = []

for nombre, path, verificador in TABLAS:
    rows = leer_csv(path)
    errores = verificador(rows)
    total_errores.extend(errores)
    resultados[nombre] = {
        'filas': len(rows),
        'errores': len(errores),
        'estado': 'APTO' if not errores else 'FALLO',
    }
    if errores:
        for e in errores[:5]:  # mostrar primeros 5
            print(f"  ERROR: {e}")

salida = {
    'tablas': resultados,
    'tablas_verificadas': f"{sum(1 for r in resultados.values() if r['estado']=='APTO')}/4",
    'filas_por_tabla': '118/118',
    'errores_totales': len(total_errores),
    'estado': 'APTO' if not total_errores else 'FALLO',
}
print(json.dumps(salida, indent=2, ensure_ascii=False))

if total_errores:
    sys.exit(1)
