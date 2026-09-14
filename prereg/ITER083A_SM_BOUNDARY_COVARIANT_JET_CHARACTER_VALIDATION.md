# Iter083A-SM preregistration — boundary-covariant K5 invariant normal-symbol character validation

Date: 2026-09-15

## Status and provenance discipline

This is a **prospective confirmation/validation gate after an exploratory derivation**. The exploratory calculation is not production authority and already suggested concrete character and multiplicity values. This preregistration therefore does not claim blinded discovery. Its purpose is to require an independent first-principles reconstruction, exact representation-theory cross-checks, and mechanically failing negative controls before any scoped scientific promotion.

## Motivation and dependency lock

Authoritative Iter082H closes the algebraic Cech blocker only for complete **scalar** `SO(3) x S_n` invariant-symbol modules and explicitly does not establish completeness for representation-valued or boundary-covariant coefficient maps.

The corrected source object is a boundary linear functional. In the frozen all-`j=1/2` K5 sector its boundary Hilbert space is

`H_boundary = tensor_{a=1}^5 Inv_SU2[(V_{1/2})^tensor4]`,

with dimension `2^5 = 32`.

The exact node-wise right-SU2 source lock and Iter081R identify the K5 normal representation

`V = spin1_SO(3) tensor Std5_S5`, `dim V = 12`,

with normal derivative orders through `k=8` allowed by the frozen scaling-degree bound.

Frozen authorities:

- `status/CURRENT.md` at `20c916ad68ff36faa57199a33f536d402d22ea98`;
- right-SU2 source-lock review `c0ae0ef208a3eccef4ece7960cdf5337e7d5fa2e`;
- Iter081R result `5fe42e766aab2660b36c654502a029930db28890`;
- Iter081R raw character rows `results/raw/iter081r_sm_invariant_jets.json`, durable commit `48674739d726f96aad68466cf230b5f1fe061f96`;
- Bianchi-Chen-Gamonal causal vertex arXiv:2601.23162v1, especially the boundary-linear vertex definition and five SU(2)-intertwiner boundary data;
- Bianchi-Chen-Gamonal Toller matrices arXiv:2604.24945v1, especially the Cartan/Wigner-factor formula giving exact compact left/right covariance.

No later exploratory numerical value may replace these inputs.

## Frozen object

Let

`M_k = (Sym^k V)^SO(3)`

with its residual `S5` action. Iter081R supplies the exact class character of `M_k` for `0 <= k <= 8`.

Let `H_boundary` carry the canonical `S5` relabeling action induced by relabeling the five K5 vertices and their incident spin-1/2 half-edges. At one vertex the local factor

`Inv_SU2[(V_{1/2})^tensor4]`

is the two-dimensional four-spin singlet space. Its leg-permutation action must be derived from the actual four-spin tensor space; it may not be inserted by naming an `S4` irrep alone.

The boundary-covariant graded normal-symbol multiplicity is

`m_k = dim (H_boundary^* tensor M_k)^S5`

or equivalently the exact `S5` character pairing

`m_k = (1/120) sum_C |C| conj(chi_H(C)) chi_Mk(C)`.

This gate classifies this **local graded principal-symbol space only**. It does not yet prove global distributional patching or coefficient transport across the physical atlas.

## Lane A — first-principles local singlet projector

Construct `(C^2)^tensor4` exactly in the computational basis.

1. Build total spin `J^2` with exact rational entries.
2. Construct the spin-zero projector as the spectral polynomial

`P0 = ((J^2 - 2 I)(J^2 - 6 I))/12`.

3. Require `P0^2=P0`, `rank(P0)=2`, and exact commutation with all 24 leg permutations.
4. For every `pi in S4`, compute `tr(P0 U_pi)`. Require class constancy and recover the complete local singlet permutation character from the projector itself.

No hard-coded local character row is accepted as Lane A authority.

## Lane B — full K5 boundary character

For every one of the 120 permutations `sigma in S5`, compute the trace on `H_boundary` by contracting the Lane-A local permutation maps around each cycle of the vertex permutation. Equivalently, for a vertex cycle of length `ell`, the cycle contribution is the local-singlet trace of `sigma^ell` acting on the four neighbors of a representative vertex.

Requirements:

- all 120 values depend only on `S5` cycle type;
- the identity trace is exactly `32`;
- the resulting character decomposes into ordinary `S5` irreducibles with nonnegative integer multiplicities and total dimension `32`;
- the character norm is an integer;
- multiplying by the `S5` sign character is an orientation-convention robustness check. Any global sign twist induced by a different consistent epsilon/dual convention must leave all multiplicities `m_k` unchanged.

