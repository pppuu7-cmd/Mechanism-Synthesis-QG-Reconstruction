# Iter076Z preregistration — scalar radial stripping leaves a non-scalar front-face coefficient

Date: 2026-09-13

## Purpose

Iter076X-Y show that the leading gamma-simple Toller singular matrix varies over the sphere of boost-normal directions and that a concrete mixed source path feeds this angular response. This gate asks the sharper object-definition question required before returning to the `epsilon^-1` degree-two problem:

> After extracting the universal radial singular power, can the remaining boundary coefficient be made direction-independent by any scalar normalization, or is a genuinely matrix/bundle-valued front-face object unavoidable?

The frozen prediction is that scalar flattening is impossible for the same `5/7` generic exact intertwiner controls because the angular response leaves the total-magnetic `M=0` sector.

## Frozen source/derived input

Use `sources/TOLLER_FRONT_FACE_NONSCALAR_SUPPLEMENT.md`, committed before implementation, plus the authoritative Iter076X and Iter076Y results.

For each wedge use the leading family

`C_n=D^j(U_n)C_zD^j(U_n)^(-1)`.

For a four-valent invariant tensor define

`F_n=iota [tensor_e C_{j_e,n}]`.

## Frozen lanes

### Lane A — provenance and object-definition locks

PASS iff the committed supplement contains:

- the radial front-face limit `beta^(2j+1)T -> C_n`;
- the boundary tensor family `F_n`;
- the angular derivative `dot F=-i F_z sum J_y`;
- the exact total-magnetic-sector obstruction to scalar flattening;
- the frozen `5/7` generic obstruction prediction;
- the explicit consequence that a scalar ordinary Taylor numerator is not source-faithful generically;
- the firewall that the full ten-wedge blow-up calculus and physical `epsilon^-1` coefficient remain unconstructed.

The authoritative Iter076X and Iter076Y result files must contain their PASS classifications.

### Lane B — exact front-face family and stabilizer control

For exact spins `j in {1/2,1,3/2,2}`, construct primitive `C_z`, standard `J_z,J_+,J_-`, and an exact nontrivial rotation control `U` not commuting with `J_z`.

PASS iff:

- `C_z` is invertible;
- `C_z` commutes with every diagonal `J_z` stabilizer control;
- for every frozen spin, a transverse rotation produces `U C_z U^-1 != C_z`;
- `C -> -C` changes only the common leading scale and leaves the projective/directional nonconstancy unchanged;
- for `j>=1`, the transverse first derivative `[J_y,C_z]` is nonzero and not proportional to `C_z`.

The `j=1/2` case may have special low-dimensional identities but must still have nonconstant single-edge `C_n` under a transverse rotation.

### Lane C — exact scalar-flattening obstruction census

Use the same seven exact 4-valent intertwiner controls as Iter076V-W-X-Y. Form `F_z=(tensor C_z)iota`.

PASS iff:

- `F_z` has support only at total magnetic number `M=0` for all `7/7` controls;
- total `J_+ F_z` and `J_- F_z` both vanish for exactly the two `(1/2)^4` controls;
- both are nonzero for exactly the remaining `5/7` controls;
- every nonzero `J_+ F_z` component has total `M=+1`;
- every nonzero `J_- F_z` component has total `M=-1`;
- therefore no scalar derivative term `lambda F_z`, which remains in `M=0`, can cancel the transverse angular derivative in those `5/7` cases.

The implementation must explicitly test the linear independence of the `M=0`, `M=+1`, and `M=-1` supports rather than infer it from prose.

### Lane D — scalar-normalization no-go and scope firewall

For every Lane C control, test a symbolic scalar normalization derivative `lambda F_z` against the transverse derivative space.

PASS iff:

- no value of symbolic `lambda` can make `lambda F_z + J_y F_z` vanish in each of the `5/7` surviving controls;
- the two all-spin-half controls remain special zeros and are not promoted to genericity;
- the aggregate records:
  - `scalar_front_face_flattening_generic=false`;
  - `matrix_or_bundle_valued_front_face_required=true`;
  - `ordinary_scalar_source_numerator_jet_source_faithful=false` for the frozen generic controls;
  - `smooth_Haar_factor_remains_separate=true`;
  - `full_ten_wedge_blowup_constructed=false`;
  - `physical_source_to_K4_pushforward_established=false`;
  - `epsilon_minus1_coefficient_established=false`;
  - no generic finite-spin signed P3 or G3/F9/G8/K5 promotion.

## PASS classification

`ITER076Z_SCALAR_RADIAL_STRIP_LEAVES_NONSCALAR_DIRECTION_DEPENDENT_TOLLER_FRONT_FACE_BUNDLE_OBJECT_REQUIRED_EXACT_SCOPED`

## Scientific meaning on PASS

The generic source branch cannot be represented, after only scalar radial stripping, by an ordinary scalar Taylor numerator at the identity. The front-face leading coefficient is intrinsically matrix/bundle-valued over boost-normal directions, and its angular variation survives exact boundary-intertwiner contraction in the frozen generic controls.

This changes the correct formulation of the source-side degree-two problem: before any physical source-to-K4 pushforward or `epsilon^-1` coefficient is formed, one must define the correlated blown-up/polyhomogeneous boundary object and its connection data.

## Next admissible gate

Construct the minimal algebraic front-face data model needed for the full source relative-coordinate complex: radial weights, normal directions, leading `C_n` matrices, and first angular connection on each wedge, with exact covariance under source-node relabeling and compact gauge action. Determine whether this data closes under the K5 incidence constraints before attempting any K4 Hodge/Sym2 transport.

## FAIL classification

`ITER076Z_TOLLER_FRONT_FACE_NONSCALAR_OBSTRUCTION_CONFIRMATION_FAIL`

A failure is an exact source-object-definition result, not a physical finiteness/divergence theorem.

## Claim locks

No `NEW_PHYSICS_FOUND`; no complete-QG claim; no full ten-wedge blow-up; no physical source-to-K4 map; no nominal `epsilon^-1` coefficient; no physical causal-vertex finiteness/divergence theorem; no generic finite-spin signed P3; no G3/F9/G8/K5 promotion; retain the source spectral `i epsilon` prescription.