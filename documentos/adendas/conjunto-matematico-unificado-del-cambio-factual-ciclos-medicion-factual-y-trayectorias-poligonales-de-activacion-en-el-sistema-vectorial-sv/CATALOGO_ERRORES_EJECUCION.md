# Autoría: Juan Antonio Lloret Egea | ORCID: 0000-0002-6634-3351 | Institución: Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA) | Publicación: IA eñ™ — La Biblia de la IA™ | ISSN: 2695-6411 | Licencia: CC BY-NC-ND 4.0 | Lugar y fecha: Madrid, 2026

# Catálogo de errores de ejecución — Hito 3

## Ruta canónica del conjunto

Ruta relativa prevista en el repositorio:

`documentos/adendas/conjunto-matematico-unificado-del-cambio-factual-ciclos-medicion-factual-y-trayectorias-poligonales-de-activacion-en-el-sistema-vectorial-sv`

URL canónica de GitHub:

`https://github.com/juantoniolloretegea/SV-matematica-semantica/tree/main/documentos/adendas/conjunto-matematico-unificado-del-cambio-factual-ciclos-medicion-factual-y-trayectorias-poligonales-de-activacion-en-el-sistema-vectorial-sv`

## Estatuto

Este catálogo documenta los códigos de error previstos por los runners del Hito 3 y el comportamiento esperado de la suite cuando ocurre un fallo material. Su función no es ornamental: fija el régimen de corte, evita cierres favorables y deja trazable qué debe ocurrir cuando pasa algo que no debía pasar.

## Tabla de códigos

| Código | Nombre canónico | Disparo | Efecto del runner | Acción correctiva esperable |
|---|---|---|---|---|
| 0 | Ejecución íntegra sin incidencias | Registro válido, autoría completa, imports correctos, resultados válidos y estados esperados | El runner completa la ejecución y, en el caso del maestro, escribe el informe JSON | Ninguna |
| 10 | Identificadores de afirmación duplicados | Dos entradas del registro comparten el mismo `id` | Corte inmediato antes de ejecutar laboratorios | Corregir unicidad del identificador en `core/assertion_registry.py` |
| 11 | Laboratorios duplicados en el registro | Dos entradas del registro apuntan al mismo laboratorio | Corte inmediato antes de ejecutar laboratorios | Eliminar duplicidad o separar afirmaciones de forma legítima |
| 12 | Laboratorio faltante | El registro declara un laboratorio cuyo archivo no existe | Corte inmediato antes de ejecutar laboratorios | Crear el archivo faltante o corregir el nombre en el registro |
| 13 | Laboratorio físico no registrado | Existe un `lab_*.py` en `laboratorios/` que no figura en el registro | Corte inmediato antes de ejecutar laboratorios | Registrar el laboratorio o retirarlo del conjunto |
| 20 | Autoría ausente | Falta la línea corrida obligatoria de autoría en uno o más `.py` | Corte inmediato antes de ejecutar laboratorios | Añadir la línea completa de autoría en cada archivo Python afectado |
| 30 | Fallo de importación | Un módulo de laboratorio no puede importarse | Corte inmediato en el laboratorio afectado | Revisar dependencias internas, imports relativos y errores sintácticos |
| 31 | Excepción no controlada | Un laboratorio lanza excepción durante `run()` | Corte inmediato en el laboratorio afectado | Corregir la excepción, estabilizar entrada y endurecer validaciones internas |
| 32 | Resultado inválido o incompleto | El laboratorio devuelve un objeto sin las claves obligatorias o con estructura no normalizable | Corte inmediato en el laboratorio afectado | Hacer que `run()` devuelva un `LabResult` o `dict` completo y válido |
| 33 | Estado no esperado | El laboratorio devuelve un estado distinto del fijado en el registro | Corte inmediato en el laboratorio afectado | Corregir el laboratorio o el registro; nunca maquillar la discrepancia |
| 34 | `passed=False` o booleano inválido | El laboratorio devuelve `passed=False` o un valor no booleano | Corte inmediato en el laboratorio afectado | Corregir el laboratorio y revisar su criterio de cierre |
| 35 | Fallo de escritura del informe | El runner maestro no puede escribir `reporte_laboratorios_hito3.json` | Corte al final de la ejecución | Corregir permisos, ruta de salida o estado del sistema de archivos |

## Comportamiento de custodia

1. Los runners trabajan en régimen **fail-fast**.
2. No se toleran laboratorios huérfanos, silenciosos o físicamente presentes pero no registrados.
3. La ausencia de autoría es motivo de corte, no de aviso blando.
4. Un laboratorio que devuelve un estado distinto del esperado no queda “marcado”: la suite corta y lo declara.
5. El informe JSON del runner maestro sólo tiene valor de cierre si el código de salida es `0`.

## Rutas negativas verificadas materialmente en la auditoría

Durante la auditoría dura del lote se verificaron, sobre copias mutadas, al menos las siguientes rutas negativas:

- **Código 20**: retirada deliberada de la línea de autoría en un laboratorio.
- **Código 13**: inserción de un laboratorio intruso `lab_99_intruso.py` no registrado.
- **Código 33**: alteración del estado esperado en el registro para forzar una discrepancia con el resultado real del laboratorio.

Estas verificaciones no forman parte del runner ordinario, pero sí del cierre de custodia de la suite.

## Relación con el siguiente paso

Una vez fijados los laboratorios bajo esta ruta canónica, el paso siguiente consiste en volver al documento `.md` principal y referenciar, con URLs vivas y precisas, los laboratorios, pseudocódigos y runners contenidos en esta carpeta. Las figuras quedan fuera del presente catálogo y de esta fase de cierre.
