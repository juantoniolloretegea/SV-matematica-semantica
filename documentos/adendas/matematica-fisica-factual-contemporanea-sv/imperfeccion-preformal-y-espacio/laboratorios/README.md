# Laboratorios reproducibles — Imperfección preformal y espacio

<p align="center">
  <img src="../imagenes/portada.svg" alt="Portada de la publicación Imperfección preformal y espacio" width="100%">
</p>

**© 2026. Todos los derechos reservados.** | **Juan Antonio Lloret Egea** | ORCID: [0000-0002-6634-3351](https://orcid.org/0000-0002-6634-3351) | Licencia CC BY-NC-ND 4.0 | Madrid, 11/05/2026

## Objeto

Estos laboratorios reproducibles verifican la disciplina transductiva de la publicación [`imperfeccion-preformal-y-espacio.md`](../imperfeccion-preformal-y-espacio.md). No fundan la doctrina ni sustituyen los teoremas; controlan que los bancos de contraste no acepten cierres silenciosos, confusiones de dominio ni dictámenes sin residual ni retorno físico.

## Ejecución

Desde la carpeta `laboratorios/`:

```bash
python runner/run_all.py
```

El ejecutor escribe la salida material en [`registros/resultado_runner.json`](registros/resultado_runner.json). Si cualquier caso falla, el proceso termina con código distinto de cero.

## Archivos principales

| Elemento | Enlace | Función |
|---|---|---|
| Catálogo de errores | [`catalogo_errores.csv`](catalogo_errores.csv) | Códigos de rechazo, contaminación, separación y pase silencioso. |
| Datos de teorías externas | [`datos/teorias_externas.csv`](datos/teorias_externas.csv) | Matriz de teorías, dominios, proyecciones y clasificación. |
| Dominios internos | [`datos/dominios_internos.csv`](datos/dominios_internos.csv) | Dominios SV usados por las proyecciones. |
| Magnitudes y unidades SV | [`datos/magnitudes_unidades_sv.csv`](datos/magnitudes_unidades_sv.csv) | Puente metrológico entre magnitudes físicas y primitivos SV. |
| Casos de origen cosmológico | [`datos/casos_origen_cosmologico.csv`](datos/casos_origen_cosmologico.csv) | ε₋₀ ante Big Bang, vacío cuántico, no-boundary, tunneling e inflación. |
| Casos de espacio | [`datos/casos_espacio.csv`](datos/casos_espacio.csv) | Espacio completo, trayectoria, métrica, volumen y distancia factual fibrosa. |
| Casos de transparencia | [`datos/casos_transparencia.csv`](datos/casos_transparencia.csv) | No visibilidad, transparencia, opacidad y no transmisibilidad. |
| Casos de materia oscura | [`datos/casos_materia_oscura.csv`](datos/casos_materia_oscura.csv) | Presencia gravitatoria no luminosa y candidatos microfísicos. |
| Casos de energía oscura | [`datos/casos_energia_oscura.csv`](datos/casos_energia_oscura.csv) | Régimen expansivo, Λ, w, quintessence y errores de dominio. |
| Separación DM / DE / BH | [`datos/casos_dm_de_bh.csv`](datos/casos_dm_de_bh.csv) | Separación entre materia oscura, energía oscura y agujero negro. |
| Casos de agujero negro | [`datos/casos_agujero_negro.csv`](datos/casos_agujero_negro.csv) | Horizonte, temperatura, entropía, volumen y NADA. |
| Falsos fundamentos | [`datos/casos_falsos_fundamentos.csv`](datos/casos_falsos_fundamentos.csv) | Probabilidad, geometría, multiverso, falta de unidad SV y falta de retorno. |
| Validador común | [`validadores/sv_validadores.py`](validadores/sv_validadores.py) | Deriva dictámenes, bloquea equivalencias prohibidas y exige autoría. |
| Runner maestro | [`runner/run_all.py`](runner/run_all.py) | Ejecuta todos los validadores y produce salida JSON. |

## Regla de rechazo de pases silenciosos

El runner exige, como mínimo, casos admisibles, admisibles parciales, no admisibles y U. También exige códigos de error en todo caso no admisible, unidades SV declaradas, retorno físico controlado y metadatos de autoría en cada fila de los CSV. Si alguna condición falta, no hay salida favorable.
