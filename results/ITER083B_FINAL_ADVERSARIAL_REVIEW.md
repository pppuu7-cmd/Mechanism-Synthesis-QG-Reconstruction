# Iter083B-SM final adversarial review — exact filtered 377-dimensional supported ambiguity

Date: 2026-09-15

## RESULT_REVIEWED

Final result: `results/ITER083B_SM_FILTERED_BOUNDARY_COVARIANT_SUPPORTED_AMBIGUITY_RESULT.md`, commit `6457ff6d94bf9adff71bcd5fd6b63d1f346ada0a`.

Prospective theorem preregistration: `c395c445c0b72ef897d1f7cb2e0bca023d64f4cd`.

Pre-numerical theorem derivation: `8e4d9e5440a2ab3767a5a993350719b6a1351b80`.

Conditional adversarial review: `536c3b9bb50aac014779eb19144dd107c21df11c`.

Numerical dependency Iter083A: production `PASS_EXACT_SCOPED`, result `4a56e325dad2c42f5ab7566c0e2f91d585cf4c9e`, adversarial confirmation `8c75e5ca96728d11091c8f22a69b4a4d6d766f86`.

## PROSPECTIVE_DISCIPLINE_CHECK

The short-exact-sequence theorem, homogeneous-space finiteness argument, density convention, adversarial controls and interpretation ceiling were all frozen before Iter083A production supplied an authoritative numerical sequence. The final result therefore does not reverse-engineer a proof to fit 377; it inserts the later confirmed values into the preregistered identity

`dim F_8 = sum_k dim G_k`.

## FILTRATION_CHECK

The definition of distributions supported on `N` of normal order at most `k` is intrinsic. A change of tubular coordinates can mix lower-order delta-derivative coefficients but cannot change normal order or the top principal-normal-symbol quotient.

Therefore noncanonicity of a coefficient tuple is not a counterexample to the dimension theorem.

## EXACT_SEQUENCE_CHECK

Before invariants, order-`k` supported distributions modulo order `k-1` are the corresponding normal-symbol distributional sections. Taking the frozen compact symmetry class preserves exactness on the right because any invariant symbol can be lifted and compact-averaged.

Averaging preserves support, order and the invariant top symbol, so the map onto

`G_k=(H_boundary^* tensor Sym^k V)^(SO(3) x S5)`

is surjective.

The kernel is exactly lower normal order. Hence

`0 -> F_(k-1) -> F_k -> G_k -> 0`

is sound.

## TANGENTIAL_FINITENESS_CHECK

The strongest possible objection to the finite count is a hidden infinite-dimensional distributional coefficient space along `N`. The compact node action is transitive on

`N ~= SU(2)^5/SU(2)_diag`.

For an invariant distributional section, testing against `phi` is equivalent to testing against its Haar average. The averaging operator has finite-dimensional invariant image, identified with isotropy-invariant fiber data. Hence no arbitrary tangential distribution survives.

This conclusion does not rely on assuming coefficient smoothness.

## DENSITY_AND_DUAL_CHECK

Upstream source geometry uses invariant product Haar and induced tubular densities. Vertex relabeling permutes identical density factors. No orientation determinant character is therefore missing from the S5 pairing.

The normal representation is real orthogonal/self-dual, so switching between normal and conormal/test-jet dual conventions does not change the multiplicities. This self-duality is separate from the density argument.

## BOUNDARY_COMPLETENESS_CHECK

The true frozen boundary coefficient space is 32-dimensional. Distribution extension is componentwise before symmetry projection. Nothing in the published source requires every supported extension difference to remain proportional to Iter077M's one explicit compact spin-network witness.

Such proportionality would itself be an additional selector condition. Therefore consuming the full Iter083A boundary-dual character is legitimate.

## NUMERICAL_CHECK

Authoritative Iter083A gives

`dim G_k = (2,0,5,1,22,10,72,48,217)`.

Their exact sum is

`377`.

The scalar 28-dimensional Iter081R result embeds only as a restricted invariant subspace and cannot be substituted for the full boundary-covariant problem.

## WAVEFRONT_CHECK

Finite normal derivatives of `delta_N` remain conormal. Ordinary support plus `WF(u) subset N^*N\0` therefore does not remove the 377-dimensional frozen space. A stronger analytic/differential/microlocal law could still do so, but none is imported.

## SELECTOR_CHECK

Exact dimension does not provide coefficients. The primary source audit remains unchanged: no joint K5 finite part, common regulator, collision boundary-value law, subtraction normalization or gluing/composition identity is stated that selects a point in the resulting affine family.

Iter083C further establishes that the complete hierarchy of additive identities derived from `T^+ + T^- = D` also has a nonzero supported nullmode. Thus one especially natural source consistency candidate does not supply the missing selection law.

## COUNTEREXAMPLE_ATTEMPTS

1. **Nonlinear transition jets destroy 377.** Rejected: they change a splitting, not the intrinsic filtered quotients or dimensions.
2. **Invariant symbols fail to lift.** Rejected by compact averaging.
3. **Distributional coefficients along N are infinite-dimensional.** Rejected by transitive homogeneous-space averaging.
4. **Boundary extension differences must be proportional to one source witness.** Rejected as an extra unsupported selector condition.
5. **Orientation/Jacobian produces an uncounted sign twist.** Rejected under invariant density conventions.
6. **Odd orders contradict scalar symmetry.** Rejected: they are representation-valued boundary-covariant channels confirmed by exact S5 representation theory.
7. **377 means 377 physical parameters have been measured/selected.** Rejected: they are ambiguity directions, not fixed physical values.
8. **377 is globally complete.** Rejected outside the frozen all-j=1/2 common-collision sector.

## VERDICT

`CONFIRMED_SCOPED`

Final authoritative classification:

`ITER083B_SM_FILTERED_BOUNDARY_COVARIANT_SUPPORTED_AMBIGUITY_DIMENSION_EXACT_SCOPED`

with

`dim_C F_8 = 377`.

## CONTROLLING LOCAL BLOCKER

The frozen common-collision ambiguity is now **classified rather than object-definition blocked**. The remaining blocker is selection:

`JOINT_K5_BOUNDARY_VALUE / COMMON_REGULATOR / COMPOSITION_NORMALIZATION_SELECTOR_MISSING`.

A preferred local coefficient splitting may still be useful for explicit formulas, but it is no longer a prerequisite for knowing the intrinsic ambiguity dimension.

## INTERPRETATION CEILING

No generic-spin completeness, all-strata global extension, regulator independence, causal-vertex divergence/nonexistence, multivertex closure, G3/F9/G8/K5 promotion, `NEW_PHYSICS_FOUND`, or complete-QG result follows.
