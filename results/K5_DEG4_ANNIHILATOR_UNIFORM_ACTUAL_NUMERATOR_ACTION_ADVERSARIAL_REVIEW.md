# AUTOMATION B adversarial review — uniform action of the confirmed K5 degree-four annihilator on the actual invariant-dual numerators

Date: 2026-09-16

Mandatory verdict: **`SCIENTIFIC_FAIL_CONFIRMED`**

## Result reviewed

Reviewed Researcher derivation:

`sources/K5_DEG4_ANNIHILATOR_UNIFORM_ACTUAL_NUMERATOR_ACTION_DERIVATION.md`, commit `d867d215c0c1a9b1777add8eab56749145dbde1e`.

Prospective parent action contract:

`prereg/K5_DEG4_ANNIHILATOR_ACTUAL_DUAL_NUMERATOR_POINTWISE_ACTION.md`, commit `2111b42adc1ab79247c72d0043e5332b24eb7679`.

The Researcher derivation claims at the raw uniform point `alpha=(1,...,1)`:

`q_i=0`, `partial_i q_i=-15`, `v_i=0`, `div v=-150`,

then concludes

`B_v[N_c](1,...,1)=-150 N_c(1,...,1)`

with exact witnesses

`1055742187500000000000`,

`821132812500000000000`.

The weaker qualitative conclusion asserted from those numbers is that the confirmed Kirchhoff annihilator does not algebraically annihilate either actual invariant-dual numerator identically.

## Exact counterexample to the Researcher equality

The already-authoritative projective-gauge identity is

`B_v[N] = s1 v(N) + {s1[div v +(1/2)sum_i q_i] - 3S} N`,

where `s1=sum_i alpha_i`, `v_i=alpha_i q_i`, and `S=sum_i v_i`.

At the Researcher-specified raw uniform point `alpha=(1,...,1)` one has **`s1=10`**, not one.

An independent exact reconstruction of the confirmed 33-orbit annihilator representative gives, for every one of the ten edges,

`q_i=0`, `partial_i q_i=-15`.

Therefore

`v_i=0`, `S=0`, `v(N_c)=0`, `sum_i q_i=0`, `div v=-150`.

Substitution into the frozen exact action formula gives

`B_v[N_c](1,...,1) = 10*(-150) N_c(1,...,1) = -1500 N_c(1,...,1)`.

Using the terminal full-all-32 invariant-dual numerator values

`N_1=-7038281250000000000`,

`N_2=-5474218750000000000`,

the correct exact actions are

`B_v[N_1]=10557421875000000000000`,

`B_v[N_2]=8211328125000000000000`.

Both differ from the Researcher witnesses by an exact factor of ten.

This is not a convention-only difference that can be silently repaired. The Researcher text evaluates the terminal numerators at raw `alpha=(1,...,1)` while using the `s1=1` simplex simplification for `B_v`; those two gauges cannot be mixed because `N` and `B_v` have different homogeneous degrees.

## Independent reconstruction / controls

Prospective Critic preregistration:

`prereg/K5_DEG4_ANNIHILATOR_UNIFORM_ACTUAL_NUMERATOR_ACTION_INDEPENDENT_CRITIC.md`, commit `5f386aeda775e5513fc37ac5767248f0b561fb45`.

Independent Critic implementation initially reconstructed, without consuming the Researcher action witnesses as mathematical inputs:

- 10 K5 edges;
- all 220 cubic monomials;
- the order-12 fixed-edge stabilizer;
- the complete 33-orbit basis with the exact parent orbit-size census;
- the emitted 33 annihilator coefficients;
- the 125 coefficient-one spanning-tree polynomial `Psi_K5`;
- exact polynomial identity `v(Psi_K5)=0`;
- `q_i=0` for all 10 edges;
- `partial_i q_i=-15` for all 10 edges;
- `div v=-150`;
- the terminal full-32/100000-source-term numerator object and exact terminal uniform numerator values.

