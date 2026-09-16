# K5 Schwinger projective-tangent normal-flux scaling — prospective gate

Status: FROZEN BEFORE IMPLEMENTATION.

## Motivation
The earlier raw-ambient `v(t)` normal-flux identity is scientifically invalid because `Omega_9=i_E Vol` is horizontal (`i_E Omega_9=0`). This successor gate replaces only that failed geometry statement. It does not alter the already-confirmed scalar blow-up Jacobian `t^(k-1)` and does not classify any physical K5 corner.

## Frozen object
Let `E=sum_i alpha_i partial_i`, `s1=sum_i alpha_i`, `Omega_9=i_E(dalpha_1 wedge ... wedge dalpha_10)`, and let `v=sum_i v_i partial_i` with `v_i=alpha_i q_i(alpha)`. Put `S=sum_i v_i`. On the simplex chart `s1=1`, define the projective tangent representative

`u = v - (S/s1) E`.

For a proper nonempty edge subset `Z` with `k=|Z|` and blow-up coordinate `t=sum_(e in Z) alpha_e`, define

`u(t)=v(t)-t*S/s1`, where `v(t)=sum_(e in Z) v_e`.

## Frozen claims to test exactly
1. Horizontality/radial invariance: `i_(v+fE) Omega_9 = i_v Omega_9` for polynomial/rational homogeneous test data where defined.
2. Simplex tangency: `u(s1)=0` exactly.
3. Correct normal component: direct pullback/contraction of `i_v Omega_9` in an explicit projective blow-up chart agrees, up to the chart orientation sign, with a nonzero tangential/angular form times `t^(k-1) * u(t)`; no raw `v(t)` substitution is allowed.
4. Euler control: for `v=E`, the projective flux is identically zero in every proper corner chart.
5. Radial-shift control: replacing `v` by `v+fE` leaves the projective normal-flux valuation and leading coefficient unchanged after canonical chart normalization.
6. Chart equivalence: at least two independent simplex/projective chart choices give the same valuation for each tested `k`; orientation signs may differ but vanishing/order may not.
7. Scalar Jacobian control: the already-established scalar measure factor remains `t^(k-1)` for `k=1,...,9`.
8. Full-set/empty-set firewall: `Z=empty` and `Z=E(K5)` are provenance/homogeneity controls, not physical projective boundary corners.

## Coverage
Exact symbolic verification for `k=1,...,9`, including representative proper subsets and permutation-related representatives. Include generic nonradial polynomial `q_i` tests plus the mandatory Euler and radial-shift controls. No floating-point-only theorem.

## Frozen classifications
- `K5_PROJECTIVE_TANGENT_NORMAL_FLUX_SCALING_EXACT_SCOPED` only if every exact identity, chart-equivalence check, and adversarial control passes.
- `SCIENTIFIC_FAIL` if a frozen mathematical identity fails with exact arithmetic.
- `INFRASTRUCTURE_OR_NUMERICAL_FAILURE` if execution/resource/tooling prevents an exact verdict.

## Claim firewall
Passing this gate establishes only corrected projective normal-flux geometry. It does NOT establish `ALL_CORNERS_VANISH`, `NONVANISHING_CORNER_FOUND`, global Stokes/IBP authority, either K5 projective period, a physical finite-part selector, F9/G3/G8, `NEW_PHYSICS_FOUND`, or complete quantum gravity. The 34-orbit physical numerator/action-flux audit remains blocked from substantive classification until this gate is terminal and independently reviewed.
