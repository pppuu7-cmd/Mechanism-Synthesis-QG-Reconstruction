# Current MSQGR research state

**Date:** 2026-09-14

## Candidate / authoritative front

- Candidate: `CRQN v0.2`, `CARRIER_SELECTED` only for source-backed carrier/mechanism structure `F1-F8`.
- Predictive local K5 amplitude: `BLOCKED_CURRENT_CANDIDATE_LOCAL_AMPLITUDE`, independently `CONFIRMED_SCOPED` after Iter080I.
- Physical F9: `BLOCKED`.
- Controlling local blocker: `FUNCTION_SPACE_K5_DISTRIBUTIONAL_EXTENSION_SELECTOR`.
- Controlling composition blocker: `CAUSAL_MULTIVERTEX_E3_E4_E6_COMPLETE_SOURCE_BRIDGE`.
- Han causal-stack blocker: `REPLACEMENT_FOR_FAILED_HAN_D2_BOUND_IN_CAUSAL_FACE_OBJECT`.
- RG/refinement: `BLOCKED_E9_COARSE_FINE_MAP_MISSING`.
- G3: `OPEN_BUT_NOT_ADMISSIBLE_UNTIL_LOCAL_AMPLITUDE_AND_COMPOSITION_ARE_DEFINED`.
- G8: `BLOCKED_CONVERGENCE_ONLY`.

**Physical active front:**
`ITER081F_TWO_WEDGE_CAUSAL_BRANCH_SUBSET_BOUNDEDNESS / NEW_BOUNDED_OR_RENORMALIZED_CAUSAL_FACE_FUNCTIONAL / GENUINELY_NEW_OR_REVISED_JOINT_K5_PRIMARY_AUTHORITY / INDEPENDENTLY_MOTIVATED_STRONGER_JOINT_FUNCTION_SPACE_SELECTOR / E7_E8_AFTER_PREREQUISITES / REGULATOR_INDEPENDENCE_AFTER_OBJECT_DEFINITION`.

## Latest authoritative Researcher result — Iter081E

Prospective chain:
- prereg `0f5414c9471a382527ca06c7f29ef2da6b8f8c1d`;
- implementation `8ceb7cc99925bb1d2a262b304ce29731f438ffdb`;
- production head `5743b4e0d6f5ce247ebe207b0ad48b0f17f3f664`;
- run `34877725730`, job `104088973504`, terminal success;
- artifact `10361621460`, digest `sha256:f2a4c52535799fad2aa7ad94b7bb2eeedde1933dde62cb66281dcff7493b4a82`;
- aggregate JSON SHA256 `726d8d6fb608a77a2f832f487d32633e1ba1a3d2c8c497c1e5071d868ce9422b`;
- durable result `results/ITER081E_SM_ACTUAL_TOLLER_HAN_BOUND_REPRODUCTION_RESULT.md`, commit `e5eb0cbd49328e4e3ffcc604428af9b36c6295a2`;
- latest specific Researcher handoff `status/MSQGR_RESEARCHER_HANDOFF_ITER081E.md`, commit `ed6ce07c38c3a93265873c90c8e8490e68334706`.

Classification:
`ITER081E_SM_ACTUAL_TOLLER_ONE_WEDGE_AND_NATURAL_TWO_WEDGE_HAN_BOUNDS_COUNTEREXAMPLES_REPRODUCED_EXACT_SCOPED`.
Researcher verdict: `PASS_EXACT_SCOPED`.

Independent Critic review:
- `results/ITER081E_ADVERSARIAL_REVIEW.md`, commit `379b5979ef0e38973af3196b678dc6d8ab7b35f6`;
- `status/MSQGR_ADVERSARIAL_CRITIC_HANDOFF.md`, commit `170fa8b1213210c62a4533ad44856afc46893795`;
- Critic verdict: **`CONFIRMED_SCOPED`**.

Durable-state qualification: the generic `status/MSQGR_RESEARCHER_HANDOFF.md` remains stale at Iter080J. Until reconciled, recovery must use the newer specific Iter081E handoff above.

## Iter081E exact scientific result

Frozen BCG Eq. (46) object: gamma-simple `j=k=1/2`, branch `+`, arbitrary fixed real `rho>0`, pure boost `g_beta=exp(-i beta K_z)`, `beta>0`.

For `m=+1/2`, exact reduction gives

`t_+(beta) = -2 exp[-(2-i rho)beta] / [(rho^2+1/4)(1-exp(-2 beta))^2]`,

hence

`|t_+(beta)| = 1/[2(rho^2+1/4)sinh^2(beta)] -> +infinity` as `beta->0+`.

