from __future__ import annotations

from dataclasses import replace
from typing import FrozenSet, Optional, Tuple, Type, TypeVar

from .authority_types import *

AUTH_SEM_ENV = "sem:auth-v0.2.1"
TToken = TypeVar("TToken", bound=TokenBase)


def _append_history(k: Configuration, record: Record) -> Configuration:
    k.semantic_env(record.semantic_env_ref)
    return replace(k, history=k.history + (record,))


def _payload(**kwargs: object) -> Tuple[Tuple[str, str], ...]:
    return tuple((str(k), "" if v is None else str(v)) for k, v in kwargs.items())


def _verified_certificates(k: Configuration) -> Tuple[VerifiedCertificate, ...]:
    return tuple(x for x in k.information if isinstance(x, VerifiedCertificate))


def _is_verified(k: Configuration, cert: VerifiedCertificate) -> bool:
    return cert in _verified_certificates(k)


def _certificate_by_id(k: Configuration, certificate_id: Optional[str]) -> Optional[VerifiedCertificate]:
    if certificate_id is None:
        return None
    matches = [c for c in _verified_certificates(k) if c.certificate_id == certificate_id]
    if len(matches) != 1:
        return None
    return matches[0]


def wf_auth(k: Configuration) -> bool:
    grant_ids = [g.grant_id for g in k.authority.grants]
    binding_principals = [b.principal for b in k.authority.bindings]
    token_ids = [t.token_id for t in k.tokens]
    act_ids = [a.act_id for a in k.human_acts]
    gov_act_ids = [a.act_id for a in k.governance_acts]
    env_ids = [e.env_id for e in k.semantic_registry]
    if len(grant_ids) != len(set(grant_ids)):
        return False
    if len(binding_principals) != len(set(binding_principals)):
        return False
    if len(token_ids) != len(set(token_ids)):
        return False
    if len(act_ids) != len(set(act_ids)):
        return False
    if len(gov_act_ids) != len(set(gov_act_ids)):
        return False
    if len(env_ids) != len(set(env_ids)):
        return False
    if any(not b.well_formed() for b in k.authority.bindings):
        return False
    if any(not grant_well_formed(k.constitution, k.authority, g) for g in k.authority.grants):
        return False
    if any(r.semantic_env_ref not in set(env_ids) for r in k.history):
        return False
    human_record_ids = {r.record_id.removeprefix("human-act:") for r in k.history if r.kind == "HumanAuthorizationAct" and r.record_id.startswith("human-act:")}
    gov_record_ids = {r.record_id.removeprefix("gov-act:") for r in k.history if r.kind == "GovernanceAuthorizationAct" and r.record_id.startswith("gov-act:")}
    if human_record_ids != set(act_ids) or gov_record_ids != set(gov_act_ids):
        return False
    if not set(k.used_human_acts).issubset(set(act_ids)):
        return False
    if not set(k.used_governance_acts).issubset(set(gov_act_ids)):
        return False
    return True


def info_add(k: Configuration, item: object) -> Configuration:
    # IU4 + certified-basis barrier: ordinary information cannot inject authority
    # objects nor forge a VerifiedCertificate.
    forbidden = (
        Grant, PrincipalBinding, AuthorityState, Constitution, TokenBase,
        SovereignDecision, HumanAuthorizationAct, GovernanceAuthorizationAct, VerifiedCertificate,
    )
    if isinstance(item, forbidden):
        raise AuthError("E601 IllegalAuthorityCoercion")
    return replace(k, information=k.information + (item,))


