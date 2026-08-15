#!/usr/bin/env python3
"""Reference implementation for finite traceable-learning examples (v0.4).

The program illustrates and regression-tests the article's finite definitions. It is
not a proof oracle and does not replace domain-specific validation of the cumulative
trajectory or independent auditing of operator implementations.
"""
from __future__ import annotations
import argparse, hashlib, json, sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Iterable, List, Mapping, Sequence, Set, Tuple

TYPES=("X","R","Lambda"); VALID_TRI={"0","1","U"}; RECORD_KINDS={"Add","Withdraw","ExecReason","ExecComp","Prov"}
class CheckError(Exception): pass
def require(c,m):
    if not c: raise CheckError(m)
def canonical_digest(obj):
    raw=json.dumps(obj,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()
def element_key(e):
    require(isinstance(e,Mapping),"knowledge element must be an object"); t=e.get("type"); i=e.get("id")
    require(t in TYPES,f"invalid knowledge type: {t!r}"); require(isinstance(i,str) and i,"knowledge element id must be non-empty")
    return t,i
def knowledge_set(k):
    require(isinstance(k,Mapping),"knowledge state must be an object"); out=set()
    for t in TYPES:
        vals=k.get(t); require(isinstance(vals,list),f"knowledge state requires list field {t}")
        for i in vals:
            require(isinstance(i,str) and i,f"knowledge id in {t} must be a string"); require((t,i) not in out,f"duplicate knowledge element {(t,i)}"); out.add((t,i))
    return out
def state_from_set(s): return {t:sorted(i for tt,i in s if tt==t) for t in TYPES}
@dataclass(frozen=True)
class RepEq:
    representatives: Mapping[Tuple[str,str],Tuple[str,str]]
    def reduce(self,x): return self.representatives.get(x,x)
    def reduce_set(self,xs): return {self.reduce(x) for x in xs}
def parse_rep_eq(ep):
    reps={}; seen=set(); classes=ep.get("representation_equivalence",[]); require(isinstance(classes,list),"representation_equivalence must be a list")
    for c in classes:
        t=c.get("type"); members=c.get("members"); require(t in TYPES,"invalid representation-equivalence type"); require(isinstance(members,list) and members,"empty equivalence class")
        rep=(t,members[0])
        for m in members:
            require(isinstance(m,str) and m,"equivalence member must be string"); k=(t,m); require(k not in seen,f"overlapping equivalence class at {k}"); seen.add(k); reps[k]=rep
    return RepEq(reps)
def validate_foundation(ep):
    f=ep.get("foundation"); require(isinstance(f,Mapping),"foundation must be a content-addressed object")
    require(isinstance(f.get("id"),str) and f["id"],"foundation id required"); desc=f.get("descriptor"); digest=f.get("sha256")
    require(isinstance(desc,Mapping),"foundation descriptor required"); require(isinstance(digest,str) and len(digest)==64,"foundation sha256 required")
    require(canonical_digest(desc)==digest,"foundation digest does not match canonical descriptor"); return digest
def validate_operator_table(op_id,op):
    arity=op.get("arity"); kind=op.get("kind"); table=op.get("table")
    require(isinstance(arity,int) and arity>=0,f"operator {op_id}: bad arity"); require(kind in {"internal","acquisition","composition","rectification"},f"operator {op_id}: bad kind")
    require(isinstance(table,list) and table,f"operator {op_id}: finite exact table required"); seen={}
    for row in table:
        ins=row.get("inputs"); out=row.get("output"); require(isinstance(ins,list) and len(ins)==arity,f"operator {op_id}: wrong arity"); require(all(isinstance(x,str) for x in ins) and isinstance(out,str),f"operator {op_id}: string table values required")
        k=tuple(ins); require(k not in seen or seen[k]==out,f"operator {op_id}: nondeterministic table at {k}"); seen[k]=out
def eval_operator(op_id,op,inputs):
    for row in op["table"]:
        if row["inputs"]==list(inputs): return row["output"]
    raise CheckError(f"operator {op_id}: inputs outside declared finite table")
def validate_vectors(ep):
    lv=ep.get("local_vectors")
    if lv is None: return
    for k in ("initial","final"):
        v=lv.get(k); require(isinstance(v,list) and v,f"local_vectors.{k} required"); require(set(v)<=VALID_TRI,f"local_vectors.{k}: invalid ternary value")
    require(len(lv["initial"])==len(lv["final"]),"endpoint vector lengths differ"); n=len(lv["initial"]); b=int(n**0.5); require(b>=3 and b*b==n,f"vector length {n} is not b^2, b>=3")
def validate_execution(ex,operators):
    eid=ex.get("id"); opid=ex.get("operator"); ins=ex.get("inputs"); out=ex.get("output")
    require(isinstance(eid,str) and eid,"execution id required"); require(opid in operators,f"execution {eid}: undeclared operator"); require(isinstance(ins,list),f"execution {eid}: inputs must be list")
    require(out==eval_operator(opid,operators[opid],ins),f"execution {eid}: output does not replay exactly")
def validate_witness(wid,w,operators,execs,prior_state,admitted_inputs,target):
    nodes_list=w.get("nodes"); root=w.get("root"); require(isinstance(nodes_list,list) and nodes_list,"witness nodes required"); nodes={n.get("id"):n for n in nodes_list}; require(root in nodes,"witness root missing")
    values={}; visiting=set(); done=set(); composition=set(); internal=False
    def visit(nid):
        nonlocal internal
        require(nid in nodes,f"witness {wid}: missing node {nid}")
        if nid in done: return
        require(nid not in visiting,f"witness {wid}: cycle at {nid}"); visiting.add(nid); n=nodes[nid]
        if n.get("kind")=="leaf":
            val=n.get("value"); src=n.get("source"); require(isinstance(val,str) and src in {"prior","external"},f"witness {wid}: invalid leaf")
            if src=="external": require(val in admitted_inputs,f"witness {wid}: unadmitted external leaf {val}")
            else:
                require(":" in val,f"witness {wid}: prior leaf must be TYPE:id"); t,i=val.split(":",1); require((t,i) in prior_state,f"witness {wid}: prior leaf {(t,i)} not active")
            values[nid]=val
        elif n.get("kind")=="op":
            for p in n.get("inputs",[]): visit(p)
            opid=n.get("operator"); require(opid in operators,f"witness {wid}: undeclared operator {opid}"); ins=[values[p] for p in n["inputs"]]; out=eval_operator(opid,operators[opid],ins); require(n.get("output")==out,f"witness {wid}: output mismatch")
            eid=n.get("execution_id"); require(eid in execs,f"witness {wid}: operator node requires recorded execution"); ex=execs[eid]; require(ex["operator"]==opid and ex["inputs"]==ins and ex["output"]==out,f"witness {wid}: execution record mismatch")
            values[nid]=out
            if operators[opid]["kind"]=="composition": composition.add(eid)
            if operators[opid]["kind"]=="internal": internal=True
        else: raise CheckError(f"witness {wid}: invalid node kind")
        visiting.remove(nid); done.add(nid)
    visit(root); require(done==set(nodes),f"witness {wid}: decorative/unreachable nodes present"); require(values[root]==f"{target[0]}:{target[1]}",f"witness {wid}: root != target")
    require(any(n.get("kind")=="leaf" and n.get("id")!=root for n in nodes.values()),f"witness {wid}: no antecedent leaf")
    return {"composition_executions":sorted(composition),"has_internal_reasoning":internal}
def validate_support_policy(ep,foundation_digest,execs,witnesses,admitted):
    p=ep.get("support_policy"); require(isinstance(p,Mapping),"support_policy required"); require(p.get("fixed_before_verdict") is True,"support policy must be fixed before verdict")
    require(p.get("foundation_sha256")==foundation_digest,"support policy not bound to episode foundation")
    require(set(p.get("executions",[]))==set(execs),"support policy execution universe mismatch"); require(set(p.get("witnesses",[]))==set(witnesses),"support policy witness universe mismatch"); require(set(p.get("admitted_inputs",[]))==admitted,"support policy input universe mismatch")
def check_episode(ep):
    for f in ("id","domain","subject","foundation","initial","final","history_before_episode","ledger","operators","witnesses","support_policy"): require(f in ep,f"missing required field {f}")
    foundation_digest=validate_foundation(ep); validate_vectors(ep); rep=parse_rep_eq(ep)
    current=knowledge_set(ep["initial"]); target_final=knowledge_set(ep["final"])
    hist_items=ep["history_before_episode"]; require(isinstance(hist_items,list),"history_before_episode must be list"); history=rep.reduce_set(element_key(x) for x in hist_items)
    require(rep.reduce_set(current)<=history,"prior history must include every initially active class")
    admitted=set(ep.get("admitted_inputs",[])); require(all(isinstance(x,str) and x for x in admitted),"admitted_inputs invalid")
    operators=ep["operators"]; require(isinstance(operators,Mapping),"operators must be object")
    for oid,op in operators.items(): validate_operator_table(oid,op)
    exec_list=ep.get("executions",[]); require(isinstance(exec_list,list),"executions must be list"); execs={}
    for ex in exec_list:
        validate_execution(ex,operators); require(ex["id"] not in execs,"duplicate execution id"); execs[ex["id"]]=ex
    witnesses=ep["witnesses"]; require(isinstance(witnesses,Mapping),"witnesses must be object"); validate_support_policy(ep,foundation_digest,execs,witnesses,admitted)
    ledger=ep["ledger"]; require(isinstance(ledger,list),"ledger must be list"); traj_refs=set(ep.get("trajectory_refs",[])); seen=set(); last=-1; changes=0; inc=[]; reasoning=False; comp_exec=set(); valid_info={}; target_ws={}
    witness_by_record={}
    for wid,w in witnesses.items():
        rid=w.get("incorporation_record"); require(isinstance(rid,str) and rid,"witness incorporation_record required"); witness_by_record.setdefault(rid,[]).append(wid)
    for rec in ledger:
        rid=rec.get("id"); kind=rec.get("kind"); ro=rec.get("registration_ordinal"); tr=rec.get("trajectory_ref")
        require(isinstance(rid,str) and rid and rid not in seen,"unique ledger id required"); seen.add(rid); require(kind in RECORD_KINDS,f"ledger {rid}: invalid kind {kind}"); require(isinstance(ro,int) and ro>=last,f"ledger {rid}: nonmonotone ordinal"); last=ro; require(tr in traj_refs,f"ledger {rid}: undeclared trajectory reference")
        before=rep.reduce_set(current)
        if kind=="Add":
            t=rec.get("type"); z=rec.get("target"); require(t in TYPES and isinstance(z,str) and z,f"ledger {rid}: typed target required"); x=(t,z); next_state=set(current); next_state.add(x); after=rep.reduce_set(next_state); dplus=after-before; dminus=before-after; current=next_state
            if dplus or dminus: changes+=1
            all_ws=sorted(witness_by_record.get(rid,[])); require(sorted(rec.get("support",[]))==all_ws,f"ledger {rid}: support list must enumerate all witnesses")
            rx=rep.reduce(x)
            related=[]
            if rx in dplus:
                for wid in all_ws:
                    wt=element_key(witnesses[wid].get("target",{})); require(rep.reduce(wt)==rx,f"witness {wid}: target does not match incorporation")
                    info=validate_witness(wid,witnesses[wid],operators,execs,set(current-{x}) if x not in (current-{x}) else set(current),admitted,x)
                    valid_info[wid]=info; related.append(wid); comp_exec.update(info["composition_executions"]); reasoning=reasoning or info["has_internal_reasoning"]
                if related:
                    target_ws[(rid,rx)]=related
                    if rx not in history: inc.append(rx)
            history.add(rx)
        elif kind=="Withdraw":
            t=rec.get("type"); z=rec.get("target"); x=(t,z); require(t in TYPES and isinstance(z,str) and z,"typed target required"); require(x in current,f"ledger {rid}: withdraw absent {x}"); current=set(current); current.remove(x); after=rep.reduce_set(current); changes += int(bool(before-after or after-before))
        elif kind in {"ExecReason","ExecComp"}:
            eid=rec.get("execution_id"); require(eid in execs,f"ledger {rid}: missing execution {eid}"); k=operators[execs[eid]["operator"]]["kind"]
            require((kind=="ExecReason" and k=="internal") or (kind=="ExecComp" and k=="composition"),f"ledger {rid}: execution kind mismatch")
            reasoning = reasoning or kind=="ExecReason"
            if kind=="ExecComp": comp_exec.add(eid)
        elif kind=="Prov": pass
    require(set(witness_by_record)<=seen,"witness references missing ledger record"); require(current==target_final,f"ledger replay final mismatch: {state_from_set(current)} != {state_from_set(target_final)}")
    foundation_preserved=True
    for tr in ep.get("machine_transitions",[]):
        require(tr.get("kind")=="machine","machine transition kind required"); require(tr.get("from_foundation_sha256")==foundation_digest,"machine transition source foundation mismatch")
        if tr.get("to_foundation_sha256")!=foundation_digest: raise CheckError(f"machine foundation rewrite forbidden: digest {foundation_digest} -> {tr.get('to_foundation_sha256')}")
    evolution=changes>0; incrementals=sorted(set(inc)); learn=evolution and bool(incrementals)
    comp_support={}; comp_essential={}
    for (rid,target),ws in target_ws.items():
        sets=[set(valid_info[w]["composition_executions"]) for w in ws]; union=set().union(*sets) if sets else set(); inter=set.intersection(*sets) if sets else set(); k=f"{target[0]}:{target[1]}"
        if union: comp_support[k]=sorted(union)
        if inter: comp_essential[k]=sorted(inter)
    q=ep.get("operational_query"); verdict=None
    if q is not None:
        if not q.get("admissible",False): verdict="ILL_FORMED_OR_OUT_OF_DOMAIN"
        else:
            scope=q.get("access_scope",[]); done=q.get("completed_access",[]); require(set(scope)==set(done),"operational verdict requires exhausted access scope")
            req=q.get("required_record_ids",[]); ret=q.get("retained_record_ids",[]); verdict=("LEARN" if learn else "NO_LEARN") if set(req)==set(ret) else "U"
    return {"episode":ep["id"],"well_formed":True,"evolution":evolution,"incrementals":[f"{t}:{i}" for t,i in incrementals],"learn":learn,"reasoning_executed":reasoning,"composition_executed":sorted(comp_exec),"composition_support":comp_support,"composition_record_essential":comp_essential,"foundation_preserved":foundation_preserved,"operational_verdict":verdict}
def check_expected(actual,expected):
    for k,v in expected.items(): require(k in actual and actual[k]==v,f"expected {k}={v!r}, got {actual.get(k)!r}")
def process(path,verify=True):
    try:
        payload=json.loads(path.read_text()); ep=payload.get("episode",payload); expected_error=payload.get("expected_error") if verify else None
        try: actual=check_episode(ep)
        except CheckError as exc:
            if expected_error is not None:
                require(expected_error in str(exc),f"expected error containing {expected_error!r}, got {str(exc)!r}"); return True,{"episode":ep.get("id"),"well_formed":False,"rejected_as_expected":True,"error":str(exc)}
            raise
        if expected_error is not None: raise CheckError(f"expected rejection containing {expected_error!r}, but episode accepted")
        if verify and "expected" in payload: check_expected(actual,payload["expected"])
        return True,actual
    except (OSError,json.JSONDecodeError,CheckError) as exc: return False,{"file":str(path),"well_formed":False,"error":str(exc)}
def main(argv=None):
    p=argparse.ArgumentParser(); p.add_argument("files",nargs="+",type=Path); p.add_argument("--no-expected",action="store_true"); p.add_argument("--json",action="store_true"); a=p.parse_args(argv); fails=0
    for path in a.files:
        ok,res=process(path,not a.no_expected); fails+=0 if ok else 1
        if a.json: print(json.dumps(res,ensure_ascii=False,sort_keys=True))
        else: print(f"[{'PASS' if ok else 'FAIL'}] {path}\n"+json.dumps(res,ensure_ascii=False,indent=2,sort_keys=True))
    return 1 if fails else 0
if __name__=="__main__": sys.exit(main())