Therefore the actual selected Toller branch violates the Han-type projected contraction `||P_j T^+(g) P_j||<=1` on the frozen path for sufficiently small positive beta.

For `m=-1/2`, exact source-formula reduction gives the opposite leading coefficient:
- `lim beta^2 t^+_{+1/2} = -1/[2(rho^2+1/4)]`;
- `lim beta^2 t^+_{-1/2} = +1/[2(rho^2+1/4)]`.

For the prospectively frozen natural two-wedge selected-branch term

`tau_{++,2}(beta)=2[(t^+_{+1/2})^2+(t^+_{-1/2})^2]`,

one has exactly

`lim_{beta->0+} beta^4 tau_{++,2}(beta)=1/(rho^2+1/4)^2>0`.

Thus this natural `(+,+)` two-wedge term is unbounded and exceeds Han's standard `d_j^2=4` bound for sufficiently small beta. This is not an all-face/all-branch or causal-stack divergence theorem.

## Han / causal-stack source authority

Muxin Han `arXiv:2602.18665v1` / Phys. Rev. D 114, 044040 remains genuine standard-EPRL/KKL stack/RG authority and independent motivation only.

- Han internal face factor is a trace of ordered projected **unitary representation** wedge factors.
- Han's `|tau_k^(h)|<=d_k^2` bound and saturation theorem rely on representation unitarity and feed the bosonic grand-canonical pole/condensation/localization chain.
- BCG `arXiv:2604.24945v1` gives `D=T^(+)+T^(-)` but explicitly states Toller matrices are functions, not a Lorentz-group representation.
- Iter081B established direct single-branch Han-stack inheritance is not source-proven; Critic `CONFIRMED_SCOPED`.
- Iter081E is stronger: the unchanged Han contraction and unchanged `d_j^2` bound are actually false on the frozen selected-Toller objects.

Beltran `arXiv:2603.22661v2` gives the causal orientation construction on arbitrary 2-complexes. Its ordinary EPRL-KKL object is recovered by summing all wedge orientations, while the causal amplitude retains only orientation assignments satisfying the causal condition. This motivates the next branch-sum cancellation test. Withdrawn Beltran--Zapata `arXiv:2603.17207` remains source-quarantined.

## Source-order / erratum lock

`status/ITER077_CONTACT_FORMULA_ERRATUM.md` remains controlling, blob `63356e5099929f2b21d9d7296ab97f15ff163dba`.

Correct `j=1/2` contact formula:
`delta^(rho,1/2)(x)=-(2 i rho/D) delta(x)-(1/D) delta'(x)`, `D=rho^2+1/4`.

Authoritative local order:
`one-wedge spectral/spinor integration -> Toller function -> product of ten Toller matrices -> full boundary contraction -> K5 group integration / extension`.

Termwise `theta/delta/delta'` multiplication/pullback is not identified with the source-ordered full Toller object without theorem. One-wedge spectral `i epsilon` is not a joint-K5 regulator or selector.

## Controlling local K5 authority

- Iter077I run `34786586785`: source-ordered all-`j=1/2` local K5 object is not locally `L1` at the common collision; this is not a full-vertex divergence theorem.
- Iter077K: one-wedge `i epsilon` does not define a correlated joint-K5 boundary value.
- Iter077L: collision `N=SU(2)^4`, codim 12; same-scaling-degree extensions carry smooth tangential freedom.
- Iter077Q: infinite-dimensional source-compatible ambiguity `W=span_C{Q^n F_SU2 delta_N}`; run `34792482045`, artifact `10328598487`, digest `sha256:58e3cb389a985838942a4d0181e6e680cdd75480cfc24e0ec7bb07d73b199a96`.
- Iter080A: finite K5 permutation covariance does not select; `CONFIRMED_SCOPED`.
- repaired Iter080D: every fixed finite scalar complex-linear selector family leaves infinite-dimensional kernel; `CONFIRMED_SCOPED`.
- repaired Iter080E: frozen BCG/Beltran corpus contains no explicit P1-P5-complete joint-K5 selector; `BLOCKED_OBJECT_DEFINITION` in frozen scope.
- Iter080H: pre-Iter077Q CRQN corpus contains no A1-A5-complete full-W selector; `CONFIRMED_SCOPED`.
- Iter080I: CRQN v0.2 local amplitude remains blocked; `CONFIRMED_SCOPED`.
- Iter080J: ordinary support + conormal/WF admissibility alone does not select; `CONFIRMED_SCOPED`.
- Iter080K: historical `INVALID_PROVENANCE`.

## Causal multivertex authority

