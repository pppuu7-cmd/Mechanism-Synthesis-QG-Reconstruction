# Iter077G-SM result — corrected all-spin-half contact has a nonzero rank-9 n=3 self-stress channel

**Date:** 2026-09-14

## Authority

- contact-formula erratum: `status/ITER077_CONTACT_FORMULA_ERRATUM.md`, commit `eba9976fb7cdc1f7f64852325a35f7c6829a6b0b`
- corrected source snapshot: `sources/CAUSAL_SPINFOAM_VERTEX_2026_CONTACT_EQ37_39_CORRECTED_SNAPSHOT.md`, commit `edc8bd718c5ac381e26b57636963cfb180f3ecd7`
- prospective preregistration: `prereg/ITER077G_SM_CORRECTED_JHALF_CONTACT_MICROLOCAL_SCALING.md`, commit `e2d3d99be0c2377690494a86556b51a85f106e9f`
- implementation: `distributional/iter077g_sm_corrected_jhalf_contact_microlocal_scaling.py`, commit `0091d3d730c2ac06fcdd2f82de69cbb212913b63`
- workflow/production head: `7cdadc77c589fff56650d7bcbc8a6e7ebf9a04dd`
- authoritative run: `34785754577`
- raw artifacts: A `10326178953`, B `10326826327`, C `10326268618`, D `10326188898`
- aggregate artifact: `10326159080`, digest `sha256:a3eba270742cd17070c2b6b11f5aff064981412a92f4d3c96d55194c6ea84991`

All frozen lanes A/B/C/D and aggregate passed.

## Classification

`ITER077G_SM_CORRECTED_JHALF_CONTACT_HAS_NONZERO_RANK9_N3_SELFSTRESS_CHANNEL_SD8_SOURCE_SELECTED_CORRELATED_EXTENSION_REQUIRED_EXACT_SCOPED`

## Corrected source contact

Appendix D Eqs. (37)-(39) of arXiv:2601.23162 give, for `j=1/2`,

`delta^(rho,1/2)(x)=-(2 i rho/D) delta(x)-(1/D) delta'(x)`, `D=rho^2+1/4`.

For `rho=gamma/2`,

`A_gamma=-4 i gamma/(1+gamma^2)`,

`C_gamma=-4/(1+gamma^2)`.

At the frozen `gamma=6/5`,

`A=-120 i/61`, `C=-100/61`.

This corrects the quarantined historical E/F transcription. The delta-prime coefficient is nonzero for every finite real gamma; the ordinary delta coefficient is nonzero for finite real `gamma != 0`.

## Corrected microlocal split

The true-source generic witness remains rank 10 with zero left nullity, so the ordinary distributional pullback is locally authorized on that submersion region.

At the frozen rank-9 witness, the exact self-stress is

`lambda=(1,-1,0,0,1,0,0,0,0,0)`

and `J^T lambda=0` exactly.

For the ten corrected all-spin-half contact factors, the exact Fourier polynomial is

`P_10(xi)=K_gamma prod_e(gamma+xi_e)`,

`K_gamma=[-4 i/(1+gamma^2)]^10`.

Along the exact self-stress ray,

`P_10(t lambda)=K_gamma gamma^7 (gamma+t)^2(gamma-t)`.

For finite real `gamma != 0`, this is a nonzero cubic polynomial. Therefore the contact target distribution is not rapidly decreasing in the source-map conormal direction. The standard Hörmander wavefront/normal-set criterion fails at this frozen rank-9 point.

This failure is **not** a theorem that the source-selected spectral boundary value does not exist.

## Highest self-stress derivative order

The Fourier restriction has exact degree

`n_eff=3`,

equal to the three nonzero components of the self-stress (`01,02,12`). Its leading coefficient is

`-K_gamma gamma^7 = 1048576 gamma^7/(1+gamma^2)^10`,

nonzero for finite real `gamma != 0` and exactly nonzero at `gamma=6/5`.

Thus a genuine rank-9 conormal/contact derivative channel of order 3 is present before the remaining smooth phase, spinor measure and boundary-intertwiner contractions. Survival in the full vertex is untested.

## Six-dimensional extension threshold

Using the canonical mixed rank-9 second-jet normal form, which is nondegenerate in six transverse variables, the scaling degrees are

| contact normal derivative n | scaling degree | consequence in d=6 |
|---:|---:|---|
| 0 | 2 | unique scaling-degree-preserving extension |
| 1 | 4 | unique scaling-degree-preserving extension |
| 2 | 6 | first marginal local ambiguity, order <=0 |
| 3 | 8 | nonunique by scaling degree alone, local derivative order <=2 |

Before source selection or symmetry constraints, the unconstrained order-<=2 local ambiguity space in six variables has dimension `1+6+21=28`.

This does not mean the physical source contains 28 free counterterms. The published spectral `i epsilon` prescription may select or cancel a specific combination.

## Scientific consequence

The missing mathematical object is now sharply localized:

`SOURCE_SELECTED_CORRELATED_SPECTRAL_I_EPSILON_EXTENSION_OF_THE_N_EFF_3_RANK9_CONTACT_CHANNEL`.

Arbitrary finite parts are not admissible substitutes. The next source-faithful gate must determine whether the original spectral prescription itself regularizes/extends the correlated rank-9 contact object, and then include the smooth Toller/spinor/intertwiner factors.

## Claim locks

No full source-vertex nonexistence/finiteness/divergence theorem; no regulator-independence theorem; no physical source-to-K4 pushforward; no nominal epsilon^-1 coefficient; no generic finite-spin signed P3; no G3/F9/G8/K5 promotion; no new physics or complete-QG claim.