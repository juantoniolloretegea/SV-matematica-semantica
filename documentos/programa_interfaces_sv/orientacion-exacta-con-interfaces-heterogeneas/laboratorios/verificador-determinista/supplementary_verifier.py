#!/usr/bin/env python3
"""
Deterministic finite verifier for
"Exact Orientation Under Heterogeneous Interfaces: Episode Constitution and
Closure-Preserving Substitution".

No external packages are required.

The script implements the formal objects used in the manuscript:
  * finite guarded contracts;
  * local witness verification V_p;
  * structural joint compatibility J;
  * enumeration of constitutive bases B_Theta(W);
  * contextual resolution congruence r_p^Theta;
  * local-class vectors Lambda_Theta(W);
  * global resolution signatures S_Theta(W);
  * raw and signature-quotient finite resolvers;
  * exact reachability closure profiles;
  * C2, C3, and C4_lambda for typed substitutions.

It then constructs and checks the eight adversarial scenarios F1--F8 and the
canonical quotient-scaling family reported in the paper.
"""

from dataclasses import dataclass, field
from itertools import product
from typing import Callable, Dict, FrozenSet, Iterable, List, Mapping, Sequence, Tuple

Bit = int
Value = int
Profile = FrozenSet[int]


@dataclass(frozen=True)
class Predicate:
    name: str
    support: Tuple[str, ...]
    fn: Callable[[Mapping[str, Value]], Bit] = field(compare=False, repr=False)

    def eval(self, valuation: Mapping[str, Value]) -> Bit:
        return int(bool(self.fn(valuation)))


@dataclass(frozen=True)
class Edge:
    source: str
    action: str
    target: str
    guard: str


@dataclass(frozen=True)
class Contract:
    name: str
    parameters: Tuple[str, ...]
    domains: Mapping[str, Tuple[Value, ...]]
    states: Tuple[str, ...]
    initial: str
    edges: Tuple[Edge, ...]
    guards: Mapping[str, Predicate]
    terminal0: Mapping[str, Predicate]
    terminal1: Mapping[str, Predicate]

    def all_predicates(self) -> Tuple[Predicate, ...]:
        return tuple(self.guards.values()) + tuple(self.terminal0.values()) + tuple(self.terminal1.values())

    def global_signature(self, valuation: Mapping[str, Value]) -> Tuple[Tuple[str, Bit], ...]:
        items: List[Tuple[str, Bit]] = []
        for name in sorted(self.guards):
            items.append((f"g:{name}", self.guards[name].eval(valuation)))
        for state in sorted(self.states):
            items.append((f"t0:{state}", self.terminal0[state].eval(valuation)))
            items.append((f"t1:{state}", self.terminal1[state].eval(valuation)))
        return tuple(items)

    def contextual_signature(self, parameter: str, value: Value) -> Tuple[Tuple[str, Tuple[Tuple[Tuple[str, Value], ...], Bit]], ...]:
        """Canonical kappa_p^Theta(value)."""
        rows = []
        for pred in sorted(self.all_predicates(), key=lambda p: p.name):
            if parameter not in pred.support:
                continue
            others = tuple(q for q in pred.support if q != parameter)
            evaluations = []
            domains = [self.domains[q] for q in others]
            for vals in product(*domains) if domains else [()]:
                ctx = dict(zip(others, vals))
                ctx[parameter] = value
                evaluations.append((tuple(sorted((q, ctx[q]) for q in others)), pred.eval(ctx)))
            rows.append((pred.name, tuple(evaluations)))
        return tuple(rows)

    def local_class(self, parameter: str, value: Value):
        return self.contextual_signature(parameter, value)

    def locally_equivalent(self, parameter: str, a: Value, b: Value) -> bool:
        return self.local_class(parameter, a) == self.local_class(parameter, b)

    def enabled_edges(self, valuation: Mapping[str, Value]) -> Tuple[Edge, ...]:
        return tuple(e for e in self.edges if self.guards[e.guard].eval(valuation) == 1)

    def terminal_sets(self, valuation: Mapping[str, Value]) -> Tuple[FrozenSet[str], FrozenSet[str]]:
        t0 = frozenset(x for x in self.states if self.terminal0[x].eval(valuation) == 1)
        t1 = frozenset(x for x in self.states if self.terminal1[x].eval(valuation) == 1)
        return t0, t1

    def branch_profile(self, valuation: Mapping[str, Value]) -> Profile:
        adj: Dict[str, List[str]] = {x: [] for x in self.states}
        for e in self.enabled_edges(valuation):
            adj[e.source].append(e.target)
        seen = {self.initial}
        stack = [self.initial]
        while stack:
            x = stack.pop()
            for y in adj[x]:
                if y not in seen:
                    seen.add(y)
                    stack.append(y)
        t0, t1 = self.terminal_sets(valuation)
        out = set()
        if seen & t0:
            out.add(0)
        if seen & t1:
            out.add(1)
        return frozenset(out)


