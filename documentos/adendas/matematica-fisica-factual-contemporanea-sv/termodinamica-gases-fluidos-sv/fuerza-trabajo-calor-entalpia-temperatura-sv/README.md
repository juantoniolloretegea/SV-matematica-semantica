# Fuerza, trabajo, calor, entalpía y temperatura en el Sistema Vectorial SV

© 2026. Todos los derechos reservados.  
Juan Antonio Lloret Egea | ORCID: 0000-0002-6634-3351 | Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español (ITVIA) | IA eñ™ — La Biblia de la IA™ | ISSN 2695-6411 | Licencia CC BY-NC-ND 4.0 | Madrid, 30/04/2026

## Descripción

Adenda del corpus Sistema Vectorial SV dedicada al cierre del dominio termodinámico factual sobre el fibrado soberano ΩSV. Contiene la fórmula factual única absoluta en sus tres formas equivalentes y únicas —explícita, implícita y paramétrica—, con seis proyecciones canónicas que recuperan trabajo WSV, calor QSV, no-clausura USV, fuerza FSV, temperatura ΘSV y entalpía ΛSV.

El conjunto articula la relación estructural entre fuerza, trabajo, calor, entalpía, temperatura, principios y fundamentos de la termodinámica dentro del Sistema Vectorial SV, con verificación reproducible mediante laboratorios Python autocontenidos.

## Contenido

| Elemento | Descripción |
|---|---|
| `formula_factual_unica_absoluta_termodinamica_sv.md` | Documento principal: fórmula factual única absoluta del dominio termodinámico en el Sistema Vectorial SV. |
| `laboratorios/` | 12 laboratorios Python autocontenidos, catálogo de errores con 120 códigos únicos, runner maestro sin pases silenciosos y 3 casos canónicos en `datos/casos_canonicos.json`. |
| `imagenes/` | Figuras asociadas al documento y material gráfico editorial del conjunto. |

## Cómo reproducir las verificaciones

Las verificaciones numéricas del documento se ejecutan íntegramente desde la carpeta `laboratorios/`:

```bash
cd laboratorios
python runner.py
```

o, alternativamente:

```bash
cd laboratorios
python run_all.py
```

El runner ejecuta los 12 laboratorios en el orden declarado, termina con `exit 0` sólo si todos los laboratorios pasan, y detiene la ejecución al primer fallo reportando el código correspondiente del catálogo `laboratorios/catalogo_errores.json`.

## Tesis del dominio

La fórmula factual única absoluta del dominio termodinámico se expresa, en su forma implícita, como la ecuación escalar nula:

```text
𝖤^thermo_SV(Γ, n; θ) := 𝔇_Γ Ω_SV(Γ, n; θ) · 𝖦_SV = 0
```

equivalente al balance canónico:

```text
𝔇_Γ 𝒜_SV = 𝒲_SV + 𝒬_SV + 𝒰_SV.
```

Sobre toda trayectoria admisible Γ y todo vector paramétrico θ, las tres formas canónicas —explícita, implícita y paramétrica— producen valores equivalentes para las seis magnitudes derivadas. La verificación numérica cruzada sobre tres casos canónicos produce coincidencias por tres caminos algebraicos independientes.

## Laboratorios reproducibles preservados

Los laboratorios canónicos asociados a esta publicación se encuentran en la carpeta:

```text
laboratorios/
```

Depósito Zenodo de los laboratorios reproducibles:

```text
https://doi.org/10.5281/zenodo.19900023
```

DOI conceptual de todas las versiones de los laboratorios:

```text
https://doi.org/10.5281/zenodo.19900022
```

Registro Zenodo:

```text
https://zenodo.org/records/19900023
```

## Publicación principal y colección

Publicación principal en Commons/KCWorks:

```text
https://works.hcommons.org/records/ptw68-d1r57
```

DOI Commons/KCWorks de la publicación principal:

```text
https://doi.org/10.17613/ptw68-d1r57
```

Colección canónica:

```text
https://doi.org/10.17613/r4dwa-d9b30
```

Fuente material canónica en GitHub:

```text
https://github.com/juantoniolloretegea/SV-matematica-semantica/tree/main/documentos/adendas/matematica-fisica-factual-contemporanea-sv/termodinamica-gases-fluidos-sv/fuerza-trabajo-calor-entalpia-temperatura-sv
```

## Referencia

Lloret Egea, Juan Antonio (2026). *Force, Work, Heat, Enthalpy, Temperature, Principles and Foundations of Thermodynamics, and the Correlation Among Them in the SV*. IA eñ™ — La Biblia de la IA™, ISSN 2695-6411. https://doi.org/10.17613/ptw68-d1r57
