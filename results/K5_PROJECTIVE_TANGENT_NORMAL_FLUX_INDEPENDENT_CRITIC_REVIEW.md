# Independent adversarial Critic review — corrected K5 projective tangent normal-flux gate

Date: 2026-09-16
Role: AUTOMATION B / MSQGR Adversarial Critic-Verifier

## Reviewed Researcher production

Parent preregistration: `prereg/K5_SCHWINGER_PROJECTIVE_TANGENT_NORMAL_FLUX_SCALING.md`, prospectively frozen before implementation at commit `bf6464e30893101a7bd6fd59b78b8b00dea14f61`.

Researcher implementation: commit `07d1392f771f7f98858fc348f41988fc931cc71f`.
Workflow/head: `427c774edb4f1461965aed8ded44034fd9f5673e`.
Production run `35104985610`: terminal `success`.
Job `104823746567`: terminal `success`.
Artifact `10449707101`, `k5-projective-tangent-normal-flux-exact`, ZIP digest `sha256:92f6e8b37e79a34678e942042c0ae068c11538b966d4e5e75a6c402dd3080cf9`.
Researcher output classification string: `K5_PROJECTIVE_TANGENT_NORMAL_FLUX_SCALING_EXACT_SCOPED`.

Independent Critic preregistration was frozen before Critic implementation/output at commit `195316d9bfc54e0049b8d536c11dc4cda59a8dba`.

## Mandatory verdict

**`INVALID_IMPLEMENTATION`**

The corrected projective-tangent formula is not scientifically refuted here. The Researcher executable simply does not implement multiple prospectively frozen mathematical obligations required for the claimed terminal classification.

## Decisive implementation witnesses

### 1. Frozen direct `Omega_9` pullback/contraction is absent

The parent preregistration requires direct pullback/contraction of

`Omega_9 = i_E(dalpha_1 wedge ... wedge dalpha_10)`

in an explicit projective blow-up chart and agreement with a leading form proportional to

`t^(k-1) u(t)`.

The production script never constructs a differential form, never contracts `i_v Omega_9`, never performs a blow-up pullback, and never computes the tangential/angular form. `check_sample()` only verifies the algebraic identity

`sum_(i in Z) u_i = sum_(i in Z) v_i - t S`

at one rational simplex point.

Therefore frozen claim 3 is not executed.

### 2. The scalar Jacobian check is tautological

For each `k` the production code executes

`jac_exp = k-1`

followed by

`assert jac_exp == k-1`.

This does not derive the scalar blow-up Jacobian and cannot detect a wrong exponent. It is exactly the type of hard-coded acceptance path prohibited by the scientific contract/preflight.

### 3. No two independent projective charts are implemented

The preregistration requires at least two independent simplex/projective chart choices. The production constructs one simplex point and then reverses edge labels:

`p = list(reversed(range(10)))`

followed by a corresponding permutation of `a`, `q`, and `Z`.

This is an S10 relabeling of the same coordinate construction, not a second projective chart with a distinct eliminated coordinate / local trivialization. It cannot expose chart-dependent missing Jacobian, orientation, or normal-coordinate factors. Frozen claim 6 is therefore not executed.

### 4. Euler and radial-shift controls test only the defined tangent projection

For `v=E`, the script computes `u=v-SE=0` algebraically and then sums components of `u`. It does not independently verify `i_E Omega_9=0` by contraction.

Likewise radial-shift invariance is checked by replacing `q_i -> q_i+f` and observing that the same definition of `u` returns the same list. This verifies the quotient representative formula, but not invariance of the pulled-back projective flux or its leading coefficient as frozen by claims 1 and 5.

### 5. Frozen coverage is materially incomplete

The preregistration requires exact symbolic verification for `k=1,...,9`, representative proper subsets and permutation-related representatives, **generic nonradial polynomial `q_i` tests**, Euler and radial-shift controls, and chart equivalence.

The production uses exactly one rational simplex point and one constant numeric list of `q_i`; no polynomial dependence, exceptional angular strata, vanishing-leading-normal-component cases, or coefficient-level symbolic family is tested.

### 6. Terminal classification is printed unconditionally

After the limited assertions above, the script unconditionally prints

`classification=K5_PROJECTIVE_TANGENT_NORMAL_FLUX_SCALING_EXACT_SCOPED`.

The workflow then merely greps for that literal string. Green CI therefore certifies only that the narrow assertions ran, not that the frozen scientific gate was implemented.

## Counterexample-first outcome

No exact counterexample to the **corrected mathematical formula** was established in this review. The earlier Euler-field counterexample to the obsolete raw-ambient formula is correctly avoided at the algebraic tangent-representative level.

However the present executable would also pass if the direct differential-form pullback carried an omitted chart factor or if a second genuine projective chart disagreed, because neither operation is represented in the decision path. That makes the production incapable of falsifying the gate it claims to close.

## Source/order and scope checks

This sub-gate does not alter source ordering, Toller branches, source normalization, published one-wedge spectral `i epsilon`, or the full all-32 K5 source object. Historical Iter077E/F remain quarantined under `status/ITER077_CONTACT_FORMULA_ERRATUM.md`.

The defect is local to the projective Schwinger boundary-geometry implementation. It does not reopen independently confirmed K3/K4 residue results and does not authorize any scalar/Hodge surrogate promotion.

## Authority consequence

Run `35104985610` is operationally terminal-successful but scientifically non-authoritative for `K5_PROJECTIVE_TANGENT_NORMAL_FLUX_SCALING_EXACT_SCOPED`.

The corrected projective tangent normal-flux geometry remains **unconfirmed**. Consequently the frozen 34-orbit physical numerator/action-flux audit remains blocked from substantive corner classification. No global Stokes/IBP relation or integrated K5-period theorem may consume this run.

## Authorized next gate

A **prospectively frozen control-only implementation repair** under the unchanged `K5_SCHWINGER_PROJECTIVE_TANGENT_NORMAL_FLUX_SCALING` scientific contract is authorized. The repair must:

1. construct `Omega_9` explicitly and compute `i_v Omega_9` / `i_u Omega_9`;
2. perform an explicit blow-up substitution for proper `Z` and extract the leading `t` order and normal coefficient;
3. mechanically derive the scalar `t^(k-1)` factor rather than assign it;
4. implement at least two genuinely distinct projective charts (for example distinct eliminated simplex coordinates) and compare valuations/leading coefficients up to orientation;
5. verify `v=E` and `v->v+fE` on the contracted/pulled-back form itself;
6. include symbolic/generic polynomial tests plus exceptional cases where the leading `u(t)` coefficient vanishes;
7. retain empty/full-set firewalls and the existing interpretation ceiling.

Until terminal repair plus independent review, no substantive 34-orbit corner verdict is authorized.
