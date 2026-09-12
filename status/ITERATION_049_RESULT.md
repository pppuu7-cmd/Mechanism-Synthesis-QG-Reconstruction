# Iteration 049 — terminal result

## Frozen gate
Cycle-coordinate permutation covariance of the Iter048 residue-residue (`RR`) commutator selector, using the unchanged K4 kernel and unchanged `FP=R+A` decomposition.

Frozen matrix: held-out cases A/B × trees `S0,S1,P0,P1` × all six permutations of the three cycle coordinates = 48 lanes. The canonical pair `(0,1)` in each permuted representation was mapped back to its original unordered cycle pair.

## Infrastructure repair
The first production attempt `34709342843` failed before the frozen classifier because the new relabeled integration symbols were created without `real=True`; SymPy therefore retained `Im(z_i)` in pole locations and correctly failed closed. Commit `1e529c954a5b31bdc1374183865c9ac087c2ada3` changed only the symbolic assumption of the relabeled cycle coordinates to real, matching the original K4 integration coordinates. No source parameter, FP algebra, contour rule, pole selection or classifier changed.

## Authoritative provenance
- repaired main commit: `1e529c954a5b31bdc1374183865c9ac087c2ada3`
- authoritative workflow run: `34709710387`
- aggregate job: `103597057749`
- aggregate artifact: `iter049-aggregate`, artifact ID `10302939028`
- artifact digest: `sha256:e1c9a052c469abf49b3ebf7ff908bc4850ef81b9303a715fce04759b30f119ff`

## Terminal machine result
Classification: `K4_RR_SELECTOR_NONCOVARIANT`.

- lanes: `48/48` valid
- all EPRL/no-contact control totals exactly zero: `true`
- all EPRL/no-contact control channel commutators exactly zero: `true`
- every fixed `(case,tree)` is covariant under reversal/orientation of the same mapped unordered pair: `true`
- selected RR-pair pattern is consistent between the two held-out cases for a given tree: `false`

Exact selected-pair patterns:

| case | S0 | S1 | P0 | P1 |
|---|---|---|---|---|
| A | `{01}` | `{}` | `{}` | `{01,02,12}` |
| B | `{}` | `{01}` | `{01,02,12}` | `{}` |

Thus the same graph/tree/pair can switch RR activation when only the held-out source parameters change. Examples:
- `S0/01`: RR on in A, off in B;
- `S1/01`: off in A, on in B;
- `P0`: all three pairs off in A, all three on in B;
- `P1`: all three pairs on in A, all three off in B.

## Scientific interpretation
The RR-active subset is not a universal graph-only selector and is not a simple positional-label artifact. Within a fixed source/tree it is internally coordinate-covariant, but its activation changes with source parameters. Therefore a parameter-independent overlap/incidence invariant cannot by itself explain the RR subset.

The next admissible gate must diagnose which source-dependent ingredient controls RR activation: Feynman pole topology, `gamma`, finite spectral `epsilon`, causal sign pattern, and/or external K4 flow `k`. This diagnosis must preserve the exact EPRL/no-contact control and the unchanged `FP=R+A` algebra.

This remains a structural diagnostic of the sequential K4 finite-part algebra. It is not a physical causal-vertex divergence/ill-definition theorem and does not authorize K5, G3, F9 or G8 promotion.
