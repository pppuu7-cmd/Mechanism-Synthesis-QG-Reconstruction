# Iter081E-SM prereg — independent Researcher reproduction of actual Toller Han-bound counterexamples

Status: **PROSPECTIVE RESEARCHER PREREGISTRATION — frozen before implementation/production**
Date: 2026-09-14

## Motivation
Iter081B is Researcher-chain `BLOCKED_SOURCE_BRIDGE` and independently confirmed. Independent Critic controls Iter081C/D subsequently reported exact actual-Toller counterexamples to (i) Han's projected-wedge contraction and (ii) the natural two-wedge selected-branch face `d_j^2` bound. Those Critic results are not yet Researcher-chain verdicts. This gate independently reproduces the algebra from the frozen BCG formula without importing Critic-derived intermediate expressions as pass labels.

## Frozen source/object
Use Bianchi--Chen--Gamonal arXiv:2604.24945v1 Eq. (46), gamma-simple specialization, pure boost `g_beta=exp(-i beta K_z)`, `beta>0`, minimal spin `j=k=1/2`, arbitrary fixed finite real `rho>0`.

Frozen Eq. (46) branch formula:
`t_{jjm}^{(±,rho,j)}(beta) = exp[-(j ∓ i rho ± m +1) beta] * Gamma(2j+2) Gamma(± i rho ∓ m) / (Gamma(j ∓ m +1) Gamma(j+1 ± i rho)) * 2F1(j ± m +1, j+1 ∓ i rho; 1 ± m ∓ i rho; exp(-2 beta)).`

No toy replacement for Toller matrices is admissible in the positive gate.

## Frozen subgate A — one-wedge projected contraction
Set branch `+`, `m=+1/2`. Independently simplify Eq. (46) using exact Gamma recurrence and the exact hypergeometric identity `2F1(a,b;b,z)=(1-z)^(-a)` only after verifying the required parameter equality.

Classification:
- `A_COUNTEREXAMPLE` iff the derived exact modulus is unbounded as `beta->0+` and therefore exceeds 1 for some admissible `beta>0`.
- `A_SURVIVES` iff the exact expression proves modulus <=1 for all beta>0 with finite compatible beta->0+ limit.
- otherwise `A_INSUFFICIENT`.

Frozen claim ceiling: only failure/survival of Han-type projected contraction on this path.

## Frozen subgate B — natural two-wedge selected-branch face
Set branch assignment `(+,+)` and two identical pure boosts. Use both diagonal magnetic components `m=+1/2` and `m=-1/2` derived independently from Eq. (46). Define only the frozen natural two-wedge term
`tau_pp_2(beta)=2[(t_{m=+1/2}^+(beta))^2+(t_{m=-1/2}^+(beta))^2]`.

Compute the exact one-sided leading coefficient `lim_{beta->0+} beta^4 tau_pp_2(beta)`.

Classification:
- `B_FACE_BOUND_COUNTEREXAMPLE` iff the exact limit exists and is nonzero positive for arbitrary fixed rho>0, implying `|tau_pp_2| -> infinity` and hence violation of Han's `d_j^2=4` bound for sufficiently small beta>0.
- `B_FACE_BOUND_SURVIVES` iff the exact result proves `|tau_pp_2|<=4` for all beta>0.
- otherwise `B_INSUFFICIENT`.

## Required implementation controls
1. Derive both m components from the frozen Eq. (46), not from Critic result files.
2. Verify all Gamma/hypergeometric parameter equalities symbolically before simplification.
3. Keep beta>0 and use one-sided limits.
4. Include at least three independent positive rational rho test values as non-authoritative numerical/symbolic regression controls; final classification must rest on symbolic rho.
5. Include a negative control showing that replacing the exact Eq. (46) coefficient by a bounded surrogate cannot satisfy the positive counterexample predicate.
6. Production artifact must record formula-derived expressions, exact limits, controls, and provenance commit SHAs.

## Frozen combined outputs
- `ITER081E_SM_ACTUAL_TOLLER_ONE_WEDGE_AND_NATURAL_TWO_WEDGE_HAN_BOUNDS_COUNTEREXAMPLES_REPRODUCED_EXACT_SCOPED` iff A=`A_COUNTEREXAMPLE` and B=`B_FACE_BOUND_COUNTEREXAMPLE` with all controls valid.
- `ITER081E_SM_ACTUAL_TOLLER_HAN_BOUND_REPRODUCTION_PARTIAL_OR_FAIL_SCOPED` for a scientifically valid nonpassing A/B outcome.
- `INVALID_IMPLEMENTATION_OR_PROVENANCE` if source/formula/control/provenance requirements fail.

## Claim locks
Even a positive result does **not** establish a complete causal face functional, all-spin/all-branch failure, causal-stack divergence, K5 selector, E3/E4/E6 inheritance, regulator independence, G3, F9/G8 promotion, or `NEW_PHYSICS_FOUND`. It only blocks unchanged transplantation of Han's projected-unitary contraction and `d_j^2` face bound to the frozen actual selected-branch objects.