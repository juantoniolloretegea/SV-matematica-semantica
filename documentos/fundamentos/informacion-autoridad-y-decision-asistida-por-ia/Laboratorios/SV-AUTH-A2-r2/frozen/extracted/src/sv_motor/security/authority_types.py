from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import FrozenSet, Optional, Tuple


class AuthError(RuntimeError):
    pass


class AuthorityKind(str, Enum):
    DET = "det"
    HUMAN = "human"
    GOV = "gov"


class AuthorityRole(str, Enum):
    DET_SERVICE = "det-service"
    HUMAN_SOVEREIGN = "human-sovereign"
    GOVERNANCE = "governance"


class PrincipalClass(str, Enum):
    HUMAN = "human"
    SERVICE = "service"
    EXTERNAL = "external"
    GOVERNANCE = "governance"


ROLE_KIND = {
    AuthorityRole.DET_SERVICE: AuthorityKind.DET,
    AuthorityRole.HUMAN_SOVEREIGN: AuthorityKind.HUMAN,
    AuthorityRole.GOVERNANCE: AuthorityKind.GOV,
}


@dataclass(frozen=True)
class PrincipalBinding:
    principal: str
    role: AuthorityRole
    principal_class: PrincipalClass

    def well_formed(self) -> bool:
        if self.role == AuthorityRole.HUMAN_SOVEREIGN:
            return self.principal_class == PrincipalClass.HUMAN
        if self.role == AuthorityRole.GOVERNANCE:
            return self.principal_class == PrincipalClass.GOVERNANCE
        return self.principal_class in {PrincipalClass.SERVICE, PrincipalClass.EXTERNAL}


@dataclass(frozen=True)
class VerifierSpec:
    verifier_id: str
    resolver: str
    can_certify_nonclosure: bool = False


@dataclass(frozen=True)
class Grant:
    grant_id: str
    principal: str
    kind: AuthorityKind
    operations: FrozenSet[str]
    scopes: FrozenSet[str]
    objects: FrozenSet[str]
    resolver: Optional[str] = None
    allowed_candidates: Optional[FrozenSet[str]] = None
    requires_verified_certificate: bool = False

    def authorizes(
        self,
        *,
        operation: str,
        scope: str,
        object_id: str,
        candidate: Optional[str],
        resolver: Optional[str],
        has_verified_basis: bool,
    ) -> bool:
        if operation not in self.operations or scope not in self.scopes or object_id not in self.objects:
            return False
        if self.resolver is not None and self.resolver != resolver:
            return False
        if self.allowed_candidates is not None and candidate not in self.allowed_candidates:
            return False
        if self.requires_verified_certificate and not has_verified_basis:
            return False
        return True


@dataclass(frozen=True)
class AuthorityState:
    epoch: int
    grants: Tuple[Grant, ...] = ()
    bindings: Tuple[PrincipalBinding, ...] = ()

    def binding(self, principal: str) -> Optional[PrincipalBinding]:
        return next((b for b in self.bindings if b.principal == principal), None)

    def grant(self, grant_id: str) -> Grant:
        matches = [g for g in self.grants if g.grant_id == grant_id]
        if len(matches) != 1:
            raise AuthError("E602 UnauthorizedGrantMutation: grant missing or ambiguous")
        return matches[0]


@dataclass(frozen=True)
class Constitution:
    version: int
    roles: FrozenSet[AuthorityRole] = frozenset(AuthorityRole)
    verifiers: Tuple[VerifierSpec, ...] = ()

    def verifier(self, verifier_id: str) -> VerifierSpec:
        matches = [v for v in self.verifiers if v.verifier_id == verifier_id]
        if len(matches) != 1:
            raise AuthError("E607 UnverifiedCommitBasis: verifier not declared")
        return matches[0]


@dataclass(frozen=True)
class RawCertificate:
    certificate_id: str
    candidate: str
    state_ref: str
    resolver: str
    certifies_nonclosure: bool = False


@dataclass(frozen=True)
class VerifiedCertificate:
    certificate_id: str
    candidate: str
    state_ref: str
    resolver: str
    verifier_id: str
    certifies_nonclosure: bool = False


@dataclass(frozen=True)
class HumanReviewRequest:
    request_id: str
    object_id: str
    state_ref: str


