# Iter076M terminal result — exact source variables admit the missing global orientation pseudoscalar

Date: 2026-09-13

## Authority
- proper-vertex orientation source snapshot: `83339c7ff5ef46dd28f30edcc35ffa4278d0b518`
- frozen candidate preregistration / administrative Iter076M renumber: `0ba0b8026f478ae8e4add2e2f0a9169db6a88afc`
- implementation: `e6a027fe8d2bae02e76ea82c5a39c65d58e7b9da`
- production/workflow head: `5989d115d27099e993fb8bfd4fed5f6e45cadafe`
- run: `34780608763`
- aggregate job: `103786841412`
- aggregate artifact: `10324832384`
- aggregate artifact ZIP digest: `sha256:d3cf6d0fe82bcc78088d29048993c4414f971cae9ae295b4997e07efc2ea1720`

Raw lane artifacts consumed by the aggregate job:
- A: artifact `10324642631`, digest `sha256:791430b2d270963d2a79a5e8ed8b3f1dad4c52731db2f2a38ef42e072d97ad46`
- B: artifact `10325295912`, digest `sha256:5a6b99937efee4e7a04eebbde3d1d23705ed5e9a309feb294ecce7d4dd78d73f`
- C: artifact `10325191027`, digest `sha256:514b9d9c6d0748c250f84fa88107e988ae7e7fa688ea62dd6b8287300cdf0e96`
- D: artifact `10324637782`, digest `sha256:6524ef0e9fc2acee2b9be18705538b3052340d660316875fa3126f910443ade5`

## Frozen scientific classification

`ITER076M_SOURCE_GROUP_AND_CAUSAL_DATA_DEFINE_NONDEGENERATE_GLOBAL_ORIENTATION_PSEUDOSCALAR_REVIEW_P3_SCOPED`

## Terminal facts

All four prospectively frozen lanes pass and aggregate output is `valid=true`.

The tested exact-source-variable candidate is

`Omega_sigma(g) = sgn Delta_sigma(g)`

on the non-degenerate locus, with

`Delta_sigma(g) = det([1 1 1 1 1 ; sigma_1 F_1 sigma_2 F_2 sigma_3 F_3 sigma_4 F_4 sigma_5 F_5])`,

`F_a = ghat_a T`, `T=(1,0,0,0)`.

1. **Algebraic covariance:** exact rational controls verify all `120/120` S5 relabelings, invariance under global `sigma -> -sigma`, invariance under a common proper-Lorentz transformation, and agreement of all five gauge-root/cofactor expansions. The exact control determinant is nonzero.
2. **Non-degenerate normal controls:** two independent closed timelike-normal configurations have nonzero `Delta_sigma`; all S5 relabelings obey the sign character, proper boosts preserve the selector, and a genuine parity reflection flips it.
3. **Proper-vertex compatibility:** individual four-dimensional Levi-Civita contractions are orientation-odd, while the pair-product structure associated with `beta_ab` is orientation-even. On the reconstructed controls the pair relation agrees with `beta_ab=-epsilon_a epsilon_b`. Thus the single global orientation bit carried by `Omega_sigma` is information not retained by pairwise `beta_ab` products.
4. **Degeneracy firewall:** when the weighted affine columns become dependent, `Delta_sigma=0` and `Omega_sigma` is explicitly undefined; no fit or regularization is used. Sigma weighting is operationally relevant, and raw label order is not promoted to physics.

## Interpretation lock

Iter076M upgrades the Iter076L observation from a semiclassical Regge pseudoscalar to an **available function of the exact causal-vertex integration variables**. The source variable set `(g_a,sigma_a)` therefore contains enough information, on the non-degenerate locus, to choose between the two Iter076K Hodge lifts in a gauge- and relabeling-compatible way.

This still does **not** establish physical signed P3. Availability is weaker than amplitude-selection provenance. A further prospective gate must identify the same orientation-odd factor, or an equivalent one, in the actual Eq.(4)/Eq.(7) Toller/intertwiner/contraction structure, or prove that the amplitude/saddle equations force its sign. Until that bridge is sourced and tested, `SOURCE_TO_K4_PUSHFORWARD` remains blocked as a physical map.

The nominal `epsilon^-1` source numerator/Jacobian coefficient remains `BLOCKED_OBJECT_DEFINITION`. No F9/G3/G8/K5 promotion, causal-vertex finiteness/divergence theorem, physical sector selection, complete-QG claim, or new-physics claim follows.