## Lane C — frozen Iter081R pairing

Read the durable Iter081R raw JSON and require its frozen scientific fields:

- normal fiber `spin1_SU2 tensor Std5_S5`;
- class sizes summing to 120;
- seven cycle types;
- scalar invariant dimensions `(1,0,1,0,3,0,7,0,16)`;
- exact per-class `su2_singlet_multiplicity_by_degree` rows.

Compute `m_k` directly from the class inner product for every `0<=k<=8`.

Independently generate the ordinary `S5` irreducible character table and decompose both `H_boundary` and each `M_k`; recompute

`m_k = sum_lambda mult_H(lambda) mult_Mk(lambda)`.

Direct class pairing and irrep-decomposition pairing must agree exactly degree by degree.

## Exploratory values frozen only as replication targets

The pre-prereg exploratory derivation suggested

`chi_H = (32,0,8,2,0,0,2)`

on cycle types

`(1^5), (2,1^3), (2^2,1), (3,1^2), (3,2), (4,1), (5)`,

and

`m_0..m_8 = (2,0,5,1,22,10,72,48,217)`,

with cumulative dimension `377`.

These values are **not** accepted merely because the implementation reproduces literals. They must emerge independently from Lanes A-C and all controls below. A scientifically valid mismatch is a `FAIL_EXACT_SCOPED`, not something to patch toward the exploratory target.

## Frozen predicates

P0. All frozen source/provenance inputs are present and the Iter081R raw row structure passes its own integrity checks.

P1. The first-principles four-spin singlet projector is exact, rank 2, permutation invariant, and yields a class-constant local `S4` character.

P2. All 120 K5 vertex relabelings give a class-constant boundary character with identity trace 32.

P3. The boundary character has an exact nonnegative integral `S5` irrep decomposition of total dimension 32.

P4. Global sign twisting leaves the final boundary character pairings `m_k` unchanged.

P5. Direct class pairing and independent irrep-decomposition pairing agree exactly for all degrees 0..8; all `m_k` are nonnegative integers.

P6. The calculation explicitly reports whether representation-valued boundary covariance opens normal orders absent in the scalar invariant sector; no parity conclusion may be assumed in advance.

P7. Negative controls are mechanically rejected by the same validators:

- replace the true four-spin singlet projector by an arbitrary rank-2 coordinate projector;
- permute only the five vertex tensor factors while suppressing induced incident-leg permutations;
- corrupt one nonidentity Iter081R class row;
- omit conjugacy-class weights in the character inner product;
- substitute scalar invariant dimensions `d_k` for boundary-covariant multiplicities `m_k`;
- force a non-class-constant boundary trace table.

A hard-coded boolean such as `rejected = ... or True` invalidates the implementation.

## Frozen outputs

If P0-P7 all pass and the two independent pairing lanes agree:

`K5_BOUNDARY_COVARIANT_INVARIANT_NORMAL_SYMBOL_CHARACTER_CLASSIFICATION_EXACT_SCOPED`

Verdict: `PASS_EXACT_SCOPED`.

If the canonical boundary relabeling representation cannot be defined from the frozen source object without an additional non-source convention that changes the character pairing:

`K5_BOUNDARY_COVARIANT_NORMAL_SYMBOL_CLASSIFICATION_BLOCKED_OBJECT_DEFINITION`

Verdict: `BLOCKED_OBJECT_DEFINITION`.

If a valid first-principles reconstruction disagrees with the exploratory values or fails an exact representation-theory predicate:

`K5_BOUNDARY_COVARIANT_NORMAL_SYMBOL_CLASSIFICATION_FAIL_EXACT_SCOPED`

Verdict: `FAIL_EXACT_SCOPED`.

Implementation defects are `INVALID_IMPLEMENTATION` and are not scientific FAIL/BLOCKED outcomes.

## Interpretation ceiling

Even a PASS establishes only the exact local source-symmetry-compatible **boundary-covariant graded normal-symbol multiplicities** in the frozen all-`j=1/2` K5 common-collision sector. It does not establish:

- the exact total physical extension-space dimension;
- a globally split jet bundle or preferred coefficient basis;
- actual distributional partition-of-unity patching on `SL(2,C)^4`;
- boundary coefficient pullback/pushforward/Jacobian laws across all nonlinear charts;
- a finite-part, boundary-value, or coefficient selector;
- uniqueness of the K5 extension;
- causal-vertex finiteness/divergence;
- regulator independence;
- generic-spin completeness;
- G3/F9/G8/K5 promotion;
- `NEW_PHYSICS_FOUND`;
- complete quantum gravity.

Frozen scientific criteria must not be changed after production inspection.