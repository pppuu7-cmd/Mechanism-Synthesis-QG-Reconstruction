# Iter058 — K4 strong tournament / positive circulation theorem

Date: 2026-09-18 (durable reconciliation of terminal 2026-09-12 run)

## Frozen authority

Prospective preregistration commit: `51c3e04da81652060a3bc76c2bad5c9825faecca`.
Implementation commit: `11513a2554ad26ef5320091eedd04337cab5454f`.
Workflow commit: `fe135f1aa2befdb959a2c40238ee98b9b54373de`.
Merged head: `dff2803ca240760861233c766b447e026fea16ae`.
GitHub Actions run: `34719879504`, terminal `completed/success`.
Artifact: `10305894028`, digest `sha256:24d06807b51f87d4751d3df3e4804c4e839e5e6cfce75ffb8d202492790bd84f`.

## Frozen terminal classification

`K4_STRICT_CHAMBER_IFF_STRONGLY_CONNECTED_TOURNAMENT`

All 64 oriented six-edge sign vectors are valid and the exact equivalence passes for all 64:

`exists x in ker(B) with s_e x_e > 0 for every edge` iff the associated K4 tournament is strongly connected.

Counts:

- 64 sign vectors checked;
- 24 strongly connected tournaments;
- 24 strict-chamber feasible vectors;
- 24 deterministic constructive positive circulations;
- 40 non-strong tournaments with exact one-way-directed-cut conservation obstruction;
- four orientation-aware S4 orbits, sizes 8, 8, 24, 24;
- exactly one S4 orbit is strongly connected / strict-chamber feasible.

Orbit invariants reproduce the prior structural interpretation:

- size 8, score sequence `[3,1,1,1]`: obstructed;
- size 8, score sequence `[2,2,2,0]`: obstructed;
- size 24, score sequence `[3,2,1,0]`: obstructed/transitive;
- size 24, score sequence `[2,2,1,1]`: strongly connected and feasible.

## Interpretation ceiling

This is an exact K4 graph-flow theorem for the frozen affine signed-normal surrogate. It does **not** establish that the physical Toller causal vertex selects strong tournaments, does not identify a physical sector, and does not promote K5/G3/F9/G8, regulator independence, `NEW_PHYSICS_FOUND`, or a complete-QG claim.

The later source-backed Boundary-S5 / K5 work in `status/CURRENT.md` supersedes Iter058 as the active pipeline. This note exists to close the historical ACTIVE Iter058 bookkeeping and preserve its exact scoped authority without reopening downstream gates.
