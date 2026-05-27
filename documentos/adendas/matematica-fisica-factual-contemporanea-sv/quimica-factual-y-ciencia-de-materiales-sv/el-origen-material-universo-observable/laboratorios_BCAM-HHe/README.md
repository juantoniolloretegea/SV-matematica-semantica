# Laboratorio BCAM-HHe

**Autor:** Juan Antonio Lloret Egea | **ORCID:** 0000-0002-6634-3351 | **Institución:** Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA) | **Publicación:** IA eñ™ — La Biblia de la IA™ | **ISSN:** 2695-6411 | **Licencia:** CC BY-NC-ND 4.0 | **Madrid, 2026** | **DOI:** pendiente | **Repositorio canónico:** https://github.com/juantoniolloretegea/SV-matematica-semantica

## Objeto

El Banco de Contraste de Admisibilidad Material H–He (`BCAM-HHe`) acompaña la publicación como laboratorio reproducible de consistencia formal. Su función es ejecutar una matriz finita de casos y comprobar que las salidas del banco distinguen admisión, defecto, no determinación legítima y salidas específicas del Catálogo de Pares Estructurales SV.

## Estructura

```text
laboratorios_BCAM-HHe/
├── README.md
├── datos/
│   └── bcam_hhe_casos.csv
├── scripts/
│   └── runner_bcam_hhe.py
└── salidas/
    └── bcam_hhe_salidas_obtenidas.csv
```

## Ejecución

Desde la raíz del repositorio:

```bash
python laboratorios_BCAM-HHe/scripts/runner_bcam_hhe.py \
  --cases laboratorios_BCAM-HHe/datos/bcam_hhe_casos.csv \
  --out bcam_hhe_salidas_verificacion.csv
```

La comprobación material consiste en comparar `bcam_hhe_salidas_verificacion.csv` con `laboratorios_BCAM-HHe/salidas/bcam_hhe_salidas_obtenidas.csv`.

## Resultado de referencia

| Magnitud | Resultado |
|---|---:|
| Casos del banco | 25 |
| Coincidencias esperadas/obtenidas | 25 |
| Divergencias | 0 |
| Veredicto | APTO |

## Alcance

El laboratorio no sustituye el razonamiento físico del cuerpo principal. Su alcance es reproducible y delimitado: verifica que la matriz BCAM-HHe opera con salidas explícitas y coherentes respecto de las condiciones declaradas en la publicación.
