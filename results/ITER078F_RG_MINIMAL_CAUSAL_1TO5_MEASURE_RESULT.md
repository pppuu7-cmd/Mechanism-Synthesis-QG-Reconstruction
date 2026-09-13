# Iter078F-RG result — a versioned causal 1-to-5 measure/embedding skeleton is definable, but the local extension and RG projection remain open

**Date:** 2026-09-14

## Provenance

- Prospective preregistration: `prereg/ITER078F_RG_MINIMAL_CAUSAL_1TO5_MEASURE_PROPOSAL.md`, commit `d2778fe40876c7dde8318ce3326fcd8a8fd6a33f`.
- Versioned measure definition: `sources/ITER078F_RG_MINIMAL_CAUSAL_1TO5_MEASURE_DEFINITION.md`, commit `b268f2fdda378efebf2e9f98184070992add0dfa`.
- External measure authority: standard Lorentzian EPRL fixed-boundary convolution state sum.
- Causal local-vertex authority: Bianchi-Chen-Gamonal single causal-Toller vertex.
- Causal orientation authority: Iter078B-RG.
- Extension-space lower bound: Iter078E-RG.

## Classification

`ITER078F_RG_VERSIONED_CAUSAL_1TO5_EPRL_CONVOLUTION_MEASURE_AND_IDENTITY_BOUNDARY_EMBEDDING_DEFINED_LOCAL_EXTENSION_STILL_EXPLICIT_SCOPED`

Scientific/object-definition verdict: **PASS** for the prospectively versioned measure/embedding skeleton.

## What is now explicitly defined

For the experimental

`CRQN v0.3-R0 (MEASURE_PROPOSAL_ONLY)`

1. the coarse complex is one 4-simplex and the fine complex is the Iter078B `1->5` subdivision;
2. the external triangulated boundary is unchanged, so the boundary Hilbert-space embedding is the identity;
3. internal spins/intertwiners are summed with the standard EPRL fixed-boundary convolution weights
   `A_f(j)=2j+1`, `A_e(i)=2i+1`;
4. every fine vertex uses the exact causal-Toller local source ordering, not an EPRL or BF substitute;
5. one redundant `SL(2,C)` group integral is removed per local vertex as in the single-vertex convention;
6. the fine amplitude is defined orientation-resolved for every compatible acyclic causal orientation from Iter078B, avoiding an invented relative orientation weight;
7. replacing every local Toller matrix by the ordinary EPRL Wigner matrix returns the standard EPRL state-sum skeleton in the same convention.

## What remains deliberately unfixed

The gate does **not** choose:

- a reference distributional extension `A_ref` of the non-L1 local causal vertex;
- the full supported extension-coupling space;
- a regulator for any remaining internal sum/group-distribution divergence;
- weights for summing different compatible fine causal orientations;
- the coarse projection/matching functional needed to define an RG transformation;
- a fixed point or beta function.

By Iter078E the all-`j=1/2` order-zero integrated ambiguity image already has complex dimension at least 32. Therefore the new measure skeleton explicitly rejects the earlier one-scalar `cL` witness truncation as a complete theory-space definition.

## New scientific fact

The previous `BLOCKED_MAP_DEFINITION` has been partially decomposed. A concrete same-boundary **measure and embedding skeleton** can be defined by a new independently motivated, source-compatible choice that preserves the causal-Toller local vertex and uses the standard EPRL convolution measure.

The remaining blocker is no longer “we do not know how to write a multi-vertex sum at all.” It is now sharper:

`REFERENCE_LOCAL_EXTENSION + FULL_EXTENSION_COUPLING_TRANSPORT + ORIENTATION_WEIGHT + COARSE_PROJECTION + REGULATOR/CLOSURE`.

## Anti-rescue status

This is new CRQN-R structure, not a retroactive property of CRQN v0.2. It is not promoted to the main candidate because its well-definedness and closure have not yet been tested.

The choice is independently motivated: the standard EPRL convolution measure is required for consistent multi-vertex composition in the parent Lorentzian spin-foam framework, regardless of the Iter077 ambiguity.

## Exact next admissible step

With the measure skeleton frozen, the highest-information successor gate is now **well-definedness before projection**:

1. choose no arbitrary low-dimensional truncation;
2. carry the complete 32-dimensional order-zero ambiguity basis in the frozen all-`j=1/2` sector;
3. test whether the refined 1-to-5 amplitude defines a finite linear/multilinear map on this sector under the new EPRL convolution weights;
4. classify pure compact/BF-like gauge redundancies under the **actual new measure**, rather than importing Ooguri results blindly;
5. only if finite, construct a coarse matching/projection and test closure.

If the reference extension itself is still required before even this regulated finite-spin map can be evaluated, the next result must say `BLOCKED_REFERENCE_EXTENSION_DEFINITION` rather than selecting a finite part post hoc.