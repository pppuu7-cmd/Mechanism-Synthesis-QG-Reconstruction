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
    blockers=[];positive=[]
    if char: (blockers if char.get("verdict")=="UNDERDETERMINED_PHASE_FAMILY" else positive).append("Naive scalar multiplicative branch leaves a free phase parameter.")
    if rank: (blockers if rank.get("nullity",0)>0 else positive).append(f"Linearized scalar-branch constraint rank={rank.get('rank')}, nullity={rank.get('nullity')}.")
    if trans: positive.append(f"Negative-control transfer-kernel winner: {trans.get('winner')}.")
    if toller: (blockers if "NOT_CLOSED" in toller.get("verdict","") else positive).append("Naive multiplicative blocking does not preserve a simple-pole Toller-like analytic class.")
    if novelty: (blockers if novelty.get("verdict")=="G8_BLOCKED_CONVERGENCE_ONLY" else positive).append(f"Novelty audit: {novelty.get('verdict')}.")
    overall="CRQN_V0_2_NOT_PROMOTED";next_target="F9_CAUSAL_ANALYTICITY_RG_INVARIANT"
    if novelty and novelty.get("verdict")!="G8_BLOCKED_CONVERGENCE_ONLY" and not blockers: overall="REVIEW_FOR_PROMOTION"
    out={"overall":overall,"positive_findings":positive,"blockers":blockers,"next_target":next_target,"interpretation":"The carrier and causal analytic ingredients are viable, but the current CRQN scaffold is covered by known source families. The sharp next test is whether a full same-realization coarse-graining map preserves the causal/Toller analytic branch without introducing independent pole/coupling data."}
    op=Path(args.output);op.parent.mkdir(parents=True,exist_ok=True);op.write_text(json.dumps(out,indent=2),encoding="utf-8");md=Path(args.markdown);md.parent.mkdir(parents=True,exist_ok=True)
    lines=[f"# MSQGR parallel campaign verdict\n\n**Overall:** `{overall}`\n\n**Next target:** `{next_target}`\n\n## Blockers\n"]+[f"- {x}\n" for x in blockers]+["\n## Positive findings\n"]+[f"- {x}\n" for x in positive]+["\n## Interpretation\n",out["interpretation"]+"\n"]
    md.write_text("".join(lines),encoding="utf-8");print(json.dumps(out,indent=2))
if __name__=="__main__": main()
