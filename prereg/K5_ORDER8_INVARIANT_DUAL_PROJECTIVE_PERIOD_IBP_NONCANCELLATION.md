# Prospective preregistration — K5 order-8 invariant-dual projective period / IBP noncancellation gate

Date: 2026-09-16

This gate is frozen after terminal rank-two sign-change result `d01790ed11881c31ca5d7c6119fa40d90bff1368` and before implementation/production inspection of the invariant-dual projective-period calculation.

No criterion below may be weakened or fitted after production output.

## Scientific question

For the already source-authorized frozen all-`j=1/2` K5 order-eight principal-symbol object, what are the two scalar projective periods obtained by the exact two-dimensional S5-invariant **dual/covector** boundary projection? Can exact projective parameter-space IBP, graph symmetry, annihilators, hyperlogarithmic reduction, or another rigorous certificate prove at least one period nonzero or prove both invariant periods zero?

This is the first gate after the exact rank-two sign change killed the global pointwise-positivity strategy. No higher-rank pointwise-positivity family is an admissible substitute.

## Frozen source/object construction

A valid implementation must simultaneously satisfy:

1. reconstruct the exact 32D boundary S5 action directly from the authoritative stripped `k=0/k=1` node tensors and induced incident-leg permutations;
2. independently recover boundary character `(32,0,8,2,0,0,2)` and Reynolds rank two;
3. treat the amplitude as a boundary **covector**: invariant channels use the dual action / transposed Reynolds projector. A vector-space Reynolds projection is not an admissible replacement because the stripped local basis is not orthonormal;
4. retain the complete all-32 boundary contraction and all ten source leading Toller wedges before projection; no `00000` representative-component substitution;
5. use the exact K5 Schwinger/projective reduction with ten positive Schwinger variables and the exact reduced weighted Laplacian;
6. independently recover the K5 Kirchhoff polynomial as the degree-four determinant with exactly 125 spanning-tree monomials of coefficient one;
7. use the exact order-eight radial insertion. After 12D Gaussian contraction the scalar dual channel must be represented projectively in the form

   `Omega_9 * [product_e alpha_e^(1/2)] * N_c(alpha) / Psi_K5(alpha)^(21/2)`

   up to an explicitly tracked common nonzero source normalization, where `N_c` is homogeneous degree 27 and `Psi_K5=det L` is homogeneous degree 4. Equivalent exact representations are allowed only if projective degree zero is verified;
8. preserve the already-confirmed 16-parameter meromorphic-family provenance. The common Schwinger scale is a computational Mellin/radial coordinate, not a one-parameter physical regulator;
9. keep published one-wedge spectral `i epsilon` unchanged and do not introduce `beta+i epsilon`;
10. retain the primitive-face authority from exact-zero K3/K4 collision residues, but do **not** identify Schwinger-simplex boundary faces `alpha_e=0` with K3/K4 collision faces. Any projective IBP boundary term must be checked on its own terms.

## Projective IBP authority lock

External mathematical guidance may use parameter-space/projective IBP identities, including the projective-form framework of Artico–Magnea, arXiv:2310.03939 / JHEP 03 (2024) 096, where Feynman-parametric integrands are treated as projective forms and exterior differentiation generates parameter-space IBP relations.

This literature is methodological authority only. It does not by itself evaluate the K5 period, authorize dropping boundary terms, or supply a physical renormalization prescription.

For this gate an IBP identity is admissible only if:

- projective homogeneity is exact;
- every generated numerator/denominator shift is tracked exactly;
- any boundary contribution on `alpha_e=0` is either proven zero for the actual K5 integrand/vector field or retained explicitly;
- graph/S5 symmetry relations are proven from the exact K5 edge action;
- no numerical fit is used to infer an exact relation.

## Frozen primary outcomes

Return exactly one scoped classification:

- `K5_INVARIANT_DUAL_PROJECTIVE_PERIOD_NONZERO_EXACT_SCOPED` if at least one of the two invariant-dual periods is rigorously proved nonzero by an exact identity/evaluation or a rigorous exact-sign/noncancellation certificate over the full projective domain;
- `K5_INVARIANT_DUAL_PROJECTIVE_PERIODS_BOTH_ZERO_EXACT_SCOPED` only if both invariant-dual periods are structurally proved zero over the complete projective domain;
- `K5_INVARIANT_DUAL_PROJECTIVE_OBJECT_DEFINED_IBP_REDUCTION_INCOMPLETE_SCOPED` if both exact dual projective integrands are fully defined and validated but the available exact IBP/symmetry/annihilator system does not yet decide either nonzero or both-zero;
- `K5_INVARIANT_DUAL_PROJECTIVE_PERIOD_BLOCKED_OBJECT_DEFINITION` if an indispensable source/projective object is genuinely missing;
- `INVALID_IMPLEMENTATION`, `INVALID_PROVENANCE`, or `INFRASTRUCTURE_FAILURE` for non-scientific failures.

Do not convert an incomplete IBP basis into a scientific zero or nonzero claim.

## Mandatory adversarial controls

The same validator must reject at least:

- invariant **vector** projection substituted for the dual/covector projection;
- representative `00000` component substituted for all-32 projection;
- one omitted Toller edge;
- a corrupted local node-tensor normalization;
- wrong boundary character or Reynolds rank;
- wrong K5 tree count / determinant polynomial;
- omitted `product alpha_e^(1/2)` Schwinger weight;
- wrong denominator exponent instead of `21/2`;
- numerator degree other than 27;
- non-projective total degree;
- an IBP relation that silently discards a non-proven boundary term;
- one-parameter Schwinger scale promoted to a physical regulator;
- pointwise witness or finite sampling promoted to a projective-period theorem;
- inference of a full 217-dimensional K5 tensor zero from vanishing of the two invariant periods.

A synthetic projective fixture with a known exact nonzero period and a synthetic exact-zero/total-derivative fixture must traverse the same decision machinery.

## Interpretation ceiling

A nonzero invariant-dual period is an exact nonzero witness for the K5 order-eight principal-symbol tensor, but does not by itself determine the complete 217-dimensional tensor rank/annihilator or select a physical finite part. If both invariant periods vanish, the remaining S5 sectors still have to be tested before any full K5 zero theorem.

No physical finite-part selector, regulator independence, global all-strata patching, causal multivertex dynamics, G3/F9/G8 promotion, `NEW_PHYSICS_FOUND`, or complete-QG claim follows from this gate.