import pytest
from dataclasses import replace

from sv_motor.security.authority import *


def base_config() -> Configuration:
    bindings = (
        PrincipalBinding("svc", AuthorityRole.DET_SERVICE, PrincipalClass.SERVICE),
        PrincipalBinding("alice", AuthorityRole.HUMAN_SOVEREIGN, PrincipalClass.HUMAN),
        PrincipalBinding("admin", AuthorityRole.GOVERNANCE, PrincipalClass.GOVERNANCE),
    )
    grants = (
        Grant("g-det", "svc", AuthorityKind.DET, frozenset({"commit_det"}),
              frozenset({"D"}), frozenset({"obj"}), "R",
              frozenset({"Zero", "One"}), True),
        Grant("g-human-u", "alice", AuthorityKind.HUMAN,
              frozenset({"commit_sov_u"}), frozenset({"D"}), frozenset({"obj"}),
              "R", frozenset({"U"}), True),
        Grant("g-human-r", "alice", AuthorityKind.HUMAN,
              frozenset({"resolve_sov_u"}), frozenset({"D"}), frozenset({"obj"}),
              "R", frozenset({"Zero", "One"}), True),
        Grant("g-gov", "admin", AuthorityKind.GOV,
              frozenset({"grant_add", "bind_principal", "constitution_revision"}),
              frozenset({"AUTH"}), frozenset({"authority"}), None, None, False),
    )
    constitution = Constitution(
        1,
        frozenset(AuthorityRole),
        (
            VerifierSpec("ver:R", "R", False),
            VerifierSpec("ver:NC", "R", True),
        ),
    )
    return Configuration(
        constitution, (), AuthorityState(1, grants, bindings),
        semantic_registry=(SemanticEnvironment(AUTH_SEM_ENV),),
    )


def raw(candidate="Zero", *, cid="c0", state="s0", resolver="R", nonclosure=False):
    return RawCertificate(cid, candidate, state, resolver, nonclosure)


def verified(k, candidate="Zero", *, cid="c0", state="s0", nonclosure=False):
    verifier = "ver:NC" if nonclosure else "ver:R"
    return verify_certificate(k, raw(candidate, cid=cid, state=state, nonclosure=nonclosure), verifier_id=verifier, verifier_admitted=True)


def human_act(k, operation, candidate, certificate, *, act_id="a1", grant_id=None,
              principal="alice", state="s0", prior=None):
    if grant_id is None:
        grant_id = "g-human-u" if operation == "commit_sov_u" else "g-human-r"
    return HumanAuthorizationAct(
        act_id, grant_id, principal, operation, "D", "obj", candidate,
        certificate.certificate_id if certificate else None, state, "R", prior,
        k.constitution.version, k.authority.epoch,
    )



def governance_token(k, *, token_id, operation, state_ref="s0"):
    act = GovernanceAuthorizationAct(
        f"act:{token_id}", "g-gov", "admin", operation, "AUTH", "authority", state_ref,
        k.constitution.version, k.authority.epoch
    )
    k = admit_governance_act(k, act, boundary_admitted=True)
    return mint_governance(k, token_id=token_id, grant_id="g-gov", act_id=act.act_id,
                           operation=operation, scope="AUTH", object_id="authority", state_ref=state_ref)


def det_token(k, candidate="Zero"):
    k, c = verified(k, candidate)
    k, t = mint_det(k, token_id="t", grant_id="g-det", operation="commit_det",
                    scope="D", object_id="obj", candidate=candidate,
                    certificate=c, state_ref="s0", resolver="R")
    return k, t, c


def human_u_committed(k=None):
    k = base_config() if k is None else k
    k, nc = verified(k, "U", cid="nc", nonclosure=True)
    act = human_act(k, "commit_sov_u", "U", nc)
    k = admit_human_act(k, act, boundary_admitted=True)
    k, h = mint_human(k, token_id="h-u", grant_id="g-human-u", act_id=act.act_id,
                      operation="commit_sov_u", scope="D", object_id="obj",
                      candidate="U", certificate=nc, state_ref="s0", resolver="R")
    k, d = commit_sovereign_u(
        k, token=h, use=UseContext("alice", "runtime", "commit_sov_u", "D", "obj", "s0", True),
        certificate=nc,
    )
    return k, d


# Baseline well-formedness

def test_base_is_wf():
    k = base_config()
    assert wf_auth(k)
    assert {g.grant_id for g in k.aenv()} == {"g-det", "g-human-u", "g-human-r", "g-gov"}


# AES — information/certificate barriers

def test_ce01_information_cannot_create_grant():
    with pytest.raises(AuthError):
        info_add(base_config(), Grant("x", "svc", AuthorityKind.DET, frozenset(), frozenset(), frozenset()))


