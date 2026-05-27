# Anexo B. Tabla de símbolos y residuales

**Autor:** Juan Antonio Lloret Egea | **ORCID:** 0000-0002-6634-3351 | **Institución:** Instituto Tecnológico Virtual de la Inteligencia Artificial para el Español™ (ITVIA) | **Publicación:** IA eñ™ — La Biblia de la IA™ | **ISSN:** 2695-6411 | **Licencia:** CC BY-NC-ND 4.0 | **Madrid, 2026** | **DOI:** pendiente | **Repositorio canónico:** https://github.com/juantoniolloretegea/SV-matematica-semantica


## B.1. Función del anexo

Este anexo amplía la tabla de símbolos del manuscrito y precisa los residuales que intervienen en la admisión del régimen H–He. Su finalidad es impedir que una fórmula sea leída como cierre automático. El residual no es una incertidumbre estadística: es una condición material no satisfecha o pendiente de retorno en el dominio examinado.

## B.2. Tramo respaldado

Respalda III.5, XIII.5, XIII.7, XIV.10 y XV. La matriz de contraste y el banco BCAM-HHe dependen de esta separación.

## B.3. Tabla material de residuales

| Residual | Entrada | Condición de anulación | Fallo típico | Salida permitida |
|---|---|---|---|---|
| `R_{Ξ→M/E}^{SV}` | Proyección material y energética | Dominio, canal, frontera, traza y retorno conservados | Materia y energía tratadas como entidades autónomas | `ADMISION`, `DEFECTO`, `U` |
| `R_{E⇄M}^{SV}` | Retención/liberación | Retención, liberación, balance, canal, frontera y traza declarados | Usar `E₀=m₀c²` como cierre completo | `ADMISION`, `DEFECTO`, `U` |
| `R_H^{circ}` | Hidrógeno | Dominio, frontera, masa, estado, traza y retorno | Nombrar H sin régimen | `ADMISION`, `DEFECTO`, `U` |
| `R_{HHe}^{SV}` | Régimen H–He | H abierto, He estabilizador, frontera, transición, retorno y continuidad | Absolutizar H–He o reducirlo a abundancia | `ADMISION`, `DEFECTO`, `U` |
| Residual SV-443 | Dominio estructural extendido | Subdominio reconocido separado de regiones de búsqueda | Presentar configuración estructural como empiria cerrada | `ADMISION`, `U` |
| Residual CPS-SV | Pares estructurales | `D(A,B)`, B.1–B.5, compatibilidad y dominio | Convertir par en molécula completa | `APTO-M`, `APTO-C`, `APTO-I`, `NO-APTO`, `U` |
| Residual molecular | Configuración compuesta | Pares, composición, geometría, estabilidad y retorno | Saltar de elemento a molécula | `ADMISION`, `DEFECTO`, `U` |
| Residual biológico | Dominio vivo | Frontera, canal, metabolismo, reparación, retorno y traza | Llamar vida a molécula orgánica aislada | `ADMISION`, `DEFECTO`, `U` |

## B.4. Restricción de lectura

Un residual no puede usarse como refugio retórico. Si puede resolverse mediante dominio, fuente, banco, cálculo o ejecución, debe resolverse. Si no puede resolverse sin invadir el dominio, la salida `U` se conserva como no determinación legítima.

## B.5. Resultado operativo

El residual decide si una afirmación queda admitida, defectiva o no determinada. El laboratorio BCAM-HHe adopta esta tabla como base de sus salidas ejecutables.