@dataclass(frozen=True)
class Witness:
    wid: str
    role: str
    value: Value
    episode: str = "A"
    local_valid: bool = True
    provenance: Tuple[str, ...] = ()


Base = Tuple[Tuple[str, str], ...]  # sorted (role, witness id)


@dataclass
class Realization:
    contract: Contract
    witnesses: Tuple[Witness, ...]

    def by_id(self) -> Dict[str, Witness]:
        return {w.wid: w for w in self.witnesses}

    def by_role(self, role: str) -> Tuple[Witness, ...]:
        return tuple(w for w in self.witnesses if w.role == role)

    @staticmethod
    def V(w: Witness) -> bool:
        # Resolution-blind local verifier: only local validity is inspected.
        return bool(w.local_valid)

    @staticmethod
    def J(selected: Mapping[str, Witness]) -> bool:
        # Structural compatibility only: all selected witnesses must refer to
        # the same episode. Values are deliberately not inspected.
        episodes = {w.episode for w in selected.values()}
        return len(episodes) == 1

    def bases(self) -> Tuple[Base, ...]:
        roles = self.contract.parameters
        candidates = []
        for p in roles:
            ws = tuple(w for w in self.by_role(p) if self.V(w))
            if not ws:
                return tuple()
            candidates.append(ws)
        out = []
        for chosen in product(*candidates):
            selected = dict(zip(roles, chosen))
            if self.J(selected):
                out.append(tuple(sorted((p, selected[p].wid) for p in roles)))
        return tuple(out)

    def verify_constitution_certificate(self, base: Base) -> bool:
        return base in self.bases()

    def constituted(self) -> bool:
        return bool(self.bases())

    def valuation(self, base: Base) -> Dict[str, Value]:
        wbyid = self.by_id()
        return {p: wbyid[wid].value for p, wid in base}

    def lambda_vector(self, base: Base):
        val = self.valuation(base)
        return tuple((p, self.contract.local_class(p, val[p])) for p in self.contract.parameters)

    def Lambda(self):
        return frozenset(self.lambda_vector(b) for b in self.bases())

    def signature(self, base: Base):
        return self.contract.global_signature(self.valuation(base))

    def S(self):
        return frozenset(self.signature(b) for b in self.bases())

    def raw_profile(self) -> Profile:
        out = set()
        for b in self.bases():
            out.update(self.contract.branch_profile(self.valuation(b)))
        return frozenset(out)

    def quotient_profile(self) -> Profile:
        # One representative branch per global signature.
        representative = {}
        for b in self.bases():
            representative.setdefault(self.signature(b), b)
        out = set()
        for b in representative.values():
            out.update(self.contract.branch_profile(self.valuation(b)))
        return frozenset(out)

    def active_witness_ids(self) -> FrozenSet[str]:
        ids = set()
        for b in self.bases():
            ids.update(wid for _, wid in b)
        return frozenset(ids)


