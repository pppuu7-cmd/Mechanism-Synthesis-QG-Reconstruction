# Iter083C-SM preregistration — Toller additivity cannot select the joint-K5 extension: exact Boolean top-mode

Date: 2026-09-15

## Status

Prospective exact algebra/source gate after an exploratory derivation. The candidate nullmode is already known; this preregistration freezes the proof obligations, exhaustive checks and interpretation ceiling before implementation/production inspection.

## Scientific question

Can the exact one-wedge source identity

`T^(+) + T^(-) = D`

and all of its factorized K5 consequences select the joint distributional extension of the ten-Toller product at the common compact collision?

The strongest version tested here grants every possible additive consistency identity obtained by summing over one or more of the ten independent wedge signs, including the full `2^10` sum that reproduces the EPRL product. If a nonzero same-scaling-degree supported deformation is invisible to **all** such partial sums while shifting every causal sector, then Toller additivity alone has zero selector power on that deformation.

## Frozen source authority

1. Bianchi--Chen--Gamonal causal vertex, arXiv:2601.23162:
   - Eq. (4): ten Toller matrices in the K5 vertex;
   - Eq. (5): `T^(+)+T^(-)=D`;
   - Eq. (6): the EPRL vertex is the unconstrained sum over all independent wedge signs `kappa_ab=+-1`;
   - causal signs are constrained to `kappa_ab=sigma_a sigma_b`, and the source explicitly states that summing causal structures does not reproduce the unconstrained EPRL sum.
2. Iter077I source derivation:
   - each all-`j=1/2` Toller branch has leading `beta^-2` singularity;
   - the opposite branch changes the leading coefficient by a nonzero minus sign;
   - switching wedge signs therefore changes a ten-wedge leading contraction only by the product of branch signs and leaves radial degree `-20` unchanged;
   - the frozen full-boundary leading contraction is nonzero, so each sign assignment has the same transverse scaling degree `20` on the witness patch.
3. Iter077L: codimension `12`, same-scaling-degree supported differences allow normal order through `8`.
4. Iter077M/Iter081R and successors: at least one nonzero source-compatible supported ambiguity exists. If Iter083A/B become authoritative, their full frozen ambiguity space may be inserted as the coefficient space, but the qualitative nullmode theorem must not depend on the number 377.

## Boolean sign cube

Let `E=E(K5)` be the ten wedges. An unconstrained Toller sign assignment is

`kappa in {+1,-1}^E`, `|E|=10`.

Define the top Boolean character

`chi_top(kappa) = product_{e in E} kappa_e`.

For any nonzero supported ambiguity `a` that is admissible in a single sign sector, define a sectorwise deformation

`Delta_kappa = chi_top(kappa) a`.

## Frozen proof obligations

### P0 — sign-sector scaling lock

Verify from frozen Iter077I data that every independent sign assignment has the same nonzero leading K5 angular tensor up to the overall factor `chi_top(kappa)` and hence the same transverse scaling degree `20`. Therefore adding the same allowed supported ambiguity with coefficient `+-1` does not violate the same-scaling-degree class in any sector.

### P1 — exhaustive Boolean marginal nullity

For every nonempty subset `S subset E` and every fixed assignment of the complementary signs, verify exactly

`sum_{kappa_S in {+-1}^S} chi_top(kappa) = 0`.

Equivalently, `chi_top` lies in the kernel of every partial sign-sum map that replaces at least one Toller pair `T^+ + T^-` by `D`.

The implementation must check all `2^10-1=1023` nonempty subsets, not merely the ten one-edge marginals.

### P2 — full EPRL sum

Verify separately

`sum_{kappa in {+-1}^10} Delta_kappa = 0`.

Thus the deformation preserves the full source Eq. (6) EPRL identity even if the EPRL-side joint extension is assumed fixed uniquely.

### P3 — causal embedding

Enumerate all node signs

`sigma in {+-1}^5`

and map them to wedge signs

`kappa_ab=sigma_a sigma_b`.

Require exactly `2^(5-1)=16` distinct causal wedge-sign patterns after the global reversal redundancy.

For every causal pattern prove/verify

`chi_top(kappa(sigma)) = product_{a<b} sigma_a sigma_b = product_a sigma_a^4 = +1`.

Hence

`Delta_kappa = +a`

for **every** causal sector.

### P4 — S5 covariance

Verify that `chi_top` is invariant under every permutation of the five K5 vertices and that the set of 16 causal patterns is S5-stable. Therefore if `a` obeys the frozen boundary/normal S5 covariance, the deformation does not break relabeling covariance.

### P5 — source/gauge/support preservation

Show that adding `Delta_kappa`:

- changes nothing off the common-collision set `N`;
- preserves the exact node-wise compact gauge symmetry whenever `a` does;
- preserves boundary linearity/covariance whenever `a` does;
- preserves same-scaling-degree order;
- does not alter any one-wedge Toller function or its Feynman prescription.

### P6 — strongest-additivity no-go

Conclude that even granting **all** factorwise additive consistency equations generated by `T^+ + T^- = D`, including mixed products with arbitrary subsets of `D` factors, does not constrain the coefficient `a` in the top Boolean mode.

This is stronger than showing only that the total EPRL sum has a kernel.

### P7 — dependency-safe dimension statement

The theorem must state two levels:

- unconditionally from the surviving Iter077M witness: a nonzero top-mode ambiguity survives Toller additivity;
- only if Iter083A/B are authoritative: the entire frozen boundary-covariant supported ambiguity space survives diagonally on the 16 causal sectors. If its exact dimension is later confirmed as 377, then the additivity-null causal ambiguity has dimension at least/exactly 377 within that frozen coefficient sector, as authorized by the corresponding upstream theorem.

No premature numerical promotion is allowed.

## Negative controls

The implementation/review must reject:

1. constant Boolean mode `1` as a full-sum nullmode;
2. any proper-subset character `product_{e in R} kappa_e` with `R != E` as being invisible to **all** nonempty partial sums (choose a summed subset disjoint from `R` to expose it);
3. an arbitrary random sign table without exact character structure;
4. the false claim that all `2^10` sign assignments are causal;
5. the false claim that the all-minus wedge assignment is causal for K5;
6. a deformation that changes one-wedge Toller functions off `N`;
7. promotion from additive consistency to a common K5 regulator/boundary-value prescription.

## PASS classification

If P0-P7 and all controls pass:

`ITER083C_SM_TOLLER_ADDITIVITY_HAS_EXACT_JOINT_K5_TOP_BOOLEAN_SELECTOR_NULLMODE`

Verdict: `PASS_EXACT_SCOPED`.

## Interpretation ceiling

A PASS proves only that the entire hierarchy of **additive** identities inherited from `T^+ + T^- = D` cannot by itself select the joint common-collision K5 extension. It does not rule out a genuinely new common-regulator limit, analytic multivariable boundary-value prescription, composition/gluing law, positivity condition, RG condition, differential equation, or other non-additive source principle.

No causal-vertex divergence/nonexistence, regulator independence, generic-spin completeness, all-strata global vertex, multivertex closure, G3/F9/G8/K5, `NEW_PHYSICS_FOUND`, or complete quantum gravity follows.
