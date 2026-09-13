# Iter075C preregistration — Toller Feynman-kernel inversion candidate audit

**Frozen before implementation/production.**

## Goal

Use the published Feynman `i epsilon` representation of Toller matrices (arXiv:2601.23162 Eq. (3), equivalently the 2026 Toller paper) to test a necessary kernel-level condition for two simple branchwise inversion candidates on the unchanged real `tilde-rho` contour:

1. same-branch candidate: `T^s_{jm,ln}(g^-1) = phase * conjugate(T^s_{ln,jm}(g))`;
2. flipped-branch candidate: `T^s_{jm,ln}(g^-1) = phase * conjugate(T^-s_{ln,jm}(g))`.

Because Wigner-D inversion supplies the conjugated matrix element, either simple candidate requires the ratio of the corresponding scalar Feynman/Gamma kernels to be independent of `tilde-rho`, up to a lane-dependent constant phase. This is a **necessary-condition audit only**.

## Frozen panel

- `(j,l)` lanes: `(1,1)`, `(1,2)`, `(3/2,1/2)`, `(2,3)`;
- `rho`: `0.7`, `1.3`;
- branch `s`: `+1`, `-1`;
- `epsilon = 1e-4`;
- real `tilde-rho` samples: `[-2.4,-1.1,-0.2,0.4,1.8,2.7]`;
- arithmetic: >= 70 decimal digits.

For each lane/candidate, normalize the complex kernel-ratio by its first sample and compute the maximum deviation from unity over the remaining samples.

## Frozen thresholds and controls

- Candidate is `kernel-compatible` only if max normalized deviation `<= 1e-20` in **every** frozen lane.
- Synthetic positive control multiplies the comparison kernel by a fixed complex phase and must recover max deviation `<= 1e-60`.
- All evaluated kernels/ratios must be finite and nonzero on the frozen panel.

## Frozen interpretations

- If neither same-branch nor flipped-branch candidate is kernel-compatible while controls pass: `ITER075C_SIMPLE_SAME_CONTOUR_TOLLER_INVERSION_CANDIDATES_OBSTRUCTED_SCOPED`.
- If at least one candidate is compatible in every lane: `ITER075C_SIMPLE_TOLLER_INVERSION_CANDIDATE_SURVIVES_KERNEL_GATE_SCOPED`.
- Any invalid arithmetic/control: `ITER075C_KERNEL_AUDIT_INVALID`.

A scoped obstruction does **not** rule out more general transformations involving representation-label changes, nontrivial `tilde-rho` changes of variable/contour, additional source-derived factors, or a different exact branch law. No tournament/sector promotion, no K5/G3/F9/G8 promotion, no finiteness/divergence theorem, no new-physics or complete-QG claim.
