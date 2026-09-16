# K5 S5-equivariant degree-two face-tangent logarithmic IBP/syzygy — terminal result

Date: 2026-09-16

## Authority

Parent terminal authority:

`results/K5_ORDER8_INVARIANT_DUAL_PROJECTIVE_IBP_REACHABILITY_RESULT.md`, commit `e9ed372a91ac1bd219dc7671a916c70405e9cd43`.

Prospective gate:

`prereg/K5_ORDER8_S5_DEG2_FACE_TANGENT_LOG_IBP_SYZYGY.md`, commit `01bc02dad5e94873e726fca75ee07f0c8c01946d`.

Exact solver:

`scripts/k5_order8_s5_deg2_log_ibp_syzygy.py`, commit `11a24a608ab8bcee5416edc2570c6f508fa71dd0`.

Workflow/head:

`.github/workflows/k5_order8_s5_deg2_log_ibp_syzygy.yml`, head `03b466cc4f212a39dea5498d06cd06062d1dfa35`.

Production:

- run `35038028770`, terminal `success`;
- job `104611421963`, terminal `success`;
- artifact `10424474143`;
- artifact ZIP digest `sha256:2b9934b117dff8265fb99fffa476542d3d24e2290c21048e0bdeb6ebcb09cfe8`;
- production JSON SHA256 `83bbd3c399ce4d5df1f15d24d2afa3b7d65d6c9b8e9d49a969dfc1ceeeb17ed0`;
- status `PASS_EXACT_SCOPED`;
- classification `K5_S5_FACE_TANGENT_LOG_IBP_DEG2_RADIAL_ONLY_EXACT_SCOPED`.

All 15 frozen implementation checks and all 5 adversarial controls passed.

## Exact construction

Use the authoritative K5 edge order

`(01),(02),(03),(04),(12),(13),(14),(23),(24),(34)`

and reconstruct

`Psi_K5(alpha)=det L(alpha)`

independently as the 125-term spanning-tree polynomial. Every monomial has degree four and coefficient one.

For a fixed K5 edge, its stabilizer in `S5` has order 12 and exactly three orbits on the ten edges, of sizes

`(1,6,3)`

corresponding to the edge itself, the six adjacent edges and the three disjoint edges. Hence the complete `S5`-equivariant regular face-tangent homogeneous degree-two ansatz is

`v_e = alpha_e [ a alpha_e + b sum_(f adjacent e) alpha_f + c sum_(f disjoint e) alpha_f ]`.

Because `Psi_K5` is homogeneous degree four and `S5`-invariant, the degree-one logarithmic quotient is necessarily

`k s1`, where `s1=sum_e alpha_e`.

The exact polynomial identity solved is therefore

`v(Psi_K5)=k s1 Psi_K5`.

No point sampling or floating-point fit enters the solve.

## Exact nullspaces

### Degree one

For

`v_e=a alpha_e`, `v(Psi)=k Psi`,

the coefficient system has rank one and nullity one. Its primitive integer basis is

`(a,k)=(1,4)`.

Thus the degree-one logarithmic space is exactly the Euler span.

### Degree two

For the complete three-parameter equivariant ansatz above, the coefficient system has rank three and nullity one. Its primitive integer basis is

`(a,b,c,k)=(1,1,1,4)`.

This is exactly

`v=s1 E`,

with `E=sum_e alpha_e d/d alpha_e`.

Therefore the quotient of the degree-two `S5`-equivariant regular face-tangent logarithmic space by the radial polynomial-Euler span has dimension

`0`.

Hence

`K5_S5_FACE_TANGENT_LOG_IBP_DEG2_RADIAL_ONLY_EXACT_SCOPED`.

## Non-circular controls

The same exact solver is applied to the synthetic homogeneous polynomial

`Psi_syn=prod_e alpha_e`.

For that fixture the degree-two equivariant logarithmic system has nullity three, with primitive basis

- `(6,-1,0,0)`;
- `(3,0,-1,0)`;
- `(1,0,0,1)`.

Its radial anchor is `(1,1,1,10)`, so the synthetic nonradial quotient dimension is exactly two. Thus the solver genuinely reaches a nonradial branch when the polynomial supports one and cannot be a hard-coded radial-only classifier.

Additional controls reject a fake logarithmic vector, a non-face-tangent field, and a broken `S5` coefficient matrix.

## Scientific meaning

There is no non-radial same-denominator logarithmic IBP direction in the complete `S5`-equivariant regular face-tangent class through component degree two for the exact K5 Kirchhoff polynomial.

This does not say that all logarithmic derivations are radial. It does not exclude higher degree or non-equivariant orbit systems, and it does not evaluate either invariant-dual K5 projective period.

Independent exploratory algebra performed after the preregistration indicates a stronger structure — the unrestricted degree-two space appears to consist entirely of linear polynomial multiples of the Euler field, while the first `S5`-equivariant nonradial Kirchhoff annihilator appears at component degree four. Those observations are not promoted here; they require their own frozen confirmatory gate.

## Relation to the rank-two Critic reconciliation

A later independent Critic reclassified the earlier edge01/edge02 `00000` sign-change Researcher lane as `REQUIRES_NEW_PREREGISTERED_GATE` because its all-32 preregistration was narrowed post hoc to one representative component. This theorem is not downstream of that representative-component claim. Its parent is the full all-32 invariant-dual projective-object reachability result `e9ed372...`, and its solver uses only the exact K5 Kirchhoff polynomial / projective IBP geometry. The rank-two reclassification therefore does not alter this gate's object or conclusion.

## Authorized successor

The highest-information successor is not another representative-component positivity lane. It is an independently frozen low-degree logarithmic-module gate that tests the full face-tangent degree-two/degree-three spaces and the first `S5`-equivariant degree-four candidate. In particular, it should determine whether:

1. all unrestricted degree-two and degree-three logarithmic derivations are polynomial multiples of Euler; and
2. the exploratory degree-four `S5`-equivariant nonradial class is a genuine exact Kirchhoff annihilator `v(Psi_K5)=0` modulo radial multiples.

If confirmed, the degree-four annihilator should then be inserted into a correctly projective `(n-2)`-form IBP construction and applied to the two actual invariant-dual degree-27 numerator channels, with Schwinger-boundary terms audited explicitly.

No K5 period zero/nonzero theorem, no full 217-dimensional tensor result, no finite-part selector, no regulator-independence theorem, no G3/F9/G8 promotion, no `NEW_PHYSICS_FOUND`, and no complete-QG claim follows from this result.