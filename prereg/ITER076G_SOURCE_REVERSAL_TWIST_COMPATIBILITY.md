# Iter076G preregistration — source reversal character vs required K4 S4 twist

Date: 2026-09-13

## Frozen objective

Iter076F established an exact algebraic fact: the K4 cut-to-cycle intertwiner is absent in the untwisted S4 representation and one-dimensional only after multiplication by `sgn(g)`. Iter059 independently derived, from the causal-EPRL/Toller source in the equal-spin wedge sector, that reversing a wedge order (`g_b^-1 g_a -> g_a^-1 g_b`) swaps the `T+`/`T-` branches and transposes/conjugates magnetic indices.

Test whether the **orientation character only** forced by source wedge-order reversal agrees exactly with the sign twist required by Iter076F. This gate must not identify the algebraic intertwiner with the physical P3 pushforward.

## Frozen objects

Use K4 vertices `{0,1,2,3}` and canonical edges `(i,j), i<j`. For every `p in S4`, count `Nrev(p)`: the number of canonical edges whose endpoint order is reversed by `p`. Define the source reversal parity character

`chi_source(p) = (-1)^Nrev(p)`.

Define the Iter076F required algebraic twist

`chi_required(p) = sgn(p)`.

The use of `chi_source` is scoped to the equal-spin causal-wedge reversal law of Iter059: each edge-order reversal is a branch swap. No unequal-spin Toller inversion law is assumed.

## Frozen lanes

A — enumerate all 24 permutations; require exact `chi_source(p)=sgn(p)` for all 24 and exactly 12 odd / 12 even cases.

B — composition/cocycle control over all 24x24 ordered pairs: require `chi_source(p∘q)=chi_source(p)chi_source(q)` exactly and verify canonical edge-reorientation bookkeeping under composition.

C — compare the source reversal character to the Iter076F required twist for all 24 elements; require 24/24 equality. This is character-level compatibility only.

D — negative controls: an orientation-blind character `chi=+1` must fail on all 12 odd permutations; dropping edge reorientation must not reproduce the required character on the full group. No fitted sign rule is allowed.

## Frozen terminal classification

All lanes valid and all predicates PASS =>
`ITER076G_EQUAL_SPIN_SOURCE_REVERSAL_CHARACTER_MATCHES_REQUIRED_S4_TWIST_EXACT_SCOPED`.

Exact mismatch =>
`ITER076G_SOURCE_REVERSAL_CHARACTER_INCOMPATIBLE_WITH_REQUIRED_TWIST`.

Technical failure => infrastructure/implementation invalid only.

## Scope guards

A PASS establishes only that the **one-dimensional orientation character** required algebraically by Iter076F is consistent with the parity of source-backed equal-spin wedge-order reversals. It does not determine the matrix-valued P3 pushforward, local branch/magnetic-index map, numerator/Haar/Jacobian jets, face coefficients, `epsilon^-1` coefficient, correlated boundary value, K5, G3, F9, G8, new physics, or complete quantum gravity.