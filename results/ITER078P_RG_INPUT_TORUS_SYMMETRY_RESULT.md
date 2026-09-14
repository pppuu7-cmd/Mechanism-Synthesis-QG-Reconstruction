# Iter078P-RG result — exact one-dimensional multiplicative input symmetry explains the structural rank-31 control map

**Date:** 2026-09-14

## Provenance

- Prospective preregistration: `prereg/ITER078P_RG_INPUT_TORUS_SYMMETRY.md`, commit `3e2a2f02e6f1feeb602ab34aa2b970012b6b9704`.
- Implementation: `distributional/iter078p_rg_input_torus_symmetry.py`, commit `c4aa5a9fb053519e4cd52de3edbbdf9704468257`.
- Workflow/production head: `.github/workflows/iter078p_rg_input_torus_symmetry.yml`, commit `ef8dd11eb36b66396bf7800a21544c1df58de451`.
- Authoritative run: `34791349154`.
- Aggregate artifact: `10329295589`, digest `sha256:0c1665388736522393d755913e75873b356af7eedfbd9b0e8cb9df1126707813`.
- Lane artifacts:
  - A `10329231978`, digest `sha256:74f2fb5e85236b6fafc4a017743900908d92987a990d3cdbf8fa18609d9d7fd0`;
  - B `10329114152`, digest `sha256:d022f71f9a7bcdb6b76b78de30c3018444751971344911416977d22577b8b5d0`;
  - C `10329109861`, digest `sha256:c06a1be6f5d40b8b46d31c3cc6f69cbdac46597fc54e3d8f297cc3ee461c0b0`;
  - D `10329230459`, digest `sha256:d70c8309d46c9dcd9517e3154b1852558d2986284eb88217881b887e0760b586`.

## Classification

`ITER078P_RG_FIXED_JHALF_1TO5_CONTROL_HAS_EXACT_INPUT_TORUS_SYMMETRY_STRUCTURAL_JACOBIAN_KERNEL_SCOPED`

Scientific verdict: **PASS**.

## Exact charge theorem

For every one of the `32*2^10=32768` raw degree-5 contraction configurations, form the 32-component exponent-count row recording how many times each local tensor component appears in that monomial.

The exact charge matrix has

- rank over `Q`: `31`;
- nullity: `1`.

A primitive integer basis of its nullspace is

`q = (1,0,-1,0,0,-1,-2,-1,-1,-2,-3,-2,-2,-3,-4,-3,0,-1,-2,-1,-1,-2,-3,-2,-1,-2,-3,-2,-2,-3,-4,-3)`.

(The basis vector is stored in the authoritative aggregate artifact; this result records the same primitive normalization.)

For every raw monomial exponent row `m`,

`m·q = 0`

exactly. Therefore the complete polynomial map obeys the finite identity

`R(z^q ⊙ C) = R(C)`

for every formal/nonzero multiplicative parameter `z` for which the coordinate rescaling is defined.

This is coefficientwise and does not depend on point sampling.

## Exact Jacobian consequence

Differentiating the finite symmetry gives

`J(C) (q ⊙ C) = 0`.

At the prospectively frozen generic points A/B/C:

- Jacobian rank is `31`;
- nullity is `1`;
- the generated vector `q⊙C` is nonzero;
- it spans the full exact Jacobian kernel.

Hence the repeated rank-31 result of Iter078M is structural, not an accident of the four samples.

On the compact tensor `L`, `q⊙L=0` identically. Therefore the torus orbit is stationary at `L`, and the distinct rank-31 null direction classified in Iter078J is a special singular-point kernel rather than the generic torus generator. Iter078J's quadratic lifting is fully compatible with the exact global torus invariance.

## Global rank statement

On the Zariski-open region where `q⊙C != 0`,

`rank J(C) <= 31`.

The A/B/C controls saturate this bound exactly, so the generic rank of the frozen polynomial control map is `31` on at least a nonempty open subset compatible with the exact symmetry.

## Scientific meaning

The fixed-spin pure order-zero tensor-network parameterization has a genuine one-dimensional multiplicative redundancy. Iter078N correctly found no fixed output hyperplane because the structural degeneracy lives in **input coordinates**, not as a universal linear relation among outputs.

This is a redundancy of the control-map coordinates. It must not be promoted automatically to a gauge symmetry of the physical causal-Toller extension space.

In particular, a coarse/fine fixed-point equation such as `R(C)=lambda C` can still constrain the torus direction because the coarse tensor on the right-hand side transforms while `R(C)` does not. The symmetry explains the rank of `R` itself; it does not by itself reduce the rank of the full coarse-minus-fine consistency equations.

## Interpretation ceiling

This theorem is restricted to the frozen labelled all-`j=1/2`, pure order-zero 1-to-5 tensor-network control. It does not establish a physical CRQN gauge redundancy, a unique extension, an RG fixed point, regulator independence, generic-spin closure, G3 or complete QG.

## Exact next admissible step

Use the exact quotient structure rather than further raw Jacobian sampling. For the fixed-spin control, formulate projective/coarse-fine consistency on the 31-dimensional torus quotient (plus overall normalization), and test exact fixed rays or selector equations there. In parallel, continue the independent causal-stabilizer symmetry reduction of the labelled boundary space; the two reductions answer different questions and should not be conflated.