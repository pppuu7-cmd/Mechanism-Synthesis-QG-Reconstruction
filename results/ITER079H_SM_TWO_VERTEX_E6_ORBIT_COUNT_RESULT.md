# Iter079H-SM — minimal two-vertex E6 orbit-count result

## Authority
- Prospective preregistration: `a9fe328ec51ab5ec23504669daa4b7cc6dedbeaa`.
- Implementation: `719364a9da114cf63983db2117e07f7ed0fbca0e`.
- Production head: `4b84977db6b223e226c8263fee851f931e4f46e6`.
- Authoritative terminal run: `34808179196`.
- Raw artifacts: A `10334191296`, B `10334280398`, C `10333277596`, D `10333448285`.
- Aggregate artifact: `10333921372`.
- Aggregate digest: `sha256:bec93b1c71d8fc2cc1a675c312216dae6adfff17c721b6d88275be74f167b8b0`.

All four raw lanes and aggregate were terminal and consumed before classification.

## Classification
`ITER079H_SM_MINIMAL_TWO_VERTEX_KKL_GLUE_RETAINS_TWO_INDEPENDENT_COMMON_LEFT_REDUNDANCIES_DIAGONAL_QUOTIENT_INSUFFICIENT_EXACT_SCOPED_E6_PARTIAL`

Verdict: **PASS, exact/scoped; E6 partial only**.

## Frozen outcomes
- Lane A `PASS`: dependencies Iter079E/F were terminal, and the frozen KKL gluing model contracts boundary-state data without identifying the distinct Lorentz-group integration variables of the two local vertices.
- Lane B `PASS`: all ten relative wedges at vertex 1 are exactly invariant under an independent `h1`, and all ten at vertex 2 under independent `h2`; the frozen glued scalar boundary contraction is independent of both redundant orbit coordinates. The minimal composed object therefore has exact `G x G` common-left redundancy in this scope.
- Lane C `PASS`: quotienting only the diagonal subgroup leaves the exact relative orbit word `h2^-1 h1`. Dimension control for `G=SL(2,C)` gives real dimensions `12 - 6 = 6`, so one full group orbit remains unfixed.
- Lane D `PASS`: all scope locks passed; no quotient measure or normalization was selected.

## Scientific effect
The E6 problem is narrowed again. In the frozen minimal two-vertex KKL-glued causal composition, the two local common-left redundancies remain independent. A single diagonal gauge fixing is therefore insufficient in this factorized local-integration model. The remaining E6 question is not whether redundant orbits exist or how many occur in this minimal case; it is how the **source-faithful quotient/fixing measure and normalization** are defined and how this extends to general multi-vertex foams.

## Scope locks
No unique gauge-fixing prescription; no finite gauge-volume claim; no Faddeev-Popov theorem; no complete E6 theorem for arbitrary foams; no E7/E8 selector; no G3/F9/G8/K5/RG promotion; no complete-QG claim; no `NEW_PHYSICS_FOUND`.

## Next admissible step
Prospectively audit whether the parent EPRL/KKL prescription fixes one redundant Lorentz-group integration per internal vertex and whether Beltran's causal construction explicitly inherits that quotient/fixing normalization. If source authority is absent, record a source/object-definition blocker rather than choosing a normalization. Independently, E3 and the physical E4 source bridge remain open.
