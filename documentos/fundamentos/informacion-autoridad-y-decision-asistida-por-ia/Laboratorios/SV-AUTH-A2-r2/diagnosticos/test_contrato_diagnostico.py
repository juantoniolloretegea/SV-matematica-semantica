"""Contrato diagnóstico suplementario para SV-AUTH A.2 r2.

Este módulo NO modifica el artefacto r2 citado en la publicación ni altera
las 78 pruebas que sustentan las cifras del artículo. Su único objetivo es
cerrar una capa adicional de auditabilidad: comprobar que casos negativos
representativos no sólo son rechazados, sino que devuelven el código de
diagnóstico previsto.

Las pruebas se ejecutan contra el código extraído del ZIP congelado. Por
ello cualquier cambio del artefacto debe detectarse antes mediante su
SHA-256, no mediante este módulo.
"""
from __future__ import annotations

from dataclasses import replace
import inspect
import re

import pytest

from sv_motor.security.authority import *
import sv_motor.security.authority_runtime as authority_runtime


CODIGOS_EMITIDOS_R2 = {
    "E601", "E602", "E603", "E604", "E605", "E606", "E607", "E608",
    "E609", "E610", "E611", "E612", "E613", "E615", "E617",
}


def base_config() -> Configuration:
    """Configuración mínima bien formada equivalente a la batería r2."""
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
        (VerifierSpec("ver:R", "R", False), VerifierSpec("ver:NC", "R", True)),
    )
    return Configuration(
        constitution,
        (),
        AuthorityState(1, grants, bindings),
        semantic_registry=(SemanticEnvironment(AUTH_SEM_ENV),),
    )


def raw(candidate: str = "Zero", *, cid: str = "c0", state: str = "s0",
        resolver: str = "R", nonclosure: bool = False) -> RawCertificate:
    return RawCertificate(cid, candidate, state, resolver, nonclosure)


def verified(k: Configuration, candidate: str = "Zero", *, cid: str = "c0",
             state: str = "s0", nonclosure: bool = False):
    verifier = "ver:NC" if nonclosure else "ver:R"
    return verify_certificate(
        k,
        raw(candidate, cid=cid, state=state, nonclosure=nonclosure),
        verifier_id=verifier,
        verifier_admitted=True,
    )


def det_token(k: Configuration, candidate: str = "Zero"):
    k, cert = verified(k, candidate)
    k, token = mint_det(
        k,
        token_id="t",
        grant_id="g-det",
        operation="commit_det",
        scope="D",
        object_id="obj",
        candidate=candidate,
        certificate=cert,
        state_ref="s0",
        resolver="R",
    )
    return k, token, cert


def human_act(k: Configuration, certificate: VerifiedCertificate,
              *, act_id: str = "a1") -> HumanAuthorizationAct:
    return HumanAuthorizationAct(
        act_id,
        "g-human-u",
        "alice",
        "commit_sov_u",
        "D",
        "obj",
        "U",
        certificate.certificate_id,
        "s0",
        "R",
        None,
        k.constitution.version,
        k.authority.epoch,
    )


def governance_token(k: Configuration, *, token_id: str, operation: str):
    act = GovernanceAuthorizationAct(
        f"act:{token_id}",
        "g-gov",
        "admin",
        operation,
        "AUTH",
        "authority",
        "s0",
        k.constitution.version,
        k.authority.epoch,
    )
    k = admit_governance_act(k, act, boundary_admitted=True)
    return mint_governance(
        k,
        token_id=token_id,
        grant_id="g-gov",
        act_id=act.act_id,
        operation=operation,
        scope="AUTH",
        object_id="authority",
        state_ref="s0",
    )


def expect_code(code: str, fn) -> None:
    """Exige AuthError y comprueba su código; evita un rechazo por motivo distinto."""
    with pytest.raises(AuthError) as exc:
        fn()
    assert str(exc.value).startswith(code), str(exc.value)


def test_catalogo_activo_coincide_con_runtime_r2():
    """El catálogo activo debe coincidir con los códigos realmente emitidos por r2."""
    source = inspect.getsource(authority_runtime)
    emitted = set(re.findall(r'AuthError\("(E\d{3})', source))
    assert emitted == CODIGOS_EMITIDOS_R2


def test_e601_coercion_informativa():
    expect_code("E601", lambda: info_add(
        base_config(),
        Grant("x", "svc", AuthorityKind.DET, frozenset(), frozenset(), frozenset()),
    ))


