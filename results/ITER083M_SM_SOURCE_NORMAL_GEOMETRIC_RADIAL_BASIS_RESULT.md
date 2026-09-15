# Iter083M-SM — source boost geometry gives a unique local forest radial quadratic basis

Date: 2026-09-15
Status: **PASS_EXACT_SCOPED**

## Provenance
- preregistration `c801299beb44816941fd441715e3eb03c73740c7`;
- theorem derivation `f566a9aad2d7adfbee16557de9a7fb9f8bdfa777`;
- validator initial `74db7bbf6c9b364e8e4e26a17d428260c3e671e9`, pre-production provenance-lock repair `3c681c85a52b0c1b7d32ec5b933f6cc7a56ad898`;
- workflow/head `6916f3fb2f89f7f009bf9d3354b9dfe8c001de74`;
- run `34917280262`, job `104217547168`, terminal success;
- artifact `10376298881`, ZIP digest `sha256:7659e611caa70da2803583ad0ee0f4ee29e7a3a9924058ee180d4c9a7a21566e`;
- production JSON SHA256 `5b11c3060b7809921d35323fec089f280c07614728e6282b7ea549301753b7a3`.

## Classification
`ITER083M_SM_SOURCE_BOOST_GEOMETRY_GIVES_UNIQUE_LOCAL_FOREST_RADIAL_QUADRATIC_BASIS_SCOPED`

Verdict: **PASS_EXACT_SCOPED**.

## Unique invariant normal metric
For a block B of size p, the label quotient normal space is the standard representation

`Std_p={u in R^p : sum u_i=0}`.

A symmetric matrix invariant under all S_p permutations has one diagonal and one off-diagonal value, hence a two-dimensional space on R^p. On Std_p the J component vanishes, so the invariant symmetric form is unique up to scale.

Production verifies this exactly for p=3,4,5:

- full invariant symmetric-form dimension 2;
- restriction dimension on Std_p exactly 1.

A 24-element exact rotation subgroup already forces the symmetric form on the three boost-vector components to be proportional to the Euclidean form. Hence on

`R^3 tensor Std_p`

the source compact/permutation symmetry gives one invariant quadratic sector for each K3, K4 and K5 normal fiber.

For K5 this is the same representation written authoritatively in Iter083B as

`spin1_SO(3) tensor Std5_S5`.

## Source-normal radial form
Define

`R_B^2=sum_(a in B)|x_a-xbar_B|^2`.

The complete graph identity is exact:

`L_Kp=p P_p`.

Therefore

`R_B^2=(1/p) sum_(a<b in B)|x_a-x_b|^2`.

Iter077I gives source small-boost rapidities

`beta_ab(r)=r|x_a-x_b|+O(r^2)`.

Thus

`sum_(a<b in B) beta_ab(r)^2 = p r^2 R_B^2 + O(r^3)`.

The local radial quadratic normalization is therefore tied directly to the source boost convention at tangent order; no ten-edge regulator-space metric Q is needed.

## Exact nested variance geometry
For B of size p and a new label v,

`R_(B union {v})^2 = R_B^2 + p/(p+1)|x_v-xbar_B|^2`.

Production verifies every p=3->4 and p=4->5 inclusion in K5: 25 exact nested-addition checks.

The coefficients are

- K3 -> K4: `3/4`;
- K4 -> K5: `4/5`.

For every maximal K3 subset K4 subset K5 chain, the label projectors

`P3`, `P4-P3`, `P5-P4`

are pairwise orthogonal projectors with ranks `(2,1,1)`. Tensoring with the physical boost-vector components gives normal ranks

`(6,3,3)`

and total 12.

All 20 maximal chains pass.

## Exact covariance
Production verifies:

- 1920/1920 block-projector S5 covariance checks;
- 7200/7200 chain-increment S5 covariance checks.

No preferred root/base label is present.

## Research consequence
The local collision geometry already supplies a canonical, label-free, S5-covariant **normal radial quadratic basis**. A future analytic regularization can therefore be formulated directly in the actual normal radii instead of introducing an independent metric on ten edge-regulator parameters.

This does not yet select a finite part. Meromorphic finite parts may still depend on nonlinear continuation of the defining function, subtraction convention, multiplicative radial rescalings when residues are nonzero, forest/partition data and global patching.

The next nonredundant gate is to regularize the authoritative critical K3/K4/K5 radial powers with these canonical local radii and compute exactly the residual rescaling/finite-part freedom.

## Interpretation ceiling
No exact nonlinear rapidity-distance identity beyond tangent order; no finite-part selector; no source-authorized global analytic continuation; no all-strata global renormalization; no regulator independence; no generic-spin theorem; no G3/F9/G8/K5 promotion; no `NEW_PHYSICS_FOUND`; no complete-QG claim.