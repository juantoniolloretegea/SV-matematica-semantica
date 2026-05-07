"""
Runner unificado de los laboratorios reproducibles del documento de
interacción, intercomposición y transmisión factual entre campos en el
Sistema Vectorial SV.

Ejecuta veintiocho laboratorios en orden secuencial bajo régimen fail-fast.
El runner evalúa el código de salida de cada laboratorio y evita alterar su
contenido matemático interno.

Resultado esperado: 28/28 laboratorios superados.

Autoría / Authorship
-------------------
© 2026 Juan Antonio Lloret Egea. Todos los derechos reservados / All rights reserved.
ORCID: 0000-0002-6634-3351
Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA)
IA eñ™ — La Biblia de la IA™
ISSN 2695-6411
Licencia / License: CC BY-NC-ND 4.0
"""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

LABORATORIOS = [
    ("LAB-01", "LAB-01_compuerta_sigma.py", "Compuerta Σ = 1 / Σ = 0"),
    ("LAB-02", "LAB-02_exclusion_herramientas.py", "Exclusión de herramientas Σ = 0"),
    ("LAB-03", "LAB-03_metrologia_solo_medida.py", "Subordinación operativa de la metrología"),
    ("LAB-04", "LAB-04_asimetria_dirigida.py", "Asimetría direccional"),
    ("LAB-05", "LAB-05_no_composicion_superior.py", "No composición superior"),
    ("LAB-06", "LAB-06_residual_interaccion.py", "Cinco tipos de residual"),
    ("LAB-07", "LAB-07_preservacion_U.py", "Preservación de U"),
    ("LAB-08", "LAB-08_funcion_ordinal.py", "Función ordinal de campo"),
    ("LAB-09", "LAB-09_ciclo_suceso.py", "Ciclo de Suceso"),
    ("LAB-10", "LAB-10_fourier_factual_posterior.py", "Mapeo Fourier factual posterior"),
    ("LAB-11", "LAB-11_distancia_factual_fibrosa.py", "Distancia factual fibrosa local"),
    ("LAB-12", "LAB-12_distancia_global_T1.py", "Distancia global y Teorema T1"),
    ("LAB-13", "LAB-13_defecto_telescopico.py", "Defecto telescópico"),
    ("LAB-14", "LAB-14_perfiles_distancia.py", "Comparación de perfiles"),
    ("LAB-15", "LAB-15_distancia_intercampo.py", "Distancia intercampo"),
    ("LAB-16", "LAB-16_uso_indebido.py", "Uso indebido de distancia factual"),
    ("LAB-17", "LAB-17_celula_mal_formada.py", "Célula SV(36,6) mal formada"),
    ("LAB-18", "LAB-18_misma_D_perfil_distinto.py", "Misma distancia global, perfil distinto"),
    ("LAB-T01", "LAB-T01_codificacion_celula.py", "Codificación y reconstrucción de célula"),
    ("LAB-T02", "LAB-T02_preservacion_U_transmision.py", "Preservación de U en transmisión"),
    ("LAB-T03", "LAB-T03_alteracion_orden.py", "Alteración de orden de parámetros"),
    ("LAB-T04", "LAB-T04_distorsion_d.py", "Distorsión local"),
    ("LAB-T05", "LAB-T05_distorsion_D.py", "Distorsión global"),
    ("LAB-T06", "LAB-T06_perdida_trayectoria.py", "Pérdida de trayectoria"),
    ("LAB-T07", "LAB-T07_perdida_frontera.py", "Pérdida de frontera"),
    ("LAB-T08", "LAB-T08_residual_global.py", "Residual global"),
    ("LAB-T09", "LAB-T09_capacidad.py", "Capacidad factual de transmisión"),
    ("LAB-T10", "LAB-T10_comparacion_shannon.py", "Comparación con canal Shannon"),
]


def ejecutar(codigo: str, fichero: str, etiqueta: str) -> bool:
    base = Path(__file__).resolve().parent
    ruta = base / fichero
    if not ruta.exists():
        print(f"✗ {codigo}: no existe {fichero}")
        return False
    env = os.environ.copy()
    env.setdefault("OPENBLAS_NUM_THREADS", "1")
    env.setdefault("OMP_NUM_THREADS", "1")
    try:
        resultado = subprocess.run(
            [sys.executable, str(ruta)],
            cwd=str(base),
            stdout=subprocess.DEVNULL,
            stderr=subprocess.PIPE,
            text=True,
            timeout=90,
            env=env,
        )
    except subprocess.TimeoutExpired:
        print(f"✗ {codigo}: tiempo máximo superado")
        return False
    if resultado.returncode == 0:
        print(f"✓ {codigo}: {etiqueta}")
        return True
    print(f"✗ {codigo}: {etiqueta}")
    if resultado.stderr:
        print(resultado.stderr.strip())
    return False


def main() -> int:
    print("Runner unificado — Interacción, intercomposición y transmisión factual entre campos")
    print(f"Laboratorios declarados: {len(LABORATORIOS)}")
    superados = 0
    for codigo, fichero, etiqueta in LABORATORIOS:
        if not ejecutar(codigo, fichero, etiqueta):
            print(f"Resultado global: {superados}/{len(LABORATORIOS)} laboratorios superados")
            return 1
        superados += 1
    print(f"Resultado global: {superados}/{len(LABORATORIOS)} laboratorios superados")
    print("APTO — verificación completa")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
