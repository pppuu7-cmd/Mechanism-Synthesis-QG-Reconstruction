# Iter079J-SM — multivertex E6 product-orbit result

## Authoritative provenance

- Prospective preregistration: `6645d44efe9319401f8c0c77e361c0a105573add`
- Implementation: `4a31a5c7ddb7627d876377e098c3ccdde221ad1c`
- Workflow/production head: `f1696f0aa2aea3bd4c0264b44006e92d3033736d`
- Run: `34811432966`
- Raw artifacts: A `10334064547`, B `10335076992`, C `10335126360`, D `10335017304`
- Aggregate artifact: `10334368430`
- Aggregate digest: `sha256:afe3c383f40c70821d8ca03665afb5b1b3ae1ac78fc7753fc4bf2a1f9b65215b`

## Frozen classification

`ITER079J_SM_VERTEX_ONLY_KKL_GLUE_RETAINS_PRODUCT_COMMON_LEFT_REDUNDANCY_G_POWER_V_DIAGONAL_QUOTIENT_LEAVES_6V_MINUS_6_RELATIVE_DIRECTIONS_EXACT_SCOPED_E6_PARTIAL`

All four frozen lanes and aggregate are valid.

## Exact findings

### A — local exact invariance
50/50 free-word checks pass for independently labeled local left actions `h_v`:

`(h_v g_{v,b})^{-1}(h_v g_{v,a}) = g_{v,b}^{-1} g_{v,a}`.

The implementation retains five distinct `h_v` labels; it does not manufacture invariance by replacing them with one common diagonal action.

### B — scoped gluing independence
For path/cycle/star representatives with `V=2..5`, every frozen symbolic KKL-like boundary-index contraction remains invariant under the independent local actions. The contraction layer contains no local group variables and therefore does not identify the `h_v` in this vertex-only inheritance class.

### C — orbit dimension
Using only `dim_R SL(2,C)=6`, the inherited product orbit has

`dim_R G^V = 6V`.

A quotient by only the diagonal subgroup removes six real dimensions and leaves

`6(V-1)`

relative directions. Frozen rows:

- `V=1`: `6 -> 0` relative after diagonal quotient;
- `V=2`: `12 -> 6`;
- `V=3`: `18 -> 12`;
- `V=4`: `24 -> 18`;
- `V=5`: `30 -> 24`.

### D — negative control
Forcing all independent local left symbols to one diagonal symbol collapses the formal action-factor count from `V` to `1`, losing exactly `V-1` independent factors. This is an artificial restriction and is not the inherited local product action tested in A/B.

## Scope ceiling

This is an exact **conditional E6 orbit-counting statement** for the frozen vertex-only KKL-gluing class. It is not:

- an arbitrary-foam theorem beyond that inheritance hypothesis;
- a quotient/fixing measure or normalization theorem;
- permission to divide by a group volume;
- an FP/Haar prescription;
- a finiteness/convergence theorem;
- an E7/E8 or downstream promotion.

## Consequence

The previous minimal two-vertex Iter079H orbit count is not an isolated two-vertex accident inside the frozen vertex-only inheritance class: the independent local redundancy persists as `G^V` on all tested connected representatives through `V=5`. The physical E6 blocker is therefore sharpened further: **orbit counting is structurally controlled in this class, while the source-defined quotient/fixing measure and normalization remain missing (Iter079I).**