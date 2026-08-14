SV-AUTH A.2 — revised reference execution artifact (post cross-audit)
Date: 2026-08-13

Status:
- Reference implementation only.
- Not merged into SV-motor main.
- Not yet J6/E6xx integration in SV-lenguaje-de-computacion.
- Formal working documents are on branch sv-auth-v0.2:
  docs/arquitectura/SV_AUTH_A2_AUDITORIA_SPEC_RUNTIME_2026_08_13.md
  docs/arquitectura/SV_AUTH_A2_CLAUSURA_OPERACIONAL_v0_2_2.md
  docs/arquitectura/SV_AUTH_A2_PRUEBAS_v0_2_2.md

Important refinement after the first 36/36 artifact:
- RawCertificate/VerifiedCertificate boundary and explicit verifier admission.
- Exact human principal/grant/basis/resolver/prior binding.
- Explicit GovernanceAuthorizationAct before GovernanceToken (D.10 preservation).
- Nominal Det/Human/Governance token types and exact stored-capability equality.
- Scope + admitted subject in UseContext.
- Sovereign-U historical lineage required for resolution.
- AEnv computed from valid grants under Constitution + AuthorityState.
- Executable information-enabled authority query.
- Trusted restore admission + semantic environment validation.
- Constitution revision checks.
- Certified nonclosure is required already at human admission for commit_sov_u.
- Implementation caches for admitted acts are checked against historical ledger records.

Exact execution result: see EXECUTION_REPORT.txt.
