#!/usr/bin/env python3
import argparse
import itertools
import json
import os
import sys
from collections import defaultdict
from fractions import Fraction


def perms(n):
    return list(itertools.permutations(range(n)))


def compose(p, q):
    return tuple(p[q[i]] for i in range(len(p)))


def ppow(p, k):
    r = tuple(range(len(p)))
    for _ in range(k):
        r = compose(p, r)
    return r


def cycle_type(p):
    seen = set()
    out = []
    for i in range(len(p)):
        if i in seen:
            continue
        j = i
        n = 0
        while j not in seen:
            seen.add(j)
            n += 1
            j = p[j]
        out.append(n)
    return tuple(sorted(out, reverse=True))


def cycles(p):
    seen = set()
    out = []
    for i in range(len(p)):
        if i in seen:
            continue
        c = []
        j = i
        while j not in seen:
            seen.add(j)
            c.append(j)
            j = p[j]
        out.append(c)
    return out


def parity(p):
    inv = sum(p[i] > p[j] for i in range(len(p)) for j in range(i + 1, len(p)))
    return -1 if inv % 2 else 1


def eye(n):
    return [[Fraction(int(i == j)) for j in range(n)] for i in range(n)]


def madd(a, b):
    return [[x + y for x, y in zip(ra, rb)] for ra, rb in zip(a, b)]


def msub(a, b):
    return [[x - y for x, y in zip(ra, rb)] for ra, rb in zip(a, b)]


def mscale(a, c):
    return [[c * x for x in r] for r in a]


def mmul(a, b):
    bt = list(zip(*b))
    return [[sum((x * y for x, y in zip(r, c)), Fraction(0)) for c in bt] for r in a]


def trace(a):
    return sum((a[i][i] for i in range(len(a))), Fraction(0))


def rank(a):
    m = [r[:] for r in a]
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
        if r == nr:
            break
    return r


def bitperm_matrix(p):
    """Permutation matrix on n qubit tensor factors, with factor i sent to p(i)."""
    n = len(p)
    d = 1 << n
    a = [[Fraction(0) for _ in range(d)] for _ in range(d)]
    for x in range(d):
        bits = [(x >> (n - 1 - i)) & 1 for i in range(n)]
        out = [0] * n
        for i in range(n):
            out[p[i]] = bits[i]
        y = 0
        for bit in out:
            y = (y << 1) | bit
        a[y][x] = 1
    return a


def local_projector():
    """Exact four-spin singlet projector from total J^2, no character literals."""
    ps = perms(4)
    ident = eye(16)
    j2 = [[Fraction(0) for _ in range(16)] for _ in range(16)]
    # For four spin-1/2 factors, J^2 = sum_{i<j} Swap_ij exactly.
    for i in range(4):
        for j in range(i + 1, 4):
            p = list(range(4))
            p[i], p[j] = p[j], p[i]
            j2 = madd(j2, bitperm_matrix(tuple(p)))
    proj = mscale(
        mmul(msub(j2, mscale(ident, 2)), msub(j2, mscale(ident, 6))),
        Fraction(1, 12),
    )
    chars = {p: trace(mmul(proj, bitperm_matrix(p))) for p in ps}
    return proj, chars


def restrict_fixed_vertex(q, v):
    neighbors = [x for x in range(5) if x != v]
    pos = {x: i for i, x in enumerate(neighbors)}
    return tuple(pos[q[x]] for x in neighbors)


def boundary_char_all(local_char):
    """Trace of canonical K5 vertex relabeling on the full 32D boundary space."""
    vals = {}
    for sigma in perms(5):
        val = Fraction(1)
        for c in cycles(sigma):
            ell = len(c)
            v = c[0]
            q = ppow(sigma, ell)
            leg_perm = restrict_fixed_vertex(q, v)
            val *= local_char[leg_perm]
        vals[sigma] = val
    return vals


def class_rows_from_map(vals):
    out = defaultdict(list)
    for p, v in vals.items():
        out[cycle_type(p)].append(v)
    return dict(out)


def representative(cycle_shape):
    arr = list(range(5))
    base = 0
    for length in cycle_shape:
        cyc = list(range(base, base + length))
        base += length
        for a, b in zip(cyc, cyc[1:] + cyc[:1]):
            arr[a] = b
    return tuple(arr)


