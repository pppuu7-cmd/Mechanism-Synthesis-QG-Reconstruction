# Iter073C result — exact nontransitive cut-space separation certificates

Date: 2026-09-13

## Authority

- preregistration commit: `77af541dfe371632c92eb3e5cda176511be7eef7`
- implementation commit: `88d4b8b4aaea32c8a8565e1460bd469b8f569f8d`
- authoritative workflow head: `291a9f6a71265c9e768960bbc0d00f039ca352c5`
- workflow run: `34748542204`
- job: `103700784152`
- artifact: `10315585117`
- digest: `sha256:27fd61945577078dd4dd16d85015b067073943ba87745dbdaa167450f81514c5`

## Frozen classification

`ITER073C_NONTRANSITIVE_ALL_FACES_EXACT_STIEMKE_SEPARATED_SCOPED`

All seven preregistered predicates passed.

## Exact result

For each of the four nontransitive source classes

`++-+`, `+-++`, `+-+-`, `+--+`,

for each of the four cycle bases `S0,S1,P0,P1`, and for every one of the 63 nonempty K4 edge subsets, an exact integer Stiemke/Gordan alternative certificate was found.  Total audited cases: `4 x 4 x 63 = 1008`.

Every certificate satisfies exactly

`A_S^T y >= 0`

componentwise, with at least one strictly positive component.  Independent weak-order/DAG recomputation agrees that the corresponding strict-positive kernel is absent.

Certificate complexity is very small:

- primitive `L1=1`: `1000/1008` cases;
- primitive `L1=2`: `8/1008` cases;
- minimum positive integer margin: `1`.

The positive control on source class `++++` correctly rejects universal separation on a known positive-admissible face.

## Interpretation

This converts the Iter073A Boolean no-face result into explicit exact separation/nonpinch data for the positive-real Schwinger cut-space of the reduced K4 common-epsilon family.  It is a stronger input for a future analytic estimate.

It is **not** yet a theorem that the `epsilon -> 0+` Schwartz action is bounded or convergent: complex deformation, distributional boundary values, numerator/group dependence and non-transverse pullback remain separate.  No physical vertex finiteness theorem, K5, G3, F9, G8, complete-QG or new-physics promotion follows.