def test_ce01b_information_cannot_inject_verified_certificate():
    forged = VerifiedCertificate("f", "Zero", "s0", "R", "ver:R")
    with pytest.raises(AuthError): info_add(base_config(), forged)


def test_ce01c_unknown_verifier_cannot_verify():
    with pytest.raises(AuthError): verify_certificate(base_config(), raw(), verifier_id="unknown", verifier_admitted=True)


def test_ce01d_nonclosure_requires_nonclosure_verifier():
    with pytest.raises(AuthError):
        verify_certificate(base_config(), raw("U", nonclosure=True), verifier_id="ver:R", verifier_admitted=True)


def test_ce02_scope_cannot_exceed_grant():
    k, c = verified(base_config())
    with pytest.raises(AuthError):
        mint_det(k, token_id="t", grant_id="g-det", operation="commit_det", scope="OTHER",
                 object_id="obj", candidate="Zero", certificate=c, state_ref="s0", resolver="R")


def test_ce03_subject_cannot_present_anothers_token():
    k, t, c = det_token(base_config())
    with pytest.raises(AuthError):
        commit_det(k, token=t, use=UseContext("external", "runtime", "commit_det", "D", "obj", "s0", True),
                   certificate=c, candidate="Zero")


def test_ce04_grant_candidate_policy_is_enforced():
    k, c = verified(base_config(), "U", cid="u")
    with pytest.raises(AuthError):
        mint_det(k, token_id="t", grant_id="g-det", operation="commit_det", scope="D",
                 object_id="obj", candidate="U", certificate=c, state_ref="s0", resolver="R")


def test_ce04b_forged_certificate_dataclass_is_not_verified_basis():
    k = base_config()
    forged = VerifiedCertificate("f", "Zero", "s0", "R", "ver:R")
    with pytest.raises(AuthError):
        mint_det(k, token_id="t", grant_id="g-det", operation="commit_det", scope="D",
                 object_id="obj", candidate="Zero", certificate=forged, state_ref="s0", resolver="R")


def test_ce05_informational_binding_cannot_change_aenv():
    k = base_config(); before = k.aenv()
    with pytest.raises(AuthError):
        info_add(k, PrincipalBinding("llm", AuthorityRole.HUMAN_SOVEREIGN, PrincipalClass.EXTERNAL))
    assert k.aenv() == before


def test_ce06_unverified_commit_basis_rejected():
    k, t, c = det_token(base_config())
    fake = replace(c, certificate_id="fake")
    with pytest.raises(AuthError):
        commit_det(k, token=t, use=UseContext("svc", "runtime", "commit_det", "D", "obj", "s0", True),
                   certificate=fake, candidate="Zero")


def test_ce07_token_candidate_cannot_be_reused_for_other_candidate():
    k, t, c = det_token(base_config(), "Zero")
    with pytest.raises(AuthError):
        commit_det(k, token=t, use=UseContext("svc", "runtime", "commit_det", "D", "obj", "s0", True),
                   certificate=c, candidate="One")


def test_ce08a_constitution_version_stales_token():
    k, t, c = det_token(base_config())
    k = replace(k, constitution=replace(k.constitution, version=2))
    with pytest.raises(AuthError):
        commit_det(k, token=t, use=UseContext("svc", "runtime", "commit_det", "D", "obj", "s0", True),
                   certificate=c, candidate="Zero")


def test_ce08b_authority_epoch_stales_token():
    k, t, c = det_token(base_config())
    k = replace(k, authority=replace(k.authority, epoch=2))
    with pytest.raises(AuthError):
        commit_det(k, token=t, use=UseContext("svc", "runtime", "commit_det", "D", "obj", "s0", True),
                   certificate=c, candidate="Zero")


def test_ce09_resolver_equivalence_does_not_inherit_permissions():
    k = base_config()
    sig = ResolverSignature("Zero", ("ctx",))
    assert resolver_equivalent(sig, sig)
    assert authority_profile(k, "external") == frozenset()
    assert authority_profile(k, "svc")


def test_ce10_human_act_cannot_be_replayed_for_second_mint():
    k = base_config(); k, nc = verified(k, "U", cid="nc", nonclosure=True)
    act = human_act(k, "commit_sov_u", "U", nc)
    k = admit_human_act(k, act, boundary_admitted=True)
    k, _ = mint_human(k, token_id="h1", grant_id="g-human-u", act_id=act.act_id,
                      operation="commit_sov_u", scope="D", object_id="obj", candidate="U",
                      certificate=nc, state_ref="s0", resolver="R")
    with pytest.raises(AuthError):
        mint_human(k, token_id="h2", grant_id="g-human-u", act_id=act.act_id,
                   operation="commit_sov_u", scope="D", object_id="obj", candidate="U",
                   certificate=nc, state_ref="s0", resolver="R")


