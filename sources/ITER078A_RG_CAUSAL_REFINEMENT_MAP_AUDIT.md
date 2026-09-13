# Iter078A-RG source audit — causal refinement / cylindrical-consistency map availability

**Date:** 2026-09-14

Prospective contract: `prereg/ITER078A_RG_CAUSAL_REFINEMENT_MAP_DEFINITION.md`, commit `97257d6830f1a386f9df3a854391e4e86e340884`.

## Causal-Toller source

Primary authority: E. Bianchi, C. Chen, M. Gamonal, *Causal spinfoam vertex for 4d Lorentzian quantum gravity*, arXiv:2601.23162.

The paper explicitly places the new construction inside the general spin-foam sum over 2-complexes, spins, intertwiners and causal edge orientations, but then states that it considers a **single vertex** dual to one 4-simplex. The new object actually defined is the fixed-causal single-vertex functional Eq. (4), obtained by replacing the ten EPRL Wigner matrices by ten Toller functions.

The paper does not define, for this new causal vertex:

- a coarse/fine pair of 2-complexes with a common physical boundary;
- a boundary embedding/refinement map;
- a causal-label propagation rule on shared internal tetrahedra of a refined complex beyond the generic statement that causal spin foams sum over oriented edges;
- a causal-model-specific internal face/edge measure for a refinement step;
- a coarse-graining/projection map back to a finite coupling family;
- a cylindrical-consistency or fixed-point equation comparing coarse and refined causal amplitudes.

Thus Eq. (4) is source authority for one local causal vertex, not a complete RG map.

## Background-independent RG authority

B. Bahr, arXiv:1407.7746, establishes that cylindrical consistency of path-integral measures provides a background-independent analogue of Wilsonian RG flow for spin foams. This is a framework-level statement: one compares amplitudes/measures assigned to different discretizations through specified refinement/coarse-graining data.

S. Asante, B. Dittrich, S. Steinhaus, arXiv:2211.09578, reviews the consistent-boundary formulation as a renormalization framework and separately discusses tensor-network, restricted-spin-foam and effective-spin-foam algorithms as concrete realizations aiming at consistent boundary amplitudes and refinement limits.

These sources establish that refinement/RG structure is independently motivated by regulator independence and continuum physics, not merely by the present K5 extension ambiguity.

They do not provide a ready-made coarse/fine map for the 2026 Lorentzian causal-Toller vertex.

## Concrete-model controls

Existing restricted/hypercuboidal EPRL/FK renormalization studies demonstrate what a computable RG flow requires: a chosen discretization family, truncated/restricted theory space, observables or amplitudes used for matching, and a projection back to a finite parameter family. For example, symmetry-restricted EPRL/FK studies define flows in explicit parameter spaces such as `(alpha,Lambda,G)` after strong geometric restriction.

Those flows cannot be silently transferred to the causal-Toller vertex:

- they are different model truncations/signatures/complexes;
- they do not contain the Toller causal data or the Iter077 supported extension freedom;
- their coarse-graining maps are part of the chosen approximation scheme.

## Required-map audit

Against the nine required data in the preregistration:

1. boundary Hilbert spaces: generic spin-network boundary spaces exist, but no causal refinement pair is selected;
2. embedding/refinement map: missing for the causal model;
3. same-boundary coarse/fine causal amplitudes: missing;
4. fine-complex face/edge measure and gauge fixing: not frozen for a causal refinement;
5. causal orientation propagation across internal shared tetrahedra/faces: not concretely defined for a refinement map;
6. internal sums/integrals: generic spin-foam state sums exist, but the causal refined object is not specified;
7. projection/truncation map: missing;
8. consistency/fixed-point equation: missing;
9. transport of the Iter077 extension freedom under coarse graining: missing.

## Scientific conclusion

The established literature supplies a well-motivated **framework** for background-independent refinement/RG, and the causal source supplies a new single-vertex kernel, but the composition of those ingredients into a concrete causal-Toller RG map has not yet been defined.

Therefore no existing source-backed RG equation can currently be evaluated to select the Iter077 extension coefficient(s). Constructing such a map is a new mechanism-development task, albeit one independently motivated by the continuum/regulator-independence requirements of any complete spin-foam model.