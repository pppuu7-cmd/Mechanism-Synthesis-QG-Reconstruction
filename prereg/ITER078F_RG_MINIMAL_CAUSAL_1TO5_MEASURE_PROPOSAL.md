# Iter078F-RG preregistration — minimal versioned causal 1-to-5 measure/embedding proposal

**Date:** 2026-09-14

## Status / anti-rescue lock

This gate does **not** claim that CRQN v0.2 already contains a multi-vertex/RG map. Iter078A proved it does not.

The gate tests a new experimental extension of the programme, provisionally named

`CRQN v0.3-R0 (MEASURE_PROPOSAL_ONLY)`.

It is independently motivated by the continuum/refinement requirement of any spin-foam model. It is not promoted to the candidate mechanism unless its own prospective gates pass.

## Scientific question

Can the missing **measure / boundary embedding / causal-orientation part** of the minimal same-boundary `1 -> 5` refinement map be specified without altering the source local Toller ordering and without hiding the known extension ambiguity?

## Frozen external measure authority

Use the standard Lorentzian EPRL state-sum convolution convention documented by Donà-Frisoni:

`Z_Delta = sum_{j_f,i_e} prod_f A_f(j_f) prod_e A_e(i_e) prod_v A_v(j_f,i_e)`

with

`A_f(j_f)=2j_f+1`,

`A_e(i_e)=2i_e+1`,

fixed by the correct convolution property at fixed boundary.

Using these weights for the causal-Toller multi-vertex model is **new CRQN-R structure**, not a claim that Bianchi-Chen-Gamonal already selected them for the new causal vertex.

## Frozen 1-to-5 complex

Use exactly the Iter078B `1 -> 5` subdivision of one 4-simplex by an interior primal vertex.

- coarse boundary triangulation is unchanged;
- therefore the coarse/fine boundary Hilbert space is the same spin-network space and the boundary embedding is the identity;
- internal fine tetrahedra/faces are summed over with the frozen EPRL convolution weights above;
- one redundant `SL(2,C)` group integration is gauge-fixed at each causal-Toller vertex exactly as in the single-vertex source convention.

## Frozen causal data

For each of the 32 coarse boundary sign patterns, use the compatible acyclic internal orientations classified by Iter078B.

This gate defines the amplitude **orientation-resolved** first. It does not assign a new relative probability/weight to different compatible internal causal orientations. A later sum over them requires a separate prospective weighting rule.

## Frozen local vertex family

At every fine vertex keep the exact source ordering

`one-wedge spectral/spinor construction -> Toller function -> ten-wedge product -> boundary contraction -> group integration/extension`.

Do not replace the Toller vertex by an EPRL or BF vertex.

The local extension is **not** silently fixed. Carry it abstractly as

`A_v = A_ref,v + Delta_v`,

where `A_ref,v` is one reference same-scaling-degree extension and `Delta_v` belongs to the allowed supported extension space.

By Iter078E, even the order-zero integrated ambiguity image in the controlling all-`j=1/2` sector has dimension at least 32. Therefore the proposal must not truncate `Delta_v` to one scalar `cL` unless a later reduction gate justifies it.

## Frozen checks

### A — measure/embedding completeness

PASS iff the 1-to-5 fine state-sum object has explicit:

- unchanged boundary Hilbert space and identity embedding;
- face weights;
- edge/intertwiner weights;
- internal spin/intertwiner sums;
- per-vertex group gauge fixing;
- orientation-resolved causal assignments;
- exact local Toller source ordering.

### B — no hidden local-amplitude selection

PASS iff the definition keeps the full known extension freedom explicit and does not set a finite part, BF normalization, or extension coefficient post hoc.

### C — source-limit control

If every causal Toller matrix is formally replaced by the ordinary EPRL Wigner matrix and the local extension issue is removed, the measure/embedding skeleton must reduce to the standard EPRL 1-to-5 state-sum prescription in the same convention.

### D — scope firewall

The BF 15j/Pachner measure is not substituted for the causal model. Iter078C/D may be used only as conditional controls inside sectors where the newly frozen EPRL convolution measure actually reduces to the corresponding compact BF contraction.

## PASS

PASS iff A-D define a complete **measure/embedding skeleton** for the 1-to-5 causal refinement family while leaving the unresolved local extension and coarse projection visible.

Classification:

`ITER078F_RG_VERSIONED_CAUSAL_1TO5_EPRL_CONVOLUTION_MEASURE_AND_IDENTITY_BOUNDARY_EMBEDDING_DEFINED_LOCAL_EXTENSION_STILL_EXPLICIT_SCOPED`

## FAIL

FAIL iff the standard EPRL convolution skeleton is incompatible with the fixed causal orientation/source vertex data already established.

## BLOCKED

BLOCKED iff an essential measure or embedding datum cannot be fixed without an additional arbitrary choice beyond the explicitly versioned proposal.

## Interpretation ceiling

PASS does not define `A_ref`, does not select the supported extension coefficients, does not define the coarse projection/matching functional, does not prove convergence of internal sums, and does not give an RG flow or fixed point.

On PASS the exact next gate is mathematical **well-definedness/closure** of this new measure skeleton when the full minimal 32-dimensional order-zero extension sector is carried explicitly.