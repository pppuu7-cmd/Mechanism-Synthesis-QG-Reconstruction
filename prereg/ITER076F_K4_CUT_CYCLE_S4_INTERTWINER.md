# Iter076F preregistration — K4 cut/cycle S4 intertwiner audit

Date: 2026-09-13

## Motivation

Iter076E established prospectively that the natural linearized source-relative carrier is incidence/cut-space data whereas the validated reduced K4 constrained-flow object is cycle-space data. At K4 both spaces are three-dimensional but intersect trivially in the frozen edge pairing. Equal dimension therefore does not define the missing P3 source-to-K4 map.

Before introducing any source-to-K4 projection, test the exact S4 representation content of the two 3D spaces. This is a structural gate only.

## Frozen objects

Use K4 vertices `{0,1,2,3}` and the six canonically oriented edges `(i,j)` with `i<j`. Let `B` be the exact signed vertex-edge incidence matrix. Define:

- cut space `C = im(B^T)`;
- cycle space `Z = ker(B)`;
- the S4 edge action by permuting vertices and including the forced sign when the image edge must be reoriented back to canonical `i<j` orientation.

No fitted metric, preferred tree, source coefficient, or physical pushforward may be inserted.

## Frozen lanes

### Lane A — exact representation census

For all 24 vertex permutations:

1. verify `dim C = dim Z = 3` and `C ∩ Z = {0}`;
2. verify both spaces are invariant under the canonical oriented-edge S4 action;
3. compute exact representation characters by conjugacy class.

Frozen expected character comparison is diagnostic, not assumed as PASS: cut should be tested against the standard 3D character and cycle against its orientation/sign twist.

### Lane B — exact intertwiner dimensions

Solve exact linear systems for `X: C -> Z`:

- untwisted: `Z_g X = X C_g` for every `g in S4`;
- sign-twisted: `Z_g X = sgn(g) X C_g` for every `g in S4`.

Frozen primary predicates:

- untwisted intertwiner-space dimension is exactly 0;
- sign-twisted intertwiner-space dimension is exactly 1.

### Lane C — constructive twisted generator

If Lane B gives a one-dimensional twisted space, choose its deterministic primitive rational/integer generator by first-nonzero normalization. Frozen predicates:

- generator determinant is nonzero;
- twisted covariance holds exactly for all 24 permutations;
- ordinary untwisted covariance fails for at least one odd permutation;
- the generator therefore provides only an orientation/sign-twisted algebraic cut↔cycle isomorphism.

This generator is **not** automatically the physical P3 map.

### Lane D — basis covariance and negative controls

Repeat the intertwiner-dimension calculation under a frozen set of exact unimodular basis changes in cut and cycle coordinates. Require dimensions `(0,1)` to remain unchanged. Negative controls must reject:

- dropping the canonical edge-reorientation sign;
- treating the twisted generator as an ordinary S4 intertwiner.

## Frozen terminal classification

Only if all lanes are valid and all primary predicates pass:

`ITER076F_K4_CUT_CYCLE_INTERTWINER_REQUIRES_ORIENTATION_SIGN_TWIST_EXACT_SCOPED`

If exact computations execute correctly but any frozen primary predicate fails:

`ITER076F_FROZEN_PREDICATE_FAIL`

If a technical/symbolic implementation failure prevents evaluation, classify infrastructure/numerical invalid and repair only the first causal technical defect without changing this preregistration.

## Scope guards

Even a full PASS establishes only the S4 representation-theoretic structure of the reduced K4 cut/cycle spaces. It does not establish that the sign-twisted algebraic generator is the source-derived P3 pushforward. It does not define P4 numerator×Haar/Jacobian data, face coefficients, the nominal `epsilon^-1` coefficient, a causal-vertex finiteness/divergence theorem, physical sector selection, G3, F9, G8, K5, `NEW_PHYSICS_FOUND`, or a complete quantum-gravity theory.
