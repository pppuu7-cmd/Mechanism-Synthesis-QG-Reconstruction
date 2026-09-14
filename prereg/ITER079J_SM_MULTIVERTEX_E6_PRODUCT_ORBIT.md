# Iter079J-SM — MULTIVERTEX E6 PRODUCT-ORBIT GATE

## Status

Prospectively frozen **before implementation/production**.

## Scientific question

Under the already-scoped inheritance class used by Iter079E/F/H — each causal/Toller local vertex factor depends on local group variables only through pairwise combinations `g_{v,b}^{-1} g_{v,a}`, and KKL gluing contracts boundary data without identifying the local common-left group variables — does the exact common-left redundancy extend from one/two vertices to a direct product `G^V`, `G=SL(2,C)`, for finite connected vertex graphs with `V=1..5`?

This gate addresses **orbit counting only**. It does not choose a quotient measure, fixing, FP determinant, Haar normalization, finite part, or physical multi-vertex amplitude.

## Frozen lanes

### Lane A — local word invariance
For every vertex `v`, every local wedge pair `(a,b)`, and a formally independent left symbol `h_v`, verify by exact free-word reduction

`(h_v g_{v,b})^{-1}(h_v g_{v,a}) = g_{v,b}^{-1} g_{v,a}`.

No cross-vertex identification of `h_v` is allowed.

### Lane B — gluing independence
For connected graph representatives with `V=2,3,4,5` (path, cycle where available, and star where available), construct a symbolic KKL-like boundary-index contraction layer that depends on vertex outputs but contains no local group variables. Verify that independent substitutions `h_v` leave the fully contracted symbolic expression unchanged vertex-by-vertex.

The gate is invalid if the implementation achieves invariance by replacing independent `h_v` with a common diagonal `h`.

### Lane C — exact orbit dimension/counting
Use only the established real Lie-group dimension `dim_R SL(2,C)=6` and the direct-product action proved in A/B. Frozen expected product-orbit dimension at generic points:

`dim_R G^V = 6 V`, for `V=1..5`.

Also verify the diagonal subgroup dimension is only `6`, leaving `6(V-1)` relative directions if one quotient removes only diagonal `G`.

This is a group-action counting statement, not a measure theorem.

### Lane D — negative control and scope locks
Negative control: force all local left symbols to one diagonal symbol and verify that this collapses the formal independent-action count from `V` to `1`; the production result must explicitly distinguish this artificial diagonal restriction from the inherited local product action.

Required locks:
- no quotient/fixing normalization;
- no informal division by group volume;
- no FP/Haar prescription;
- no finiteness/convergence claim;
- no E7/E8 promotion;
- no G3/F9/G8/K5 promotion;
- no claim that arbitrary physical foams necessarily satisfy the scoped vertex-only inheritance assumption.

## Frozen classifications

If all lanes are exact and valid:

`ITER079J_SM_VERTEX_ONLY_KKL_GLUE_RETAINS_PRODUCT_COMMON_LEFT_REDUNDANCY_G_POWER_V_DIAGONAL_QUOTIENT_LEAVES_6V_MINUS_6_RELATIVE_DIRECTIONS_EXACT_SCOPED_E6_PARTIAL`

If A/B fail for an independently labeled local action:

`ITER079J_SM_MULTIVERTEX_PRODUCT_REDUNDANCY_FAILS_IN_FROZEN_VERTEX_ONLY_GLUE_MODEL_EXACT_SCOPED`

If implementation/provenance/scope requirements fail:

`ITER079J_SM_INVALID`

Frozen criteria may not be changed after production results are viewed.