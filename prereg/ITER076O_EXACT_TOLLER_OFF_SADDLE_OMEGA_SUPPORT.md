# Iter076O preregistration — does exact finite-spin Toller bulk support fix Omega off saddle?

Date: 2026-09-13

## Purpose

Iter076N establishes that the exact Toller restrictor selects one parity/`Omega_sigma` sector on the non-degenerate Lorentzian Regge saddle locus. It explicitly does not establish a generic finite-spin off-saddle signed source-to-K4 pushforward.

The newly frozen source snapshot `sources/CAUSAL_SPINFOAM_VERTEX_2026_OFF_SADDLE_TOLLER_SUPPORT_SNAPSHOT.md` records two exact ingredients that are absent from the saddle substitution:

1. each wedge has its own auxiliary projective spinor `z_ab`;
2. `exp(B(z,g))` is the Rayleigh quotient of `H=g g^dagger`.

For non-unitary `g in SL(2,C)`, `H` has reciprocal eigenvalues above and below one. Thus a single exact Toller wedge has open bulk support for either sign of `B`, depending on its independent spinor.

This prospective gate tests whether the ten-wedge exact bulk support contains **both signs of the non-degenerate Iter076M orientation pseudoscalar for the same fixed source causal assignment**, demonstrating that support alone is not an exact finite-spin global orientation projector.

No Iter076O production output exists at preregistration time. Frozen criteria below may not be changed after viewing results.

## Frozen causal assignment and group controls

Use the fixed physically relevant combinatorial causal class

`sigma = (-1,+1,+1,+1,+1)`

(`1 -> 4`, up to global reversal), with `kappa_ab=sigma_a sigma_b`.

Construct five pure boosts `g_a in SL(2,C)` from the fixed rational ball coordinates

- `u_0=(0,0,0)`;
- `u_1=(1/3,0,0)`;
- `u_2=(0,1/4,0)`;
- `u_3=(0,0,1/5)`;
- `u_4=(1/6,1/7,1/8)`.

Use

`g(u) = (I + u.sigma_Pauli)/sqrt(1-|u|^2)`.

Its Lorentz image of the unit future vector is

`F(u)=((1+|u|^2)/(1-|u|^2), 2u/(1-|u|^2))`.

Configuration `X+` assigns `(F_0,F_1,F_2,F_3,F_4)` to labels `(0,1,2,3,4)`. Configuration `X-` swaps only labels `1` and `2`. Since `sigma_1=sigma_2=+1`, this is an odd swap of two equally weighted affine columns and must flip `Delta_sigma` without changing the causal assignment.

## Frozen lanes

### Lane A — exact single-wedge spectral support lemma

For every one of the ten relative elements `g_ab=g_b^-1 g_a` of `X+` and `X-`:

1. verify `det(g_ab)=1` within a fixed numerical tolerance `1e-12`;
2. form `H_ab=g_ab g_ab^dagger`;
3. verify `H_ab` is Hermitian positive and `det(H_ab)=1` within `1e-12`;
4. verify `trace(H_ab)>2+1e-12`, hence the relative element is non-unitary;
5. compute its two eigenvalues from trace and determinant and verify `lambda_max>1+1e-12>lambda_min` and `lambda_max*lambda_min=1` within `1e-12`.

PASS iff all `20` configuration-wedge instances pass. This proves that for every wedge both signs `B>0` and `B<0` occur on open spinor sets.

### Lane B — opposite Omega controls at fixed causal data

Using the exact rational Lorentz vectors `F(u)` and the Iter076M determinant

`Delta_sigma(F)=det([1; sigma_a F_a])`,

compute `Delta_+` for `X+` and `Delta_-` for `X-` with exact rational arithmetic.

PASS iff:
- both are nonzero;
- `Delta_-=-Delta_+` exactly;
- `Omega_-=-Omega_+`;
- the source causal assignment `sigma` is identical for both configurations;
- all five future vectors remain pairwise distinct in both configurations.

### Lane C — ten-wedge bulk-support intersection in both Omega sectors

For each configuration and each wedge `(ab)`, let `kappa_ab=sigma_a sigma_b`.

Use the spectral extrema of `H_ab` to select the sign required by the open Heaviside bulk:
- if `kappa_ab=+1`, use the `lambda_max` eigendirection, giving `B=log(lambda_max)>0`;
- if `kappa_ab=-1`, use the `lambda_min` eigendirection, giving `B=log(lambda_min)<0`.

Because the source integrates independent `z_ab` for different wedges, the ten choices form a product point in the exact spinor integration domain.

PASS iff all ten inequalities `kappa_ab B_ab>0` are simultaneously realizable for both `X+` and `X-`, with a frozen margin `min_ab |B_ab| > 1e-8` so no boundary `B=0` contribution is being used.

Record all ten signed margins for both configurations.

### Lane D — boundary and interpretation controls

Use a unitary control `g=I`, for which `B(z,I)=0` for every spinor, and verify that the strict bulk test correctly rejects it (`trace(H)=2`, no positive/negative open Rayleigh sectors).

PASS iff the aggregate locks all of the following:
- `exact_bulk_support_global_Omega_projector = false`;
- `both_Omega_sectors_in_same_fixed_causal_bulk_support = true`;
- `boundary_distribution_used_for_counterexample = false`;
- `full_amplitude_interference_conclusion = UNTESTED`;
- `generic_finite_spin_signed_P3_promoted = false`;
- `Iter076N_saddle_selection_unchanged = true`;
- `epsilon_minus1_coefficient_established = false`.

## Frozen interpretation

If A-D pass, classify:

`ITER076O_EXACT_TOLLER_BULK_SUPPORT_CONTAINS_BOTH_OMEGA_SECTORS_OFF_SADDLE_NO_GLOBAL_FINITE_SPIN_SELECTOR_SCOPED`

Meaning: the exact finite-spin Heaviside support restriction is not, by itself, a global projector onto one `Omega_sigma` orientation sector away from stationary points. Both nonzero orientation sectors occur in its open bulk for the same fixed `1->4` source causal assignment. Therefore Iter076N's orientation selection is genuinely a saddle-locus result unless a stronger phase/contraction/interference mechanism is separately source-provenanced.

This result would not prove that the fully integrated finite-spin amplitude receives nonzero net contributions from both sectors: cancellations, oscillatory phases, damping and intertwiner contractions remain untested.

If any relative element lacks both Rayleigh signs, classify:
`ITER076O_SINGLE_WEDGE_SPECTRAL_SUPPORT_FAIL`.

If the two controls do not have exact opposite nonzero `Omega`, classify:
`ITER076O_OPPOSITE_OMEGA_CONTROL_FAIL`.

If the ten-wedge support intersection fails for either sector, classify:
`ITER076O_MULTI_WEDGE_SUPPORT_FAIL`.

Technical/runtime errors are `INFRASTRUCTURE_OR_NUMERICAL_FAIL`, not scientific FAIL.

## Claim locks

No `NEW_PHYSICS_FOUND`; no complete-QG claim; no generic finite-spin signed P3; no statement that both sectors survive full integration; no nominal `epsilon^-1` coefficient; no physical causal-vertex finiteness/divergence theorem; no F9/G3/G8/K5 promotion.
