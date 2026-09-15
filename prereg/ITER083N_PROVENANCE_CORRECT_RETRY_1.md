# Iter083N-SM provenance-correct retry 1

Date: 2026-09-15
Status: **PROSPECTIVELY FROZEN BEFORE RETRY IMPLEMENTATION / PRODUCTION OUTPUT**

Parent scientific preregistration: `prereg/ITER083N_SM_RADIAL_FINITE_PART_DEFINING_FUNCTION_JET_DEPENDENCE.md`, commit `c29ba0ddbaa4d6e1581db558b792565a7916a0cd`.

This file authorizes a fresh retry only. It does not rehabilitate or modify the historical Iter083N result, which remains `INVALID_PROVENANCE` under `results/ITER083N_ADVERSARIAL_PROVENANCE_REVIEW.md`, commit `fbff993fc920e707d0ff885b73549f3204d208c5`.

## HYPOTHESIS

Under the unchanged parent Iter083N scientific contract, a simple-pole radial analytic/Hadamard regularization obeys

`FP_(exp(phi) rho) u - FP_rho u = phi A_-1`,

and universal independence for every supported residue of normal order `<= omega` requires `phi in I_N^(omega+1)`. The source-normal tangent metric fixes only `phi|_N=0`; this is universally sufficient for K3 (`omega=0`) but not by itself for the full allowed K4/K5 residue classes (`omega=3,8`).

## OBJECT

Exactly the parent Iter083N object: a formal simple-pole meromorphic family

`U_rho(z)=rho^z u=A_-1/z+A_0+O(z)`

near one collision stratum, with conformally related defining functions `rho'=exp(phi)rho`, supported residues bounded by the already-authoritative forest normal-order ceilings `omega=(0,3,8)`. No physical Toller residue is inserted or selected.

## DEPENDENCY

P0 must consume controlling repository authority, not stale Researcher PASS text. Required authorities are:

1. repaired Iter083M independent Critic confirmation `results/ITER083M_REPAIRED_ADVERSARIAL_REVIEW.md`, commit `e7623cb5303ea49894e480e2fc4a884df44e7713`, verdict `CONFIRMED_SCOPED`;
2. current durable authority `status/CURRENT.md`, which explicitly authorizes only a fresh Iter083N retry and keeps the old result `INVALID_PROVENANCE`;
3. Iter082D normal-order forest ceilings and Iter083B `F_8` authority used by the unchanged parent contract.

## SOURCE AUTHORITY

- Parent preregistration commit: `c29ba0ddbaa4d6e1581db558b792565a7916a0cd`.
- Actual Iter083N source-lock commit: `cf9d17cc8dae087f2c59ff0adb9f8aeff8ef7533`.
- Actual Iter083N theorem derivation commit: `70a756c9c7c66f822d0e5933e9522b2d359dafe8`.
- Repaired Iter083M controlling Critic commit: `e7623cb5303ea49894e480e2fc4a884df44e7713`.
- Historical Iter083N invalidation commit: `fbff993fc920e707d0ff885b73549f3204d208c5`.
- `status/ITER077_CONTACT_FORMULA_ERRATUM.md` remains controlling; historical source-lock-invalid siblings stay quarantined.

The Felder-Kazhdan theorem remains motivation/crosscheck only; full applicability to the Toller amplitude is not assumed.

## FROZEN INPUTS

- candidate: CRQN v0.2 unchanged;
- spins/boundary scope: unchanged frozen all-`j=1/2` common-collision scope inherited by the parent gate; no boundary state is chosen post hoc;
- forest normal-order ceilings: K3 `omega=0`, K4 `omega=3`, K5 `omega=8`;
- supported-distribution exact identities through order 8;
- conformal defining-function relation `rho'=exp(phi)rho`;
- simple Laurent pole only, exactly as parent contract;
- no numerical quadrature, fitted constant, regulator path, subtraction scale, finite-part normalization, new branch convention or new physical selector;
- actual source-lock/theorem commit identifiers are frozen exactly as above.

## POSITIVE CONTROLS

The retry must mechanically reproduce the parent exact algebra:

1. residue unchanged and finite-part shift `phi A_-1`;
2. exact `n^q delta^(k)` identities through `k=8`;
3. annihilation by `I_N^(omega+1)` and sharp witnesses for every `q<=omega`;
4. thresholds `(1,4,9)` for K3/K4/K5;
5. same tangent quadratic Hessian implies only `phi|_N=0` in the conformal class;
6. constant rescaling gives `(log c) A_-1`.

## NEGATIVE CONTROLS

Unchanged from the parent gate. The retry must reject:

- unique tangent metric automatically fixing the finite part for `omega>0`;
- treating every supported residue as order zero;
- claiming actual K5 scheme dependence without the source residue;
- importing Felder-Kazhdan odd-codimension residue simplifications into K4 without an applicability proof;
- excluding the possibility that an exact nonlinear source radial function fixes all relevant jets;
- excluding the possibility that the actual residue annihilates the defining-function change;
- promoting this local theorem to global forest/partition patching.

Additionally, P0 must fail if either controlling Iter083M Critic confirmation or CURRENT authorization is absent; stale historical Iter083M Researcher PASS text alone is not sufficient.

## PASS

Exactly the parent PASS condition and label:

`ITER083N_SM_RADIAL_FINITE_PART_CHANGE_IS_RESIDUE_TIMES_DEFINING_FUNCTION_JET_AND_TANGENT_METRIC_ALONE_IS_INSUFFICIENT_FOR_K4_K5_SCOPED`

with verdict `PASS_EXACT_SCOPED`, provided P0-P7 and all unchanged controls pass under provenance-correct authority.

## FAIL

Exactly the parent scientific failure semantics: if a valid exact calculation contradicts any frozen mathematical predicate while implementation/provenance remain valid, classify `FAIL_EXACT_SCOPED` and record the first exact counterexample. Do not relabel a scientific mismatch as an implementation failure.

## BLOCKED

If controlling Iter083M authority, required source/theorem files, or the frozen normal-order object cannot be established from current repository authority, classify `BLOCKED_OBJECT_DEFINITION` / dependency-blocked as appropriate. Do not substitute a surrogate parent object.

## INVALID

Use `INVALID_IMPLEMENTATION` only for broken code, malformed/missing controls, inconsistent hashes/commit identifiers, or workflow/provenance defects. The historical run remains separately `INVALID_PROVENANCE` forever.

## INTERPRETATION CEILING

Unchanged from the parent preregistration. No actual nonzero physical finite-part dependence; no proof that the physical Toller residue activates the allowed channels; no full Felder-Kazhdan applicability theorem; no unique physical K5 extension; no source-authorized finite-part or subtraction-scale selector; no global renormalization/patching theorem; no regulator dependence/independence theorem for the physical amplitude; no generic-spin theorem; no causal E3/E4/E6 closure; no G3/F9/G8/K5 promotion; no `NEW_PHYSICS_FOUND`; no complete-QG claim.

## PRODUCTION DISCIPLINE

The retry must use a new validator/workflow identity so the historical run cannot be confused with the fresh authority. Durable result/provenance must record the exact checkout head, run/job/artifact IDs, artifact ZIP digest, production JSON SHA256, actual source-lock/theorem commits, and the controlling repaired Iter083M Critic commit. No second scientific gate may be opened in the same Researcher run.
