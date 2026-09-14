# Iter079B-SM — EPRL-KKL to causal-Toller composition inheritance result

## Authority
- Prospective preregistration: `45121d1b772057c61a861169ae93902c0b42e725`
- Frozen source matrix: `f0f746665e222d4c61c401dc3013383a23c3d900`
- Implementation: `e871c3a3741a930dfa2ce041799b91e441cb2b4f`
- Production head / workflow: `2ce5edac7f125f0345101fe158b191d2cb5cd91b`
- Authoritative run: `34794348389`
- Raw artifacts: A `10329072156`, B `10329022300`, C `10329880059`, D `10328987312`
- Aggregate artifact: `10329172140`
- Aggregate digest: `sha256:074a329a902df070692a76503db7dd98e9e8b450e102f37c94f97aeb41b5a06a`

All four raw lanes and the aggregate were consumed before classification.

## Classification
`ITER079B_SM_PARENT_COMPOSITION_SKELETON_EXISTS_BUT_CAUSAL_INHERITANCE_REQUIRES_NEW_BRIDGE_E3_E8_BLOCKED_EXACT_SOURCE_AUDIT`

Verdict: **BLOCKED** (scientific/object-definition blocker, not infrastructure failure).

## Frozen lane outcomes
- Lane A: `PASS`. Parent EPRL-KKL supplies the algebraic composition skeleton: arbitrary 2-cell structure, generic boundaries/arbitrary valence, orientation/duality structure, and parent vertex construction. Parent structure is not itself causal authority.
- Lane B: `PASS`. Beltran supplies E1 causal structure on arbitrary oriented 2-complexes and E2 generalized causal vertex, while the frozen source scope does not provide a complete causal multi-vertex inheritance theorem.
- Lane C: `BLOCKED`. E3-E6 remain missing required objects: causal local-vertex product/contraction; inherited face/edge weights, internal sums and normalization; causal boundary gluing/duality convention; and composed-object noncompact gauge quotient/fixing.
- Lane D: `BLOCKED`. E7-E8 remain missing. Ordinary linear gluing transports the Iter077Q supported extension ambiguity unless a source theorem supplies an annihilation theorem or an extension selector.

## New scientific fact
The parent EPRL-KKL algebraic composition skeleton does **not by itself** remove the need for a causal E3-E8 bridge. In particular, if `A_ext -> A_ext + h` with `h` in the Iter077Q supported ambiguity space and `G` is an ordinary linear gluing/contraction map, then

`G(A_ext + h) = G(A_ext) + G(h)`.

Therefore gluing does not select an extension unless the full allowed ambiguity space lies in `ker(G)` or an additional source-derived selector is supplied. Neither condition is established by the frozen sources.

## Scope locks
This result is not a no-go theorem for causal multi-vertex spin foams. It does not prove that a complete causal composition cannot be defined; it proves that the currently frozen source/model axioms do not uniquely define it without additional bridge data.

No unique K5 extension, regulator independence, RG/G3/F9/G8/K5 promotion, complete-QG claim, or `NEW_PHYSICS_FOUND` claim follows.

## Next admissible gate
Separate the blockers:
1. E3-E6: on a minimal two-vertex foam, test whether one-vertex causal data plus the parent combinatorial skeleton uniquely determine the composed functional, or whether explicit normalization/pairing/weight freedoms yield inequivalent two-vertex amplitudes while preserving all frozen one-vertex data.
2. E7-E8: only after E3-E6 are fixed, test whether the resulting gluing map annihilates, transports, or selects the Iter077Q function-space ambiguity.
