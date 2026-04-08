# Conjunto matemático unificado del cambio factual, ciclos, medición factual y trayectorias poligonales de activación en el Sistema Vectorial SV

Este directorio queda preparado para **subida de un golpe mediante GitHub Desktop** y para contrastar, desde la publicación de PubPub, que las URLs absolutas que apuntan a laboratorios, runners, pseudocódigo y catálogo de errores resuelven correctamente una vez el contenido esté en GitHub.

## Ruta canónica

- Ruta relativa: `documentos/adendas/conjunto-matematico-unificado-del-cambio-factual-ciclos-medicion-factual-y-trayectorias-poligonales-de-activacion-en-el-sistema-vectorial-sv`
- URL canónica GitHub: <https://github.com/juantoniolloretegea/SV-matematica-semantica/tree/main/documentos/adendas/conjunto-matematico-unificado-del-cambio-factual-ciclos-medicion-factual-y-trayectorias-poligonales-de-activacion-en-el-sistema-vectorial-sv>
- URL canónica PubPub: <https://www.itvia.online/pub/conjunto-matematico-unificado-del-cambio-factual-ciclos-medicion-factual-y-trayectorias-poligonales-de-activacion-en-el-sistema-vectorial-sv>
- Colección PubPub: **Nueva Matemática y Física Factual del SV**

## Documento rector

- `conjunto_matematico_unificado_pubpub_definitivo.html`: **fuente editorial de verdad** exportada desde PubPub.
- `conjunto_matematico_unificado.md`: espejo GitHub ajustado sobre el HTML definitivo.
- `conjunto_matematico_unificado_pubpub.md`: alias en Markdown conservado por conveniencia operativa.

## Infraestructura incluida

- `figuras/`: portada y figuras 1–7.
- `laboratorios/`: 17 laboratorios auditables.
- `pseudocodigo/`: 5 piezas de pseudocódigo.
- `runners/`: runner maestro y runner rápido.
- `core/`: soporte común.
- `CATALOGO_ERRORES_EJECUCION.md`: catálogo operativo de errores.
- `reporte_laboratorios_hito3.json`: último informe de ejecución.
- `MANIFIESTO_PAQUETE.md`: inventario y estatuto del paquete.
- `AUDITORIA_PAQUETE_FINAL.json`: verificación final del lote.

## Ejecución local

Desde esta carpeta raíz:

```bash
python runners/runner_maestro.py
python runners/runner_rapido.py
```

## Criterio de cierre

La suite distingue entre resultados `CONFIRMA`, `REFUTA` y `ABIERTO`. No clausura como demostradas las zonas que el propio documento mantiene abiertas.
