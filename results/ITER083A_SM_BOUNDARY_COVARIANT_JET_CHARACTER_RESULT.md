# Iter083A-SM — exact boundary-covariant K5 invariant normal-symbol character classification

Date: 2026-09-15

Status: **PASS_EXACT_SCOPED**

## Prospective provenance

- preregistration: `prereg/ITER083A_SM_BOUNDARY_COVARIANT_JET_CHARACTER_VALIDATION.md`, commit `38abc8bfbc78fe07e56a4f29a09733925e96d9b2`;
- implementation: `scripts/iter083a_boundary_covariant_jet_character_validation.py`, commit `1447c9412de9bea91ce5ed3be8f15f096b3fc27d`;
- initial workflow commit: `7aa1f859de9fd7b2b9138b7b36cefb12aa07779c`;
- first post-registration marker: `fb98eb35ffd0a51cdefde53e3f03c57f3145bbb2`;
- historical run `34908559463` remained stale queued and is not used as scientific authority;
- workflow-only retrigger, no scientific change: commit `f0c0996192fabe049a497924a7d26a7e4883a970`;
- authoritative GitHub Actions run: `34910602967`, terminal `success`;
- authoritative job: `104197010950`, terminal `success`;
- artifact: `10374461752`, `iter083a-boundary-covariant-character-validation`;
- artifact ZIP digest: `sha256:da52890c29d86fc5d246c074e26fd670b5a860a635bdbf654042690637bcd973`;
- production JSON SHA256: `65e99a1011723848f53451c967fbd1d1af8c77580da5fa562427c5695ec16394`.

The retrigger changed only a workflow comment documenting the stale run. The preregistered object, implementation, predicates and controls were unchanged.

## Classification

`K5_BOUNDARY_COVARIANT_INVARIANT_NORMAL_SYMBOL_CHARACTER_CLASSIFICATION_EXACT_SCOPED`

Verdict: **`PASS_EXACT_SCOPED`**.

## Frozen object

For the all-`j=1/2` K5 boundary,

`H_boundary = tensor_(a=1)^5 Inv_SU2[(V_1/2)^tensor4]`,

so

`dim_C H_boundary = 2^5 = 32`.

The normal representation inherited from Iter081R is

`V = spin1_SO(3) tensor Std5_S5`, `dim_R V=12`.

For each normal order `k`, define

`M_k = (Sym^k V)^SO(3)`.

Iter081R supplies the exact residual S5 character of `M_k` through `k=8`.

Iter083A computes

`m_k = dim (H_boundary^* tensor M_k)^S5`

by exact character pairing.

## First-principles boundary representation

No boundary character was inserted by name. The implementation builds the exact four-spin singlet projector in `(C^2)^tensor4`,

`P0 = ((J^2-2 I)(J^2-6 I))/12`,

checks `P0^2=P0`, rank two, and exact commutation with all 24 leg permutations, then derives the local S4 traces from the projector itself.

The canonical K5 relabeling action is then reconstructed for all 120 vertex permutations, including the induced permutations of the four incident legs at every vertex.

The resulting S5 boundary character on cycle types

`(1^5), (2,1^3), (2^2,1), (3,1^2), (3,2), (4,1), (5)`

is exactly

`chi_boundary = (32,0,8,2,0,0,2)`.

Its exact irreducible decomposition is

`2[5] + [4,1] + 2[3,2] + 2[2,2,1] + [2,1,1,1] + 2[1^5]`.

All multiplicities are nonnegative integers and the dimensions sum to 32. The character norm is 18.

## Exact normal-symbol multiplicities

Direct S5 class pairing gives

`m_0..m_8 = (2,0,5,1,22,10,72,48,217)`.

An independent decomposition of every `M_k` into ordinary S5 irreducibles gives the identical sequence degree by degree.

Therefore the cumulative boundary-covariant graded normal-symbol dimension through the source scaling-degree ceiling is

`2+0+5+1+22+10+72+48+217 = 377`.

## New representation-valued channels

The authoritative scalar Iter081R sequence is

`d_0..d_8 = (1,0,1,0,3,0,7,0,16)`.

In particular, scalar odd orders vanish. Iter083A instead finds

- `m_3=1`;
- `m_5=10`;
- `m_7=48`.

Thus true boundary covariance opens representation-valued odd normal-symbol channels that the scalar invariant sector cannot see.

## Exact controls

All preregistered predicates P0-P7 passed in production.

All six negative controls passed:

- arbitrary rank-two coordinate projector rejected;
- vertex-only action that suppresses induced incident-leg permutations rejected;
- corrupted Iter081R class row rejected;
- unweighted character inner product rejected;
- substitution of scalar dimensions for boundary-covariant multiplicities rejected;
- non-class-constant boundary trace table rejected.

The global S5 sign twist leaves the final pairings unchanged, as required by the frozen orientation-convention robustness control.

## Scientific meaning

This closes the previously open **representation-valued boundary-covariant graded normal-symbol classification** in the frozen all-`j=1/2` common-collision sector.

The number 377 in this file is a graded-symbol count. Promotion to the exact dimension of the full filtered supported extension-difference space requires the separate Iter083B exactness theorem; that theorem is not replaced by this character computation.

## Interpretation ceiling

This result alone does not select a normal-coordinate splitting, connection, finite part, boundary value, regulator or physical coefficient tuple. It does not establish global patching across every collision stratum, generic-spin completeness, causal-vertex divergence/nonexistence, regulator independence, multivertex closure, G3/F9/G8/K5 promotion, `NEW_PHYSICS_FOUND`, or complete quantum gravity.
