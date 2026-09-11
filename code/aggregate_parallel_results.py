#!/usr/bin/env python3
"""Aggregate JSON outputs from the parallel MSQGR research campaign."""
from __future__ import annotations
import argparse, json
from pathlib import Path

def read_named(root,name):
    hits=list(root.rglob(name));return json.loads(hits[0].read_text(encoding="utf-8")) if hits else None

def main():
    ap=argparse.ArgumentParser();ap.add_argument("--input",default="parallel-results");ap.add_argument("--output",default="combined-results/combined_verdict.json");ap.add_argument("--markdown",default="combined-results/summary.md");args=ap.parse_args();root=Path(args.input)
    char=read_named(root,"causal_character_scan.json");rank=read_named(root,"constraint_rank.json");trans=read_named(root,"transfer_semigroup.json");toller=read_named(root,"toller_rg_closure_toy.json");novelty=read_named(root,"novelty_overlap.json")
    carc=read_named(root,"causal_rg_commutator.json");cci=read_named(root,"causal_embedding_consistency.json");multi=read_named(root,"carc_multiscale_scan.json");codim=read_named(root,"carc_codimension.json");f9=read_named(root,"f9_gate.json")
    poles=read_named(root,"gamma_simple_toller_pole_closure.json");taxonomy=read_named(root,"toller_embedding_taxonomy.json");gammaflow=read_named(root,"gamma_flow_causal_sector.json");eprl=read_named(root,"published_eprl_delta4_convergence.json")
    blockers=[];positive=[];structural=[];backend=[]
    if char: blockers.append("Naive scalar multiplicative branch leaves a free phase parameter; retained only as a negative control.") if char.get("verdict")=="UNDERDETERMINED_PHASE_FAMILY" else positive.append(f"Scalar scan: {char.get('verdict')}.")
    if rank: blockers.append(f"Scalar negative-control rank={rank.get('rank')}, nullity={rank.get('nullity')}.") if rank.get("nullity",0)>0 else positive.append(f"Scalar constraint rank={rank.get('rank')}.")
    if trans: structural.append(f"Negative-control transfer-kernel winner: {trans.get('winner')}.")
    if toller: blockers.append("Naive multiplicative blocking does not preserve a simple-pole Toller-like analytic class; full glued/summed RG is required.") if "NOT_CLOSED" in toller.get("verdict","") else structural.append(f"Pole surrogate: {toller.get('verdict')}.")
    if carc: structural.append(f"CARC linear surrogate: {carc.get('verdict')}.")
    if cci: positive.append(f"Finite-scale CCI test: {cci.get('verdict')}.")
    if multi: positive.append(f"Multiscale leakage scan: {multi.get('verdict')}.")
    if codim: positive.append(f"Constraint-count result: {codim.get('verdict')}.")
    if poles: structural.append(f"Gamma-simple Toller pole test: {poles.get('verdict')} over {poles.get('tested_configurations')} exact configurations; integer-N matches={poles.get('exact_integer_N_matches')}.")
    if taxonomy: positive.append(f"Embedding hierarchy: {taxonomy.get('verdict')} — CCI permits same-sector superpositions and is weaker than single-pole closure.")
    if gammaflow: structural.append("Gamma-flow topology diagnostic completed; gamma=0 is the boost-frequency sign-degeneracy surface for gamma-simple causal branch labeling.")
    if eprl:
        overlap=eprl.get('max15_vs_max25_overlap',{})
        backend.append(f"Published Lorentzian EPRL Delta4 data parsed successfully; max15/max25 overlap={overlap.get('verdict')} with max relative difference={overlap.get('max_relative_difference')}.")
        grades={}
        for row in eprl.get('convergence_summary',[]): grades[row.get('grade')]=grades.get(row.get('grade'),0)+1
        backend.append(f"Observed shell-cutoff final-step convergence grades across published series: {grades}.")
    if novelty and novelty.get("verdict")=="G8_BLOCKED_CONVERGENCE_ONLY": blockers.append("Current established CRQN features remain covered by the union of source families; novelty requires physical F9/F10.")
    elif novelty: positive.append(f"Novelty audit: {novelty.get('verdict')}.")
    if f9 and not f9.get("passed",False): blockers.append("F9 is fail-closed BLOCKED: " + ", ".join(f9.get("missing",[])) + ".")
    elif f9: positive.append("F9 physical same-realization gate passed.")
    f9_pass=bool(f9 and f9.get("passed"))
    overall="CRQN_V0_2_PHYSICAL_BACKEND_PREPARED__F9_OPEN" if eprl else "CRQN_V0_2_TOLLER_STRUCTURE_SHARPENED__PHYSICAL_F9_OPEN"
    if f9_pass and novelty and novelty.get("verdict")!="G8_BLOCKED_CONVERGENCE_ONLY": overall="CRQN_REVIEW_FOR_PROMOTION"
    out={"overall":overall,"positive_findings":positive,"backend_evidence":backend,"structural_controls":structural,"blockers":blockers,"next_target":"RUN_OR_REUSE_LORENTZIAN_EPRL_AMPLITUDE_AND_BUILD_TOLLER_PROJECTED_EMBEDDING_MAP","candidate_relation":"P_bprime^± iota_bprime,b = iota_bprime,b P_b^±","new_exact_negative_control":"For raw same-branch gamma-simple pole multiplication at fixed nonzero gamma, matching to one coarse pole forces N=n1+n2+1/2, so single-pole closure is impossible.","interpretation":"The project now has both an explicit Toller analytic target and a reproducibility audit against published sl2cfoam-next Lorentzian EPRL multi-vertex data. The remaining scientific step is not more abstract surrogate work: it is to construct the same-realization causal projector and dynamical boundary map on an actual Lorentzian amplitude/truncation and measure cross-sector leakage plus cutoff convergence."}
    op=Path(args.output);op.parent.mkdir(parents=True,exist_ok=True);op.write_text(json.dumps(out,indent=2),encoding="utf-8");md=Path(args.markdown);md.parent.mkdir(parents=True,exist_ok=True)
    lines=[f"# MSQGR parallel campaign verdict\n\n**Overall:** `{overall}`\n\n**Candidate relation:** `{out['candidate_relation']}`\n\n**Next target:** `{out['next_target']}`\n\n## Blockers\n"]+[f"- {x}\n" for x in blockers]+["\n## Physical backend evidence\n"]+[f"- {x}\n" for x in backend]+["\n## Positive findings\n"]+[f"- {x}\n" for x in positive]+["\n## Structural/negative controls\n"]+[f"- {x}\n" for x in structural]+["\n## Interpretation\n",out["interpretation"]+"\n"]
    md.write_text("".join(lines),encoding="utf-8");print(json.dumps(out,indent=2))
if __name__=="__main__": main()
