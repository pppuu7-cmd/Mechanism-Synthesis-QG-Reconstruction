# Iter078M adversarial preregistration — internal-edge gauge symmetry and structural Jacobian rank ceiling

**Date:** 2026-09-14

## Reviewed result

Research Iter078M-RG froze the exact fixed-all-`j=1/2` order-zero map `R_EPRL:C^32 -> C^32` implemented in `distributional/iter078h_rg_full32_orderzero_1to5.py` and searched three frozen tensors for a rank-32 Jacobian witness. Terminal run `34791083678` returned exact rank 31 at A/B/C and at the control tensor L, hence `INCONCLUSIVE_GENERIC_RANK` under the Research preregistration.

This critic audit does **not** alter that frozen Research verdict. It asks whether rank 31 follows from an exact continuous gauge symmetry of the control tensor network, in which case rank 32 is structurally impossible for this map.

## Frozen object

Use exactly the Iter078H/Iter078M map with:

- local tensor coordinates `C[e,k1,k2,k3,k4]`, dimension 32;
- five copies of the same local tensor in the 1-to-5 contraction;
- ten internal binary edge labels;
- EPRL-control internal edge metric/weight `D=diag(1,3)`;
- output external legs left untransformed;
- no Toller reference amplitude, higher spins, causal-orientation sum, or physical RG interpretation.

Unit-edge-weight mode `D=I` is a negative/independent measure control, not the physical source map.

## Hypothesis

For any `2x2` matrix `G` satisfying

`G^T D G = D`,

define `T_G C` by applying the same `G` independently to each of the four internal legs of the local rank-5 tensor while leaving the external leg unchanged.

Hypothesis:

`R_D(T_G C) = R_D(C)`

for every local tensor `C`.

Infinitesimally, with nonzero generator `X` satisfying

`X^T D + D X = 0`,

the tangent

`v_X(C) = sum_{r=1}^4 X_(r) C`

must obey

`J_R(C) v_X(C) = 0`

for every `C`. For `D=diag(1,3)` freeze

`X_EPRL = [[0,-3],[1,0]]`.

For `D=I` freeze

`X_unit = [[0,-1],[1,0]]`.

## Exact analytic proof target

Each internal edge contracts the two endpoint tensor legs with the same bilinear form `D`. Under `G` the edge contraction becomes `G^T D G`, equal to `D`. Since all ten internal edges are contracted and external legs are untouched, the complete output tensor is invariant. Differentiating at the identity gives the universal right-null tangent above.

If this proof is correct, the Jacobian determinant polynomial vanishes identically and

`rank J_R(C) <= 31`

for all `C`; hence Iter078M's rank-32 PASS target is impossible in this frozen control map.

## Frozen exact controls

Evaluate the exact null identity at the already-frozen Research tensors A/B/C/L and at one new critic control fixed before execution:

`W_i = (i+1)^3 + 2(i+1) + 7`, `i=0,...,31`.

For each lane require:

1. exact `J_R(C)` over integers/rationals;
2. exact gauge tangent `v_X(C)`;
3. `v_X(C) != 0`;
4. exact verification `J_R(C) v_X(C)=0`;
5. exact Jacobian rank recorded, but rank is only a control — the theorem is the edge-metric invariance.

Unit-weight control repeats W with `D=I` and `X_unit`.

## PASS

PASS iff the analytic edge-metric argument is valid for the implemented contraction and every frozen exact control verifies the nonzero universal tangent null identity.

Allowed critic conclusion:

`ITER078M_CRITIC_FIXED_JHALF_ORDERZERO_MAP_HAS_INTERNAL_EDGE_ORTHOGONAL_GAUGE_SYMMETRY_STRUCTURAL_JACOBIAN_RANK_LE31_EXACT_CONTROL_THEOREM`

and the Research `INCONCLUSIVE_GENERIC_RANK` result is scientifically qualified: failure to find rank 32 is explained by a structural gauge orbit, not by insufficient generic sampling.

## FAIL / INVALID

FAIL if any correctly implemented frozen control gives nonzero `Jv`, or if the edge contraction is not actually represented by the same bilinear metric at both endpoints. INVALID if code/object identity does not match Iter078H/Iter078M.

## Interpretation ceiling

This is a theorem only about the versioned fixed-all-`j=1/2` pure order-zero tensor-network control. It does not define the source-faithful causal-Toller 1-to-5 map, does not select the K5 distributional extension, does not establish a physical gauge redundancy of CRQN, and does not imply RG closure, a fixed point, regulator independence, G3, or complete quantum gravity.