# Iteration 057 result — complete K4 oriented pole-sign space and S4 orbit atlas

**Status:** terminal

**Classification:** `K4_ORIENTED_SIGN_SPACE_EXACT_BASIS_AND_S4_COVARIANT`

Authoritative run: `34719626599`

Artifact: `10305747534`

Artifact digest: `sha256:53cb834063b722aed716ad524ec79de76c25d6a63087456c227db84264c380c4`

Preregistration commit: `00c92f5f35f21209e4501a4ff8dcbd00e1d3a39b` before implementation/output.

## Complete exact audit

The domain is every six-edge oriented pole-sign vector `s in {+1,-1}^6` in edge order `01,02,03,12,13,23`.

For each of 64 sign vectors and each of four K4 cycle bases, Iter057 exhaustively enumerated all positive-circuit supports of size 1..4 for `diag(s)A`.

Totals:

- sign vectors: **64**;
- basis lanes: **256/256 valid**;
- exact support tests: **14,336**;
- basis consistency: PASS;
- orientation-aware S4 actions: **1,536/1,536 covariant**;
- feasibility constant on every S4 orbit: PASS;
- strict-chamber feasible vectors: **24**;
- obstructed vectors: **40**.

## Exact S4 orbit decomposition

The 64 oriented sign vectors split into exactly four S4 orbits:

1. size 8, obstructed, one minimal positive circuit per vector;
2. size 8, obstructed, one minimal positive circuit per vector;
3. size 24, obstructed, three minimal positive circuits per vector;
4. size 24, **strict-chamber feasible**, zero positive circuits.

The original eight factorized `sigma_a sigma_b` sign vectors intersect the two 24-element orbits. Their orientation-aware S4 orbit closure has size **48**, exactly the same 48 effective oriented sign vectors independently generated in Iter056.

Among the original factorized representatives:

- obstructed 24-orbit: `+++`, `++-`, `+--`, `---`;
- feasible 24-orbit: `+-+`, `-++`, `-+-`, `--+`.

Thus the 4/8 Iter054 split is not an arbitrary class artifact. Its correct invariant statement is that the factorized representatives lie in two distinct **orientation-aware S4 orbits of oriented pole-sign data**, one obstructed and one feasible. Physical causal wedge data and oriented pole-sign data remain distinct objects.

## Graph-theoretic clue

Interpreting each six-edge sign vector as an orientation of the complete graph K4 gives exactly the four unlabeled four-vertex tournament types expected from the four S4 orbits. The feasible 24-orbit has tournament score sequence `[2,2,1,1]`; the obstructed 24-orbit is the transitive tournament `[3,2,1,0]`; the two obstructed size-8 orbits have score sequences `[3,1,1,1]` and `[2,2,2,0]`.

This strongly suggests that strict affine chamber feasibility is the graph-flow condition for a strictly positive circulation, equivalently strong connectivity for a tournament. This interpretation was **not** part of Iter057's frozen classifier and requires a separate prospective theorem gate.

## Claim locks

This is an exact combinatorial/linear-algebra atlas of the frozen oriented K4 pole-sign surrogate. It does not identify physical causal sectors, prove a full Toller vertex permutation law, define a causal amplitude, unblock K5/G3/F9/G8, or establish new physics.
