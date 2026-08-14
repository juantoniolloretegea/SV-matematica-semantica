# Laboratorio reproducible — SV-AUTH A.2 r2

Este laboratorio acompaña a la publicación española **«La sustitución en el plano de la información no transfiere autoridad en sistemas de decisión asistidos por IA»**.

Su finalidad es permitir que un lector compruebe de forma independiente las cifras de evidencia operacional citadas en el artículo y, adicionalmente, audite la clase diagnóstica de casos negativos representativos.

## 1. Regla de integridad

El objeto binario citado por la publicación es:

`frozen/SV_AUTH_A2_revised_reference_r2_20260813.zip`

SHA-256:

`7c18761cf5546c8fdd9ad962c0ea3e0a54a9ddd4a4bf6d43c0ab29c7e4cf794f`

**El ZIP congelado no debe modificarse.** Cualquier ampliación del laboratorio vive fuera de él y no altera las cifras 78/78 y 96 % atribuidas al r2.

La carpeta `frozen/extracted/` contiene los ficheros exactos del ZIP y `reports/manifest_contenido_r2.txt` fija su SHA-256 individual. Si el ZIP está presente, el script verifica el hash global y ejecuta desde una extracción temporal. Si el ZIP todavía no está alojado, verifica todos los hashes individuales y ejecuta desde una copia temporal del árbol extraído. En ambos casos se evita confiar silenciosamente en ficheros alterados.

## 2. Qué contiene

- `frozen/`: artefacto r2 exacto y copia extraída para lectura.
- `reports/`: salidas reproducidas de pytest y cobertura.
- `diagnosticos/`: catálogo de errores y contrato suplementario de códigos de rechazo.
- `ejecutar_laboratorio.py`: reproducción integral y automática.
- `requirements.txt`: versiones de herramientas usadas para fijar la reproducción.
- `manifest.json`: valores esperados y trazabilidad de la ejecución.

## 3. Reproducción

Requisitos recomendados:

- Python 3.13;
- `pytest==9.0.2`;
- `coverage==7.13.3`.

Desde esta carpeta:

```bash
python -m venv .venv
# Linux/macOS
source .venv/bin/activate
# Windows PowerShell
# .venv\Scripts\Activate.ps1

python -m pip install -r requirements.txt
python ejecutar_laboratorio.py
```

La ejecución debe acreditar por separado:

```text
78 passed, 0 failed
537 sentencias, 24 no cubiertas, 96 %
```

Después ejecuta un contrato diagnóstico suplementario. Sus pruebas **no se suman** a las 78 del artículo.

## 4. Por qué existe un contrato diagnóstico adicional

La batería r2 impide que los casos negativos ensayados sean aceptados silenciosamente: si una operación que debe rechazarse no lanza `AuthError`, el test falla. Sin embargo, varias pruebas originales sólo exigen la clase general `AuthError` y no fijan el código exacto.

El módulo `diagnosticos/test_contrato_diagnostico.py` añade una obligación distinta: un conjunto representativo de fallos debe devolver el código diagnóstico concreto (`E601`, `E602`, etc.). De este modo se distingue entre:

1. **rechazo operacional**, que ya pertenece al r2 sellado; y
2. **clasificación diagnóstica del rechazo**, que se audita aquí como capa suplementaria.

Esta segunda capa no se utiliza para demostrar TA, TB o IS y no modifica el artefacto citado.

## 5. Catálogo de errores

`diagnosticos/catalogo_errores_auth.json` documenta los códigos emitidos por `authority_runtime.py` en r2. `E614` y `E616` quedan marcados como reservados/no emitidos.

El runtime AUTH, no el resolvedor semántico, es quien rechaza las transiciones no admisibles mediante guardas y precondiciones de las reglas operacionales. El resolvedor conserva su función semántica propia y no debe describirse como un motor universal de errores.

## 6. Alcance

Este laboratorio aporta **reproducibilidad y conformidad ejecutable**. No convierte la cobertura en una prueba de seguridad universal, no autentica físicamente a personas, no prueba criptografía/host/hardware y no afirma integración con un motor productivo.

Las demostraciones TA, TB e IS pertenecen a la semántica sellada; las pruebas ejecutables son evidencia de conformidad de la realización de referencia.

## 7. Preparación para Code Ocean

La estructura está deliberadamente preparada para ser trasladada sin alterar el r2 a una cápsula reproducible. En Code Ocean debe mantenerse el mismo ZIP y verificarse el mismo SHA-256 antes de ejecutar `ejecutar_laboratorio.py`.
