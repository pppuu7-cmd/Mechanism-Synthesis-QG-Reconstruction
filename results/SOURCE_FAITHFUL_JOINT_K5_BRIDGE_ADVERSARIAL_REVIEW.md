# Independent adversarial review — source-faithful joint K5 meromorphic bridge

Date: 2026-09-15

Reviewed result: `results/SOURCE_FAITHFUL_JOINT_K5_BRIDGE_AUTHORITY_RESULT.md`, repaired Researcher commit `79d166fdf89a9e42a653ed3bbb4b0cac426820da`.
Review preregistration: `prereg/SOURCE_FAITHFUL_JOINT_K5_BRIDGE_ADVERSARIAL_REVIEW.md`, commit `836eef6d898abd00e39523f81dd2e996fed60814`.

Verdict: **CONFIRMED_SCOPED**.

The confirmation is strictly for existence/definition of the frozen local full-source **q_B-regularized multivariate meromorphic family and its polar germ**. It is not confirmation of a unique physical regularization, regulator independence, a holomorphic projection, a finite part, a one-parameter residue, or a unique K5 extension.

## A1 — Cartan-radius analyticity: PASS

With the source convention

`h = U1 exp(-i beta K_z) U2`, `K_z=i sigma_z/2`,

one has

`exp(-i beta K_z)=diag(exp(beta/2),exp(-beta/2))`.

Therefore

`(1/2)Tr(h h^dagger)=cosh(beta)`.

Writing `s=(1/2)Tr(h h^dagger)-1`, exact formal inversion of

`cosh(sqrt(q))=1+s`

gives

`q=beta^2=2s-(1/3)s^2+(4/45)s^3+O(s^4)`.

Thus `q` is real analytic through the compact locus even though `beta` is only a radial coordinate there. It is nonnegative, `q=0` iff `beta=0` iff `h in SU(2)`, and its normal Hessian is positive definite. Cartan rapidity is invariant under compact left/right factors and under inversion, so the claimed compact covariance and wedge-reversal invariance hold.

The repaired production independently enforces the exact tuple `(2,-1/3,4/45)`.

## A2 — block-radius authority and nonlinear freedom: PASS WITH SCHEME FIREWALL

The proposed block function

`q_B=(1/|B|) sum_(a<b in B) beta(g_b^-1 g_a)^2`

uses only exact source Cartan rapidities and the true complete-graph incidence inside the physical collision block. It is label-free, nonnegative, and vanishes exactly when every block-relative element lies in `SU(2)`.

At a collision its quadratic normal part is

`(1/|B|) sum_(a<b)|x_a-x_b|^2 = sum_a |x_a-xbar_B|^2`,

so it agrees exactly with the source-normal radial form independently established in repaired Iter083M. The `1/|B|` normalization is therefore not an arbitrary regulator-space metric.

However the source does not imply regulator independence under all nonlinear replacements of defining functions. If

`q'_B = exp(phi_B) q_B`

with smooth invariant `phi_B`, then the regularized families obey exactly

`U'(lambda)=exp[(1/2)sum_B lambda_B phi_B] U(lambda)`.

The multiplier is holomorphic and invertible in the regulator parameters. Consequently the meromorphic divisor, pole orders, and highest Laurent coefficient at a given pole direction are stable under such a change, while lower negative Laurent coefficients can mix when higher-order poles are present. For example, in one variable,

`A_-2/lambda^2 + A_-1/lambda + ...`

transforms to

`A_-2/lambda^2 + (A_-1 + phi A_-2/2)/lambda + ...`.

This is not a defect in bridge existence. It is a hard interpretation ceiling: the Researcher construction defines an explicit source-faithful `q_B` scheme, not a theorem that every polar coefficient is regulator-independent or physically canonical.

## A3 — full collision arrangement and blow-up: PASS

Let `G=SL(2,C)`, `K=SU(2)`, and `X=G/K`. For every block condition,

`g_b^-1 g_a in K  <=>  g_a K = g_b K`.

