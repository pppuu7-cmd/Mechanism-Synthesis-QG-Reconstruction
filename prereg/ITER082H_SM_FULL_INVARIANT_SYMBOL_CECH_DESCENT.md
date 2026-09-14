# Iter082H-SM preregistration — full invariant-symbol Čech descent

Date: 2026-09-15

## Motivation and dependency lock

Iter082G proved exact Čech descent only for abstract scalar normal-order coefficient modules of dimensions `omega_k+1`. It explicitly did **not** prove the corresponding statement for the corrected source-symmetry-compatible invariant normal tensors identified by Iter081R.

This gate prospectively lifts the descent audit to the complete **scalar invariant-symbol submodule** at each frozen divergent block size `K3/K4/K5`, while keeping all finite parts, subtraction scales and physical selector coefficients symbolic.

The gate does not claim to cover representation-valued boundary-covariant coefficient maps beyond the scalar invariant-symbol sector, and does not construct globally patched physical distributions.

## Frozen geometry

For a collision block with `n` vertices, use the normal representation

`V_n = spin1_SO(3) tensor Std_n_Sn`, dimension `3(n-1)`.

Frozen maximal normal derivative orders from the established forest/scaling analysis are

- K3: `omega_3 = 0`;
- K4: `omega_4 = 3`;
- K5: `omega_5 = 8`.

For each `n=3,4,5`, compute exactly

`d_{n,k} = dim Sym^k(V_n)^(SO(3) x S_n)` for `0 <= k <= omega_n`

by the same exact Laurent-character/Molien method as Iter081R, generalized from S5 to S3/S4/S5.

The K5 row is independently required to reproduce Iter081R exactly through order 8:

`(1,0,1,0,3,0,7,0,16)`.

## Frozen atlas input

Use the three Iter082F formal radial coordinate systems X/V/W and their six directed finite-jet transition maps. Required facts are re-computed independently in this gate, not assumed by labels:

1. every transition fixes the collision origin and has identity linear term;
2. each directed transition is exactly SO(3)-equivariant and S_n-equivariant because it acts by the same radial scalar law on every node;
3. pairwise inverse identities hold to the required finite order;
4. all six oriented triple-overlap cocycle identities hold through the K5 order needed for derivative order 8.

From equivariance, pullback preserves `Sym^{<=omega_n}(V_n)^(SO(3) x S_n)`. From identity linear part and formal invertibility, it preserves the normal-order filtration and induces an invertible filtered automorphism on the truncated invariant-symbol module.

## Frozen Čech gate

For each n=3,4,5 let

`J_n^inv = direct_sum_{k=0}^{omega_n} Sym^k(V_n)^(SO(3) x S_n)`.

The exact dimension is `D_n = sum_k d_{n,k}`.

The X/V/W overlaps form the complete 2-simplex nerve. For a local system with invertible transition operators satisfying the frozen triple cocycle, audit the full module, not a one-dimensional surrogate:

- construct deterministic basis-labelled 1-cocycles spanning all `D_n` invariant-symbol directions on the X→V and X→W edges;
- reconstruct a 0-cochain exactly using the transition operators/cocycle identity;
- require zero residual on all three overlaps;
- verify that adding an arbitrary globally transported vector in the full `D_n` module leaves the coboundary unchanged (global supported-jet gauge freedom);
- require no normal-order lowering;
- require all S_n block-label covariance checks.

Because an explicit polynomial invariant basis is not required to establish exactness on a contractible three-chart nerve, basis labels may index the rigorously counted invariant subspaces degree-by-degree. No claim about a preferred physical basis is permitted.

## Frozen predicates

P0. Exact Molien/character dimensions are integral and nonnegative for K3/K4/K5, and K5 reproduces Iter081R exactly.

P1. Six X/V/W maps are pairwise inverse-consistent and satisfy all oriented triple cocycles through the required finite order.

P2. The maps are source-symmetry equivariant and therefore preserve each full scalar invariant-symbol module; the induced maps are filtered automorphisms with no order lowering.

P3. Every deterministic basis-labelled full-module Čech 1-cocycle is an exact coboundary with zero overlap residual.

P4. Full-dimensional global transported gauge freedom remains: Čech solvability does not select finite parts.

P5. S3/S4/S5 block-label covariance is exact.

P6. All negative controls are rejected by the same validators:

- corrupt one triple-overlap map coefficient;
- use a singular/noninvertible transition;
- introduce explicit normal-order lowering;
- introduce an absolute preferred vertex label;
- replace the invariant dimensions by the old scalar `omega+1` surrogate and falsely declare that to be the full invariant module;
- declare global Čech gauge freedom to be a physical selector.

## Frozen outputs

If P0–P6 all pass:

`K5_FULL_SCALAR_INVARIANT_SYMBOL_CECH_DESCENT_EXACT_WITH_GLOBAL_JET_GAUGE_FREEDOM_SCOPED`

Verdict: `PASS_EXACT_SCOPED`.

If the exact representation/module cannot be defined from the frozen source-compatible data:

`K5_FULL_SCALAR_INVARIANT_SYMBOL_CECH_DESCENT_BLOCKED_OBJECT_DEFINITION`

Verdict: `BLOCKED_OBJECT_DEFINITION`.

If a scientific cocycle/covariance/filtration predicate fails with valid implementation:

`K5_FULL_SCALAR_INVARIANT_SYMBOL_CECH_DESCENT_FAIL_EXACT_SCOPED`

Verdict: `FAIL_EXACT_SCOPED`.

Implementation/control defects are `INVALID_IMPLEMENTATION` and are not scientific FAIL/BLOCKED results.

## Claim locks

A PASS would establish only algebraic finite-jet Čech descent for the complete scalar `SO(3) x S_n` invariant-symbol modules of the frozen K3/K4/K5 normal representations. It would **not** establish:

- a unique extension or physical selector;
- explicit invariant tensor basis preference;
- representation-valued/boundary-covariant coefficient-map completeness;
- actual global distributional partition-of-unity patching on `SL(2,C)^4`;
- Toller amplitude finiteness/divergence;
- regulator independence;
- G3/F9/G8/K5 promotion;
- `NEW_PHYSICS_FOUND`;
- complete quantum gravity.

Frozen scientific criteria must not be changed after production inspection.
