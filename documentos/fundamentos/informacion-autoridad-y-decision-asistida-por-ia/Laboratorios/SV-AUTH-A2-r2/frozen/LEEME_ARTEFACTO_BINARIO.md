# Artefacto binario r2

El artefacto citado por la publicación tiene nombre:

`SV_AUTH_A2_revised_reference_r2_20260813.zip`

SHA-256:

`7c18761cf5546c8fdd9ad962c0ea3e0a54a9ddd4a4bf6d43c0ab29c7e4cf794f`

La API utilizada para preparar este laboratorio no permitió transferir el ZIP binario. Por ello el repositorio contiene desde el primer commit **todos los ficheros extraídos exactos** y `reports/manifest_contenido_r2.txt`, que fija el SHA-256 individual de cada fichero contenido en el ZIP original.

`ejecutar_laboratorio.py` funciona en ambos regímenes:

1. si el ZIP está presente en esta carpeta, exige primero el SHA-256 global y ejecuta desde una extracción temporal;
2. si todavía no está presente, exige que los SHA-256 de todos los ficheros de `extracted/` coincidan con el manifiesto del ZIP y ejecuta desde una copia temporal de ese árbol.

Para completar la cadena binaria puede añadirse manualmente el ZIP exacto a esta carpeta **sin cambiar ningún otro fichero**. El script lo detectará automáticamente.
