# Iter076T result — exact Toller/Haar regularized wedge one-jet

**Date:** 2026-09-13

## Authority

- source snapshot: `20b9928f2c18b0c73ed5c4eae67713cf699dd74d`
- preregistration: `24cc5269abc56761efdc4248776f2911ffd5a4f4`
- symbolic-normalization repair: `0675e1c2ab529e51049c31989e85b6912390689c`
- authoritative evidence-path repair: `5fa0f7f6ad5afbafb335894d97dc7ab02fa2aacd`
- production/workflow head: `562f75cd3b74b8cf8c40d60113dc12f76af1b20b`
- authoritative run: `34782826916`
- aggregate job: `103792853336`

Authoritative artifacts:

- A: artifact `10325149879`, digest `sha256:6f5ec848249e87759e7f7ba2c2e595a85506951700179ff9ce14485904aab493`
- B: artifact `10325324748`, digest `sha256:b7fe78b0191c9a6819c2277cd1df276f0e236d864aefca65f0fda37a498e3a75`
- C: artifact `10325845536`, digest `sha256:5a5067d4a85d8dc4e6bfab8096936875a60b802439337c0334aeccf3f61241d8`
- D: artifact `10325479401`, digest `sha256:e109e05ff1d79a5e60c074c833edb34c5f384dd8a0c3119064437c6aebedbc0e`
- aggregate: artifact `10325424697`, digest `sha256:4b8e43807a9680e8319ad58480ac46d49549f1de3b58ea82bfcbcdaffa35a287`

All frozen lanes A/B/C/D and the aggregate completed successfully.

## Frozen classification

`ITER076T_EXACT_TOLLER_HAAR_REGULARIZED_WEDGE_HAS_NONZERO_ONEJET_WITNESS_FULL_VERTEX_CONTRACTED_ONEJET_STILL_REQUIRED_SCOPED`

## Lane A — exact source specialization

For the source Eq. (9) gamma-simple extremal block with

`j=k=l=1/2`, `rho=gamma/2`,

the exact reduced branches are

`t_plus(beta) = - exp(+i rho beta) / [2 (rho^2+1/4) sinh(beta)^2]`,

`t_minus(beta) = - exp(-i rho beta) / [2 (rho^2+1/4) sinh(beta)^2]`.

After removing the collision pole with the matching radial factor,

`u_+/- (beta)=sinh(beta)^2 t_+/- (beta)`,

one obtains exactly

`u_plus'(0) = - i rho/[2(rho^2+1/4)]`,

`u_minus'(0) = + i rho/[2(rho^2+1/4)]`.

Thus the regularized causal Toller wedge has a nonzero one-jet for real `rho != 0`.

The only implementation repair in the authoritative lane was to apply the frozen identity

`1-exp(-2 beta)=2 exp(-beta) sinh(beta)`

explicitly before symbolic comparison. No scientific formula or pass threshold changed.

## Lane B — independent source-backed oracle

The independent general Toller implementation `code/toller_general_eprl_reference.py` was evaluated at

- `gamma in {0.4,1.2}`;
- `beta in {0.3,0.8,1.7}`;
- both extremal causal branches.

All 12 comparisons passed the preregistered `1e-35` relative threshold.

The worst relative residual was

`6.9327686047772950741e-66`.

Derivative controls were nonzero with the predicted opposite signs:

- `gamma=0.4`, `rho=0.2`: `Im u_plus'(0)=-0.34482758620689655...`, `Im u_minus'(0)=+0.34482758620689655...`;
- `gamma=1.2`, `rho=0.6`: `Im u_plus'(0)=-0.49180327868852459...`, `Im u_minus'(0)=+0.49180327868852459...`.

## Lane C — Haar cancellation does not erase the one-jet

The normalized source radial Haar/KAK density is even,

`(sinh beta / beta)^2 = 1 + beta^2/3 + 2 beta^4/45 + ...`,

so its one-jet at `beta=0` is exactly zero.

But the raw radial `sinh(beta)^2` factor cancels the extremal Toller `1/sinh(beta)^2` collision pole and leaves the regular phase factor `exp(+- i rho beta)`. Therefore Haar evenness does not imply branch one-jet evenness and does not remove the source Toller phase one-jet for `rho != 0`.

## Lane D — full-vertex firewall

This result is deliberately local/source-wedge scoped.

It proves that there is no universal theorem forcing all source Toller/Haar one-jets to vanish identically: an exact source magnetic component provides a nonzero witness.

It does **not** establish whether the one-jet survives or cancels after:

1. the ten-wedge product;
2. magnetic-index sums;
3. the five boundary-intertwiner contractions;
4. correlated multi-wedge collision geometry;
5. the four `SL(2,C)` group integrations.

The next missing object is therefore

`FULL_TOLLER_INTERTWINER_CONTRACTED_NUMERATOR_ONEJET`.

## Consequence for the degree-two / nominal epsilon^-1 problem

Iter076Q showed that the global Hodge sign disappears in homogeneous quadratic linear transport. Iter076R/S showed that a unique symmetry-compatible nonlinear curvature channel exists and can transmit a generic one-jet into the transitive degree-two face layer. Iter076T now establishes a nonzero source-native local one-jet witness.

Therefore the source one-jet cannot be discarded by Haar evenness, Hodge-sign cancellation or S4 symmetry. The physical degree-two coefficient still requires the contracted numerator one-jet and the actual nonlinear source-to-K4 curvature.

The nominal `epsilon^-1` coefficient remains `BLOCKED_OBJECT_DEFINITION`: neither zero, nonzero nor divergent is authorized.

## Claim locks

No `NEW_PHYSICS_FOUND`; no complete-QG claim; no generic finite-spin signed P3; no physical nonlinear source-to-K4 map; no physical causal-vertex finiteness/divergence theorem; no nominal `epsilon^-1` coefficient; no G3/F9/G8/K5 promotion; retain the published spectral `i epsilon`.
