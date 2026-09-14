# Iter080B-SM — joint E3/E4/E6 generalized-causal source-bridge audit

## Verdict

`BLOCKED_SOURCE_BRIDGE`

Classification:

`ITER080B_SM_PARENT_E3_E4_E6_STRUCTURES_EXIST_LOCAL_CAUSAL_VERTICES_EXIST_BUT_COMPLETE_MULTIVERTEX_INHERITANCE_BRIDGE_NOT_SOURCE_EXPLICIT_BLOCKED_EXACT_SCOPED`

## Prospective provenance

- Frozen preregistration: `d9b4d8a6c489b2c7560cfad538ff62fd1e4f7b07`.
- Frozen source matrix: `65483fb99c913e6b99e0e1b9c17bafdd45b69b62`.
- Implementation: `660dfee9e0e3540ebf05c53ef9cc6f98a5e44db8`.
- Workflow / production head: `3b7bbfbbae5f1718ea1c4195e4fd44675f2c456e`.
- Terminal run: `34825084313`.
- Aggregate job: `103915305607`.
- Aggregate artifact: `10339454847`, digest `sha256:73cf815a59649f0e5b8ec8b972dc0583fe0d4a869e94da13f9e3686c60bd601b`.
- All A/B/C/D lanes and aggregate completed successfully. Scientific classification comes from the frozen source predicates, not from green CI.

## Source findings

### Parent KKL/EPRL

The already-authoritative parent construction contains the relevant noncausal structures: E3 contraction/gluing, E4 face/edge weights and internal sums/normalization structure, and a noncompact `SL(2,C)` redundancy/fixing prescription. This reproduces the narrower Iter079E/G/K/L conclusions and is not a new claim.

### Bianchi–Chen–Gamonal 2601.23162

The primary causal-Toller paper defines and studies a causal EPRL **single-vertex** amplitude. Its discussion explicitly states that the paper focused on a single vertex and describes that object as a building block for a future path integral with many vertices. Under the frozen criterion this supplies the local causal vertex but not P1–P4 for a complete many-vertex causal inheritance prescription.

Source: https://arxiv.org/abs/2601.23162

### Beltrán 2603.22661v2

Beltrán makes the causal structure itself applicable to arbitrary 2-complexes and defines a generalized EPRL-KKL **causal vertex amplitude**. This closes the local/generalized causal-vertex side of the bridge more strongly than the simplicial-only paper. However, in the audited source the required complete state-sum inheritance statements are not made explicit: the paper gives the generalized causal vertex and its asymptotics and still lists finiteness of that generalized causal vertex as open. Under the prospectively frozen contract this does not by itself establish P1–P4 as a complete many-vertex prescription.

Source: https://arxiv.org/abs/2603.22661

## Frozen predicate result

For the combined validated corpus:

- P1 complete causal many-vertex functional explicit: **false** under the frozen source-definition criterion.
- P2 E3 parent contraction inheritance explicit as a physical causal prescription: **false**.
- P3 E4 weights/sums/normalization inheritance explicit as a physical causal prescription: **false**.
- P4 E6 per-vertex quotient/fixing normalization inheritance explicit for the causal many-vertex functional: **false**.
- P5 compatibility with the actual BCG/Beltrán causal local vertex: **true at the local-vertex level**, but insufficient to rescue P1–P4.

## Scientific effect

This joint audit consolidates the previously separate E3, E4 and E6 blockers into one source-definition statement: the parent ingredients exist and the causal local/generalized vertices exist, but the validated KKL + BCG + Beltrán corpus does **not explicitly define or derive the complete many-vertex causal inheritance bridge required by the frozen gate**.

This is narrower than saying a causal many-vertex theory is impossible. Algebraic conditional inheritance under a strict vertex-only replacement remains valid as a mathematical statement. What remains missing is source authorization/derivation that the physical causal theory is exactly that replacement with unchanged E3/E4/E6 data.

## Scope firewall

No conclusion is made about E7/E8, the unique K5 extension, regulator independence, causal-vertex finiteness/divergence, G3, F9/G8, RG/E9, `NEW_PHYSICS_FOUND`, or complete quantum gravity. The independent Iter077Q/Iter080A infinite-dimensional K5 extension-selector blocker remains fully active.

## Next admissible direction

Do not repeat source scans of the same frozen corpus unless a genuinely new primary source or revised version changes the object definition. The composition branch is now efficiently frozen at `BLOCKED_SOURCE_BRIDGE` for this corpus. High-value Researcher effort should move to a genuinely stronger, source-compatible K5 distributional-extension selection principle acting on the full Iter077Q function space, or to a newly identified primary source that explicitly supplies the missing many-vertex causal prescription.
