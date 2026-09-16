# AUTOMATION B pre-implementation audit — K5 34-orbit Schwinger physical flux valuation gate

Date: 2026-09-16

Status: **OUTCOME-INDEPENDENT PREFLIGHT ONLY — NO SCIENTIFIC VERDICT**

Controlling prospective Researcher preregistration: `prereg/K5_SCHWINGER_34ORBIT_PHYSICAL_NUMERATOR_ACTION_FLUX_VALUATION_AUDIT.md`, commit `b6580a731c88027dc568672840c4c77333ff7c16`.

This note does not alter the frozen Researcher contract and does not create a competing gate. It records adversarial implementation requirements discovered before any substantive production output exists.

## 1. Projective-boundary versus raw-homogeneous subset scaling

The existing denominator lemma partitions all `2^10=1024` labeled edge subsets into 34 S5 orbits, including the two extreme orbits `Z=empty` and `Z=E(K5)`.

For the projective Schwinger simplex, these two cases are **not ordinary boundary corners**:

- `Z=empty` performs no boundary scaling at all;
- `Z=E(K5)` scales every Schwinger coordinate simultaneously and is a pure common homogeneous/radial scaling, not a projective boundary face after quotient/fixing of overall scale.

A valid implementation may still evaluate both extreme orbits as homogeneity/provenance controls because the frozen contract asks for all 34 orbit types. However, neither extreme orbit may by itself trigger `NONVANISHING_CORNER_FOUND`, `NONINTEGRABLE_CORNER_FOUND`, or defeat `ALL_CORNERS_VANISH`. The physical projective boundary verdict must be based on nonempty proper subsets `empty != Z != E(K5)`, while the two extreme orbits are reported separately as non-boundary controls.

A malformed control should deliberately treat `Z=E(K5)` as a physical projective corner and require the validator to reject that interpretation.

## 2. Exact projective normal-measure exponent must be derived, not guessed

For a proper subset `Z` with `k=|Z|`, simultaneous scaling `alpha_e=t beta_e` for `e in Z` produces several distinct contributions to the boundary exponent:

- `prod_e alpha_e^(1/2)` contributes `k/2`;
- `N_c` contributes `ord_Z N_c`;
- `Psi_K5^(-21/2)` contributes `-(21/2) ord_Z Psi_K5`;
- the projective/blow-up normal measure contributes its own Jacobian power;
- the **normal flux** induced by the vector field may shift the effective power relative to the scalar integrand.

The Researcher preregistration correctly says to combine these explicitly. Automation B therefore freezes the following audit requirement: the implementation must mechanically derive the normal/projective measure power and the flux contraction in one chosen projective chart/blow-up convention and then prove chart-equivalent valuation. It is invalid to insert `k-1`, `k`, or any other measure exponent as an unexplained literal.

A malformed control should shift the measure exponent by one and be rejected by an independent chart/homogeneity identity.

## 3. Exact cancellation valuation cannot be obtained from generic-point sampling

The frozen gate requires exact simultaneous valuation of `N_1`, `N_2` and the action/normal-flux numerator. Because the canonical objects are DAGs with large exact cancellations, valuation must be determined from the lowest nonvanishing homogeneous coefficient after exact collection, not by evaluation at one generic positive `beta` point. A generic point can miss an identically cancelling leading coefficient or hide exceptional angular strata.

For each orbit representative, implementation should produce a hashable exact leading homogeneous coefficient object and certify it is nonzero (or exactly zero before advancing to the next order). At least one malformed fixture with a leading term that cancels only after exact collection should be rejected.

## 4. Orbit covariance must use the physical dual channels

S5 orbit compression is legitimate only if the transported object includes the full boundary dual action. The two invariant dual/covector channels are source-authorized only after transposed Reynolds projection in the non-orthonormal stripped boundary basis. A subset orbit representative may not be transported merely by permuting edge labels while leaving the physical covector data untouched.

The implementation must check that the exact transported `N_c`/flux valuation agrees for every labeled member of each orbit using the actual dual action. Representative-component or scalar-edge permutation alone is insufficient.

## 5. Boundary strata are not automatically K3/K4 collision residues

The already-confirmed K3/K4 simple collision residues vanish, but Schwinger-simplex corners are parameter-space boundary strata of the projective representation. No implementation may use `K3=0` or `K4=0` as an automatic reason to set a Schwinger corner flux to zero. Vanishing must come from the exact frozen numerator/flux valuation at that Schwinger orbit.

## Preflight conclusion

The new 34-orbit preregistration is usable without modification provided the implementation respects the distinctions above. No scientific classification is assigned here. The authoritative next substantive review remains whichever terminal Researcher production occurs first: the already-frozen constant-2x2 action repair/retry or this 34-orbit flux valuation audit.
