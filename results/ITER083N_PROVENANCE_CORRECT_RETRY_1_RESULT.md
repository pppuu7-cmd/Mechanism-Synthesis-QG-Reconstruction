# Iter083N-SM provenance-correct retry 1 — radial finite-part defining-function jet dependence

Date: 2026-09-15

Status: **PASS_EXACT_SCOPED — RESEARCHER RESULT; INDEPENDENT CRITIC REVIEW REQUIRED BEFORE DOWNSTREAM PROMOTION**

## Prospective provenance

Parent scientific preregistration:

- `prereg/ITER083N_SM_RADIAL_FINITE_PART_DEFINING_FUNCTION_JET_DEPENDENCE.md`;
- commit `c29ba0ddbaa4d6e1581db558b792565a7916a0cd`.

Fresh retry preregistration:

- `prereg/ITER083N_PROVENANCE_CORRECT_RETRY_1.md`;
- commit `d9edb0fd2a5c522ddec021f2b4f8e1a964ee3d96`.

First fresh retry production:

- head `62407b98b51985d60ca1746af3aa2e9804ca314a`;
- run `34925091322`;
- job `104241339442`;
- verdict `INVALID_IMPLEMENTATION` due only to one brittle historical-review phrase lock;
- no authoritative artifact;
- no scientific verdict taken from its substantive fields.

Prospective control-only repair:

- `prereg/ITER083N_PROVENANCE_CORRECT_RETRY_CONTROL_REPAIR_1.md`;
- commit `74ec4edd547d07503e70a0a972a500df70c7c60a`.

Repaired validator / authoritative Researcher production head:

- `scripts/iter083n_provenance_correct_retry.py`;
- head `15472a83a6fc5e73c10b050649578822b65558cf`.

Authoritative Researcher production:

- run `34925157771`, terminal `success`;
- job `104241540969`, terminal `success`;
- artifact `10379901560`, `iter083n-provenance-correct-retry-1`;
- artifact ZIP digest `sha256:ac44a7a209847a097902904bb7114ffafa40edc8d40d8f15324b0c66204f0384`;
- production JSON SHA256 `b5e1f14e728c1ee9342a5433084b6c1d122faad4af360ffbcd627f60a76cd9ec`;
- durable raw copy `results/raw/iter083n_provenance_correct_retry_1.json`, commit `2fae0515891dfbe444672d1b05cd2fb23d3e6ac9`.

Required actual authority identifiers consumed by P0:

- Iter083M repaired controlling Critic commit `e7623cb5303ea49894e480e2fc4a884df44e7713`, verdict `CONFIRMED_SCOPED`;
- Iter083N source-lock commit `cf9d17cc8dae087f2c59ff0adb9f8aeff8ef7533`;
- Iter083N theorem derivation commit `70a756c9c7c66f822d0e5933e9522b2d359dafe8`;
- historical Iter083N invalidation commit `fbff993fc920e707d0ff885b73549f3204d208c5`, which remains permanently authoritative for the old result only.

## Classification

`ITER083N_SM_RADIAL_FINITE_PART_CHANGE_IS_RESIDUE_TIMES_DEFINING_FUNCTION_JET_AND_TANGENT_METRIC_ALONE_IS_INSUFFICIENT_FOR_K4_K5_SCOPED`

Researcher verdict: **`PASS_EXACT_SCOPED`**.

This result is not yet independently Critic-confirmed and therefore must not authorize substantive Iter083O production or downstream promotion by itself.

## Exact object

The frozen object is the same as the parent Iter083N contract:

`U_rho(z)=rho^z u=A_-1/z+A_0+O(z)`

near a collision stratum `N`, with a conformally related defining function

`rho'=exp(phi) rho`.

The supported residue is allowed to have normal order bounded by the already-authoritative forest ceilings

- K3: `omega=0`;
- K4: `omega=3`;
- K5: `omega=8`.

No physical Toller residue, finite-part prescription, subtraction constant, scale choice or new regulator is inserted.

## Exact Laurent transformation

Since

`U_rho'(z)=exp(z phi)U_rho(z)`

and

`exp(z phi)=1+z phi+O(z^2)`, 

formal Laurent multiplication gives exactly

