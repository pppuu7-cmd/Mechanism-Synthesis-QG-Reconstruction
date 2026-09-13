# Iter078A-RG preregistration — causal refinement / cylindrical-consistency map definition

**Date:** 2026-09-14

## Layer transition

This is the first authoritative gate after the Iter077 local-amplitude line. It moves outward to the refinement/RG layer instead of adding another collision lemma.

## Scientific question

Does an already established source-backed refinement/coarse-graining framework provide a **concrete map for the causal-Toller vertex** that is sufficient to evolve/select the supported K5 extension freedom found in Iter077L-N?

The relevant object is not generic “RG exists”. It is a defined map between coarse and refined causal spin-foam amplitudes with enough data to compute or constrain the local extension parameter(s).

## Frozen authority

1. Bianchi-Chen-Gamonal, *Causal spinfoam vertex for 4d Lorentzian quantum gravity*, arXiv:2601.23162.
2. B. Bahr, *On background-independent renormalization of spin foam models*, arXiv:1407.7746: cylindrical consistency of path-integral measures as the background-independent analogue of Wilsonian RG.
3. S. Asante, B. Dittrich, S. Steinhaus, *Spin foams, Refinement limit and Renormalization*, arXiv:2211.09578: consistent-boundary formulation, refinement and coarse-graining frameworks for spin foams.
4. Existing concrete restricted/truncated examples such as Bahr-Steinhaus hypercuboidal renormalization and Bahr-Rabuffo-Steinhaus symmetry-restricted EPRL/FK RG are controls for what data a real RG map requires; they are not automatically source authority for the causal-Toller model.

## Required concrete map data

For a refinement `Delta <= Delta'`, a usable causal RG/cylindrical map must freeze at minimum:

1. boundary Hilbert spaces `H_Delta`, `H_Delta'`;
2. an embedding/refinement map `i_DeltaDelta'` or equivalent coarse-graining map;
3. coarse and fine amplitude maps on the same physical boundary data;
4. fine-complex face/edge/vertex measure and gauge-fixing convention;
5. causal-label propagation/orientation on shared internal tetrahedra and faces;
6. treatment of internal sums/integrals;
7. a projection/truncation map if the coarse-grained fine amplitude leaves the chosen coupling family;
8. an explicit consistency/fixed-point equation, e.g. schematically
   `A_Delta(theta) = A_Delta'(theta') o i_DeltaDelta'`
   or an observable-matching equivalent;
9. a rule identifying how the Iter077 supported extension freedom is represented in `theta` and transported by the map.

A generic statement that “spin foams can be renormalized” is not sufficient.

## Frozen local input

Iter077N established that at least one supported extension coefficient changes the integrated vertex in the all-`j=1/2` sector (`16/32` nonzero compact boundary functionals) and that ordinary state-sum gluing merely propagates the coefficient.

Therefore any RG selector must supply an additional coarse/fine comparison, not merely multiply/glue vertices.

## PASS

PASS iff the frozen sources already determine all map data needed to write a concrete causal-Toller coarse/fine consistency equation whose dependence on the supported extension coefficient can in principle be evaluated without adding a new dynamical prescription.

Classification:
`ITER078A_RG_EXISTING_SOURCE_BACKED_CAUSAL_REFINEMENT_MAP_DEFINED_SELECTOR_GATE_OPEN`

## FAIL

FAIL iff an existing concrete causal map is defined but the supported extension freedom is proven to be an exact null direction of the coarse/fine consistency equations in the frozen scope.

## BLOCKED_MAP_DEFINITION

BLOCKED iff consistent-boundary/RG theory supplies the general framework but the causal-Toller model has not yet defined one or more essential map data above.

Classification:
`ITER078A_RG_CAUSAL_TOLLER_REFINEMENT_MAP_NOT_YET_DEFINED_FRAMEWORK_EXISTS_BUT_SELECTOR_NOT_COMPUTABLE`

## INVALID

INVALID if a restricted Euclidean/hypercuboidal/tensor-network RG flow is silently substituted for the Lorentzian causal-Toller source object, or if a new embedding/coarse-graining map is introduced and described as already source-derived.

## Interpretation ceiling

A BLOCKED result does not mean CRQN cannot be renormalized. It means CRQN v0.2 lacks the map needed to ask the RG fixed-point/selector question. A new refinement/RG mechanism may be scientifically admissible because refinement/regulator independence is required for a complete spin-foam theory independently of the Iter077 ambiguity, but it must be versioned and prospectively tested as new structure rather than used post hoc.

No RG fixed point, continuum limit, G3 PASS, regulator independence, Einstein IR, or complete-QG claim follows from this object-definition gate.