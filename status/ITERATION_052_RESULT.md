# Iteration 052 — terminal result: canonical triple-residue antisymmetry remains obstructed

**Date:** 2026-09-12

## Authoritative production

- workflow run: `34716166419`
- production head: `6a212175e5e2f091c841b51e05c029c9c1df4613`
- aggregate artifact: `10305101542` (`iter052-aggregate`)
- artifact digest: `sha256:7ac12a5666cd337062ae143da864372eb011223563b47f36b733261b102ccc8f`
- frozen matrix: 9 preregistered conditions × 4 K4 tree bases = **36 lanes**

## Frozen classification

`K4_RRR_CANONICAL_ANTISYMMETRY_OBSTRUCTION_NONZERO`

All 36/36 lanes pass reconstruction/validity gates. Every F=1 control antisymmetrizer is exactly zero, while the source canonical full-S3 triple-residue antisymmetrizer is nonzero in **9/36** lanes. The preregistered nontriviality guard is satisfied.

Exact nonzero source positions:

- `BASE/S0`
- `E_HI/S0`
- `E_LO/S0`
- `G_HI/S0`
- `G_LO/S0`
- `K_ALT1/S0`
- `K_ALT2/S0`
- `S_ALT1/P0`
- `S_ALT2/P1`

The number of distinct six-order triple-residue values per lane has histogram: 18 lanes with 1 distinct value, 2 lanes with 2, and 16 lanes with 3.

## Scientific interpretation

The prospectively fixed canonical parity-weighted S3 antisymmetrizer does **not** remove the sequential K4 triple-residue order obstruction on the frozen matrix. Because the same construction vanishes exactly for all no-contact controls, the nonzero source result is not an implementation-level generic antisymmetry artifact.

This closes the preregistered `universal canonical antisymmetry identity` branch. No coefficients may now be refit to force cancellation. The permitted continuation is an independent source/analyticity-selected **simultaneous multivariate** K4 prescription audit, beginning with whether the six causal Feynman-sign shifts are compatible with a single global deformation of the three independent cycle variables.

This remains a structural distributional diagnostic, not a physical causal-vertex finiteness/divergence theorem. K5 remains `BLOCKED`; G3 remains `OPEN`; physical F9 remains `BLOCKED`; G8 remains `BLOCKED_CONVERGENCE_ONLY`.
