# Laboratorios de Génesis factual del hidrógeno y tabla periódica estructural

Este directorio agrupa los laboratorios reproducibles de la publicación y de su anexo técnico integrado.

- `publicacion/`: laboratorio de la publicación principal, tabla periódica estructural, banco demostrativo y banco negativo.
- `anexo-tecnico/`: laboratorio de las propiedades estructurales SV de los 118 candidatos de la duplicación periódica.

## DOI del laboratorio canónico

- DOI de la versión depositada: `10.5281/zenodo.20058612`.
- DOI del conjunto de versiones: `10.5281/zenodo.20058611`.
- Publicación principal asociada: `10.17613/qq4q9-sd847`.

## Estructura del depósito canónico

El depósito de laboratorio contiene el ZIP de laboratorios, el sello OpenTimestamps, la firma criptográfica, la portada asociada y el PDF descriptivo del laboratorio canónico.

| Fichero | Función | SHA-256 |
|---|---|---|
| `laboratorios.zip` | ZIP canónico de laboratorios reproducibles | `6f34ede5a57714128e67451c9aa031a68c5c6c062de04b14a707035214caf642` |
| `laboratorios.zip.ots` | Sello OpenTimestamps del ZIP de laboratorios | `64474fbd6b7b942ca4a5a4dd92b8fa49c515452bbc6f64f7bd99041a1b7432fe` |
| `laboratorios.zip_signed.csig` | Firma criptográfica del ZIP de laboratorios | `7f179505f5badeed1b0002202c200ae574ff356c02172d0e631016bff7030853` |
| `Portada.png` | Imagen de portada incluida en el depósito | `b0991d712a4dddf5391b0b5e663bb6346153003a929f190ca5949dba8ea7bf75` |
| `Canonical Laboratory for the Publication _Factual Genesis of Hydrogen and Structural Periodic Table in the Vectorial System SV.pdf` | PDF descriptivo del laboratorio canónico | `0d0df6d17d8398a20cce21095f6b2a3f69746114a23ca5e9627228c47e4a8f6a` |
| `Zenodo.zip` | Paquete completo del depósito aportado para verificación | `f14be77e91925841af3e93d3715cb544228d8e0c45048f97e6084d72c8339bd8` |

## Ejecución local

Desde `laboratorios/publicacion/`:

```bash
python runner.py
python runner_bis.py
python runner_publicacion_integral.py
```

Desde `laboratorios/anexo-tecnico/`:

```bash
python runner_prop.py
```

## Nota de custodia

Los SHA-256 identifican los ficheros canónicos depositados o sellados. La actualización de README, DOI o metadatos en GitHub no altera el depósito canónico ya identificado por DOI.

© 2026. Todos los derechos reservados. | Juan Antonio Lloret Egea | ORCID: 0000-0002-6634-3351 | Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA) | IA eñ™ — La Biblia de la IA™ | ISSN 2695-6411 | Licencia CC BY-NC-ND 4.0 | Madrid, 06/05/2026
