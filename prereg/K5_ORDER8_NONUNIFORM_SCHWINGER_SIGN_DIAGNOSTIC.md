# K5 order-8 nonuniform Schwinger sign diagnostic — frozen before evaluation

Date: 2026-09-15
Parent scientific contract: `prereg/ACTUAL_SOURCE_ORDERED_MULTIVARIATE_POLAR_NORMAL_JET_ANNIHILATOR_K5_LANE.md`, commit `7466325187f22043d1794379fd6e6dcf62e05abd`.
Parent exact reduction result: commit `7cd6c11b6ac7fb32ebc9fc06086f22efc278d5aa`.
Parent uniform diagnostic result: commit `9ba9ed9e1f6bed4af3dbd03864f4867b117c99c9`.

## Purpose

Test the cheapest remaining rigorous noncancellation route before attempting a full 9-simplex period proof: determine whether the actual order-eight radial-probe Gaussian moment for the fixed stripped boundary component `k=(0,0,0,0,0)` keeps one sign at a frozen set of positive rational Schwinger points or already exhibits an exact sign change.

This is a diagnostic only. It does not alter the frozen K5 zero/nonzero criterion and cannot by itself assign a K5 residue verdict.

## Exact object

Use the authoritative ten K5 edges in the frozen order

`(01),(02),(03),(04),(12),(13),(14),(23),(24),(34)`.

For positive Schwinger weights `alpha_e`, form the reduced weighted K5 Laplacian

`L(alpha)=sum_e alpha_e r_e r_e^T`

in the same four-coordinate translation gauge as the validated Schwinger reduction. Let

`Q = L(1,...,1)/5`,

so `x^T Q x = R_K5^2` for one Cartesian component.

For the actual leading source numerator `N10^(00000)`, define the zero-equivalent unnormalized Gaussian function

`J(s)=det(L(alpha)+s Q)^(-3/2) * Wick[N10^(00000); (L(alpha)+s Q)^(-1)]`.

The fourth derivative at zero is a positive common multiple of the actual radial-probe moment with insertion `(R_K5^2)^4`. Therefore its sign/zero status is the sign/zero status used in this diagnostic. Compute it by exact truncated rational series through order four; no floating point and no numerical differentiation are allowed.

The full source contraction for `k=(0,0,0,0,0)` must use all `4^5=1024` node-tensor choice terms from `distributional/iter077i_sm_source_ordered_jhalf_k5_l1.py`. All 945 Wick pairings are retained at nonuniform points; no uniform-point sparsity shortcut may be assumed.

## Frozen positive rational points

The following weight vectors are frozen before evaluation, in the edge order above:

1. `uniform = (1,1,1,1,1,1,1,1,1,1)` — reproduction control only.
2. `ascending = (1,2,3,4,5,6,7,8,9,10)`.
3. `descending = (10,9,8,7,6,5,4,3,2,1)`.
4. `edge01_heavy = (16,1,1,1,1,1,1,1,1,1)`.
5. `edge01_light = (1/16,1,1,1,1,1,1,1,1,1)`.
6. `star0_heavy = (8,8,8,8,1,1,1,1,1,1)`.
7. `star0_light = (1,1,1,1,8,8,8,8,8,8)`.
8. `mixed = (1,2,5,3,7,4,11,6,13,8)`.

## Frozen checks

- exact weighted Laplacian is positive definite at every frozen point;
- uniform point reproduces the prior sign/nonzero status for `k=(0,0,0,0,0)`;
- all 1024 source node-choice terms are included;
- all 945 Wick pairings are allowed by the algorithm at nonuniform points;
- imaginary part of the final exact radial moment is recorded, not assumed zero;
- no K5 scientific zero/nonzero verdict is assigned by this diagnostic.

## Frozen interpretation

If at least two frozen points have opposite nonzero real signs while the exact imaginary parts vanish, classify the simple pointwise sign-definite route for this boundary component as

`K5_00000_POINTWISE_SIGN_CERTIFICATE_FALSIFIED_BY_EXACT_NONUNIFORM_WITNESS`.

If any exact imaginary part is nonzero, classify the real-sign route as inapplicable and continue with invariant-dual/complex noncancellation methods.

If all frozen values are real, nonzero, and have one sign, classify only

`K5_00000_FROZEN_SIGN_DIAGNOSTIC_SURVIVES_SCOPED`

and proceed to symbolic factorization or a genuine global positivity proof. Finite sampling never proves global sign-definiteness.

## Claim lock

No point sample or finite set of point samples proves the projective period nonzero. No K5 residue verdict, finite-part selector, regulator-independence result, physical amplitude, F9/G3 promotion, or new-physics claim follows from this diagnostic.
