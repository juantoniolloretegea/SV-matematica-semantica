# Laboratorio Python — VII.3

## Finalidad

Este laboratorio acompaña al documento **VII.3 — Cadenas, acumulación y regímenes de paso entre sucesos admisibles en el Sistema Vectorial SV**.

Su función es ilustrar y verificar, en régimen mínimo reproducible, los ejemplos formales principales del manuscrito:

- cadena legítima finita en `SV(9,3)`;
- pseudoacumulación ilegítima;
- paso de régimen estable a singular;
- respuesta estructural a suceso de horizonte.

## Archivo

- `laboratorio_vii3.py`

## Ejecución mínima

```bash
python3 laboratorio_vii3.py
```

## Alcance y límite

El laboratorio:

- usa solo biblioteca estándar de Python;
- verifica condiciones locales de cadena `(C1–C4)`;
- calcula acumulación eventiva con regla tipada de actualización;
- y delimita regímenes de paso en forma reproducible.

No sustituye al manuscrito, no fija doctrina soberana y no constituye todavía integración con backend, runner, IR ni Lenguaje SV.