`Res_rho'=A_-1`,

`FP_rho' u-FP_rho u=phi A_-1`.

The production validator records `laurent_residue_unchanged=true` and `laurent_finite_part_shift="phi*A_-1"`.

## Exact supported-jet theorem

For one normal coordinate,

`n^q delta^(k)=(-1)^q k!/(k-q)! delta^(k-q)` for `q<=k`,

and zero for `q>k`.

Production executed all 90 exact checks for `0<=k<=8`, `0<=q<=9`, with zero failures.

Consequently, for a supported distribution of normal order at most `omega`, every

`phi in I_N^(omega+1)`

annihilates the residue universally. Sharp witnesses exist for every `q<=omega`, so this threshold cannot be lowered as a universal statement over the whole allowed supported-residue class.

The exact universal thresholds are therefore

- K3: `phi in I_N^1`;
- K4: `phi in I_N^4`;
- K5: `phi in I_N^9`.

## What repaired Iter083M fixes — and what it does not

Repaired Iter083M, now independently Critic-confirmed, fixes a unique invariant tangent/tubular radial quadratic basis with source tangent normalization. For conformally related Morse-Bott defining functions with the same normalized quadratic Hessian,

`rho'=exp(phi)rho`,

one obtains only

`phi|_N=0`, i.e. `phi in I_N`.

That condition is universally sufficient for K3 because `omega=0`. It is not, by itself, universally sufficient for the full allowed K4 (`omega<=3`) or K5 (`omega<=8`) supported-residue classes.

Therefore **a unique tangent metric does not by itself define a unique finite part in the general allowed K4/K5 residue space**.

## Constant rescaling control

For `rho'=c rho`, `c>0`,

`FP_(c rho)u-FP_rho u=(log c)A_-1`.

This is only a structural control. If source normalization fixes the overall radial scale, this particular freedom is absent; higher defining-function jets can still matter in the universal supported-residue class.

## Physical firewall

This result does **not** prove that the actual full source-ordered Toller residue is nonzero, reaches maximal order, or has nonzero contraction with an unfixed defining-function jet.

The physical residue could:

- have lower normal order;
- lie in an annihilator subspace;
- vanish in some or all boundary channels;
- become independent because an exact nonlinear source-derived radial function fixes the relevant higher jets.

Accordingly, no actual nonzero physical scheme dependence is established.

## Felder-Kazhdan firewall

Felder-Kazhdan supplies an external mathematical crosscheck that conformal regularizer changes affect Hadamard finite parts through local residue data in their Morse-Bott differential-form class.

The retry does not prove that the Toller amplitude belongs to that complete singularity class and does not import their odd-codimension residue-vanishing conclusion into K4.

## Historical provenance quarantine

The old Iter083N result `results/ITER083N_SM_RADIAL_FINITE_PART_JET_DEPENDENCE_RESULT.md` remains permanently **`INVALID_PROVENANCE`** under commit `fbff993fc920e707d0ff885b73549f3204d208c5`.

The first fresh retry run `34925091322` remains **`INVALID_IMPLEMENTATION`**. Neither is rehabilitated by the successful repaired retry.

Only run `34925157771` on head `15472a83a6fc5e73c10b050649578822b65558cf` is the present Researcher production authority for this retry.

## Claim ceiling

No actual nonzero physical finite-part dependence; no source-authorized finite-part selector; no actual physical Toller residue theorem; no unique K5 extension; no physical regulator dependence or independence; no global forest/partition-of-unity patching theorem; no generic-spin theorem; no causal E3/E4/E6 closure; no G3/F9/G8/K5 promotion; no `NEW_PHYSICS_FOUND`; no complete-QG claim.

## Downstream effect

The local selector problem is narrowed but not solved.

A future positive selector must now do at least one of the following in a source/microlocal-authorized way:

1. construct the exact nonlinear source-derived defining function and fix its required jets through the relevant order; or
2. compute the actual source-ordered K3/K4/K5 residue distributions and prove that all unfixed higher-jet changes annihilate them; or
3. supply another independently justified composition/microlocal normalization that selects the extension.

Until independent Critic review confirms this retry, Iter083O remains preparation-only and no downstream promotion is authorized.
