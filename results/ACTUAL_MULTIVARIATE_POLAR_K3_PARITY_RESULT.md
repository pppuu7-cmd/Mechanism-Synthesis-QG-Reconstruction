# Actual source-ordered multivariate polar gate — exact K3 parity result

Date: 2026-09-15

Status: **PASS_EXACT_SCOPED**

Classification:

`K3_PHYSICAL_ORIGIN_POLAR_COEFFICIENT_ZERO_EXACT_BY_NORMAL_INVERSION_PARITY`

## Prospective provenance

Parent polar/annihilator gate preregistration:

`prereg/ACTUAL_SOURCE_ORDERED_MULTIVARIATE_POLAR_NORMAL_JET_ANNIHILATOR.md`, commit `4c4478db20e08387fb7067a55d773fce31d3fc34`.

K3 parity derivation:

`sources/ACTUAL_MULTIVARIATE_POLAR_K3_PARITY_DERIVATION.md`, commit `78e63844a8fe0a70af9ac8dc574d358e7ecab927`.

Initial validator/workflow:

- validator commit `c8ddedab0530cb08b17aea08299c1e45a1897d30`;
- workflow/head `7f15c4f4188990f2bd7b0c08329fb46345da43cd`.

The initial run `34955091523` executed all scientific checks successfully but classified `INVALID_IMPLEMENTATION` solely because one bridge provenance lock required a wording variant absent from the repaired bridge result. All K3 scientific predicates and all ten malformed controls were already true.

The repair was prospectively frozen before code modification:

`prereg/ACTUAL_MULTIVARIATE_POLAR_K3_PARITY_CONTROL_ONLY_REPAIR_1.md`, commit `6a048a91eb668787d1227331025888d86f8fb3ed`.

Only the provenance phrase was repaired:

- repaired validator/head `4d45991d381930d84da2d5bf33c02d7d7050aa74`.

## Authoritative production

- run `34955160116`, terminal success;
- job `104335856061`, terminal success;
- head `4d45991d381930d84da2d5bf33c02d7d7050aa74`;
- artifact `10390188871`, `actual-multivariate-polar-k3-parity-gate`;
- artifact ZIP digest `sha256:e519d0b2c01327532ba5ad4024cd4791efe390b447f1ad5f705ca0af31794b83`;
- production JSON SHA256 `537c477b1bf2207a2935814dca6cffa532a0581dc539247653b4fe47176cddf9`.

The exact Iter077I full-32 contraction engine was executed in production and returned 32 components with checksum

`2fd44a481c5ca7a87744727678f211b17be048c173a9cf79fe10ff3a7b1decfd`.

## Exact K3 geometry

There are exactly 10 K3 blocks in K5. Fix one block `B={a,b,c}`. Its source-normal fiber has real dimension 6 after barycentric removal of the common mode.

Exactly three of the ten K5 wedges are internal to B, and the remaining seven are smooth with respect to the K3 normal variable at the interior of the K3 face.

For the authoritative frozen `j=1/2` leading source matrix,

`M(v)=[[v_z,-v_x-i v_y],[-v_x+i v_y,-v_z]]`,

so exactly

`M(-v)=-M(v)`.

Production verifies this exact map on a spanning set of integer vectors in addition to locking the analytic formula.

Under simultaneous inversion of the six-dimensional K3 normal variable, all three internal relative vectors reverse. Hence the product of the three singular leading K3 wedge matrices acquires

`(-1)^3=-1`.

It is odd on the K3 front sphere.

## Why the complete residue integrand is odd

The K3 candidate pole through the physical regulator origin has source normal Taylor order

`omega_K3=0`.

Therefore only the zeroth coefficient in the K3 radial variable enters the candidate residue.

At `rho_K3=0`:

- the seven non-internal K5 wedges depend only on the collapsed K3 point and tangential/outer variables, not on the K3 front direction;
- the leading pulled-back Haar/front-face angular density is even under inversion;
- the source-derived K3 radius is even;
- finite matrix multiplication and the complete 32-component boundary contraction preserve the odd sign of the product of the three internal leading matrices.

Thus every boundary component of the full residue integrand is odd on the inversion-symmetric K3 front sphere.

## K2 angular subfaces are integrable

A K2 subcollision inside the K3 front sphere has three relative boost dimensions. One frozen wedge contributes `beta^-2` while the local relative radial measure contributes `beta^2 d beta`.

The resulting radial exponent is exactly `0`, verified in production. Therefore K2 angular singularities are locally integrable and do not obstruct the inversion cancellation by a nonintegrable boundary term.

## Exact scientific conclusion

The K3 front-face angular pairing at the physical regulator origin is identically zero:

`Res_(L_K3=0) U = 0`

for every one of the 10 K3 blocks and for all 32 boundary components/tangential values in the frozen local all-`j=1/2` source object.

Hence the actual K3 polar coefficient is not merely below its formal order-zero ceiling: it is exactly absent.

Its annihilator is therefore the whole test-function space, strictly stronger than the formal `I_K3^1` annihilator ceiling.

## Nested-corner consequence

There are exactly 20 maximal K3-K4-K5 chains. At such a corner the K3 residue can be extracted while keeping the outer K4/K5 variables and regulator parameters symbolic.

The same odd K3 front-direction argument holds pointwise in those remaining variables. Thus the coefficient of `1/L_K3` is the zero meromorphic family before any outer residue extraction.

Consequently every multiresidue containing a K3 factor vanishes, including the candidate maximal-chain product pole coefficient

`coeff[1/(L_K3 L_K4 L_K5)] = 0`.

## Scheme status

This zero is **scheme invariant** under the allowed defining-function holomorphic gauge action

`U -> exp[(1/2)sum_B lambda_B phi_B] U`.

A holomorphic multiplier cannot create an `L_K3^-1` coefficient when that residue is already identically zero as a meromorphic family in the remaining variables.

## Mechanical controls

Production rejects all ten malformed variants:

1. even internal-edge count;
2. representative boundary component only;
3. nonintegrable K2 front subcollision;
4. non-inversion-symmetric angular domain;
5. direction-dependent external zeroth coefficient;
6. odd front-face measure;
7. non-even source radius;
8. wrong K3 candidate normal order;
9. overclaim that K4/K5 also vanish;
10. non-holomorphic defining-function change promoted as allowed scheme covariance.

All 13 scientific predicates and all ten controls passed.

## What this does not prove

No K4 or K5 residue conclusion follows. In particular the K4 physical pole is associated with Taylor order 3 and can receive contributions from subleading internal Toller coefficients, smooth external wedge Taylor coefficients, Haar/BCH corrections and nonlinear source geometry.

No physical finite part, selector, regulator independence, unique extension, global patching, generic-spin theorem or downstream quantum-gravity claim follows.

## Next step

After independent Critic review of the K3 result, continue the parent gate with K4. The first K4 target should separate its principal normal-order-3 symbol from lower-order residue pieces rather than assuming the whole K4 residue shares the leading-product parity.