# Figuras

## Finalidad

Esta carpeta reúne las **imágenes estructurales** asociadas al paper de semántica. No se trata de ornamentación, sino de apoyo visual controlado a la arquitectura del artículo.

## Contenido

Se espera encontrar, al menos:

- `portada_semantica_sv_1200x800.png`  
  Imagen principal del artículo, preparada para uso editorial y visualización en plataforma.

- `fig_01_sv93_particion_exhaustiva.png`  
  Visualización de la partición exhaustiva del espacio ternario en la célula meta SV(9,3)-IA.

- `fig_02_trayectorias_u.png`  
  Representación de trayectorias estructurales de `U`.

- `fig_03_verificacion_geometrica_auxiliar.png`  
  Apoyo visual para la verificación geométrica auxiliar.

- `fig_04_tres_vallas.png`  
  Esquema del régimen metodológico de tres vallas.

## Criterio metodológico

Las figuras de esta carpeta deben cumplir una regla fuerte: **hacer visible algo estructuralmente relevante**. No deben sustituir la formalización ni introducir ruido visual ajeno al marco del artículo.

## Compatibilidad de rutas

Dado que el manuscrito se encuentra en `../manuscrito/`, las referencias desde el Markdown deben apuntar, por regla general, a:

`../figuras/<nombre_del_archivo>`

## Recomendación

Cuando se regenere una figura mediante código, conviene:
- preservar el nombre del archivo si ya está enlazado en el manuscrito;
- o, si cambia el nombre, actualizar inmediatamente las rutas del paper para evitar roturas en GitHub o PubPub.
