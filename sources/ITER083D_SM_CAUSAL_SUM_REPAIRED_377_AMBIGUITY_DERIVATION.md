# Iter083D-SM source/theorem derivation — repaired causal-sum persistence of the exact 377-dimensional K5 ambiguity

Date: 2026-09-15

Prospective contract: `prereg/ITER083D_SM_CAUSAL_SUM_REPAIRED_377_AMBIGUITY.md`, commit `7656ae687ce16ad05bacfc34349c8206b583237e`.

## 1. Historical repair target

Historical Iter081I correctly observed that a finite causal orientation sum is an off-collision linear combination and does not, merely by being finite, define values of distributions supported exactly on the common-collision locus. However its quantitative conclusion was wrong: it used the Iter077Q family

`Q(y)^n F(y) delta_N`, `n=0,1,...`,

to claim an infinite-dimensional tangential ambiguity.

The corrected right-SU2 source lock later showed that the exact node-wise compact action is transitive on

`N ~= SU(2)^5/SU(2)_diag`,

so arbitrary nonconstant tangential scalar functions such as that `Q^n` family are not invariant source data. Iter083B replaces the invalid infinite family by the exact finite source-symmetry-compatible filtered ambiguity space

`F_8`, `dim_C F_8=377`.

This iteration therefore supersedes only the historical **infinite-dimensional** classification. It re-tests the qualitative causal-sum nonuniqueness against the corrected exact space.

## 2. Source-defined causal sums

### Bianchi--Chen--Gamonal convention

The primary causal-vertex paper defines fixed-causal-structure amplitudes

`A_v^(sigma_a sigma_b)`

with five node orientations `sigma_a=+-1` and wedge signs

`kappa_ab=sigma_a sigma_b`.

It explicitly writes the comparison

`sum_(sigma_a=+-1) A_v^(sigma_a sigma_b) != A_v^EPRL`.

Thus this source-level causal-structure sum has 32 node-sign labels and unit coefficient for each label.

Global reversal

`sigma_a -> -sigma_a`

leaves every `kappa_ab` unchanged. Therefore the 32 labels represent 16 distinct wedge-sign patterns, each exactly twice.

### Beltran eta=+1 convention

Authoritative Iter081H freezes Beltran v2 Eq. (36) as

`A_gamma_v^+ = sum_([epsilon_ab], eta=+1) A_v^(epsilon_ab)`

with unit coefficient over the 16 inequivalent factorized K5 patterns

`epsilon_ab=sigma_a sigma_b`

modulo global reversal.

Thus on any family that depends only on the wedge signs,

`S_BCG = 2 S_Beltran`.

No fitted or alternating weights occur in either frozen object.

## 3. Causal value of the Iter083C top mode

Iter083C defines for every supported ambiguity vector `a`

`Delta_kappa = chi_top(kappa) a`,

where

`chi_top(kappa)=product_(a<b) kappa_ab`.

For a causal K5 pattern,

`kappa_ab=sigma_a sigma_b`,

so

`chi_top`

`= product_(a<b) sigma_a sigma_b`

`= product_a sigma_a^(deg_K5(a))`

`= product_a sigma_a^4`

`= +1`.

Therefore the sectorwise deformation is exactly

`Delta_kappa=a`

on every causal wedge pattern.

This statement is already authoritative from Iter083C production and does not use the historical Iter077Q tangential family.

## 4. Exact action of the two causal sums

For the 16-pattern Beltran sum,

`S_Beltran(Delta)`

`= sum_(kappa in C16) a`

`= 16 a`.

For the 32-label Bianchi--Chen--Gamonal sum,

`S_BCG(Delta)`

`= sum_(sigma in {+-1}^5) a`

`= 32 a`.

Over the complex numbers, multiplication by 16 and by 32 is injective. Hence the full map

`F_8 -> summed supported ambiguity`

is injective in either convention.

Using Iter083B,

`dim_C F_8=377`,

so both source-defined unit-weight causal sums retain at least 377 linearly independent supported ambiguity directions.

## 5. Why the Beltran summed space has no additional directions in the frozen class

A lower bound is not enough for the preregistered exact claim.

Iter081H independently establishes that the Beltran unit-weight sum has a nonzero `r^-20` leading term in every one of the 32 frozen boundary components on the common-collision patch:

`I_alpha^+ = 16 C_alpha r^-20 + O(r^-19)`, `C_alpha != 0`.

Therefore its exact transverse scaling degree remains

`sd_N=20`.

The sum does not change the common-collision geometry

`N subset M`, `codim_R N=12`,

the 32-dimensional boundary-dual coefficient fiber, the compact node-gauge action, the source Haar/tubular density, or S5 covariance.

Iter083B is a theorem about exactly this source-symmetry-compatible same-scaling-degree extension-difference class, not about a particular unsummed branch. Therefore any two admissible extensions of the already-summed Beltran off-collision distribution differ by an element of the same intrinsic space `F_8`.

This gives

`dim ambiguity(S_Beltran) <=377`.

The injective top-mode construction gives the opposite inequality

`dim ambiguity(S_Beltran) >=377`.

Hence

`dim_C ambiguity(S_Beltran)=377`.

## 6. Bianchi--Chen--Gamonal 32-label sum

The BCG source sum uses the same 16 factorized wedge patterns, each counted twice. Therefore off collision,

`S_BCG = 2 S_Beltran`

for the same fixed-causal-structure Toller amplitudes. Since the Beltran sum has nonzero `r^-20` leading coefficient, multiplication by two preserves its scaling degree and all source symmetries.

Thus the same Iter083B upper-bound theorem applies, while the top-mode injection is `a ->32a`.

Consequently

`dim_C ambiguity(S_BCG)=377`

in the same frozen class.

The distinction between factors 16 and 32 is normalization/counting convention only; it does not change the surviving dimension because both factors are nonzero.

## 7. Compatibility with all Toller additive identities

Iter083C proves more than causal-sum survival. The same sectorwise family

`Delta_kappa=chi_top(kappa)a`

is annihilated by **every nonempty partial sign sum** generated by

`T+ + T- = D`.

Thus the 377-dimensional causal-sum ambiguity cannot be removed indirectly by also demanding consistency with the full EPRL sign sum or any mixed product containing arbitrary subsets of `D` factors.

Causal summation and Toller additivity together still leave the entire frozen `F_8` coefficient space free.

## 8. Weighted-sum scope

For a different weighted causal object

`S_w(Delta)=sum_C w_C Delta_C`,

the top mode gives

`S_w(Delta)=(sum_C w_C)a`.

If the total source-authorized weight vanished, this particular top mode would cancel. Such an object is not the unit-weight BCG or Beltran sum tested here.

Therefore no theorem about arbitrary weights is claimed.

## 9. Repaired status of historical Iter081I

Historical classification:

`ITER081I_SM_BELTRAN_ETA_PLUS_CAUSAL_SUM_RETAINS_ITER077Q_INFINITE_DIMENSIONAL_TANGENTIAL_EXTENSION_AMBIGUITY_EXACT_COROLLARY_SCOPED`

is superseded because its claimed invariant tangential family is not compatible with the corrected exact node-wise compact symmetry.

Its repaired finite statement is:

`ITER083D_SM_CAUSAL_SUM_RETAINS_EXACT_377_DIMENSIONAL_K5_SUPPORTED_AMBIGUITY_REPAIRED_SCOPED`.

The qualitative conclusion survives and is stronger in source fidelity: causal summation does not select the K5 extension, but the surviving frozen ambiguity is **exactly finite-dimensional, 377**, not countably infinite.

## 10. Selector consequence

A finite source-defined orientation sum fixes an off-collision linear combination. It does not supply a rule for choosing a point in the 377-dimensional affine family of same-scaling-degree extensions.

Moreover Iter083C already excludes the whole additive Toller/EPRL identity hierarchy as such a selector.

Therefore any successful local selector must be genuinely additional and non-additive at the joint K5 level: e.g. a source-authorized correlated multivariable boundary value/common regulator, composition/gluing normalization, differential/analytic constraint, positivity law or RG consistency condition.

## Verdict pending production

The theorem obligations P0-P7 are proved structurally here. Promotion to authoritative `PASS_EXACT_SCOPED` requires the independent finite combinatorial/dependency validation in GitHub Actions and subsequent adversarial review.

No generic-spin, all-strata global, regulator-independence, vertex-nonexistence, multivertex, G3/F9/G8/K5, `NEW_PHYSICS_FOUND`, or complete-QG claim follows.