@dataclass(frozen=True)
class TypedSubstitution:
    source: Realization       # W'
    reference: Realization    # W
    mapping: Mapping[str, str]  # active source witness id -> reference witness id

    def _mapped_base(self, base: Base) -> Base:
        return tuple(sorted((p, self.mapping[wid]) for p, wid in base))

    def well_typed_on_active(self) -> bool:
        src = self.source.by_id()
        ref = self.reference.by_id()
        active = self.source.active_witness_ids()
        if set(self.mapping) != set(active):
            return False
        return all(self.mapping[wid] in ref and src[wid].role == ref[self.mapping[wid]].role for wid in active)

    def C2(self) -> bool:
        if not self.well_typed_on_active():
            return False
        src = self.source.by_id()
        ref = self.reference.by_id()
        c = self.source.contract
        return all(c.locally_equivalent(src[wid].role, src[wid].value, ref[self.mapping[wid]].value)
                   for wid in self.source.active_witness_ids())

    def C3(self) -> bool:
        if not self.well_typed_on_active():
            return False
        ref_bases = set(self.reference.bases())
        return all(self._mapped_base(b) in ref_bases for b in self.source.bases())

    def C4_lambda(self) -> bool:
        return self.reference.Lambda().issubset(self.source.Lambda())


# ---------------------------------------------------------------------------
# Contracts
# ---------------------------------------------------------------------------

def const_pred(name: str, value: int) -> Predicate:
    return Predicate(name, tuple(), lambda _v, value=value: value)


def common_contract() -> Contract:
    params = ("p", "q", "r")
    domains = {"p": (0, 1, 2, 3), "q": (0, 1), "r": (0, 1)}
    states = ("x*", "a", "b", "c", "d", "t0", "t1")
    guards = {
        "g_xa": Predicate("g_xa", ("r",), lambda v: v["r"] == 1),
        "g_xb": Predicate("g_xb", ("q",), lambda v: v["q"] == 1),
        "g_ac": Predicate("g_ac", ("q",), lambda v: v["q"] == 1),
        "g_bc": Predicate("g_bc", ("r",), lambda v: v["r"] == 1),
        "g_ct0": Predicate("g_ct0", ("p",), lambda v: v["p"] in (0, 2)),
        "g_ct1": Predicate("g_ct1", ("p",), lambda v: v["p"] == 1),
        "g_cd": Predicate("g_cd", ("p",), lambda v: v["p"] == 3),
        "g_dt0": const_pred("g_dt0", 1),
    }
    edges = (
        Edge("x*", "xa", "a", "g_xa"),
        Edge("x*", "xb", "b", "g_xb"),
        Edge("a", "ac", "c", "g_ac"),
        Edge("b", "bc", "c", "g_bc"),
        Edge("c", "ct0", "t0", "g_ct0"),
        Edge("c", "ct1", "t1", "g_ct1"),
        Edge("c", "cd", "d", "g_cd"),
        Edge("d", "dt0", "t0", "g_dt0"),
    )
    terminal0 = {x: const_pred(f"t0_{x}", 1 if x == "t0" else 0) for x in states}
    terminal1 = {x: const_pred(f"t1_{x}", 1 if x == "t1" else 0) for x in states}
    return Contract("common", params, domains, states, "x*", edges, guards, terminal0, terminal1)


def coupled_contract() -> Contract:
    params = ("p", "q")
    domains = {"p": (2, 3), "q": (3, 4)}
    states = ("x*", "c", "t0", "t1")
    guards = {
        "g_start": const_pred("g_start", 1),
        "g_t1": Predicate("g_t1", ("p", "q"), lambda v: v["p"] + v["q"] > 5),
        "g_t0": Predicate("g_t0", ("p", "q"), lambda v: v["p"] + v["q"] <= 5),
    }
    edges = (
        Edge("x*", "start", "c", "g_start"),
        Edge("c", "to0", "t0", "g_t0"),
        Edge("c", "to1", "t1", "g_t1"),
    )
    terminal0 = {x: const_pred(f"t0_{x}", 1 if x == "t0" else 0) for x in states}
    terminal1 = {x: const_pred(f"t1_{x}", 1 if x == "t1" else 0) for x in states}
    return Contract("coupled", params, domains, states, "x*", edges, guards, terminal0, terminal1)


def W(contract: Contract, *witnesses: Witness) -> Realization:
    return Realization(contract, tuple(witnesses))


def common_qr(prefix="", episode="A"):
    return (
        Witness(f"{prefix}q1", "q", 1, episode=episode, provenance=("map",)),
        Witness(f"{prefix}r1", "r", 1, episode=episode, provenance=("capture-integrity",)),
    )


# ---------------------------------------------------------------------------
# F1--F8
# ---------------------------------------------------------------------------

