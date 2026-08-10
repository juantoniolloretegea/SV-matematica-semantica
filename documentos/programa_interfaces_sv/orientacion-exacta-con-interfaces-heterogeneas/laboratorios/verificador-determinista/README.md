# Laboratorio reproducible — verificador determinista

Laboratorio asociado a la publicación:

**Orientación exacta con interfaces heterogéneas: constitución del episodio y sustitución que preserva la clausura**

Preprint ITVIA: **DOI 10.21428/39829d0b.e5347310**

Este directorio contiene el verificador determinista utilizado para reproducir la evaluación formal finita de la publicación. El laboratorio implementa los objetos formales necesarios para comprobar mecánicamente la suite adversarial F1–F8 y la familia canónica de escalado descritas en la sección de evaluación reproducible.

## Contenido

- `supplementary_verifier.py`: verificador determinista completo.
- `verification_output.txt`: salida de referencia obtenida al ejecutar el verificador.
- `LICENSE`: licencia MIT aplicable al código de este laboratorio.

## Requisitos

- Python 3.
- No requiere paquetes externos.
- No requiere conjuntos de datos externos.

## Ejecución

En GNU/Linux, macOS o cualquier entorno con `python3`:

```text
python3 supplementary_verifier.py
```

En Windows, si Python está registrado como `python`:

```text
python supplementary_verifier.py
```

La ejecución correcta debe comenzar con:

```text
Formal adversarial suite: 8/8 scenarios verified.
```

A continuación se muestran los resultados de F1–F8 y la familia canónica de escalado para `k = 2, …, 8`. La salida íntegra de referencia se conserva en `verification_output.txt`.

## Qué verifica

El programa implementa contratos finitos guardados, verificación local de testigos, compatibilidad estructural conjunta, enumeración de bases constitutivas, congruencia contextual de resolución, vectores de clases locales, firmas globales de resolución, resolutores finitos bruto y cociente, perfiles exactos de clausura alcanzable y las condiciones C2, C3 y C4λ para sustituciones tipadas.

La suite adversarial comprueba de forma separada los siguientes límites del criterio de preservación:

- **F1**: independencia de C2, congruencia local de resolución.
- **F2**: necesidad de congruencia contextual, no sólo coincidencia puntual.
- **F3**: independencia de C3, preservación de bases constitutivas.
- **F4**: independencia de C4λ, completitud de clases locales realizadas.
- **F5**: irrelevancia de testigos inactivos para el certificado de sustitución.
- **F6**: conservación de testigos postransducción legítimos y potencialmente conflictivos.
- **F7**: sustitución física sin igualdad de valores brutos cuando se conserva la clase contextual.
- **F8**: suficiencia sin necesidad; puede fallar el criterio suficiente y conservarse el mismo perfil exacto.

La familia de escalado compara, para `k = 2, …, 8`, el número de bases físicas `4^k` con el número de firmas semánticas `2^k`, mostrando la reducción exacta obtenida por el cociente.

## Alcance

Este laboratorio **no sustituye las demostraciones matemáticas de la publicación**. Su función es reproducir mecánicamente las construcciones finitas, los escenarios adversariales y los recuentos declarados. No constituye una evaluación empírica de navegación física, sensores, calibración, latencia ni rendimiento robótico.

## Correspondencia con la publicación

El laboratorio corresponde a la sección de evaluación reproducible de la publicación. Los identificadores F1–F8 y la familia de escalado conservan la misma semántica que en el texto principal.

## Integridad de la ejecución de referencia

La salida incluida en `verification_output.txt` se generó directamente mediante:

```text
python3 supplementary_verifier.py
```

El proceso finaliza sin errores y verifica los ocho escenarios formales.
