# Iter076C preregistration — source-coordinate bridge completeness audit

Date: 2026-09-13

## Purpose

Prospectively audit whether the repository already contains a source-faithful, explicit map from the full causal vertex of Eq. (4), together with the Cartan/magnetic decomposition Eq. (7), to the reduced K4 collision variables used in Iter068–076, including the local measure/numerator Jacobian through quadratic order.

This is a source/object-definition gate. It is not a denominator-only numerical gate and it does not authorize an epsilon^-1 coefficient calculation unless all required objects are explicitly present and provenance-linked.

## Frozen evidence set

Audit only the following already-existing objects plus the immutable primary-source snapshot:

1. `sources/CAUSAL_SPINFOAM_VERTEX_2026_SOURCE_SNAPSHOT.md`
2. `vertex/direct_causal_integrand_smoke.py`
3. `vertex/regulated_haar_mc_vertex.py`
4. `distributional/iter068c_prepullback_eprl_control.py`
5. `distributional/iter069a_k4_joint_spectral_homogeneous.py`
6. `distributional/iter072b_k4_signed_cutspace_theorem.py`
7. `distributional/iter076b_degree2_overlap_jet_complex.py`
8. their controlling status/result notes where needed for provenance.

No new physical assumption, fitted coefficient, Euclidean cycle metric, preferred tree/order, or post-hoc coordinate identification may be introduced.

## Frozen predicates

P0 SOURCE_VERTEX: Eq. (4) is represented as four independent SL(2,C) group integrations after g1=1 and ten ordered wedge factors T(g_b^-1 g_a).

P1 SOURCE_CARTAN: Eq. (7) / repository implementation explicitly reconstructs full Toller matrix elements from compact factors plus the reduced boost kernel.

P2 HAAR_OBJECT: repository contains an explicit Haar-matched group-domain measure object sufficient to identify at least the source-domain radial density, with all truncation/normalization limitations stated.

P3 K4_MAP_EXPLICIT: there exists an explicit, provenance-linked coordinate/pushforward map from the four-group local variables (or an explicitly derived source submanifold thereof) to the exact reduced K4 collision variables used by Iter068–076.

P4 QUADRATIC_DENSITY_EXPLICIT: under that same map, the induced local numerator × Haar/Jacobian density is explicitly derived through quadratic order, including all magnetic/compact-factor dependence required by the ten-wedge integrand.

P5 FACE_COEFFICIENT_READY: the six admissible transitive proper-face coefficients can be computed without introducing any coefficient, metric, projection, or subtraction not fixed by P0–P4.

## Frozen classification

- If P0–P5 all hold: `ITER076C_SOURCE_TO_K4_QUADRATIC_DENSITY_OBJECT_PRESENT_SCOPED`. This only authorizes prospective preregistration of the actual degree-two / nominal epsilon^-1 coefficient gate.
- If P0–P2 hold but any of P3–P5 fails because an object is absent/not derived: `ITER076C_BLOCKED_SOURCE_TO_K4_PUSHFORWARD_OR_QUADRATIC_DENSITY_MISSING`. This is BLOCKED_OBJECT_DEFINITION, not a scientific divergence/finiteness result.
- If P0–P2 themselves fail due to source/code inconsistency: `ITER076C_SOURCE_CARRIER_INCONSISTENT` and stop before any coefficient work.

## Claim locks

No NEW_PHYSICS_FOUND; no complete-QG claim; no physical causal-vertex finiteness/divergence theorem; no physical sector selection; no G3/F9/G8/K5 promotion; no arbitrary counterterm or fitted cancellation; keep source i epsilon; distinguish full source vertex, regulated pilot, reduced denominator skeleton, source-derived pushforward, and distributional boundary value.
