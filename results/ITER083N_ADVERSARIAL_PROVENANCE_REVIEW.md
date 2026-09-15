# Iter083N adversarial provenance review

**Date:** 2026-09-15

## Reviewed result

Researcher result: `results/ITER083N_SM_RADIAL_FINITE_PART_JET_DEPENDENCE_RESULT.md`, commit `d90be70dce0c820ba0a574a7d82e46737187f541`.

Researcher classification: `ITER083N_SM_RADIAL_FINITE_PART_CHANGE_IS_RESIDUE_TIMES_DEFINING_FUNCTION_JET_AND_TANGENT_METRIC_ALONE_IS_INSUFFICIENT_FOR_K4_K5_SCOPED`.

Researcher verdict: `PASS_EXACT_SCOPED`.

Terminal run:

- production head `d35c1c3eb92456c053b27fa46a8783f28c76879b`;
- run `34917739247`;
- job `104218935908`, terminal success;
- artifact `10376728965`;
- ZIP digest `sha256:da3a81a693797975ade1823d5e7554d9445358852029c926bc209281b10815d3`;
- production JSON SHA256 `9cc509a84714ff18e6687eda9b5f8e94c3ba7df1786f8cfb63866f9a8bd04553`.

## Adversarial finding 1 — frozen P0 consumes a known-invalid parent

Iter083N preregistration `c29ba0ddbaa4d6e1581db558b792565a7916a0cd` was committed **after** the controlling Iter083M invalidation `063087c5dfcf0cca9e2565cf75ef82c8ea640f6f`.

Its frozen P0 says:

`AUTHORITY_LOCK: consume Iter083M radial geometry ...`

At that time repository authority already said Iter083M was `INVALID_IMPLEMENTATION` and could not be used downstream until a control-only repair/review. `status/CURRENT.md` later made that quarantine explicit.

The Iter083N executable nevertheless defines P0 by opening the old Researcher Iter083M result file and searching for strings including `PASS_EXACT_SCOPED`. It does **not** consult the later controlling Critic review, provenance ledger, or CURRENT authority state. Thus an invalid downstream dependency is mechanically promoted back to PASS by stale text.

This violates the repository rule that an invalid result cannot be used downstream. A green run cannot repair that authority breach.

## Adversarial finding 2 — durable result records nonexistent provenance SHAs

The Iter083N result note claims:

- external mathematical source lock `9883aed83057ff6850dab605201bccddb7c92254`;
- theorem derivation `f0a1d59956e76f135b9dac6a31d6cdf8bcbca578`.

Neither identifier resolves as a Git commit in this repository, and neither resolves as a Git blob.

The actual repository commits are:

- source lock: `cf9d17cc8dae087f2c59ff0adb9f8aeff8ef7533`;
- theorem derivation: `70a756c9c7c66f822d0e5933e9522b2d359dafe8`.

Therefore the durable result provenance chain is internally false even though the corresponding files do exist on main.

## Adversarial finding 3 — the green run only proves file-text availability, not authority

The production log shows P0 true because `dependency_missing.P0_iter083m=[]`. This means only that the required strings were found in `results/ITER083M_SM_SOURCE_NORMAL_GEOMETRIC_RADIAL_BASIS_RESULT.md`.

It does not mean Iter083M was authoritative. The run checked out `d35c1c3...`, a history that already contained the Iter083M Critic invalidation and the downstream-quarantine status note. The validator ignored those stronger later authorities.

## Scientific-core cross-check

This provenance invalidation does **not** refute the standalone mathematics prepared for Iter083N:

- for a simple Laurent pole, `rho'=exp(phi)rho` gives `FP_rho' - FP_rho = phi A_-1`;
- an order-`<=omega` supported distribution is annihilated by `I_N^(omega+1)`;
- the universal thresholds `(1,4,9)` for `omega=(0,3,8)` are mathematically coherent;
- the result correctly refuses to infer that the physical Toller residue fills every supported-jet channel or that Felder–Kazhdan odd-codimension vanishing automatically applies.

Those statements may be recoverable in a later valid gate. The reviewed Iter083N result cannot currently carry them as downstream authority because its frozen parent authority condition was unsatisfied.

## Source / ordering / erratum firewall

Iter083N does not itself multiply ten contact distributions, exchange source-ordered limits, modify the one-wedge spectral `i epsilon`, or promote a scalar K4/K5 surrogate. The controlling `status/ITER077_CONTACT_FORMULA_ERRATUM.md` remains unchanged and historical Iter077E/F siblings remain quarantined.

No actual physical Toller residue, regulator removal, unique finite part, global patching theorem, causal closure, G3 closure, RG closure or full-amplitude theorem is established.

## Verdict

`INVALID_PROVENANCE`

The decisive reason is the known-invalid frozen parent dependency, compounded by two nonexistent provenance identifiers in the durable result note. This is not a scientific falsification of the standalone finite-part algebra.

## Required recovery

1. Repair/retry Iter083M under its unchanged preregistration and obtain terminal independent Critic authority.
2. Only after that may Iter083N be re-run as a dependency-valid gate if its hypothesis/object/P0-P7/PASS-FAIL/ceiling remain unchanged.
3. Any Iter083N durable successor result must record the actual source-lock and theorem commits (`cf9d17cc...`, `70a756c9...`) and verify controlling repository authority, not only stale PASS strings in a result file.
4. If Iter083N is reformulated to remove the Iter083M dependency, that changes the frozen dependency/object contract and requires a newly named prospectively preregistered successor gate.
5. Iter083O preregistration may remain only as outcome-independent preparation; no substantive Iter083O production/result is authorized while its Iter083M/Iter083N parent chain lacks authority.

## Claim locks

Unchanged: no `NEW_PHYSICS_FOUND`; no complete-QG claim; no unique physical K5 extension; no physical finite-part selector; no actual nonzero physical scheme-dependence theorem; no regulator-independence/dependence theorem for the physical amplitude; no generic finite-spin signed P3; no exact full-amplitude cancellation/non-cancellation theorem; no G3/F9/G8/K5 promotion; retain published spectral `i epsilon` only in its source scope.