# Iteration 068A result — K4 microlocal denominator-skeleton collision audit

Date: 2026-09-13

## Authoritative provenance

- Preregistration commit: `d64bf56cb4eac29228262d80bc57960911e507f5`
- Implementation commit: `633fe38e6a121768bca30325a808365aa035113b`
- Launch/head commit: `9d32dbbc0c6542d24ae684fbd58fce31e1cf6729`
- Workflow run: `34739048517`
- Aggregate job: `103675510433`
- Aggregate artifact: `10311807799`
- Artifact digest: `sha256:cb4713dde51dbfb390f6c5276b1d33aaa92b7129d2fbbb2716d6c5c61a701268`

## Frozen result

All `16/16` lanes were valid and the classification was invariant under the unfixed global ordered-branch convention `c=±1`.

Terminal classification:

`ITER068A_K4_MICROLOCAL_SKELETON_MIXED_8_OBSTRUCTED_8_COMPATIBLE_CONVENTION_INVARIANT`

Compatible sigma classes:

- `++++`
- `+++-`
- `++--`
- `+---`

Obstructed sigma classes:

- `++-+`
- `+-++`
- `+-+-`
- `+--+`

Equivalently, at the denominator-incidence skeleton level, half of the physical K4 sigma classes admit no positive opposing-covector circulation at the full collision, while half contain a directed-cycle/positive-circulation witness. The result is unchanged by `c -> -c`.

## Scientific interpretation

This is a **necessary microlocal skeleton classification only**. It does not compute the full Toller wavefront set. In particular, it does not yet include the symmetric wavefront contribution of the Appendix-D contact distributions produced after the spectral transform, nor does it prove a joint multivariate analytic boundary value.

Therefore:

- compatible skeleton classes are not proven to define a Toller product;
- obstructed skeleton classes only fail this simple Hörmander denominator-product route;
- no causal sector is physically selected;
- no causal-vertex finiteness/divergence or nonexistence theorem follows;
- K5 remains blocked pending a source/analyticity-selected correlated extension object and distributional Eq.(5)/(6) inheritance.

## Next admissible tests

1. Include the source-backed `j=1/2` Appendix-D contact layer and test its exact conormal collision structure (`Iter068B`).
2. Independently test the additive EPRL control at the distributional pre-pullback level, preserving the order `independent branch sum -> boundary limit` (`Iter068C`).
3. Independently test S4 vertex-permutation covariance of the Iter068A skeleton partition (`Iter068D`).

No G3/F9/G8/K5 promotion is authorized by this result.
