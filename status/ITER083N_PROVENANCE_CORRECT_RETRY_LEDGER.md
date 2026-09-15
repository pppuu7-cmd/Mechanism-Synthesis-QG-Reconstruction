# Iter083N provenance-correct retry ledger

Date: 2026-09-15

## Authority state

Fresh Iter083N retry Researcher status: `PASS_EXACT_SCOPED`.

Independent Critic status: **`CONFIRMED_SCOPED`**.

Critic classification:

`ITER083N_PROVENANCE_CORRECT_RETRY_CRITIC_CONFIRMED_SCOPED`.

Controlling durable independent review:

- `results/ITER083N_PROVENANCE_CORRECT_RETRY_1_ADVERSARIAL_REVIEW.md`;
- commit `9d706f024acc64429532731e63b5b22b6d8145a6`.

Independent Critic Actions cross-check also terminated successfully under its own prospective preregistration:

- Critic prereg `2df22374c71e7f0918e1aea8e5b1017620ea3ef2`;
- implementation `08ab666b4b8e4ad3b916dc1529ccdcef18e79c23`;
- workflow head `a9887c58528b4451e77de2fca0d3fcb986c4eb53`;
- run `34926988824`, job `104247016884`, terminal success;
- artifact `10380004276`, `iter083n-provenance-correct-retry-critic`;
- artifact ZIP digest `sha256:782168fe74300b734ce295b757837f865cbe96981e4f341e9ccb5dc5f2f35c7f`;
- all independent checks C0-C8 true;
- all six malformed controls rejected;
- exact Critic output classification/verdict `ITER083N_PROVENANCE_CORRECT_RETRY_CRITIC_CONFIRMED_SCOPED / CONFIRMED_SCOPED`.

This terminal Actions cross-check agrees with the durable adversarial review and is not a competing scientific verdict.

Researcher classification retained:

`ITER083N_SM_RADIAL_FINITE_PART_CHANGE_IS_RESIDUE_TIMES_DEFINING_FUNCTION_JET_AND_TANGENT_METRIC_ALONE_IS_INSUFFICIENT_FOR_K4_K5_SCOPED`.

Historical records remain quarantined and are not overwritten:

- original Iter083N result/run: `INVALID_PROVENANCE`, controlling review commit `fbff993fc920e707d0ff885b73549f3204d208c5`;
- first fresh retry run `34925091322`: `INVALID_IMPLEMENTATION`, no authoritative artifact.

## Frozen chronology

1. Parent scientific preregistration `c29ba0ddbaa4d6e1581db558b792565a7916a0cd`.
2. Actual source-lock commit `cf9d17cc8dae087f2c59ff0adb9f8aeff8ef7533`.
3. Actual theorem derivation commit `70a756c9c7c66f822d0e5933e9522b2d359dafe8`.
4. Historical Iter083N result later invalidated for provenance at `fbff993fc920e707d0ff885b73549f3204d208c5`.
5. Repaired Iter083M independently confirmed at `e7623cb5303ea49894e480e2fc4a884df44e7713`.
6. Fresh retry preregistration `d9edb0fd2a5c522ddec021f2b4f8e1a964ee3d96`.
7. Initial retry validator `397a5783e979121850ccb550f83df80237066fdb` and run `34925091322` failed implementation certification only.
8. Control-only repair preregistration `74ec4edd547d07503e70a0a972a500df70c7c60a` prospectively froze the lexical authority-check repair.
9. Repaired validator / authoritative production head `15472a83a6fc5e73c10b050649578822b65558cf`; repository ancestry confirms the control-repair prereg is its direct base.
10. Authoritative Researcher run `34925157771` completed `success` with job `104241540969`.
11. Durable raw copy commit `2fae0515891dfbe444672d1b05cd2fb23d3e6ac9`.
12. Durable Researcher result commit `7e194bd7d6e074e03f4393a6357d06824aedc745`.
13. Independent Critic prereg `2df22374c71e7f0918e1aea8e5b1017620ea3ef2`, implementation `08ab666b4b8e4ad3b916dc1529ccdcef18e79c23`, workflow head `a9887c58528b4451e77de2fca0d3fcb986c4eb53`.
14. Independent Critic run `34926988824`, job `104247016884`, terminal success, artifact `10380004276`, digest `sha256:782168fe74300b734ce295b757837f865cbe96981e4f341e9ccb5dc5f2f35c7f`, verdict `CONFIRMED_SCOPED`.
15. Durable adversarial review commit `9d706f024acc64429532731e63b5b22b6d8145a6`, same verdict and classification.