def verify_certificate(
    k: Configuration, raw: RawCertificate, *, verifier_id: str, verifier_admitted: bool
) -> Tuple[Configuration, VerifiedCertificate]:
    if not verifier_admitted:
        raise AuthError("E607 UnverifiedCommitBasis: verifier boundary did not admit result")
    verifier = k.constitution.verifier(verifier_id)
    if raw.resolver != verifier.resolver:
        raise AuthError("E607 UnverifiedCommitBasis: verifier/resolver mismatch")
    if raw.certifies_nonclosure and raw.candidate != "U":
        raise AuthError("E607 UnverifiedCommitBasis: nonclosure certificate must target U")
    if raw.certifies_nonclosure and not verifier.can_certify_nonclosure:
        raise AuthError("E607 UnverifiedCommitBasis: verifier cannot certify nonclosure")
    if any(c.certificate_id == raw.certificate_id for c in _verified_certificates(k)):
        raise AuthError("E607 UnverifiedCommitBasis: duplicate certificate id")
    cert = VerifiedCertificate(
        certificate_id=raw.certificate_id,
        candidate=raw.candidate,
        state_ref=raw.state_ref,
        resolver=raw.resolver,
        verifier_id=verifier_id,
        certifies_nonclosure=raw.certifies_nonclosure,
    )
    return replace(k, information=k.information + (cert,)), cert


def request_human(
    k: Configuration, *, request_id: str, object_id: str, state_ref: str
) -> Tuple[Configuration, HumanReviewRequest]:
    req = HumanReviewRequest(request_id, object_id, state_ref)
    return info_add(k, req), req


def _valid_grant(k: Configuration, grant_id: str) -> Grant:
    grant = k.authority.grant(grant_id)
    if grant not in k.aenv():
        raise AuthError("E603 TokenAuthorityEscalation: grant outside AEnv")
    return grant


def _basis_matches(
    k: Configuration,
    cert: Optional[VerifiedCertificate],
    *,
    candidate: Optional[str],
    state_ref: str,
    resolver: Optional[str],
) -> bool:
    if cert is None:
        return False
    return (
        _is_verified(k, cert)
        and cert.candidate == candidate
        and cert.state_ref == state_ref
        and cert.resolver == resolver
    )


def admit_human_act(
    k: Configuration, act: HumanAuthorizationAct, *, boundary_admitted: bool
) -> Configuration:
    if not boundary_admitted:
        raise AuthError("E608 HumanReviewLaundering: human act not admitted by boundary")
    if (act.constitution_version, act.authority_epoch) != (
        k.constitution.version, k.authority.epoch
    ):
        raise AuthError("E605 StaleAuthorityEnvironment")
    if act.act_id in k.used_human_acts or any(a.act_id == act.act_id for a in k.human_acts):
        raise AuthError("E611 AuthorizationRecordReplay")
    grant = _valid_grant(k, act.grant_id)
    if grant.kind != AuthorityKind.HUMAN or grant.principal != act.principal:
        raise AuthError("E608 HumanReviewLaundering: principal/grant mismatch")
    binding = k.authority.binding(act.principal)
    if binding is None or binding.role != AuthorityRole.HUMAN_SOVEREIGN or not binding.well_formed():
        raise AuthError("E608 HumanReviewLaundering: principal is not a human sovereign")
    cert = _certificate_by_id(k, act.certificate_id)
    has_basis = cert is not None and _basis_matches(
        k, cert, candidate=act.candidate, state_ref=act.state_ref, resolver=act.resolver
    )
    if not grant.authorizes(
        operation=act.operation,
        scope=act.scope,
        object_id=act.object_id,
        candidate=act.candidate,
        resolver=act.resolver,
        has_verified_basis=has_basis,
    ):
        raise AuthError("E604 TokenBindingMismatch: human act outside grant")
    if grant.requires_verified_certificate and not has_basis:
        raise AuthError("E607 UnverifiedCommitBasis")
    if act.operation == "commit_sov_u" and (cert is None or not cert.certifies_nonclosure):
        raise AuthError("E607 UnverifiedCommitBasis: sovereign U requires certified nonclosure")
    if act.operation == "resolve_sov_u" and not act.prior_decision_ref:
        raise AuthError("E610 UnauthorizedSovereignUResolution: missing prior decision")
    k2 = replace(k, human_acts=k.human_acts + (act,))
    return _append_history(
        k2,
        Record(
            f"human-act:{act.act_id}",
            "HumanAuthorizationAct",
            _payload(
                act_id=act.act_id,
                principal=act.principal,
                grant_id=act.grant_id,
                operation=act.operation,
                object_id=act.object_id,
                candidate=act.candidate,
                certificate_id=act.certificate_id,
                state_ref=act.state_ref,
                prior_decision_ref=act.prior_decision_ref,
            ),
            AUTH_SEM_ENV,
        ),
    )


