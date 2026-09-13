# Iter076O terminal result — exact Toller bulk support contains both Omega sectors off saddle

Date: 2026-09-13

## Authority

- exact off-saddle Toller spinor-support source snapshot: `98fa54aab0876707bf4b6e902a7d2fc059cbe665`
- frozen preregistration: `735a0bf1d2a7f8b9c5a13404bb4cd9b12fd8547b`
- implementation: `e9ba9d9bcb1218e821657456fb2987a63532c4bd`
- production/workflow head: `164bb65fa8b120c6e6d697bb2f75b433ac5e92e9`
- authoritative run: `34781757359` (`success`)
- aggregate job: `103789956658`
- aggregate artifact: `10324732666`
- aggregate artifact ZIP digest: `sha256:e40cbcf8d6372c8718b388b6c078a9bb9b9c24fc7eec64789b0bc2e71b00a0f8`

Raw lane artifacts consumed by the aggregate job:
- A: job `103789932924`, artifact `10324882431`, digest `sha256:d067ba48fd3b1369e07597e3b0c9578bb85fb20138a7a91f65663b4a57c72add`
- B: job `103789932629`, artifact `10324428527`, digest `sha256:f2692748950caa6662a6a1cf026ada4e2551e729fe3097e4226b5507da9b01d5`
- C: job `103789932930`, artifact `10324928810`, digest `sha256:f43a37493242ee983835651bb13d1503fe982953cbc58d7c44cbb3e9fcf6624f`
- D: job `103789932752`, artifact `10324737693`, digest `sha256:7ef5557d9dbeb15e05f5115a1826591b7e41709e3a6198542c7fd2d70fda5eda`

## Frozen scientific classification

`ITER076O_EXACT_TOLLER_BULK_SUPPORT_CONTAINS_BOTH_OMEGA_SECTORS_OFF_SADDLE_NO_GLOBAL_FINITE_SPIN_SELECTOR_SCOPED`

All four prospectively frozen lanes pass and the aggregate output is `valid=true`.

## Terminal facts

### Lane A — every tested wedge has both Rayleigh-sign sectors

For the two frozen group configurations `X+` and `X-`, all `20/20` configuration-wedge relative elements pass the exact-support spectral controls:

- `det(g_ab)=1` within the frozen `1e-12` tolerance;
- `H_ab=g_ab g_ab^dagger` is Hermitian positive with `det(H_ab)=1` within tolerance;
- every relative element is non-unitary: `trace(H_ab)>2`;
- every spectrum satisfies `lambda_max>1>lambda_min>0` and `lambda_max lambda_min=1` within tolerance.

Thus, for every one of the ten wedges in both configurations, the exact source quantity

`exp(B(z,g_ab)) = z^dagger H_ab z / z^dagger z`

attains values above and below one on open projective-spinor sets. Both strict signs `B>0` and `B<0` therefore occur without using the distributional boundary `B=0`.

### Lane B — opposite nonzero Omega at identical causal data

The fixed source causal assignment is

`sigma=(-1,+1,+1,+1,+1)`,

representing the `1->4` causal class. It is identical in both controls.

Using exact rational arithmetic for the Iter076M affine determinant:

- `Delta_sigma(X+) = +6552/26423`;
- `Delta_sigma(X-) = -6552/26423`.

Hence

- `Omega_sigma(X+)=+1`;
- `Omega_sigma(X-)=-1`.

The determinants are exact global opposites and nonzero, and all five future timelike vectors remain pairwise distinct in both controls.

### Lane C — simultaneous ten-wedge open bulk support in both sectors

The source provides an independent projective spinor `z_ab` for every wedge. For the same fixed causal assignment, Lane C chooses for each wedge the appropriate spectral eigendirection:

- `kappa_ab=+1`: the `lambda_max` direction, so `B_ab>0`;
- `kappa_ab=-1`: the `lambda_min` direction, so `B_ab<0`.

All ten inequalities

`kappa_ab B_ab > 0`

hold simultaneously for `X+`, and all ten hold simultaneously for `X-`.

The smallest absolute bulk margin over both configurations is

`min |B_ab| = 0.4054651081081643`,

far above the frozen margin `1e-8`. No `B=0` distributional contribution is used in the counterexample.

Therefore the same fixed causal Toller bulk support contains group configurations with both nonzero signs of `Omega_sigma`.

### Lane D — boundary and interpretation control

For the unitary control `g=I`, the exact spectrum is `lambda_min=lambda_max=1`, `trace(H)=2`, hence `B(z,I)=0` for every spinor. The strict bulk test correctly rejects this control.

The aggregate hard locks are:

- `exact_bulk_support_global_Omega_projector = false`;
- `both_Omega_sectors_in_same_fixed_causal_bulk_support = true`;
- `boundary_distribution_used_for_counterexample = false`;
- `full_amplitude_interference_conclusion = UNTESTED`;
- `generic_finite_spin_signed_P3_promoted = false`;
- `Iter076N_saddle_selection_unchanged = true`;
- `epsilon_minus1_coefficient_established = false`.

## Interpretation lock

Iter076N remains valid: on the non-degenerate Lorentzian Regge stationary locus, the exact Toller restrictor selects one parity/`Omega_sigma` saddle sector.

Iter076O establishes a different exact finite-spin fact. Away from stationary points, the **Heaviside bulk support itself is not a global orientation projector**. The independent wedge spinors permit the exact source inequalities to be satisfied in open bulk neighborhoods for two group configurations carrying opposite nonzero `Omega_sigma`, while the source causal data are held fixed.

Therefore the generic finite-spin signed Hodge/P3 map cannot be promoted merely from Toller support. Any stronger exact finite-spin orientation selection would have to come from additional structure of the complete integrand or integrated amplitude — phases, damping, magnetic/intertwiner contractions, correlations, or exact interference/cancellation — and must be source-provenanced and prospectively tested separately.

This result does **not** show that both orientation sectors give nonzero net contributions after the full group/spinor integrations. Support overlap is weaker than amplitude survival. Exact cancellation or suppression by the remaining integrand is still an open question.

## Next admissible question

The next finite-spin provenance question is whether the **full exact causal Toller integrand/amplitude**, rather than its support alone, possesses a parity/conjugation/interference relation that eliminates one `Omega_sigma` sector for fixed causal data. If no such exact selector exists, signed P3 must remain explicitly saddle/effective in scope.

## Claim locks

No `NEW_PHYSICS_FOUND`; no complete-QG claim; no generic finite-spin signed P3; no statement that both orientation sectors survive full integration; no nominal `epsilon^-1` coefficient; no physical causal-vertex finiteness/divergence theorem; no F9/G3/G8/K5 promotion.
