#!/usr/bin/env python3
"""Iter046: K4 forest/cycle-basis/integration-order consistency.

The script applies exactly the Iter045 one-dimensional polynomial-subtraction
plus residue/PV operator sequentially to the three independent cycle variables
of a constrained K4 edge-flow kernel.  Production compares four spanning-tree
bases and all six integration orders.  An F=1 no-contact control is computed in
every job.

Scientific scope: this tests consistency of one candidate extension rule.  It
is not a causal-vertex finiteness theorem and cannot promote G3/F9/G8.
"""
from __future__ import annotations

import argparse
import itertools
import json
import math
import time
from pathlib import Path
import sympy as sp

EDGES = [(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
EDGE_NAMES = ["01","02","03","12","13","23"]
TREES = {
    "S0": (0,1,2),       # 01,02,03
    "S1": (0,3,4),       # 01,12,13
    "P0": (0,3,5),       # 01,12,23
    "P1": (1,3,4),       # 02,12,13
}
ORDERS = ("012","021","102","120","201","210")


def parse_signs(txt: str):
    if len(txt) != 6 or any(c not in "+-" for c in txt):
        raise ValueError("signs must contain six +/- characters")
    return tuple(1 if c == "+" else -1 for c in txt)


def parse_k(txt: str):
    vals = tuple(sp.Rational(x.strip()) for x in txt.split(","))
    if len(vals) != 4:
        raise ValueError("k must contain four comma-separated rationals")
    if sp.simplify(sum(vals)) != 0:
        raise ValueError("external K4 flow must sum exactly to zero")
    return vals


def incidence():
    B = sp.zeros(4,6)
    for j,(a,b) in enumerate(EDGES):
        B[a,j] = -1
        B[b,j] = 1
    return B


def constrained_edge_flows(tree_name: str, k):
    tree = TREES[tree_name]
    chords = tuple(i for i in range(6) if i not in tree)
    y = sp.symbols("y0:3", real=True)
    Bred = incidence()[:3,:]
    BT = Bred[:,list(tree)]
    det = sp.simplify(BT.det())
    if abs(int(det)) != 1:
        raise RuntimeError(f"non-unimodular tree incidence minor: {det}")
    BC = Bred[:,list(chords)]
    xT = BT.inv() * (sp.Matrix(k[:3]) - BC*sp.Matrix(y))
    x = [None]*6
    for i,e in enumerate(tree):
        x[e] = sp.expand(xT[i])
    for i,e in enumerate(chords):
        x[e] = y[i]
    # exact constraint check
    residual = incidence()*sp.Matrix(x) - sp.Matrix(k)
    if any(sp.simplify(z) != 0 for z in residual):
        raise RuntimeError(f"incidence solve failed: {residual}")
    return y, tuple(x), tree, chords, det


def build_kernel(gamma, epsilon, signs, k, tree_name, control=False):
    y,x,tree,chords,det = constrained_edge_flows(tree_name,k)
    rho = gamma/2
    den0 = rho*rho + sp.Rational(1,4)
    c1 = 2*rho/den0
    c2 = 2/den0
    expr = sp.Integer(1)
    for xe,se in zip(x,signs):
        if control:
            numer = sp.Integer(1)
        else:
            numer = sp.expand(1 + c1*xe + (c2/2)*xe*xe)
        expr *= numer/(xe - sp.I*se*epsilon)
    return y, sp.factor(expr), {
        "tree_edges":[EDGE_NAMES[i] for i in tree],
        "chord_edges":[EDGE_NAMES[i] for i in chords],
        "tree_incidence_det":str(det),
        "rho":str(rho),"c1":str(c1),"c2":str(c2),
    }


def _linear_roots_of_denominator(den, var):
    factors = sp.factor_list(den, var)[1]
    roots=[]
    for fac,mult in factors:
        P = sp.Poly(fac,var,domain="EX")
        deg=P.degree()
        if deg == 0:
            continue
        if deg != 1:
            raise RuntimeError(f"nonlinear denominator factor in {var}: degree={deg}, factor={fac}")
        if mult != 1:
            raise RuntimeError(f"repeated denominator pole in {var}: multiplicity={mult}, factor={fac}")
        a,b=P.all_coeffs()
        r=sp.cancel(-b/a)
        imr=sp.simplify(sp.im(r))
        if imr.free_symbols:
            raise RuntimeError(f"pole imaginary part depends on remaining real variables: root={r}, Im={imr}")
        roots.append((r,imr))
    return roots


def finite_part_1d(expr, var):
    """Exactly the Iter045 operator, optimized for simple linear poles."""
    expr=sp.cancel(expr)
    num,den=sp.fraction(expr)
    Pn=sp.Poly(num,var,domain="EX")
    Pd=sp.Poly(den,var,domain="EX")
    Q,R=sp.div(Pn,Pd)
    rem=sp.cancel(R.as_expr()/Pd.as_expr())

    rn,rd=sp.fraction(rem)
    Prn=sp.Poly(rn,var,domain="EX")
    Prd=sp.Poly(rd,var,domain="EX")
    dn,dd=Prn.degree(),Prd.degree()
    if dn == dd-1:
        a_minus1=sp.cancel(Prn.LC()/Prd.LC())
    elif dn < dd-1:
        a_minus1=sp.Integer(0)
    else:
        raise RuntimeError(f"improper remainder after division: deg(num)={dn}, deg(den)={dd}")

    roots=_linear_roots_of_denominator(Prd.as_expr(),var)
    Dprime=sp.diff(Prd.as_expr(),var)
    Nexpr=Prn.as_expr()
    residue_sum=sp.Integer(0)
    upper_count=0
    for root,imr in roots:
        sign=float(sp.N(imr,30))
        if abs(sign) < 1e-14:
            raise RuntimeError(f"unexpected real-axis pole: {root}")
        if sign > 0:
            # all frozen generic production poles are simple
            residue=sp.cancel(Nexpr.subs(var,root)/Dprime.subs(var,root))
            residue_sum += residue
            upper_count += 1

    out=sp.cancel(2*sp.pi*sp.I*residue_sum - sp.pi*sp.I*a_minus1)
    qdeg=-1 if Q.is_zero else int(Q.degree())
    return out, {
        "quotient_degree":qdeg,
        "remainder_num_degree":int(dn),
        "remainder_den_degree":int(dd),
        "upper_pole_count":upper_count,
        "pole_count":len(roots),
    }


def sequential_result(gamma,epsilon,signs,k,tree_name,order,control=False):
    y,expr,meta=build_kernel(gamma,epsilon,signs,k,tree_name,control=control)
    current=expr
    stages=[]
    for c in order:
        idx=int(c)
        t0=time.time()
        current,stage=finite_part_1d(current,y[idx])
        stage["coordinate_index"]=idx
        stage["seconds"]=time.time()-t0
        stages.append(stage)
    current=sp.cancel(current)
    if any(v in current.free_symbols for v in y):
        raise RuntimeError(f"sequential result still depends on cycle variables: {current.free_symbols}")
    meta.update({"stages":stages})
    return current,meta


def compute(args):
    gamma=sp.Rational(args.gamma)
    epsilon=sp.Rational(args.epsilon)
    if epsilon <= 0:
        raise ValueError("epsilon must be positive")
    signs=parse_signs(args.signs)
    k=parse_k(args.k)
    if args.tree not in TREES:
        raise ValueError(f"unknown tree {args.tree}")
    if args.order not in ORDERS:
        raise ValueError(f"unknown order {args.order}")

    t0=time.time()
    source,smeta=sequential_result(gamma,epsilon,signs,k,args.tree,args.order,False)
    control,cmeta=sequential_result(gamma,epsilon,signs,k,args.tree,args.order,True)
    elapsed=time.time()-t0
    out={
        "iteration":"Iter046",
        "case":args.case,
        "gamma":args.gamma,"epsilon":args.epsilon,"signs":args.signs,"k":list(map(str,k)),
        "tree":args.tree,"order":args.order,
        "source_exact":str(source),
        "source_numeric":[str(sp.re(sp.N(source,25))),str(sp.im(sp.N(source,25)))],
        "control_exact":str(control),
        "control_numeric":[str(sp.re(sp.N(control,25))),str(sp.im(sp.N(control,25)))],
        "source_meta":smeta,"control_meta":cmeta,
        "total_seconds":elapsed,
        "claim_lock":"Single K4 forest/order lane only; aggregate comparison decides scientific classification. No G3/F9/G8 claim.",
    }
    return out


def _complex_pair(row,key):
    re,im=row[key]
    return complex(float(re),float(im))


def aggregate(input_dir: Path):
    rows=[]
    for p in sorted(input_dir.rglob("iter046_*.json")):
        try:
            r=json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            continue
        if r.get("iteration") == "Iter046" and "source_exact" in r:
            rows.append(r)
    if not rows:
        raise RuntimeError("no Iter046 lane JSON files found")

    cases={}
    for case in sorted(set(r["case"] for r in rows)):
        cr=[r for r in rows if r["case"]==case]
        expected=24
        source_vals=[_complex_pair(r,"source_numeric") for r in cr]
        control_vals=[_complex_pair(r,"control_numeric") for r in cr]
        def spread(vals):
            scale=max(max(abs(v) for v in vals),1e-30)
            return max(abs(v-w) for v in vals for w in vals)/scale
        source_spread=spread(source_vals)
        control_spread=spread(control_vals)

        # final exact strings are compact; sympify and compare after cancellation
        src_expr=[sp.sympify(r["source_exact"]) for r in cr]
        ctl_expr=[sp.sympify(r["control_exact"]) for r in cr]
        source_exact_equal=all(sp.simplify(v-src_expr[0])==0 for v in src_expr[1:])
        control_exact_equal=all(sp.simplify(v-ctl_expr[0])==0 for v in ctl_expr[1:])
        control_pass=(len(cr)==expected and (control_exact_equal or control_spread < 1e-10))
        source_pass=(len(cr)==expected and source_exact_equal and source_spread < 1e-10)
        if not control_pass:
            classification="K4_CONTROL_INVALID"
        elif source_pass:
            classification="K4_FINITE_PART_FOREST_ORDER_COVARIANT"
        else:
            classification="K4_FINITE_PART_ORDER_OR_FOREST_DEPENDENT"

        # extrema for a useful negative-result witness
        max_pair=None; max_delta=-1.0
        for i in range(len(cr)):
            for j in range(i+1,len(cr)):
                d=abs(source_vals[i]-source_vals[j])
                if d>max_delta:
                    max_delta=d; max_pair=(i,j)
        witness=None
        if max_pair:
            i,j=max_pair
            witness={
                "a":{"tree":cr[i]["tree"],"order":cr[i]["order"],"value":cr[i]["source_numeric"]},
                "b":{"tree":cr[j]["tree"],"order":cr[j]["order"],"value":cr[j]["source_numeric"]},
                "absolute_difference":max_delta,
            }
        cases[case]={
            "lane_count":len(cr),"expected_lane_count":expected,
            "source_exact_equal":source_exact_equal,
            "source_relative_spread":source_spread,
            "control_exact_equal":control_exact_equal,
            "control_relative_spread":control_spread,
            "classification":classification,
            "max_source_difference_witness":witness,
        }
    return {
        "iteration":"Iter046",
        "cases":cases,
        "all_cases_control_valid":all(v["classification"]!="K4_CONTROL_INVALID" for v in cases.values()),
        "all_cases_source_covariant":all(v["classification"]=="K4_FINITE_PART_FOREST_ORDER_COVARIANT" for v in cases.values()),
        "claim_lock":"K4 forest/order consistency only. A source FAIL with valid control is a multi-cycle extension negative result, not a physical vertex divergence theorem or G3/F9/G8 result.",
    }


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--mode",choices=["compute","aggregate"],default="compute")
    ap.add_argument("--case")
    ap.add_argument("--gamma")
    ap.add_argument("--epsilon")
    ap.add_argument("--signs")
    ap.add_argument("--k")
    ap.add_argument("--tree",choices=sorted(TREES))
    ap.add_argument("--order",choices=ORDERS)
    ap.add_argument("--input-dir",default="results")
    ap.add_argument("--output",required=True)
    a=ap.parse_args()
    if a.mode=="compute":
        required=[a.case,a.gamma,a.epsilon,a.signs,a.k,a.tree,a.order]
        if any(v is None for v in required):
            raise SystemExit("compute mode requires case,gamma,epsilon,signs,k,tree,order")
        out=compute(a)
    else:
        out=aggregate(Path(a.input_dir))
    p=Path(a.output); p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(out,indent=2),encoding="utf-8")
    print(json.dumps(out,indent=2))

if __name__=="__main__":
    main()