def test_ce11a_deserialization_cannot_create_token():
    with pytest.raises(AuthError): deserialize_token({"token_id": "t"})


def test_ce11b_sovereign_import_not_operational_constructor():
    with pytest.raises(AuthError): deserialize_sovereign_decision({"value": "U"})


def test_ce11c_same_id_modified_token_is_forgery():
    k, t, c = det_token(base_config())
    forged = replace(t, object_id="other")
    with pytest.raises(AuthError):
        commit_det(k, token=forged, use=UseContext("svc", "runtime", "commit_det", "D", "other", "s0", True),
                   certificate=c, candidate="Zero")


def test_ce12a_history_payload_immutable():
    r = Record("r", "x", (("a", "b"),), AUTH_SEM_ENV)
    with pytest.raises(Exception): r.payload = (("a", "c"),)


def test_ce12b_semantic_ref_immutable():
    r = Record("r", "x", (("a", "b"),), AUTH_SEM_ENV)
    with pytest.raises(Exception): r.semantic_env_ref = "sem:new"


def test_ce12c_restore_rejects_missing_semantic_environment():
    k = base_config()
    bad = replace(k, history=(Record("r", "x", (), "missing"),))
    with pytest.raises(AuthError): restore(bad, snapshot_admitted=True)


def test_ce13_det_grant_cannot_mint_human_token():
    k = base_config(); k, nc = verified(k, "U", cid="nc", nonclosure=True)
    act = human_act(k, "commit_sov_u", "U", nc)
    k = admit_human_act(k, act, boundary_admitted=True)
    with pytest.raises(AuthError):
        mint_human(k, token_id="h", grant_id="g-det", act_id=act.act_id,
                   operation="commit_sov_u", scope="D", object_id="obj", candidate="U",
                   certificate=nc, state_ref="s0", resolver="R")


def test_ce14_governance_cannot_make_det_sovereign_grant():
    k = base_config(); k, gt = governance_token(k, token_id="g", operation="grant_add", state_ref="s0")
    bad = Grant("bad", "svc", AuthorityKind.DET, frozenset({"commit_sov_u"}),
                frozenset({"D"}), frozenset({"obj"}), "R", frozenset({"U"}), True)
    with pytest.raises(AuthError):
        governance_add_grant(k, token=gt,
            use=UseContext("admin", "runtime", "grant_add", "AUTH", "authority", "s0", True), grant=bad)


def test_ce14b_governance_cannot_bind_external_as_human_sovereign():
    k = base_config(); k, gt = governance_token(k, token_id="g", operation="bind_principal", state_ref="s0")
    bad = PrincipalBinding("llm", AuthorityRole.HUMAN_SOVEREIGN, PrincipalClass.EXTERNAL)
    with pytest.raises(AuthError):
        governance_bind_principal(k, token=gt,
            use=UseContext("admin", "runtime", "bind_principal", "AUTH", "authority", "s0", True), binding=bad)


def test_ce14c_governance_operation_mismatch_cannot_add_grant():
    k = base_config(); k, gt = governance_token(k, token_id="g", operation="bind_principal", state_ref="s0")
    new = Grant("x", "svc", AuthorityKind.DET, frozenset({"commit_det"}),
                frozenset({"D"}), frozenset({"obj"}), "R", frozenset({"Zero"}), True)
    with pytest.raises(AuthError):
        governance_add_grant(k, token=gt,
            use=UseContext("admin", "runtime", "bind_principal", "AUTH", "authority", "s0", True), grant=new)


def test_ce15_det_token_cannot_commit_sovereign_u():
    k, t, _ = det_token(base_config())
    k, nc = verified(k, "U", cid="nc", nonclosure=True)
    with pytest.raises((AuthError, TypeError)):
        commit_sovereign_u(k, token=t,  # type: ignore[arg-type]
            use=UseContext("svc", "runtime", "commit_det", "D", "obj", "s0", True), certificate=nc)


def test_ce16_det_token_cannot_resolve_sovereign_u():
    k, t, c = det_token(base_config())
    prior = SovereignDecision("u", "alice", "obj", "U", "nc", "s0")
    with pytest.raises((AuthError, TypeError)):
        resolve_sovereign_u(k, prior=prior, token=t,  # type: ignore[arg-type]
            use=UseContext("svc", "runtime", "commit_det", "D", "obj", "s0", True),
            certificate=c, candidate="Zero")


