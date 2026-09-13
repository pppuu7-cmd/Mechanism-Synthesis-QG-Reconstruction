# Iteration 063C preregistration — primary-source causal-vertex / EPRL-control pinning

Date: 2026-09-13

Prospective preregistration after terminal Iter063B BLOCKED and after acquisition of the independent primary-source snapshot in `sources/CAUSAL_SPINFOAM_VERTEX_2026_SOURCE_SNAPSHOT.md`. Iter063B remains terminal BLOCKED and is not reclassified.

## Question

Does the newly acquired primary-source object provide an internally consistent, equation-level specification sufficient to authorize a later direct causal-vertex numerical gate, while preserving the exact distinction between constrained causal signs and the ordinary EPRL control?

## Frozen source authority

- Bianchi, Chen, Gamonal, *Causal spinfoam vertex for 4d Lorentzian quantum gravity*, arXiv:`2601.23162`, DOI `10.1103/fwql-t4yr`.
- Tracked source snapshot commit: `7df82d28dd6426aa7aaac353a1e0abf795e6fdee`.

No MSQGR result file, audit script, or prior numerical output may substitute for the source equations.

## Frozen independent lanes

1. `vertex_object`: require Eq. (4) data — four unfixed `SL(2,C)` integrations after `g1=1`, ten wedges `1<=a<b<=5`, gamma-simple Toller blocks, and `g_ab=g_b^-1 g_a`.
2. `eprl_control`: require Eq. (5) `T+ + T- = D` and Eq. (6) ordinary EPRL as the unconstrained sum over all independent wedge signs; reject replacement by the constrained causal `sigma` sum.
3. `causal_conventions`: require source edge orientations `sigma_a`, `kappa_ab=sigma_a sigma_b`, gamma-simple `(rho,k)=(gamma j_ab,j_ab)`, and the source Feynman spectral `i epsilon` definition rather than `beta+i epsilon`.
4. `representation_guard`: require the direct Eq. (4) object to be stated without a preferred spanning tree, cycle basis, or sequential finite-part order, and require Eq. (7) Cartan/magnetic decomposition only as a representation of the same source Toller object.

Each lane is a qualification check, not an amplitude computation.

## Frozen aggregate rule

PASS requires all 4 lanes valid and all required source clauses present in the tracked snapshot. Any missing or contradictory clause yields BLOCKED/FAIL without fitting or inference.

Frozen outputs:
- `ITER063C_PRIMARY_SOURCE_VERTEX_CONTROL_PINNED`
- `ITER063C_BLOCKED_SOURCE_OBJECT_INCOMPLETE`
- `ITER063C_FAIL_EPRL_CONTROL_CONFLATED_WITH_CAUSAL_SUM`
- `ITER063C_IMPLEMENTATION_INVALID`

## Interpretation

A PASS only authorizes preregistration of a **later** direct Eq.(4)-level numerical/symbolic gate with exact Eq.(5)/(6) EPRL control. It does not establish causal-vertex finiteness, physical sector selection, F9/G3/G8/K5, a continuum limit, or new physics.
