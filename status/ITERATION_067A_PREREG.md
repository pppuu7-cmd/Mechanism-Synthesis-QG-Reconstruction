# Iteration 067A preregistration — joint boundary-value / microlocal selector qualification

Date: 2026-09-13

This gate is frozen **before** implementation/production.

## Question

Can an already-established mathematical boundary-value or microlocal theorem provide the missing *source-faithful selector* for the physical BCG2026 finite-spectral-`i epsilon` Toller family at correlated K5 level, without arbitrary counterterms or preferred sequential order?

## Candidate lanes

1. `BCG2026_PHYSICAL_PRESCRIPTION`
2. `HORMANDER_ANALYTIC_BOUNDARY_VALUE`
3. `HORMANDER_WAVEFRONT_PRODUCT`
4. `BRUNETTI_FREDENHAGEN_EXTENSION`

## Frozen predicates

Each lane is audited against four predicates:

- `Q1_JOINT_PHYSICAL_FAMILY`: the result either supplies, or directly applies to, a **joint multivariate** analytic/distributional family identified with the physical Toller finite-`i epsilon` prescription rather than a surrogate subtraction scheme;
- `Q2_CHECKABLE_EXISTENCE_HYPOTHESES`: it states checkable holomorphy/tube, growth/temperedness, cone/wavefront or scaling-degree hypotheses sufficient to define the relevant boundary value/product/extension;
- `Q3_UNIQUE_SOURCE_SELECTOR`: when its hypotheses hold, the resulting distribution is unique in the needed sense without free local counterterms, fitted coefficients or a preferred integration/tree/cycle order;
- `Q4_DISTRIBUTIONAL_EPRL_BRIDGE`: the theorem/source supplies, or the repo already proves, the hypotheses needed to inherit BCG Eq.(5)/(6) independent-wedge EPRL control at the **distributional K5** level.

A lane is a `complete_selector_bridge` iff all Q1-Q4 are true.

## Frozen aggregate interpretation

- If any lane is a complete selector bridge: `ITER067A_BOUNDARY_VALUE_SELECTOR_ROUTE_QUALIFIED`.
- Else if at least one lane satisfies Q2+Q3 but fails Q1 or Q4: `ITER067A_THEOREM_ROUTE_EXISTS_PHYSICAL_HYPOTHESES_UNPROVEN`.
- Else: `ITER067A_BOUNDARY_VALUE_SELECTOR_ROUTE_NOT_YET_AVAILABLE`.

The aggregate must report exactly which missing hypotheses prevent promotion. Green CI is not scientific PASS.

## Scope / claim locks

This gate cannot prove physical causal-vertex finiteness, absolute integrability, existence of the full amplitude, F9/G3/G8 closure, physical sector selection or `NEW_PHYSICS_FOUND`. It may only qualify a theorem route or localize missing hypotheses. Generic renormalization freedom is not a physical selector. The published spectral `i epsilon` is not replaced by `beta+i epsilon`.