def test_ce17_scope_and_object_binding_cannot_move():
    k, t, c = det_token(base_config())
    with pytest.raises(AuthError):
        commit_det(k, token=t, use=UseContext("svc", "runtime", "commit_det", "OTHER", "obj", "s0", True),
                   certificate=c, candidate="Zero")


def test_ce18_external_consensus_does_not_mint_authority():
    k = base_config(); before = k.aenv()
    for i in range(100): k = info_add(k, {"actor": i, "candidate": "Zero"})
    assert k.aenv() == before and authority_profile(k, "external") == frozenset()


def test_ce19_exact_output_equality_no_authority_transfer():
    k = base_config()
    a = ResolverSignature("Zero", ("ctx",)); b = ResolverSignature("Zero", ("ctx",))
    assert resolver_equivalent(a, b)
    assert authority_profile(k, "external") == frozenset()
    assert authority_profile(k, "svc")


def test_ce20_resolution_context_cannot_change_grants():
    k = base_config(); before = k.aenv(); k = info_add(k, {"resolution_context": "new"})
    assert k.aenv() == before


def test_ce21_review_request_does_not_mint_human_token():
    k, req = request_human(base_config(), request_id="r", object_id="obj", state_ref="s0")
    assert req in k.information and not k.human_acts and not k.tokens


# Additional spec-runtime attacks found in cross-audit

def test_ax01_human_act_principal_must_match_grant():
    k = base_config(); k, nc = verified(k, "U", cid="nc", nonclosure=True)
    act = human_act(k, "commit_sov_u", "U", nc, principal="mallory")
    with pytest.raises(AuthError): admit_human_act(k, act, boundary_admitted=True)


def test_ax02_human_act_basis_is_bound():
    k = base_config(); k, nc = verified(k, "U", cid="nc", nonclosure=True)
    forged = replace(nc, certificate_id="other")
    act = HumanAuthorizationAct("a", "g-human-u", "alice", "commit_sov_u", "D", "obj", "U",
                                forged.certificate_id, "s0", "R", None, 1, 1)
    with pytest.raises(AuthError): admit_human_act(k, act, boundary_admitted=True)


def test_ax03_use_scope_is_bound():
    k, t, c = det_token(base_config())
    with pytest.raises(AuthError):
        commit_det(k, token=t, use=UseContext("svc", "runtime", "commit_det", "X", "obj", "s0", True),
                   certificate=c, candidate="Zero")


def test_ax04_fabricated_prior_sovereign_u_cannot_be_resolved():
    k = base_config(); k, c = verified(k, "Zero", cid="r1")
    prior = SovereignDecision("fake", "alice", "obj", "U", "nc", "s0")
    act = human_act(k, "resolve_sov_u", "Zero", c, act_id="aR", prior="fake")
    k = admit_human_act(k, act, boundary_admitted=True)
    k, h = mint_human(k, token_id="hR", grant_id="g-human-r", act_id="aR",
                      operation="resolve_sov_u", scope="D", object_id="obj", candidate="Zero",
                      certificate=c, state_ref="s0", resolver="R", prior_decision_ref="fake")
    with pytest.raises(AuthError):
        resolve_sovereign_u(k, prior=prior, token=h,
            use=UseContext("alice", "runtime", "resolve_sov_u", "D", "obj", "s0", True),
            certificate=c, candidate="Zero")


def test_ax05_duplicate_grant_id_rejected():
    k = base_config(); k, gt = governance_token(k, token_id="g", operation="grant_add", state_ref="s0")
    dup = k.authority.grant("g-det")
    with pytest.raises(AuthError): governance_add_grant(k, token=gt,
        use=UseContext("admin", "runtime", "grant_add", "AUTH", "authority", "s0", True), grant=dup)


def test_ax06_constitution_cannot_remove_required_authority_role():
    k = base_config(); k, gt = governance_token(k, token_id="g", operation="constitution_revision", state_ref="s0")
    bad = Constitution(2, frozenset({AuthorityRole.DET_SERVICE, AuthorityRole.GOVERNANCE}), k.constitution.verifiers)
    with pytest.raises(AuthError): constitution_revision(k, token=gt,
        use=UseContext("admin", "runtime", "constitution_revision", "AUTH", "authority", "s0", True),
        new_constitution=bad)


# P1 witnesses

def test_p1_w1_same_resolver_signature_different_authority():
    k = base_config(); sig = ResolverSignature("Zero", ("role:A", "ctx:1"))
    assert resolver_equivalent(sig, sig)
    assert authority_profile(k, "external") != authority_profile(k, "svc")


