# Iter076E — Source-relative tangent complex vs K4 cycle space

Date: 2026-09-13

## Frozen gate

Preregistration: `6fccf148acaab9b21a4b46f28efd801d9b716e34`
Production head: `9fb0e6c7ae7351ee38a67eba8f07f1d75f15f6cf`
Authoritative run: `34767157817`

The gate was frozen before implementation to test only the exact linearized source relative-coordinate complex induced by pairwise relative arguments and its relation to the already validated reduced K4 cycle-flow object. It was not allowed to define a physical source-to-K4 pushforward or any epsilon coefficient.

## Raw lanes consumed

- Lane A job `103750063457`, artifact `10320967744`, digest `sha256:10cf83b5b610a38db1802798c6f8eaade8033b66c58db6a8a2df4c2c8a970a81`: all five K5 roots give incidence rank 4, cut dimension 4 and cycle nullity 6 exactly.
- Lane B job `103750063428`, artifact `10320572366`, digest `sha256:cfc293a72d42feac750c24e1fcca75ee56223fedc4855bfab40e2299e0c82d94`: for all four K4 roots, cut dimension 3, cycle dimension 3, cut∩cycle dimension 0, and the cycle constraint is exact.
- Lane C job `103750063491`, artifact `10321007719`, digest `sha256:45e26540f6b94174f44eb8c469760131fbfdc32745819171077057644b1c7d23`: exact rank/subspace mismatch predicate passes; source relative tangents are cut-space data while the reduced K4 constrained-flow object is cycle-space data.
- Lane D job `103750063312`, artifact `10320297713`, digest `sha256:75eb29a435e8a053b30c0ad3e79c46674bf827c1e891b9ae58d0902f7689a343`: K5 invariance across 120 permutations and K4 invariance across 24 permutations pass; deliberately wrong free-edge and cut-as-cycle controls are rejected.

Aggregate job `103750110924`, artifact `10320284136`, digest `sha256:aaf2db22769c52dc25c57e21fb90697c1f22900e52d6abefab31edb9e4848ae4` consumed all four lanes and returned `valid=true`, `scope_guard_ok=true`.

## Scientific classification

`ITER076E_SOURCE_RELATIVE_TANGENT_IS_CUT_SPACE_K4_CYCLE_IDENTIFICATION_REQUIRES_EXTRA_MAP_SCOPED`

This is a scoped exact structural result. The natural linearized carrier of pairwise source relative coordinates is an incidence/cut-space object. The validated reduced K4 collision variables are cycle-space constrained flows. Equal dimensions at K4 do not identify these subspaces: their exact intersection is zero in the frozen Euclidean edge pairing.

Therefore an additional projection, dualization, orientation-dependent map, submanifold prescription, or other source-derived structure is mathematically required before source relative-coordinate data can be interpreted as the reduced K4 cycle variables.

## Claim locks

This result does **not** define the missing map physically; it does not define the source-induced numerator×Haar/Jacobian quadratic density; it does not determine any transitive-face coefficient; it does not determine the nominal `epsilon^-1` coefficient; and it does not establish causal-vertex finiteness/divergence, G3, F9, G8 or K5.

## Next admissible step

Prospectively audit the symmetry representation content of the K4 cut and cycle spaces. In particular, determine whether an untwisted S4-equivariant linear isomorphism exists and whether an orientation/sign-twisted intertwiner is required. This is a structural prerequisite only; even a unique algebraic intertwiner would still require source provenance before being promoted to the physical P3 pushforward.
