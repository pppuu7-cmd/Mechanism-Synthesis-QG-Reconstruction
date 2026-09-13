# Iter073C preregistration — exact nontransitive cut-space separation certificates

Date: 2026-09-13

## Objective
For the four source K4 sign classes with no positive-admissible full or proper face in Iter073A (`++-+`, `+-++`, `+-+-`, `+--+`), construct exact rational Stiemke/Gordan alternative certificates for every nonempty edge subset. This strengthens a Boolean no-face census into explicit nonpinch separation data.

## Scope
Reduced K4 common-epsilon signed cut-space geometry only. A separation certificate is a necessary ingredient for later integration-by-parts/boundary-value estimates; it is not by itself a boundedness or finiteness theorem.

## Frozen object
For each source sigma, each cycle basis `S0,S1,P0,P1`, and each nonempty subset S of the six K4 edges, form `A_S = L_S^T diag(s_S)`.

For every case search for an exact integer vector `y in Z^3` such that `w = A_S^T y >= 0` componentwise and `w != 0`. Canonicalize by primitive gcd/sign normalization and lexicographically minimal `L1` norm, using a deterministic exhaustive integer cube enlarged until a certificate is found or a frozen hard cap is reached.

## Frozen predicates
P1. Every one of the `4 x 4 x 63 = 1008` nonempty-subset cases has an exact certificate.
P2. Every certificate satisfies `A_S^T y >= 0` with at least one strictly positive component.
P3. Independent weak-order/DAG recomputation marks the same subset infeasible.
P4. Feasibility verdicts are basis-independent; certificate coordinates need not be.
P5. Report primitive certificate `L1` norms, positive-component counts, and minimal positive integer margin.
P6. S4 relabelling preserves the certificate-existence census/support-size histogram.
P7. Positive-control source class `++++` must fail the universal-separation claim on at least one known positive-admissible face.

## Classification
PASS: `ITER073C_NONTRANSITIVE_ALL_FACES_EXACT_STIEMKE_SEPARATED_SCOPED`

otherwise: `ITER073C_EXACT_SEPARATION_CERTIFICATE_FAIL`

## Claim lock
A PASS certifies absence of positive-real Schwinger cut-space pinches in the frozen reduced family for these source classes. It does not prove epsilon->0 boundedness/convergence, exclude complex/distributional singular behavior, or establish a physical causal-vertex finiteness theorem, K5, G3, F9, G8, complete QG or new physics.
