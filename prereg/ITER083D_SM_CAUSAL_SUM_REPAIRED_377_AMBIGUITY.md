# Iter083D-SM preregistration — repaired causal-sum persistence of the exact 377-dimensional K5 ambiguity

Date: 2026-09-15

## Status

Prospective repair gate. This iteration replaces the invalid infinite-dimensional conclusion of historical Iter081I, whose `Q(y)^n F delta_N` tangential family depended on the superseded Iter077Q symmetry model. No historical infinite tangential family may be used in this gate.

## Scientific question

After the exact node-wise compact gauge symmetry has reduced the common-collision same-scaling-degree ambiguity to the authoritative finite space `F_8` of complex dimension 377, can the source-defined finite sum over causal orientation sectors remove that ambiguity?

The candidate theorem is no: the causal sum remains a nonzero scalar multiple of every Iter083C top-Boolean ambiguity vector, and the already-summed non-L1 object independently has the same intrinsic `F_8` extension-difference space.

## Frozen authority

1. Bianchi--Chen--Gamonal, arXiv:2601.23162v1:
   - fixed causal vertex `A_v^(sigma_a sigma_b)` is defined by ten Toller factors;
   - global reversal `sigma_a -> -sigma_a` leaves all wedge causal data unchanged;
   - Eq. (6) gives the unconstrained `2^10` EPRL sign sum;
   - the paper explicitly compares this with the unweighted causal-structure sum
     `sum_(sigma_a=+-1) A_v^(sigma_a sigma_b)`, i.e. 32 node-sign labels, with each of the 16 distinct wedge-sign patterns counted twice.
2. Beltran `arXiv:2603.22661v2` as frozen by authoritative Iter081H:
   - positive-signature causal vertex is the unit-weight sum over the 16 inequivalent `eta=+1` assignments;
   - those assignments are exactly `epsilon_ab=sigma_a sigma_b` modulo global reversal.
3. Iter081H authoritative source-ordered corollary:
   - all 16 Beltran causal patterns have the same nonzero `r^-20` leading coefficient for each of the 32 frozen boundary basis components;
   - their unit-weight sum therefore has coefficient `16 C_alpha != 0` and transverse scaling degree 20.
4. Iter083A authoritative production:
   - true boundary-covariant graded multiplicities
     `m=(2,0,5,1,22,10,72,48,217)`.
5. Iter083B authoritative theorem:
   - for the frozen all-`j=1/2` common collision, the intrinsic symmetry-compatible same-scaling-degree supported extension-difference space `F_8` has exact complex dimension 377.
6. Iter083C authoritative theorem and production:
   - for every `a in F_8`, the sectorwise deformation
     `Delta_kappa=(product_e kappa_e) a`
     is annihilated by every additive Toller partial-sign-sum identity;
   - on every causal factorized pattern `kappa_ab=sigma_a sigma_b`, `product_e kappa_e=+1`.

## Frozen objects

Let `C16` be the 16 distinct factorized K5 wedge-sign patterns modulo global node-sign reversal.

Let

`S_Beltran(A) = sum_(kappa in C16) A_kappa`.

Let

`S_BCG(A) = sum_(sigma in {+-1}^5) A_(sigma_a sigma_b)`.

Because global reversal produces the same wedge pattern,

`S_BCG = 2 S_Beltran`

on any family depending only on the wedge signs.

No arbitrary orientation weights are introduced.

## Frozen proof obligations

### P0 — historical repair

Identify the exact historical Iter081I dependency on the now-invalid Iter077Q infinite tangential family and prohibit re-use of its infinite-dimensional conclusion. Preserve only source facts that remain independently valid: the unit-weight causal sum, the nonzero summed `r^-20` source term, and the generic observation that a finite off-collision sum does not by itself assign values to supported distributions.

### P1 — exact causal multiplicities

Enumerate all 32 node-sign assignments, quotient by global reversal, and require exactly 16 distinct wedge-sign patterns, each with multiplicity two in the Bianchi--Chen--Gamonal `sum_(sigma_a=+-1)` convention.

Require the Beltran `eta=+1` convention to contain exactly those 16 distinct patterns once each.

