# Iter081R-SM — corrected right-SU(2) / S5 invariant K5 normal-jet ambiguity classification

**Date:** 2026-09-14  
**Status:** `PASS_EXACT_SCOPED`

## Prospective chain

- source-lock correction: `results/ITER077Q_ADVERSARIAL_RIGHT_SU2_SOURCE_LOCK_REVIEW.md`, commit `c0ae0ef208a3eccef4ece7960cdf5337e7d5fa2e`;
- preregistration: `18945b681978cf22a8253a6489034e68a1cae372`;
- implementation: `62c8ee3ac378ddc96df8263cb56c38ae76988517`;
- production head: `22f87a8cb1e5a87285066ac658e7823b223a3bc9`;
- GitHub Actions run: `34882711232`, terminal `success`;
- job: `104105657918`, terminal `success`;
- artifact: `10363029817`, name `iter081r-sm-invariant-jets`;
- artifact ZIP digest: `sha256:260017c1b2ac7186f8f2d5e10a499f40293315fec3d26ad174f3ba67726bf8a8`;
- downloaded aggregate JSON SHA256: `ede1d88e1cabf8ca7c545aa88172ddd425e31a9e6ccd8376e45f382d9c4ab939`;
- durable normalized raw copy: `results/raw/iter081r_sm_invariant_jets.json`, commit `48674739d726f96aad68466cf230b5f1fe061f96`.

## Frozen classification

`ITER081R_SM_RIGHT_SU2_S5_INVARIANT_NORMAL_JET_SPACE_NONTRIVIAL_EXACT_SCOPED`

Verdict: **`PASS_EXACT_SCOPED`**.

## Corrected geometry

The historical Iter077Q infinite-dimensional tangential family is not source-compatible because it omitted the exact node-wise compact gauge symmetry of the fully boundary-contracted causal vertex.

After common-left `SL(2,C)` gauge fixing, the collision manifold is

`N = SU(2)^4`.

The node compact gauge orbit is

`SU(2)^5 / SU(2)_diag ~= SU(2)^4 = N`,

so it is transitive along `N`. Scalar tangential coefficient functions therefore carry no physical functional freedom along `N`: after the exact gauge quotient they reduce to fiber data at one point.

The 12-dimensional normal fiber at the identity orbit is

`V = spin1_SO(3) tensor Std5_S5`,

where the spin-1 factor is the boost-vector adjoint representation and `Std5` is the 4-dimensional standard representation of vertex relabeling `S5`.

Iter077L gives source scaling degree `20` against codimension `12`, hence normal derivative orders through `8` remain allowed.

## Exact invariant-jet count

The preregistered Molien/character computation counts

`d_k = dim Sym^k(V)^(SO(3) x S5)`

for `0<=k<=8`.

The exact production result is

`(d_0,d_1,d_2,d_3,d_4,d_5,d_6,d_7,d_8)`

`= (1,0,1,0,3,0,7,0,16)`.

Therefore the scalar invariant normal-jet subspace allowed through scaling-degree order 8 has dimension

`1 + 1 + 3 + 7 + 16 = 28`.

All odd orders vanish in this scalar invariant sector.

## Exact controls

All frozen controls passed:

- all seven `S5` cycle types were included;
- conjugacy-class sizes sum to `120`;
- every final `d_k` is a nonnegative integer;
- `d_0=1`, `d_1=0`;
- the quadratic invariant exists (`d_2=1`);
- invariant even-order jets exist at orders `0,2,4,6,8`;
- the `S5` projection is active.

The SO(3)-only negative-control sequence before the S5 average is

`(1,0,10,4,55,36,220,180,714)`,

which differs strongly from the final `S5`-invariant sequence.

The exact class-by-class twisted singlet traces are recorded in the aggregate artifact/raw result. Negative entries in some non-identity conjugacy-class rows are character traces, not dimensions; their `S5` class average gives the nonnegative invariant dimensions above.

## Distributional meaning

Each invariant symmetric normal tensor can be realized, using an equivariant tubular neighborhood/compact-group averaging, as the principal normal symbol of a source-symmetry-compatible distribution supported on `N`. Multiplying by the actual nonzero compact boundary functional of Iter077M gives a boundary-linear supported extension difference.

A derivative of order `k` of `delta_N` has transverse scaling degree `12+k`, so every counted jet with `k<=8` remains within the maximal source scaling degree `20`.

At minimum, the familiar invariant family

`delta_N, Delta_perp delta_N, ..., (Delta_perp)^4 delta_N`

supplies five explicit independent even-order directions; the exact invariant theory shows that the full scalar invariant-symbol lower bound is 28-dimensional, with additional independent invariants at orders 4, 6 and 8.

## Scientific correction to Iter077Q

The old statement

`source-compatible ambiguity contains an infinite-dimensional tangential subspace span{Q^n F delta_N}`

is no longer authoritative. Historical Iter077Q is `INVALID_SOURCE_LOCK` because `Q` is not invariant under the omitted node-wise right `SU(2)` gauge action.

The corrected statement is:

**after imposing the exact node-wise compact gauge symmetry and S5 covariance, arbitrary scalar tangential functions collapse, but the frozen minimal-sector K5 extension still contains at least a 28-dimensional source-symmetry-compatible scalar normal-jet ambiguity through order 8.**

Thus the local predictive amplitude remains nonunique, but the demonstrated obstruction is finite-dimensional in this repaired scalar sector, not infinite-dimensional tangential.

## Interpretation ceiling

The number `28` is a **lower bound/subspace dimension**, not the proven exact dimension of the complete physical extension space. Boundary-covariant coefficient maps, other representation-valued normal jets, or additional source structures may enlarge it. Conversely, a future independently motivated boundary-value/composition/normalization law may reduce or select these coefficients.

This result does not prove causal-vertex divergence or nonexistence, generic-spin full-boundary non-L1 behavior, regulator dependence/independence, causal multivertex closure, G3, F9/G8/K5 promotion, `NEW_PHYSICS_FOUND`, or complete quantum gravity.

## Immediate dependency consequence

Any downstream result whose essential physical premise is the historical infinite-dimensional `W=span{Q^n F delta_N}` requires reconciliation. In particular:

- Iter080D's theorem that **any** fixed finite scalar-linear selector family necessarily leaves an infinite-dimensional kernel is not applicable to the repaired finite 28-dimensional scalar subspace; sufficiently many independent conditions could in principle select it.
- Iter080H's `full-W` corpus census and the rationale of Iter080I must be re-evaluated against the corrected jet space.
- Iter080J's weak conormal/WF-only conclusion is expected to survive in repaired form because derivatives of `delta_N` remain conormal, but it requires a new source-compatible jet proof rather than reliance on historical `Q^n`.
- Iter081I's claim of an **infinite-dimensional** ambiguity surviving causal summation is upstream-invalid; a repaired finite-jet persistence statement must be proved separately.

The controlling local blocker is now

`RIGHT_SU2_COVARIANT_K5_EXTENSION_SELECTOR / INVARIANT_NORMAL_JET_COEFFICIENT_SELECTION`.