def s5_irrep_chars(class_types):
    """Generate the complete S5 irreducible character table from the 4D standard rep."""
    names = ["[5]", "[4,1]", "[3,2]", "[3,1,1]", "[2,2,1]", "[2,1,1,1]", "[1^5]"]
    out = {name: [] for name in names}
    for ct in class_types:
        p = representative(ct)
        chi_std = sum(i == p[i] for i in range(5)) - 1
        p2 = compose(p, p)
        chi_std2 = sum(i == p2[i] for i in range(5)) - 1
        sign = parity(p)
        wedge2 = (chi_std * chi_std - chi_std2) // 2
        sym2 = (chi_std * chi_std + chi_std2) // 2
        chi_32 = sym2 - 1 - chi_std
        vals = {
            "[5]": 1,
            "[4,1]": chi_std,
            "[3,2]": chi_32,
            "[3,1,1]": wedge2,
            "[2,2,1]": chi_32 * sign,
            "[2,1,1,1]": chi_std * sign,
            "[1^5]": sign,
        }
        for name, value in vals.items():
            out[name].append(value)
    return out


def inner(class_sizes, a, b):
    return sum(
        Fraction(size) * Fraction(x) * Fraction(y)
        for size, x, y in zip(class_sizes, a, b)
    ) / 120


def decompose(class_sizes, char, irreps):
    return {name: inner(class_sizes, char, chi) for name, chi in irreps.items()}


def jsonable(x):
    if isinstance(x, Fraction):
        return x.numerator if x.denominator == 1 else f"{x.numerator}/{x.denominator}"
    if isinstance(x, tuple):
        return list(x)
    if isinstance(x, list):
        return [jsonable(v) for v in x]
    if isinstance(x, dict):
        return {str(k): jsonable(v) for k, v in x.items()}
    return x


