# Iter077J-SM preregistration — full-32 source-ordered leading angular span

Date: 2026-09-14

## Scientific question

In the all-`j=1/2` source-ordered Toller-function K5 sector closed by Iter077I-SM, can a nonzero **angle-independent** linear combination of the 32 five-node boundary-intertwiner basis states cancel the complete leading common-collision term identically as a function of collision direction?

This gate tests only the leading source-ordered homogeneous coefficient. It does not test a correlated distributional boundary value, subleading Toller terms, the full causal vertex, regulator independence, or generic spins.

## Frozen source/object locks

1. Use the same source ordering as Iter077I-SM:
   `one-wedge source construction -> Toller function -> K5 product -> group integration`.
2. Use the `j=1/2` leading off-axis matrix, up to nonzero common edge scalars,
   `M(v)=[[v_z,-v_x-i v_y],[-v_x+i v_y,-v_z]]`.
3. Use all `2^5=32` boundary basis components with the exact stripped node tensors frozen in Iter077I-SM.
4. Gauge fix vertex 0 at the origin. A collision-direction sample is four integer 3-vectors `x_1,...,x_4`, with all ten edge differences nonzero.
5. Branch signs are not summed. Iter077I-SM already established that factorized causal assignments multiply the leading coefficient only by an overall nonzero sign, so they cannot change angular-span rank.

## Frozen deterministic ray families

No ray may be changed after looking at rank.

For integer seed `s`, define

- `x_0=(0,0,0)`
- `x_1=(1+s, 2+2s, 3+3s)`
- `x_2=(2+2s, 5+3s, 7+5s)`
- `x_3=(4+3s, 8+5s, 13+7s)`
- `x_4=(7+5s, 11+7s, 19+11s)`.

Main family: seeds `s=0,...,39`.
Held-out family: seeds `s=41,...,56`.

A seed is valid only if all ten edge differences are nonzero. Invalid frozen seeds are a gate failure, not silently replaced.

## Frozen lanes

### Lane A — provenance/admissibility

Verify the Iter077I source/order locks and that all 56 frozen rays used by main+held-out families have ten nonzero edges. Record squared edge lengths for seeds 0 and 56 as provenance controls.

### Lane B — exact main angular-span rank

For each of the 40 main rays compute the exact 32-component Gaussian-integer leading contraction vector. Form the 40x32 matrix over `Q(i)` and compute exact rank.

Frozen PASS target: `rank=32`.

If rank is less than 32, output an exact nonzero right-nullspace witness and classify scientific FAIL for the frozen full-rank hypothesis. Do not fit or change rays.

### Lane C — held-out rank / basis witness

Compute the 16 held-out vectors and append them to the main 40. Verify the exact combined rank. If Lane B is full rank, identify the lexicographically first 32-row independent minor from the main family and record its exact determinant/nonzero certificate.

Frozen PASS target: main rank 32, combined rank 32, exact nonzero 32x32 minor.

### Lane D — relabeling covariance and negative control

For the lexicographically first 8 main rays, apply all 120 vertex permutations to the five vertex coordinates, regauge by subtracting the permuted root coordinate, and recompute the 32-vector. Verify that the span rank of the resulting set is 32 and that direct relabeling does not create a universal boundary null vector.

Negative control: replace every ray by a collinear family `x_a = t_a (1,0,0)` with distinct frozen integers `t=(0,1,3,7,12)` and verify that its single-ray matrix cannot itself certify rank 32.

The negative control is diagnostic only; it is not a model of the source collision geometry.

## Frozen interpretation

If all lanes pass, classification is:

`ITER077J_SM_SOURCE_ORDERED_JHALF_LEADING_ANGULAR_COEFFICIENT_SPANS_FULL_32_BOUNDARY_SPACE_EXACT_SCOPED`.

Allowed conclusion: in this all-`j=1/2` leading source-ordered sector, there is no nonzero angle-independent boundary-state coefficient vector whose contraction cancels the leading `r^-20` common-collision coefficient identically for all angles. Full rank on finitely many exact angular witnesses is sufficient for this identity-level exclusion.

This does **not** imply divergence/nonexistence of the full causal vertex. It does not exclude an angle-dependent cancellation, a source-selected conditional/Hadamard/Feynman boundary value, cancellation involving subleading terms in a distributional extension, or generic-spin effects.

If the main rank is <32, classification is scientific FAIL of the full-span hypothesis; retain the exact nullspace witness for the next gate.

## Claim locks

No `NEW_PHYSICS_FOUND`; no complete-QG claim; no physical causal-vertex finiteness/divergence theorem; no regulator-independence theorem; no source-selected correlated extension theorem; no generic finite-spin result; no physical source-to-K4 pushforward; no nominal `epsilon^-1` coefficient; no G3/F9/G8/K5 promotion.