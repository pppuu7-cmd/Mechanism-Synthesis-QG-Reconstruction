# Iteration 051A — terminal result: factorized causal-sign RR nuisance stability

**Date:** 2026-09-12

## Authoritative production

- workflow run: `34713025288`
- merged implementation: `910db9ea333f88db55c47bcbca297ac98e7fa964`
- preregistration commit: `fd0086e0fe75663834ebc0fe665cf3bde7521896`
- aggregate artifact: `10303884916` (`iter051a-aggregate`)
- artifact digest: `sha256:56270b122eee124d02388d246d687f4b85337c5ba5aa6307bb5d68b0f5265a0c`
- frozen matrix: 2 held-out nuisance points × 8 factorized causal-sign classes × 4 trees × 3 pairs = **192 lanes**

## Frozen classification

`K4_RR_SIGN_CLASS_NUISANCE_STABLE`

All 192/192 lanes are valid. All EPRL/F=1 control totals and channel commutators are exactly zero, and all factorized-sign consistency checks pass.

For every one of the eight factorized causal-sign classes, the 12-bit RR mask is identical at H1 and H2. Total Hamming distance across all eight classes is exactly **0**.

Frozen class masks (`tree/pair`) are:

- `+++` — 4 active: `P1/01`, `P1/02`, `P1/12`, `S0/01`.
- `++-` — 7 active: `P0/12`, `P1/01`, `P1/02`, `P1/12`, `S0/01`, `S0/12`, `S1/12`.
- `+-+` — 5 active: `P0/01`, `P0/02`, `P0/12`, `P1/01`, `S0/01`.
- `+--` — 8 active: `P0/01`, `P0/02`, `P0/12`, `P1/01`, `P1/12`, `S0/01`, `S0/12`, `S1/12`.
- `-++` — 6 active: `P0/01`, `P0/02`, `P0/12`, `P1/12`, `S1/01`, `S1/12`.
- `-+-` — 5 active: `P0/01`, `P0/02`, `P0/12`, `S0/12`, `S1/01`.
- `--+` — 7 active: `P0/01`, `P0/12`, `P1/01`, `P1/02`, `P1/12`, `S1/01`, `S1/12`.
- `---` — 6 active: `P0/01`, `P1/01`, `P1/02`, `P1/12`, `S0/12`, `S1/01`.

## Scientific interpretation

This establishes **scoped nuisance stability** of the sequential K4 RR sign-class masks on two prospectively held-out nuisance points. It is stronger than the Iter050 one-at-a-time sign observation, but it is not a theorem of global sign universality and does not define a physical multivariate K4 extension.

The next admissible sign-specific test is an independently preregistered wider-range nuisance validation with the H1/H2 masks frozen as references before implementation.

K5 remains `BLOCKED`; G3 remains `OPEN`; physical F9 remains `BLOCKED`; G8 remains `BLOCKED_CONVERGENCE_ONLY`.