def test_p1_w2_same_authority_different_resolver_signature():
    b2 = PrincipalBinding("svc2", AuthorityRole.DET_SERVICE, PrincipalClass.SERVICE)
    g2 = replace(base_config().authority.grant("g-det"), grant_id="g-det-2", principal="svc2")
    k = base_config(); auth = replace(k.authority, bindings=k.authority.bindings + (b2,), grants=k.authority.grants + (g2,)); k = replace(k, authority=auth)
    assert authority_profile(k, "svc") == authority_profile(k, "svc2")
    assert not resolver_equivalent(ResolverSignature("Zero", ("ctx:1",)), ResolverSignature("One", ("ctx:1",)))


# LAS — legitimate authorization

def test_la01_verified_information_enables_existing_grant_without_changing_aenv():
    k = base_config(); before_env = k.aenv()
    before = enabled_authority(k, candidate="Zero", state_ref="s0", resolver="R", principal="svc")
    assert before == frozenset()
    k, _ = verified(k, "Zero")
    after = enabled_authority(k, candidate="Zero", state_ref="s0", resolver="R", principal="svc")
    assert k.aenv() == before_env and ("g-det", "commit_det", "D", "obj") in after


def test_la02_external_data_can_determine_and_authorized_service_commit():
    k, t, c = det_token(base_config(), "Zero")
    k, d = commit_det(k, token=t,
        use=UseContext("svc", "runtime", "commit_det", "D", "obj", "s0", True),
        certificate=c, candidate="Zero")
    assert d.value == "Zero" and d.principal == "svc"


def test_la03_local_u_can_be_replaced_by_new_information_without_human_token():
    k = base_config(); k = info_add(k, {"tri": "U"}); k = info_add(k, {"tri": "Zero"})
    assert not k.human_acts and not k.tokens


def test_la04_human_review_request_is_legitimate_and_non_authorizing():
    k, req = request_human(base_config(), request_id="r", object_id="obj", state_ref="s0")
    assert req in k.information and not k.tokens


def test_la05_human_act_can_mint_scoped_token_and_commit_sovereign_u():
    k, d = human_u_committed()
    assert d.is_u and d.principal == "alice" and any(r.record_id == d.decision_id for r in k.history)


def test_la06_governance_channel_can_bind_external_service_and_add_grant():
    k = base_config()
    k, gt = governance_token(k, token_id="gb", operation="bind_principal", state_ref="s0")
    k = governance_bind_principal(k, token=gt,
        use=UseContext("admin", "runtime", "bind_principal", "AUTH", "authority", "s0", True),
        binding=PrincipalBinding("idp:alice", AuthorityRole.DET_SERVICE, PrincipalClass.EXTERNAL))
    # epoch advanced: mint a fresh governance token before the second governance act
    k, gt2 = governance_token(k, token_id="gg", operation="grant_add", state_ref="s1")
    new = Grant("g-idp", "idp:alice", AuthorityKind.DET, frozenset({"commit_det"}),
                frozenset({"D"}), frozenset({"obj"}), "R", frozenset({"Zero", "One"}), True)
    k = governance_add_grant(k, token=gt2,
        use=UseContext("admin", "runtime", "grant_add", "AUTH", "authority", "s1", True), grant=new)
    assert "g-idp" in {g.grant_id for g in k.aenv()} and k.authority.epoch == 3


def test_la07_existing_sovereign_u_can_be_resolved_with_fresh_human_act():
    k, prior = human_u_committed()
    k, c = verified(k, "Zero", cid="resolve", state="s1")
    act = human_act(k, "resolve_sov_u", "Zero", c, act_id="aR", state="s1", prior=prior.decision_id)
    k = admit_human_act(k, act, boundary_admitted=True)
    k, h = mint_human(k, token_id="hR", grant_id="g-human-r", act_id="aR",
                      operation="resolve_sov_u", scope="D", object_id="obj", candidate="Zero",
                      certificate=c, state_ref="s1", resolver="R", prior_decision_ref=prior.decision_id)
    k, d = resolve_sovereign_u(k, prior=prior, token=h,
        use=UseContext("alice", "runtime", "resolve_sov_u", "D", "obj", "s1", True),
        certificate=c, candidate="Zero")
    assert d.value == "Zero" and prior.is_u


def test_la08_constitution_revision_preserves_invariants_and_stales_old_tokens():
    k = base_config(); k, dt, _ = det_token(k)
    k, gt = governance_token(k, token_id="gc", operation="constitution_revision", state_ref="s0")
    newc = Constitution(2, k.constitution.roles, k.constitution.verifiers)
    k = constitution_revision(k, token=gt,
        use=UseContext("admin", "runtime", "constitution_revision", "AUTH", "authority", "s0", True),
        new_constitution=newc)
    assert wf_auth(k) and k.constitution.version == 2
    with pytest.raises(AuthError): _resolve_live_token_for_test(k, dt)


