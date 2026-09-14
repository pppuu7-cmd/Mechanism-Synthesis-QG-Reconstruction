# Iter081B pre-gate formula note — causal Toller branch face transport into Han stack

Status: **Critic pre-gate object definition only; no Researcher verdict.**
Date: 2026-09-14

## Exact source algebra motivating the successor

Han's internal EPRL/KKL face functional is

`tau_k^(h)(g_h) = d_k Tr_[k,rho] [ ordered_product_{v in boundary h} P_k D(U_v) P_k ]`,

with `U_v = g_ve^{-1} g_ve'` and `D` the principal-series unitary `SL(2,C)` representation matrix. Han's subsequent UV mechanism uses a uniform bound and saturation theorem for this `tau`, the bosonic grand-canonical product `Xi_h(s)`, pole dominance, condensation/localization, gauge-fixed integration, cut/gluing and boundary-block reduction.

BCG's exact additive identity is

`D(U) = T^(+)(U) + T^(-)(U)`.

Therefore, by ordinary matrix distributivity, Han's **standard** face functional admits the exact algebraic expansion

`tau_k^(h) = sum_{epsilon: boundary h -> {+,-}} tau_{k,epsilon}^(h)`,

where a natural branch term is

`tau_{k,epsilon}^(h) := d_k Tr [ ordered_product_{v in boundary h} P_k T^(epsilon_v)(U_v) P_k ]`.

This identity is only an algebraic decomposition of Han's original EPRL/KKL face functional. It does **not** by itself install any single `tau_{k,epsilon}^(h)` as a source-authorized causal stack face amplitude.

Beltran v2 provides independent motivation for branch selection at the vertex level: the causal EPRL-KKL vertex on an arbitrary 2-complex is obtained by replacing wedge Wigner matrices by Toller matrices with causal signs. It does not derive the Han stack state sum built from `tau_{k,epsilon}^(h)`.

## Exact transport obstruction to test

Han's proofs use properties that are not automatic consequences of `D=T^+ + T^-`:

1. **Uniform face bound:** source-prove an analogue of `|tau_k^(h)| <= d_k^2` for the selected causal branch functional.
2. **Saturation locus:** source-prove the exact maximizers and whether they remain the SU(2)/flat locus used by Han.
3. **Vanishing/compactness control:** Han uses matrix coefficients of a nontrivial unitary representation tending to zero at infinity and operator-norm estimates. BCG explicitly states that individual Toller matrices are not Lorentz-group representations, so this proof cannot be inherited by citation alone.
4. **Bosonic partition function:** establish convergence/meromorphy for a causal `Xi_h^epsilon(s)` and identify its dominant poles without importing the standard-EPRL bound post hoc.
5. **Localization/condensation:** prove that the causal branch pole structure yields the same or a controlled replacement critical manifold and stationary-phase localization.
6. **Cut/gluing:** prove that branch assignments and causal constraints compose under Han's SU(2)-boundary gluing and coupling relation, rather than assuming the standard EPRL/KKL identity survives.
7. **Source-order compatibility:** connect the face/stack object back to the source-ordered causal local Toller object without replacing the K5 distributional-extension problem by a different face surrogate.
8. **Full-W reachability remains downstream:** even a successful causal stack construction must still derive a map on the entire Iter077Q `W`; finite boundary-block scalar data are insufficient by repaired Iter080D.

## Negative theorem ceiling

The available source facts justify only:

`DIRECT_HAN_D_TO_SINGLE_TOLLER_BRANCH_INHERITANCE_IS_NOT_SOURCE_PROVEN`.

They do **not** justify:

`NO_CAUSAL_TOLLER_STACK_CAN_EXIST`.

A new causal face functional and new proofs could in principle close the bridge, but that is new model/theorem content and must be prospectively frozen rather than retroactively attributed to Han/BCG/Beltran.

## Recommended Iter081B contract

Prospectively test the natural branch functional above against items 1--7 using primary-source formulas and explicit mathematics. A result may be source-blocked if the needed theorem is absent, but the implementation must not encode the scientific answer as preassigned booleans. If a new proof is attempted, its assumptions, function spaces, branch consistency, convergence, regulator ordering and claim ceiling must be frozen before calculation.
