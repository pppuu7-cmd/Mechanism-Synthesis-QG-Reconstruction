# Iter081Y-SM Critic exact result — partial K3/K4 collision strata have finite invariant normal-jet types but function-valued external tangential coefficient spaces

Date: 2026-09-14
Status: **EXACT CONDITIONAL GEOMETRY THEOREM; NO PHYSICAL K3/K4 DIVERGENCE CLAIM**

## Prospective lock
Preregistered before result at `prereg/ITER081Y_SM_PARTIAL_STRATUM_INVARIANT_COUNTERTERM_GEOMETRY.md`, commit `83586c4a6afd5dd343059c02532ed00a886ff3dd`.

## Block geometry
For a connected collision block of size `k` in the five-node linearized boost configuration modulo common translation,

`V_k = spin1_SO(3) tensor Std_k_Sk`,

`dim V_k=3(k-1)`.

The all-j=1/2 source-leading internal-edge scaling degree is

`sd_k = 2*C(k,2)=k(k-1)`

and the normal singular order is

`omega_k = sd_k-3(k-1)=(k-1)(k-3)`.

The remaining external tangential boost dimension is

`t_k=12-3(k-1)=3(5-k)`.

Hence:

| block | codim | sd | omega | external tangential dimension |
|---|---:|---:|---:|---:|
| K3 | 6 | 6 | 0 | 6 |
| K4 | 9 | 12 | 3 | 3 |
| K5 | 12 | 20 | 8 | 0 |

## K3 invariant normal jets
For `k=3`, `omega_3=0`, so only total normal order zero is allowed by same-scaling-degree extension power counting.

Therefore the scalar `SO(3) x S3` invariant normal-jet type space is one-dimensional:

`(d_0^(3))=(1)`.

It is represented by the delta distribution on the K3 partial diagonal, multiplied by a coefficient distribution/function along that stratum.

## K4 invariant normal jets
For `k=4`,

`V_4 = R^3 tensor Std_4`, `dim=9`, `omega_4=3`.

The scalar invariant dimensions through order 3 are

`(d_0^(4),d_1^(4),d_2^(4),d_3^(4)) = (1,0,1,0)`.

Reason:

- order 0: the scalar delta-type invariant;
- order 1: no invariant vector in either nontrivial factor;
- order 2: a unique invariant from the product of the SO(3) metric and the S4-standard metric;
- order 3: an SO(3) scalar from three vector indices is proportional to `epsilon_ijk`; symmetrizing the total tensor requires the S4-standard indices to occupy the alternating cube `wedge^3 Std_4`, which is the sign representation rather than the trivial representation, so no `S4` singlet survives.

Thus K4 has two scalar invariant normal structures within the allowed singular order: normal orders 0 and 2.

## K5 consistency control
For `k=5`, the same representation is `spin1 tensor Std_5`, `omega_5=8`. Iter081R independently gives

`(1,0,1,0,3,0,7,0,16)`,

total 28. This is consistent with the block formula and is not recomputed here.

## External tangential coefficient spaces
The crucial difference from the deepest K5 stratum is that partial strata retain noncompact external boost coordinates after internal cluster collapse and compact gauge quotient.

### K4 stratum
Collapse four vertices to one cluster and leave the fifth external. The remaining relative boost coordinate is

`Y in R^3`.

Residual compact frame rotation acts diagonally as `Y -> RY`. Internal `S4` acts trivially on this external vector; global S5 covariance carries the same coefficient law between the five equivalent K4 strata.

Therefore any smooth radial function

`f(|Y|^2)`

is an allowed scalar tangential coefficient candidate away from the deeper collision `Y=0`. The polynomial family

`f_n(Y)=(|Y|^2)^n`, `n=0,1,2,...`

is linearly independent. Thus the scalar tangential coefficient function space on a representative K4 stratum is infinite-dimensional.

Each of the two invariant normal structures (orders 0 and 2) may, at the level of extension geometry, carry such a function-valued coefficient unless an additional source/locality/composition law fixes it.

### K3 stratum
Collapse three vertices and retain two external singleton nodes. Relative to the collapsed cluster use

`(Y_4,Y_5) in R^3 x R^3`.

Residual compact rotation acts simultaneously on both vectors; exchange of the two external singleton labels is an `S2` symmetry of the representative stratum.

Examples of smooth scalar invariants include

`a=|Y_4|^2+|Y_5|^2`,
`b=Y_4 dot Y_5`,
`c=(|Y_4|^2-|Y_5|^2)^2`.

Already the family `a^n`, `n=0,1,2,...`, is linearly independent and invariant under rotations and external-node exchange. Hence the coefficient multiplying the unique K3 order-zero normal delta structure may be an infinite-dimensional invariant function of external tangential data unless additional physics fixes it.

## Exact conditional conclusion
The **normal tensor type** problem and the **tangential coefficient** problem separate:

- K3: 1 invariant normal type, function-valued coefficient on a 6-dimensional external quotient;
- K4: 2 invariant normal types, function-valued coefficients on a 3-dimensional external quotient;
- K5: >=28 invariant scalar normal types, but no external noncompact tangential boost variable at the deepest stratum, so the demonstrated scalar coefficients reduce to finite fiber data.

Classification:

`ITER081Y_SM_PARTIAL_STRATA_HAVE_FINITE_INVARIANT_NORMAL_JET_TYPES_BUT_FUNCTION_VALUED_EXTERNAL_TANGENTIAL_COEFFICIENT_SPACES_EXACT_GEOMETRY_SCOPED`.

## Physical qualification
This theorem is **conditional geometry**. It does not establish that the fully boundary-contracted source amplitude actually requires extension on every K3 or K4 stratum. Historical Iteration 022 gives numerical evidence for K3 borderline and K4 power divergence, but exact full-boundary nonvanishing is currently authoritative only at K5 (Iter077I).

If future source-ordered full-boundary analysis proves a K3/K4 stratum physically singular, the corresponding extension ambiguity is potentially function-valued along the external variables and is more demanding than the finite deepest-stratum coefficient problem.

## Claim ceiling
No exact physical K3/K4 divergence theorem, no global forest renormalization, no selector, no regulator independence, no causal-vertex nonexistence, no G3/F9/G8/K5, `NEW_PHYSICS_FOUND`, or complete-QG claim follows.
