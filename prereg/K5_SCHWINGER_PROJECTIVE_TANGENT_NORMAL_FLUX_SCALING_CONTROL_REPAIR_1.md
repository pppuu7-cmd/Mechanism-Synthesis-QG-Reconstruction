# K5 Schwinger projective tangent normal-flux scaling — control repair 1 preregistration

Date: 2026-09-16
Status: PROSPECTIVELY FROZEN BEFORE REPAIR IMPLEMENTATION / OUTPUT
Parent scientific contract: `prereg/K5_SCHWINGER_PROJECTIVE_TANGENT_NORMAL_FLUX_SCALING.md`
Trigger: independent Critic review `results/K5_PROJECTIVE_TANGENT_NORMAL_FLUX_INDEPENDENT_CRITIC_REVIEW.md`, mandatory verdict `INVALID_IMPLEMENTATION` for run 35104985610.

## Scope

This is a control-only implementation repair. It does not alter the parent mathematical hypothesis, success/failure criteria, source ordering, physical interpretation ceiling, or claim locks. It repairs the executable so the already-frozen projective-tangent normal-flux claims are actually falsifiable.

## Frozen implementation obligations

The repaired executable MUST, without hard-coded acceptance exponents:

1. Construct the ambient 10-form `Vol=dalpha_1 wedge ... wedge dalpha_10` and `Omega_9=i_E Vol`, with `E=sum_i alpha_i partial_i`, as exact antisymmetric differential-form data.
2. Construct generic polynomial logarithmic fields `v_i=alpha_i q_i(alpha)` and the projective tangent representative `u=v-(S/s1)E`, `S=sum_i v_i`, and verify exactly `u(s1)=0`.
3. Compute contraction `i_v Omega_9` and independently `i_u Omega_9`; verify exact equality and exact Euler/radial controls `i_E Omega_9=0` and invariance under `v -> v+f(alpha)E` at the contracted-form level.
4. For every `k=1,...,9`, choose proper subsets `Z` of size k and perform an explicit blow-up substitution `alpha_e=t beta_e` for `e in Z` in a genuine projective chart. Pull back the contracted form mechanically, expand in `t`, and extract the lowest nonzero t-order and its exact coefficient. The scalar `t^(k-1)` behavior must emerge from this pullback; it may not be assigned as `k-1` in the decision path.
5. Implement at least two genuinely distinct projective/simplex charts, using different eliminated coordinates/local trivializations, and compare the extracted t-valuations and leading normal coefficients up to the exact orientation/Jacobian relation. A mere edge permutation is not a second chart.
6. Include generic nonradial polynomial `q_i(alpha)` families with exact rational/integer coefficients, plus exceptional cases in which the naively leading `u(t)` coefficient vanishes so that the extractor must advance to the next nonzero t-order.
7. Include representative proper subsets and permutation-related subsets, but keep permutation covariance logically separate from chart equivalence.
8. Keep `Z=empty` and `Z=E(K5)` as provenance/homogeneity firewalls only; neither may produce a physical projective-boundary verdict.
9. Emit machine-readable witnesses sufficient for an independent Critic to reconstruct at least one sample for every k and both charts, including form terms before/after pullback, extracted valuation, leading coefficient, chart identifier, and radial-control result.

## Frozen decision rule

The repair may emit `K5_PROJECTIVE_TANGENT_NORMAL_FLUX_SCALING_EXACT_SCOPED` only if every obligation above is executed and all exact identities agree. Any mathematical disagreement with the parent formula is a scientific failure/counterexample and must be reported as such. Any missing implementation obligation, unsupported chart comparison, hard-coded acceptance path, parser/resource failure, or incomplete witness coverage is `INVALID_IMPLEMENTATION` / infrastructure-numerical failure as appropriate, not a scientific PASS.

## Interpretation firewall

Even a terminal PASS closes only the corrected local projective blow-up geometry sub-gate. It does NOT establish the 34-orbit physical numerator/action-flux valuations, global Stokes authority, an integrated K5 period relation, a physical finite-part selector, F9/G3/G8, or `NEW_PHYSICS_FOUND`. The 34-orbit substantive corner classification remains blocked until this repair is terminal and independently reviewed.
