# Iter078N adversarial review — exact internal-edge gauge symmetry explains the rank-31 control-map defect

**Date:** 2026-09-14

## Result reviewed

Latest terminal substantive Researcher result available before this review:

- preregistration: `prereg/ITER078N_RG_UNIVERSAL_OUTPUT_HYPERPLANE.md`, commit `03db4f6400ab04ade810972f6d5eaf929abe489b`;
- implementation: `distributional/iter078n_rg_universal_output_hyperplane.py`, commit `7856e1cda12ae4616f2990c95968703411b7e395`;
- terminal run: `34791220947`;
- durable result: `results/ITER078N_RG_UNIVERSAL_OUTPUT_HYPERPLANE_RESULT.md`, commit `0f5acf6cba788e95b3bfa7fa51f9e5729f43e6dd`;
- Research classification: `ITER078N_RG_NO_COMMON_LEFT_NULL_ACROSS_FROZEN_RANK31_POINTS`;
- Research verdict: `INCONCLUSIVE_STRUCTURAL_RANK`.

The Research result is correct in its exact frozen scope: the primitive **left** null vectors of the rank-31 Jacobians at A/B/C/L are not one common proportional vector, so the repeated defect is not explained by one fixed linear output hyperplane.

## Adversarial theorem found

The frozen Iter078H/Iter078M control map has a different, exact **input-space** redundancy.

The map is a five-copy rank-5 tensor network with local tensor

`C[e,k1,k2,k3,k4] in C^32`,

where `e` is the external binary leg and the four `k` legs are internal. Every internal K5 edge contracts the two endpoint legs with the same bilinear edge metric. In the EPRL-edge-weight control this metric is

`D = diag(1,3)`.

Let a common `2x2` matrix `G` act on each of the four internal legs of every local tensor, leaving the external leg untouched. If

`G^T D G = D`,

then every internal edge contraction is unchanged, hence the complete coarse tensor obeys the exact identity

`R_D(T_G C) = R_D(C)`

for every local tensor `C`.

Differentiating at the identity gives an exact universal Jacobian right-null direction. For

`X_EPRL = [[0,-3],[1,0]]`,

one has

`X_EPRL^T D + D X_EPRL = 0`,

and therefore

`J_R(C) v_X(C) = 0`,

with

`v_X(C) = sum_(r=1)^4 X_(r) C`.

Thus, wherever `v_X(C)` is nonzero,

`rank J_R(C) <= 31`.

The same construction holds for the unit-edge-weight control with `D=I` and `X_unit=[[0,-1],[1,0]]`.

This proves that a rank-32 witness is structurally impossible for the **unquotiented frozen control map**. The repeated rank 31 is not a failure to sample sufficiently generic tensors.

## Prospective critic control

The theorem was frozen before its substantive exact controls in:

- preregistration `prereg/ITER078M_CRITIC_INTERNAL_EDGE_GAUGE_SYMMETRY.md`, commit `df63f66f1f8302b79a278577bd9088deeb28ef39`;
- implementation `distributional/iter078m_critic_internal_edge_gauge.py`, commit `11ceb5b671184970c70e480cf81fde1254fade3e`;
- workflow `.github/workflows/iter078m_critic_internal_edge_gauge.yml`, commit `d343da6d052ae1e421307e5b77323733ad4a6589`;
- terminal run `34791227073`.

All six frozen lanes A/B/C/L/W/U completed successfully. W is a new critic generic tensor frozen prospectively; U repeats W with unit edge metric.

Artifacts and uploaded ZIP digests:

