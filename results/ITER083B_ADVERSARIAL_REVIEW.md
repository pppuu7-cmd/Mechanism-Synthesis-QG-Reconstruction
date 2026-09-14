# Iter083B-SM adversarial review — filtered boundary-covariant supported ambiguity

Date: 2026-09-15

## RESULT_REVIEWED

Theorem derivation: `sources/ITER083B_SM_FILTERED_BOUNDARY_COVARIANT_SUPPORTED_AMBIGUITY_DERIVATION.md`, commit `8e4d9e5440a2ab3767a5a993350719b6a1351b80`.

Prospective contract: `prereg/ITER083B_SM_FILTERED_BOUNDARY_COVARIANT_SUPPORTED_AMBIGUITY_EXACTNESS.md`, commit `c395c445c0b72ef897d1f7cb2e0bca023d64f4cd`.

Numerical dependency: Iter083A. At the time of this review its independent local exact computation has replicated the preregistered targets, but the GitHub Actions production run has not yet reached a terminal result. Therefore this review may confirm the structural theorem but may **not** promote the numerical value 377 to authoritative production status unless Iter083A subsequently passes.

## SOURCE_OBJECT_CHECK

The primary Bianchi--Chen--Gamonal causal-vertex definition treats the vertex amplitude as a linear functional on spin-network boundary states. For a 4-simplex boundary it uses ten spins and five SU(2) intertwiners, with the common `SL(2,C)` redundancy gauge-fixed by one group element. In the all-`j=1/2` frozen sector each four-valent intertwiner space has dimension two, hence the true boundary intertwiner fiber has dimension `2^5=32`.

A distributional extension of a finite-dimensional vector-valued (equivalently boundary-dual-valued) distribution is componentwise. Two extensions that agree off `N` may differ by an arbitrary `H_boundary^*`-valued distribution supported on `N`, subject to the frozen source symmetries. There is no theorem requiring every supported difference to remain pointwise proportional to Iter077M's one explicit witness `F_SU2`. That witness proved nonuniqueness; it was not a boundary-completeness theorem.

Therefore upgrading from Iter081R's scalar coefficient subspace to the complete frozen `H_boundary^*` coefficient fiber is mathematically legitimate, provided the exact boundary covariance is imposed. Iter083A is precisely the separate character gate for that covariance.

## SOURCE_ORDERING_CHECK

The theorem acts only on differences between local extensions after the exact source ordering

`one-wedge Toller construction -> ten-wedge product -> boundary contraction -> K5 group distribution/extension`.

It does not multiply historical contact terms wedge-by-wedge, interchange a spectral limit with a collision limit, or replace the Toller product by a scalar surrogate.

## DISTRIBUTIONAL_CHECK

The key filtered statement is sound.

For distributions supported on a smooth submanifold, normal derivative order gives a coordinate-independent filtration. Under a change of tubular coordinates, local delta-derivative coefficients mix triangularly, but the top-order quotient is intrinsic. The order-`k` principal symbol is distributional coefficient data on `N` valued in `Sym^k NN` (and the finite boundary dual fiber).

Thus before taking invariants there is an exact sequence whose kernel is precisely order `<=k-1` and whose quotient is the order-`k` normal-symbol bundle. No choice of connection is needed to define the quotient.

The possible objection that an invariant symbol might fail to lift invariantly is rejected by compact averaging. Choose any supported representative with that principal symbol and average over the compact node symmetry and finite relabeling group. Support, normal order, and the invariant top symbol are preserved. Therefore the invariant principal-symbol map is surjective.

This proves the short exact sequence

`0 -> F_{k-1} -> F_k -> G_k -> 0`

in the frozen symmetry class.

## HOMOGENEOUS_SPACE_CHECK

A hidden infinite-dimensional coefficient distribution along `N` would invalidate the finite dimension formula, so this point was checked separately.

The node compact orbit is

`N ~= SU(2)^5 / SU(2)_diag`.

Let `T` be an invariant distributional section of any finite-rank equivariant coefficient bundle over this compact homogeneous space. For a test section `phi`, invariance gives

`T(phi) = T( integral_G g.phi dg )`.

The Haar average is a smooth invariant section. Hence `T` factors through the finite-dimensional averaging projection. Invariant sections are determined by their value at the identity coset subject to isotropy invariance. Therefore no arbitrary tangential function or distribution survives the exact transitive node gauge symmetry.

This argument is stronger than merely assuming smooth coefficient functions.

## ISOTROPY/REPRESENTATION_CHECK

At the identity collision the isotropy is the diagonal compact group, acting on boost normals by spin 1; vertex relabeling acts through the four-dimensional standard representation. This is the upstream Iter081R normal fiber

`V = spin1_SO(3) tensor Std5_S5`.

The boundary fiber is inert under the local node gauge action because the five boundary tensors are SU(2)-invariant intertwiners, while `S5` relabels vertices and induces the corresponding incident-leg permutations. Therefore the degree-`k` invariant symbol space is exactly the Iter083A object

`G_k = (H_boundary^* tensor Sym^k V)^(SO(3) x S5)`.

The normal representation and the frozen S5 boundary characters are real, so dualizing the normal/test-jet convention does not change the multiplicity. This does not license an independent orientation sign.

## DENSITY/JACOBIAN_CHECK

