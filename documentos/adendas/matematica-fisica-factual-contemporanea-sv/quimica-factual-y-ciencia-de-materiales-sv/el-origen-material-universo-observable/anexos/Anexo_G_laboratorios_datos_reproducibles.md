# Anexo G. Laboratorio BCAM-HHe y datos reproducibles

**Autor:** Juan Antonio Lloret Egea | **ORCID:** 0000-0002-6634-3351 | **Institución:** Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA) | **Publicación:** IA eñ™ — La Biblia de la IA™ | **ISSN:** 2695-6411 | **Licencia:** CC BY-NC-ND 4.0 | **Madrid, 2026** | **DOI:** pendiente | **Repositorio canónico:** https://github.com/juantoniolloretegea/SV-matematica-semantica

## G.1. Objeto

Este anexo documenta el laboratorio reproducible del Banco de Contraste de Admisibilidad Material H–He (`BCAM-HHe`). Su función es mostrar que la matriz de admisibilidad no queda sólo formulada en el cuerpo principal: se expresa en datos, runner determinista y salida de referencia.

## G.2. Archivos del laboratorio

| Archivo | Función |
|---|---|
| `laboratorios_BCAM-HHe/README.md` | Descripción del laboratorio y modo de ejecución |
| `laboratorios_BCAM-HHe/datos/bcam_hhe_casos.csv` | Banco de 25 casos con dominio, condición, regla, residual, salida esperada y motivo |
| `laboratorios_BCAM-HHe/scripts/runner_bcam_hhe.py` | Runner determinista del banco |
| `laboratorios_BCAM-HHe/salidas/bcam_hhe_salidas_obtenidas.csv` | Salida de referencia incluida |

## G.3. Resultado de referencia

| Magnitud | Resultado |
|---|---:|
| Casos del banco | 25 |
| Filas completas | 25 |
| Filas incompletas | 0 |
| Salidas esperadas fuera de catálogo | 0 |
| Salidas obtenidas fuera de catálogo | 0 |
| Coincidencias esperadas/obtenidas | 25 |
| Divergencias | 0 |
| Veredicto global | APTO |

## G.4. Reejecución

Desde la raíz del repositorio, el laboratorio puede verificarse sin modificar la salida de referencia mediante una salida local de comprobación:

```bash
python laboratorios_BCAM-HHe/scripts/runner_bcam_hhe.py \
  --cases laboratorios_BCAM-HHe/datos/bcam_hhe_casos.csv \
  --out bcam_hhe_salidas_verificacion.csv
```

La comparación reproducible debe hacerse entre `bcam_hhe_salidas_verificacion.csv` y `laboratorios_BCAM-HHe/salidas/bcam_hhe_salidas_obtenidas.csv`.

## G.5. Alcance

El laboratorio no funda la tesis física, no sustituye el análisis doctrinal del cuerpo principal y no convierte la matriz en verdad automática. Su función es acotada: verificar que las reglas declaradas producen salidas explícitas y reproducibles para los casos incluidos en el banco.
