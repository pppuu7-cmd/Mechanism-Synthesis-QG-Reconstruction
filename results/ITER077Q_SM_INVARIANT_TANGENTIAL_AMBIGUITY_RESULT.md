# Iter077Q-SM result — source-compatible K5 extension ambiguity contains an infinite-dimensional tangential subspace

**Date:** 2026-09-14

## Provenance

- Prospective preregistration: `prereg/ITER077Q_SM_INVARIANT_TANGENTIAL_EXTENSION_AMBIGUITY_DIMENSION.md`, commit `df7d9167067d21be7b5ff1fdafa5aa9cea7ac39d`.
- Exact/theorem derivation: `sources/ITER077Q_SM_INVARIANT_TANGENTIAL_AMBIGUITY_DERIVATION.md`, commit `49f262f3fc92dafb368bcdd663fd8e9b05e9e160`.
- Implementation: `distributional/iter077q_sm_invariant_tangential_ambiguity.py`, commit `356e65fa77d83fb95a5cc342ed453a91b2bcded6`.
- Workflow/production head: `.github/workflows/iter077q_sm_invariant_tangential_ambiguity.yml`, commit `242d5d6267ad2c04d7e4aa4dfd69f9876f740450`.
- Authoritative terminal run: `34792482045`.
- Aggregate artifact: `10328598487`, digest `sha256:58e3cb389a985838942a4d0181e6e680cdd75480cfc24e0ec7bb07d73b199a96`.
- Lane artifacts:
  - A `10328304202`, digest `sha256:60cee2a51806cf148cf593391c5f99809848e8d49e7c9d4c1a91612332d28325`;
  - B `10328785637`, digest `sha256:5b63704b195e2333c0450538f30e32d4bc38397e91987eb3c48d526e9d9bc014`;
  - C `10328563653`, digest `sha256:f2085ad7035db1eb88edbb4cbb2d0ee3aefc2b538305b6329ea5e301d2b8e451`;
  - D `10328563655`, digest `sha256:2b388f26d0767ade2f7b208179c5b50ee77b4d53d11dc18b1a6a86025fb53f72`.

All four preregistered lanes are terminal `PASS`; the aggregate is execution-valid. Green CI is not used as the scientific argument: the controlling argument is the exact analytic construction below, with exact symmetry and Vandermonde controls.

## Classification

`ITER077Q_SM_SOURCE_COMPATIBLE_K5_EXTENSION_AMBIGUITY_CONTAINS_INFINITE_DIMENSIONAL_TANGENTIAL_SUBSPACE_EXACT_THEOREM_SCOPED`

Scientific verdict: **PASS** for the preregistered scoped hypothesis.

## Exact construction

The authoritative Iter077L/M chain gives the actual common-collision submanifold

`N = SU(2)^4 subset SL(2,C)^4`

after source gauge fixing, together with at least one nonzero actual-boundary compact functional `F_SU2(y;Psi)` and the supported ambiguity `F_SU2 delta_N`.

Before gauge fixing define on the common-collision set

`Q(g) = sum_(a<b) tr_(1/2)(g_b^-1 g_a)`.

`Q` is exactly invariant under the source common-left `SL(2,C)` action because all relative elements are unchanged. It is exactly invariant under every vertex relabeling because the sum runs over all ten unordered pairs.

On the frozen path

`g_1=g_3=g_4=g_5=I`, `g_2=diag(e^{it},e^{-it})`,

one obtains exactly

`Q(t)=12+8 cos(t)`.

Thus `Q` is nonconstant.

Freeze an actual boundary state `Psi_0` with `F(y)=F_SU2(y;Psi_0)` not identically zero; the independent Iter077M compact-boundary control supplies such states (`16/32` minimal-sector components are nonzero at the identity compact configuration).

Then

`{ Q(y)^n F(y) delta_N(x) : n=0,1,2,... }`

