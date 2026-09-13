# Iteration 064A preregistration — source-defined direct causal integrand / exact EPRL control

Date: 2026-09-13

Prospective preregistration after terminal Iter063C `ITER063C_PRIMARY_SOURCE_VERTEX_CONTROL_PINNED` and before Iter064A production.

## Question

On generic separated `SL(2,C)` group configurations, does the repository's direct ten-wedge carrier implement the source-defined Eq.(4) Toller structure consistently with the exact source Eq.(5)/(6) EPRL control, without replacing the source spectral prescription or conflating constrained causal signs with the unconstrained EPRL sum?

## Frozen source

Primary source snapshot commit `7df82d28dd6426aa7aaac353a1e0abf795e6fdee`, qualified by Iter063C authoritative run `34732046499`.

## Frozen panel

Six independent lanes:

- `gamma ∈ {0.4, 1.2}`
- `seed ∈ {1701, 1702, 1703}`
- direct group samples generated with minimum pair boost `beta >= 0.12`
- `j=1/2` pointwise ten-wedge carrier already implemented in `vertex/direct_causal_integrand_smoke.py`

No result-dependent seed/gamma replacement is allowed.

## Frozen per-lane checks

1. KAK reconstruction error `< 1e-10`.
2. Every edge obeys source additive control `T+ + T- = D`, with lane maximum relative residual `< 1e-35`.
3. Explicit sum over all `2^10` independent wedge signs agrees with the direct EPRL pointwise integrand, relative residual `< 1e-35`.
4. The 32 edge-orientation assignments reduce by global reversal to the 16 causal classes, duplication residual `< 1e-60`.
5. The implementation keeps the constrained causal 16-class sum separate from the unconstrained EPRL control. No equality between those two objects is required or inferred.
6. No `beta+i epsilon`, fitted subtraction, counterterm, preferred tree/cycle basis, or sequential finite-part rule is introduced.

## Frozen aggregate rule

PASS requires all 6 lanes structurally valid and all four numerical controls above their frozen tolerances. Green CI alone is not PASS; raw lane artifacts and aggregate must be consumed.

Frozen outputs:

- `ITER064A_DIRECT_CAUSAL_POINTWISE_EPRL_CONTROL_PASS`
- `ITER064A_DIRECT_CAUSAL_POINTWISE_CONTROL_FAIL`
- `ITER064A_IMPLEMENTATION_OR_NUMERICAL_INVALID`

## Interpretation

Even full PASS is only a **pointwise integrand/carrier** certificate for the frozen small-spin panel. It is not a four-group Haar integral, not a boundary-intertwiner-contracted vertex, not a finiteness/absolute-integrability theorem, and does not promote K5/F9/G3/G8 or establish new physics. A later integrated gate must be separately preregistered with regulator/quadrature convergence controls.