Iter080B run `34825084313`, artifact `10339454847`, digest `sha256:73cf815a59649f0e5b8ec8b972dc0583fe0d4a869e94da13f9e3686c60bd601b` remains controlling. Parent KKL/EPRL E3/E4/E6 structures and local causal vertices exist separately, but the complete causal many-vertex functional with E3 contraction, E4 weights/sums/normalization and E6 gauge fixing/quotient normalization remains `BLOCKED_SOURCE_BRIDGE`.

## Exact blockers

1. `FUNCTION_SPACE_K5_DISTRIBUTIONAL_EXTENSION_SELECTOR`.
2. `CAUSAL_MULTIVERTEX_E3_E4_E6_COMPLETE_SOURCE_BRIDGE`.
3. `REPLACEMENT_FOR_FAILED_HAN_D2_BOUND_IN_CAUSAL_FACE_OBJECT`.
4. `PROPER_CAUSAL_BRANCH_SUM_CANCELLATION_OR_BOUNDEDNESS`.
5. `E7_E8_DISTRIBUTIONAL_EXTENSION_TRANSPORT_OR_SELECTOR`.
6. `RG_REFINEMENT_E9_COARSE_FINE_BOUNDARY_MAP_AND_MATCHING_FUNCTIONAL`.
7. `REGULATOR_INDEPENDENCE_AFTER_OBJECT_DEFINITION`.

Any blocked mandatory arrow prevents full-QG completion.

## Survival chain

`carrier/source F1-F8` -> `source-ordered local K5` -> `non-L1 collision` -> `extension freedom` -> `Iter077Q infinite-dimensional ambiguity` -> `finite covariance DOES NOT SELECT` -> `finite scalar-linear conditions DO NOT SELECT` -> `ordinary WF/conormal admissibility DOES NOT SELECT` -> `frozen source corpus has no full-W selector` -> `CRQN v0.2 local amplitude BLOCKED` -> `Han standard stack/RG motivation` -> `Iter081A INVALID_IMPLEMENTATION` -> `Iter081B direct single-branch Han inheritance NOT SOURCE PROVEN (CONFIRMED_SCOPED)` -> `Iter081E actual selected-Toller Han contraction and natural two-wedge d^2 bound FAIL (CONFIRMED_SCOPED)` -> `proper causal branch-sum boundedness ?` -> `new causal face functional / grand-canonical transport ?` -> `full-W transport/selector ?` -> `causal E3/E4/E6 ?` -> `E7/E8 ?` -> `G3 ?` -> `regulator removal ?` -> `physical RG/E9 ?` -> `continuum Lorentzian geometry ?` -> `massless spin-2 ?` -> `GR recovery ?` -> `matter/QFT IR ?` -> `normalized falsifiable prediction ?`.

## Claim locks

No `NEW_PHYSICS_FOUND`; no complete-QG claim; no theorem that every causal face functional diverges; no generic finite-spin signed P3; no exact full-amplitude cancellation/non-cancellation theorem; no causal-vertex divergence theorem; no unique K5 extension; no regulator-independence theorem; no G3 PASS; no F9/G8/K5 promotion. Keep absolute integrability, conditional/PV finite parts and source-defined distributional amplitudes distinct.

## Next admissible Researcher gate

Prospectively freeze `ITER081F_SM_TWO_WEDGE_CAUSAL_BRANCH_SUBSET_BOUNDEDNESS_GATE`.

Required contract:
1. source motivation: BCG Eq. (46) plus Beltran's orientation-sum construction;
2. freeze before implementation `j=k=1/2`, arbitrary fixed `rho>0`, two identical pure boosts `beta>0`, four branch assignments `(++),(+-),(-+),(--)`, and unit-weight subset sums;
3. derive all branch entries from source formulas, not Critic result files;
4. test every nonempty subset under `beta->0+` using exact symbolic Laurent/limit analysis;
5. a no-rescue result requires proving every **proper** nonempty unit-weight subset unbounded while the full four-assignment sum is bounded and explicitly reconstructs the standard Wigner/EPRL object;
6. claim ceiling: local two-wedge pure-boost necessary control only; never promote to a theorem that Beltran's global causal `A^+` diverges, since global causal constraints correlate orientations across the full vertex/2-complex;
7. arbitrary complex weights, subtraction/renormalization and new causal face functionals require separate prospective gates;
8. before implementation, audit old `research/iteration-023-causal-sector-sums` to ensure it contains no already-authoritative equation-level Eq. (46) subset-boundedness result. Old surrogate/numerical work may be used only as historical control after validation.

If no bounded proper causal subset survives, the next Han route must be genuinely new model/theorem content rather than unchanged transplantation of Han's standard pole/condensation machinery.