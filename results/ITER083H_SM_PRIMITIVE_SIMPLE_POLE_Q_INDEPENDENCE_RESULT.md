# Iter083H-SM — primitive deepest K5 single simple pole finite part is Q-independent under S5

Date: 2026-09-15
Status: **PASS_EXACT_SCOPED**

## Provenance

- preregistration: `prereg/ITER083H_SM_PRIMITIVE_SIMPLE_K5_POLE_Q_INDEPENDENCE.md`, commit `8a959d565777bd57e5d102c467b140bd618abce0`;
- theorem derivation: `sources/ITER083H_SM_PRIMITIVE_SIMPLE_K5_POLE_DERIVATION.md`, commit `238c3828fd69b01eb8c71d2f25948529f06a8972`;
- validator: `scripts/iter083h_primitive_simple_pole_q_independence.py`, initial commit `7d6f8e062278931f8ce042fc817fdcc37d018563`, pre-production provenance-needle repair `cfd5b83f7f2bd8e0f9e6ee027b01688c322d8583`;
- workflow/head: `.github/workflows/iter083h_primitive_simple_pole_q_independence.yml`, commit `4614ad24ee1f54df1b81b7ce9f473117c28526c1`;
- Actions run `34915559808`, terminal success;
- job `104212300023`, terminal success;
- artifact `10375774823`, `iter083h-primitive-simple-pole-q-independence`;
- artifact ZIP digest `sha256:af944f8616d980e392174dfb218aac5969b97d2e2d1e0195516afac538f6c41c`;
- production JSON SHA256 `409b5ec3467b534eef0d1caeda7c49adfeb31913a4ad7f0dff61022b51dde483`.

The validator needle was corrected before the first production workflow was created; no production failure or scientific criterion repair occurred.

## Classification

`ITER083H_SM_PRIMITIVE_DEEPEST_K5_SINGLE_SIMPLE_S5_POLE_FINITE_PART_Q_INDEPENDENT_SCOPED`

Verdict: **`PASS_EXACT_SCOPED`**.

## Primitive multivariate radial pole

Introduce one regulator per K5 edge,

`x_e=s_e-1`,

and regularize the frozen leading edge factor as `r^(-2s_e)`.

With ten edges, codimension 12 and a normal Taylor term of order n,

`I_n(x)=integral_0^1 r^(11+n-20-2 sum_e x_e) dr`

continues meromorphically to

`I_n(x)=1/(n-8-2L(x))`,

where

`L(x)=sum_e x_e`.

At the physical point x=0 the unique pole in this isolated radial model occurs at

`n=8`,

and is

`I_8(x)=-1/(2L(x))`.

Production checked Taylor orders 0 through 16 and found exactly one physical-point pole order: `[8]`.

## Why invariant Q cannot affect this one-pole finite part

Iter083G gives the regulator representation

`E=[5]+[4,1]+[3,2]`

and the full invariant metric family

`Q=aI+bA+cB`.

The pole covector L is the unique S5-invariant line. Production verifies the basis matrices act on the all-ones vector with exact eigenvalues

`I:1`, `A:6`, `B:3`.

Therefore every S5-invariant nondegenerate Q preserves the same splitting

`E* = span(L) direct_sum ([4,1]+[3,2])`.

Equivalently,

`L^(perp,Q*)=[4,1]+[3,2]`

for every invariant Q, even though Iter083G proved that the three Q-sector eigenvalues themselves are not fixed by S5.

## True boundary-valued numerator — no scalar surrogate

The authoritative boundary representation is

`H_boundary^*=2[5]+[4,1]+2[3,2]+2[2,2,1]+[2,1,1,1]+2[1^5]`,

with complex dimension 32.

Hence

`dim Hom_S5(E,H_boundary^*) = 2+1+2 = 5`.

Production preserves all five regulator-linear channels:

- 2 from the trivial regulator input [5];
- 1 from [4,1];
- 2 from [3,2].

Thus there are 3 genuine nontrivial-regulator linear channels, and the theorem does not obtain Q-independence by scalarizing the boundary object.

## Exact finite-part statement

For an S5-equivariant holomorphic boundary-valued numerator

`h(x)=h_0+h_1(x)+h_2(x)+...`,

consider the simple germ

`h(x)/L(x)`.

The holomorphic projection behaves degree-by-degree as follows:

- `h_0/L` is pure polar and contributes zero after projection/evaluation;
- the trivial-regulator component of `h_1` has form `L C`, so division by L gives the constant C;
- the 3 nontrivial-regulator linear channels lie in the common Q-independent orthogonal complement of L and remain polar, contributing zero to the evaluated constant;
- for every homogeneous degree `m>=2`, any holomorphic term created by cancelling one L has degree at least one and vanishes at x=0; uncancelled terms remain polar.

Therefore

`ev_0 pi_Q(h/L)=C`

for every nondegenerate S5-invariant Q.

The evaluated finite part of this isolated single simple overall pole is exactly Q-independent.

## What this changes after Iter083G

Iter083G correctly showed that S5 symmetry leaves a three-sector family of regulator metrics and therefore does not make a generic Q-based projection unique.

Iter083H now proves a stronger special fact: **that Q freedom is harmless for the isolated primitive deepest K5 one-simple-pole channel**.

Thus one should not search for regulator-metric dependence in the overall simple pole again.

Any actual Q dependence must come from structure absent here, especially simultaneous independent pole forms from nested K3/K4/K5 collisions, higher pole multiplicity, or additional nontrivial regularization data.

## Nested-pole firewall

Production explicitly retains two independent proper-subgraph covectors (two different K3 triangles) as a witness that multiple-pole geometry exists outside the theorem.

No claim is made about a germ of the form

`h/(L_1 L_2 ... L_r)`

with `r>=2`.

The next nonredundant gate is therefore the exact resolved forest pole geometry.

## Controls

All P0–P7 and all eight controls passed. The gate rejects:

- replacing the true boundary representation by a scalar;
- pretending all five equivariant linear maps come from the trivial regulator input;
- a non-S5-invariant Q mixing the trivial line with the sum-zero subspace;
- promoting a one-pole theorem to multiple poles;
- promoting it to higher pole order without proof;
- promoting it to the global K3/K4/K5 forest renormalization problem.

It retains both the possibility of nested-pole Q dependence and the possibility that a stronger locality/functoriality principle fixes Q before projection.

## Interpretation ceiling

No full K5 meromorphic continuation theorem; no all-strata renormalization theorem; no claim that the complete K5 amplitude is Q-independent; no generic-spin theorem; no regulator independence; no unique physical selector; no G3/F9/G8/K5 promotion; no `NEW_PHYSICS_FOUND`; no complete-QG claim.