# Iteration 028 — multi-wedge distribution-product geometry

Status: **RUNNING / PARALLEL INCIDENCE-PRODUCT AUDIT**

Date: 2026-09-12

## Why this gate is now required

The conditional-finiteness campaign has removed several cheap escape routes without proving a full causal-vertex no-go:

1. Iter026 completed successfully at workflow level and a consumed raw lane shows `NO_GENERIC_ANTIPODAL_CANCELLATION`: k=3 can have strong odd/parity cancellation, but k=4 and k=5 rows in that lane have antipodal ratio 1.
2. Iter027A completed successfully at workflow level and a consumed raw lane gives `NO_UNIVERSAL_GLOBAL_ANGULAR_CANCELLATION`; full-sphere mean/RMS ratios remain O(10^-2..10^-1) rather than universally vanishing.
3. The exact K5 Christensen spanning-tree audit proves that any positive absolute-value convex tree cover needs a maximum tree-edge exponent M >= 5/2, while a beta^-2 Toller norm permits only m < 3/2 for local single-edge integrability. Therefore that specific standard finiteness strategy cannot close for the tested Toller singularity. This is a method no-go, not a causal-vertex divergence theorem.
4. The weighted full-matrix Toller control reproduces p approximately 2 and excludes the required K5 weight 2.5 in the consumed lane.

These results make the product/intersection of the Appendix-D boundary distributions the next legitimate mathematical target.

## Active gate

Workflow: `Multiwedge Incidence Distribution Product Audit`

Run: `34668954203` (launched from `dda173e9b3dd4069ad6a9d24adae3a7d4c76ee1a`).

Parallel lanes:
- K3, j=1/2, rho=0.2;
- K4, j=1, rho=0.6;
- K5, j=3/2, rho=1.0.

The reduced incidence matrix linearizes edge boundary coordinates as y_ab=x_a-x_b after one vertex is gauge-fixed. The audit computes:

- exact incidence rank;
- cycle nullity E-rank;
- the nonzero lowest Appendix-D delta coefficient;
- the exact Gaussian-mollifier integral of the product of all edge delta terms;
- the fitted eta-divergence exponent versus the predicted redundancy exponent E-rank.

For complete graphs the predicted cycle nullities are:
- K3: 1;
- K4: 3;
- K5: 6.

A matching eta^{-nullity} divergence would exclude a regulator-independent **naive pointwise product** of the lowest boundary delta terms in this linearized realization. It would not exclude a correlated source-backed i-epsilon extension, wavefront-compatible distributional prescription, matrix/intertwiner cancellation, or counterterm/renormalized extension.

## Decision discipline

- Do not promote the linearized incidence result to a full causal-EPRL divergence theorem.
- Do not weaken the radial or absolute-integrability gates.
- If the redundancy divergence is confirmed, the next target is a source-backed microlocal/correlated-i-epsilon extension criterion, not further random angular scans.
- F9 and G8 novelty remain blocked until a finite same-realization causal carrier and refinement law are established.