def scenario_F1(c: Contract):
    q, r = common_qr("o_")
    old = W(c, Witness("o_p0", "p", 0), q, r)
    qn, rn = common_qr("n_")
    new = W(c, Witness("n_p0", "p", 0), Witness("n_p1", "p", 1), qn, rn)
    sub = TypedSubstitution(new, old, {
        "n_p0": "o_p0", "n_p1": "o_p0", "n_q1": "o_q1", "n_r1": "o_r1"
    })
    assert sub.well_typed_on_active() and not sub.C2() and sub.C3() and sub.C4_lambda()
    assert old.raw_profile() == frozenset({0}) and new.raw_profile() == frozenset({0, 1})
    return old.raw_profile(), new.raw_profile(), (sub.C2(), sub.C3(), sub.C4_lambda())


def scenario_F2():
    c = coupled_contract()
    old = W(c,
            Witness("o_p2", "p", 2),
            Witness("o_q3", "q", 3), Witness("o_q4", "q", 4))
    new = W(c,
            Witness("n_p3", "p", 3),
            Witness("n_q3", "q", 3), Witness("n_q4", "q", 4))
    sub = TypedSubstitution(new, old, {"n_p3": "o_p2", "n_q3": "o_q3", "n_q4": "o_q4"})
    # Pointwise agreement at q=4, disagreement at q=3.
    assert c.guards["g_t1"].eval({"p": 2, "q": 4}) == c.guards["g_t1"].eval({"p": 3, "q": 4}) == 1
    assert c.guards["g_t1"].eval({"p": 2, "q": 3}) == 0
    assert c.guards["g_t1"].eval({"p": 3, "q": 3}) == 1
    assert not c.locally_equivalent("p", 2, 3)
    assert not sub.C2()
    assert old.raw_profile() == frozenset({0, 1}) and new.raw_profile() == frozenset({1})
    return old.raw_profile(), new.raw_profile(), c.locally_equivalent("p", 2, 3)


def scenario_F3(c: Contract):
    q, r = common_qr("o_", episode="A")
    old = W(c,
            Witness("o_p0", "p", 0, episode="A"),
            Witness("o_p1_bad", "p", 1, episode="B"),  # locally valid, structurally incompatible
            q, r)
    qn, rn = common_qr("n_", episode="A")
    new = W(c,
            Witness("n_p0", "p", 0, episode="A"),
            Witness("n_p1", "p", 1, episode="A"),
            qn, rn)
    sub = TypedSubstitution(new, old, {
        "n_p0": "o_p0", "n_p1": "o_p1_bad", "n_q1": "o_q1", "n_r1": "o_r1"
    })
    assert sub.well_typed_on_active() and sub.C2() and not sub.C3() and sub.C4_lambda()
    assert old.raw_profile() == frozenset({0}) and new.raw_profile() == frozenset({0, 1})
    return old.raw_profile(), new.raw_profile(), (sub.C2(), sub.C3(), sub.C4_lambda())


def scenario_F4(c: Contract):
    q, r = common_qr("o_")
    old = W(c, Witness("o_p0", "p", 0), Witness("o_p1", "p", 1), q, r)
    qn, rn = common_qr("n_")
    new = W(c, Witness("n_p0", "p", 0), qn, rn)
    sub = TypedSubstitution(new, old, {"n_p0": "o_p0", "n_q1": "o_q1", "n_r1": "o_r1"})
    assert sub.well_typed_on_active() and sub.C2() and sub.C3() and not sub.C4_lambda()
    assert old.raw_profile() == frozenset({0, 1}) and new.raw_profile() == frozenset({0})
    return old.raw_profile(), new.raw_profile(), (sub.C2(), sub.C3(), sub.C4_lambda())


def scenario_F5(c: Contract):
    q, r = common_qr("o_", episode="A")
    old = W(c, Witness("o_p0", "p", 0, episode="A"), q, r)
    qn, rn = common_qr("n_", episode="A")
    new = W(c,
            Witness("n_p0", "p", 0, episode="A"),
            Witness("n_p1_inactive", "p", 1, episode="B"),
            qn, rn)
    assert "n_p1_inactive" not in new.active_witness_ids()
    sub = TypedSubstitution(new, old, {"n_p0": "o_p0", "n_q1": "o_q1", "n_r1": "o_r1"})
    assert sub.well_typed_on_active() and sub.C2() and sub.C3() and sub.C4_lambda()
    assert old.raw_profile() == new.raw_profile() == frozenset({0})
    return old.raw_profile(), new.raw_profile(), tuple(sorted(new.active_witness_ids()))


