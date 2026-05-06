# Laboratorio del anexo técnico integrado

Este laboratorio verifica las propiedades estructurales SV de los 118 candidatos de la duplicación periódica.

## DOI y depósito canónico

- DOI del laboratorio canónico, versión depositada: `10.5281/zenodo.20058612`.
- DOI del conjunto de versiones del laboratorio canónico: `10.5281/zenodo.20058611`.
- DOI de la publicación principal asociada: `10.17613/qq4q9-sd847`.

Este laboratorio forma parte del fichero canónico `laboratorios.zip`.

| Fichero canónico | Función | SHA-256 |
|---|---|---|
| `laboratorios.zip` | ZIP que contiene este laboratorio y el laboratorio de la publicación | `6f34ede5a57714128e67451c9aa031a68c5c6c062de04b14a707035214caf642` |
| `laboratorios.zip.ots` | Sello OpenTimestamps del ZIP de laboratorios | `64474fbd6b7b942ca4a5a4dd92b8fa49c515452bbc6f64f7bd99041a1b7432fe` |
| `laboratorios.zip_signed.csig` | Firma criptográfica del ZIP de laboratorios | `7f179505f5badeed1b0002202c200ae574ff356c02172d0e631016bff7030853` |

## Ejecución

```bash
python runner_prop.py
```

El laboratorio lee los CSV situados en `data/` y valida las fórmulas internas frente a las tablas integradas en el documento principal.

## Salida esperada

```text
tablas_verificadas: 4/4
filas_por_tabla: 118/118
errores_totales: 0
estado: APTO
```

© 2026. Todos los derechos reservados. | Juan Antonio Lloret Egea | ORCID: 0000-0002-6634-3351 | Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA) | IA eñ™ — La Biblia de la IA™ | ISSN 2695-6411 | Licencia CC BY-NC-ND 4.0 | Madrid, 06/05/2026
