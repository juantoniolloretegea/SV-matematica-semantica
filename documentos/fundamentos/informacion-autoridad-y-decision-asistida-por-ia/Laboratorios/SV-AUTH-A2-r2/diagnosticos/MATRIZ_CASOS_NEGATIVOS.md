# Matriz diagnóstica suplementaria — SV-AUTH A.2 r2

Esta matriz **no sustituye** a las 78 pruebas congeladas de `tests/test_authority.py`.
Añade una obligación más estricta: cada caso negativo representativo debe ser rechazado
por la **clase diagnóstica esperada**, no simplemente por cualquier `AuthError`.

| Código | Caso negativo representativo | Resultado exigido |
|---|---|---|
| E601 | `INFO` intenta introducir un `Grant` | rechazo `E601 IllegalAuthorityCoercion` |
| E602 | token de `bind_principal` presentado a `GOV_GRANT` | rechazo `E602 UnauthorizedGrantMutation` |
| E603 | `mint_det` intenta usar grant humano | rechazo `E603 TokenAuthorityEscalation` |
| E604 | `mint_det` usa un ámbito fuera del grant | rechazo `E604 TokenBindingMismatch` |
| E605 | token acuñado bajo otra versión constitucional | rechazo `E605 StaleAuthorityEnvironment` |
| E606 | segundo token con el mismo `token_id` | rechazo `E606 TokenReplay` |
| E607 | verificación no admitida por Γ_V | rechazo `E607 UnverifiedCommitBasis` |
| E608 | acto humano no admitido por Γ_H | rechazo `E608 HumanReviewLaundering` |
| E609 | `DetToken` presentado a `COMMIT_SOV_U` | rechazo `E609 UnauthorizedSovereignU` |
| E610 | resolución soberana sobre antecedente que no es U | rechazo `E610 UnauthorizedSovereignUResolution` |
| E611 | segundo ingreso del mismo acto humano | rechazo `E611 AuthorizationRecordReplay` |
| E612 | deserialización usada como constructor de token | rechazo `E612 TokenDeserializationForgery` |
| E613 | deserialización usada como constructor de decisión soberana | rechazo `E613 SovereignImportBypass` |
| E615 | gobernanza intenta ligar `External` como `HUMAN_SOVEREIGN` | rechazo `E615 InvariantDerogationAttempt` |
| E617 | restauración con referencia semántica inexistente | rechazo `E617 HistoricalSemanticDrift` |

`E614` y `E616` quedan documentados como **reservados y no emitidos** por el runtime r2.

## Qué evita esta capa

La batería congelada usa en muchos casos `pytest.raises(AuthError)`. Eso prueba que la
operación prohibida **no pasa silenciosamente**, pero por sí solo no obliga a que el motivo
del rechazo sea el correcto. `test_contrato_diagnostico.py` añade esa comprobación sin
modificar el artefacto citado en el artículo.
