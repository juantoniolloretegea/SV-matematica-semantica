# Código

## Finalidad

Esta carpeta contiene los **scripts de generación de figuras y apoyo experimental** del paper de semántica. Su estatuto no es decorativo: forman parte de la trazabilidad del trabajo y de la posibilidad de reproducir ciertos resultados visuales o estructurales.

## Contenido esperado

Los scripts actuales deben corresponder, al menos, a:

- generación de la partición exhaustiva del espacio SV(9,3)-IA;
- generación de trayectorias estructurales de `U`;
- verificación geométrica auxiliar;
- esquema del régimen experimental de tres vallas.

## Criterio de uso

El código aquí depositado debe ser:
- legible,
- ejecutable sin dependencias opacas,
- y estable respecto de los nombres de salida que ya estén enlazados desde el manuscrito.

## Relación con el paper

El código no reemplaza la argumentación teórica, pero sí sostiene la capa de:
- reproducibilidad,
- regeneración de figuras,
- y control sobre cambios editoriales.

## Recomendación de mantenimiento

Si se modifique un script:
1. regenere la figura correspondiente;
2. confirme que el nombre de salida no rompe los enlaces del manuscrito;
3. deje constancia del cambio en commit o registro auxiliar.