### P2 — top-mode causal value

For every causal pattern verify

`chi_top(kappa)=product_(a<b) kappa_ab=product_a sigma_a^4=+1`.

Thus Iter083C gives

`Delta_kappa=a`

for every causal sector and every `a in F_8`.

### P3 — exact summed deformation

Prove and verify

`S_Beltran(Delta)=16 a`,

`S_BCG(Delta)=32 a`.

Because the base field is complex/characteristic zero, multiplication by 16 or 32 is injective. Therefore the complete 377-dimensional `F_8` embeds into the ambiguity of either causal sum.

### P4 — direct extension-space upper bound

Do not stop at a lower bound. Use authoritative Iter081H plus Iter083B:

- the Beltran summed off-collision object has exact transverse scaling degree 20 on the frozen common-collision patch;
- it has the same support geometry `N`, boundary-dual fiber and exact compact-gauge/S5 covariance used to define `F_8`;
- therefore any two same-scaling-degree source-symmetry-compatible extensions of the summed object differ by an element of `F_8`.

This gives an upper bound `dim <=377`. Combined with P3, conclude the exact dimension of the frozen Beltran causal-sum extension ambiguity is 377.

For the Bianchi--Chen--Gamonal 32-label sum, either establish the same nonzero `r^-20` statement from its equality `S_BCG=2 S_Beltran` on the common 16-pattern source family, or refrain from an exact-dimension promotion if source conventions make the identification invalid. No normalization assumption beyond the frozen unit sums is allowed.

### P5 — additive consistency survives

Because Iter083C top-mode deformations are invisible to every nonempty partial sign sum generated by `T+ + T-=D`, show that the 377-dimensional surviving causal-sum family is compatible with the complete additive Toller/EPRL identity hierarchy. Causal summation therefore does not recover selector power indirectly from those identities.

### P6 — no hidden orientation-weight selector

The source sums tested here use unit coefficients. Do not generalize the exact 377 persistence theorem to arbitrary externally chosen weights `w_sigma`. For a weighted sum, the top mode maps `a -> (sum w_sigma) a`; cancellation is possible only when that total weight vanishes, and such weights are a different object requiring separate source authority.

### P7 — finite repaired conclusion

The historical conclusion `infinite-dimensional causal-sum ambiguity` must be explicitly superseded by

`exactly 377-dimensional` within the frozen all-`j=1/2`, common-collision, boundary-linear, compact-gauge/S5-covariant same-scaling-degree class.

No infinite-dimensional tangential freedom may remain in the current classification.

## Negative controls

The implementation/review must reject:

1. treating all 32 node-sign labels as 32 distinct wedge-sign patterns;
2. treating the 16-pattern Beltran sum as having coefficient 32;
3. treating the 32-label BCG sum as having coefficient 16;
4. inserting alternating or fitted orientation weights absent from the source definitions;
5. reusing `Q(y)^n F delta_N` as a valid exact-symmetry ambiguity;
6. claiming that nonzero scaling degree alone proves a 377-dimensional lower bound without Iter083A/B;
7. claiming that causal summation selects a unique extension because it is finite;
8. claiming the result rules out a future non-additive common regulator/boundary-value/composition selector.

## PASS classification

If P0-P7 and all controls pass:

`ITER083D_SM_CAUSAL_SUM_RETAINS_EXACT_377_DIMENSIONAL_K5_SUPPORTED_AMBIGUITY_REPAIRED_SCOPED`

Verdict: `PASS_EXACT_SCOPED`.

The historical Iter081I infinite-dimensional classification is then `SUPERSEDED_INVALID_SOURCE_SYMMETRY_MODEL`, while its qualitative nonuniqueness conclusion is repaired and retained in finite form.

## Interpretation ceiling

A PASS proves only that the source-defined unit-weight finite causal orientation sums do not remove the frozen local 377-dimensional common-collision ambiguity. It does not select any coefficient, prove that the physical causal vertex fails to exist distributionally, prove regulator dependence/independence, classify generic spins or every collision stratum, establish multivertex E3/E4/E6 closure, G3/F9/G8/K5 promotion, `NEW_PHYSICS_FOUND`, or complete quantum gravity.
