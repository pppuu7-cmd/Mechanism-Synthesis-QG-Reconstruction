# Iter081R-SM prereg — right-SU(2)^5 / S5 invariant K5 normal-jet extension classification

Status: **PROSPECTIVE REPAIR GATE — frozen before implementation/production**
Date: 2026-09-14

## Motivation
`results/ITER077Q_ADVERSARIAL_RIGHT_SU2_SOURCE_LOCK_REVIEW.md` invalidates historical Iter077Q's infinite-dimensional tangential `Q^n` family because the fully boundary-contracted source object has an omitted exact node-wise compact gauge symmetry. The local amplitude nevertheless remains nonunique by Iter077M's constant `F_SU2 delta_N` witness and Iter077L's normal jets through order 8. The next task is to classify, rather than guess, the scalar normal-jet freedom that survives the corrected exact symmetries.

## Frozen geometric object
Before source global gauge fixing there are five SL(2,C) vertex variables. At a common compact collision, infinitesimal normal directions are five boost vectors `X_a in R^3`, modulo the common boost removed by global left SL(2,C) gauge. Therefore the 12-dimensional normal fiber is

`V = R^3 \otimes Std_5`,

where `Std_5` is the real 4-dimensional standard representation of `S5` (`R^5 / diagonal`).

After fixing one group variable to identity, the exact node-wise compact gauge action is

`g_a -> u_1^-1 g_a u_a`, `u_a in SU(2)`.

It is transitive on `N=SU(2)^4`; the stabilizer of the identity compact configuration is diagonal `SU(2)`. Its action on the boost normal fiber is the spin-1 / SO(3) adjoint action on the `R^3` factor. Vertex relabeling acts on `Std_5`.

Thus scalar invariant normal jets at one point are classified by

`Sym^k(V)^(SO(3) x S5)`, `0<=k<=8`.

## Frozen distributional link
Iter077L allows normal derivatives through total order 8 because `sd_N=20` and `codim(N)=12`. A normal derivative of total order `k` applied to `delta_N` has transverse scaling degree `12+k`, so all `k<=8` remain within maximal scaling degree 20.

Fix one actual gauge-invariant boundary state `Psi_0` for which the Iter077M compact functional is nonzero at the identity. Node-wise compact gauge invariance makes `F_SU2(y;Psi_0)` constant on the transitive compact collision orbit. Each invariant symmetric normal tensor therefore defines a source-symmetry-compatible supported jet multiplied by this nonzero boundary functional.

The gate classifies only this scalar invariant-jet subspace. It does not claim to classify all boundary-covariant jet maps.

## Exact Molien/character computation
For each `S5` conjugacy cycle type `lambda` with cycle lengths `ell`, the standard-representation determinant obeys

`det(1-s Std(lambda)) = prod_(ell in lambda)(1-s^ell)/(1-s)`.

Use an SU(2) torus variable `x` in which the spin-1 weights are `x^2,1,x^-2`. The symmetric-power character generating function for `V=spin1 x Std_5` at class `lambda` is

`G_lambda(t,x) = prod_(w in {2,0,-2}) [(1-t x^w) / prod_(ell in lambda)(1-(t x^w)^ell)]`.

Expand exactly through `t^8`. For each degree `k`, extract the SU(2) spin-0 multiplicity by

`m0_lambda(k) = coeff[x^0] G_lambda|_(t^k) - coeff[x^2] G_lambda|_(t^k)`.

Then average over `S5` classes:

`d_k = (1/120) sum_lambda |C_lambda| m0_lambda(k)`.

All arithmetic must be exact integers/rationals; no floating eigenvalues or numerical group integration may determine `d_k`.

## Required controls
1. Enumerate all seven partitions/cycle types of 5 and verify class sizes sum to 120.
2. Verify `d_0=1` and `d_1=0` as structural controls.
3. Explicitly verify existence of the unique quadratic invariant from the product of the SO(3) metric and the S5-standard metric, so the exact count must have `d_2>=1`.
4. Verify every returned `d_k` is a nonnegative integer.
5. Independently check at least the lower-bound family `(Delta_perp)^r delta_N`, `r=0,...,4`, corresponding to invariant even orders `0,2,4,6,8`.
6. Include a negative control omitting the S5 average; the resulting SO(3)-only invariant counts must differ at some degree >=4, proving the S5 projection is active.
7. Record exact class-by-class singlet multiplicities and the final vector `(d_0,...,d_8)` in the production artifact.

## Frozen classifications
- `ITER081R_SM_RIGHT_SU2_S5_INVARIANT_NORMAL_JET_SPACE_NONTRIVIAL_EXACT_SCOPED` iff the exact count is valid and `sum_(k=0)^8 d_k > 1`.
- `ITER081R_SM_RIGHT_SU2_S5_INVARIANT_NORMAL_JET_SPACE_SCALAR_ONLY_EXACT_SCOPED` iff exact valid count gives only the order-zero invariant.
- `INVALID_IMPLEMENTATION_OR_GEOMETRIC_REPRESENTATION` if class arithmetic, normal representation, or controls fail.

## Claim ceiling
A nontrivial result establishes only a finite-dimensional **source-symmetry-compatible scalar jet lower bound** at the frozen all-j=1/2/common-collision extension problem. It replaces the invalid infinite tangential claim; it does not prove the entire extension space has that exact dimension, because boundary-covariant coefficient maps and other jet representations may enlarge it. It does not define a selector, prove causal-vertex divergence/nonexistence, establish regulator independence, composition, G3, F9/G8/K5, generic-spin physical non-L1 behavior, new physics or complete QG.
