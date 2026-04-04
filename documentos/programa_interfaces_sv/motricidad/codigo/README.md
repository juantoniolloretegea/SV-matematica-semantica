# Código del carril de motricidad del Sistema Vectorial SV

**Fecha y Versión: V.1 del conjunto**  
**Fecha:** 4 de abril de 2026  
**Versión del conjunto:** V.1 del conjunto  
**Autor del corpus:** Juan Antonio Lloret Egea  
**ORCID:** 0000-0002-6634-3351  
**Institución:** ITVIA — IA eñ™  
**ISSN:** 2695-6411  
**Licencia:** CC BY-NC-ND 4.0  
**Titularidad y autoría:** © Juan Antonio Lloret Egea, 2026. Este conjunto se distribuye con atribución explícita de autoría y bajo la licencia indicada, sin autorización para apropiación de la paternidad intelectual del Sistema Vectorial SV.  

---


Este directorio contiene el evaluador mínimo y el dataset de casos del carril de motricidad.

## Contenido

- `evaluador.py`  
  Implementación en Python del predicado de habilitación estructural `H` sobre grafos finitos dirigidos.

- `datos.json`  
  Dataset de casos formales, incluyendo los cuatro ejemplos del artículo.

## Uso

Desde este directorio:

```bash
python3 evaluador.py
```

No requiere dependencias externas.

## Resultado esperado

La salida del evaluador debe ser:

```text
T1 no_habilitable
T2 no_habilitable
T3 no_habilitable
T4 habilitable
```

## Criterio

Este bloque acompaña al paper y verifica parcialmente sus ejemplos formales. No constituye una teoría de acción ni un modelo de ejecución física.
