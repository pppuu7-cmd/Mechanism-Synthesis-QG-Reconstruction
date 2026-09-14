# Iter083D pre-terminal Critic audit

**Date:** 2026-09-15

**Status:** contract/provenance/code audit only. No scientific verdict is issued here because production run `34910997659` is non-terminal. No partial substantive production values are used.

## Frozen chain recovered

- preregistration: `prereg/ITER083D_SM_CAUSAL_SUM_REPAIRED_377_AMBIGUITY.md`, commit `7656ae687ce16ad05bacfc34349c8206b583237e`;
- implementation: `scripts/iter083d_causal_sum_repaired_377_ambiguity.py`, commit `f2661d98a7a934ad6cefc46de1e44a7989a4f92a`;
- workflow head: `b9d5347c087a8d9c70c82d2602be366f921af19e`;
- Actions run: `34910997659`, non-terminal at this audit;
- latest completed authority remains Iter083A/B/C as reconciled in `status/CURRENT.md` and `status/MSQGR_ADVERSARIAL_CRITIC_HANDOFF.md`.

The preregistered scientific object is a repaired finite-dimensional causal-sum persistence theorem. It explicitly forbids reuse of historical Iter081I's invalid Iter077Q-dependent infinite tangential family.

## Contract audit

The frozen obligations are materially stronger than merely enumerating causal sign patterns. In particular P4 requires a direct **upper-bound** argument for the summed off-collision object: the Beltran unit sum must have exact transverse scaling degree 20 and the same support geometry, boundary-dual fiber and exact compact-gauge/S5 covariance that define `F_8`, so that any two same-scaling-degree extensions differ by an element of `F_8`. P6 requires the unit-weight source object to be protected against insertion of unauthorized orientation weights. The negative controls require actual rejection of altered objects, not only a statement that the altered objects differ numerically.

## Implementation audit targets

The implementation substantively enumerates the 32 node-sign labels, their 16 distinct factorized wedge-sign patterns, multiplicity two under global reversal, and the top Boolean character. It also computes the unit-sum top-mode factors. Those are appropriate exact controls for P1-P3.

Several frozen controls are not yet mechanically demonstrated by the current executable and must be inspected in any terminal result before authority is granted:

1. **P4 upper-bound machinery.** `p4` is set from a text-presence lock on the Iter081H note. The executable does not independently validate the frozen conjunction `same support geometry + same boundary-dual fiber + same compact-gauge/S5 covariance + exact summed sd=20` or implement the logical upper-bound implication. A terminal scientific note may supply an analytic proof, but green CI alone cannot certify P4.

2. **Unauthorized-weight negative control.** `reject_alternating_weight_insertion` is currently the Boolean statement that a hard-coded alternating sixteen-weight list sums to zero. There is no source-weight validator through which this malformed object is passed and rejected. Indeed the zero total is exactly why such an unauthorized weighted object would cancel the top mode. Passing this Boolean therefore does not itself demonstrate rejection of the wrong source object.

3. **Scaling-only negative control.** `reject_scaling_only_as_377_proof` is currently equivalent to checking that the authoritative Iter083A and Iter083B text locks are present. It does not run a negative case in which scaling-degree evidence is present while the representation/dimension dependencies are absent, so it does not by itself certify the frozen negative control.

4. **Finite-sum-as-selector negative control.** `reject_finite_sum_as_unique_selector` is currently the precomputed condition `beltran_factor != 0 and dim_f8 > 0`. This is a correct logical observation but is not a same-machinery malformed-input rejection.

5. **Dependency phrase locks.** P0/P4/P5/P7 use exact phrase-presence tests in durable result notes. Such locks are useful provenance checks but are not independent re-derivations. Their scientific use is acceptable only where the upstream result itself is already authoritative and the terminal Iter083D result clearly distinguishes imported theorem authority from newly executed controls.

## Counterexample-first targets for terminal review

Any terminal review should try at least the following without changing the frozen object:

- replace the unit Beltran weights by an alternating zero-total vector and confirm the implementation rejects the object before using the causal-sum theorem;
- remove one of the Iter083A/B dependencies while retaining the scaling-degree source lock and confirm the implementation cannot promote 377;
- mutate the historical Iter081I text so the invalid `Q(y)^n F delta_N` dependency is absent and confirm P0 does not silently pass;
- distinguish explicitly the 32 BCG node-sign labels from the 16 distinct wedge-sign patterns and avoid treating them as independent causal sectors;
- verify the equality `S_BCG=2 S_Beltran` only for the exact frozen family depending solely on factorized wedge signs, with no hidden normalization or branch convention change;
- check that no result promotes finite causal summation, one-wedge `i epsilon`, or Toller additivity into a non-additive joint-K5 selector.

## Source-order / erratum firewall

`status/ITER077_CONTACT_FORMULA_ERRATUM.md` remains controlling and historical source-lock-invalid Iter077E/F siblings remain quarantined. Source ordering remains

`one-wedge spectral/spinor integration -> Toller function -> product of ten Toller matrices -> full boundary contraction -> K5 group integration / extension`.

Iter083D may act on the final source-ordered extension ambiguity and exact source-defined causal sums. It may not infer a physical full-amplitude theorem from termwise contact products or from unconstrained independent wedge-sign assignments.

## No verdict while non-terminal

This note does not classify Iter083D as PASS, FAIL, BLOCKED or INVALID. If the authoritative production remains non-terminal, no substantive production values or downstream transition may be taken from it. The eventual mandatory Critic verdict must be issued only after terminal run/job/artifact/hash recovery and comparison to the unchanged preregistration.