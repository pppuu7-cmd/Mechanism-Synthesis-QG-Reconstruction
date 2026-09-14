# Iter081W-SM Critic exact result — exact transverse dilation covariance still leaves a 16-dimensional invariant order-8 ambiguity

Date: 2026-09-14
Status: **EXACT SELECTOR-POWER THEOREM SCOPED TO THE LEADING HOMOGENEOUS SINGULARITY**

## Prospective lock
Preregistered before result at `prereg/ITER081W_SM_EXACT_DILATION_COVARIANCE_SELECTOR_POWER.md`, commit `be6f8a19a1e7163ef67b160c3d2d1cf7afb82ec6`.

## Inputs
Authoritative local geometry:

- collision submanifold `N=SU(2)^4`;
- transverse codimension `d=12`;
- leading source-ordered minimal-sector K5 homogeneity degree `lambda=-20` (Iter077I/Iter077L);
- repaired scalar invariant normal-jet dimensions through order 8 (Iter081R):
  `[1,0,1,0,3,0,7,0,16]`.

Let `E=X^i partial/partial X^i` be the transverse Euler vector field.

## Euler action on supported normal jets
In `d` normal dimensions,

`E delta_N = -d delta_N`.

For a normal derivative `partial^alpha delta_N` of total order `|alpha|=k`, the distribution identity

`E(partial^alpha delta_N) = -(d+k) partial^alpha delta_N`

follows from `[E,partial_i]=-partial_i` together with `E delta_N=-d delta_N`.

Therefore a total-order-`k` supported jet has exact transverse homogeneity degree

`-(12+k)`.

## Difference of equally scale-covariant extensions
Let `U1,U2` extend the same leading off-collision homogeneous distribution `u_0` of degree `lambda=-20`.

If both satisfy the same exact homogeneous equation

`(E-lambda) U_i = 0`,

or, more generally, the same fixed anomalous equation

`(E-lambda)U_i=A`

with identical supported anomaly `A`, their difference `W=U1-U2` is supported on `N` and obeys

`(E-lambda)W=0`.

A supported normal jet can occur in `W` only if

`-(12+k) = -20`,

hence exactly

`k=8`.

All lower even orders `0,2,4,6` are excluded by exact dilation covariance of the **difference**.

## Repaired invariant dimension
Iter081R gives

`dim J_8^(SO(3) x S5) = 16`.

Every element of this degree-8 invariant sector has exactly homogeneity `-20`, satisfies the corrected node-wise right-SU(2)/S5 symmetry, is supported on `N`, and lies within the maximal scaling-degree class.

Therefore exact transverse homogeneity, or equality of a fixed scaling anomaly, does **not** uniquely select the leading extension on the demonstrated scalar invariant subspace. It leaves at least a 16-dimensional difference space.

Classification:

`ITER081W_SM_EXACT_DILATION_COVARIANCE_LEAVES_16_DIMENSIONAL_INVARIANT_ORDER8_AMBIGUITY_EXACT_SCOPED`.

## Interpretation
This is stronger than ordinary scaling-degree control: the repaired scalar ambiguity is reduced from the 28-dimensional orders `0,2,4,6,8` to the 16-dimensional resonant order-8 sector, but uniqueness still fails.

The result also identifies the natural location of a scaling anomaly in analytic regularization: degree `-20=-12-8` is resonant with order-8 delta derivatives. Iter081V separately asks whether the actual Rühl-motivated radial analytic family has a nonzero residue in this sector.

## Important qualification
This theorem does not prove that an exactly homogeneous extension exists. At resonant degree a nonzero residue/anomaly can obstruct exact homogeneity. The result is conditional selector power: **if two extensions obey the same exact dilation law or same fixed anomaly, their difference may still span the 16-dimensional invariant order-8 sector unless an additional law fixes it.**

A source-derived anomaly whose full 16 coefficients are fixed could supply further information, but no such K5 source equation is presently established.

## Claim ceiling
No statement is made that the complete physical amplitude is exactly homogeneous, that the total extension space has dimension 16, that analytic regularization must have a nonzero residue, or that no stronger selector exists. No causal-vertex divergence/nonexistence, regulator independence, generic-spin physical vertex theorem, G3/F9/G8/K5, `NEW_PHYSICS_FOUND`, or complete-QG claim follows.
