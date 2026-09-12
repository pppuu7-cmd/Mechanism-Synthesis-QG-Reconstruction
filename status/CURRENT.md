# Current MSQGR research state

**Date:** 2026-09-12

- Candidate: `CRQN v0.2` (`CARRIER_SELECTED`)
- Established/source-backed mechanism union: `F1-F8`
- First MSQGR-derived prospective selector: Causal Cylindrical Intertwining (CCI)
  - `P_b'^± iota_b'b = iota_b'b P_b^±`
  - common-space/linearized form: `P_± R - R P_± = 0`
- Physical F9 (`CAUSAL_ANALYTICITY_RG_INVARIANT`): `BLOCKED`
- G8 novelty: `BLOCKED_CONVERGENCE_ONLY` until physical F9/F10 evidence exists
- Active programme front: `ITERATION_029 / MICROLOCAL_CYCLE_WAVEFRONT_OBSTRUCTION`

## What is established

1. The repository has a source-backed Lorentzian EPRL/Toller computational carrier and explicit causal/co-causal branch machinery.
2. The gamma-simple single-mode blocking ansatz is excluded by the half-integer mismatch `N=n1+n2+1/2`; this does not exclude superposition embeddings or a full RG map.
3. Multi-collision radial power counting gives a serious finiteness warning: k=3 is approximately logarithmically borderline, while k=4 and k=5 fail absolute first-moment power counting on tested generic collision rays; ordinary EPRL control remains regular.
4. Summing the tested causal sectors and performing the tested j=1/2 K5 boundary-intertwiner contraction did not remove the naive radial multi-pole scaling.
5. Appendix-D causal boundary distributions are validated as individual distributional primitives beyond j=1/2 at workflow level; this alone does not define their products at intersecting wedge singularities.
6. Iter026 excludes generic antipodal cancellation as a universal mechanism: a consumed raw lane has k=4 and k=5 antipodal ratios exactly 1, although k=3 shows strong parity cancellation.
7. Iter027A excludes universal full-sphere cancellation in a consumed raw lane: angular mean/RMS ratios remain nonzero and O(10^-2..10^-1) across tested rows.
8. A Christensen-type positive absolute-value spanning-tree proof cannot close for a beta^-2 Toller kernel on K5: exact graph geometry requires M>=5/2 while single-edge local integrability requires m<3/2. The full-matrix numerical norm scan independently reproduces p≈2. This is a no-go for that proof strategy, not a divergence theorem for the physical vertex.
9. Iter028 gives a structural warning for naive products of Appendix-D boundary singular terms. The reduced complete-graph incidence constraints have cycle nullity 1,3,6 for K3,K4,K5. Exact Gaussian-mollifier products diverge as eta^-1.00075, eta^-3.00085, eta^-6.00091 respectively, matching the redundancy exponents while the lowest Appendix-D delta coefficient is nonzero in all three lanes.
10. Iter029 upgrades that warning to an exact microlocal statement in the tested linearized common-spectral geometry. The reduced incidence conormals have left-nullity exactly 1,3,6 on K3,K4,K5, so the standard transverse/Hormander criterion for the naive product fails on every complete-graph collision tested. Spanning-tree controls have nullity 0. On K5 all 16 source-induced causal sign sectors preserve rank 4 and left-nullity 6. Exact forest enumeration shows that at least 6 of the 10 K5 constraints must be removed to recover a transverse subset; the 125 maximal transverse connected subsets are exactly the 125 spanning trees, matching Cayley.

## Iter029 runs

### Iter029A — exact microlocal cycle wavefront audit

Run `34671531875`, commit `8a10e81de137350d55d92f6fddc37d0724a6a92e`: 7/7 lanes SUCCESS and logs/artifacts consumed.

- K3 complete: rank 2, conormal left-nullity 1.
- K4 complete: rank 3, conormal left-nullity 3.
- K5 complete: rank 4, conormal left-nullity 6.
- K3/K4/K5 spanning-tree controls: left-nullity 0.
- K5 source-induced causal sectors: all 16 have left-nullity 6; all are non-transverse under the same naive delta-product criterion.

### Iter029B — exact forest-basis redundancy audit

Run `34671550029`, commit `314b594543e1e068fccbbaf558e7e058f4950f38`: 3/3 lanes SUCCESS and logs consumed.

For K5:

- 10 complete-graph wedge constraints;
- maximum transverse subset size 4;
- minimum removals for transversality 6;
- 125 spanning-tree subsets, exactly Cayley `5^(5-2)`;
- no transverse subsets of size >=5;
- redundancy count 6 exactly matches the Iter028 `eta^-6.000905` scaling exponent within the numerical fit accuracy.

Classification:
`EXACT_CYCLE_CONORMAL_DEPENDENCE_BLOCKS_STANDARD_NAIVE_MULTIWEDGE_DELTA_PRODUCT_ON_COMPLETE_GRAPH_COLLISIONS__OBSTRUCTION_DIMENSION_EQUALS_GRAPH_CYCLE_NULLITY_AND_SURVIVES_ALL_SOURCE_INDUCED_K5_CAUSAL_SIGN_SECTORS__SPANNING_TREE_CONTROLS_ARE_TRANSVERSE__CORRELATED_SOURCE_BACKED_IEPSILON_OR_RENORMALIZED_EXTENSION_STILL_OPEN`.

Record: `results/ITER029_MICROLOCAL_CYCLE_WAVEFRONT_AUDIT.md`.

## Current decisive target

The immediate blocker is now sharper:

`SOURCE_BACKED_CORRELATED_MULTI_WEDGE_DISTRIBUTIONAL_EXTENSION_NOT_YET_ESTABLISHED`

The standard naive product route is now blocked twice independently in the tested linearized common-spectral realization: numerically by the Iter028 regulator scaling and exactly by the Iter029 conormal-cycle dependence. Further random angular scans or independent pointwise regularizations are lower priority.

The next legitimate step is to construct or extract the **full source-backed correlated spectral i-epsilon boundary value before termwise wedge multiplication**, and then determine whether that correlated object admits a unique finite distributional extension. If the source only defines individual wedge boundary values, the next task is an explicit extension/renormalization analysis whose ambiguity dimension is tied to the cycle sector and whose finite parts must be fixed by physical consistency rather than by arbitrary subtraction.

Only after a well-defined finite same-realization causal carrier is established should the programme promote the physical CCI/F9 refinement test.

## Claim locks

- no `NEW_PHYSICS_FOUND`;
- no claim that causal EPRL is divergent nonperturbatively;
- no universal no-go theorem for causal EPRL;
- no F9 promotion from convergence-only evidence;
- no G8 novelty promotion before physical F9/F10 evidence;
- Iter029 is an exact statement for the tested linearized common-spectral boundary geometry, not a theorem excluding correlated source-backed i-epsilon constructions, renormalized extensions, full matrix/intertwiner cancellations, or alternative wavefront-compatible representations of the physical amplitude.
