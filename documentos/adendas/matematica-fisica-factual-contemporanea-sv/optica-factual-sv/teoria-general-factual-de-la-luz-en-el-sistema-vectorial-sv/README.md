[![Teoría general factual de la luz en el Sistema Vectorial SV](imagenes/portada.png)](https://raw.githubusercontent.com/juantoniolloretegea/SV-matematica-semantica/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/optica-factual-sv/teoria-general-factual-de-la-luz-en-el-sistema-vectorial-sv/imagenes/portada.png)

<p align="center"><em>Pulse sobre la portada para abrirla como imagen en el navegador.</em></p>

---

# Teoría general factual de la luz en el Sistema Vectorial SV

Adenda del corpus **Sistema Vectorial SV** (ISSN 2695-6411) dedicada al cierre
canónico del régimen luminoso factual sobre el fibrado soberano Ω<sub>SV</sub>.
Contiene la ecuación única **L**<sub>SV</sub>(Φ<sup>L</sup><sub>SV</sub>; {𝓛<sub>i</sub><sup>(gr)</sup>}) = 0
sobre el objeto fibroso factual luminoso con quince proyecciones canónicas
declaradas y familia absolutamente abierta por encima de P15 gobernada por el
algoritmo canónico de búsqueda A1–A5.

## Contenido

| Elemento | Descripción |
|---|---|
| [`teoria-general-factual-luz-sv.md`](teoria-general-factual-luz-sv.md) | Documento principal: 24 secciones + anexo operatorio A.1–A.7, 27 teoremas, 14 corolarios, 9 proposiciones, 36 definiciones, 44 observaciones, 56 Q.E.D., 17 bancos B-LUZ visibles, 22 laboratorios L-LUZ declarados, 159 referencias al corpus. |
| [`laboratorios/`](laboratorios/) | 22 laboratorios Python autocontenidos, catálogo de errores con 182 códigos únicos organizados en 43 prefijos LUZ, runner maestro sin pases silenciosos, y 3 casos canónicos en `datos/casos_canonicos.json`. |
| [`imagenes/`](imagenes/) | Figuras asociadas al documento; incluye la portada editorial definitiva [`imagenes/portada.png`](imagenes/portada.png). |
| [`VERIFICACION_LABORATORIOS_2026-04-24.md`](VERIFICACION_LABORATORIOS_2026-04-24.md) | Informe local de verificación de los 22 laboratorios. |

## Depósito reproducible preservado

Los laboratorios de esta carpeta están preservados en Zenodo como suplemento computacional reproducible de la publicación principal.

DOI de versión:
https://doi.org/10.5281/zenodo.19892662

DOI conceptual:
https://doi.org/10.5281/zenodo.19892661

## Cómo reproducir las verificaciones

Las verificaciones numéricas y estructurales declaradas en §18, §19 y §20
del documento se ejecutan íntegramente mediante el runner de `laboratorios/`:

```bash
cd laboratorios
python3 runner.py
```

El runner ejecuta los 22 laboratorios en el orden declarado en
[`laboratorios/runner_config.json`](laboratorios/runner_config.json), termina
con exit 0 sólo si los 22 pasan, y **detiene la ejecución al primer fallo**
reportando el código del catálogo
[`laboratorios/catalogo_errores.json`](laboratorios/catalogo_errores.json).

## Tesis del dominio

El régimen luminoso factual se establece por la ecuación única soberana:

```
L_SV(Φ^L_SV; {𝓛_i^(gr)}) = 0
```

sobre el objeto fibroso factual luminoso Φ<sup>L</sup><sub>SV</sub> ⊂ **D**<sup>L</sup><sub>SV</sub>,
emergente del sustrato preternario Ω<sub>pre</sub> por cadenas de activaciones
honestas Π<sub>3</sub><sup>H</sup>. El operador maestro **L**<sub>SV</sub> se
construye con quince sumandos estructurales, cada uno articulado con un
sector canónico del corpus SV. Cinco teoremas de reducción establecen su
compatibilidad con el bloque Maxwell factual, con la relación de Planck,
con la disolución de la dualidad onda–corpúsculo, con la curvatura
gravitacional de la luz y con el aparato NM–TPA.

La verificación numérica sobre los tres casos canónicos A SV(3,4),
B SV(3,6) y C SV(3,9) produce **L_SV = 0 con tolerancia 1e-9** sobre los
quince sumandos. Los diecisiete bancos B-LUZ embebidos en el texto
proporcionan compatibilidad empírica absoluta: seis calibratorios con
identidad exacta por construcción metrológica y once no calibratorios
dentro del 5% respecto al valor heredado clásico.

## Referencias

Lloret Egea, Juan Antonio (2026). _Teoría general factual de la luz en el Sistema Vectorial SV_. ISSN 2695-6411.

Publicación principal en Commons/KCWorks:
https://works.hcommons.org/records/1z7c0-mqb40

DOI de la publicación principal:
https://doi.org/10.17613/1z7c0-mqb40

Depósito Zenodo de los laboratorios reproducibles:
https://doi.org/10.5281/zenodo.19892662

DOI conceptual de todas las versiones de los laboratorios:
https://doi.org/10.5281/zenodo.19892661

Colección canónica:
https://doi.org/10.17613/r4dwa-d9b30