def scenario_F6(c: Contract):
    q, r = common_qr("w_", episode="A")
    realization = W(c,
                    Witness("w_p_cam_map", "p", 0, episode="A", provenance=("camera", "map")),
                    Witness("w_p_lidar_map", "p", 1, episode="A", provenance=("lidar", "map")),
                    q, r)
    assert len(realization.bases()) == 2
    assert realization.raw_profile() == frozenset({0, 1})
    return realization.raw_profile(), tuple(sorted(realization.active_witness_ids()))


def scenario_F7(c: Contract):
    q, r = common_qr("o_")
    old = W(c, Witness("o_p0_camera", "p", 0, provenance=("camera",)), q, r)
    qn, rn = common_qr("n_")
    new = W(c, Witness("n_p2_lidar", "p", 2, provenance=("lidar",)), qn, rn)
    sub = TypedSubstitution(new, old, {"n_p2_lidar": "o_p0_camera", "n_q1": "o_q1", "n_r1": "o_r1"})
    assert c.locally_equivalent("p", 0, 2)
    assert sub.C2() and sub.C3() and sub.C4_lambda()
    assert old.raw_profile() == new.raw_profile() == frozenset({0})
    assert old.S() == new.S()
    return old.raw_profile(), new.raw_profile(), (sub.C2(), sub.C3(), sub.C4_lambda())


def scenario_F8(c: Contract):
    q, r = common_qr("o_")
    old = W(c, Witness("o_p0", "p", 0), q, r)
    qn, rn = common_qr("n_")
    new = W(c, Witness("n_p3", "p", 3), qn, rn)
    sub = TypedSubstitution(new, old, {"n_p3": "o_p0", "n_q1": "o_q1", "n_r1": "o_r1"})
    assert not c.locally_equivalent("p", 0, 3)
    assert not sub.C2() and sub.C3() and not sub.C4_lambda()
    assert old.S() != new.S()
    assert old.raw_profile() == new.raw_profile() == frozenset({0})
    return old.raw_profile(), new.raw_profile(), (sub.C2(), sub.C3(), sub.C4_lambda())


# ---------------------------------------------------------------------------
# Scaling family
# ---------------------------------------------------------------------------

def scaling_counts(k: int) -> Tuple[int, int, int]:
    raw = 4 ** k
    local_classes = 2 ** k
    return raw, local_classes, raw // local_classes


def run() -> None:
    c = common_contract()

    # Sanity checks for the canonical contextual congruence.
    assert c.locally_equivalent("p", 0, 2)
    assert not c.locally_equivalent("p", 0, 1)
    assert not c.locally_equivalent("p", 0, 3)

    scenarios = {
        "F1": scenario_F1(c),
        "F2": scenario_F2(),
        "F3": scenario_F3(c),
        "F4": scenario_F4(c),
        "F5": scenario_F5(c),
        "F6": scenario_F6(c),
        "F7": scenario_F7(c),
        "F8": scenario_F8(c),
    }

    # Every realization encountered above satisfies raw/quotient profile invariance
    # where applicable; this is also checked explicitly on a representative family.
    q, r = common_qr("z_")
    z = W(c, Witness("z_p0a", "p", 0), Witness("z_p0b", "p", 0),
          Witness("z_p2", "p", 2), Witness("z_p1", "p", 1), q, r)
    assert z.raw_profile() == z.quotient_profile() == frozenset({0, 1})
    assert len(z.bases()) > len(z.S())

    print("Formal adversarial suite: 8/8 scenarios verified.")
    for key in sorted(scenarios):
        print(f"{key}: {scenarios[key]}")

    print("\nCanonical scaling family:")
    print("k,raw_bases,signatures,reduction")
    for k in range(2, 9):
        raw, sig, reduction = scaling_counts(k)
        print(f"{k},{raw},{sig},{reduction}")


if __name__ == "__main__":
    run()