def _resolve_live_token_for_test(k, token):
    # exercise the stale-token condition through a public commit rather than importing private helpers
    c = next(x for x in k.information if isinstance(x, VerifiedCertificate) and x.candidate == "Zero")
    return commit_det(k, token=token,
        use=UseContext("svc", "runtime", "commit_det", "D", "obj", "s0", True),
        certificate=c, candidate="Zero")


# Structural theorem witnesses / semantic-history checks

def test_ta_ordinary_trace_preserves_aenv():
    k = base_config(); before = k.aenv()
    for i in range(20): k = info_add(k, {"i": i})
    k, c = verified(k, "Zero")
    k, t = mint_det(k, token_id="t", grant_id="g-det", operation="commit_det", scope="D",
                    object_id="obj", candidate="Zero", certificate=c, state_ref="s0", resolver="R")
    k, _ = commit_det(k, token=t,
        use=UseContext("svc", "runtime", "commit_det", "D", "obj", "s0", True),
        certificate=c, candidate="Zero")
    assert k.aenv() == before


def test_tb_no_human_act_no_sovereign_u_path():
    k = base_config(); k, nc = verified(k, "U", cid="nc", nonclosure=True)
    with pytest.raises(AuthError):
        mint_human(k, token_id="h", grant_id="g-human-u", act_id="none",
                   operation="commit_sov_u", scope="D", object_id="obj", candidate="U",
                   certificate=nc, state_ref="s0", resolver="R")


def test_history_is_prefix_under_ordinary_trace():
    k = base_config(); h0 = k.history
    k, c = verified(k, "Zero"); k, t = mint_det(k, token_id="t", grant_id="g-det",
        operation="commit_det", scope="D", object_id="obj", candidate="Zero",
        certificate=c, state_ref="s0", resolver="R")
    h1 = k.history
    k, _ = commit_det(k, token=t,
        use=UseContext("svc", "runtime", "commit_det", "D", "obj", "s0", True), certificate=c, candidate="Zero")
    assert k.history[:len(h0)] == h0 and k.history[:len(h1)] == h1


def test_semantic_denotation_of_old_record_does_not_drift_when_new_env_is_added():
    k, _ = human_u_committed(); r = k.history[-1]; before = denote(k, r)
    k2 = replace(k, semantic_registry=k.semantic_registry + (SemanticEnvironment("sem:new", (("U", "changed"),)),))
    assert denote(k2, r) == before


def test_restore_drops_live_tokens_and_preserves_history():
    k, _, _ = det_token(base_config()); h = k.history
    r = restore(k, snapshot_admitted=True)
    assert r.tokens == () and r.history == h and wf_auth(r)

def test_ax07_verifier_boundary_is_explicit():
    with pytest.raises(AuthError):
        verify_certificate(base_config(), raw(), verifier_id="ver:R", verifier_admitted=False)


def test_ax08_governance_token_requires_admitted_governance_act():
    with pytest.raises(AuthError):
        mint_governance(base_config(), token_id="g", grant_id="g-gov", act_id="missing",
                        operation="grant_add", scope="AUTH", object_id="authority", state_ref="s0")


def test_ax09_execution_subject_requires_boundary_admission():
    k, t, c = det_token(base_config())
    with pytest.raises(AuthError):
        commit_det(k, token=t,
                   use=UseContext("svc", "runtime", "commit_det", "D", "obj", "s0", False),
                   certificate=c, candidate="Zero")


def test_ax10_restore_requires_trusted_snapshot_admission():
    with pytest.raises(AuthError): restore(base_config(), snapshot_admitted=False)

# Branch-completeness attacks for the reference runtime

def test_b01_verifier_resolver_mismatch_rejected():
    with pytest.raises(AuthError):
        verify_certificate(base_config(), raw(resolver="OTHER"), verifier_id="ver:R", verifier_admitted=True)


def test_b02_duplicate_verified_certificate_id_rejected():
    k, _ = verified(base_config(), "Zero", cid="dup")
    with pytest.raises(AuthError):
        verify_certificate(k, raw("One", cid="dup"), verifier_id="ver:R", verifier_admitted=True)


def test_b03_invalid_grant_is_outside_aenv_and_cannot_mint():
    k = base_config()
    bad = Grant("bad", "missing", AuthorityKind.DET, frozenset({"commit_det"}),
                frozenset({"D"}), frozenset({"obj"}), "R", frozenset({"Zero"}), True)
    k = replace(k, authority=replace(k.authority, grants=k.authority.grants + (bad,)))
    assert bad not in k.aenv()
    k, c = verified(k, "Zero")
    with pytest.raises(AuthError):
        mint_det(k, token_id="x", grant_id="bad", operation="commit_det", scope="D",
                 object_id="obj", candidate="Zero", certificate=c, state_ref="s0", resolver="R")


