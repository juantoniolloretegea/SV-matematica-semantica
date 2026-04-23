# Fuerza, trabajo, calor, entalpía y temperatura en el Sistema Vectorial SV

Adenda del corpus **Sistema Vectorial SV** (ISSN 2695-6411) dedicada al cierre
absoluto del dominio termodinámico factual sobre el fibrado soberano Ω<sub>SV</sub>.
Contiene la fórmula factual única absoluta en sus tres formas equivalentes y únicas
(explícita, implícita y paramétrica), con seis proyecciones canónicas que recuperan
trabajo 𝒲<sub>SV</sub>, calor 𝒬<sub>SV</sub>, no-clausura 𝒰<sub>SV</sub>, fuerza
𝓕<sub>SV</sub>, temperatura Θ<sub>SV</sub> y entalpía Λ<sub>SV</sub>.

## Contenido

| Elemento | Descripción |
|---|---|
| [`formula_factual_unica_absoluta_termodinamica_sv.md`](formula_factual_unica_absoluta_termodinamica_sv.md) | Documento principal: 19 secciones, 15 teoremas, 5 corolarios, 3 proposiciones, 3 lemas, 10 definiciones, 21 pruebas con c.q.d., 55 citas al corpus, apartado §19 de laboratorios y §20 de referencias. |
| [`laboratorios/`](laboratorios/) | 12 laboratorios Python autocontenidos, catálogo de errores con 120 códigos únicos, runner maestro sin pases silenciosos, y 3 casos canónicos en `datos/casos_canonicos.json`. |
| [`imagenes/`](imagenes/) | Figuras asociadas al documento (carpeta reservada para diagramas editoriales). |

## Cómo reproducir las verificaciones

Las verificaciones numéricas del §17 del documento se ejecutan íntegramente
mediante el runner de `laboratorios/`:

```bash
cd laboratorios
python3 runner.py
```

El runner ejecuta los 12 laboratorios en el orden declarado en
[`laboratorios/runner_config.json`](laboratorios/runner_config.json), termina
con exit 0 sólo si los 12 pasan, y **detiene la ejecución al primer fallo**
reportando el código del catálogo
[`laboratorios/catalogo_errores.json`](laboratorios/catalogo_errores.json).

## Tesis del dominio

La fórmula factual única absoluta del dominio se expresa, en su forma implícita,
como la ecuación escalar nula:

```
𝖤^thermo_SV(Γ, n; θ) := 𝔇_Γ Ω_SV(Γ, n; θ) · 𝖦_SV = 0
```

equivalente al balance canónico:

```
𝔇_Γ 𝒜_SV = 𝒲_SV + 𝒬_SV + 𝒰_SV.
```

Sobre toda trayectoria admisible Γ y todo vector paramétrico θ, las tres formas
canónicas (explícita, implícita, paramétrica) producen valores idénticos para las
seis magnitudes derivadas. La verificación numérica cruzada sobre tres casos
canónicos produce **90 de 90 coincidencias** por tres caminos algebraicos
genuinamente distintos.

## Referencias
 
Lloret Egea, Juan Antonio (2026). _Fórmula factual única absoluta del dominio
termodinámico en el Sistema Vectorial SV_. ISSN 2695-6411. DOI por asignar.
