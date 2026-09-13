# Iter076L preregistration — can semiclassical Regge 4-volume orientation select the Hodge global sign?

Date: 2026-09-13

## Purpose
Iter076J establishes the unique unsigned K4 complementary-edge support from the source gauge-fixed K5 incidence. Iter076K establishes that the signed lift is exactly the two-element line `+H/-H`, while the exact combinatorial causal data `sigma_a` and `kappa_ab=sigma_a sigma_b` contain no sign-equivariant selector.

The primary-source supplement `sources/CAUSAL_SPINFOAM_VERTEX_2026_REGGE_ORIENTATION_SUPPLEMENT.md` records a distinct source-motivated object available only in the semiclassical Regge sector: five timelike boundary 4-normals `N_a^I`, nonzero 4-volume, and the proper-vertex remark that a 4-volume orientation constraint selects a single critical point.

This prospective gate asks a sharply scoped mathematical/provenance question: **does oriented Regge 4-volume provide exactly the missing odd-relabeling pseudoscalar needed to choose one of `+H/-H`, while remaining only a semiclassical selector rather than an exact Eq.(4) P3?**

No production output exists at preregistration time. Frozen criteria below may not be changed after viewing results.

## Source authority and scope
Use only:
1. the exact Iter076K Hodge line and oriented-edge representation;
2. source-defined semiclassical Regge boundary normals `N_a^I` of a non-degenerate Lorentzian 4-simplex;
3. the source separation between combinatorial `sigma_a` and Regge causal/geometric data;
4. the source statement that the causal/proper-vertex relation through 4-volume orientation remains to be clarified.

The Regge 4-volume orientation may be used as a semiclassical orientation datum. It must **not** be inserted into the exact Eq.(4) causal amplitude or promoted to physical P3 by this gate.

## Frozen object
For gauge root `r`, let the remaining four tetrahedral labels be `U_r=(i,j,k,l)`. Define an oriented-volume sign abstractly by

`omega_r = sign epsilon_IJKL X_i^I X_j^J X_k^K X_l^L`,

for any source-compatible non-degenerate oriented four-vector realization `X` representing the corresponding semiclassical 4-simplex orientation data. Only its transformation law is tested: under a permutation `p` of the four unfixed labels,

`omega_r -> sgn(p) omega_r`.

The actual normalization and Lorentz-frame coordinates are irrelevant. Degenerate `omega_r=0` configurations are outside the frozen source sector because the source asymptotics assume non-vanishing 4-volume.

## Independent frozen lanes

### Lane A — orientation character
Verify exhaustively on `S4` that the determinant/Levi-Civita orientation sign transforms by the sign character:

`omega(p.X)=sgn(p) omega(X)`.

PASS iff all `24/24` permutations obey the law, with exactly `12` preserving and `12` flipping orientation.

### Lane B — Hodge-line selection
Take the two Iter076K lifts `+H` and `-H`. Define the semiclassical selector

`H_omega = omega H`.

PASS iff `H_omega` obeys the frozen twisted covariance law and orientation reversal `omega -> -omega` exchanges the two and only the two admissible lifts. Reject an orientation-blind same-sign selector.

### Lane C — gauge-root covariance
For all five gauge roots, transport the oriented-volume selector and K4 complement/Hodge structure under full source-node relabelings. PASS iff the family is covariant provided the orientation variable is transported as a pseudoscalar, and fails the deliberately wrong control in which `omega` is held fixed under odd relabelings.

### Lane D — provenance/scope firewall
Check the source-scope assertions as frozen metadata controls:
- combinatorial `sigma/kappa` and Regge orientation are distinct source levels;
- the bridge to Regge geometry is semiclassical;
- the paper does not establish the proper-vertex 4-volume orientation as an exact Eq.(4) selector;
- therefore a successful A-C result is `SEMICLASSICAL_ONLY` and cannot promote physical signed P3.

PASS iff all four scope controls are true. Any implementation that labels a positive A-C result as exact Eq.(4) P3 must fail this lane.

## Frozen interpretation
If A-D pass, classify:

`ITER076L_REGGE_4VOLUME_ORIENTATION_SELECTS_HODGE_SIGN_SEMICLASSICAL_EXACT_BRIDGE_STILL_BLOCKED_SCOPED`

Meaning: the source-motivated semiclassical oriented 4-volume has exactly the missing pseudoscalar transformation character and can select `+H` versus `-H` at the Regge boundary level, but this does not establish that the exact causal Eq.(4) integrand supplies that selector. Physical P3 remains blocked on an exact contraction/orientation bridge.

If A-C fail, classify:

`ITER076L_REGGE_4VOLUME_ORIENTATION_DOES_NOT_SELECT_HODGE_SIGN_REVIEW`

If D fails because an exact source bridge is actually identified, classify:

`ITER076L_EXACT_ORIENTATION_BRIDGE_FOUND_REQUIRES_INDEPENDENT_SOURCE_REVIEW`

and require a new prospective gate before P3 promotion.

Technical/runtime errors are `INFRASTRUCTURE_OR_NUMERICAL_FAIL`, not scientific FAIL.

## Claim locks
Even a full PASS does not establish physical signed P3, the exact source numerator/Jacobian quadratic jet, the nominal `epsilon^-1` coefficient, causal-vertex finiteness/divergence, F9/G3/G8/K5, physical sector selection, complete QG, or new physics.
