# Iter076A result — exact transitive overlap Möbius bookkeeping

Date: 2026-09-13

## Scientific classification

`ITER076A_TRANSITIVE_OVERLAP_MOBIUS_BOOKKEEPING_EXACT_SCOPED`

This is a scoped scientific PASS against the prospectively frozen gate in `status/ITERATION_076A_PREREG.md`.

## Authority / provenance

- preregistration commit: `71e765cf597131424e297fd6b70587fa33db7b63`
- initial production run `34758486126`: infrastructure-only failure before frozen predicates (`ModuleNotFoundError: No module named 'distributional'`); it is not a scientific classification
- authoritative retry head: `85ecaac967f78ac675552708f4fa2fc15f857e2d`
- authoritative retry run: `34758521734`
- job: `103727049365` (`exact-overlap-poset`)
- artifact: `10318116775` (`iter076a-transitive-overlap-mobius`)
- artifact digest: `sha256:23edf7fc462f8b2e9cf82a2c1701b4fcde7c6bbd4ffcbd0e5f5f2011c7e07f31`

The retry changed only the import-path execution environment; the frozen scientific inputs, predicates and interpretation rule were unchanged.

## Frozen predicates consumed from the raw artifact

All seven pass exactly:

1. `P1_ITER073D_SIX_FACE_HISTOGRAM_RECOVERED = true`
2. `P2_FINITE_DUPLICATE_FREE_INTERSECTION_POSET = true`
3. `P3_EXACT_MOBIUS_INCIDENCE_IDENTITY = true`
4. `P4_BASIS_INVARIANT_POSET_AND_TOP_COEFFICIENTS = true`
5. `P5_TRANSITIVE_ORBIT_POSET_SIGNATURE_EQUAL = true`
6. `P6_EVERY_ORIGINAL_FACE_IN_CLOSURE_AND_CHAIN_TO_TOP = true`
7. `P7_NONTRANSITIVE_NEGATIVE_CONTROL_EMPTY = true`

For every transitive source class and each of the four cycle bases, the nonempty-intersection closure has 13 support nodes with cardinality histogram

`1:1, 2:2, 3:3, 4:3, 5:3, 6:1`.

The top-column Möbius coefficient histogram is

`-1:4, 0:5, +1:4`.

The frozen nontransitive control has zero admissible proper faces in all four bases.

## Scientific meaning

The six positive proper faces of the reduced transitive K4 collision problem admit an exact finite, duplicate-free, basis-consistent and S4-orbit-consistent intersection-poset/Möbius bookkeeping object. This closes the combinatorial prerequisite for an analytically defined overlap treatment.

It does **not** define a subtraction prescription, finite part or counterterm; it does not compute the degree-two / nominal `epsilon^-1` coefficient; and it does not establish a causal-vertex finiteness/divergence theorem.

## Next allowed gate

A separately prospectively preregistered analytic gate may now combine this overlap poset with the actual degree-two local numerator/Jacobian data and explicit overlap terms. Its interpretation must distinguish a source-defined regulated coefficient from arbitrary finite-part subtraction. No cancellation may be inferred from the degree-zero/one result of Iter074A.

## Claim lock

No `NEW_PHYSICS_FOUND`; no complete-QG claim; no physical sector selection; no G3/F9/G8/K5 promotion; no arbitrary counterterm, fitted cancellation or preferred sequential order; published spectral `i epsilon` remains unchanged.