# Prospective preregistration — K5 invariant-dual degree-27 canonical numerator-DAG materialization

Date: 2026-09-16

Parent exact authority: `results/K5_ORDER8_INVARIANT_DUAL_PROJECTIVE_IBP_REACHABILITY_RESULT.md`, commit `e9ed372a91ac1bd219dc7671a916c70405e9cd43`.

Outcome-independent object audit: `sources/K5_INVARIANT_DUAL_DEG27_NUMERATOR_MATERIALIZATION_AUDIT.md`, commit `ecebc3670c63fe877e2ec5eddd84bc36252b3430`.

This gate is frozen before implementation/production inspection. It is independent of the terminal verdict of the separately running degree-four annihilator Critic. No result from that Critic is required to define the present numerator objects.

## Scientific/object question

Materialize the two actual full-all-32 S5-invariant **dual/covector** K5 order-eight numerator channels `N_1(alpha),N_2(alpha)` as deterministic reusable exact algebraic objects suitable for later projective-IBP differentiation.

A fully expanded sparse degree-27 coefficient table is not required if it is combinatorially inefficient. A canonical exact DAG is admissible only if its nodes, ordering, coefficients and evaluation semantics are completely fixed and hashable, and if independent exact evaluation controls establish that it represents the same two source-authorized numerator polynomials.

## Frozen source object

Use only the already-authorized all-`j=1/2` leading K5 source object:

- source edge order `(01),(02),(03),(04),(12),(13),(14),(23),(24),(34)`;
- exact leading edge-entry linear coefficients reconstructed from `distributional/iter077i_sm_source_ordered_jhalf_k5_l1.py`;
- all 32 boundary intertwiner components and all `100000=(4+6)^5` source node-choice terms;
- exact 32D boundary S5 action reconstructed from the stripped node tensors;
- exact dual/covector Reynolds projection `P^T`, with boundary character `(32,0,8,2,0,0,2)`, rank two, RREF pivots `(1,4)`;
- weighted reduced K5 Laplacian `L(alpha)` and `Psi_K5(alpha)=det L(alpha)`;
- source quadratic radius matrix `Q=L_uniform/5`, equivalently `R_K5^2=(1/5) sum_(a<b)|x_a-x_b|^2` in the common-left gauge;
- order-eight insertion `(R_K5^2)^4` realized exactly as the fourth derivative at `s=0` of the Gaussian family with `L(alpha)+s Q`.

For a boundary component source polynomial `P(y)` of Cartesian degree ten, the normalized exact radial moment is

`J_4(alpha) = [d^4/ds^4]_{s=0} { [det(L+sQ)/det L]^(-3/2) Wick_P[(L+sQ)^(-1)] }`.

Every term has total inverse-L degree nine. The canonical polynomial numerator is therefore

`N(alpha) = Psi_K5(alpha)^9 J_4(alpha)`,

which must be homogeneous degree 27. The physical projective integrand remains

`Omega_9 * prod_e alpha_e^(1/2) * N(alpha) / Psi_K5(alpha)^(21/2)`

up to the already-tracked common nonzero source normalization.

## Required canonical DAG

The production artifact must deterministically encode at least:

1. edge order and reduced incidence rows;
2. the 125-term coefficient-one `Psi_K5` polynomial;
3. all 4x4 polynomial adjugate entries of `L(alpha)` or an exactly equivalent cofactor representation;
4. all edge-pair covariance numerators `G_ef(alpha)=r_e^T adj(L) r_f` required by the Wick engine;
5. the rational 4x4 source-radius matrix `Q`;
6. the four source matrix-entry linear coefficient triples derived from the authoritative source module;
7. the exact two-row invariant dual basis / Reynolds data and pivots;
8. a fixed recurrence for inverse series `(L+sQ)^(-1)` through order four and determinant-ratio series through order four;
9. the fixed source-Wick pairing recursion over ten edge factors;
10. the rule `N_c=Psi^9 * J_{4,c}` after full-all-32 contraction and dual projection.

The canonical serialization must have a reported SHA256 digest.

## Frozen validation points

Use exact rational arithmetic at exactly these three positive Schwinger points:

- `uniform=(1,1,1,1,1,1,1,1,1,1)`;
- `edge01_2=(2,1,1,1,1,1,1,1,1,1)`;
- `mixed_small=(1,2,1,3,1,2,1,1,2,1)`.

No point may be changed after production output.

## Mandatory acceptance checks

A valid materialization must establish all of the following:

1. exact K5 tree/determinant equality with 125 coefficient-one degree-four monomials;
2. exact `Q=L_uniform/5` and the source-radius identity;
3. full 32 boundary components and exactly 100000 raw source node-choice terms at every production evaluation;
4. exact boundary character `(32,0,8,2,0,0,2)`, Reynolds rank two and pivots `(1,4)`;
5. dual projection differs from vector projection in the stripped basis;
6. at `uniform`, the new generic radial-series evaluator reproduces the pre-existing independently validated all-32 boundary moment exactly, not just its projection;
7. at `uniform`, the dual coordinates reproduce exactly `(-9225216/9765625,-7175168/9765625)`;
8. at `edge01_2` and `mixed_small`, the new full-all-32 evaluator's `00000` component agrees exactly with the independently existing `scripts/k5_order8_nonuniform_schwinger_sign_diagnostic.py` evaluator using the same frozen radial insertion;
9. the two numerator values obtained as `Psi^9 J_4` obey exact degree-27 scaling under the control rescaling `alpha -> 2 alpha` at `edge01_2`;
10. the serialized DAG evaluates exactly to the same two projected numerator values as the direct rational evaluator at all three frozen points;
11. the two channels are not replaced by the representative `00000` component or by vector projection;
12. no integrated-period zero/nonzero verdict is emitted.

## Mandatory malformed controls

The same validator must reject or detect:

- omission of one boundary component;
- omission of one Toller edge;
- vector Reynolds projection substituted for dual projection;
- `Q` replaced by the identity or any matrix not equal to `L_uniform/5`;
- wrong `Psi` tree count or determinant;
- order-eight derivative replaced by a lower derivative;
- numerator clearing power other than `Psi^9`;
- promotion of a single exact point value to an integrated-period theorem.

## Frozen outcomes

Return exactly one:

- `K5_INVARIANT_DUAL_DEG27_CANONICAL_DAG_MATERIALIZED_EXACT_SCOPED` iff the canonical DAG is deterministic/hashable and all exact controls above pass;
- `K5_INVARIANT_DUAL_DEG27_MATERIALIZATION_BLOCKED_RESOURCE_SCOPED` iff the source object is exact but the full-all-32 exact evaluation/materialization cannot be completed within the frozen computational envelope without changing the representation;
- `INVALID_IMPLEMENTATION`, `INVALID_PROVENANCE`, or `INFRASTRUCTURE_FAILURE` for non-scientific failures.

A resource blocker is not a scientific zero and must not be converted into a smaller representative-component object.

## Interpretation ceiling

This gate only materializes the two exact numerator objects. It does not evaluate their projective integrals, does not prove either period zero/nonzero, does not reduce the full 217-dimensional K5 tensor, does not reduce the 377-dimensional extension freedom, and does not select a physical finite part.
