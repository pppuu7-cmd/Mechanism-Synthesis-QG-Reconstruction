#!/usr/bin/env python3
"""Aggregate JSON outputs from the parallel MSQGR structural research campaign."""
from __future__ import annotations
import argparse, json
from pathlib import Path

def read_named(root,name):
    hits=list(root.rglob(name));return json.loads(hits[0].read_text(encoding="utf-8")) if hits else None

def main():
    ap=argparse.ArgumentParser();ap.add_argument("--input",default="parallel-results");ap.add_argument("--output",default="combined-results/combined_verdict.json");ap.add_argument("--markdown",default="combined-results/summary.md");args=ap.parse_args();root=Path(args.input)
    char=read_named(root,"causal_character_scan.json");rank=read_named(root,"constraint_rank.json");trans=read_named(root,"transfer_semigroup.json");toller=read_named(root,"toller_rg_closure_toy.json");novelty=read_named(root,"novelty_overlap.json")
    carc=read_named(root,"causal_rg_commutator.json");cci=read_named(root,"causal_embedding_consistency.json");multi=read_named(root,"carc_multiscale_scan.json");codim=read_named(root,"carc_codimension.json");f9=read_named(root,"f9_gate.json")
    blockers=[];positive=[]
    if char: (blockers if char.get("verdict")=="UNDERDETERMINED_PHASE_FAMILY" else positive).append("Naive scalar multiplicative branch leaves a free phase parameter; retained only as a negative control.")
    if rank: (blockers if rank.get("nullity",0)>0 else positive).append(f"Scalar negative-control rank={rank.get('rank')}, nullity={rank.get('nullity')}.")
    if trans: positive.append(f"Negative-control transfer-kernel winner: {trans.get('winner')}.")
    if toller: (blockers if "NOT_CLOSED" in toller.get("verdict","") else positive).append("Naive multiplicative blocking does not preserve a simple-pole Toller-like analytic class; full glued/summed RG is required.")
    if carc: positive.append(f"CARC linear surrogate: {carc.get('verdict')}.")
    if cci: positive.append(f"Finite-scale CCI test: {cci.get('verdict')}.")
    if multi: positive.append(f"Multiscale leakage scan: {multi.get('verdict')}.")
    if codim: positive.append(f"Constraint-count result: {codim.get('verdict')}.")
    if novelty and novelty.get("verdict")=="G8_BLOCKED_CONVERGENCE_ONLY": blockers.append("Current established CRQN features remain covered by the union of source families; novelty requires physical F9/F10.")
    elif novelty: positive.append(f"Novelty audit: {novelty.get('verdict')}.")
    if f9 and not f9.get("passed",False): blockers.append("F9 is fail-closed BLOCKED: " + ", ".join(f9.get("missing",[])) + ".")
    elif f9: positive.append("F9 physical same-realization gate passed.")
    f9_pass=bool(f9 and f9.get("passed"))
    overall="CRQN_V0_2_F9_FORMULATED_NOT_PHYSICALLY_CLOSED"
    if f9_pass and novelty and novelty.get("verdict")!="G8_BLOCKED_CONVERGENCE_ONLY": overall="CRQN_REVIEW_FOR_PROMOTION"
    out={"overall":overall,"positive_findings":positive,"blockers":blockers,"next_target":"PHYSICAL_SAME_REALIZATION_CCI_TOLLER_RG","candidate_relation":"P_bprime^± iota_bprime,b = iota_bprime,b P_b^±","interpretation":"MSQGR now has a finite-scale causal/RG selector (CCI) and an infinitesimal CARC form. Structural surrogates show it is nonredundant with ordinary cylindrical consistency and restrictive under repeated RG composition. However, no physical causal-Toller/EPRL embedding map has yet been shown to satisfy it, so CRQN is not promoted."}
    op=Path(args.output);op.parent.mkdir(parents=True,exist_ok=True);op.write_text(json.dumps(out,indent=2),encoding="utf-8");md=Path(args.markdown);md.parent.mkdir(parents=True,exist_ok=True)
    lines=[f"# MSQGR parallel campaign verdict\n\n**Overall:** `{overall}`\n\n**Candidate relation:** `{out['candidate_relation']}`\n\n**Next target:** `{out['next_target']}`\n\n## Blockers\n"]+[f"- {x}\n" for x in blockers]+["\n## Positive findings\n"]+[f"- {x}\n" for x in positive]+["\n## Interpretation\n",out["interpretation"]+"\n"]
    md.write_text("".join(lines),encoding="utf-8");print(json.dumps(out,indent=2))
if __name__=="__main__": main()
