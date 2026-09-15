# Iter083M-SM derivation — source-normal geometric radial basis

Date: 2026-09-15
Status: PRE-PRODUCTION DERIVATION AFTER PREREGISTRATION

Preregistration: `prereg/ITER083M_SM_SOURCE_NORMAL_GEOMETRIC_RADIAL_BASIS.md`, commit `c801299beb44816941fd441715e3eb03c73740c7`.

## 1. Source-normal tangent variables
In the frozen source-ordered collision chart, write

`g_a(r)=exp[r (x_a . sigma)/2]`, `x_a in R^3`.

For every wedge `(a,b)`, authoritative Iter077I gives

`beta_ab(r)=r |x_a-x_b|+O(r^2)`.

Thus the source rapidity fixes the tangent Euclidean norm on relative boost directions. The common-left compact collision removes the common translation of all label vectors.

## 2. Block normal quotient and barycentric projector
For a block B of p labels, let

`xbar_B=(1/p) sum_(a in B) x_a`.

The translation-free label space is

`Std_p={u in R^p : sum u_a=0}`.

The exact projector is

`P_B=I-(1/p)J`.

Iter082D already verifies this projector for every K3/K4/K5 block and its exact S5 transport.

Define the block tangent radial quadratic form

`R_B^2 = sum_(a in B) |x_a-xbar_B|^2`.

In matrix form on each boost component,

`R_B^2=x^T P_B x`.

## 3. Uniqueness of the invariant label metric
A symmetric p-by-p matrix invariant under all S_p permutations has one diagonal value and one off-diagonal value, hence

`G=a I+b(J-I)=(a-b)I+bJ`.

On `Std_p`, J acts as zero. Therefore

`G|_Std_p=(a-b) I`.

So the S_p-invariant symmetric form on the translation-free label quotient is unique up to one scalar for p=3,4,5.

The boost-vector representation has the unique SO(3)-invariant symmetric form `delta_ij` up to scale. Hence on

`R^3 tensor Std_p`

the product source symmetry supplies a unique invariant quadratic form up to scale. For p=5 this is the same representation written in Iter083B as

`spin1_SO(3) tensor Std5_S5`.

## 4. Pairwise relative-boost identity
The complete graph K_p has Laplacian

`L_Kp=p I-J=p P_p`.

Therefore, componentwise and then summed over the three boost components,

`sum_(a<b in B) |x_a-x_b|^2 = p sum_(a in B) |x_a-xbar_B|^2 = p R_B^2`.

Combining with the source small-boost law,

`sum_(a<b in B) beta_ab(r)^2 = p r^2 R_B^2 + O(r^3)`.

Thus the normalization of the local radial quadratic form can be tied directly to the source rapidity convention at tangent order. No ten-edge regulator-space metric Q is involved.

## 5. Nested variance / orthogonal increment identity
Let B have p labels and add one label v. Set `B'=B union {v}`. Then

`R_B'^2 = R_B^2 + p/(p+1) |x_v-xbar_B|^2`.

Proof: the label-space projector difference

`D=P_B'-P_B`

is the rank-one orthogonal projector onto the contrast vector

`w=(-1/p,...,-1/p,1)`

supported on B'. Since

`|w|^2=(p+1)/p`,

`D=w w^T/|w|^2`, and therefore

`x^T D x = p/(p+1) (x_v-xbar_B)^2`.

For a maximal K3 subset K4 subset K5 chain the exact label-space projectors

`A=P_3`, `B=P_4-P_3`, `C=P_5-P_4`

are pairwise orthogonal with ranks `(2,1,1)`. Tensoring with R^3 gives physical normal ranks

`(6,3,3)`

and total 12.

The coefficients are exactly

`3/4` for K3 -> K4,

`4/5` for K4 -> K5.

## 6. Meaning for analytic regularization
The result supplies a label-free, S5-covariant, source-normal local quadratic geometry for every divergent block and every nested chain. It suggests a different candidate regularization class based on complex powers of actual normal radii (or squared radii), rather than complex parameters attached independently to the ten wedges and a separately chosen regulator metric Q.

This does not yet define a renormalized extension. Even after a radial defining function is fixed, meromorphic finite parts can depend on:

- how the local radial function is continued beyond tangent order;
- subtraction/finite-part convention;
- multiplicative rescaling of a defining function when residues are nonzero;
- forest ordering/partition-of-unity data;
- nonlinear chart transition and global patching.

These must be tested prospectively in a successor.

## 7. Scope ceiling
No exact nonlinear identity `beta_ab=distance(x_a,x_b)` is claimed beyond tangent order. No physical finite part, unique extension, regulator independence, generic-spin theorem, all-strata global renormalization, G3/F9/G8/K5 promotion, NEW_PHYSICS_FOUND or complete-QG claim follows.