def admit_governance_act(
    k: Configuration, act: GovernanceAuthorizationAct, *, boundary_admitted: bool
) -> Configuration:
    # This boundary admission represents the declared human intervention required
    # before design/policy authority is exercised. Authentication itself is external.
    if not boundary_admitted:
        raise AuthError("E608 HumanReviewLaundering: governance act not admitted by boundary")
    if (act.constitution_version, act.authority_epoch) != (k.constitution.version, k.authority.epoch):
        raise AuthError("E605 StaleAuthorityEnvironment")
    if act.act_id in k.used_governance_acts or any(a.act_id == act.act_id for a in k.governance_acts):
        raise AuthError("E611 AuthorizationRecordReplay")
    grant = _valid_grant(k, act.grant_id)
    if grant.kind != AuthorityKind.GOV or grant.principal != act.principal:
        raise AuthError("E608 HumanReviewLaundering: governance principal/grant mismatch")
    binding = k.authority.binding(act.principal)
    if binding is None or binding.role != AuthorityRole.GOVERNANCE or not binding.well_formed():
        raise AuthError("E608 HumanReviewLaundering: invalid governance principal")
    if not grant.authorizes(
        operation=act.operation, scope=act.scope, object_id=act.object_id,
        candidate=None, resolver=None, has_verified_basis=False
    ):
        raise AuthError("E604 TokenBindingMismatch: governance act outside grant")
    k2 = replace(k, governance_acts=k.governance_acts + (act,))
    return _append_history(
        k2, Record(
            f"gov-act:{act.act_id}", "GovernanceAuthorizationAct",
            _payload(act_id=act.act_id, principal=act.principal, grant_id=act.grant_id,
                     operation=act.operation, scope=act.scope, object_id=act.object_id,
                     state_ref=act.state_ref), AUTH_SEM_ENV
        )
    )


def _mint(
    k: Configuration,
    *,
    token_cls: Type[TToken],
    expected_kind: AuthorityKind,
    token_id: str,
    grant_id: str,
    operation: str,
    scope: str,
    object_id: str,
    candidate: Optional[str],
    certificate: Optional[VerifiedCertificate],
    state_ref: str,
    resolver: Optional[str],
    prior_decision_ref: Optional[str] = None,
) -> Tuple[Configuration, TToken]:
    grant = _valid_grant(k, grant_id)
    if grant.kind != expected_kind:
        raise AuthError("E603 TokenAuthorityEscalation")
    has_basis = _basis_matches(
        k, certificate, candidate=candidate, state_ref=state_ref, resolver=resolver
    )
    if not grant.authorizes(
        operation=operation,
        scope=scope,
        object_id=object_id,
        candidate=candidate,
        resolver=resolver,
        has_verified_basis=has_basis,
    ):
        raise AuthError("E604 TokenBindingMismatch")
    if certificate is not None and not has_basis:
        raise AuthError("E607 UnverifiedCommitBasis")
    if any(t.token_id == token_id for t in k.tokens):
        raise AuthError("E606 TokenReplay")
    token = token_cls(
        token_id=token_id,
        grant_id=grant_id,
        principal=grant.principal,
        operation=operation,
        scope=scope,
        object_id=object_id,
        candidate=candidate,
        certificate_id=certificate.certificate_id if certificate else None,
        state_ref=state_ref,
        resolver=resolver,
        prior_decision_ref=prior_decision_ref,
        constitution_version=k.constitution.version,
        authority_epoch=k.authority.epoch,
    )
    k2 = replace(k, tokens=k.tokens + (token,))
    return _append_history(
        k2,
        Record(
            f"token-mint:{token_id}",
            "TokenMintRecord",
            _payload(
                token_id=token_id,
                grant_id=grant_id,
                principal=grant.principal,
                operation=operation,
                scope=scope,
                object_id=object_id,
                candidate=candidate,
                certificate_id=token.certificate_id,
                state_ref=state_ref,
                prior_decision_ref=prior_decision_ref,
                v=k.constitution.version,
                g=k.authority.epoch,
            ),
            AUTH_SEM_ENV,
        ),
    ), token


