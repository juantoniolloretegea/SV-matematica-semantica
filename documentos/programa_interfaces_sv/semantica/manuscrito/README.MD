# Manuscrito

## Finalidad

Esta carpeta contiene los **textos nucleares de la publicación** del carril de semántica. Su función es preservar tanto el documento editable como el testigo de la publicación efectivamente visible.

## Contenido esperado

- `paper_sv_semantica_pubpub.md`  
  Manuscrito principal en Markdown, adaptado para flujo conservador de importación o copia/pegado en PubPub.

- `paper_sv_semantica_publicado_pubpub.html`  
  Testigo descargado de la publicación ya visible en plataforma, útil para contrastar renderizado, cierre efectivo y consistencia editorial.

## Criterio de uso

El archivo Markdown es la **pieza viva** para:
- correcciones de texto,
- ajustes de rutas de imagen,
- inserción de referencias,
- y nuevas versiones editoriales.

El archivo HTML funciona como **testigo publicado**, no como fuente primaria de edición.

## Recomendación práctica

Antes de modificar el manuscrito, conviene:
1. comparar el `.md` con el `.html`;
2. verificar que el bloque final de referencias está presente;
3. comprobar que las imágenes apuntan correctamente a `../figuras/`;
4. documentar en commit cualquier cambio que afecte al texto ya publicado.