def validate_boundary(candidate, canonical, class_types):
    rows = class_rows_from_map(candidate)
    return (
        candidate == canonical
        and all(len(set(rows[ct])) == 1 for ct in class_types)
        and candidate[tuple(range(5))] == 32
    )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", default="results/raw/iter081r_sm_invariant_jets.json")
    ap.add_argument("--output")
    args = ap.parse_args()

    with open(args.input, encoding="utf-8") as fh:
        raw = json.load(fh)
    class_types = [tuple(r["cycle_type"]) for r in raw["s5_class_rows"]]
    class_sizes = [r["class_size"] for r in raw["s5_class_rows"]]
    rows = [r["su2_singlet_multiplicity_by_degree"] for r in raw["s5_class_rows"]]
    degrees = list(range(9))

    proj, local = local_projector()
    local_by_class = class_rows_from_map(local)
    p1 = (
        mmul(proj, proj) == proj
        and rank(proj) == 2
        and all(
            mmul(proj, bitperm_matrix(p)) == mmul(bitperm_matrix(p), proj)
            for p in perms(4)
        )
        and all(len(set(v)) == 1 for v in local_by_class.values())
    )
    local_class_char = {ct: vals[0] for ct, vals in local_by_class.items()}

    bmap = boundary_char_all(local)
    brow = class_rows_from_map(bmap)
    class_const = all(len(set(brow[ct])) == 1 for ct in class_types)
    bchar = [brow[ct][0] for ct in class_types]
    irreps = s5_irrep_chars(class_types)
    hdec = decompose(class_sizes, bchar, irreps)
    dims = {
        "[5]": 1,
        "[4,1]": 4,
        "[3,2]": 5,
        "[3,1,1]": 6,
        "[2,2,1]": 5,
        "[2,1,1,1]": 4,
        "[1^5]": 1,
    }
    p2 = class_const and bchar[0] == 32
    p3 = (
        all(v.denominator == 1 and v >= 0 for v in hdec.values())
        and sum(int(hdec[name]) * dims[name] for name in dims) == 32
    )

    sign = irreps["[1^5]"]
    twisted = [a * b for a, b in zip(bchar, sign)]
    direct = []
    direct_twisted = []
    mdecs = []
    via_decomposition = []
    for k in degrees:
        mk = [r[k] for r in rows]
        direct.append(inner(class_sizes, bchar, mk))
        direct_twisted.append(inner(class_sizes, twisted, mk))
        dec = decompose(class_sizes, mk, irreps)
        mdecs.append(dec)
        via_decomposition.append(sum(hdec[name] * dec[name] for name in irreps))

    p4 = direct_twisted == direct
    p5 = direct == via_decomposition and all(x.denominator == 1 and x >= 0 for x in direct)
    scalar = raw["degree_dimensions_d0_to_d8"]
    odd_open = [k for k in degrees if scalar[k] == 0 and direct[k] > 0]
    p6 = len(odd_open) > 0
    p0 = (
        raw.get("verdict") == "PASS_EXACT_SCOPED"
        and raw.get("geometry", {}).get("normal_fiber") == "spin1_SU2 tensor Std5_S5"
        and sum(class_sizes) == 120
        and len(class_types) == 7
        and scalar == [1, 0, 1, 0, 3, 0, 7, 0, 16]
        and all(len(r) == 9 for r in rows)
    )

    # Frozen negative controls, each passed through the same structural validator.
    bad_rank2 = [
        [Fraction(int(i == j and i < 2)) for j in range(16)]
        for i in range(16)
    ]
    bad_projector_accepted = (
        mmul(bad_rank2, bad_rank2) == bad_rank2
        and rank(bad_rank2) == 2
        and all(
            mmul(bad_rank2, bitperm_matrix(p)) == mmul(bitperm_matrix(p), bad_rank2)
            for p in perms(4)
        )
    )

    vertex_only = {sigma: Fraction(2) ** len(cycles(sigma)) for sigma in perms(5)}
    neg_vertex = not validate_boundary(vertex_only, bmap, class_types)

    badrows = [r[:] for r in rows]
    badrows[1][0] += 1
    bad_scalar = [
        inner(class_sizes, [1] * 7, [r[k] for r in badrows]) for k in degrees
    ]
    neg_corrupt = bad_scalar != [Fraction(x) for x in scalar]

    unweighted = [
        sum(Fraction(a) * Fraction(r[k]) for a, r in zip(bchar, rows)) / 120
        for k in degrees
    ]
    neg_unweighted = unweighted != direct
    neg_scalar_substitution = [Fraction(x) for x in scalar] != direct

    forced = dict(bmap)
    nonidentity = next(p for p in perms(5) if p != tuple(range(5)))
    forced[nonidentity] += 1
    neg_nonclass = not all(
        len(set(v)) == 1 for v in class_rows_from_map(forced).values()
    )

    controls = {
        "arbitrary_rank2_projector_rejected": not bad_projector_accepted,
        "vertex_only_action_rejected": neg_vertex,
        "corrupted_iter081r_row_rejected": neg_corrupt,
        "unweighted_inner_product_rejected": neg_unweighted,
        "scalar_dimensions_substitution_rejected": neg_scalar_substitution,
        "non_class_constant_table_rejected": neg_nonclass,
    }
    p7 = all(controls.values())
    predicates = {
        f"P{i}": value
        for i, value in enumerate([p0, p1, p2, p3, p4, p5, p6, p7])
    }
    passed = all(predicates.values())

    verdict = "PASS_EXACT_SCOPED" if passed else "INVALID_IMPLEMENTATION"
    classification = (
        "K5_BOUNDARY_COVARIANT_INVARIANT_NORMAL_SYMBOL_CHARACTER_CLASSIFICATION_EXACT_SCOPED"
        if passed
        else "K5_BOUNDARY_COVARIANT_NORMAL_SYMBOL_CLASSIFICATION_INVALID_IMPLEMENTATION"
    )
    result = {
        "iteration": "Iter083A-SM",
        "classification": classification,
        "verdict": verdict,
        "predicates": predicates,
        "controls": controls,
        "local_s4_singlet_character": [
            {"cycle_type": list(ct), "trace": jsonable(local_class_char[ct])}
            for ct in sorted(local_class_char, reverse=True)
        ],
        "s5_cycle_types": [list(x) for x in class_types],
        "s5_class_sizes": class_sizes,
        "boundary_character": jsonable(bchar),
        "boundary_irrep_decomposition": jsonable(hdec),
        "boundary_character_norm": jsonable(inner(class_sizes, bchar, bchar)),
        "m_k_0_to_8": jsonable(direct),
        "m_k_via_irrep_decomposition": jsonable(via_decomposition),
        "total_m_leq8": jsonable(sum(direct)),
        "scalar_d_k_0_to_8": scalar,
        "orders_opened_beyond_scalar": odd_open,
        "M_k_irrep_decompositions": [jsonable(x) for x in mdecs],
        "interpretation_ceiling": (
            "local boundary-covariant graded normal-symbol multiplicities only; "
            "not global distributional patching, selector, finiteness, uniqueness, "
            "or full extension-space dimension"
        ),
    }
    text = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        os.makedirs(os.path.dirname(args.output) or ".", exist_ok=True)
        with open(args.output, "w", encoding="utf-8") as fh:
            fh.write(text)
    print(text, end="")
    return 0 if passed else 2


if __name__ == "__main__":
    sys.exit(main())
