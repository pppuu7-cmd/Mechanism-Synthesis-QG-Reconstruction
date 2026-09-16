# K5 34-orbit physical numerator/action-flux audit provenance ledger

Date: 2026-09-17

## Scientific parent

- parent gate: `K5_34_ORBIT_PHYSICAL_NUMERATOR_ACTION_FLUX_AUDIT`;
- prospective parent preregistration: `9c42a26350e547eb02649c6ee44f8dd2477100d0`;
- controlling upstream projective-tangent geometry: independent Critic `CONFIRMED_SCOPED` at `57109026cf5bc95262395a3f42e5f121aa9be3ae`.

## Implementation history

1. Historical first production run `35150430183`, job `104977054981`: implementation failure in one-leading-term determinant inversion; no scientific authority.
2. Repair-1 preregistration `3143586174f977da12afc68218a2dd5064b2e2ab`: frozen but not executed.
3. Repair-2 preregistration `f47ce5a88f98d20f330428480010c3068ebd2328`; implementation `2652c05b2947897d0c953fd9886dc48669c7d8ab`; run `35151178918`, job `104979592873`: `INVALID_IMPLEMENTATION` because `PSI_POLY` exponent vectors were misinterpreted as edge lists.
4. Repair-3 prospective preregistration `a4ee7d25be79079b042b6be9820a4fc264fefc1d`.
5. Repair-3 implementation `ba3c6b62ea25244c04535e816e6dcc1665b1466c`.
6. Terminal workflow/head `9b12eee8d6a6998dcf10ccc53e221e32afc4fd8e`.

No scientific orbit/channel/weight/prime/classifier criterion was changed by repair 3.

## Terminal production

- run: `35151265283`;
- job: `104979878770`;
- workflow conclusion: `success`;
- artifact ID: `10469187008`;
- artifact name: `k5-34-orbit-physical-numerator-action-flux-audit`;
- artifact ZIP SHA256: `5330f15d854f7e52aa67d29c1f8bcd1a9443a8c8d8905d0b9258bf53968404a6`;
- `result.json` SHA256: `432301902a1aaf4ea6d4d345adf6ab738baa606706711be35ab8faa0fe5c75bf`;
- terminal classification: `K5_34_ORBIT_PHYSICAL_NUMERATOR_ACTION_FLUX_PARTIAL_BLOCKED_SCOPED`;
- terminal status: `PASS_EXACT_PARTIAL_BLOCKED_SCOPED`.

## Independent artifact checks

The terminal artifact was downloaded independently and its `result.json` SHA256 recomputed as exactly

`432301902a1aaf4ea6d4d345adf6ab738baa606706711be35ab8faa0fe5c75bf`.

Independent reconstruction from the machine payload gives:

- 34 total S5 orbit rows;
- 32 proper physical orbit rows;
- all orbit sizes sum to 1024;
- proper orbit sizes sum to 1022;
- 64 physical channel-orbit components;
- 0 certified and 64 blocked components;
- 0/64 `rN_certified`;
- 0/64 `rB_rP_certified`;
- 0/64 `uZ_certified`;
- 0/64 S5 numerator/action/projective-normal covariance certificates;
- every final interior/flux/action exponent is null;
- empty/full subsets have `physical=false`;
- all global Stokes/period/finite-part/regulator verdict fields are null;
- all repair-3 authority controls are true.

## Interpretation lock

The terminal result is a valid exact **partial-blocked** audit. It closes the denominator implementation defect but does not resolve the physical numerator/action/projective-normal cancellations. It is not evidence that all corners diverge, that all corners are finite, or that a global Stokes/IBP identity exists.

Durable human-readable result: `results/K5_34_ORBIT_PHYSICAL_NUMERATOR_ACTION_FLUX_AUDIT_RESULT.md` (initial result commit `2e83381a404a64f6aebb5084820039c8f362049c`).