@dataclass(frozen=True)
class GovernanceAuthorizationAct:
    act_id: str
    grant_id: str
    principal: str
    operation: str
    scope: str
    object_id: str
    state_ref: str
    constitution_version: int
    authority_epoch: int


@dataclass(frozen=True)
class HumanAuthorizationAct:
    act_id: str
    grant_id: str
    principal: str
    operation: str
    scope: str
    object_id: str
    candidate: Optional[str]
    certificate_id: Optional[str]
    state_ref: str
    resolver: Optional[str]
    prior_decision_ref: Optional[str]
    constitution_version: int
    authority_epoch: int


@dataclass(frozen=True)
class TokenBase:
    token_id: str
    grant_id: str
    principal: str
    operation: str
    scope: str
    object_id: str
    candidate: Optional[str]
    certificate_id: Optional[str]
    state_ref: str
    resolver: Optional[str]
    prior_decision_ref: Optional[str]
    constitution_version: int
    authority_epoch: int
    consumed: bool = False


@dataclass(frozen=True)
class DetToken(TokenBase):
    pass


@dataclass(frozen=True)
class HumanToken(TokenBase):
    pass


@dataclass(frozen=True)
class GovernanceToken(TokenBase):
    pass


@dataclass(frozen=True)
class SemanticEnvironment:
    env_id: str
    interpretation: Tuple[Tuple[str, str], ...] = ()


@dataclass(frozen=True)
class Record:
    record_id: str
    kind: str
    payload: Tuple[Tuple[str, str], ...]
    semantic_env_ref: str


@dataclass(frozen=True)
class SovereignDecision:
    decision_id: str
    principal: str
    object_id: str
    value: str  # Zero | One | U
    basis_ref: str
    state_ref: str

    @property
    def is_u(self) -> bool:
        return self.value == "U"


@dataclass(frozen=True)
class CommittedDecision:
    decision_id: str
    principal: str
    object_id: str
    value: str
    basis_ref: str
    state_ref: str


@dataclass(frozen=True)
class ResolverSignature:
    candidate: str
    context_signature: Tuple[str, ...]


@dataclass(frozen=True)
class UseContext:
    subject: str
    executor: str
    operation: str
    scope: str
    object_id: str
    state_ref: str
    subject_admitted: bool = False


def required_role(kind: AuthorityKind) -> AuthorityRole:
    if kind == AuthorityKind.DET:
        return AuthorityRole.DET_SERVICE
    if kind == AuthorityKind.HUMAN:
        return AuthorityRole.HUMAN_SOVEREIGN
    return AuthorityRole.GOVERNANCE


def grant_well_formed(constitution: Constitution, authority: AuthorityState, grant: Grant) -> bool:
    binding = authority.binding(grant.principal)
    if binding is None or not binding.well_formed():
        return False
    if binding.role not in constitution.roles or binding.role != required_role(grant.kind):
        return False
    sovereign_ops = {"commit_sov_u", "resolve_sov_u"}
    if grant.kind != AuthorityKind.HUMAN and sovereign_ops.intersection(grant.operations):
        return False
    if grant.requires_verified_certificate:
        if grant.resolver is None:
            return False
        if not any(v.resolver == grant.resolver for v in constitution.verifiers):
            return False
    return True


@dataclass(frozen=True)
class Configuration:
    constitution: Constitution
    information: Tuple[object, ...]
    authority: AuthorityState
    tokens: Tuple[TokenBase, ...] = ()
    history: Tuple[Record, ...] = ()
    semantic_registry: Tuple[SemanticEnvironment, ...] = ()
    human_acts: Tuple[HumanAuthorizationAct, ...] = ()
    used_human_acts: FrozenSet[str] = frozenset()
    governance_acts: Tuple[GovernanceAuthorizationAct, ...] = ()
    used_governance_acts: FrozenSet[str] = frozenset()

    def aenv(self) -> FrozenSet[Grant]:
        return frozenset(
            g for g in self.authority.grants
            if grant_well_formed(self.constitution, self.authority, g)
        )

    def semantic_env(self, env_id: str) -> SemanticEnvironment:
        matches = [e for e in self.semantic_registry if e.env_id == env_id]
        if len(matches) != 1:
            raise AuthError("E617 HistoricalSemanticDrift: semantic environment missing or ambiguous")
        return matches[0]
