# Iter076J terminal result — gauge-fixed K5 incidence fixes K4 complement support

Date: 2026-09-13

## Authority
- preregistration: `c62d638c537de5f44590c8520242c82274cf84be`
- implementation: `1a73a4f6a221e8d9b635a90f55aba46e4df10d66`
- production/workflow head: `8a2526ab3cd9bb0ee5d53f2bf8673effa4a8c00f`
- run: `34776203868`
- aggregate job: `103774690236`
- aggregate artifact: `10323372997`
- aggregate digest: `sha256:8b96d5e952a8804eaa5718a7b7c9e1bc57cccddee3e87922cc79eafaa3e4ea48`

Raw lane artifacts consumed:
- A: job `103774666163`, artifact `10323941087`, digest `sha256:da872ca60109e934bd9d30ecff90978129c957e4cc7e6daa3b760632dcd9b597`
- B: job `103774666272`, artifact `10323182839`, digest `sha256:bfa08325c5d27436669c47ebc13ff7e669d624340becfe07414a94f5369161d9`
- C: job `103774666286`, artifact `10323667086`, digest `sha256:c37794f9cee67a910e852c7004ba5c257a903eecd224a8704044def90643f04e`
- D: job `103774666351`, artifact `10323726903`, digest `sha256:ad7f2da873389ffcc0450fc099cbec9293bd43b47fbdac57703fb8549f950e3a`

## Frozen scientific classification
`ITER076J_SOURCE_GAUGE_FIXED_K5_INCIDENCE_CANONICALLY_DEFINES_K4_COMPLEMENT_SUPPORT_EXACT_SCOPED`

## Terminal facts
All four prospectively frozen lanes pass.

1. For every one of the five possible source gauge roots, the K5 wedge graph decomposes exactly into six internal K4 edges and four root spokes, with complete ten-edge coverage and no overlap.
2. On the six internal edges there is exactly one bijective, fixed-point-free involution that sends every edge to a disjoint internal edge. The unique permutation is the complementary-edge pairing (`[5,4,3,2,1,0]` in the frozen canonical ordering).
3. The unsigned complement support is covariant under the stabilizer S4 of each gauge root: `720/720` checks pass exactly.
4. The family of complement maps is covariant under all tested full source-node relabelings and gauge-root changes: `3600/3600` checks pass exactly. Adjacent-edge, fixed-point, and unrelabelled-root controls are rejected.

## Interpretation lock
This closes only the **unsigned support provenance** subproblem exposed by Iter076I: the larger source Eq.(4) gauge-fixed K5 incidence canonically provides the complementary-edge pairing on the internal K4 wedges.

It does not establish the orientation sign on that pairing, the signed Hodge map, the physical source-to-K4 pushforward P3, the source numerator/Jacobian quadratic jet, or the nominal `epsilon^-1` coefficient. The next admissible provenance question is whether source orientation/order/contraction data fix the signed lift of this unique support, or leave a global-orientation/sign ambiguity.

No G3/F9/G8/K5 promotion, causal-vertex finiteness/divergence theorem, physical sector selection, complete-QG claim, or new-physics claim follows.
