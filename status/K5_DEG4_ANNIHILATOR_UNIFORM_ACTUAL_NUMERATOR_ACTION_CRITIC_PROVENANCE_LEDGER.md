# Provenance ledger — Critic review of uniform K5 annihilator action

Date: 2026-09-16

## Reviewed Researcher authority

- parent action preregistration `prereg/K5_DEG4_ANNIHILATOR_ACTUAL_DUAL_NUMERATOR_POINTWISE_ACTION.md`, commit `2111b42adc1ab79247c72d0043e5332b24eb7679`;
- Researcher uniform analytic derivation `sources/K5_DEG4_ANNIHILATOR_UNIFORM_ACTUAL_NUMERATOR_ACTION_DERIVATION.md`, commit `d867d215c0c1a9b1777add8eab56749145dbde1e`;
- parent exact action formula `sources/K5_DEG4_ANNIHILATOR_PROJECTIVE_GAUGE_ACTION_DERIVATION.md`, commit `97e71f0c20173b0c387461ff7f860baa12897fcd`;
- independently confirmed annihilator summary from Researcher run `35043883583` and independent Critic run `35044426437`;
- terminal physical numerator DAG run `35044686796`, job `104631868911`, artifact `10426617568`, ZIP digest `sha256:6da2c3346b14aaa2d8d3dd342f6305dcf4896391a3f4ac9153ed86d1dc1b1b45`.

## Researcher action production status

The broader pointwise-action / constant-closure production:

- run `35045552470`;
- head `c78c572669f7ccbabf880b953c631735f2d7c216`;
- job `104634474033`;
- terminal status `completed`, conclusion `cancelled`;
- artifact `10427599407`;
- artifact digest `sha256:42f20555554466348342922c817fe291de7ad470fb41d756df6c0e5bd1e74a99`.

No partial substantive value from that run was used by the Critic. The constant-`2x2` closure question remains unresolved.

## Prospective Critic chronology

Independent Critic review preregistration:

`prereg/K5_DEG4_ANNIHILATOR_UNIFORM_ACTUAL_NUMERATOR_ACTION_INDEPENDENT_CRITIC.md`, commit `5f386aeda775e5513fc37ac5767248f0b561fb45`.

Initial Critic implementation:

`scripts/critic_k5_deg4_annihilator_uniform_actual_numerator_action.py`, initial commit `298cafc8cd6dd0cd8088651df2e2be9dd29cfd28`.

Initial Critic workflow/head `a613b920b0152d072d80580953690268130116d0` produced run `35049778265`, job `104647415957`. The independent reconstruction found the exact factor-ten mismatch but the first decision implementation misclassified scientific disagreement as `INVALID_IMPLEMENTATION`. This run has no controlling review authority.

Prospective control-only classification repair:

`prereg/K5_DEG4_ANNIHILATOR_UNIFORM_ACTUAL_NUMERATOR_ACTION_CRITIC_CONTROL_REPAIR_1.md`, commit `1424f2cce9f4e5669988ef31af11586d101bf1e5`.

Repaired implementation commit:

`debd30a5373b7e469d269abcb21b099fbc1b39e2`.

Repaired workflow/head:

`08ff6b73acb3c73f45d06e169b405315a981b77e`.

Repaired run `35049858473` was queued/non-terminal at the durable review cut and is not required for or consumed by the controlling scientific verdict. If it later becomes terminal, it may be added as an independent machine cross-check without changing the frozen review logic.

## Exact independent witness

The Critic independently reconstructs from terminal parent authority:

- all 10 K5 edges;
- all 220 cubic monomials;
- fixed-edge stabilizer order 12;
- 33 fixed-edge cubic orbits with the parent orbit-size census;
- the emitted 33 annihilator coefficients;
- the 125 coefficient-one spanning trees of `Psi_K5`;
- exact `v(Psi_K5)=0`;
- uniform `q_i=0` and `partial_i q_i=-15` for all edges;
- `div v=-150`;
- terminal full-all-32/100000-source-term numerator values.

At raw `alpha=(1,...,1)`, `s1=10`, so the authoritative formula gives

`B_v[N]=-1500 N`,

not the Researcher `-150 N`.

Correct exact actions:

- channel 1: `10557421875000000000000`;
- channel 2: `8211328125000000000000`.

These are exactly ten times the Researcher witnesses while remaining nonzero.

## Controlling Critic result

`results/K5_DEG4_ANNIHILATOR_UNIFORM_ACTUAL_NUMERATOR_ACTION_ADVERSARIAL_REVIEW.md`, commit `42f769d6330faa52b606d3c64f08e113bc776da3`.

Mandatory verdict: `SCIENTIFIC_FAIL_CONFIRMED`.

The failure is scoped to the Researcher raw-uniform equality/witness normalization. The weaker nonzero-action conclusion survives with corrected normalization.

## Claim locks

No constant-`2x2` closure verdict; no integrated-period relation; no global Stokes theorem; no full 217-dimensional K5 tensor theorem; no reduction of the 377-dimensional supported-extension freedom; no physical finite-part selector; no regulator independence; no G3/F9/G8/K5 promotion; no `NEW_PHYSICS_FOUND`; no complete-QG claim. Historical Iter077E/F remain quarantined and published spectral `i epsilon` is retained.
