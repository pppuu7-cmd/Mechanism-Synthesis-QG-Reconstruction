# K5 order-8 principal-symbol reduction — post-prereg derivation

Date: 2026-09-15
Parent scientific contract: `prereg/ACTUAL_SOURCE_ORDERED_MULTIVARIATE_POLAR_NORMAL_JET_ANNIHILATOR_K5_LANE.md`, commit `7466325187f22043d1794379fd6e6dcf62e05abd`.

Status: DERIVATION / REACHABILITY REDUCTION ONLY. No K5 zero/nonzero verdict is assigned here.

## 1. Exact scaling and inversion parity

At the total K5 collision all ten graph edges are internal. Repaired Iter077I gives one `j=1/2` leading source Toller factor per edge with collision order `beta^-2` and odd Cartesian numerator

`M(v)=[[v_z,-v_x-i v_y],[-v_x+i v_y,-v_z]]`,

so `M(-v)=-M(v)` while the scalar denominator is even.

The total leading scaling degree is therefore `20` in the 12-dimensional K5 normal fiber. Hence the simple K5 pole is produced at

`omega_5 = 20-12 = 8`.

The baseline numerator parity degree is ten. Every complete order-eight Taylor contribution has total Cartesian normal degree

`10+8=18`,

which is even. Therefore the global normal-inversion cancellation that kills K3 order zero and K4 order three cannot force the K5 order-eight coefficient to vanish. This is only a non-vanishing permission, not a nonzero proof.

## 2. Order-eight object is mathematically defined by existing exact source functions

The independently confirmed K4 cubic bridge uses an algebraic identity for the complete spin-half Toller matrix,

`T^kappa(h)=t0^kappa(beta)[h+h^{-dagger}]/[2 cosh(beta/2)] + t3^kappa(beta)[h-h^{-dagger}]/[2 sinh(beta/2)]`.

This is an exact identity before Taylor expansion, not a cubic fit. Together with the exact reduced Toller functions, exact relative products `h_ab=exp(-X_b)exp(X_a)`, and exact source rapidity `beta(h)`, it defines finite jets to arbitrary order, including order eight.

Likewise the bridge defining functions

`q(h)=beta(h)^2`,

`q_B=(1/|B|) sum_(a<b in B) q(g_b^-1 g_a)`

are exact analytic functions. No additional regulator metric or fitted order-eight coefficient is required to define their K5 jets.

For the source normal Haar factor the exact radial Jacobian is even,

`(sinh r/r)^2 = 1 + r^2/3 + 2 r^4/45 + r^6/315 + 2 r^8/14175 + O(r^10)`.

Thus absence of an order-eight Toller/Haar/q formula is not, by itself, an object-definition blocker. The unresolved work is the actual full source contraction and resolved angular/Mellin coefficient extraction with all nested faces retained.

## 3. Exact S5 representation reduction at order eight

Let

`V = spin1_SO(3) tensor Std5_S5`

be the 12-dimensional K5 normal fiber and

`M_8=(Sym^8 V)^{SO(3)}`.

Using the authoritative Iter081R K5 order-eight class character

`chi_M8=(714,70,26,3,1,2,-1)`

on the class order

`(1^5),(2,1^3),(2^2,1),(3,1^2),(3,2),(4,1),(5)`,

exact character inner products give

`M_8 = 16[5] + 36[4,1] + 38[3,2] + 29[3,1,1] + 27[2,2,1] + 13[2,1,1,1] + 3[1^5]`.

The full all-j=1/2 boundary representation is

`H_boundary = 2[5] + [4,1] + 2[3,2] + 2[2,2,1] + [2,1,1,1] + 2[1^5]`.

Therefore

`dim Hom_S5(H_boundary,M_8)=217`,

reproducing the independently obtained boundary-covariant order-eight multiplicity.

Every irreducible sector present in `H_boundary` occurs in `M_8` with at least the required multiplicity. Consequently symmetry alone permits an equivariant order-eight residue map of full boundary rank 32. There is no representation-theoretic forced K5 zero or forced missing boundary channel.

The Hom-sector dimensions are:

- `[5]`: `16*2=32`;
- `[4,1]`: `36*1=36`;
- `[3,2]`: `38*2=76`;
- `[2,2,1]`: `27*2=54`;
- `[2,1,1,1]`: `13*1=13`;
- `[1^5]`: `3*2=6`;

summing to `217`.

The maximal possible image rank is

`2*1 + 1*4 + 2*5 + 2*5 + 1*4 + 2*1 = 32`.

## 4. Independent reconstruction of the boundary S5 action

The complete 32-dimensional action was independently reconstructed directly from the frozen four-spin node tensors by permuting vertex labels together with their induced incident-leg permutations, rather than importing the Iter083A character as a literal.

Its exact character is

`(32,0,8,2,0,0,2)`,

and the fixed subspace has dimension exactly two. This reproduces the prior boundary-character result from the raw intertwiner algebra.

Thus an invariant degree-eight probe such as the fourth power of the source K5 quadratic radius reduces to two scalar S5-invariant boundary periods. A nonzero value of either period would be a valid witness that the order-eight principal symbol is nonzero. Vanishing of both would not prove the full 217-dimensional tensor zero.

## 5. Exact pointwise channel reachability

At the authoritative nondegenerate Iter077I integer K5 collision ray, the exact leading full-32 boundary contraction was projected with the exact S5 character projectors.

The projection is nonzero in every boundary-allowed irreducible sector:

`[5], [4,1], [3,2], [2,2,1], [2,1,1,1], [1^5]`.

The `[3,1,1]` projection is zero, exactly as required because that irrep is absent from the boundary representation.

This establishes that no boundary-algebra or S5 channel is pointwise killed already at the leading K5 tensor. It does not establish that the resolved angular/Mellin order-eight moment in any channel is nonzero.

## 6. Proper-face zeros make the physical-origin K5 face primitive

The exact K3 theorem proves the K3 simple residue is identically zero as a meromorphic function of the remaining regulator variables, so every multiresidue containing a K3 factor vanishes.

The exact K4 theorem likewise proves that every compatible iterated/multiresidue containing the simple K4 residue factor vanishes under the frozen normal-crossing convention.

Therefore the proper K3/K4 candidate poles are removable for the purpose of physical-origin residue extraction, and no nonzero proper-face multiresidue can mix into the surviving simple K5 residue. In this precise sense the physical-origin K5 face is primitive relative to the already-classified proper divergent faces.

This has two consequences.

First, the K5 principal-symbol calculation does not require choosing forest subtraction constants or a sequential finite part. Nested-face bookkeeping must still be retained in the meromorphic construction, but the already-proved proper-face residues contribute zero to the physical-origin K5 residue.

Second, under an allowed defining-function gauge

`q'_B=exp(phi_B) q_B`,

one has

`U'(lambda)=exp[(1/2) sum_B lambda_B phi_B] U(lambda)`

with holomorphic multiplier equal to one at the regulator origin. The simple physical-origin K5 residue is therefore unchanged by such a gauge. In particular, for the principal-symbol calculation one may replace an exact nonlinear `q_B` by its source-normal quadratic representative when their ratio is a smooth positive unit on the resolved face. This does not imply invariance of the regular/finite part.

## 7. Authorized next computation

The highest-information next calculation is the actual order-eight principal-symbol moment of the leading K5 homogeneous tensor, preferably first in the two invariant boundary channels. If either invariant principal-symbol period is proved nonzero, lower normal-order Toller/Haar/q corrections cannot cancel that order-eight distributional symbol, and the full K5 residue is necessarily nonzero.

If both invariant periods vanish, the calculation must continue in the remaining S5 sectors; no zero theorem follows from the invariant subspace alone.

Because K5 is primitive relative to the exact-zero K3/K4 proper residues, this angular calculation may be organized as a primitive K5 period/residue problem while retaining the joint-family provenance. It must not replace the 16-parameter family by a one-parameter physical regulator.

## Interpretation ceiling

No K5 zero/nonzero classification is made here. No finite part, unique extension, regulator independence of the full amplitude, physical amplitude, F9/G3 promotion, new physics, or complete-QG claim follows.
