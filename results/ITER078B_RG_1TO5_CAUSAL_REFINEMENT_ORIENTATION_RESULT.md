# Iter078B-RG result — all coarse causal boundary patterns extend to the 1-to-5 refinement

**Date:** 2026-09-14

## Provenance

- Prospective preregistration: `prereg/ITER078B_RG_1TO5_CAUSAL_REFINEMENT_ORIENTATION.md`, commit `6f4360ca249c1b5ad9c6b1bd78c9be747be24acd`.
- Implementation: `distributional/iter078b_rg_1to5_causal_refinement.py`, commit `a5d14bf75920c38a0c46106731c76ca65e2ebe07`.
- Workflow/production head: `.github/workflows/iter078b_rg_1to5_causal_refinement.yml`, commit `047b19fe75630a88aac3f0b783e34198756e6f05`.
- Authoritative run: `34790158373`.
- Aggregate artifact: `10328585276`, digest `sha256:db941e5cbf45e8f89012a8a7b0cef9568d3c289544c4b98a8027bb36f7d9a566`.
- Chunk artifacts:
  - chunk 0: `10328231025`, digest `sha256:0102d2d7e133dc889c0135452946e09a868ee13d46cf24eb9c83c45eb0ee4f3b`;
  - chunk 1: `10327696397`, digest `sha256:a7a27d4ec395eccb1e5c51bc2f9ba25463e8c8fbc4c49b4c3f0cd31ac88a03cf`;
  - chunk 2: `10327596959`, digest `sha256:292273ba2294eec1bb96d1734d571b3d17f31f62d8cc7ad94b6e71991c86da40`;
  - chunk 3: `10327577262`, digest `sha256:554c2d21dd643096eb42b3f6f10050ef99df4dd05595b870e2697e4dde3bceea`.

## Classification

`ITER078B_RG_1TO5_CAUSAL_BOUNDARY_ORIENTATIONS_EXTEND_TO_FINE_ACYCLIC_K5_ALL32_EXACT_COMBINATORIAL_SCOPED`

Scientific verdict: **PASS** for the preregistered causal-combinatorial refinement statement.

## Exact findings

All `32/32` coarse boundary sign vectors admit at least one fine acyclic orientation of the internal `K5` dual graph satisfying the frozen condition that every fine vertex attached to an ingoing coarse boundary edge precedes every fine vertex attached to an outgoing one.

The exact compatible-orientation counts depend only on the number `p` of incoming coarse boundary edges and equal the prospective analytic prediction `p!(5-p)!`:

- `p=0`: `120`;
- `p=1`: `24`;
- `p=2`: `12`;
- `p=3`: `12`;
- `p=4`: `24`;
- `p=5`: `120`.

Additional frozen checks all PASS:

- every induced local fine-vertex five-sign tuple belongs to one of the three source causal classes `0<->5`, `1<->4`, `2<->3`;
- reversing all coarse boundary signs and all internal orientations is an exact bijection between compatible refinement sets;
- exact aggregate-row checksum: `d64dacd896b81e02da143157c4d15056f0d9b6038aaea3c03594999d6d779a8d`.

## New scientific fact

There is no causal-combinatorial obstruction to extending any single-vertex coarse causal transition through the minimal same-boundary `1->5` simplicial refinement. The missing RG map therefore lies at the amplitude/measure/coarse-graining level, not at the existence of a compatible causal partial order.

## Interpretation ceiling

This result does not define the refined causal amplitude. It does not select the K5 distributional extension, define internal face/edge weights for the new causal model, freeze a boundary embedding/projection map, establish RG closure, produce a fixed point, prove regulator independence, or promote G3.

## Exact next admissible step

Freeze the **1->5 refined amplitude map** prospectively:

1. use the standard Lorentzian EPRL face/edge convolution weights as an explicitly new-but-independently-motivated causal multi-vertex prescription unless a more specific causal source rule exists;
2. freeze internal spin/intertwiner sums and per-vertex gauge fixing;
3. freeze the boundary embedding/matching between the coarse 4-simplex and the unchanged refined boundary;
4. carry the Iter077 supported extension coefficient(s) explicitly at every fine vertex;
5. test whether the refined amplitude is mathematically defined and whether coarse graining closes on the chosen extension-coupling family before asking for an RG fixed point.
