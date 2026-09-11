#!/usr/bin/env python3
"""Aggregate JSON outputs from the parallel MSQGR research campaign."""
from __future__ import annotations
import argparse,json
from pathlib import Path

def read_named(root,name):
    hits=list(root.rglob(name));return json.loads(hits[0].read_text(encoding='utf-8')) if hits else None

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--input',default='parallel-results');ap.add_argument('--output',default='combined-results/combined_verdict.json');ap.add_argument('--markdown',default='combined-results/summary.md');args=ap.parse_args();root=Path(args.input)
    names=['causal_character_scan.json','constraint_rank.json','transfer_semigroup.json','toller_rg_closure_toy.json','novelty_overlap.json','causal_rg_commutator.json','causal_embedding_consistency.json','carc_multiscale_scan.json','carc_codimension.json','f9_gate.json','gamma_simple_toller_pole_closure.json','toller_embedding_taxonomy.json','gamma_flow_causal_sector.json','toller_gamma_simple_reference.json','published_eprl_delta4_convergence.json','eprl_cutoff_selector.json','eprl_tail_estimator_validation.json','eprl_tail_model_selection.json','eprl_power_tail_extrapolation.json','eprl_backend_readiness_gate.json','eprl_precision_readiness_gate.json']
    d={n:read_named(root,n) for n in names}
    char=d[names[0]];rank=d[names[1]];trans=d[names[2]];toller=d[names[3]];novelty=d[names[4]];carc=d[names[5]];cci=d[names[6]];multi=d[names[7]];codim=d[names[8]];f9=d[names[9]];poles=d[names[10]];taxonomy=d[names[11]];gammaflow=d[names[12]];tref=d[names[13]];eprl=d[names[14]];cutoff=d[names[15]];tail=d[names[16]];models=d[names[17]];power=d[names[18]];ready=d[names[19]];precision=d[names[20]]
    blockers=[];positive=[];structural=[];backend=[]
    if char and char.get('verdict')=='UNDERDETERMINED_PHASE_FAMILY': blockers.append('Naive scalar multiplicative branch leaves a free phase parameter; retained only as a negative control.')
    if rank and rank.get('nullity',0)>0: blockers.append(f"Scalar negative-control rank={rank.get('rank')}, nullity={rank.get('nullity')}.")
    if trans: structural.append(f"Negative-control transfer-kernel winner: {trans.get('winner')}.")
    if toller and 'NOT_CLOSED' in toller.get('verdict',''): blockers.append('Naive multiplicative blocking does not preserve a simple-pole Toller-like analytic class; full glued/summed RG is required.')
    if carc: structural.append(f"CARC linear surrogate: {carc.get('verdict')}.")
    if cci: positive.append(f"Finite-scale CCI test: {cci.get('verdict')}.")
    if multi: positive.append(f"Multiscale leakage scan: {multi.get('verdict')}.")
    if codim: positive.append(f"Constraint-count result: {codim.get('verdict')}.")
    if poles: structural.append(f"Gamma-simple Toller pole test: {poles.get('verdict')} over {poles.get('tested_configurations')} exact configurations; integer-N matches={poles.get('exact_integer_N_matches')}.")
    if taxonomy: positive.append(f"Embedding hierarchy: {taxonomy.get('verdict')} — CCI permits same-sector superpositions and is weaker than single-pole closure.")
    if gammaflow: structural.append('Gamma-flow topology diagnostic completed; gamma=0 is the boost-frequency sign-degeneracy surface for gamma-simple causal branch labeling.')
    if tref:
        structural.append(f"Direct gamma-simple Toller formula reference: {tref.get('verdict')}; worst t+ + t- - d residual={tref.get('worst_relative_sum_residual')}.")
        if not tref.get('passed',False): blockers.append('The numerical Toller reference failed its additive sum rule and must be corrected before C integration.')
    if eprl:
        ov=eprl.get('max15_vs_max25_overlap',{});backend.append(f"Published Lorentzian EPRL Delta4 overlap={ov.get('verdict')} with max relative difference={ov.get('max_relative_difference')}.")
    if cutoff: backend.append(f"Observed cutoff selector 0.2% candidates={cutoff.get('datasets_meeting_0p2_percent_observed_stability')}.")
    if tail: backend.append(f"Finite-Dl tail-estimator back-test validated choices={tail.get('validated_choices')}.")
    if models: backend.append(f"Finite-tail model preference={models.get('preference_counts')}; use this to choose extrapolator, not as asymptotic proof.")
    if power: backend.append(f"Power-tail extrapolation: max median unresolved tail={power.get('max_median_relative_remaining_tail')}, fit-window spread={power.get('max_fit_window_spread_relative')}.")
    if ready: backend.append(f"Observed-shell backend gate: {ready.get('verdict')}.")
    if precision:
        backend.append(f"Power-tail precision gate: {precision.get('verdict')}; max unresolved tail={precision.get('max_median_tail_fraction')}.")
        if not precision.get('prototype_2pct_ready',False): blockers.append('Published Lorentzian EPRL baseline is not even 2% prototype-ready under the power-tail model.')
    if novelty and novelty.get('verdict')=='G8_BLOCKED_CONVERGENCE_ONLY': blockers.append('Current established CRQN features remain covered by the union of source families; novelty requires physical F9/F10.')
    if f9 and not f9.get('passed',False): blockers.append('F9 is fail-closed BLOCKED: '+', '.join(f9.get('missing',[]))+'.')
    elif f9: positive.append('F9 physical same-realization gate passed.')
    proto=bool(precision and precision.get('prototype_2pct_ready'));quant=bool(precision and precision.get('quantitative_1pct_ready'));f9pass=bool(f9 and f9.get('passed'))
    if proto and not quant: overall='CRQN_V0_2_EPRL_PROJECTOR_PROTOTYPE_READY__PRECISION_F9_OPEN'
    elif quant: overall='CRQN_V0_2_EPRL_QUANTITATIVE_BACKEND_READY__F9_OPEN'
    elif eprl: overall='CRQN_V0_2_PHYSICAL_BACKEND_PREPARED__F9_OPEN'
    else: overall='CRQN_V0_2_TOLLER_STRUCTURE_SHARPENED__PHYSICAL_F9_OPEN'
    if f9pass and novelty and novelty.get('verdict')!='G8_BLOCKED_CONVERGENCE_ONLY': overall='CRQN_REVIEW_FOR_PROMOTION'
    out={'overall':overall,'positive_findings':positive,'backend_evidence':backend,'structural_controls':structural,'blockers':blockers,'prototype_backend_ready':proto,'quantitative_1pct_backend_ready':quant,'next_target':'INSERT_TOLLER_T_PLUS_MINUS_AT_SL2CFOAM_DSMALL_BOOSTER_LEVEL_AND_COMPUTE_CAUSAL_VERTEX','candidate_relation':'P_bprime^± iota_bprime,b = iota_bprime,b P_b^±','interpretation':'Run 006c distinguishes observed shell stability from the modelled unresolved tail and supplies a direct high-precision Toller reference implementation. The physically meaningful next step is to branch the reduced Lorentzian Wigner d-matrix inside the booster integration into Toller t+ and t- components, then recompute vertices/boundary maps. Scalar post-projection is not sufficient.'}
    op=Path(args.output);op.parent.mkdir(parents=True,exist_ok=True);op.write_text(json.dumps(out,indent=2),encoding='utf-8');md=Path(args.markdown);md.parent.mkdir(parents=True,exist_ok=True)
    lines=[f"# MSQGR parallel campaign verdict\n\n**Overall:** `{overall}`\n\n**Next target:** `{out['next_target']}`\n\n## Blockers\n"]+[f"- {x}\n" for x in blockers]+['\n## Physical backend evidence\n']+[f"- {x}\n" for x in backend]+['\n## Positive findings\n']+[f"- {x}\n" for x in positive]+['\n## Structural/negative controls\n']+[f"- {x}\n" for x in structural]+['\n## Interpretation\n',out['interpretation']+'\n'];md.write_text(''.join(lines),encoding='utf-8');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
