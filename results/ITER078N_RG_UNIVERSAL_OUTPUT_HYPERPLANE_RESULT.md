# Iter078N-RG result — repeated rank 31 is not explained by a universal linear output hyperplane

**Date:** 2026-09-14

## Provenance

- Prospective preregistration: `prereg/ITER078N_RG_UNIVERSAL_OUTPUT_HYPERPLANE.md`, commit `03db4f6400ab04ade810972f6d5eaf929abe489b`.
- Implementation: `distributional/iter078n_rg_universal_output_hyperplane.py`, commit `7856e1cda12ae4616f2990c95968703411b7e395`.
- Workflow/production head: `.github/workflows/iter078n_rg_universal_output_hyperplane.yml`, commit `23ad481d6b86fa3c93a891160bff28ab1b860994`.
- Authoritative run: `34791220947`.
- Aggregate artifact: `10327687626`, digest `sha256:d03983013876037fd409be9c0b617cd170a87be7341667601d14e6a100fa1006`.
- Lane artifacts:
  - A `10328661547`, digest `sha256:fb5a3632ed7a12159bb8e03bca6dd3209048778e9128c530ce8748eabb5cca07`;
  - B `10327598064`, digest `sha256:fbefd7d3133bb4de507f1e2a136bb2c2f0e5b1495e489d4fa46179fe8827f2f7`;
  - C `10327798678`, digest `sha256:567e8559787bc161754ff004b2dd54a6f4ac7b07619786358466e73829b917e7`;
  - D `10328046995`, digest `sha256:06bd41818eab6f48a388b136e5433107b0016d9fca66e2944854e56c2d3bae53`.

## Classification

`ITER078N_RG_NO_COMMON_LEFT_NULL_ACROSS_FROZEN_RANK31_POINTS`

Scientific verdict: **INCONCLUSIVE_STRUCTURAL_RANK**.

## Exact findings

For the EPRL-edge-weight fixed-spin map, the exact primitive left-null vectors of the rank-31 Jacobians at the four frozen points A/B/C/L are **different**, not one common proportional vector.

Therefore no candidate common `w` exists from the frozen points and the prospectively specified coefficientwise identity test `w·R(C)≡0` is not applicable. No universal linear output hyperplane is established.

The frozen simple-character catalogue also yields no common candidate.

The independent unit-edge-weight control gives the same qualitative outcome: its left-null vectors across A/B/C/L are also different.

## New scientific fact

The repeated exact rank-31 Jacobians of Iter078M are not explained by a fixed linear conservation law on the 32 output components. Any structural rank ceiling, if present, must be nonlinear or arise from an input-space redundancy/symmetry rather than a universal output hyperplane of the tested form.

## Interpretation ceiling

This result does not prove generic rank 32 and does not prove a structural rank-31 ceiling. It only falsifies the simplest universal-left-null explanation under the frozen exact test.

## Exact next admissible step

Test an input-space multiplicative symmetry directly from the tensor-network monomials. Seek nonzero charges `q_i` such that for every one of the `32*2^10=32768` degree-5 contraction configurations,

`sum_(five local factors) q_(component index) = 0`.

Any such exact charge vector generates

`C_i -> exp(t q_i) C_i`

under which every monomial, and hence the full map, is invariant. Then `J(C)(q_i C_i)=0` wherever that generator is nonzero, giving an exact structural right-kernel and global rank ceiling without relying on point sampling.