#!/usr/bin/env python3
"""Aggregate the 16 integrated Toller branch masks of an accurate B4 calculation.

Authoritative test: sum the full complex post-Speziale QAGP tensors BEFORE the
ordinary sl2cfoam `crealq` projection and compare with the ordinary EPRL tensor.
The real B4 matrices are checked as a secondary linearity test.
"""
from __future__ import annotations

import argparse
import csv
import json
import math
import statistics
from pathlib import Path

import mpmath as mp
mp.mp.dps = 80

CASES = ("jhalf_lhalf", "jhalf_lthreehalf")


def read_integrals(path: Path):
    out={}
    with path.open(newline="") as f:
        for r in csv.DictReader(f,delimiter="\t"):
            k=tuple(int(r[x]) for x in ("two_p1","two_p2","two_p3","two_p4"))
            out[k]={
                "z":mp.mpc(mp.mpf(r["re"]),mp.mpf(r["im"])),
                "abserr":mp.mpf(r["abserr"]),"rcode":int(r["rcode"])
            }
    return out


def read_matrix(path: Path):
    out={}
    with path.open(newline="") as f:
        for r in csv.DictReader(f,delimiter="\t"):
            k=(r["case"],int(r["two_i"]),int(r["two_k"]))
            out[k]=mp.mpf(r["value"])
    return out


def rel(a,b,floor=mp.mpf("1e-60")):
    return abs(a-b)/max(abs(b),floor)


