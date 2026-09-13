# Iter072B result — K4 signed cut-space leading coefficient

Date: 2026-09-13

## Gate
`K4_SCHWINGER_SIGNED_CUTSPACE_LEADING_COEFFICIENT`

Prospective preregistration: `b334f75f4ffa15a1148a178fca20bc6def465ecf`.
Production head: `c04afc38db5d8ff454246574e784b89648a73b5e`.
Run: `34744334585`.
Aggregate job: `103689386630`.
Aggregate artifact: `10313588852`.
Aggregate digest: `sha256:4ab193fb0e66cabfe48ce6fa1bdad180154d00c2f7a258b933f729f9e09db48f`.

## Frozen classification
`ITER072B_K4_COMMON_EPSILON_EPS_MINUS3_LEADING_COEFFICIENT_IFF_TRANSITIVE_TOURNAMENT_SCOPED`

All 8 raw sigma lanes were consumed. All were structurally valid and all frozen predicates P1–P8 passed in all four exact cycle bases. The strict-positive Schwinger kernel `L^T diag(s)t=0`, `t>0`, has a three-dimensional relative interior exactly for the four transitive/acyclic source sigma classes `++++`, `+++-`, `++--`, `+---`. The other four source classes `++-+`, `+-++`, `+-+-`, `+--+` have no strict-positive full-collision kernel witness. Exact rank is 3 and full kernel dimension is 3; every proper denominator stratum has degree at most 2. Source numerator/test constant terms are nonzero and basis-independent in this gate.

The wrong-sign-map control disagrees on the nontransitive lanes and the frozen global negative-control requirement passes.

## Scientific interpretation
This is a scoped exact result for the leading full-collision `epsilon^-3` coefficient of the reduced K4 common-epsilon rational family. It corrects the failed cycle-space premise of Iter072A by using the Schwinger cut-space condition. It is not a physical causal-sector selection, not a theorem for the complete causal EPRL vertex, and not a K5/distributional-boundary-value theorem.

For the four nontransitive classes the leading full-collision coefficient vanishes under this criterion; subleading/proper-collision contributions remain open and must be classified separately before any stronger statement.
