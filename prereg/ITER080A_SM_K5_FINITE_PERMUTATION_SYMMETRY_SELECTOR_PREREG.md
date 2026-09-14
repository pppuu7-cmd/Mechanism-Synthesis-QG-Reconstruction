# Iter080A-SM — K5 finite-permutation symmetry versus extension-selector ambiguity

## Status
Prospectively frozen before implementation/production/result inspection.

## Scientific question
Can imposing the finite K5 vertex relabeling/permutation covariance by itself collapse the Iter077Q infinite-dimensional smooth tangential coefficient freedom to a unique (or finite-dimensional) K5 distributional extension?

## Frozen object and scope
Work only on the already controlling Iter077Q tangential ambiguity sector over the collision manifold `N = SU(2)^4` after fixing one K5 group variable. Treat K5 vertex relabelings as the finite relabeling group inherited from the five group variables, with gauge refixing after relabeling. This gate does not define the distributional extension and does not assume a regulator.

## Frozen exact witness
Set `g1 = I` and consider the gauge-invariant/relabeling-invariant continuous class function

`F(g1,...,g5) = sum_{a<b} |Tr(g_a^{-1} g_b)|^2`

restricted to `SU(2)^5 / SU(2)_left` and represented on the gauge-fixed `SU(2)^4` chart. Along the exact one-parameter family `g2 = diag(exp(i t),exp(-i t))`, `g3=g4=g5=I`, compute `F(t)` symbolically. The gate must verify that `F(t)` is nonconstant and has an interval of values. Then the invariant functions `1,F,F^2,...,F^M` must have exact full polynomial rank `M+1` for the frozen finite test set `M=12` using distinct exact values of `x=cos^2(t)`; this finite-rank ladder is a computational witness for the analytic theorem that all powers are linearly independent because a nonzero polynomial cannot vanish on an interval.

## Frozen lanes
A. Derive exact `F(t)` as an affine function of `x=cos^2(t)` and verify nonconstancy.
B. Verify permutation invariance algebraically from the unordered pair sum and common-left gauge invariance from trace cyclicity/cancellation.
C. For `M=12`, build the exact evaluation matrix of `1,F,...,F^M` at 13 distinct rational `x` values in `[0,1]` and require exact rank 13.
D. Interpretation control: finite-group covariance alone can at most restrict to the invariant smooth subspace; because the displayed invariant powers are linearly independent for arbitrary degree, that invariant subspace remains infinite-dimensional. No uniqueness, finiteness, regulator-independence, or physical extension is inferred.

## Frozen classifications
1. `ITER080A_SM_FINITE_K5_PERMUTATION_COVARIANCE_LEAVES_INFINITE_DIMENSIONAL_TANGENTIAL_EXTENSION_AMBIGUITY_EXACT_SCOPED`
   iff A+B+C+D all pass.
2. `ITER080A_SM_INVARIANT_FUNCTION_WITNESS_FAILED_INVALID`
   if any exact algebra/rank/invariance control fails.

## Scope ceiling
A PASS only proves that finite K5 relabeling covariance by itself cannot be the missing Iter077Q selector. It does not exclude stronger analytic, positivity, causality, locality, composition, or source-defined selection principles; it does not promote K5/F9/G3/G8 or constitute new physics.
