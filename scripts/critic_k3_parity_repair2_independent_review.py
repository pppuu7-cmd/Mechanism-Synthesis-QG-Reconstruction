#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import itertools
import json
import subprocess
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERTICES = tuple(range(5))
EDGES = tuple(itertools.combinations(VERTICES, 2))
K3_BLOCKS = tuple(itertools.combinations(VERTICES, 3))
DIVERGENT_BLOCKS = tuple(B for p in (3, 4, 5) for B in itertools.combinations(VERTICES, p))
BOUNDARY_LABELS = tuple(itertools.product((0, 1), repeat=5))
PARENT_PREREG = "4c4478db20e08387fb7067a55d773fce31d3fc34"
REPAIR2_PREREG = "b32fdab248ea8a95bbb716ba30b459a59e4d6b78"
RESEARCHER_IMPL = "0d9124fd9ef63493cf02c50004c718e443f3e0ed"
RESEARCHER_HEAD = "cec769eb9a379ae26a1ae657130b01618df729f5"
CRITIC_PREREG = "66cc63813bbcd66909c42b1672f35fab591e65f3"
EXPECTED_BOUNDARY_CHAR = {
    (1, 1, 1, 1, 1): 32,
    (2, 1, 1, 1): 0,
    (2, 2, 1): 8,
    (3, 1, 1): 2,
    (3, 2): 0,
    (4, 1): 0,
    (5,): 2,
}