def main():
    ap=argparse.ArgumentParser();ap.add_argument("--input",default="all-results");ap.add_argument("--output",default="branch-results/branch_b4_verdict.json");args=ap.parse_args()
    root=Path(args.input)
    baseline_mats=list(root.rglob("matrix_baseline.tsv"))
    if len(baseline_mats)!=1: raise SystemExit(f"expected one matrix_baseline.tsv, found {len(baseline_mats)}")
    bmat=read_matrix(baseline_mats[0])

    missing=[]; masks={}
    for m in range(16):
        hits=list(root.rglob(f"matrix_mask{m}.tsv"))
        if len(hits)!=1: missing.append(m)
        else: masks[m]=read_matrix(hits[0])
    if missing: raise SystemExit(f"missing branch matrix masks: {missing}")

    case_reports={}; global_diffs=[]; global_base=[]; all_conditions=[]
    for case in CASES:
        bh=list(root.rglob(f"integrals_baseline_{case}.tsv"))
        if len(bh)!=1: raise SystemExit(f"expected baseline integral dump for {case}, found {len(bh)}")
        base=read_integrals(bh[0])
        branches={}
        for m in range(16):
            hh=list(root.rglob(f"integrals_mask{m}_{case}.tsv"))
            if len(hh)!=1: raise SystemExit(f"expected mask {m} integral dump for {case}, found {len(hh)}")
            branches[m]=read_integrals(hh[0])
        keysets=[set(base)]+[set(branches[m]) for m in range(16)]
        common=set.intersection(*keysets)
        exact_grid=all(s==set(base) for s in keysets)
        entries=[];diff2=mp.mpf('0');base2=mp.mpf('0');worst_rel=mp.mpf('0');worst_abs=mp.mpf('0');worst=None;conds=[]
        branch_rcodes={m:sum(v["rcode"]!=0 for v in branches[m].values()) for m in range(16)}
        for k in sorted(common):
            bz=base[k]["z"]
            zs=[branches[m][k]["z"] for m in range(16)]
            s=mp.fsum(zs)
            d=s-bz
            ae=abs(d); re=rel(s,bz)
            cond=mp.fsum(abs(z) for z in zs)/max(abs(bz),mp.mpf('1e-80'))
            conds.append(float(cond));diff2+=ae*ae;base2+=abs(bz)**2
            global_diffs.append(ae);global_base.append(abs(bz));all_conditions.append(float(cond))
            if re>worst_rel:worst_rel=re;worst_abs=ae;worst=(k,bz,s,cond)
            entries.append({"p":list(k),"baseline":[float(mp.re(bz)),float(mp.im(bz))],"sum16":[float(mp.re(s)),float(mp.im(s))],"absolute_error":float(ae),"relative_error":float(re),"branch_cancellation_condition":float(cond)})
        frob=mp.sqrt(diff2)/max(mp.sqrt(base2),mp.mpf('1e-80'))
        nonzero_imag=max((abs(mp.im(v["z"])) for v in base.values()),default=mp.mpf('0'))
        case_reports[case]={
            "integral_entries":len(common),"exact_complex_tensor_grid_match":exact_grid,
            "frobenius_relative_complex_reconstruction_error":float(frob),
            "worst_complex_entry_relative_error":float(worst_rel),
            "worst_complex_entry_absolute_error":float(worst_abs),
            "max_baseline_imaginary_magnitude":float(nonzero_imag),
            "branch_cancellation_condition":{"median":statistics.median(conds) if conds else None,"p90":sorted(conds)[min(len(conds)-1,math.ceil(.9*len(conds))-1)] if conds else None,"max":max(conds) if conds else None},
            "nonzero_qagp_rcodes_by_mask":branch_rcodes,
            "worst_entry":{"p":list(worst[0]),"baseline":[float(mp.re(worst[1])),float(mp.im(worst[1]))],"sum16":[float(mp.re(worst[2])),float(mp.im(worst[2]))],"condition":float(worst[3])} if worst else None,
            "entries":entries
        }

    # Secondary real-projected full B4 matrix reconstruction.
    matrix_rows=[];mdiff2=mp.mpf('0');mbase2=mp.mpf('0');mworst=mp.mpf('0')
    for k,b in sorted(bmat.items()):
        vals=[masks[m][k] for m in range(16)]
        s=mp.fsum(vals);d=s-b;mdiff2+=abs(d)**2;mbase2+=abs(b)**2;er=rel(s,b,mp.mpf('1e-30'));mworst=max(mworst,er)
        matrix_rows.append({"case":k[0],"two_i":k[1],"two_k":k[2],"baseline":float(b),"sum16_real_projected_branches":float(s),"absolute_error":float(abs(d)),"relative_error":float(er)})
    mfrob=mp.sqrt(mdiff2)/max(mp.sqrt(mbase2),mp.mpf('1e-80'))

    max_frob=max(v["frobenius_relative_complex_reconstruction_error"] for v in case_reports.values())
    max_qagp_bad=max(max(v["nonzero_qagp_rcodes_by_mask"].values()) for v in case_reports.values())
    passed=(max_frob<5e-4 and float(mfrob)<5e-4 and max_qagp_bad==0)
    out={
        "branch_masks":16,"cases":list(CASES),"passed":passed,
        "complex_tensor_threshold":5e-4,"max_case_frobenius_complex_error":max_frob,
        "real_projected_matrix_frobenius_error":float(mfrob),"worst_real_projected_matrix_relative_error":float(mworst),
        "max_nonzero_qagp_rcodes_per_mask_case":max_qagp_bad,
        "global_branch_cancellation_condition":{"median":statistics.median(all_conditions),"p90":sorted(all_conditions)[min(len(all_conditions)-1,math.ceil(.9*len(all_conditions))-1)],"max":max(all_conditions)},
        "case_reports":case_reports,"matrix_rows":matrix_rows,
        "verdict":"INTEGRATED_16_BRANCH_TOLLER_EXPANSION_RECONSTRUCTS_EPRL_B4" if passed else "BRANCH_RESOLVED_B4_NUMERICAL_GATE_OPEN",
        "interpretation":"All 2^4 analytic Toller choices were integrated independently under the same Lorentzian measure and Speziale phase. The authoritative comparison is performed on the full complex QAGP tensor before upstream's ordinary-EPRL real projection; the real B4 matrix sum is secondary.",
        "scientific_guardrail":"These 16 four-leg booster masks are the algebraic branch expansion of one B4 building block. A physical causal vertex must additionally impose the vertex-level wedge-sign constraints kappa_ab=sigma_a sigma_b; this result alone is not F9."
    }
    op=Path(args.output);op.parent.mkdir(parents=True,exist_ok=True);op.write_text(json.dumps(out,indent=2),encoding="utf-8")
    print(json.dumps({k:v for k,v in out.items() if k not in ("case_reports","matrix_rows")},indent=2))
    if not passed: raise SystemExit(5)

if __name__=="__main__": main()