- A: `10327822318`, `sha256:98e2c3216a3f2e5ee2c1069bc771083666a717a6967030ee01615df6a383b0bf`;
- B: `10328472277`, `sha256:dff4da35be1f46e7678deab62a9b72e578563f048fbf9685ab906731d80ccdab`;
- C: `10328362407`, `sha256:d626f245c05b483da5d59f3b83f5fc65d3b9b28821966ed5f9e9c013dba7b3c9`;
- L: `10328745905`, `sha256:8d67c72431c013ccd7153604fa51e92059b03d75c2fb88a6ce4d4b92dffea21c`;
- W: `10328750943`, `sha256:1fb23becf5c46ab82ecace115758f5506f3abdc7b80c922bb648ec0eab97d5d0`;
- U: `10328337596`, `sha256:99971857bbbff352daac5fa546298f052d1d5cf51a5fb24d1e58de206babe810`.

For every frozen control the gauge tangent is nonzero, `Jv=0` exactly, and the metric-generator residual vanishes exactly. At L and W the exact Jacobian has rank 31/nullity 1 and the constructed gauge tangent is projectively identical to the exact RREF null witness.

At L, the previously reported Iter078J null direction is exactly the same gauge tangent up to an overall factor: the critic tangent equals `-8` times the recorded null vector.

## Consequences for prior controls

### Iter078M

The raw rank-31 calculations remain valid, but the Research interpretation `INCONCLUSIVE_GENERIC_RANK` is now scientifically superseded for this control object: rank 32 cannot occur before quotienting the internal `O(D)` basis-gauge orbit.

Further random searches for an unquotiented rank-32 witness in the same map are inadmissible because the determinant vanishes identically by symmetry.

### Iter078N

Iter078N survives review in its exact stated scope. A varying left null normal is fully compatible with a fixed **right/input** gauge symmetry: the left null space can vary with the base point even though the Jacobian always annihilates the tangent to the gauge orbit.

Therefore the no-common-output-hyperplane result is confirmed, but it is not the explanation of the rank defect.

### Iter078J

The previously observed second-order change along the affine path `C(t)=L+t n` does not establish nonlinear physical selection of `n`. The true finite gauge orbit `T_{G(t)}L` is curved in the 32-dimensional coordinate space. Its tangent at `t=0` is `n`, while the straight affine line leaves that orbit at order `t^2`. A nonzero second-order response on the straight line is therefore compatible with exact gauge invariance and cannot by itself lift the gauge redundancy.

## Source / surrogate firewall

This theorem is exact only for the versioned fixed-all-`j=1/2` pure order-zero tensor-network **control map** introduced after the source-faithful local K5 analysis. It is not a theorem that the physical Lorentzian causal-Toller refinement map has the same gauge symmetry, because that source-faithful 1-to-5 amplitude/measure/embedding/projection/regulator/extension-transport map remains undefined.

No scalar K4/K5/Hodge surrogate is promoted into the physical source-amplitude line.

## Critic verdict

`CONFIRMED_SCOPED`

The Iter078N conclusion “no common linear output hyperplane across the frozen controls” is confirmed. Its interpretation is sharpened by an exact stronger fact: the frozen unquotiented control map has a continuous internal-edge `O(D)` input redundancy that enforces `rank J <= 31` everywhere along nontrivial gauge orbits.

## Authorized next control gate

If this control map is retained, first quotient or gauge-fix the one-dimensional internal `O(D)` orbit and compute the induced differential on the 31-dimensional quotient. Rank 31 in the ambient map with a unique null equal to the gauge tangent would then mean local full rank on the quotient, not a missing physical selector.

Do not continue unquotiented rank-32 witness searches or interpret the affine second-order response as selector evidence.

## Physical priority / claim ceiling

The upstream physical blocker remains

`SOURCE_FAITHFUL_CAUSAL_1TO5_AMPLITUDE_MEASURE_EMBEDDING_PROJECTION_REGULATOR_AND_EXTENSION_TRANSPORT_MAP`.

The gauge theorem does not establish a source-selected K5 extension, physical RG flow, regulator independence, G3, F9/G8/K5 promotion, new physics, or complete quantum gravity. It does not retroactively define the missing causal-Toller refinement map.