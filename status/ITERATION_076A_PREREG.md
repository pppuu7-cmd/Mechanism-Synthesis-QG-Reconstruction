# Iter076A preregistration — transitive overlap intersection-poset / Möbius bookkeeping

Date: 2026-09-13

This gate is frozen before implementation and production.

## Objective

Construct the exact overlap bookkeeping object required before any degree-two / nominal `epsilon^-1` coefficient can be assigned on the transitive K4 collision strata. The gate is purely combinatorial/algebraic: it does **not** assign finite parts, counterterms, amplitudes or physical coefficients.

Starting from the six positive-admissible proper faces per transitive source class established by Iter073D, close their edge-support family under nonempty intersection, adjoin the full six-edge support as the top element, and compute the exact incidence-poset Möbius function.

## Frozen inputs

- transitive source classes: `++++`, `+++-`, `++--`, `+---`;
- all four unimodular cycle bases `S0,S1,P0,P1`;
- proper positive faces are generated independently by the Iter073D exact criterion, not hard-coded from a single class;
- nontransitive `++-+` is the negative control and must have zero positive proper faces.

## Frozen predicates

P1. Recompute exactly six positive proper faces per transitive class in every basis with the Iter073D histogram `(3,1)x2,(4,1)x1,(5,2)x3`.

P2. Build the closure under all nonempty intersections of these supports plus the six-edge top. Require a finite duplicate-free support poset and exact inclusion partial order.

P3. Compute the integer Möbius function `mu(A,B)` recursively for every comparable pair `A subseteq B`; verify the defining incidence identity `sum_{A<=Z<=B} mu(A,Z)=delta_{A,B}` exactly.

P4. Record the top-column coefficients `mu(A,TOP)` and the rank/cardinality histogram of the intersection closure. Require basis invariance within each source class.

P5. Require the complete unlabeled poset signature and multiset of top-column Möbius coefficients to agree across the four S4-related transitive source classes. This is only an overlap-bookkeeping covariance test; no physical sector meaning is attached.

P6. Every original Iter073D proper face must appear as a node of the closure and participate in at least one comparable chain to TOP; report, but do not fit or discard, zero Möbius coefficients if any occur.

P7. Negative control `++-+` must reproduce zero positive proper faces and therefore no transitive six-face overlap object.

## Frozen interpretation

PASS classification:

`ITER076A_TRANSITIVE_OVERLAP_MOBIUS_BOOKKEEPING_EXACT_SCOPED`

This means that the reduced transitive K4 proper-stratum family has an exact, basis-consistent, S4-orbit-consistent intersection-poset/Möbius bookkeeping object that can be used as a prerequisite for a later analytically defined overlap subtraction. It does **not** prove that a source-defined subtraction exists, does not choose a finite-part prescription, and does not determine whether the nominal `epsilon^-1` coefficient vanishes or survives.

Scientific FAIL classification:

`ITER076A_TRANSITIVE_OVERLAP_MOBIUS_BOOKKEEPING_OBSTRUCTED_SCOPED`

if any frozen exact predicate fails.

Infrastructure/implementation failure is reserved for inability to execute the exact audit; no criterion may be weakened after viewing production output.

## Claim lock

No physical causal-vertex finiteness/divergence theorem; no arbitrary counterterm or preferred sequential order; no K5/G3/F9/G8 promotion; no complete-QG or new-physics claim. Published spectral `i epsilon` and the distinction between absolute integrability, conditional/PV finite part and source-defined distributional boundary value remain unchanged.
