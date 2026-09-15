# Actual multivariate polar gate — exact K3 residue parity derivation

Date: 2026-09-15
Parent preregistration: `prereg/ACTUAL_SOURCE_ORDERED_MULTIVARIATE_POLAR_NORMAL_JET_ANNIHILATOR.md`, commit `4c4478db20e08387fb7067a55d773fce31d3fc34`.

## Scope

This file derives only the K3-face polar coefficient at the physical regulator origin for the frozen all-`j=1/2`, source-ordered, full-32-boundary `q_B`-scheme family. It does not infer the K4 or K5 coefficients.

## 1. K3 normal fiber and inversion

Fix a K3 collision block `B={a,b,c}`. In source-normal symmetric-space coordinates write the three boost-normal vectors relative to their barycenter as

`y_a,y_b,y_c in R^3`, `y_a+y_b+y_c=0`.

The K3 normal fiber therefore has real dimension 6.

The involution

`I_B : (y_a,y_b,y_c) -> (-y_a,-y_b,-y_c)`

preserves the source-normal quadratic radius

`R_B^2=sum_i |y_i|^2=(1/3)sum_(i<j)|y_i-y_j|^2`

and hence preserves the K3 front sphere, its angular density, and the exact nonlinear defining function `q_B` to the order needed for the residue at `L_B=0`.

## 2. The only singular K3 factors are the three internal wedges

At the interior of the K3 collision face, exactly the three edges internal to `B` have vanishing Cartan rapidity. The remaining seven K5 edges are smooth with respect to the K3 normal variables at `rho_B=0`.

For an internal edge `(i,j)`, repaired Iter077I gives the frozen `j=1/2` leading Toller matrix, up to a nonzero common branch/scalar factor, as

`beta_ij^-2 C(n_ij)`

with

`C(n)=-n.sigma`

(up to one common convention sign), equivalently in unnormalized vector form

`M(v)=[[v_z,-v_x-i v_y],[-v_x+i v_y,-v_z]]`.

Therefore

`M(-v)=-M(v)`,

while `|v|^-3` and `beta^-2` are even under inversion.

Every internal K3 leading wedge coefficient is odd under `I_B`.

There are exactly three such edges. Their product is therefore odd:

`A_internal^(0)(-Omega_B)=-A_internal^(0)(Omega_B)`.

The branch sign of each wedge is independent of `Omega_B`; multiplying by any fixed branch pattern cannot change this parity statement.

## 3. External factors do not repair the odd parity at residue order zero

The K3 candidate pole through the physical regulator origin occurs at normal Taylor order

`omega_K3=0`.

Hence the residue only uses the zeroth Taylor coefficient in the K3 radial variable.

At `rho_B=0`:

- every wedge not internal to `B` is evaluated at the collapsed K3 configuration and is independent of the K3 front-face direction `Omega_B`;
- the pulled-back Haar/tubular leading angular density is even under `I_B`;
- every other block regulator that is nonvanishing on the interior of this K3 face contributes a smooth positive zeroth-order factor independent of `Omega_B`;
- the full boundary contraction is finite multilinear algebra and therefore preserves the odd parity inherited from the three internal leading matrices.

Thus for each of the 32 boundary components and pointwise in all tangential/external variables, the complete residue integrand on the K3 front sphere is odd.

## 4. K2 subfaces do not spoil the cancellation

The K3 front sphere contains angular loci corresponding to internal K2 subcollisions. A single `j=1/2` wedge behaves as `beta^-2` in three relative boost dimensions, while the local K2 radial measure is `beta^2 d beta`.

Therefore K2 singularities are locally absolutely integrable on the K3 front face. The K3 angular integral is a legitimate improper integral and the inversion can be applied without a nonintegrable boundary contribution.

The complete angular pairing hence satisfies exactly

`Integral_(front sphere) A_K3^(0)(Omega_B) dOmega_B = 0`.

## 5. Exact K3 polar conclusion

The corrected bridge local form at a K3 face is

`rho_B^(L_B-1) [A_0(Omega_B)+O(rho_B)]`.

The coefficient of the candidate pole `1/L_B` is the front-face angular pairing of `A_0` against the order-zero test-function coefficient.

By the parity argument above, that coefficient vanishes identically.

Therefore the actual full-source family has

`Res_(L_K3=0) U = 0`

for every K3 block in the frozen local all-`j=1/2` sector.

This is stronger than the formal annihilator ceiling `I_K3^1`: the zero residue annihilates the entire test-function space.

Classification for the K3 lane:

`K3_PHYSICAL_ORIGIN_POLAR_COEFFICIENT_ZERO_EXACT_BY_NORMAL_INVERSION_PARITY`.

## 6. Nested-corner strengthening

At a compatible corner `K3 subset K4 subset K5`, take the K3 boundary variable `rho3` to zero while keeping the outer front-face variables fixed.

All factors not internal to the chosen K3 have a zeroth `rho3` coefficient independent of the K3 angular direction. The three K3 internal leading matrices remain odd under inversion of the six-dimensional incremental K3 normal variable.

Therefore the coefficient of `1/L_K3` vanishes as a meromorphic function of the remaining regulator variables before any K4/K5 residue extraction.

Consequently **every multiresidue containing a K3 face factor vanishes**, including the maximal-chain candidate coefficient

`coeff[1/(L_K3 L_K4 L_K5)] = 0`.

This zero is scheme invariant: multiplying by a holomorphic defining-function gauge factor cannot create a pole in `L_K3` where the residue is identically zero.

## 7. What this does not establish

The result does not determine the K4 or K5 polar coefficients. In particular, odd/even counting of only the leading internal matrices is not sufficient for K4 order 3 because that residue receives third-order Taylor data from external smooth factors, Haar corrections, BCH/nonlinear group geometry and subleading Toller coefficients.

No K4/K5 zero or nonzero conclusion is inferred here.

No finite part, physical selector, regulator independence, global patching, generic-spin or downstream physics conclusion follows.