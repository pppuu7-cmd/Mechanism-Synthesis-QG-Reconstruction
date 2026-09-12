# Iteration 051B — terminal result: RR beyond preregistered coarse residue structure

**Date:** 2026-09-12

## Authoritative production

- workflow run: `34713037668`
- merged implementation: `1483a71dc2eaf3cc72e915453c6891d3f1daa595`
- preregistration commit: `596b431d5d4173f6d8674a774f4ffec03d0ab1f0`
- aggregate artifact: `10304474485` (`iter051b-aggregate`)
- artifact digest: `sha256:3c0483a01b283178193965a5dc54fe92ab19b85f7998041834336967cc27af43`
- frozen matrix: 8 factorized causal-sign classes × 4 trees × 3 pairs = **96 lanes** at independent held-out point H3

## Frozen classification

`K4_RR_BEYOND_PREREG_RESIDUE_STRUCTURE`

All 96/96 lanes are valid. All control RR commutators are exactly zero and all factorized-sign checks pass. The source RR diagnostic is nontrivial, with **48/96** RR-active lanes.

No one of the eight prospectively frozen coarse discrete residue/cancellation booleans exactly matches `RR_nonzero` on all 96 lanes. Therefore `exact_matching_diagnostics = []`.

Frozen contingency counts `(RR1/F1, RR1/F0, RR0/F1, RR0/F0)` are:

- first upper-count asymmetry: `(14, 34, 24, 24)`
- second upper-count asymmetry: `(32, 16, 11, 37)`
- first nonzero-residue-count asymmetry: `(14, 34, 24, 24)`
- second nonzero-residue-count asymmetry: `(32, 16, 11, 37)`
- first residue-sum-zero asymmetry: `(0, 48, 16, 32)`
- second residue-sum-zero asymmetry: `(10, 38, 0, 48)`
- internal-cancellation asymmetry: `(0, 48, 0, 48)`
- combined discrete residue-signature asymmetry: `(32, 16, 34, 14)`

## Scientific interpretation

The independent H3 test rejects all preregistered **coarse discrete** residue/cancellation diagnostics as exact selectors of the sequential RR obstruction. This is compatible with Iter051's sharper exact ordered residue-sum statement, because the latter uses the actual exact residue sums rather than a compressed boolean signature.

No post-hoc selector fitting is authorized. The negative result shifts priority toward source/analyticity-selected simultaneous multivariate K4 constructions and exact algebraic identities fixed before seeing production output.

K5 remains `BLOCKED`; G3 remains `OPEN`; physical F9 remains `BLOCKED`; G8 remains `BLOCKED_CONVERGENCE_ONLY`.
