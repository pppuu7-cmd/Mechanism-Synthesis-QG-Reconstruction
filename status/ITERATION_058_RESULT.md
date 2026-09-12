# Iteration 058 result — strict K4 chamber iff strongly connected tournament

**Status:** terminal

**Classification:** `K4_STRICT_CHAMBER_IFF_STRONGLY_CONNECTED_TOURNAMENT`

Authoritative run: `34719879504`

Artifact: `10305894028`

Artifact digest: `sha256:24d06807b51f87d4751d3df3e4804c4e839e5e6cfce75ffb8d202492790bd84f`

Preregistration commit: `51c3e04da81652060a3bc76c2bad5c9825faecca` before implementation/output.

## Frozen theorem gate

For every oriented K4 sign vector `s in {+1,-1}^6`, define the tournament `D(s)` by orienting edge `(a,b)`, `a<b`, as `a->b` when `s_e=+1` and `b->a` when `s_e=-1`.

Iter058 tested the exact equivalence

`exists x in ker(B) such that s_e x_e > 0 for all six edges`

iff

`D(s) is strongly connected`.

Because each frozen K4 cycle matrix `A` is an exact basis of `ker(B)`, this is equivalent to existence of `v` with

`diag(s) A v > 0`.

## Terminal exact result

- oriented sign vectors audited: **64/64**;
- audit validity: **PASS**;
- equivalence passes: **64/64**;
- strongly connected tournaments: **24**;
- strict-chamber feasible sign vectors: **24**;
- deterministic constructive strictly positive circulations: **24**;
- exact one-way directed-cut obstruction certificates: **40**;
- S4 orbit count: **4**;
- exactly one S4 orbit is strongly connected and feasible.

For every strongly connected tournament, the implementation constructs a strictly positive circulation by taking each directed edge, appending a deterministic shortest directed return path to form a directed cycle, and summing the six directed-cycle flows. The result satisfies exactly

`B x = 0`

and

`s_e x_e > 0`

on all six edges, and is reconstructed exactly in all four frozen cycle bases.

For every non-strong tournament, the implementation finds a nonempty proper vertex subset with a one-way directed cut. Summing the conservation equations over that subset yields a strictly nonzero net cut flux, giving an exact obstruction to a strictly positive circulation.

The complete positive-circuit criterion is independently recomputed and agrees on all 64 sign vectors.

## Exact S4 orbit interpretation

The four orientation-aware S4 orbits coincide with the four unlabeled K4 tournament types:

- size 8: score sequence `[3,1,1,1]`, 1 directed triangle, obstructed;
- size 8: score sequence `[2,2,2,0]`, 1 directed triangle, obstructed;
- size 24: score sequence `[3,2,1,0]`, 0 directed triangles, transitive, obstructed;
- size 24: score sequence `[2,2,1,1]`, 2 directed triangles, **strongly connected and strict-chamber feasible**.

Thus the Iter054/057 feasible 24-orbit has an exact graph-flow characterization rather than being an accidental finite enumeration.

## Mathematical scope

The audited K4 statement is an instance of the standard circulation principle: a directed graph admits a strictly positive circulation on every edge exactly when every directed edge belongs to a directed cycle; strong connectivity is sufficient and, for tournaments, equivalent to the condition relevant here.

Iter058 establishes the full K4 domain constructively and exactly. It does **not** identify this tournament condition with a physical Toller causal-sector selection.

## Physics boundary

The next required step is source-backed. One must derive and test the actual branch transformation under wedge reversal / group inversion for

`T^(kappa)(g_b^-1 g_a)`

rather than infer it from the denominator surrogate. Toller branches are functions on SL(2,C), not representations, so ordinary representation inversion/composition identities cannot be transferred branchwise without proof.

## Claim locks

- no physical causal-sector selection from tournament strong connectivity;
- no physical causal-vertex finiteness/divergence theorem;
- no K5 or G3 PASS;
- no F9/G8 promotion;
- no complete-QG or new-physics claim.
