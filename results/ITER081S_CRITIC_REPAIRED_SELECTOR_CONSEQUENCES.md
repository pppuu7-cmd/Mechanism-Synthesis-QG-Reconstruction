# Iter081S Critic repaired selector consequences after right-SU(2) source-lock correction

Date: 2026-09-14
Status: **EXACT COROLLARIES FROM ITER081R; SUPERSEDES USE OF HISTORICAL INFINITE W FOR THESE QUESTIONS**

## Repaired ambiguity object
Iter081R establishes a 28-dimensional source-symmetry-compatible **scalar invariant normal-jet subspace** `J_inv` through total normal order 8 in the frozen all-`j=1/2` K5 common-collision sector:

`dim J_inv = 28`,

with graded dimensions

`(1,0,1,0,3,0,7,0,16)`.

This is a lower bound on the complete extension space, not an assertion that the full physical ambiguity is exactly 28-dimensional.

Historical Iter077Q's tangential `W=span{Q^n F delta_N}` is not source-compatible and must not be used as the physical object.

## Consequence A — S5/permutation covariance still does not select
Iter081R has already imposed the full `S5` vertex-relabeling symmetry in addition to the corrected node-wise compact gauge symmetry. Nevertheless `dim J_inv=28>1`.

Therefore finite K5 permutation/S5 covariance is **not** a unique extension selector in the repaired physical source scope.

This repairs the qualitative conclusion of historical Iter080A without its invalid nonconstant tangential multiplier. The historical Iter080A claim of an infinite-dimensional S5-invariant tangential sector is upstream-source-lock invalid; the corrected result is the finite lower bound `>=28` in this scalar jet sector.

## Consequence B — ordinary support + conormal/WF admissibility still does not select
Each normal derivative of `delta_N` is supported on `N` and has wavefront set contained in the conormal bundle `N^*N\0`. Finite linear combinations and multiplication by the smooth compact boundary functional do not enlarge this wavefront-set containment.

Every one of the 28 invariant scalar normal-jet directions counted by Iter081R therefore obeys the weak standalone condition

`supp(u) subset N`, `WF(u) subset N^*N\0`.

Hence ordinary support plus conormal/WF admissibility leaves at least a 28-dimensional source-compatible scalar ambiguity and cannot uniquely select the K5 extension.

This **repairs** the qualitative conclusion of Iter080J. Historical Iter080J's particular `Q^n F delta_N` witness family is not source-compatible, but its selector-class conclusion survives with the corrected invariant normal jets.

## Consequence C — finite scalar-linear conditions have a corrected threshold
Let

`L:J_inv -> C^m`

be any complex-linear family of `m` scalar conditions on the repaired 28-dimensional subspace. Rank-nullity gives

`dim ker L >= 28-m`.

Therefore:

- if `m<28`, no such family can uniquely select the extension even on `J_inv`;
- if `m=28`, injectivity is algebraically possible if the conditions have full rank;
- if `m>28`, finite dimensionality alone gives no obstruction to injectivity.

Thus historical Iter080D's universal statement

`every fixed finite family of scalar-linear conditions has infinite-dimensional kernel`

is **not applicable** after the right-SU(2) repair. Its conditional rank-nullity theorem on the old infinite vector space is mathematically correct, but the physical premise is source-lock invalid.

The repaired theorem is only:

`m<28 => dim ker(L|J_inv) >= 28-m >0`.

Any proposal with `m>=28` still needs independent physical/source motivation, actual rank proof, normalization consistency and action on the complete extension space; Iter081R does not provide such a selector.

## Consequence D — causal orientation summation does not remove the repaired ambiguity
Iter081H/K establish that source-defined proper-causal orientation sums retain transverse scaling degree 20 and do not cancel the common-collision leading singularity. Orientation summation fixes only an off-collision finite linear combination of Toller products.

Every element of `J_inv` is supported exactly on `N`; hence adding it to an extension leaves the off-collision causal sum unchanged. The node-wise compact gauge symmetry and S5 symmetry used to construct `J_inv` are compatible with the globally summed causal object.

Therefore the eta=+ causal sum, and likewise the sum of both proper causal signature sectors, retains **at least the same 28-dimensional scalar invariant normal-jet ambiguity** in the frozen minimal sector.

This repairs the qualitative content of historical Iter081I while invalidating its claim of an infinite-dimensional surviving tangential `W`.

## Consequence E — current local amplitude remains nonunique
The local CRQN v0.2 K5 amplitude remains blocked, now for a corrected reason:

- source-ordered off-collision object is non-L1 at the common collision (Iter077I; causal sums Iter081H/K);
- the old infinite tangential ambiguity is invalid;
- exact source symmetries still leave a demonstrated 28-dimensional scalar invariant normal-jet lower bound (Iter081R);
- no validated source/candidate prescription has yet been shown to fix those jet coefficients.

Therefore `BLOCKED_CURRENT_CANDIDATE_LOCAL_AMPLITUDE` survives, but historical Iter080I's **infinite-dimensional dependency justification** is superseded by the Iter081R/S repair.

## Consequence F — source audits
Repaired Iter080E's narrow source statement remains useful only after qualification: the audited BCG/Beltran corpus did not supply an explicit correlated joint-K5 extension/boundary-value prescription satisfying its P1-P5 completeness conditions. Its reference to acting on the old full `W` is obsolete, but no source-defined prescription has appeared that fixes the corrected invariant jet coefficients either.

Iter080H's exhaustive pre-Iter077Q CRQN candidate-corpus census targeted A2/A3 predicates defined explicitly against the old infinite `W`. It therefore cannot be promoted unchanged to a theorem about the repaired jet space. A corrected pre-existing-axiom selector census, if needed, requires a new prospectively frozen gate with `J_inv`/normal-jet reach as the target.

## Corrected blocker
Replace

`FUNCTION_SPACE_K5_DISTRIBUTIONAL_EXTENSION_SELECTOR`

when it specifically means the invalid infinite tangential `W`, by

`RIGHT_SU2_COVARIANT_K5_INVARIANT_NORMAL_JET_COEFFICIENT_SELECTOR`.

The demonstrated scalar target contains at least 28 independent coefficients through order 8 in the frozen minimal sector.

## Claim ceiling
No assertion is made that the total physical extension space has exactly dimension 28, that 28 conditions are sufficient physically, or that no source-derived selector can exist. No causal-vertex divergence/nonexistence, generic-spin full-boundary theorem, regulator independence, G3/F9/G8/K5 promotion, `NEW_PHYSICS_FOUND`, or complete-QG claim follows.