Iter077M and the right-SU2 source-lock review already fix product Haar and the induced quotient/tubular density as invariant under the relevant compact actions. Vertex relabeling permutes identical Haar factors. Since the source integration is density-valued, an orientation reversal does not create a sign character.

Consequently there is no missing determinant twist in the character pairing used by the theorem.

A general nonlinear tubular-coordinate change can still alter lower-order displayed delta coefficients through Jacobian and transition jets. That fact is real but affects a chosen coefficient splitting, not the intrinsic filtered dimension. The theorem deliberately does not claim a canonical coefficient tuple.

## BOUNDARY_COMPLETENESS_CHECK

A potentially stronger objection is that the off-collision source integrand has a specific boundary tensor structure, so perhaps supported extension terms must be proportional to it.

That restriction does not follow from distribution extension theory or from the published boundary-linear source definition. The off-`N` distribution determines an element of `D'(M\N; H_boundary^*)`. The difference of two extensions is any `H_boundary^*`-valued supported distribution satisfying the required symmetries. Requiring proportionality to the off-collision value would itself be an additional selector/normalization condition, and no such condition is frozen in the primary source audit.

Thus Iter077M's `F_SU2 delta_N` is one explicit order-zero witness inside the larger boundary-linear ambiguity, not a proof that the fiber is one-dimensional.

## WAVEFRONT_CHECK

Ordinary conormal admissibility does not reduce the new finite jet space. For every finite normal multi-index `alpha`,

`WF(partial_n^alpha delta_N) subset N^*N \ 0`,

and multiplication by smooth/equivariant finite-rank coefficients does not enlarge the wavefront set beyond the same conormal bundle.

Therefore the narrow `WF(u) subset N^*N\0` condition studied historically cannot by itself select among the finite invariant normal jets. The old Iter080J dependence on Iter077Q's invalid infinite tangential family must not be reused, but its basic conormal mechanism has a repaired finite-jet analogue.

A stronger differential, analytic, spectral or microlocal boundary-value law could still constrain the space; none is manufactured here.

## SCALING_CHECK

`delta_N` has transverse scaling degree 12. A normal derivative of order `k` has scaling degree `12+k`. Upstream source scaling degree is 20, so precisely `k<=8` belongs to the same-scaling-degree ambiguity class. The filtration cutoff is therefore exact within the frozen local theorem.

## CANONICAL_SPLITTING_COUNTEREXAMPLE

Take two tubular/frame extensions agreeing on `N` but differing to first normal order, schematically

`B_A(y,n)=B_0(y)`,

`B_B(y,n)=B_0(y)+n C(y)`.

They define the same order-zero fiber data and the same intrinsic filtration but different displayed first-order coefficient tuples. This confirms that compact averaging cannot be interpreted as discovering a source-selected coefficient basis.

The dimension theorem survives because it uses only the intrinsic exact sequence and invariant principal symbols.

## SELECTOR_CHECK

The exact source audit remains decisive: the causal-vertex paper and Toller companion do not state a joint-K5 finite part, subtraction condition, common K5 regulator, collision boundary-value prescription, or gluing/composition identity that selects supported extension coefficients.

Therefore even an exact finite dimension does not produce a predictive unique local amplitude.

## COUNTEREXAMPLE_ATTEMPTS

1. **Nonlinear coordinate mixing changes the dimension.** Rejected: it is triangular with respect to normal order; the principal quotient and filtered dimension are invariant.
2. **Invariant principal symbols need not lift.** Rejected: compact averaging supplies an invariant lift while preserving the symbol.
3. **Distributional tangential coefficients restore infinite dimension.** Rejected by the homogeneous-space averaging projection under transitive compact node gauge symmetry.
4. **All boundary ambiguities must be proportional to the original compact spin-network witness.** Rejected: that is an extra unsupported selector; finite-dimensional vector-valued extension freedom is componentwise before symmetry projection.
5. **A determinant/sign twist changes the S5 character.** Rejected under source Haar-density conventions; orientation signs are not part of a density transformation.
6. **Conormal wavefront admissibility selects a unique element.** Rejected: all finite normal delta derivatives remain conormal.
7. **The theorem supplies a canonical splitting.** Rejected: it supplies exact dimension and existence of equivariant lifts only.
8. **The theorem supplies the physical selector.** Rejected: source audit still finds none.

## VERDICT

Structural theorem T1--T7:

`CONFIRMED_CONDITIONAL`.

Current numerical classification:

`PROVED_CONDITIONAL_PENDING_ITER083A_PRODUCTION`.

If Iter083A subsequently obtains authoritative production `PASS_EXACT_SCOPED` with

`m=(2,0,5,1,22,10,72,48,217)`,

then this review authorizes promotion, without changing the proof, to

`ITER083B_SM_FILTERED_BOUNDARY_COVARIANT_SUPPORTED_AMBIGUITY_DIMENSION_EXACT_SCOPED`

with

`dim_C F_8 = 377`.

If Iter083A fails scientifically, the structural theorem remains but the number 377 is not authoritative.

## INTERPRETATION CEILING

The theorem is exact only for the frozen all-`j=1/2`, common-K5-collision, boundary-linear, compact-node-gauge/S5-covariant same-scaling-degree supported ambiguity through order 8. It does not classify generic spins, every partial-collision stratum, or a globally patched multistratum vertex, and it does not select a finite part, prove regulator independence, establish multivertex composition, G3/F9/G8/K5, `NEW_PHYSICS_FOUND`, or complete quantum gravity.
