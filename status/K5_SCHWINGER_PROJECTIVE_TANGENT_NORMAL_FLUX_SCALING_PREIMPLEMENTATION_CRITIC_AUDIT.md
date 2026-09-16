# AUTOMATION B pre-implementation Critic audit — corrected K5 projective tangent normal-flux scaling

Date: 2026-09-16
Authority cut: `bf6464e30893101a7bd6fd59b78b8b00dea14f61`
Prospective Researcher preregistration: `prereg/K5_SCHWINGER_PROJECTIVE_TANGENT_NORMAL_FLUX_SCALING.md`, commit `bf6464e30893101a7bd6fd59b78b8b00dea14f61`.

This note is outcome-independent preparation only. No Researcher implementation, production run, artifact, or substantive result exists at this authority cut, so no competing scientific verdict is assigned.

## Contract consistency

The successor gate correctly repairs the previously falsified raw-ambient flux statement by working with the projective class modulo the Euler field. With

`Omega_9=i_E(dalpha_1 wedge ... wedge dalpha_10)`, `E=sum_i alpha_i partial_i`,

one has exactly `i_E Omega_9=0`, hence `i_(v+fE)Omega_9=i_vOmega_9`. The simplex-tangent representative

`u=v-(S/s1)E`, `S=sum_i v_i`, `s1=sum_i alpha_i`,

satisfies `u(s1)=0`, and is invariant under the replacement `v -> v+fE` after the corresponding change in `S`.

For a proper nonempty subset `Z`, `t=sum_(e in Z) alpha_e`, the candidate projective normal component is therefore

`u(t)=v(t)-t*S/s1`.

The already-confirmed scalar blow-up Jacobian `t^(k-1)` is compatible with the standard simplex blow-up coordinates `alpha_e=t beta_e` for `e in Z`, `sum_Z beta_e=1`; however the future implementation must derive the full contracted form rather than infer flux from the scalar Jacobian alone.

## Mandatory implementation firewalls

1. **No hard-coded geometry booleans.** Horizontality, tangency, chart equivalence, Euler-zero flux and radial-shift invariance must be derived from explicit differential-form pullback/contraction, not literal `True` predicates.
2. **Direct form calculation.** At least one chart must construct `Omega_9`, contract with the actual symbolic `v`, impose/project to `s1=1`, perform the blow-up substitution, and extract the coefficient of the boundary tangential form. A second genuinely distinct chart/elimination choice must reproduce the valuation and vanishing/nonvanishing result.
3. **Euler counterexample control.** `q_i=1`, hence `v=E`, must give identically zero projective flux for every proper `k=1,...,9` corner even though raw `v(t)=t` is nonzero. Any validator accepting nonzero flux here is invalid.
4. **Radial-shift invariance control.** For a generic nonradial polynomial test field `v`, choose nonzero polynomial `f` and verify coefficient-level equality of the projective flux for `v` and `v+fE`; merely comparing final exponents is insufficient.
5. **Normal-component control.** The implementation must mechanically compute both `v(t)` and `S`, and show that the extracted boundary coefficient agrees with `u(t)=v(t)-tS/s1`; it must not inject this identity as an expected literal before the independent pullback calculation.
6. **Scalar-vs-flux distinction.** `t^(k-1)` is a measure/Jacobian factor, not by itself the flux valuation. If `u(t)` vanishes to additional order, that extra order must be retained.
7. **Projective-corner firewall.** `Z=empty` and the full 10-edge set remain homogeneity/provenance controls only and must never be classified as physical boundary corners.
8. **Exceptional strata.** Charts must not divide by an angular coordinate without either covering the complementary chart or proving that the omitted locus cannot alter valuation/vanishing. Rank-deficient angular choices are explicit adversarial targets.
9. **No K3/K4 boundary identification.** Confirmed K3/K4 collision residue zeros do not automatically cancel Schwinger projective corner fluxes.
10. **No downstream promotion.** Even a terminal PASS of this geometry gate authorizes only the corrected flux geometry needed by the already-frozen 34-orbit audit; it does not establish any corner classification, Stokes theorem, K5 period, finite part, regulator independence, F9/G3/G8, or physical amplitude.

## Counterexample-first tests to require

- `v=E` (mandatory zero-flux witness against raw `v(t)` logic);
- `v=fE` for nonconstant homogeneous polynomial/rational `f` where defined;
- a generic nonradial diagonal-log field with `S != 0` so that `u(t)` differs nontrivially from `v(t)`;
- a tangent field with `S=0`, where `u=v`, as a positive structural control;
- a field for which `u(t)` vanishes to first or higher order although `v(t)` does not, to ensure the implementation tracks valuation rather than only a binary flux flag;
- two chart choices with different eliminated simplex coordinates and at least one chart transition crossing a potential angular-coordinate zero.

## Authority consequence at this cut

The corrected gate is prospectively frozen and mathematically well-posed at contract level, but it has no scientific result yet. The 34-orbit physical numerator/action-flux audit remains barred from substantive corner classification until this gate reaches terminal production and receives an independent Critic review. The constant-`2x2` action repair remains an independent admissible front.
