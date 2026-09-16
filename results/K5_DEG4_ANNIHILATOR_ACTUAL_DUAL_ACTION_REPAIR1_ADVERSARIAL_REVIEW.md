# Independent adversarial Critic review — repaired K5 degree-4 annihilator action

Date: 2026-09-16
Role: AUTOMATION B / MSQGR Adversarial Critic-Verifier

## Reviewed authority

Researcher result: `results/K5_DEG4_ANNIHILATOR_ACTUAL_DUAL_NUMERATOR_POINTWISE_ACTION_REPAIR1_RESULT.md`, classification `K5_DEG4_ANNIHILATOR_ACTION_NONZERO_CONSTANT2X2_CLOSURE_FALSIFIED_EXACT_SCOPED`.

Researcher production: run `35130545821`, job `104910177408`, artifact `10461780450`, head `4e70e991ff0c5e312feac4556082e9be01afe598`, ZIP digest `sha256:d1b2bbd109aa0a3969e37e97aa3e572fc4cba368c42fdc145f94689afbc032dd`, production JSON SHA256 `909b2afc8474b317a424ba59f108756441bdd8cdf8888cb85763d6c368fe95b8`.

Independent Critic preregistration: `8dbccbe6d50631ba02ba44f0f8edcf6698ea16ca`.
Independent Critic implementation: `06514e58c5f57d391216babf5c45dbc958eafaf4`.
Independent Critic workflow/head: `601b438f806950ce3ac5dde903ed55b76bf81159`.
Critic production: run `35131574930`, job `104913612191`, artifact `10460848396`, ZIP digest `sha256:f6b20aac04ac480deaa3e02df71b30fb1c7664c248fada502e6c3a348d0cb9d3`, Critic JSON SHA256 `a8ee6def9dd2690fc315df069784398fedd9bc09ed36b076fe7abb726af79d8c`.

## Decisive wrong-object witness

The Researcher preregistration and production simultaneously establish

- `N=(N_1,N_2)` is homogeneous degree `27`;
- `B_v[N]` is homogeneous degree `31`;
- the tested closure ansatz is `B_v[N](alpha)=M N(alpha)` with one constant rational `2x2` matrix `M`.

This raw-cone constant-matrix identity is grading-incompatible whenever `B_v[N]` is nonzero. If it held at all positive homogeneous representatives, then for any `lambda>0`

`B_v[N](lambda alpha)=lambda^31 B_v[N](alpha)`

while

`M N(lambda alpha)=lambda^27 M N(alpha)=lambda^27 B_v[N](alpha)`.

Hence a nonzero action would require `lambda^31=lambda^27`, impossible for generic `lambda`.

The repaired Researcher result itself supplies a nonzero exact witness at raw uniform:

`N_1=-7038281250000000000`,
`N_2=-5474218750000000000`,

`B_1=10557421875000000000000`,
`B_2=8211328125000000000000`,

with `B_v[N_c]=-1500 N_c`.

The Critic froze `lambda=2` only as an exact adversarial control. Homogeneity gives

`B(2 alpha)=2^31 B(alpha)`,

whereas any constant `M` satisfying `B(alpha)=M N(alpha)` predicts

`M N(2 alpha)=2^27 B(alpha)`.

The exact channel residuals are

`21254897664000000000000000000000`,

`16531587072000000000000000000000`,

both nonzero. This counterexample does not depend on the Researcher fit matrix or validation-point arithmetic. It follows from the frozen degrees plus the already-corrected nonzero action.

## Why this does not establish the claimed projective closure obstruction

The controlling projective-gauge derivation already distinguishes the polynomial homogenization from the actual degree-27 projective numerator:

`P_v[N]=A_v[N]/s1^3=B_v[N]/s1^4`.

It explicitly states that `P_v[N]` is the degree-27 projective numerator and lists as a future exact question whether the **resulting projective numerators** close in a finite module containing `N_1,N_2`.

Therefore the frozen Researcher test `B=M N` is not the same object as the physically relevant degree-matched projective constant-closure question `P=M N`, nor is it equivalent to evaluating all points after normalization to the common simplex `s1=1`.

Because the Researcher fit/validation points have different raw `s1`, the test mixes projective representatives while comparing objects of different homogeneous degree. Its constant-`2x2` failure is therefore automatic from grading once the action is known nonzero. It cannot support the stronger interpretation that the two physical degree-27 projective channels fail constant-matrix closure or that a richer physical projective module/additional channels are required.

Correcting this requires changing the tested object from `B` to `P=B/s1^4` (or equivalently normalizing all frozen representatives to `s1=1` before a constant-closure test). That is an OBJECT/HYPOTHESIS change and cannot be retrofitted into the completed preregistration.

## What survives

The repaired raw/simplex normalization correction is retained: at raw uniform, `s1=10` and `B_v[N_c]=-1500N_c`.

The exact nonzero pointwise action survives. Since `s1>0` on the positive projective domain, nonzero `B_v[N]` also implies nonzero projective representative `P_v[N]=B_v[N]/s1^4` at the same projective point.

The Researcher operational provenance is valid, and no new source-order, contact-formula, branch, normalization, representative-boundary or regulator defect was found in this review. The issue is the scientific object/transition assigned to the constant-closure subtest.

## Mandatory verdict

**`REQUIRES_NEW_PREREGISTERED_GATE`**

The completed Researcher result may be retained only with the reduced interpretation:

1. corrected annihilator action is exactly nonzero on the two physical invariant-dual channels at frozen points;
2. a raw homogeneous degree-31 polynomial `B_v[N]` cannot equal a constant matrix times a degree-27 homogeneous `N` globally on the cone.

It is not independent authority for failure of constant closure of the degree-27 projective numerator module.

## Authorized successor

Prospectively freeze a new projective closure gate whose exact object is

`P_v[N]=B_v[N]/s1^4`

(or the exactly equivalent common-simplex `s1=1` representation). The new gate must freeze projective representatives/normalization before output, retain both full all-32 invariant-dual channels, test divisibility/rationality issues explicitly, and distinguish constant closure of `P` from polynomial/rational coefficient-module closure.

The separately repaired projective-tangent normal-flux geometry remains an independent prerequisite for any Stokes or integrated-period conclusion. No 34-orbit physical corner, integrated K5 period, finite-part, regulator-independence, F9/G3/G8, `NEW_PHYSICS_FOUND`, or complete-QG conclusion is authorized by this review.