Thus the compact collision stratum for a vertex block is precisely the inverse image, under the smooth quotient submersion `G^5 -> X^5`, of the corresponding ordinary polydiagonal in the five-point configuration on the three-dimensional symmetric space `X`.

This identifies the collision arrangement locally with a genuine polydiagonal arrangement rather than only its tangent surrogate. Standard wonderful/iterated real blow-up constructions therefore apply locally and equivariantly. Pullback under a submersion preserves the clean-intersection structure needed here.

The complete nontrivial block census is exactly

- 10 K2;
- 10 K3;
- 5 K4;
- 1 K5;

for 26 blocks. The divergent K3/K4/K5 family contains 16 blocks. The 20 maximal divergent chains have physical incremental normal ranks `(6,3,3)`, agreeing with authoritative Iter082D and repaired production.

K2 faces are retained in the resolution even though individually locally integrable; this is necessary to resolve every pairwise Toller singularity and is correctly done by the Researcher construction.

## A4 — KAK angular degeneracy: PASS WITH DERIVATION REFINEMENT

Individual KAK compact factors `U1,U2` are not unique at `beta=0`, so they must not be treated as separately smooth coordinates through the compact locus.

This does not invalidate the construction. Near `K`, use the local polar/symmetric-space description instead: the noncompact normal variable is `X in p`, with `beta=|X|`, and the real blow-up replaces `X=0` by its normal direction `omega=X/|X|`. The actual Toller matrix is a well-defined matrix-valued function on the group away from the singular locus and has exact compact covariance. In the frozen `j=1/2` sector its explicit entries are finite combinations of radial functions `exp(+/-i rho beta)`, `sinh(beta)^(-2)`, `cosh(beta)`, `sinh(beta)` with compact/angular matrix coefficients. After writing `X=r omega`, these coefficients are smooth on the front face and the radial factors have classical power expansions.

Therefore the **actual matrix-valued function**, not the nonunique individual KAK factors, has the required polyhomogeneous/conormal lift. The Researcher derivation is confirmed only with this invariant interpretation.

## A5 — full 32-component object: PASS

Each lifted wedge object acts in a finite-dimensional matrix space. Finite matrix multiplication preserves polyhomogeneous/conormal expansions. The complete all-`j=1/2` boundary space has exactly 32 components and the construction contracts against the whole boundary tensor rather than selecting a representative component. Finite linear contraction preserves the same class.

No scalar/Hodge/cycle surrogate enters B3.

## A6 — continuation-theorem matching: PASS IN THE FROZEN LOCAL SECTOR

On the resolved manifold with corners, every boundary face has a defining radius and the lifted full source object has product-type polyhomogeneous conormal expansions. Multiplication by

`product_B q_B^(lambda_B/2)`

shifts the boundary exponents linearly in the complex parameters. Because K2 singularities are already locally integrable and every divergent K3/K4/K5 face receives regulator weight, taking all relevant real parts sufficiently positive supplies a nonempty convergence chamber.

The Mellin transform of polyhomogeneous conormal distributions is meromorphic with poles determined by the boundary index sets. Equivalently, resolution-of-singularities/complex-power theorems give distribution-valued meromorphic continuation for analytic complex-power families. The continuation is unique by equality with the convergent family on a nonempty open parameter domain.

Finite-dimensional matrix/boundary values do not alter the theorem: continuation applies componentwise. The original product Haar density is retained; on a maximal K3-K4-K5 corner its blow-up Jacobian supplies the exact radial powers `(5,2,2)` derived from ranks `(6,3,3)`.

This establishes B6 for meromorphic-family existence. It does **not** establish uniqueness of a value at `lambda=0`; such a value requires a separate projection/finite-part rule.

## A7 — branch/sign and spectral firewall: PASS

The new factors are scalar functions of squared Cartan rapidities and are inserted only after the source one-wedge Toller matrices have been constructed. They are branch blind and invariant under wedge reversal. No `beta+i epsilon` replacement is made, no one-wedge `rho` contour is modified, and no Toller representation/composition law is assumed.

