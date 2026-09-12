# Iteration 024 — Boundary-intertwiner multi-collision power counting

Status: **COMPLETED / BOUNDARY CONTRACTION DOES NOT CURE MULTI-COLLISION POLES**

Workflow: `Boundary Intertwiner Collision Power`

- 6/6 GitHub jobs completed successfully.
- gamma = 0.2, 1.2, 2.0; two independent collision rays (seeds 19, 43).
- all ten boundary spins fixed at j=1/2.
- four representative gauge-invariant five-node boundary states in the 4-valent recoupling basis were contracted before power fitting:
  - `(0,0,0,0,0)`,
  - `(2,2,2,2,2)`,
  - `(0,2,0,2,0)`,
  - `(2,0,2,0,2)` in doubled-intertwiner notation.
- modes: `Cplus16`, `Cminus16`, `Cboth32`, fixed all-plus and EPRL control.

The calculation constructs the full 2x2 Toller matrix on every wedge and contracts the complete K5 boundary spin network with five normalized 4-valent SU(2) intertwiners before measuring the common-scale collision power.

## Aggregate causal result

Across the three summed causal modes and all six gamma/ray runs there are 72 causal rows per cluster size.

### k = 2

- slope range: **-2.387808 ... -1.695986**
- first moment: **72/72 PASS**
- second moment: **0/72 PASS**

### k = 3

- slope range: **-6.538676 ... -5.944706**
- first moment: **66/72 BORDERLINE_LOG**, **6/72 FAIL**
- second moment: **0/72 PASS**

The few stronger-than-logarithmic rows are boundary-state/ray dependent; they do not indicate a softening mechanism.

### k = 4

- slope range: **-12.142049 ... -11.833104**
- first moment: **72/72 FAIL**
- second moment: **0/72 PASS**

### k = 5

- slope range: **-20.091897 ... -19.862215**
- first moment: **72/72 FAIL**
- second moment: **0/72 PASS**

## EPRL control

All **96/96** EPRL boundary-contracted rows pass both the first- and second-moment power criteria. Some EPRL components vanish with extra positive powers because of boundary-state cancellations, but none develop the causal multi-pole divergence.

## Interpretation

The multi-collision warning survives all ordinary linear structures tested so far:

1. individual causal magnetic components,
2. sums over the 16 factorized causal structures,
3. addition of the co-causal partner,
4. full gauge-invariant SU(2) boundary-intertwiner contraction.

Therefore ordinary magnetic or boundary-state cancellation is not a viable generic cure of the k>=3 Toller collision strata in this j=1/2 carrier.

This is still not a proof that the physical causal vertex is undefined. The published causal construction defines Toller matrices through a Feynman i-epsilon distribution. In the coherent/spinor representation the result contains boundary-supported delta and delta-derivative terms. Pointwise power counting of the ordinary Toller functions does not include the action of those distributions on the boundaries of causal integration regions.

## Next target

Iteration 025 validates and implements the Appendix-D distributional boundary term for j=1/2 on smooth test functions. Only after that unit is under control is it meaningful to define a multi-wedge distributional prescription for intersecting collision strata.
