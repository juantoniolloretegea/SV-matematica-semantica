# Laboratorios reproducibles

Autor: Juan Antonio Lloret Egea  
ORCID: 0000-0002-6634-3351  
© 2026. Todos los derechos reservados.  
Licencia: CC BY-NC-ND 4.0  
DOI PubPub: https://doi.org/10.21428/39829d0b.b56ed853  
Publicación principal: [../edades-relativas-universo-observable-y-objetos-fisicos.md](../edades-relativas-universo-observable-y-objetos-fisicos.md)  
Portada de referencia: [../imagenes/portada.png](../imagenes/portada.png)

Ejecutar desde esta carpeta:

```bash
python3 runner.py
```

Salida esperada: `overall_status: APTO`.

Los CSV conservan los registros declarativos. La carpeta [`datos/`](datos/) contiene copias JSON de esos registros y el resultado estructurado de ejecución: [`resultado_laboratorio_edades.json`](datos/resultado_laboratorio_edades.json) y [`resultados_laboratorios.json`](datos/resultados_laboratorios.json). El laboratorio biomolecular conserva sus datos propios en [`biologia_molecular_medicina/datos/`](biologia_molecular_medicina/datos/) y su salida JSON en [`biologia_molecular_medicina/resultados/salida_obtenida.json`](biologia_molecular_medicina/resultados/salida_obtenida.json).

Archivos principales: [`manifest_unidades.csv`](manifest_unidades.csv), [`banco_objetos.csv`](banco_objetos.csv), [`banco_valores.csv`](banco_valores.csv), [`banco_diferencias.csv`](banco_diferencias.csv), [`banco_fracciones.csv`](banco_fracciones.csv), [`banco_negativos.csv`](banco_negativos.csv), [`catalogo_errores.csv`](catalogo_errores.csv), [`runner.py`](runner.py), [`salida_esperada.txt`](salida_esperada.txt), [`salida_obtenida.txt`](salida_obtenida.txt).
