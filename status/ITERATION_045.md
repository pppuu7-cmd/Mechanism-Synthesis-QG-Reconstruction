# Iteration 045 — correlated K3 finite-part covariance and epsilon-limit audit

Date: 2026-09-12

## Motivation
Iter044 established a nonzero polynomial quotient of degree 3 in the source-faithful joint K3 common-cycle spectral integrand, with a nonzero even t^2 term and predicted symmetric-cutoff R^3 growth. The next question was whether subtracting exactly that polynomial quotient produces a mathematically canonical correlated finite part.

A development-only pilot at the already-consumed Iter044 point `(gamma,epsilon,signs,k1,k2)=(1.2,0.05,++-,0.37,-0.61)` indicated that a residue-defined finite part may agree when the redundant cycle is parameterized by q1, q2, or q3. That point was excluded from production acceptance. Production values below were held out from that pilot.

## Frozen finite-part definition
For each equivalent cycle coordinate `u in {q1,q2,q3}`:

1. Express the same joint K3 rational spectral density in `u`, including the absolute Jacobian of the real-line reparameterization.
2. Perform exact polynomial division `K_u(u)=Q_u(u)+r_u(u)` with `r_u=O(1/u)`.
3. Define the symmetric Hadamard/PV finite part of the remainder by the exact upper-half-plane identity

   `FP_u = 2*pi*i*sum Res(r_u, upper poles) - i*pi*a_minus1`,

   where `a_minus1 = lim_{u->infinity} u*r_u(u)`.

Only the exact polynomial quotient is subtracted; no fitted coefficient or arbitrary counterterm is introduced.

## Authority
Main production commit: `977c0c518c7f64714d70ee94df6b8f85f0994166`.

- Iter045A held-out covariance run `34702746193`: **24/24 completed SUCCESS**.
- Iter045B independent Fourier-kinematic holdout run `34702746220`: **8/8 jobs SUCCESS**, with two frozen epsilons in each job, i.e. 16 additional held-out parameter points.
- Iter045C epsilon-scaling diagnostic run `34702746188`: **12/12 SUCCESS**, each with epsilon sequence `{0.2,0.05,0.01,0.002}`.

## Terminal scientific result — A+B
**PASS for the frozen K3 coordinate-covariance gate.** Across all 40 held-out A+B parameter points, the exact finite parts obtained by using q1, q2, or q3 as the redundant cycle coordinate are symbolically identical; the workflows require exact pairwise difference zero, numerical relative spread `<1e-11`, exact rational reconstruction, and polynomial quotient degree three. Every production job passed those gates.

This equality is nontrivial in mixed-sign sectors: for `(gamma,epsilon,signs,k1,k2)=(1.7,0.11,-++,0.23,-0.47)`, the three coordinate representations have different upper-half-plane pole counts `(1,2,2)` and the `a_minus1` coefficient changes sign, yet all three give exactly

`FP = 13.039479712959696978 - 38.805383257266235060 i`,

with exact pairwise differences `(0,0,0)` and numerical spread `0`.

Independent kinematic holdout example `(gamma,signs,k1,k2)=(1.35,++-,-0.41,0.58)`:
- epsilon `0.04`: all coordinates give `FP = -4.3542437456679353294 - 81.462057947464330035 i` exactly;
- epsilon `0.13`: all coordinates give `FP = -6.5433103375245265702 - 66.693265243880476780 i` exactly.

Classification: `K3_FINITE_PART_COORDINATE_COVARIANT` under the frozen source-faithful j=1/2 rational spectral representation.

## Epsilon diagnostic — C
All 12 epsilon-scaling jobs remain exactly coordinate-covariant at every tested epsilon. The finite parts show decreasing successive changes in inspected representative lanes, consistent with — but not proving — a finite epsilon->0 limit. Example `(gamma,signs)=(0.9,++-)`:

successive changes `42.6028608 -> 8.60169865 -> 1.46934819` as epsilon goes `0.2 -> 0.05 -> 0.01 -> 0.002`.

Example `(gamma,signs)=(1.7,-++)`:

successive changes `8.68352755 -> 6.83642261 -> 1.53014821`.

This stream remains **diagnostic only**; no distributional epsilon->0 theorem is claimed.

## Scientific classification
Iter045 removes one important ambiguity left by Iter044: the exact polynomial-subtraction + residue/PV finite part is not an artifact of choosing q1 versus q2 versus q3 on the K3 common cycle, over the frozen held-out coverage. It is therefore a viable **candidate correlated extension rule at K3**.

It is not yet a physical causal-spinfoam vertex definition. K4/K5 forest, cycle-basis, and integration-order consistency remain open. No G3, F9, G8, RG-closure, continuum, or novelty promotion follows.

## Next gate
Apply the **same frozen one-dimensional finite-part operator without retuning** to the three independent cycle variables of a K4 complete-graph source kernel. Compare different spanning-tree/fundamental-cycle bases and all sequential integration orders. A physical candidate must give the same result independent of forest/cycle basis/order, with an ordinary EPRL/no-contact control.