Historical Critic run `35049778265`, job `104647415957`, exposed the exact factor-ten contradiction but classified it as `INVALID_IMPLEMENTATION` because the first Critic decision code incorrectly required agreement with the Researcher target as part of implementation validity. That Critic classification is itself non-authoritative and was repaired prospectively.

Control-only Critic repair:

`prereg/K5_DEG4_ANNIHILATOR_UNIFORM_ACTUAL_NUMERATOR_ACTION_CRITIC_CONTROL_REPAIR_1.md`, commit `1424f2cce9f4e5669988ef31af11586d101bf1e5`.

The repair changes only classification logic: a valid exact contradiction now maps to the preregistered `SCIENTIFIC_FAIL_CONFIRMED` branch. Repaired implementation commit `debd30a5373b7e469d269abcb21b099fbc1b39e2`; repaired workflow/head `08ff6b73acb3c73f45d06e169b405315a981b77e`. Repaired Critic run `35049858473` was queued/non-terminal at the durable-review cut and is **not** used as authority for this verdict.

The exact contradiction above is already independently determined by repository-terminal parent formulas and exact arithmetic. No partial value from the cancelled Researcher action run is used.

## Researcher production status firewall

The broader forward-mode action / constant-`2x2` closure production `35045552470`, job `104634474033`, has now terminated `cancelled`; artifact `10427599407` exists with digest `sha256:42f20555554466348342922c817fe291de7ad470fb41d756df6c0e5bd1e74a99` because the workflow uploads artifacts on `always()`.

No partial substantive value from that cancelled computation is consumed here. Consequently the frozen constant-`2x2` closure question remains unresolved.

## Scientific consequence

The exact Researcher theorem **as written** is false: the raw-uniform action is `-1500 N`, not `-150 N`.

However the weaker one-sided conclusion survives and is in fact strengthened numerically: both corrected exact actions remain nonzero. Therefore the confirmed degree-four Kirchhoff annihilator is still proven not to algebraically annihilate either physical invariant-dual numerator identically, but the two Researcher witness integers and their normalization are non-authoritative.

This review does not reopen the independently confirmed existence of the Kirchhoff annihilator or the terminal degree-27 numerator DAG.

## Source/order, boundary and surrogate audit

The reviewed object is the correct full source object at this layer: the terminal numerator authority retains all 32 boundary components and exactly 100000 source node-choice terms, with the dual/covector Reynolds rank-two projection. No representative `00000` component is substituted. The source-order firewall remains

`one-wedge spectral/spinor integration -> Toller function -> ten-Toller product -> full boundary contraction -> K5 group/distributional object`.

The published spectral `i epsilon` is untouched. Historical Iter077E/F remain quarantined under `status/ITER077_CONTACT_FORMULA_ERRATUM.md`.

## Verdict

**`SCIENTIFIC_FAIL_CONFIRMED`**

Scope of failure: only the exact Researcher uniform action equality and quoted witness normalization in commit `d867d215...`.

Retained scoped fact: the action is exact nonzero on both physical invariant-dual channels at uniform, with corrected values ten times larger.

## Authorized next gate

Do not rewrite the old derivation/result. The next Researcher action computation must be a prospectively frozen **control-only normalization/performance repair/retry** under the unchanged parent action contract, explicitly distinguishing raw homogeneous coordinates from the simplex gauge and checking homogeneity of `N` and `B_v` before any frozen-point comparison.

Because run `35045552470` was cancelled, the constant-`2x2` closure classification remains `?`. A repaired implementation may target that still-open part, while retaining the already-corrected nonzero uniform witness as a control rather than recomputing it as a new scientific claim.

Independently, a prospectively frozen 34-orbit higher-codimension Schwinger-corner audit remains high-value. No projective total derivative may be promoted to an integrated-period relation until that boundary/Stokes authority is terminal and independently reviewed.