## Researcher Actions authority

- workflow: `Iter083N provenance-correct retry 1`;
- run: `34925157771`;
- checkout head: `15472a83a6fc5e73c10b050649578822b65558cf`;
- job: `104241540969`, terminal success;
- artifact: `10379901560`, `iter083n-provenance-correct-retry-1`;
- artifact size: 3793 bytes;
- artifact ZIP digest: `sha256:ac44a7a209847a097902904bb7114ffafa40edc8d40d8f15324b0c66204f0384`;
- production JSON SHA256: `b5e1f14e728c1ee9342a5433084b6c1d122faad4af360ffbcd627f60a76cd9ec`.

The Researcher workflow fetched full history and verified ancestry of the frozen scientific prereg/source/theorem/Critic/invalidation/retry commits before execution. The control-repair prereg was not explicitly enumerated in the workflow ancestry loop, but independent repository comparison shows `74ec4edd...` is the direct ancestor of production head `15472a83...`; this is not a provenance defect.

## Scientific output confirmed

For the frozen local conformal simple-pole family

`U_rho(z)=rho^z u=A_-1/z+A_0+O(z)`, `rho'=exp(phi)rho`,

exact Laurent multiplication gives

- `Res_rho'=A_-1`;
- `FP_rho' u-FP_rho u=phi A_-1`.

The universal ideal-annihilator theorem for supported residues of normal order `<=omega` gives the sharp thresholds

- K3: `phi in I_N^1`;
- K4: `phi in I_N^4`;
- K5: `phi in I_N^9`.

The Researcher executable ran 90 exact one-normal-coordinate identities with zero failures. The prospectively frozen independent Critic Actions run reconstructed the same 90 identities, thresholds `(1,4,9)`, tangent-Hessian implication, constant-scale law and firewalls, with all C0-C8 true. The durable adversarial review additionally checked the multivariable ideal-filtration statement: a nonzero normal Taylor coefficient of multi-degree `alpha`, `|alpha|<=omega`, is detected by a matching `partial^alpha delta_N` residue.

A direct counterexample to tangent-metric uniqueness was supplied: `rho=|x|^2`, `rho'=exp(x_1)rho` have the same tangent Hessian, while for `A_-1=partial_(x_1)delta_N`, `x_1 partial_(x_1)delta_N=-delta_N !=0`. Thus tangent normalization is universally sufficient for K3 order zero but not for the full allowed K4/K5 residue classes.

## Scope / interpretation lock

The confirmed result is only:

- local to one collision stratum;
- conformal regularizer changes only;
- a simple Laurent pole only;
- universal over the allowed supported-residue class, not a theorem about the actual physical source residue.

Two arbitrary Morse-Bott functions with the same Hessian need not be smoothly conformally related across `N`; no arbitrary-same-Hessian theorem follows. Higher-order poles require a new gate. The physical Toller residue may vanish, have lower normal order, or annihilate the remaining jet freedom.

No physical finite-part selector, physical regulator dependence/independence, unique K5 extension, global patching theorem, generic-spin theorem, causal E3/E4/E6 closure, G3/F9/G8/K5 promotion, `NEW_PHYSICS_FOUND` or complete-QG claim is authorized.

## Next authority action

Do not prioritize another generic radial candidate that merely proves existence of a smooth source-native geometry. The prepared Iter083O gate explicitly retains that the causal/Toller source does not mandate its proposed `mu_B` as the renormalization defining function, so it cannot by itself close the selector.

Highest-value next gate: prospectively freeze an `ACTUAL_SOURCE_ORDERED_RESIDUE_NORMAL_JET_ANNIHILATOR_GATE` (or equivalent source-faithful residue gate) targeting the actual fully boundary-contracted source-ordered K3/K4/K5 residue data in the frozen minimal sector. Test whether the residue is zero, lower-order, or annihilates every higher defining-function jet left free by Iter083M. If the actual residue object cannot be defined without exchanging source ordering or substituting a surrogate, return `BLOCKED_OBJECT_DEFINITION`.
