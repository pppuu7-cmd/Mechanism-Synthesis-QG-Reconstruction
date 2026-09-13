# Iter076H preregistration — canonical tetrahedral Hodge star vs Iter076F twisted generator

Date: 2026-09-13

## Frozen objective

Iter076F established that the exact K4 cut-to-cycle S4 intertwiner space is zero untwisted and one-dimensional after the sign character; Iter076G independently established that the equal-spin source wedge-reversal parity character equals that required sign character. The remaining matrix-valued P3 pushforward is not source-derived.

Before attempting any physical identification, test a canonical, non-fitted algebraic candidate: the orientation-defined tetrahedral Hodge complement on the six oriented K4 edges. For canonical edge `(i,j)`, `i<j`, let `{k,l}` be the complementary vertex pair with `k<l`, and define

`H e_ij = eps(i,j,k,l) e_kl`,

where `eps(0,1,2,3)=+1` and `eps` is the permutation sign. This definition is frozen before evaluating its relation to the Iter076F generator.

## Frozen lanes

A — construct the 6x6 integer matrix `H` directly from the complement/orientation rule. Require exactly: one nonzero `±1` per row/column, `H^T H=I`, `H^2=I`, `H(CUT)=CYCLE`, `H(CYCLE)=CUT`, with exact rank three on each restricted map.

B — in the exact CUT/CYCLE bases used by Iter076F, compute the coordinate matrix `X_H` defined by `CYCLE X_H = H CUT`. Independently recompute the full twisted-intertwiner linear system over all 24 permutations and its primitive unique generator `X_F`. Require twisted-Hom dimension exactly one and `X_H = X_F` or `X_H = -X_F` with no fitted entries or basis adjustment.

C — require exact orientation covariance over all 24 permutations:

`H R(p) = sgn(p) R(p) H`

for the signed canonical edge action `R(p)`. Also require exact composition consistency over all 24x24 ordered permutation pairs.

D — negative controls. An orientation-blind complementary-edge map with all complement signs `+1` must fail the twisted covariance gate. At least one deliberately flipped complement sign must fail either involution/cut-cycle transport/covariance. No control matrix may be re-fit after evaluation.

## Frozen terminal classifications

All lanes valid and all predicates PASS =>
`ITER076H_CANONICAL_TETRAHEDRAL_HODGE_STAR_REALIZES_UNIQUE_K4_TWISTED_GENERATOR_EXACT_SCOPED`.

Any exact scientific predicate mismatch with valid implementation =>
`ITER076H_CANONICAL_HODGE_IDENTIFICATION_FAILS_FROZEN_GATE`.

Technical/runtime/dependency failure => infrastructure/implementation invalid only.

## Interpretation and claim locks

PASS would establish a canonical orientation-defined algebraic realization of the unique Iter076F sign-twisted cut-to-cycle generator. It would not establish that the Toller/EPRL source physically selects this Hodge dualization, nor the full branch/magnetic-index P3 map, numerator/Haar/Jacobian jets, face coefficients, nominal `epsilon^-1` coefficient, correlated boundary value, K5, G3, F9, G8, new physics, or complete quantum gravity.

The next physics-critical gate after PASS must test source provenance of this Hodge/complement map from the actual wedge-reversal plus magnetic-index transport; no physical P3 promotion is allowed merely because the algebra closes.