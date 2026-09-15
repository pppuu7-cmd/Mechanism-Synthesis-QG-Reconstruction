# Iter083D provenance ledger — repaired causal-sum persistence of exact 377-dimensional ambiguity

**Date:** 2026-09-15

## Controlling scientific contract

Original scientific preregistration:

- `prereg/ITER083D_SM_CAUSAL_SUM_REPAIRED_377_AMBIGUITY.md`
- commit `7656ae687ce16ad05bacfc34349c8206b583237e`.

This preregistration froze before the first implementation:

- the repaired finite object `F_8`, with authoritative Iter083B dimension 377;
- the source-defined Beltran 16-pattern and Bianchi--Chen--Gamonal 32-node-label unit causal sums;
- P0-P7, including the exact 16/32 top-mode factors and the required upper-bound argument;
- the prohibition on resurrecting historical Iter081I's invalid Iter077Q-dependent infinite tangential family;
- the unit-weight-only scope and the full interpretation ceiling.

No later repair changes these scientific items.

## First implementation and production attempt

Initial validator:

- `scripts/iter083d_causal_sum_repaired_377_ambiguity.py`
- commit `f2661d98a7a934ad6cefc46de1e44a7989a4f92a`.

Workflow / production head:

- `b9d5347c087a8d9c70c82d2602be366f921af19e`.

First Actions run:

- run `34910997659`, terminal `failure`;
- job `104198223502`, terminal `failure`;
- failing step: `Run exact Iter083D validation`;
- artifact upload skipped, so this run has no authoritative artifact/digest.

The executed validator reported P0, P1, P2, P3, P5, P6, P7 true and P4 false. Its own classification was `ITER083D_SM_CAUSAL_SUM_REPAIR_INVALID_IMPLEMENTATION` / `INVALID_IMPLEMENTATION`. The only missing P4 dependency token was the literal phrase `transverse scaling degree`.

The authoritative Iter081H dependency instead records the needed scientific content explicitly as:

- `q=-20`;
- transverse dimension `d=12`;
- the 16 `eta=+1` source assignments;
- nonzero summed leading term `16 C_alpha r^(-20)+O(r^-19)` for every frozen boundary component.

Durable Critic review of this first attempt:

- `results/ITER083D_FIRST_PRODUCTION_ADVERSARIAL_REVIEW.md`
- commit `b559d8a5734c829abbae2b5c89bfedea4d1e2916`;
- verdict `INVALID_IMPLEMENTATION` for run `34910997659` only.

## Structural theorem derivation

After the failed first production attempt, the repository recorded the full analytic theorem derivation:

- `sources/ITER083D_SM_CAUSAL_SUM_REPAIRED_377_AMBIGUITY_DERIVATION.md`
- commit `dff3407d3ffa86f5aa5c3b4e7550a15798d6ed7c`.

It supplies the non-string-lock upper-bound argument required by P4: Iter081H keeps the Beltran sum in the same nonzero `r^-20`, codimension-12 common-collision class with the same boundary-dual fiber, compact node-gauge action, S5 covariance and density convention; Iter083B therefore bounds its same-scaling-degree source-symmetry-compatible extension differences by `F_8`. Iter083C provides the opposite 377-dimensional injection because its top Boolean character is +1 on every factorized causal pattern.

## Control-only P4 repair and authoritative run

A control-only code edit:

- commit `10e9fdd9ba4aeb2cda800af32c74eeebd137e48e`;
- changed only the brittle P4 dependency token from absent prose `transverse scaling degree` to exact frozen dependency wording `q=-20`;
- no scientific hypothesis, source object, causal weights, dimension, PASS/FAIL rule or interpretation ceiling changed.

This commit triggered the authoritative second production run:

- run `34911072018`, terminal `success`;
- job `104198440273`, terminal `success`;
- checked-out head `10e9fdd9ba4aeb2cda800af32c74eeebd137e48e`;
- artifact `10374652013`, `iter083d-causal-sum-repaired-377-ambiguity`;
- artifact ZIP digest `sha256:338697c0e56a857c407685befd5023706a3080f1629fccdd27feb5dd180af91b`;
- production JSON SHA256 `a95e47e8833142a49cc8d3b4455f272cfca632fb21d8da12db6dac2599b403b1`.

The executed production reported P0-P7 all true, all eight registered controls true, 32 node-sign labels, 16 distinct wedge patterns with multiplicity two, top-character set `[1]`, Beltran factor 16, BCG factor 32, and frozen ambiguity dimension 377.

## Repair-note chronology clarification

`prereg/ITER083D_SM_CONTROL_ONLY_P4_DEPENDENCY_LOCK_REPAIR.md`, commit `dfe59b418c80f0b440556edf08797b8174bbf910`, was committed after the authoritative run had already been triggered on head `10e9fdd...`. It is therefore **not** the prospective authority for run `34911072018`. Prospectivity for the scientific object and criteria comes from the original Iter083D preregistration `7656ae...`; the `10e9fdd...` change is admissible only as a transparent control/dependency-token repair under that unchanged contract.

A still later code-alignment commit `99f37180615d5076983a88c4c9e4c62c1aa75c07` is not the production head of the authoritative run and must not be substituted for `10e9fdd...` in provenance.

## Durable result and review

Researcher result:

- `results/ITER083D_SM_CAUSAL_SUM_REPAIRED_377_AMBIGUITY_RESULT.md`
- commit `6632b65df27cf47d6b7445544ccc534e6902a74e`.

Authoritative classification:

`ITER083D_SM_CAUSAL_SUM_RETAINS_EXACT_377_DIMENSIONAL_K5_SUPPORTED_AMBIGUITY_REPAIRED_SCOPED`

Researcher verdict: `PASS_EXACT_SCOPED`.

Adversarial review:

- `results/ITER083D_ADVERSARIAL_REVIEW.md`
- commit `d663834c99fabbba9a41671335b10cb720f3dc1e`;
- verdict `CONFIRMED_SCOPED`.

Historical Iter081I was then durably superseded by commit `78b40d6cd57a391a994b5dbb938ffed553d49af1` as `SUPERSEDED_INVALID_SOURCE_SYMMETRY_MODEL`, preserving only its independently valid qualitative observations.

`status/CURRENT.md` was reconciled through authoritative Iter083D at commit `bb8ef36decc611dd05502f0bafdec9fccf8642df`.

## Exact scope

Within the frozen all-`j=1/2`, common-K5-collision, boundary-linear, compact-node-gauge/S5-covariant, same-scaling-degree class:

- the Beltran 16-pattern unit sum maps every Iter083C top-mode ambiguity `a` to `16a`;
- the BCG 32-node-label unit sum maps it to `32a`;
- both maps are injective over `C`;
- Iter081H plus Iter083B gives the matching upper bound;
- hence both summed extension-ambiguity spaces have exact complex dimension 377.

This is not a theorem for arbitrary orientation weights, generic spin, all collision strata, global distributional patching, regulator independence or many-vertex composition. It does not select any coefficient.

## Claim locks

No `NEW_PHYSICS_FOUND`; no complete-QG claim; no unique K5 extension; no causal-vertex distributional nonexistence/finiteness theorem; no generic-spin exact ambiguity dimension; no all-strata global patching theorem; no regulator independence; no G3/F9/G8/K5 promotion; retain published one-wedge spectral `i epsilon` only in its source scope.

The next local scientific question must be genuinely non-additive and independently motivated; causal summation and the complete additive Toller/EPRL identity hierarchy are now both known not to select the frozen local extension.