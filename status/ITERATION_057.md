# Iteration 057 — complete K4 oriented pole-sign space and S4 orbit atlas

## Preregistration

This file is committed before Iter057 implementation and production output.

Iter057 does not consume Iter056 output. It addresses a separate structural question suggested by Iter055: the original eight factorized sign vectors are not closed under the naive relabeling relevant to the frozen oriented-flow surrogate. Rather than post-hoc modifying those eight classes, Iter057 prospectively enlarges the surrogate domain to **all 64 six-edge sign vectors** and asks for its exact orientation-aware symmetry structure.

## Frozen domain

Edge order is

`01,02,03,12,13,23`.

Enumerate every vector

`s in {+1,-1}^6`.

For each `s` and each frozen tree/cycle basis `S0,S1,P0,P1`, form

`M(s)=diag(s) A`

and exhaustively enumerate all support-minimal positive circuits of row normals on supports of size 1..4, using exact rational algebra only.

Strict chamber feasibility is defined exactly as **absence of any positive circuit**.

## Frozen orientation-aware S4 action

For every vertex permutation `p`:

- map each old edge to the corresponding target undirected edge;
- attach orientation sign `q=+1` if the mapped old orientation agrees with the canonical target orientation, and `q=-1` otherwise;
- define the target pole-sign vector by

  `s'_newedge = q * s_oldedge`.

No other correction is allowed.

This is the same algebraic edge-orientation rule implied by rewriting the frozen denominator `x-i s epsilon` in the target canonically oriented edge-flow variable, but Iter057 implements and checks the action independently rather than reading Iter056 artifacts.

## Frozen gates

1. **Basis invariance:** for each of all 64 sign vectors, the complete minimal-positive-circuit support atlas must be identical across `S0,S1,P0,P1`.
2. **Orientation-aware S4 covariance:** for all `64×24=1536` sign/permutation actions, permuting every source circuit support by the induced edge map must exactly reproduce the target sign vector's circuit-support atlas.
3. **Feasibility orbit invariance:** strict chamber feasibility must be constant on every exact S4 orbit.
4. **Factorized-subset orbit closure:** independently identify the eight original factorized `sigma_a sigma_b` edge-sign vectors and compute their exact closure under the orientation-aware S4 action. Do not assume the closure has size 8, 16, 32, or 64.
5. Report all S4 orbits of the 64 vectors, orbit sizes, feasible/infeasible status, circuit-count and support-size histograms, and which orbits intersect the original factorized subset.

## Exact completeness

For each sign/basis lane all `56=sum_{k=1}^4 C(6,k)` supports are tested. Total support tests are therefore `64×4×56=14336`.

All circuit certificates must have strictly positive exact weights summing to 1 and exact zero weighted normal. No floating tolerances, optimizer, fitted sign rule, or post-hoc orbit merge is allowed.

## Frozen terminal classifications

- `ITER057_ORIENTED_SIGN_SPACE_INVALID` if any basis/certificate/action validation fails.
- `K4_ORIENTED_SIGN_SPACE_BASIS_DEPENDENT` if a valid sign vector has different complete circuit atlases across bases.
- `K4_ORIENTED_SIGN_SPACE_S4_NONCOVARIANT` if basis invariance passes but any orientation-aware S4 circuit mapping or feasibility mapping fails.
- `K4_ORIENTED_SIGN_SPACE_EXACT_BASIS_AND_S4_COVARIANT` iff all exact checks pass.

## Claim locks

This is an exact combinatorial/linear-algebra atlas of the frozen K4 oriented pole-sign surrogate. It does not identify physical causal sectors, prove a full Toller vertex permutation law, define a causal amplitude, unblock K5/G3/F9/G8, or establish new physics.