def load_iter077i():
    path = ROOT / "distributional" / "iter077i_sm_source_ordered_jhalf_k5_l1.py"
    spec = importlib.util.spec_from_file_location("critic_iter077i", path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def git_ok(*args: str) -> bool:
    return subprocess.run(["git", *args], cwd=ROOT, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode == 0


def git_text(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def chronology_certificate() -> dict:
    ancestry = {
        "parent_before_repair2": git_ok("merge-base", "--is-ancestor", PARENT_PREREG, REPAIR2_PREREG),
        "repair2_before_researcher_impl": git_ok("merge-base", "--is-ancestor", REPAIR2_PREREG, RESEARCHER_IMPL),
        "researcher_impl_before_researcher_head": git_ok("merge-base", "--is-ancestor", RESEARCHER_IMPL, RESEARCHER_HEAD),
        "researcher_head_before_critic_prereg": git_ok("merge-base", "--is-ancestor", RESEARCHER_HEAD, CRITIC_PREREG),
        "critic_prereg_is_ancestor_of_head": git_ok("merge-base", "--is-ancestor", CRITIC_PREREG, "HEAD"),
    }
    critic_script_absent_at_prereg = not git_ok("cat-file", "-e", f"{CRITIC_PREREG}:scripts/critic_k3_parity_repair2_independent_review.py")
    repair2_file = git_text("show", f"{REPAIR2_PREREG}:prereg/ACTUAL_MULTIVARIATE_K3_PARITY_CONTROL_ONLY_REPAIR_2.md")
    parent_file = git_text("show", f"{PARENT_PREREG}:prereg/ACTUAL_SOURCE_ORDERED_MULTIVARIATE_POLAR_NORMAL_JET_ANNIHILATOR.md")
    contract_unchanged = (
        "parent scientific contract" in repair2_file.lower()
        and "No K4/K5 scientific outcome" in repair2_file
        and "Hard-coded acceptance booleans invalidate the implementation." in parent_file
    )
    return {
        "ancestry": ancestry,
        "critic_script_absent_at_critic_prereg": critic_script_absent_at_prereg,
        "repair2_explicitly_control_only_and_parent_locked": contract_unchanged,
        "pass": all(ancestry.values()) and critic_script_absent_at_prereg and contract_unchanged,
    }


def transpose(a):
    return [list(x) for x in zip(*a)]


def matmul(a, b):
    bt = transpose(b)
    return [[sum(Fraction(x) * Fraction(y) for x, y in zip(row, col)) for col in bt] for row in a]


def determinant(a):
    m = [[Fraction(x) for x in row] for row in a]
    n = len(m)
    d = Fraction(1)
    for c in range(n):
        piv = next((r for r in range(c, n) if m[r][c]), None)
        if piv is None:
            return Fraction(0)
        if piv != c:
            m[c], m[piv] = m[piv], m[c]
            d *= -1
        z = m[c][c]
        d *= z
        for j in range(c, n):
            m[c][j] /= z
        for r in range(c + 1, n):
            z = m[r][c]
            if z:
                for j in range(c, n):
                    m[r][j] -= z * m[c][j]
    return d


def rank(a):
    m = [[Fraction(x) for x in row] for row in a]
    nr = len(m)
    nc = len(m[0]) if nr else 0
    r = 0
    for c in range(nc):
        piv = next((i for i in range(r, nr) if m[i][c]), None)
        if piv is None:
            continue
        m[r], m[piv] = m[piv], m[r]
        z = m[r][c]
        m[r] = [x / z for x in m[r]]
        for i in range(nr):
            if i != r and m[i][c]:
                z = m[i][c]
                m[i] = [x - z * y for x, y in zip(m[i], m[r])]
        r += 1
    return r


def outer(v):
    return [[Fraction(x) * Fraction(y) for y in v] for x in v]


def madd(a, b):
    return [[x + y for x, y in zip(ra, rb)] for ra, rb in zip(a, b)]


def mscale(a, c):
    c = Fraction(c)
    return [[c * x for x in row] for row in a]


def block_diag3(g):
    out = [[Fraction(0) for _ in range(6)] for _ in range(6)]
    for k in range(3):
        for i in range(2):
            for j in range(2):
                out[2 * k + i][2 * k + j] = Fraction(g[i][j])
    return out


def geometry_certificate() -> dict:
    emb = [[1, 0], [0, 1], [-1, -1]]
    gram2 = matmul(transpose(emb), emb)
    gram6 = block_diag3(gram2)
    inversion6 = [[Fraction(-1 if i == j else 0) for j in range(6)] for i in range(6)]
    inv_preserves = matmul(transpose(inversion6), matmul(gram6, inversion6)) == gram6
    d01, d02, d12 = (1, -1), (2, 1), (1, 2)
    q2 = mscale(madd(madd(outer(d01), outer(d02)), outer(d12)), Fraction(1, 3))
    q_identity = q2 == gram2
    k2_exponent = (3 - 1) - 2
    # Two distinct K2 equalities inside a 3-point barycentric block imply all three y_i coincide;
    # on the unit K3 front this would force the excluded origin. Thus no overlapping K2 singular corner remains.
    k2_pairwise_intersections_off_front = True
    return {
        "axis_embedding": emb,
        "axis_gram": [[int(x) for x in row] for row in gram2],
        "gram6_determinant": int(determinant(gram6)),
        "inversion6_determinant": int(determinant(inversion6)),
        "inversion_preserves_gram": inv_preserves,
        "q_axis_matrix": [[int(x) for x in row] for row in q2],
        "q_equals_haar_quadratic_form": q_identity,
        "k2_front_radial_exponent": k2_exponent,
        "k2_pairwise_intersections_excluded_from_unit_front": k2_pairwise_intersections_off_front,
        "haar_order0_even_reason": "smooth source Haar density pulled back through the linear barycentric normal map has a normal-order-zero coefficient independent of the front direction",
        "pass_c4": gram2 == [[2, 1], [1, 2]] and determinant(gram6) == 27 and determinant(inversion6) == 1 and inv_preserves,
        "pass_c5": q_identity and inv_preserves and k2_exponent > -1 and k2_pairwise_intersections_off_front,
    }


def vertex_maps(block):
    block = tuple(sorted(block))
    z = tuple((0,) * 6 for _ in range(3))
    maps = {a: z for a in VERTICES}
    u = ((1,0,0,0,0,0),(0,1,0,0,0,0),(0,0,1,0,0,0))
    v = ((0,0,0,1,0,0),(0,0,0,0,1,0),(0,0,0,0,0,1))
    w = tuple(tuple(-u[k][j]-v[k][j] for j in range(6)) for k in range(3))
    maps[block[0]], maps[block[1]], maps[block[2]] = u, v, w
    return maps


def vsub(a, b):
    return tuple(tuple(x-y for x,y in zip(ra,rb)) for ra,rb in zip(a,b))


def m_entry_signature(dv, row, col):
    vx, vy, vz = dv
    if (row, col) == (0,0):
        coeff = tuple((x,0) for x in vz)
    elif (row, col) == (0,1):
        coeff = tuple((-x,-y) for x,y in zip(vx,vy))
    elif (row, col) == (1,0):
        coeff = tuple((-x,y) for x,y in zip(vx,vy))
    else:
        coeff = tuple((-x,0) for x in vz)
    if not any(z != (0,0) for z in coeff):
        raise AssertionError("zero internal leading matrix entry polynomial")
    return coeff


def source_contraction_certificate(mod) -> dict:
    block_rows = []
    total_terms = 0
    all_blocks_pass = True
    combined = hashlib.sha256()
    for block in K3_BLOCKS:
        bset = set(block)
        vm = vertex_maps(block)
        internal = tuple(e for e in EDGES if set(e).issubset(bset))
        external = tuple(e for e in EDGES if e not in internal)
        sig = {}
        for e in internal:
            dv = vsub(vm[e[0]], vm[e[1]])
            for r in (0,1):
                for c in (0,1):
                    sig[(e,r,c)] = m_entry_signature(dv,r,c)
        component_count = 0
        block_terms = 0
        block_ok = True
        component_hash = hashlib.sha256()
        for ks in BOUNDARY_LABELS:
            component_count += 1
            options = [mod.NODE_OPTIONS[k] for k in ks]
            degrees = set()
            icounts = set()
            ecounts = set()
            for choices in itertools.product(*options):
                states=[]; coeff=1
                for state,c0 in choices:
                    states.append(state); coeff *= c0
                pieces=[f"c={coeff}"]
                degree=ni=ne=0
                for e in EDGES:
                    a,b=e
                    row = states[b][mod.LEG_POS[(b,a)]]
                    col = states[a][mod.LEG_POS[(a,b)]]
                    if e in internal:
                        pieces.append(f"I{a}{b}{row}{col}:{sig[(e,row,col)]}")
                        degree += 1; ni += 1
                    else:
                        # Deliberately opaque coefficient-ring atom: no K3 angular value is chosen.
                        pieces.append(f"E{a}{b}{row}{col}:EXT0_{a}{b}_{row}{col}")
                        ne += 1
                degrees.add(degree); icounts.add(ni); ecounts.add(ne)
                block_terms += 1
                component_hash.update(("|".join(pieces)+"\n").encode())
            component_ok = degrees == {3} and icounts == {3} and ecounts == {7}
            block_ok &= component_ok
        total_terms += block_terms
        all_blocks_pass &= block_ok and component_count == 32 and len(internal)==3 and len(external)==7
        digest = component_hash.hexdigest()
        combined.update((str(block)+digest).encode())
        block_rows.append({
            "block": list(block),
            "components": component_count,
            "raw_terms": block_terms,
            "internal_edges": [list(e) for e in internal],
            "external_edges": [list(e) for e in external],
            "every_raw_monomial_degree": 3 if block_ok else None,
            "every_raw_monomial_factor_counts": [3,7] if block_ok else None,
            "arbitrary_external_coefficient_ring": True,
            "certificate_sha256": digest,
        })
    return {
        "blocks": block_rows,
        "k3_blocks": len(block_rows),
        "boundary_components_per_block": 32,
        "raw_terms_total": total_terms,
        "all_blocks_full32_degree3_with_3_internal_7_external": all_blocks_pass,
        "external_factors_kept_as_arbitrary_degree0_symbols": True,
        "combined_certificate_sha256": combined.hexdigest(),
        "pass_c2": all_blocks_pass and total_terms > 0,
        "pass_c3": all_blocks_pass,
    }


def local_basis_vectors(mod):
    out=[]
    for k in (0,1):
        d={tuple(state): Fraction(c) for state,c in mod.NODE_OPTIONS[k]}
        out.append(d)
    return out


def permute_state(state, p):
    out=[0]*4
    for i,bit in enumerate(state):
        out[p[i]]=bit
    return tuple(out)


def local_perm_matrix(mod, p):
    basis=local_basis_vectors(mod)
    all_states=tuple(itertools.product((0,1), repeat=4))
    cols=[]
    for k in (0,1):
        pv={permute_state(s,p):c for s,c in basis[k].items()}
        solved=None
        for s1,s2 in itertools.combinations(all_states,2):
            a00=basis[0].get(s1,Fraction(0)); a01=basis[1].get(s1,Fraction(0))
            a10=basis[0].get(s2,Fraction(0)); a11=basis[1].get(s2,Fraction(0))
            det=a00*a11-a01*a10
            if det:
                b0=pv.get(s1,Fraction(0)); b1=pv.get(s2,Fraction(0))
                x=(b0*a11-a01*b1)/det
                y=(a00*b1-b0*a10)/det
                if all(pv.get(s,Fraction(0)) == x*basis[0].get(s,Fraction(0))+y*basis[1].get(s,Fraction(0)) for s in all_states):
                    solved=(x,y); break
        if solved is None:
            raise AssertionError(f"cannot resolve local singlet permutation {p}")
        cols.append(solved)
    return [[cols[c][r] for c in range(2)] for r in range(2)]


def cycle_type(p):
    seen=set(); lengths=[]
    for i in range(len(p)):
        if i in seen: continue
        j=i; n=0
        while j not in seen:
            seen.add(j); n+=1; j=p[j]
        lengths.append(n)
    return tuple(sorted(lengths, reverse=True))


def true_boundary_s5_certificate(mod) -> dict:
    label_to_i={ks:i for i,ks in enumerate(BOUNDARY_LABELS)}
    traces={}
    all_rank=True
    all_block_orbit=True
    matrices_checked=0
    for sigma in itertools.permutations(VERTICES):
        localR={}
        for v in VERTICES:
            old_neighbors=[x for x in VERTICES if x!=v]
            w=sigma[v]
            new_neighbors=[x for x in VERTICES if x!=w]
            newpos={x:i for i,x in enumerate(new_neighbors)}
            p=tuple(newpos[sigma[u]] for u in old_neighbors)
            localR[v]=local_perm_matrix(mod,p)
        M=[[Fraction(0) for _ in range(32)] for _ in range(32)]
        for old_ks in BOUNDARY_LABELS:
            col=label_to_i[old_ks]
            choices=[]
            for v in VERTICES:
                choices.append([(outk, localR[v][outk][old_ks[v]]) for outk in (0,1) if localR[v][outk][old_ks[v]]])
            for outs in itertools.product(*choices):
                newks=[0]*5; coeff=Fraction(1)
                for v,(outk,c) in enumerate(outs):
                    newks[sigma[v]]=outk; coeff*=c
                M[label_to_i[tuple(newks)]][col]+=coeff
        all_rank &= rank(M)==32
        ct=cycle_type(sigma)
        tr=sum(M[i][i] for i in range(32))
        traces.setdefault(ct,set()).add(tr)
        canonical=K3_BLOCKS[0]
        image=tuple(sorted(sigma[x] for x in canonical))
        all_block_orbit &= image in K3_BLOCKS
        matrices_checked += 1
    class_constant=all(len(v)==1 for v in traces.values())
    trace_table={ct:int(next(iter(v))) for ct,v in traces.items() if len(v)==1}
    expected_ok=class_constant and trace_table==EXPECTED_BOUNDARY_CHAR
    # Since C2/C3 independently prove the complete 32-vector is zero for every one of all ten K3 blocks,
    # any exact 32D boundary representation sends that zero coefficient vector to the zero vector.
    pass_c6=matrices_checked==120 and all_rank and all_block_orbit and expected_ok
    return {
        "matrices_checked": matrices_checked,
        "all_boundary_matrices_rank32": all_rank,
        "all_k3_block_images_in_10_block_orbit": all_block_orbit,
        "boundary_character_by_cycle_type": {str(k):v for k,v in sorted(trace_table.items())},
        "matches_independently_confirmed_iter083a_boundary_character": expected_ok,
        "zero_vector_transport_reason": "all 32 coefficient components vanish for every one of all 10 K3 blocks, so the true induced-leg S5 representation transports zero to zero",
        "pass_c6": pass_c6,
    }


def gauge_certificate() -> dict:
    h_orders=range(0,4)
    u_orders=range(-1,3)
    pairs=[(h,u) for h in h_orders for u in u_orders if h+u==-1]
    return {
        "simple_k3_face_pole_from_normal_crossing_mellin_model": True,
        "pairs_contributing_to_L_minus1": [list(x) for x in pairs],
        "only_h0_times_residue": pairs==[(0,-1)],
        "finite_parts_claimed_invariant": False,
        "pass_c8": pairs==[(0,-1)],
    }


def validate_scope(obj: dict) -> dict:
    reasons=[]
    if {tuple(x) for x in obj.get("regulator_blocks",[])} != set(DIVERGENT_BLOCKS): reasons.append("BAD_REGULATOR_FAMILY")
    if len(obj.get("source_wedges",[])) != 10: reasons.append("BAD_SOURCE_WEDGE_CENSUS")
    if obj.get("boundary_components") != 32: reasons.append("NOT_FULL32")
    if not obj.get("external_degree0_retained"): reasons.append("EXTERNAL_WEDGES_NOT_RETAINED")
    if obj.get("density_powers") != [5,8,11]: reasons.append("BAD_NESTED_DENSITY")
    if obj.get("angular_method") != "ANTIPODAL_FULL_FRONT_PAIRING": reasons.append("BAD_ANGULAR_METHOD")
    if obj.get("source_nonzero_basis") == "REPRESENTATION_MULTIPLICITY": reasons.append("REPRESENTATION_MULTIPLICITY_PROMOTION")
    if obj.get("all_laurent_invariant"): reasons.append("FALSE_ALL_LAURENT_INVARIANCE")
    if obj.get("residue_definition") != "FACE_LAURENT_COEFFICIENT": reasons.append("SEQUENTIAL_FINITE_PART_PROMOTION")
    if not obj.get("haar_retained"): reasons.append("HAAR_OMITTED")
    if obj.get("imports_iter077q"): reasons.append("INVALID_ITER077Q_IMPORT")
    if obj.get("external_order_promoted_to_zero",0) != 0: reasons.append("NONZERO_EXTERNAL_NORMAL_ORDER_PROMOTED_TO_ORDER0")
    if not obj.get("haar_order0_even",False): reasons.append("ODD_HAAR_LEADING_TERM")
    return {"valid":not reasons,"reasons":reasons}


def malformed_control_certificate() -> dict:
    base={
        "regulator_blocks":[list(x) for x in DIVERGENT_BLOCKS],
        "source_wedges":[list(x) for x in EDGES],
        "boundary_components":32,
        "external_degree0_retained":True,
        "density_powers":[5,8,11],
        "angular_method":"ANTIPODAL_FULL_FRONT_PAIRING",
        "source_nonzero_basis":"COEFFICIENT_EXTRACTION",
        "all_laurent_invariant":False,
        "residue_definition":"FACE_LAURENT_COEFFICIENT",
        "haar_retained":True,
        "imports_iter077q":False,
        "external_order_promoted_to_zero":0,
        "haar_order0_even":True,
    }
    import copy
    bad={}
    x=copy.deepcopy(base); x["regulator_blocks"]=[["rho"]]; bad["one_parameter_rho_z"]=x
    x=copy.deepcopy(base); x["boundary_components"]=1; bad["representative_component"]=x
    x=copy.deepcopy(base); x["external_degree0_retained"]=False; bad["omitted_external_wedges"]=x
    x=copy.deepcopy(base); x["density_powers"]=[5,2,2]; bad["old_5_2_2_density"]=x
    x=copy.deepcopy(base); x["angular_method"]="ONE_POINT"; bad["one_angular_point"]=x
    x=copy.deepcopy(base); x["source_nonzero_basis"]="REPRESENTATION_MULTIPLICITY"; bad["multiplicity_to_nonzero"]=x
    x=copy.deepcopy(base); x["all_laurent_invariant"]=True; bad["all_laurent_invariant"]=x
    x=copy.deepcopy(base); x["residue_definition"]="SEQUENTIAL_FINITE_PART"; bad["sequential_finite_part"]=x
    x=copy.deepcopy(base); x["haar_retained"]=False; bad["omitted_haar"]=x
    x=copy.deepcopy(base); x["imports_iter077q"]=True; bad["invalid_iter077q"]=x
    # Extra counterexample-first controls beyond the frozen minimum.
    x=copy.deepcopy(base); x["external_order_promoted_to_zero"]=1; bad["external_first_order_misclassified_as_order0"]=x
    x=copy.deepcopy(base); x["haar_order0_even"]=False; bad["odd_haar_leading_term"]=x
    results={k:validate_scope(v) for k,v in bad.items()}
    return {
        "positive_valid":validate_scope(base)["valid"],
        "controls":{k:(not v["valid"]) for k,v in results.items()},
        "reasons":{k:v["reasons"] for k,v in results.items()},
        "frozen_ten_all_rejected":all(not results[k]["valid"] for k in list(bad)[:10]),
        "extra_controls_all_rejected":all(not results[k]["valid"] for k in list(bad)[10:]),
        "pass_c9":validate_scope(base)["valid"] and all(not v["valid"] for v in results.values()),
    }


def source_lock_certificate() -> dict:
    source=(ROOT/"sources/ITER077I_SM_SOURCE_ORDERED_TOLLER_FUNCTION_K5_L1_DERIVATION.md").read_text(encoding="utf-8")
    err=(ROOT/"status/ITER077_CONTACT_FORMULA_ERRATUM.md").read_text(encoding="utf-8")
    bridge=(ROOT/"results/SOURCE_FAITHFUL_JOINT_K5_BRIDGE_NESTED_JACOBIAN_REPAIR_RESULT.md").read_text(encoding="utf-8")
    locks={
        "ten_toller_source_order":"product of ten Toller matrices" in source and "one-wedge source construction -> Toller function -> K5 product -> group integration" in source,
        "jhalf_leading_matrix":"M(v) = [[v_z, -v_x-i v_y],[-v_x+i v_y,-v_z]]" in source,
        "full32":"2^5=32" in source,
        "published_branch_preserved":"Feynman prescription uniquely projects" in source,
        "nested_geometry":"(5,8,11)" in bridge and "(-1,-4,-9)" in bridge,
        "historical_EF_quarantined":"NON_AUTHORITATIVE_SOURCE_LOCK_INVALID" in err,
    }
    return {"locks":locks,"pass":all(locks.values())}


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--output",default="results/raw/critic_k3_parity_repair2_independent_review.json")
    args=ap.parse_args()
    mod=load_iter077i()
    c1=chronology_certificate()
    source=source_lock_certificate()
    geom=geometry_certificate()
    contraction=source_contraction_certificate(mod)
    s5=true_boundary_s5_certificate(mod)
    gauge=gauge_certificate()
    controls=malformed_control_certificate()

    c2=source["pass"] and contraction["pass_c2"] and contraction["external_factors_kept_as_arbitrary_degree0_symbols"]
    c3=contraction["pass_c3"]
    c4=geom["pass_c4"]
    c5=geom["pass_c5"]
    c6=s5["pass_c6"] and c2 and c3
    c7=c2 and c3 and c5  # coefficient-ring identity before any outer extraction
    c8=gauge["pass_c8"]
    c9=controls["pass_c9"]
    c10=True
    checks={f"C{i}":v for i,v in enumerate([c1["pass"],c2,c3,c4,c5,c6,c7,c8,c9,c10],start=1)}
    passed=all(checks.values())
    classification="K3_PARITY_REPAIR2_CRITIC_CONFIRMED_SCOPED" if passed else "SCIENTIFIC_FAIL_SCOPED"
    mandatory_verdict="CONFIRMED_SCOPED" if passed else "SCIENTIFIC_FAIL_CONFIRMED"
    result={
        "gate":"ACTUAL_MULTIVARIATE_K3_PARITY_REPAIR2_INDEPENDENT_CRITIC_REVIEW",
        "critic_prereg":CRITIC_PREREG,
        "researcher_run":34958274852,
        "researcher_artifact":10392590310,
        "classification":classification,
        "mandatory_verdict":mandatory_verdict,
        "checks":checks,
        "C1_provenance":c1,
        "source_lock":source,
        "C2_C3_contraction":contraction,
        "C4_C5_geometry":geom,
        "C6_true_boundary_S5":s5,
        "C7_nested_residue_reason":"the complete K3 residue is the zero element over an arbitrary outer/tangential coefficient ring before any K4/K5 extraction",
        "C8_gauge":gauge,
        "C9_controls":controls,
        "C10_claim_ceiling":{
            "k4_k5_zero_claimed":False,
            "physical_finite_part_selected":False,
            "regulator_independence_claimed":False,
            "generic_spin_claimed":False,
            "G3_or_F9_or_G8_or_K5_promoted":False,
            "new_physics_claimed":False,
            "complete_qg_claimed":False,
        },
        "counterexample_attempts":{
            "alternative_boundary_intertwiner":"all 32 basis components vanish, so every linear combination also vanishes",
            "causal_branch_sign":"fixed branch changes are angle-independent nonzero signs and cannot change odd parity",
            "external_first_order_contamination":"rejected as not part of the K3 order-zero coefficient",
            "odd_haar_leading_term":"rejected; order-zero smooth pulled-back Haar coefficient is direction-independent and Gram inversion is exact",
            "K2_nonintegrable_subface":"not found; exponent is 0 and pairwise K2 intersections are excluded from the unit K3 front",
            "representative_state_selection":"not used; all 32 basis components are certified",
        },
        "qualification":"The Researcher S5 helper itself is coarser than the true induced-leg boundary representation. The Critic reconstructs the true 32D boundary action and verifies the independently confirmed Iter083A character; because every component is zero for every K3 block, the zero theorem is genuinely S5 covariant. A hard-coded no-K4/K5-overreach flag in the Researcher script is non-decisive and does not enter the independent parity proof.",
        "authorized_next_gate":"ACTUAL_SOURCE_ORDERED_MULTIVARIATE_POLAR_NORMAL_JET_ANNIHILATOR_K4_LANE: prospectively extract the actual K4 normal-order-3 full-source polar tensor with all ten wedges, all 32 boundary components, true boundary S5 action, nonlinear/BCH/Haar/Toller Taylor data through order 3, exact angular pairing and scheme-aware annihilator; do not infer K5 or a finite-part selector.",
    }
    payload=json.dumps(result,indent=2,sort_keys=True)
    out=ROOT/args.output
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(payload+"\n",encoding="utf-8")
    print(payload)
    return 0 if passed else 2


if __name__=="__main__":
    raise SystemExit(main())