is linearly independent. If a finite relation existed, it would give `P(Q(y))F(y)=0`. On a nonempty open set where `F != 0`, `P(Q)=0`. Since `Q` is real analytic and nonconstant on connected `SU(2)^4`, it cannot be constant on any nonempty open subset; hence `Q` takes infinitely many values there, forcing the polynomial `P` to vanish identically.

Therefore the already source-compatible supported extension space contains at least a **countably infinite-dimensional tangential subspace**, before using any of the additional normal-derivative freedom through order 8 allowed by Iter077L.

## Independent frozen controls

- Lane A: recovered the exact Iter077L/M source/theorem locks, `N=SU(2)^4`, codimension 12, scaling degree 20, smooth coefficient data along `N`, true `F_SU2`, and the independent `16/32` nonzero-boundary witness.
- Lane B: exact rational `SU(2)` controls checked all `120` vertex permutations and a nontrivial common-left transformation; `Q` was unchanged in every case. An absolute-coordinate negative control changed, so the invariance is not a vacuous implementation artifact.
- Lane C: eight prospectively frozen rational `SU(2)` controls gave eight distinct exact `Q` values and a nonzero exact rational Vandermonde determinant. This is an independent finite control only; the infinite-dimensional result comes from the analytic theorem, not extrapolation from eight samples.
- Lane D: support, source ordering, fixed causal labels, true-boundary linearity, common-left gauge covariance, relabeling covariance and transverse scaling-degree locks all pass. No already-frozen source condition was found that restricts the smooth tangential multiplier to a constant.

## Adversarial review

The obvious rescue attempts fail within the frozen source constraints:

1. **Global gauge invariance does not collapse the family:** `Q` is constructed entirely from relative compact elements.
2. **Vertex relabeling does not collapse the family:** `Q` is fully `S_5` invariant.
3. **Boundary-state completeness does not remove the witness:** the multiplier acts on the already-authorized true compact boundary functional; no representative scalar surrogate is substituted.
4. **Scaling degree does not remove the family:** every `Q^n` is smooth and bounded on compact `N`; multiplying `delta_N` by it keeps transverse scaling degree 12, and adding it to an extension of scaling degree 20 remains in the same maximal class.
5. **Source ordering is unchanged:** these are supported extension differences added only after the one-wedge Toller functions and off-collision ten-wedge product are fixed.
6. **The result is independent of the Iter078O control workflow:** no partial or terminal Iter078O value enters this theorem.

A future new condition — e.g. a genuinely source-derived many-vertex composition, cylindrical/RG condition, analyticity/normalization principle, or other law — may reduce this function space. No such selector is imported here.

## New scientific fact

Iter077M's scalar coefficient `c` is not the whole local ambiguity. Under the constraints already present in CRQN v0.2, the fixed-causal K5 local extension is **function-space underdetermined**: there is at least a countably infinite-dimensional source-compatible smooth tangential subspace at normal-derivative order zero alone.

This materially strengthens the local-amplitude blocker. A predictive continuation cannot merely choose or fit one finite-part constant. It must derive a new prospectively motivated principle capable of restricting a tangential function space (and ultimately the higher normal-jet sectors as well).

## Interpretation ceiling

This is not a theorem that no future independently motivated principle can select a unique extension. It is not a full causal-vertex nonexistence/divergence theorem. It does not establish regulator independence, generic-spin behavior, a source-faithful refinement map, RG closure/fixed point, G3, F9/G8/K5 promotion, new physics or complete quantum gravity.

## Exact next admissible step

Before any RG flow or coefficient fit, test whether the causal-Toller construction plus standard spin-foam composition supplies a **source-faithful many-vertex inheritance rule** strong enough to define the minimal two-/few-vertex causal amplitude and act on the tangential coefficient function space. Freeze the 2-complex, causal orientation compatibility, face/edge measure, internal sums, boundary map and extension transport prospectively.

If the causal source does not actually inherit those data uniquely, classify `BLOCKED_MULTI_VERTEX_CAUSAL_OBJECT_DEFINITION`; do not silently import a restricted/EPRL/BF RG prescription. If it does, the next gate is whether that composition map reduces the infinite-dimensional ambiguity or merely propagates it.