def mint_det(
    k: Configuration, *, token_id: str, grant_id: str, operation: str, scope: str,
    object_id: str, candidate: str, certificate: VerifiedCertificate,
    state_ref: str, resolver: str
) -> Tuple[Configuration, DetToken]:
    return _mint(
        k, token_cls=DetToken, expected_kind=AuthorityKind.DET,
        token_id=token_id, grant_id=grant_id, operation=operation, scope=scope,
        object_id=object_id, candidate=candidate, certificate=certificate,
        state_ref=state_ref, resolver=resolver,
    )


def mint_human(
    k: Configuration, *, token_id: str, grant_id: str, act_id: str,
    operation: str, scope: str, object_id: str, candidate: Optional[str],
    certificate: Optional[VerifiedCertificate], state_ref: str,
    resolver: Optional[str], prior_decision_ref: Optional[str] = None,
) -> Tuple[Configuration, HumanToken]:
    act = next((a for a in k.human_acts if a.act_id == act_id), None)
    if act is None or act_id in k.used_human_acts:
        raise AuthError("E608 HumanReviewLaundering")
    expected = (
        grant_id, operation, scope, object_id, candidate,
        certificate.certificate_id if certificate else None,
        state_ref, resolver, prior_decision_ref,
    )
    actual = (
        act.grant_id, act.operation, act.scope, act.object_id, act.candidate,
        act.certificate_id, act.state_ref, act.resolver, act.prior_decision_ref,
    )
    if expected != actual:
        raise AuthError("E604 TokenBindingMismatch")
    k2, token = _mint(
        k, token_cls=HumanToken, expected_kind=AuthorityKind.HUMAN,
        token_id=token_id, grant_id=grant_id, operation=operation, scope=scope,
        object_id=object_id, candidate=candidate, certificate=certificate,
        state_ref=state_ref, resolver=resolver, prior_decision_ref=prior_decision_ref,
    )
    return replace(
        k2,
        used_human_acts=frozenset(set(k2.used_human_acts) | {act_id}),
    ), token


def mint_governance(
    k: Configuration, *, token_id: str, grant_id: str, act_id: str, operation: str,
    scope: str, object_id: str, state_ref: str
) -> Tuple[Configuration, GovernanceToken]:
    act = next((a for a in k.governance_acts if a.act_id == act_id), None)
    if act is None or act_id in k.used_governance_acts:
        raise AuthError("E608 HumanReviewLaundering: missing admitted governance act")
    expected = (grant_id, operation, scope, object_id, state_ref)
    actual = (act.grant_id, act.operation, act.scope, act.object_id, act.state_ref)
    if expected != actual:
        raise AuthError("E604 TokenBindingMismatch")
    k2, token = _mint(
        k, token_cls=GovernanceToken, expected_kind=AuthorityKind.GOV,
        token_id=token_id, grant_id=grant_id, operation=operation, scope=scope,
        object_id=object_id, candidate=None, certificate=None, state_ref=state_ref,
        resolver=None,
    )
    return replace(
        k2, used_governance_acts=frozenset(set(k2.used_governance_acts) | {act_id})
    ), token