def test_e602_mutacion_de_grant_sin_operacion_correcta():
    k, token = governance_token(base_config(), token_id="g", operation="bind_principal")
    new = Grant("x", "svc", AuthorityKind.DET, frozenset({"commit_det"}),
                frozenset({"D"}), frozenset({"obj"}), "R", frozenset({"Zero"}), True)
    expect_code("E602", lambda: governance_add_grant(
        k,
        token=token,
        use=UseContext("admin", "runtime", "bind_principal", "AUTH", "authority", "s0", True),
        grant=new,
    ))


def test_e603_escalada_de_clase_de_token():
    k, nc = verified(base_config(), "U", cid="nc", nonclosure=True)
    expect_code("E603", lambda: mint_det(
        k,
        token_id="x",
        grant_id="g-human-u",
        operation="commit_sov_u",
        scope="D",
        object_id="obj",
        candidate="U",
        certificate=nc,
        state_ref="s0",
        resolver="R",
    ))


def test_e604_binding_contextual_incorrecto():
    k, cert = verified(base_config())
    expect_code("E604", lambda: mint_det(
        k,
        token_id="x",
        grant_id="g-det",
        operation="commit_det",
        scope="OTRO",
        object_id="obj",
        candidate="Zero",
        certificate=cert,
        state_ref="s0",
        resolver="R",
    ))


def test_e605_entorno_de_autoridad_obsoleto():
    k, token, cert = det_token(base_config())
    stale = replace(k, constitution=replace(k.constitution, version=2))
    expect_code("E605", lambda: commit_det(
        stale,
        token=token,
        use=UseContext("svc", "runtime", "commit_det", "D", "obj", "s0", True),
        certificate=cert,
        candidate="Zero",
    ))


def test_e606_repeticion_de_token():
    k, _, cert = det_token(base_config())
    expect_code("E606", lambda: mint_det(
        k,
        token_id="t",
        grant_id="g-det",
        operation="commit_det",
        scope="D",
        object_id="obj",
        candidate="Zero",
        certificate=cert,
        state_ref="s0",
        resolver="R",
    ))


def test_e607_base_no_verificada():
    expect_code("E607", lambda: verify_certificate(
        base_config(), raw(), verifier_id="ver:R", verifier_admitted=False
    ))


def test_e608_acto_humano_no_admitido():
    k, nc = verified(base_config(), "U", cid="nc", nonclosure=True)
    act = human_act(k, nc)
    expect_code("E608", lambda: admit_human_act(k, act, boundary_admitted=False))


def test_e609_commit_soberano_con_token_determinista():
    k, token, _ = det_token(base_config())
    k, nc = verified(k, "U", cid="nc", nonclosure=True)
    expect_code("E609", lambda: commit_sovereign_u(
        k,
        token=token,  # type: ignore[arg-type]
        use=UseContext("svc", "runtime", "commit_det", "D", "obj", "s0", True),
        certificate=nc,
    ))


def test_e610_resolucion_soberana_sobre_antecedente_no_u():
    prior = SovereignDecision("p", "alice", "obj", "Zero", "basis", "s0")
    expect_code("E610", lambda: resolve_sovereign_u(
        base_config(),
        prior=prior,
        token=None,  # type: ignore[arg-type]
        use=None,  # type: ignore[arg-type]
        certificate=None,  # type: ignore[arg-type]
        candidate="Zero",
    ))


def test_e611_repeticion_de_acto_de_autorizacion():
    k, nc = verified(base_config(), "U", cid="nc", nonclosure=True)
    act = human_act(k, nc)
    k = admit_human_act(k, act, boundary_admitted=True)
    expect_code("E611", lambda: admit_human_act(k, act, boundary_admitted=True))


def test_e612_deserializacion_no_crea_capacidad():
    expect_code("E612", lambda: deserialize_token({"token_id": "t"}))


def test_e613_importacion_no_crea_decision_soberana():
    expect_code("E613", lambda: deserialize_sovereign_decision({"value": "U"}))


def test_e615_derogacion_de_invariante_de_binding():
    k, token = governance_token(base_config(), token_id="g", operation="bind_principal")
    bad = PrincipalBinding("llm", AuthorityRole.HUMAN_SOVEREIGN, PrincipalClass.EXTERNAL)
    expect_code("E615", lambda: governance_bind_principal(
        k,
        token=token,
        use=UseContext("admin", "runtime", "bind_principal", "AUTH", "authority", "s0", True),
        binding=bad,
    ))


def test_e617_deriva_semantica_en_snapshot():
    k = base_config()
    bad = replace(k, history=(Record("r", "x", (), "entorno-inexistente"),))
    expect_code("E617", lambda: restore(bad, snapshot_admitted=True))
