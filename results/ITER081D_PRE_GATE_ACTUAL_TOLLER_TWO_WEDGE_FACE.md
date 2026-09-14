# Iter081D pre-gate — actual gamma-simple two-wedge Toller face vs Han face bound

Status: **Critic prospective object freeze only; no Researcher verdict.**
Date: 2026-09-14

## Frozen question
Does the natural all-`+` Toller branch term of a two-wedge internal face satisfy Han's standard uniform face bound, or is it already unbounded for actual gamma-simple Toller data?

## Frozen source objects
Use BCG arXiv:2604.24945v1 Eq. (46) and the exact pure-boost projected matrix elements. Use Han arXiv:2602.18665v1 internal-face structure `tau=d Tr[ordered product_v P D(U_v) P]` and comparison bound `|tau|<=d^2`.

## Frozen labels/path
- BCG spin labels: `j=k=1/2`;
- arbitrary fixed real `rho>0` (therefore the result, if obtained, is insensitive to factor-of-two Immirzi-label conventions between sources);
- branch assignment: `(+,+)`;
- face length: exactly two wedge factors;
- both wedge group elements: `g_beta=exp(-i beta K_z)`, `beta>0`;
- one-sided limit: `beta -> 0+`;
- projected magnetic basis: `m=+1/2,-1/2`.

Define the natural branch face term

`tau_{++,2}(beta) := d_j Tr_{H_j}[(P_j T^+(g_beta) P_j)^2]`, `d_j=2`.

For a pure z boost this is diagonal, so

`tau_{++,2}(beta)=2[(t_{m=+1/2}^+(beta))^2+(t_{m=-1/2}^+(beta))^2]`.

## Frozen criterion
Compare directly against Han's `d_j^2=4` face bound.
Classify this Critic control only as:
1. `TWO_WEDGE_BRANCH_FACE_BOUND_SURVIVES_ON_FROZEN_PATH` if exact algebra proves `|tau_{++,2}(beta)|<=4` for all `beta>0` with finite `beta->0+` limit;
2. `ACTUAL_TWO_WEDGE_TOLLER_FACE_BOUND_COUNTEREXAMPLE` if exact asymptotics prove `|tau_{++,2}(beta)|` diverges or exceeds 4 for admissible `beta>0`;
3. `ANALYTIC_CONTROL_INSUFFICIENT` otherwise.

## Controls / ceiling
- Use actual Eq. (46), not abstract matrices.
- Derive both magnetic components; do not infer the trace from a single element.
- No posthoc branch reassignment or rho choice.
- This is a natural algebraic branch term, not yet a source-authorized causal Han stack amplitude.
- A counterexample may rule out direct inheritance of Han's **same face bound** for this natural branch term, but it does not prove no alternative renormalized causal face functional exists, no full stack can exist, or any K5/W-selector/downstream claim.