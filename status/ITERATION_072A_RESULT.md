# Iteration 072A result — common-epsilon leading-collision Schwinger-cone route

Date: 2026-09-13

## Authoritative provenance

- Prospective preregistration: `1e011e9804ee2cde41260039c551f77562c68a4c`
- Lane implementation: `39a60064ea666dc9d021396eec20324d70b2b9cc`
- Aggregate implementation: `1a4ff3698a119f7e20acfe7f55c77fd3e7bab1f5`
- Authoritative production head: `9ac6e5f766b73531c58de9d5cf636033189274a5`
- Run: `34744136699`
- Aggregate artifact: `10313745085`
- Aggregate digest: `sha256:263f46b94d10835e3ec156e553697f98ca213d5619ef1f58a6ff57c8d9ffb96d`

Frozen classification:

`ITER072A_LEADING_COLLISION_THEOREM_ROUTE_FAIL`

The run emitted artifacts for all eight source sigma lanes despite four lane jobs exiting nonzero under the frozen classifier.

## What passed

The aggregate independently recovered:

- strong-tournament classes: `++-+`, `+-++`, `+-+-`, `+--+`;
- the same four classes from the constructive positive-circulation test;
- proper-stratum power separation in every lane: every proper denominator subset has divergence degree strictly below the full-collision value `6-3=3`;
- the deliberately wrong orientation control disagrees with the source classification.

Thus the historical Iter058 strong-tournament / positive-circulation theorem is not contradicted.

## First causal scientific failure

The frozen Iter072A theorem route incorrectly identified the Schwinger/Fourier delta constraint with the circulation space.

For zero external flow, the six edge linear forms are

`x = L y`,

where the three columns of `L` span the K4 cycle space `ker(B)`. For

`prod_e (x_e - i s_e epsilon)^(-1)`

and the Schwinger parameters `t_e >= 0`, Fourier integration over the three cycle coordinates imposes

`L^T diag(s) t = 0`.

Therefore `diag(s)t` belongs to `ker(L^T)`, i.e. the K4 **cut space** (row space of the incidence matrix), not to the circulation space `ker(B)`.

A representative strong lane `sigma=+-++` makes the failure explicit: the lane correctly reports strong connectivity, a three-dimensional positive cycle span and a constructive positive circulation, but that circulation does not annihilate `L^T diag(s)` in any of the four cycle bases. The failed P2 predicate is therefore not an implementation/parser/numerical problem; it exposes a wrong dual-space premise in the preregistered theorem route.

This is a genuine scoped scientific negative result for Iter072A. Frozen criteria are not modified and the run is not rerun with a changed theorem.

## Scientific consequence

Iter072A does **not** establish an `epsilon^-3` coefficient iff strong tournament. Instead it identifies the correct next object: the strict-positive intersection of the Schwinger parameter orthant with the **signed cut space**.

For a complete graph, a strict cut-space vector has components proportional to vertex-potential differences. Its strict sign pattern induces an acyclic tournament; for a tournament, acyclic is equivalent to transitive. This motivates a separate prospectively frozen gate, not a repair of Iter072A.

No conclusion follows yet about the complete causal vertex, physical causal-sector selection, K5, G3, F9 or G8.
