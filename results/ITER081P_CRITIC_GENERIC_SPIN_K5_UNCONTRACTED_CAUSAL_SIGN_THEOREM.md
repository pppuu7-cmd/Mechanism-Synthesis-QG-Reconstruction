# Iter081P Critic exact theorem — generic finite-spin K5 proper-causal branch assignments have the same uncontracted leading tensor in the gamma-simple minimal blocks

Date: 2026-09-14
Status: **EXACT PRE-BOUNDARY CARRIER THEOREM; NOT A PHYSICAL FULL-VERTEX NON-L1 THEOREM**

## Inputs

1. BCG Eq. (13): Cartan reconstruction of each full Toller matrix.
2. Iter081N: for every finite `j>0`, every `m`, fixed real `rho!=0`, the gamma-simple minimal reduced branches satisfy
   `t^-_(jjm) = - t^+_(jjm)` at the nonzero leading order `beta^(-(2j+1))`.
3. Iter081O: therefore each full projected wedge block satisfies
   `Leading[P_j T^- P_j] = - Leading[P_j T^+ P_j]`,
   with an invertible leading magnetic-space matrix.
4. Beltran v2 causal K5 signs: `epsilon_ab=eta sigma_a sigma_b`, modulo global reversal.

## Frozen K5 carrier setting
Consider the ten K5 wedges `e=(ab)`. Assign to each wedge an arbitrary finite nonzero spin `j_e>0` in the gamma-simple minimal block and a fixed real `rho_e!=0` (in EPRL one may specialize to `rho_e=gamma j_e`, `gamma!=0`).

Take a common-collision approach on which every relative wedge boost rapidity tends to zero,

`beta_e(r)=c_e r+o(r)`, `c_e>0`, `r->0+`,

with arbitrary admissible Cartan SU(2) angular data. No boundary intertwiner contraction is performed in this theorem.

For each edge define the nonzero invertible leading plus-branch matrix

`L_e := c_e^(-(2j_e+1)) D^(j_e)(U1_e) C_(j_e)(rho_e) D^(j_e)(U2_e)`.

Then

`P_(j_e) T_e^(epsilon_e) P_(j_e)`
`= epsilon_e r^(-(2j_e+1)) L_e + o(r^(-(2j_e+1)))`,

where `epsilon_e=+1` denotes branch `+` and `epsilon_e=-1` branch `-`.

## Ten-wedge tensor product
Let

`P_total := sum_(e in E(K5)) (2j_e+1)`.

The uncontracted ten-wedge leading tensor for a branch assignment `epsilon` is

`K_epsilon(r)`
`= (prod_e epsilon_e) r^(-P_total) [tensor_product_e L_e] + o(r^(-P_total)).`

Because every `L_e` is invertible, their tensor product is invertible and in particular nonzero.

Thus branch dependence of the full uncontracted leading K5 carrier is **only** the scalar parity `prod_e epsilon_e`.

## Proper causal assignments
For a Beltran proper causal K5 assignment

`epsilon_ab=eta sigma_a sigma_b`,

one has exactly

`prod_(a<b) epsilon_ab = eta^10 prod_a sigma_a^4 = +1`.

Therefore **every proper causal assignment in either signature sector has the same nonzero uncontracted leading tensor**:

`K_(eta,sigma)(r) = r^(-P_total) [tensor_product_e L_e] + o(r^(-P_total)).`

There is no leading cancellation between proper causal assignments at the uncontracted magnetic carrier level, for arbitrary finite nonzero edge spins satisfying the frozen minimal-block hypotheses.

## Finite causal sums
Consequently:

- eta=+ unit-weight sum: leading tensor is `16 r^(-P_total) tensor_e L_e`;
- eta=+ plus eta=- proper-causal unit-weight sum: leading tensor is `32 r^(-P_total) tensor_e L_e`;
- arbitrary radius-independent causal weights `w_s`: leading tensor is `(sum_s w_s) r^(-P_total) tensor_e L_e` and cancels iff `sum_s w_s=0`.

This is the generic finite-spin **carrier-level** analogue of Iter081H/K/M.

## Unrestricted branch cube
Over all `2^10` independent branch assignments,

`sum_epsilon prod_e epsilon_e = 0`.

Hence the leading pole cancels in the unrestricted branch sum, consistent with edgewise `T^+ + T^- = D`. As in Iter081L, proper causal assignments all lie in the positive parity class; the remaining non-causal assignments supply the compensating negative parity at leading order.

## Why this is not yet a generic-spin physical K5 theorem
The source-order firewall requires the full boundary contraction before promoting a carrier singularity to the physical local K5 amplitude. Although `tensor_e L_e` is nonzero and invertible as a product magnetic-space operator, a particular boundary intertwiner functional can annihilate its contraction.

Iter077I independently proved nonvanishing for all 32 boundary components only in the all-`j=1/2` sector. No corresponding complete generic-spin intertwiner-space nonvanishing theorem is imported here.

Therefore the present theorem does **not** establish a generic-spin local `L1` obstruction for the fully contracted causal vertex.

## Optional operator-valued observation
If every nonzero spin satisfies `j_e>=1/2`, then `P_total>=20`. The uncontracted carrier operator norm therefore has a radial singularity at least as strong as `r^-20` on a nondegenerate common-collision ray. This is a pre-boundary diagnostic only; it must not replace the required full boundary contraction.

## Classification
`ITER081P_SM_GENERIC_FINITE_NONZERO_SPIN_K5_PROPER_CAUSAL_ASSIGNMENTS_HAVE_IDENTICAL_NONZERO_UNCONTRACTED_LEADING_TENSOR_AND_NO_CAUSAL_SECTOR_LEADING_CANCELLATION_EXACT_CARRIER_THEOREM_SCOPED`.

## Claim ceiling
No generic-spin full-boundary nonvanishing theorem; no generic-spin physical K5 L1 theorem; no causal-vertex divergence/nonexistence; no statement for zero-spin edges, nonminimal `(j,l)` blocks or all partial-collision strata; no extension selector, regulator independence, E3/E4/E6 closure, G3/F9/G8/K5, `NEW_PHYSICS_FOUND` or complete QG.