def _resolve_live_token(k: Configuration, token: TToken) -> TToken:
    live = next((t for t in k.tokens if t.token_id == token.token_id), None)
    if live is None or live.consumed:
        raise AuthError("E606 TokenReplay")
    if live != token:
        raise AuthError("E612 TokenDeserializationForgery: token payload is not the stored capability")
    if (live.constitution_version, live.authority_epoch) != (
        k.constitution.version, k.authority.epoch
    ):
        raise AuthError("E605 StaleAuthorityEnvironment")
    return live  # type: ignore[return-value]


def _consume(k: Configuration, token: TToken) -> Configuration:
    live = _resolve_live_token(k, token)
    tokens = tuple(
        replace(t, consumed=True) if t.token_id == live.token_id else t for t in k.tokens
    )
    return replace(k, tokens=tokens)


def _check_use(token: TokenBase, use: UseContext) -> None:
    # The trusted execution boundary is responsible for authenticating `subject`.
    if not use.subject_admitted:
        raise AuthError("E604 TokenBindingMismatch: subject not admitted by execution boundary")
    if use.subject != token.principal:
        raise AuthError("E604 TokenBindingMismatch: subject is not token principal")
    if (
        use.operation, use.scope, use.object_id, use.state_ref
    ) != (
        token.operation, token.scope, token.object_id, token.state_ref
    ):
        raise AuthError("E604 TokenBindingMismatch")


def _check_commit_certificate(
    k: Configuration, token: TokenBase, certificate: VerifiedCertificate
) -> None:
    if not _is_verified(k, certificate):
        raise AuthError("E607 UnverifiedCommitBasis")
    if (
        token.certificate_id,
        token.candidate,
        token.state_ref,
        token.resolver,
    ) != (
        certificate.certificate_id,
        certificate.candidate,
        certificate.state_ref,
        certificate.resolver,
    ):
        raise AuthError("E607 UnverifiedCommitBasis")


def commit_det(
    k: Configuration, *, token: DetToken, use: UseContext,
    certificate: VerifiedCertificate, candidate: str
) -> Tuple[Configuration, CommittedDecision]:
    if not isinstance(token, DetToken) or token.operation != "commit_det":
        raise AuthError("E603 TokenAuthorityEscalation")
    live = _resolve_live_token(k, token)
    _check_use(live, use)
    if live.candidate != candidate:
        raise AuthError("E604 TokenBindingMismatch")
    _check_commit_certificate(k, live, certificate)
    k2 = _consume(k, live)
    decision = CommittedDecision(
        f"commit:{live.token_id}", live.principal, live.object_id,
        candidate, certificate.certificate_id, live.state_ref,
    )
    return _append_history(
        k2,
        Record(
            decision.decision_id, "CommittedDecision",
            _payload(
                principal=decision.principal, object_id=decision.object_id,
                value=decision.value, basis_ref=decision.basis_ref,
                state_ref=decision.state_ref,
            ),
            AUTH_SEM_ENV,
        ),
    ), decision


def commit_sovereign_u(
    k: Configuration, *, token: HumanToken, use: UseContext,
    certificate: VerifiedCertificate
) -> Tuple[Configuration, SovereignDecision]:
    if not isinstance(token, HumanToken) or token.operation != "commit_sov_u":
        raise AuthError("E609 UnauthorizedSovereignU")
    live = _resolve_live_token(k, token)
    _check_use(live, use)
    _check_commit_certificate(k, live, certificate)
    if live.candidate != "U" or not certificate.certifies_nonclosure:
        raise AuthError("E607 UnverifiedCommitBasis")
    k2 = _consume(k, live)
    decision = SovereignDecision(
        f"sovU:{live.token_id}", live.principal, live.object_id,
        "U", certificate.certificate_id, live.state_ref,
    )
    return _append_history(
        k2,
        Record(
            decision.decision_id, "SovereignDecision",
            _payload(
                principal=decision.principal, object_id=decision.object_id,
                value=decision.value, basis_ref=decision.basis_ref,
                state_ref=decision.state_ref,
            ),
            AUTH_SEM_ENV,
        ),
    ), decision


