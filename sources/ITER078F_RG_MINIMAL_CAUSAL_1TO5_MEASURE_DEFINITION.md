# Iter078F-RG definition — versioned minimal causal 1-to-5 measure/embedding skeleton

**Date:** 2026-09-14

Prospective contract: `prereg/ITER078F_RG_MINIMAL_CAUSAL_1TO5_MEASURE_PROPOSAL.md`, commit `d2778fe40876c7dde8318ce3326fcd8a8fd6a33f`.

## External measure authority and what is new

Donà-Frisoni's standard Lorentzian EPRL state sum is

`Z_Delta = sum_{j_f,i_e} prod_f (2j_f+1) prod_e (2i_e+1) prod_v A_v(j_f,i_e)`

in the convolution convention used in their practical construction. The face and edge weights are fixed there by the correct fixed-boundary convolution property.

Bianchi-Chen-Gamonal define the causal local vertex by replacing the EPRL Wigner matrices inside a single Lorentzian 4-simplex vertex with source-ordered Toller functions and state that a causal spin-foam path integral also sums over edge orientations. Their paper explicitly studies one vertex and does not define the multi-vertex measure.

Therefore this construction makes one new, versioned choice:

**retain the standard EPRL convolution face/edge measure and replace only the local vertex kernel by the causal-Toller vertex.**

This is `CRQN v0.3-R0 (MEASURE_PROPOSAL_ONLY)`, not a recovered fact about v0.2.

## Minimal 1-to-5 amplitude skeleton

Let `Delta_1` be the coarse single-4-simplex 2-complex and `Delta_5` its Iter078B interior-vertex `1->5` refinement. The external triangulated boundary is identical, so

`H_boundary(Delta_1)=H_boundary(Delta_5)`

and the boundary embedding map is exactly the identity in the same spin-network labeling convention.

For one fixed compatible fine causal orientation `Sigma` from the Iter078B set, define the orientation-resolved fine skeleton

`Z_Delta5^Sigma[Psi; A]`

by:

1. fixing the external boundary spins/intertwiners from `Psi`;
2. summing every internal face spin `j_f` and internal edge intertwiner `i_e`;
3. inserting `A_f(j_f)=2j_f+1` for every internal face and the corresponding fixed-boundary factors required by the EPRL convolution convention;
4. inserting `A_e(i_e)=2i_e+1` for every internal edge in that convention;
5. at each of the five fine 4-simplices inserting the fixed-causal Toller vertex with the local edge signs induced by `Sigma`;
6. removing one redundant `SL(2,C)` group integration inside each local vertex exactly as in the single-vertex source convention;
7. contracting all shared internal boundary representation/intertwiner indices according to the refined 2-complex.

This defines the **measure/embedding skeleton**, provided each local causal vertex is itself supplied as a distributional linear functional.

## Orientation handling

Iter078B proves all 32 coarse causal boundary patterns admit compatible acyclic fine orientations. This definition is orientation-resolved and therefore does not invent a relative weight among the compatible orientations.

A future causal path-integral sum

`sum_Sigma w(Sigma) Z_Delta5^Sigma`

requires a separately frozen rule for `w(Sigma)`. The generic statement that causal spin foams sum over edge orientations is not sufficient to infer a nontrivial weighting law.

## Local extension family

At each fine vertex write only schematically

`A_v = A_ref,v + Delta_v`,

where `A_ref,v` is one reference same-scaling-degree extension of the exact source-ordered off-collision Toller object and `Delta_v` is a supported extension difference.

No reference extension is selected by this measure gate. No component of `Delta_v` is set to zero.

Iter078E proves that, already after integration in the controlling all-`j=1/2` sector, the order-zero ambiguity image has complex dimension at least 32. Hence a one-parameter `cL` ansatz is only a diagnostic truncation and is not part of the v0.3-R0 definition.

## EPRL limit control

If every local Toller matrix is formally replaced by its ordinary EPRL Wigner matrix and the local distributional extension issue is removed, the skeleton is exactly the standard EPRL state-sum skeleton in the frozen convolution convention. Thus the new structure modifies the local causal vertex while preserving the independently established coarse/fine measure convention.

## BF comparator firewall

The local supported tensor identified in Iter078C is a BF 15j tensor. However, BF Pachner identities apply only when the **internal measure** is the Ooguri BF one. They are not inserted as the definition of this causal measure skeleton. Iter078D remains a conditional comparator for any sector where the chosen EPRL convolution measure and compact restriction actually reproduce the BF weights.

## Data now defined vs still missing

Defined prospectively:

- coarse/fine same-boundary complex pair;
- identity boundary embedding;
- internal face weights;
- internal edge/intertwiner weights;
- internal spin/intertwiner sums;
- per-vertex local group gauge fixing;
- compatible orientation-resolved causal data;
- exact local source ordering.

Still missing:

- a selected reference local distributional extension;
- the full supported-jet coupling parameterization beyond the proven 32-dimensional lower bound;
- a regulator for internal sums/group distributions if required;
- a weighting law over multiple compatible causal orientations;
- a coarse projection/matching functional defining the actual RG map;
- convergence and closure of the refined amplitude family.

This separation is the purpose of the gate.