# Iteration 058 — K4 strict contour chamber as a positive-circulation / strong-tournament theorem

## Preregistration

This file is committed **before** Iter058 implementation and before any Iter058 output is inspected.

Iter057 independently established an exact basis- and orientation-aware-S4-covariant atlas of all 64 oriented K4 pole-sign vectors. Exactly 24 vectors are strict-chamber feasible and form one 24-element S4 orbit. Iter058 prospectively tests a graph-theoretic explanation fixed here.

## Frozen theorem candidate

Use canonical K4 edge order `01,02,03,12,13,23` and incidence matrix `B` with `-1` at the lower-index tail and `+1` at the higher-index head.

For a sign vector `s in {+1,-1}^6`, orient each undirected K4 edge as follows:

- `s_e=+1`: canonical direction `a -> b` for edge `(a,b)` with `a<b`;
- `s_e=-1`: reversed direction `b -> a`.

Let `D(s)` be this tournament.

The frozen theorem candidate is

`exists x in ker(B) with s_e x_e > 0 for all six edges`

**iff**

`D(s) is strongly connected`.

Because every K4 cycle matrix `A` used in Iter053–057 is an exact basis of `ker(B)`, this is equivalent to existence of a cycle-coordinate vector `v` with

`diag(s) A v > 0`.

## Prospectively fixed constructive proof audit

### Forward obstruction certificate

If `D(s)` is not strongly connected, find a nonempty proper vertex subset `U` whose cut is one-way: all edges crossing `U | V\U` point out of `U` (or, equivalently after complement, all point into `U`).

For any edge flow `x` with signs aligned to `D(s)` and strictly positive magnitudes, summing the exact conservation equations `Bx=0` over vertices in `U` leaves a strictly nonzero net cut flux. This contradicts conservation.

The computation must record an exact directed-cut certificate and verify the nonzero cut sign algebraically.

### Reverse constructive certificate

If `D(s)` is strongly connected, every directed edge `u->v` lies on a directed cycle: choose a directed path `v -> ... -> u` and append `u->v`.

For each of the six directed edges, choose deterministically the lexicographically first shortest return path and form that directed cycle. Sum the six signed cycle-flow incidence vectors. The resulting canonical edge-flow vector `x_constructive` must satisfy exactly:

- `B x_constructive = 0`;
- `s_e x_constructive_e > 0` on all six edges.

Then for each frozen cycle basis `S0,S1,P0,P1`, solve exactly for `v` and verify `A v = x_constructive` and `diag(s)A v > 0`.

No optimization, floating tolerance, fitted coefficient, or witness search is allowed.

## Frozen full-domain checks

All 64 oriented sign vectors are audited. For each vector record:

- strong connectivity;
- tournament outdegree score multiset;
- number of directed 3-cycles;
- Iter058 constructive positive circulation or exact one-way-cut obstruction;
- exact strict-chamber feasibility from the graph proof;
- independent agreement with the positive-circuit criterion (zero minimal positive circuits iff feasible) recomputed from the exact signed-normal atlas code, without reading Iter057 artifacts.

## Frozen S4 orbit characterization

Recompute the orientation-aware S4 orbits independently and verify that:

- strong connectivity is constant on every orbit;
- score multiset and directed-triangle count are constant on every orbit;
- the unique strongly connected orbit, if unique, coincides exactly with the strict-chamber feasible orbit.

No expected orbit sizes or score sequences are hard-coded into the classifier.

## Frozen terminal classifications

- `ITER058_GRAPH_FLOW_AUDIT_INVALID` if any incidence, path/cycle, cut, cycle-basis reconstruction, positive-circuit, or S4 action validation fails.
- `K4_STRICT_CHAMBER_STRONG_TOURNAMENT_EQUIVALENCE_FAIL` if the audit is valid but any of the 64 vectors violates the frozen equivalence.
- `K4_STRICT_CHAMBER_IFF_STRONGLY_CONNECTED_TOURNAMENT` iff all 64 vectors satisfy the equivalence with exact constructive/cut certificates and the independent positive-circuit criterion agrees everywhere.

## General proof scope

The underlying graph statement is more general than K4: a finite directed graph supports a strictly positive circulation on every directed edge iff every directed edge lies on a directed cycle; for a strongly connected digraph this condition holds. Iter058, however, freezes its computational claim to the complete K4 tournament domain and does not promote a broader theorem beyond the explicitly verified algebra without a separate written proof.

## Claim locks

This gate explains the frozen affine signed-normal surrogate. It does not prove that the physical causal Toller vertex selects strongly connected tournaments, does not establish a full branch inversion/permutation law, and does not unblock K5/G3/F9/G8 or establish new physics.