Thus the construction respects the source-order firewall and does not conflict with Iter083E/F.

## A8 — multivariate residue firewall: PASS

The bridge object has 16 independent block parameters. The result correctly refuses to identify it with a one-parameter family and sets

`one_parameter_A_minus_1_authorized=false`.

No unique `A_-1`, holomorphic projection, Hadamard finite part, or physical extension follows. The authorized successor must consume the actual multivariate polar data or first prospectively justify any specialization.

## A9 — scheme dependence: PASS AS A REQUIRED DOWNSTREAM CONTROL

The exact transformation law in A2 shows that the whole Laurent presentation is not automatically invariant under nonlinear changes of defining functions. Therefore the next normal-jet/annihilator gate must do at least one of the following prospectively:

1. compute invariants of the multivariate polar germ under the holomorphic gauge action `U -> exp[(1/2)sum lambda_B phi_B] U`;
2. prove that the particular polar coefficient/order relevant to the physical question is invariant under the allowed defining-function class;
3. explicitly freeze the source-derived `q_B` scheme and keep the result scheme-scoped.

It may not infer regulator independence from the present bridge PASS.

This restriction is already compatible with the parent preregistration interpretation ceiling and therefore does not downgrade bridge existence to QUALIFIED.

## A10 — repaired production/provenance: PASS

The only authoritative production is the repaired run:

- head `87e732bab75e3d60f1df1390561fc584f667526f`;
- run `34953022566`, terminal success;
- job `104328280379`, terminal success;
- artifact `10389449925`;
- artifact ZIP digest `sha256:abf75fdd1d1bfe97a0913cdcddb723b9c9fec6ca075dd47cc414fff593769d1b`;
- production JSON SHA256 `3a66499afb5c16b4fd0643ab3796f7da827d5ec09d3e03359fba2a5ba6c56011`.

The historical pre-repair run and its `1/30` diagnostic are superseded. The durable raw JSON and Researcher result were reconciled to the corrected `4/45` production before this review.

## Counterexample attempts summary

The following attacks do not overturn the scoped bridge:

- nonuniqueness of individual KAK factors — resolved by invariant symmetric-space/polar blow-up coordinates;
- non-polydiagonal appearance in group variables — resolved by the exact quotient identity `g_b^-1 g_a in K iff g_aK=g_bK`;
- representative-component loophole — absent, all 32 components retained;
- omission of K2 singular faces — absent, all 10 K2 blocks included in the resolution;
- spectral-regulator substitution — absent;
- arbitrary 10-dimensional regulator-space Q — absent;
- sequential finite part — absent;
- physical finite-part overclaim — explicitly absent;
- nonlinear defining-function freedom — real, but affects scheme dependence rather than existence of the prospectively specified meromorphic family.

## Final Critic verdict

**`CONFIRMED_SCOPED`** for:

`BRIDGE_AUTHORITY_CONFIRMED_SCOPED`.

The prior Iter083P object-definition blocker is closed only at the level of a frozen local, all-`j=1/2`, full-source, block-multivariate meromorphic family/polar germ. The 377-dimensional physical extension-selection problem remains unsolved.

## Authorized next gate

The next Researcher gate may now be opened prospectively as

`ACTUAL_SOURCE_ORDERED_MULTIVARIATE_POLAR_NORMAL_JET_ANNIHILATOR`,

with an additional frozen obligation to track the defining-function holomorphic-gauge action described in A2/A9.

## Claim locks

No unique K5 extension; no physical finite-part selector; no regulator independence/dependence theorem for the causal vertex; no causal-vertex finiteness/divergence theorem; no generic-spin completeness; no global all-strata patching; no E3/E4/E6 closure; no G3/F9/G8/K5 promotion; no RG/continuum/spin-2/GR/matter/prediction result; no `NEW_PHYSICS_FOUND`; no complete quantum gravity.