def test_b04_human_act_boundary_rejection():
    k = base_config(); k, nc = verified(k, "U", cid="nc", nonclosure=True)
    with pytest.raises(AuthError): admit_human_act(k, human_act(k, "commit_sov_u", "U", nc), boundary_admitted=False)


def test_b05_human_act_stale_and_duplicate_admission_rejected():
    k = base_config(); k, nc = verified(k, "U", cid="nc", nonclosure=True)
    stale = replace(human_act(k, "commit_sov_u", "U", nc), authority_epoch=99)
    with pytest.raises(AuthError): admit_human_act(k, stale, boundary_admitted=True)
    act = human_act(k, "commit_sov_u", "U", nc); k = admit_human_act(k, act, boundary_admitted=True)
    with pytest.raises(AuthError): admit_human_act(k, act, boundary_admitted=True)


def test_b06_human_act_missing_prior_for_resolution_rejected():
    k = base_config(); k, c = verified(k, "Zero")
    act = human_act(k, "resolve_sov_u", "Zero", c, prior=None)
    with pytest.raises(AuthError): admit_human_act(k, act, boundary_admitted=True)


def test_b07_governance_boundary_stale_replay_and_mismatch_rejected():
    k = base_config()
    act = GovernanceAuthorizationAct("ga", "g-gov", "admin", "grant_add", "AUTH", "authority", "s0", 1, 1)
    with pytest.raises(AuthError): admit_governance_act(k, act, boundary_admitted=False)
    with pytest.raises(AuthError): admit_governance_act(k, replace(act, authority_epoch=9), boundary_admitted=True)
    k = admit_governance_act(k, act, boundary_admitted=True)
    with pytest.raises(AuthError): admit_governance_act(k, act, boundary_admitted=True)
    bad_principal = GovernanceAuthorizationAct("gb", "g-gov", "other", "grant_add", "AUTH", "authority", "s0", 1, 1)
    with pytest.raises(AuthError): admit_governance_act(base_config(), bad_principal, boundary_admitted=True)


def test_b08_governance_act_outside_grant_rejected():
    k = base_config()
    act = GovernanceAuthorizationAct("ga", "g-gov", "admin", "forbidden", "AUTH", "authority", "s0", 1, 1)
    with pytest.raises(AuthError): admit_governance_act(k, act, boundary_admitted=True)


def test_b09_mint_kind_escalation_and_duplicate_token_id_rejected():
    k = base_config(); k, c = verified(k, "Zero")
    # human mint cannot use det grant
    fake_act = HumanAuthorizationAct("x", "g-det", "svc", "commit_det", "D", "obj", "Zero", c.certificate_id, "s0", "R", None, 1, 1)
    kfake = replace(k, human_acts=(fake_act,))
    with pytest.raises(AuthError):
        mint_human(kfake, token_id="h", grant_id="g-det", act_id="x", operation="commit_det",
                   scope="D", object_id="obj", candidate="Zero", certificate=c, state_ref="s0", resolver="R")
    k, t = mint_det(k, token_id="dup", grant_id="g-det", operation="commit_det", scope="D",
                    object_id="obj", candidate="Zero", certificate=c, state_ref="s0", resolver="R")
    with pytest.raises(AuthError):
        mint_det(k, token_id="dup", grant_id="g-det", operation="commit_det", scope="D",
                 object_id="obj", candidate="Zero", certificate=c, state_ref="s0", resolver="R")


def test_b10_governance_mint_act_binding_mismatch_rejected():
    k = base_config()
    act = GovernanceAuthorizationAct("ga", "g-gov", "admin", "grant_add", "AUTH", "authority", "s0", 1, 1)
    k = admit_governance_act(k, act, boundary_admitted=True)
    with pytest.raises(AuthError):
        mint_governance(k, token_id="g", grant_id="g-gov", act_id="ga", operation="bind_principal",
                        scope="AUTH", object_id="authority", state_ref="s0")


def test_b11_consumed_token_cannot_be_reused():
    k, t, c = det_token(base_config())
    k, _ = commit_det(k, token=t, use=UseContext("svc", "runtime", "commit_det", "D", "obj", "s0", True),
                      certificate=c, candidate="Zero")
    with pytest.raises(AuthError):
        commit_det(k, token=t, use=UseContext("svc", "runtime", "commit_det", "D", "obj", "s0", True),
                   certificate=c, candidate="Zero")


