# Iter079F-SM — common-left gauge inheritance result

## Authority
- Prospective preregistration: `3e5926623b547bc1088d518cebb4ca0eb8d66657`.
- Implementation: `c6d2b0daeedc6c860be90f4b90f06565e48fca72`.
- Production head: `e42b93541e2d739cb271770e8913cc2cc008af40`.
- Authoritative terminal run: `34807939721`.
- Raw artifacts: A `10333358231`, B `10333418161`, C `10333182814`, D `10333358230`.
- Aggregate artifact: `10333931825`.
- Aggregate digest: `sha256:a542e13e6ebe2d59e78fc47d5da12b586141e224fec9a621ab8dd82345ad88da`.

All four raw lanes and aggregate were terminal and consumed before classification.

## Classification
`ITER079F_SM_CAUSAL_TOLLER_VERTEX_COMMON_LEFT_GAUGE_REDUNDANCY_CONDITIONALLY_INHERITS_EXACT_SCOPED_E6_PARTIAL`

Verdict: **PASS, conditional/scoped; E6 partial only**.

## Frozen outcomes
- Lane A `PASS`: the frozen source/provenance contract contains causal dependence on relative elements `g_b^-1 g_a`, the parent common-left redundancy premise, Iter079E's local-replacement inheritance scope, and the finiteness lock. No ordinary representation-composition property of Toller functions was used.
- Lane B `PASS`: for all ten K5 wedges, exact free-group reduction gives
  `inv(h g_b) (h g_a) = inv(g_b) g_a`.
  Thus simultaneous common-left multiplication leaves every causal relative argument unchanged exactly.
- Lane C `PASS`: all ten local relative factors are unchanged along the common-left orbit. Hence the redundant orbit survives and an ungauge-fixed integration formally carries the common group-volume factor. This establishes the need for quotient/fixing but does not select its normalization.
- Lane D `PASS`: independent left actions `g_a -> h_a g_a` do not cancel generically. The inherited redundancy is the single simultaneous common-left action. All scope locks passed.

## Scientific effect
The earlier E6 blocker is narrowed. Under the same local causal-vertex replacement hypothesis used in Iter079E, the **existence and algebraic form of the one-vertex common-left gauge redundancy are inherited exactly**. Therefore causal/Toller branch replacement does not by itself destroy the standard one-vertex common-left redundancy.

What remains unresolved inside E6 is the genuinely physical/compositional part: multi-vertex gauge-orbit counting after gluing, quotient/fixing measure and normalization, treatment of residual/noncompact gauge volume, and compatibility of that prescription with E3/E4 and E7/E8.

## Scope locks
This is not a complete E6 theorem; it does not prove finiteness, unique quotient normalization, a multi-vertex gauge-fixing theorem, regulator independence, E7/E8 extension selection, G3/F9/G8/K5 promotion, RG, complete QG, or `NEW_PHYSICS_FOUND`.

## Next admissible step
A dependent E6 successor may now prospectively test the **minimal two-vertex gauge-orbit quotient** under KKL gluing with the inherited E5 convention and one common-left redundancy per local causal vertex. The gate must distinguish exact orbit-counting/gauge-redundancy facts from any unsupported choice of quotient normalization. In parallel, an independent source audit may test whether E4 face/edge weights are explicitly inherited under the local causal-vertex replacement; do not assume this without source authority.