def _prior_sovereign_exists(k: Configuration, prior: SovereignDecision) -> bool:
    expected = dict(_payload(
        principal=prior.principal, object_id=prior.object_id, value=prior.value,
        basis_ref=prior.basis_ref, state_ref=prior.state_ref,
    ))
    for r in k.history:
        if r.record_id == prior.decision_id and r.kind == "SovereignDecision":
            return dict(r.payload) == expected
    return False


def resolve_sovereign_u(
    k: Configuration, *, prior: SovereignDecision, token: HumanToken,
    use: UseContext, certificate: VerifiedCertificate, candidate: str
) -> Tuple[Configuration, SovereignDecision]:
    if not prior.is_u or candidate not in {"Zero", "One"}:
        raise AuthError("E610 UnauthorizedSovereignUResolution")
    if not isinstance(token, HumanToken) or token.operation != "resolve_sov_u":
        raise AuthError("E610 UnauthorizedSovereignUResolution")
    live = _resolve_live_token(k, token)
    _check_use(live, use)
    if not _prior_sovereign_exists(k, prior):
        raise AuthError("E613 SovereignImportBypass: prior decision is not historical")
    if live.prior_decision_ref != prior.decision_id or live.object_id != prior.object_id:
        raise AuthError("E604 TokenBindingMismatch")
    if live.candidate != candidate:
        raise AuthError("E604 TokenBindingMismatch")
    _check_commit_certificate(k, live, certificate)
    k2 = _consume(k, live)
    decision = SovereignDecision(
        f"sovR:{live.token_id}", live.principal, live.object_id,
        candidate, certificate.certificate_id, live.state_ref,
    )
    return _append_history(
        k2,
        Record(
            decision.decision_id, "SovereignDecision",
            _payload(
                principal=decision.principal, object_id=decision.object_id,
                value=decision.value, basis_ref=decision.basis_ref,
                state_ref=decision.state_ref, prior_decision_ref=prior.decision_id,
            ),
            AUTH_SEM_ENV,
        ),
    ), decision


def _governance_ready(
    k: Configuration, token: GovernanceToken, use: UseContext, expected_operation: str
) -> GovernanceToken:
    if not isinstance(token, GovernanceToken) or token.operation != expected_operation:
        raise AuthError("E602 UnauthorizedGrantMutation")
    live = _resolve_live_token(k, token)
    _check_use(live, use)
    return live


def governance_bind_principal(
    k: Configuration, *, token: GovernanceToken, use: UseContext,
    binding: PrincipalBinding
) -> Configuration:
    live = _governance_ready(k, token, use, "bind_principal")
    if k.authority.binding(binding.principal) is not None or not binding.well_formed():
        raise AuthError("E615 InvariantDerogationAttempt")
    k2 = _consume(k, live)
    new_auth = replace(
        k2.authority,
        epoch=k2.authority.epoch + 1,
        bindings=k2.authority.bindings + (binding,),
    )
    out = replace(k2, authority=new_auth)
    return _append_history(
        out,
        Record(
            f"gov-bind:{binding.principal}:{new_auth.epoch}", "GovernanceRecord",
            _payload(principal=binding.principal, role=binding.role.value,
                     principal_class=binding.principal_class.value), AUTH_SEM_ENV,
        ),
    )