def test_b12_commit_det_requires_det_commit_operation():
    k = base_config(); k, c = verified(k, "Zero")
    # forged type is rejected before use even if not stored
    t = DetToken("x", "g-det", "svc", "other", "D", "obj", "Zero", c.certificate_id, "s0", "R", None, 1, 1)
    with pytest.raises(AuthError):
        commit_det(k, token=t, use=UseContext("svc", "runtime", "other", "D", "obj", "s0", True),
                   certificate=c, candidate="Zero")


def test_b13_sovereign_u_authorization_requires_nonclosure_basis():
    k = base_config(); k, c = verified(k, "U", cid="u")
    act = human_act(k, "commit_sov_u", "U", c)
    with pytest.raises(AuthError):
        admit_human_act(k, act, boundary_admitted=True)


def test_b14_resolution_rejects_non_u_prior_and_wrong_reference_or_candidate():
    k, prior = human_u_committed()
    k, c = verified(k, "Zero", cid="r", state="s1")
    act = human_act(k, "resolve_sov_u", "Zero", c, act_id="ar", state="s1", prior=prior.decision_id)
    k = admit_human_act(k, act, boundary_admitted=True)
    k, h = mint_human(k, token_id="hr", grant_id="g-human-r", act_id="ar", operation="resolve_sov_u",
                      scope="D", object_id="obj", candidate="Zero", certificate=c, state_ref="s1",
                      resolver="R", prior_decision_ref=prior.decision_id)
    with pytest.raises(AuthError):
        resolve_sovereign_u(k, prior=replace(prior, value="Zero"), token=h,
            use=UseContext("alice", "runtime", "resolve_sov_u", "D", "obj", "s1", True),
            certificate=c, candidate="Zero")
    with pytest.raises(AuthError):
        resolve_sovereign_u(k, prior=prior, token=replace(h, prior_decision_ref="wrong"),
            use=UseContext("alice", "runtime", "resolve_sov_u", "D", "obj", "s1", True),
            certificate=c, candidate="Zero")
    with pytest.raises(AuthError):
        resolve_sovereign_u(k, prior=prior, token=h,
            use=UseContext("alice", "runtime", "resolve_sov_u", "D", "obj", "s1", True),
            certificate=c, candidate="One")


def test_b15_constitution_revision_version_and_grant_compatibility_checked():
    k = base_config(); k, gt = governance_token(k, token_id="gcx", operation="constitution_revision")
    with pytest.raises(AuthError):
        constitution_revision(k, token=gt,
            use=UseContext("admin", "runtime", "constitution_revision", "AUTH", "authority", "s0", True),
            new_constitution=replace(k.constitution, version=3))
    no_r = Constitution(2, k.constitution.roles, ())
    with pytest.raises(AuthError):
        constitution_revision(k, token=gt,
            use=UseContext("admin", "runtime", "constitution_revision", "AUTH", "authority", "s0", True),
            new_constitution=no_r)


def test_b16_enabled_authority_principal_filter():
    k, _ = verified(base_config(), "Zero")
    assert enabled_authority(k, candidate="Zero", state_ref="s0", resolver="R", principal="nobody") == frozenset()


def test_ax11_nonclosure_certificate_must_target_u():
    with pytest.raises(AuthError):
        verify_certificate(base_config(), raw("Zero", nonclosure=True), verifier_id="ver:NC", verifier_admitted=True)


def test_ax12_human_u_act_requires_nonclosure_certificate_before_mint():
    k = base_config(); k, c = verified(k, "U", cid="u-ordinary")
    act = human_act(k, "commit_sov_u", "U", c)
    with pytest.raises(AuthError): admit_human_act(k, act, boundary_admitted=True)


def test_ax13_ienabled_sov_u_requires_certified_nonclosure():
    k = base_config(); k, _ = verified(k, "U", cid="u-ordinary")
    assert enabled_authority(k, candidate="U", state_ref="s0", resolver="R", principal="alice") == frozenset()
    k, _ = verified(k, "U", cid="u-nc", nonclosure=True)
    assert ("g-human-u", "commit_sov_u", "D", "obj") in enabled_authority(
        k, candidate="U", state_ref="s0", resolver="R", principal="alice"
    )


def test_ax14_wf_auth_rejects_history_cache_divergence():
    k = base_config(); k, nc = verified(k, "U", cid="nc", nonclosure=True)
    act = human_act(k, "commit_sov_u", "U", nc); k = admit_human_act(k, act, boundary_admitted=True)
    assert wf_auth(k)
    bad = replace(k, human_acts=())
    assert not wf_auth(bad)
