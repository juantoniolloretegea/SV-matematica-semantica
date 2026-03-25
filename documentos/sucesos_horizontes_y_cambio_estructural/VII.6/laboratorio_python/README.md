# Laboratorio acompañante

Este laboratorio acompaña el manuscrito sobre equivalencia parcial, preservación e invariancia local entre regímenes en el Sistema Vectorial SV.

## Qué hace

- Declara la célula canónica `SV(9,3)` y el alfabeto `{0,1,U}`.
- Implementa propiedades relevantes como observables locales tipados sobre subdominios declarados.
- Verifica preservación bajo transporte comparando valores de propiedades, no coincidencias narrativas.
- Implementa invariancia local sin umbrales heurísticos: exige preservación íntegra de la familia declarada.
- Reproduce cinco ejemplos canónicos del manuscrito y cinco casos de borde con aserciones verificables.

## Qué no hace

- No legisla sobre la doctrina.
- No sustituye al manuscrito.
- No constituye backend del Lenguaje SV.
- No convierte el dato de enlace en criterio automático de comparabilidad o equivalencia parcial.

## Ejecución

```bash
python3 laboratorio_equivalencia_regimenes_sv.py
```

Salida esperada:

```text
Laboratorio: verificación canónica completada correctamente.
─── Informe de clasificación del laboratorio ───
...
```
