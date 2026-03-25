# Laboratorio Python VII.5

Este laboratorio acompaña el documento VII.5 y cumple una función subordinada de verificación e ilustración.

## Qué hace

- declara una célula canónica `SV(9,3)`;
- modela el dato de enlace `Lambda = (J, Theta, Pi)` de forma deliberadamente sobria;
- clasifica cinco tipos mínimos de enlace:
  - separación completa,
  - enlace débil,
  - reinicialización pura,
  - reinicialización con memoria,
  - enlace fuerte;
- reproduce el ejemplo canónico del manuscrito;
- e incorpora comprobaciones con `assert` para que el laboratorio no sólo imprima, sino que también verifique.

## Nota de prudencia operativa

- El umbral de `herencia_significativa` del laboratorio es **heurístico y auxiliar**. No deriva todavía de una ley doctrinal cerrada y sólo se utiliza para evitar sobreclasificaciones en la capa de código.
- Del mismo modo, una proyección auxiliar no nula sin transporte declarado se rebaja en el laboratorio al borde más pobre del **enlace débil**. Esta convención es operativa, no soberana.

## Qué no hace

- no implementa una teoría general del cambio de régimen;
- no constituye backend del Lenguaje SV;
- no sustituye al manuscrito doctrinal.