def governance_add_grant(
    k: Configuration, *, token: GovernanceToken, use: UseContext, grant: Grant
) -> Configuration:
    live = _governance_ready(k, token, use, "grant_add")
    if any(g.grant_id == grant.grant_id for g in k.authority.grants):
        raise AuthError("E602 UnauthorizedGrantMutation: duplicate grant")
    prospective = replace(k.authority, grants=k.authority.grants + (grant,))
    if not grant_well_formed(k.constitution, prospective, grant):
        raise AuthError("E615 InvariantDerogationAttempt")
    k2 = _consume(k, live)
    new_auth = replace(
        k2.authority,
        epoch=k2.authority.epoch + 1,
        grants=k2.authority.grants + (grant,),
    )
    out = replace(k2, authority=new_auth)
    return _append_history(
        out,
        Record(
            f"gov-grant:{grant.grant_id}:{new_auth.epoch}", "GovernanceRecord",
            _payload(grant_id=grant.grant_id, principal=grant.principal,
                     kind=grant.kind.value), AUTH_SEM_ENV,
        ),
    )


def constitution_revision(
    k: Configuration, *, token: GovernanceToken, use: UseContext,
    new_constitution: Constitution
) -> Configuration:
    live = _governance_ready(k, token, use, "constitution_revision")
    if new_constitution.version != k.constitution.version + 1:
        raise AuthError("E605 StaleAuthorityEnvironment")
    if not set(AuthorityRole).issubset(new_constitution.roles):
        raise AuthError("E615 InvariantDerogationAttempt")
    if any(not grant_well_formed(new_constitution, k.authority, g) for g in k.authority.grants):
        raise AuthError("E615 InvariantDerogationAttempt")
    k2 = _consume(k, live)
    out = replace(k2, constitution=new_constitution)
    return _append_history(
        out,
        Record(
            f"constitution:{new_constitution.version}", "ConstitutionRevisionRecord",
            _payload(version=new_constitution.version), AUTH_SEM_ENV,
        ),
    )


def deserialize_token(_: dict) -> TokenBase:
    raise AuthError("E612 TokenDeserializationForgery")


def deserialize_sovereign_decision(_: dict) -> SovereignDecision:
    raise AuthError("E613 SovereignImportBypass")


def restore(snapshot: Configuration, *, snapshot_admitted: bool) -> Configuration:
    # Trusted snapshot restoration is initialization, not an operational constructor.
    if not snapshot_admitted:
        raise AuthError("E613 SovereignImportBypass: snapshot not admitted by restore boundary")
    out = replace(snapshot, tokens=())
    if not wf_auth(out):
        raise AuthError("E617 HistoricalSemanticDrift: invalid snapshot")
    return out


def denote(k: Configuration, record: Record) -> Tuple[str, Tuple[Tuple[str, str], ...]]:
    env = k.semantic_env(record.semantic_env_ref)
    return env.env_id, record.payload


def authority_profile(k: Configuration, principal: str) -> FrozenSet[Tuple[str, str]]:
    valid = k.aenv()
    return frozenset(
        (op, scope)
        for g in k.authority.grants if g in valid and g.principal == principal
        for op in g.operations for scope in g.scopes
    )


def resolver_equivalent(a: ResolverSignature, b: ResolverSignature) -> bool:
    return a == b


def enabled_authority(
    k: Configuration, *, candidate: Optional[str], state_ref: str,
    resolver: Optional[str], principal: Optional[str] = None
) -> FrozenSet[Tuple[str, str, str, str]]:
    out = set()
    verified = _verified_certificates(k)
    for grant in k.authority.grants:
        if grant not in k.aenv():
            continue
        if principal is not None and grant.principal != principal:
            continue
        for operation in grant.operations:
            has_basis = any(
                c.candidate == candidate
                and c.state_ref == state_ref
                and c.resolver == resolver
                and (operation != "commit_sov_u" or c.certifies_nonclosure)
                for c in verified
            )
            for scope in grant.scopes:
                for object_id in grant.objects:
                    if grant.authorizes(
                        operation=operation, scope=scope, object_id=object_id,
                        candidate=candidate, resolver=resolver,
                        has_verified_basis=has_basis,
                    ):
                        out.add((grant.grant_id, operation, scope, object_id))
    return frozenset(out)
