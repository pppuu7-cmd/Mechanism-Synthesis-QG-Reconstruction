# K5 34-orbit exact leading-coefficient cancellation resolution

Status: **PROSPECTIVELY FROZEN BEFORE OUTCOME**.

## Motivation

The terminal parent audit `K5_34_ORBIT_PHYSICAL_NUMERATOR_ACTION_FLUX_PARTIAL_BLOCKED_SCOPED` has valid denominator/projective geometry coverage but certifies `0/64` physical channel-orbit components. All 64 remain `BLOCKED_CANCELLATION_RESOLUTION`. Global Stokes/IBP is therefore still inadmissible.

This gate resolves only that blocker. It does not change the physical model or enlarge the channel space.

## Frozen parent authority

- terminal parent result: `results/K5_34_ORBIT_PHYSICAL_NUMERATOR_ACTION_FLUX_AUDIT_RESULT.md`;
- parent production run `35151265283`, job `104979878770`, artifact `10469187008`;
- parent result JSON SHA256 `432301902a1aaf4ea6d4d345adf6ab738baa606706711be35ab8faa0fe5c75bf`;
- same 32 proper S5 orbit representatives; empty/full subsets remain controls only;
- same two physical invariant-dual channels;
- same canonical degree-27 numerator DAG/all-32 parent authority;
- same degree-four annihilator action and corrected projective-tangent representative;
- same S5 edge action and orientation conventions.

## Frozen mathematical objective

For every proper orbit representative `Z` and both physical channels, determine the actual lowest nonzero `t` coefficient/order, or prove exact zero within the complete a priori degree support, for:

1. `N_c(alpha(t))`;
2. the projective degree-matched annihilator action `P_v[N_c]=B_v[N_c]/s1^4` (equivalently record the polynomial `B_v[N_c]` before division);
3. the projective normal polynomial numerator used for `u_Z`.

The one-leading-term `LT` approximation is not an admissible certificate for this gate.

## Bounded exact representation

Before any validation outcome, freeze a finite coefficient representation in `t` whose maximum order is implied by the authoritative polynomial/rational degree structure, not by observed cancellations.

Required ceilings:

- `N_c`: polynomial degree at most 27 in the alpha variables, hence after the frozen linear corner substitution retain all possible `t` coefficients through order 27;
- `B_v[N_c]`: degree 31, retain all possible `t` coefficients through order 31;
- projective normal polynomial numerator: derive and record its exact degree ceiling from the frozen `u` formula before production, then retain the complete coefficient support through that ceiling;
- `Psi`: continue using the exact authoritative 125-tree polynomial and its independently verified order; it is a control, not the unresolved target.

Exact rational/integer arithmetic is preferred. If modular reconstruction is used, primes must be frozen prospectively, reconstruction bounds stated before outcome, and exact-zero certification must not rely on one prime or one witness.

## Frozen witnesses and covariance

Use the same two asymmetric weight assignments already frozen by the parent audit and the same K5/S5 cyclic permutation control. For each target object:

- extract the complete coefficient vector up to the frozen ceiling;
- locate the first exact nonzero coefficient mechanically;
- distinguish exact polynomial zero from a finite higher-order cancellation;
- transport the full coefficient object under the frozen S5 permutation before comparing, rather than comparing only an uncertified leading monomial;
- independently reconstruct at least one representative from every orbit-size/collision-size class by a second implementation path.

No weight, representative, prime, degree ceiling, basis, normalization, or S5 map may be changed after viewing production coefficients.

## Terminal classifier

`INVALID_IMPLEMENTATION` if the complete bounded coefficient support is not actually evaluated, if authority/coverage/covariance controls fail, or if exact-zero claims exceed the frozen reconstruction guarantee.

`K5_34_ORBIT_EXACT_LEADING_COEFFICIENT_CANCELLATION_RESOLUTION_PARTIAL_BLOCKED_SCOPED` if implementation is valid but any required channel-orbit target remains uncertified.

`K5_34_ORBIT_EXACT_LEADING_COEFFICIENT_CANCELLATION_RESOLUTION_EXACT_SCOPED` only if every required physical numerator/action/projective-normal order is exactly resolved for all 64 channel-orbit components and all frozen S5 covariance controls pass.

No local finite/divergent label is authorized for unresolved components. No global Stokes/IBP, integrated-period, finite-part, regulator-independence, complete-amplitude, or downstream-QG conclusion is authorized by this gate alone.

## Downstream unlock

Only a terminal exact resolution sufficient to populate the previously null local exponents may return to the 34-orbit integrability/flux classifier. Global Stokes/IBP remains a separate prospective gate after that local classification is valid.