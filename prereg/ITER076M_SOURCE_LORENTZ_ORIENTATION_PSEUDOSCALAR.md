# Iter076M preregistration — source Lorentz-frame orientation pseudoscalar for the Hodge global sign

Date: 2026-09-13

## Administrative provenance
This is an identifier-only continuation of the previously committed, never-produced candidate gate `prereg/ITER076L_SOURCE_LORENTZ_ORIENTATION_PSEUDOSCALAR.md`. That file collided with the already controlling Iter076L semiclassical Regge-volume gate. The scientific object, lanes, thresholds, and claim locks below are unchanged; only the iteration identifier is moved to Iter076M before any production implementation or output for this candidate.

## Purpose
Iter076K establishes that the gauge-fixed K5 incidence plus source causal data `sigma_a`/`kappa_ab` fix the Hodge line and twist character but do not select the global sign between `+H` and `-H`. Iter076L then shows that Regge 4-volume orientation has exactly the required pseudoscalar character, but only semiclassically; an exact Eq.(4)-level bridge remains blocked.

The Lorentzian proper-vertex source structure gives a candidate object class directly on the group variables: future timelike vectors `F_a = Xhat_a T`, with `T=(1,0,0,0)`, are standard EPRL/proper-vertex variables, and single four-dimensional Levi-Civita contractions of these vectors occur explicitly in the proof underlying the proper-vertex sign `beta_ab`.

This prospective gate tests whether the causal signs `sigma_a`, together with the full source group variables already present in the 2026 causal Eq.(4) integral, define a relabeling-covariant global pseudoscalar that can select one of the two Hodge lifts.

No Iter076M production output exists at preregistration time. Frozen criteria below may not be changed after viewing results.

## Source authority and scope
Use only:
1. `sources/CAUSAL_SPINFOAM_VERTEX_2026_SOURCE_SNAPSHOT.md` for the five causal edge labels, `sigma_a`, group variables `g_a in SL(2,C)`, gauge fixing `g_1=1`, and relative-group structure;
2. `sources/LORENTZIAN_PROPER_VERTEX_ORIENTATION_2016_SOURCE_SNAPSHOT.md` for the standard EPRL/proper-vertex vectors `F_a = Xhat_a T`, common-left proper-Lorentz gauge action, and explicit Levi-Civita orientation contractions.

No proper-vertex projector or extra dynamics may be imported into the causal vertex. Only the orientation-covariant group-variable object class is admitted.

## Frozen candidate
For each source node `a`, define

`F_a := ghat_a T`,

with `T=(1,0,0,0)`. Define

`Delta_sigma(g) := det( [ 1 1 1 1 1 ; sigma_1 F_1 sigma_2 F_2 sigma_3 F_3 sigma_4 F_4 sigma_5 F_5 ] )`.

Equivalently, for any root `r`, column subtraction gives

`Delta_sigma = (-1)^(r-1) det( sigma_a F_a - sigma_r F_r )_{a != r}`

with the induced ordered complementary columns.

Define

`Omega_sigma(g) := sgn Delta_sigma(g)`

only when `Delta_sigma != 0`. No arbitrary sign is assigned at `Delta_sigma=0`.

## Independent frozen lanes

### Lane A — algebraic covariance and redundancy
Prove/test exactly that:
1. simultaneous common-left `SO+(3,1)` transformation of all `F_a` leaves `Delta_sigma` invariant;
2. global causal reversal `sigma_a -> -sigma_a` leaves `Omega_sigma` invariant;
3. any `p in S5` gives `Omega_sigma(p.g,p.sigma)=sgn(p) Omega_sigma(g,sigma)` on the nonzero locus;
4. all five root-expanded determinant formulas agree with the prescribed cofactor sign.

PASS iff all identities hold exactly on deterministic exact-rational controls with all `120` S5 permutations and all five roots.

### Lane B — non-degenerate Regge reconstruction control
Construct at least two non-degenerate timelike-normal configurations with positive closure weights such that `sigma_a F_a` forms a consistently oriented closed normal family. Verify:
1. `Delta_sigma != 0`;
2. all `120` S5 relabelings obey the sign character;
3. common proper-Lorentz transformations preserve the sign;
4. a genuine parity-reflected control flips the sign and is not an `SO+(3,1)` gauge transformation.

PASS iff all controls behave as preregistered.

### Lane C — relation to proper-vertex pair sign
On the same non-degenerate controls compute individual four-dimensional contractions

`E_a := epsilon(F_b,F_c,F_d,F_e)`

and the pair-product structure entering `beta_ab`.

PASS iff:
1. pair quantities are orientation-even under global orientation reversal while individual `E_a` are orientation-odd;
2. `Omega_sigma` is orientation-odd and therefore retains information absent from pairwise `beta_ab` products;
3. there is no contradiction with the source relation `beta_ab = -epsilon_a epsilon_b` on reconstructed non-degenerate data.

This is provenance/compatibility only and must not claim the causal vertex contains the proper-vertex projector.

### Lane D — degeneracy and no-overclaim controls
Generate `Delta_sigma=0` controls by coalescing or affinely dependent weighted normals. Verify `Omega_sigma` is explicitly undefined, not fitted or regularized. Verify that omitting the `sigma_a` weights can change the selector and that raw label-order Levi-Civita sign alone is not treated as physical data.

PASS iff the implementation reports the degeneracy locus separately and never assigns a physical sign there.

## Frozen classification
If A-D pass, classify:

`ITER076M_SOURCE_GROUP_AND_CAUSAL_DATA_DEFINE_NONDEGENERATE_GLOBAL_ORIENTATION_PSEUDOSCALAR_REVIEW_P3_SCOPED`

Meaning: the exact Eq.(4) source variable set `(g_a,sigma_a)` admits a gauge-invariant, global-reversal-invariant, S5 sign-equivariant pseudoscalar on the non-degenerate locus, sufficient mathematically to choose between `+H` and `-H`. This is still not physical P3 promotion: a subsequent provenance gate must show that this exact `Omega_sigma` or an equivalent contraction-derived sign is actually selected by the causal amplitude's contraction/intertwiner structure rather than merely available as a function of integration variables.

If A/B fail, classify `ITER076M_CANDIDATE_ORIENTATION_PSEUDOSCALAR_REJECTED_SCOPED`.
If C reveals incompatibility, classify `ITER076M_PROPER_VERTEX_ORIENTATION_COMPATIBILITY_FAIL_SCOPED`.
Technical/runtime errors are `INFRASTRUCTURE_OR_NUMERICAL_FAIL`, not scientific FAIL.

## Claim locks
Even full PASS does not establish physical `SOURCE_TO_K4_PUSHFORWARD`, the source numerator/Jacobian quadratic jet, nominal `epsilon^-1` coefficient, causal-vertex finiteness/divergence, F9, G3, G8, K5, physical sector selection, complete QG, or new physics. No fitted sign, counterterm, sequential-order prescription, or replacement of the source spectral `i epsilon` is authorized.
