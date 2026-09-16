# K5 S5-equivariant degree-three face-tangent logarithmic IBP/syzygy — repaired terminal result

Date: 2026-09-16

## Authority chain

Parent scientific preregistration: `prereg/K5_ORDER8_S5_DEG3_FACE_TANGENT_LOG_IBP_SYZYGY.md`, commit `b93145159d9535992208a15a56c33b13732ad155`.

Outcome-independent implementation audit: `results/K5_ORDER8_S5_DEG3_IMPLEMENTATION_AUDIT.md`, commit `cf618ae9a3bbe8a4b97171dce973c2a4cb1b803f`, verdict `INVALID_IMPLEMENTATION` for the first implementation because three mandatory frozen controls were not actually executed.

Prospective control-only repair: `prereg/K5_ORDER8_S5_DEG3_CONTROL_ONLY_REPAIR.md`, commit `27ffc236cf2f7e3b555811f2a1b2aa1684a61ddf`.

Repaired implementation: `scripts/k5_order8_s5_deg3_log_ibp_syzygy_repair.py`, commit `48ad8b9c8624866ae4089513594dc71b2d1ab258`.

Repaired workflow/head: `.github/workflows/k5_order8_s5_deg3_log_ibp_syzygy_repair.yml`, head `dbaedce551ce4554e900189970e70e066df09e0a`.

## Production

- run `35043530093`, terminal `success`;
- job `104628346999`, terminal `success`;
- artifact `10425543584`;
- artifact ZIP digest `sha256:3479e8458649ef0438b83bcf1ce7c70a42d0e024e0d71c53299ded6c1622a19f`;
- production JSON SHA256 `b4c1ea8b4aefbef905b1354b70786b7c644181d261140830291d0ff8f0f3797e`;
- status `PASS_EXACT_SCOPED`;
- classification `K5_S5_FACE_TANGENT_LOG_IBP_DEG3_RADIAL_ONLY_EXACT_SCOPED`.

All repaired exact checks and all six executed controls passed.

## Exact result

The complete fixed-edge stabilizer has 11 orbits on the 55 homogeneous quadratic edge monomials, with sizes

`(3,3,12,6,6,6,3,6,3,6,1)`.

The complete S5-invariant homogeneous quadratic quotient space has dimension three, with global orbit sizes

`(10,30,15)`.

The exact K5 coefficient system therefore has

- rows: `2565`;
- columns: `14`;
- exact rank: `11`;
- exact nullity: `3`.

The full invariant-quadratic Euler subspace `F_2(alpha) E` has exact dimension `3` and is contained in the nullspace. Therefore

`nonradial_quotient_dimension = 3 - 3 = 0`.

Hence

`K5_S5_FACE_TANGENT_LOG_IBP_DEG3_RADIAL_ONLY_EXACT_SCOPED`.

No genuinely non-radial S5-equivariant regular face-tangent logarithmic derivation exists at component degree three for the exact K5 Kirchhoff polynomial.

## Repaired adversarial controls

The repair actually executes the controls that were missing from the first implementation:

- an explicit non-face-tangent malformed field is rejected;
- an explicit face-tangent but S5-breaking field is rejected;
- an explicit fake logarithmic coefficient vector is rejected by the full coefficient matrix;
- the synthetic fixture `Psi_syn=prod_e alpha_e` is sent through the same generic orbit/matrix/nullspace engine;
- on that fixture the same engine finds rank `3`, nullity `11`, radial dimension `3`, and non-radial quotient dimension `8`;
- the known synthetic non-radial direction `v_e=alpha_e^3`, `H_2=sum_e alpha_e^2` satisfies the exact identity and is verified outside the radial span.

This excludes a hard-coded radial-only classifier.

## Consequence

Together with the terminal component-degree-two theorem, the complete S5-equivariant same-denominator regular face-tangent logarithmic sector is radial-only through component degree three.

This does not evaluate either invariant-dual K5 projective period. It also does not exclude non-equivariant modules, denominator-shifting identities, singular fields, or higher component degree.

Independent exploratory exact algebra performed only after the degree-three repair preregistration identifies component degree four as the first S5-equivariant degree with a non-radial quotient: the complete degree-four system has an eight-dimensional logarithmic nullspace, seven-dimensional invariant-cubic Euler subspace, and a one-dimensional quotient. A representative of that quotient has zero logarithmic quotient, i.e. is a candidate genuine Kirchhoff annihilator `v(Psi_K5)=0`. This exploratory fact is not promoted by the present result and requires its own prospective gate.

## Interpretation ceiling

No K5 integrated-period zero/nonzero theorem, no full 217-dimensional tensor/annihilator theorem, no physical finite-part selector, no regulator-independence theorem, no G3/F9/G8 promotion, no `NEW_PHYSICS_FOUND`, and no complete-QG claim follows.
