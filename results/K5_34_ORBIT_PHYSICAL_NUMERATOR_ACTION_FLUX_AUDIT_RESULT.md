# K5 34-orbit physical numerator/action-flux audit — terminal result

Date: 2026-09-17

## Terminal classification

`K5_34_ORBIT_PHYSICAL_NUMERATOR_ACTION_FLUX_PARTIAL_BLOCKED_SCOPED`

Status: `PASS_EXACT_PARTIAL_BLOCKED_SCOPED`.

This is a valid terminal **partial-blocked** result. It is not a scientific falsification of the K5 object, not a divergence theorem, and not a global Stokes/IBP result.

## Frozen authority

Parent prospective gate preregistration: `9c42a26350e547eb02649c6ee44f8dd2477100d0`.

Execution-only repairs were kept separate from scientific interpretation:

- repair 1 preregistration `3143586174f977da12afc68218a2dd5064b2e2ab` was not executed;
- repair 2 preregistration `f47ce5a88f98d20f330428480010c3068ebd2328` replaced the signed-determinant leading-term path by direct evaluation of the authoritative 125-tree Kirchhoff polynomial plus cofactor inverse;
- repair 2 production `35151178918` / job `104979592873` was `INVALID_IMPLEMENTATION` because the wrapper misread the authoritative `PSI_POLY` monomial key as an edge list rather than a 10-component exponent vector;
- repair 3 was prospectively frozen at `a4ee7d25be79079b042b6be9820a4fc264fefc1d` before repair-3 production and changed only that exponent-vector interpretation.

Repair-3 implementation commit: `ba3c6b62ea25244c04535e816e6dcc1665b1466c`.

Terminal workflow/head commit: `9b12eee8d6a6998dcf10ccc53e221e32afc4fd8e`.

## Production authority

- GitHub Actions run: `35151265283`;
- job: `104979878770`;
- conclusion: `success`;
- artifact: `10469187008` (`k5-34-orbit-physical-numerator-action-flux-audit`);
- artifact ZIP SHA256: `5330f15d854f7e52aa67d29c1f8bcd1a9443a8c8d8905d0b9258bf53968404a6`;
- production `result.json` SHA256: `432301902a1aaf4ea6d4d345adf6ab738baa606706711be35ab8faa0fe5c75bf`.

The workflow completed the exact audit, validated the outcome-neutral payload, and uploaded the terminal artifact.

## Exact coverage and controls

The machine payload contains exactly 34 S5 edge-subset orbits. Exactly 32 are proper physical corner orbits; the empty subset and full ten-edge subset remain controls only.

Independent artifact reconstruction verifies:

- all 34 orbit sizes sum to `1024`, covering the complete ten-edge subset space;
- the 32 proper-orbit sizes sum to `1022`;
- there are exactly 64 physical channel-orbit components (`32` proper orbits x `2` invariant-dual channels);
- all repair-3 authority checks are true;
- direct authoritative-tree `Psi` order agrees with the independently computed combinatorial spanning-tree order on every proper orbit;
- the generic no-cancellation control gives exact agreement between direct-tree `Psi` and the signed determinant;
- `Psi` authority has exactly 125 unit-coefficient spanning-tree monomials represented by 10-component exponent vectors.

Thus the previous denominator crash is closed as an implementation artifact. The Kirchhoff-denominator order is not the remaining blocker.

## Scientific payload

The frozen cancellation/covariance certificate does **not** certify any physical channel-orbit component:

- certified channel-orbit components: `0 / 64`;
- blocked channel-orbit components: `64 / 64`;
- interior classifications: `64 x BLOCKED_CANCELLATION_RESOLUTION`;
- flux classifications: `64 x BLOCKED_CANCELLATION_RESOLUTION`;
- annihilator-action classifications: `64 x BLOCKED_CANCELLATION_RESOLUTION`.

Independently recomputed from the artifact:

- `rN_certified`: `0 / 64`;
- `rB_rP_certified`: `0 / 64`;
- `uZ_certified`: `0 / 64`;
- S5 numerator covariance certificates: `0 / 64`;
- S5 action covariance certificates: `0 / 64`;
- S5 projective-normal covariance certificates: `0 / 64`.

Therefore every final physical `interior_exponent`, `flux_exponent`, and `action_exponent` is `null` in the authoritative payload. Raw tentative one-leading-term orders that appear before certification are not scientific corner verdicts and must not be promoted.

## What is established

1. The corrected projective-tangent geometry can be consumed consistently across the complete 34-orbit edge-subset decomposition.
2. The direct Kirchhoff denominator/order path is mechanically valid on all proper orbits.
3. The current one-leading-term cancellation certificate is insufficient for **every** physical channel-orbit component once the frozen independent-prime/weight/S5 controls are required.
4. The obstruction is localized upstream of any legitimate local integrability or global Stokes/IBP conclusion: exact leading-coefficient cancellation and covariance resolution for the physical numerator, annihilator action, and projective normal component is still missing.

## What is not established

This result does not establish that any physical corner is finite or divergent. It does not establish a global projective Stokes/IBP relation, either invariant-dual K5 period, a physical finite-part selector, regulator independence, global patching, a complete K5 amplitude, or any downstream F9/G3/G8/QG promotion.

The production payload keeps `global_stokes_ibp_verdict`, `integrated_period_verdict`, `finite_part_selector`, and `regulator_independence` equal to `null`.

## Highest-information next gate

The next admissible substantive gate is an exact cancellation/covariance resolver, prospectively bounded before outcome:

`K5_34_ORBIT_EXACT_LEADING_COEFFICIENT_CANCELLATION_RESOLUTION`.

It must keep the same 32 proper orbit representatives, two physical invariant-dual channels, canonical degree-27 numerator authority, corrected projective action/tangent field, and S5 transport. It must replace the one-leading-term representation only by a bounded exact coefficient representation capable of distinguishing exact zero from a finite higher t-order, with an a priori order/degree ceiling and independent reconstruction. No global Stokes/IBP gate is admissible until this blocker is resolved.