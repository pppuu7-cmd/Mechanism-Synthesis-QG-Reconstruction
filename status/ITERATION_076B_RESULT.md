# Iter076B result — exact covariant degree-two overlap-jet complex

Date: 2026-09-13

## Scientific classification

`ITER076B_TRANSITIVE_DEGREE2_OVERLAP_JET_COMPLEX_EXACT_COVARIANT_SCOPED`

This is a scoped scientific PASS against the prospectively frozen gate in `status/ITERATION_076B_PREREG.md`.

## Authority / provenance

- preregistration commit: `ddafd0c3df126d30f0135931abb2349f69464bad`
- implementation commits: `906304040af0e56893a6d37de3a580183e978430`, `ad8380fea04ddfb3964e03dc6b254cb9bbcc0ed3`, `ea7ae2d74ad48c345ff80b6dd2413844c7a029b8`
- authoritative production/workflow head: `30633fb7d4b6de6c5880c6e19116ff1bfa1d2473`
- run: `34761228718`
- source-class jobs:
  - `++++`: job `103734304527`
  - `+++-`: job `103734304537`
  - `++--`: job `103734304441`
  - `+---`: job `103734304563`
- aggregate job: `103734341502`
- aggregate artifact: `10318722679` (`iter076b-degree2-overlap-jet-aggregate`)
- aggregate digest: `sha256:dc73bd0be09b53029160ae841189e315f21427b0d02508872079dd83d44fd005`
- raw lane artifacts/digests:
  - lane 0: `10318764004`, `sha256:1d672db24de2011235953e1fa131de561766d4ba41fa2d63fa3bbae53e33f979`
  - lane 1: `10319355648`, `sha256:0c109aff1a7aebd82d776ebdb3551bdc5ba049f08eacff6c905adf5066f8eb86`
  - lane 2: `10318936806`, `sha256:350cba6d915540e0203a8b2f44ebc36f55495d4cb1052d7720ecfaee80f8f01a`
  - lane 3: `10319021537`, `sha256:660f6ba9ba852430d4b6029595f8044bd60a7ecac815098e7bfa8c40dea5725e`

All raw lane artifacts and the frozen aggregate were consumed; green CI alone was not used as the scientific classification.

## Frozen predicates

All pass:

- P0 all four independent lanes present;
- P1 Iter076A overlap poset/Möbius data exactly reproduced;
- P2 quadratic restriction rank is monotone under deeper intersections;
- P3 all comparable restriction diagrams commute exactly over the rationals;
- P4 complete quadratic-overlap signature is invariant across `S0,S1,P0,P1`;
- P5 the signature agrees across the four S4-related transitive source classes;
- P6 degree-two data remain nontrivial on proper/intersection strata;
- P7 the nontransitive `++-+` control has zero transitive-face complex in all four bases.

The common exact signature `(support-cardinality, nullity, quadratic-rank, mu-to-top)` is

`(1,2,3,0); (2,1,1,0)x2; (3,0,0,-1); (3,1,1,0)x2; (4,0,0,+1)x3; (5,0,0,-1)x3; (6,0,0,+1)`.

## Scientific meaning

The reduced transitive K4 overlap geometry supports a well-defined exact homogeneous-quadratic restriction complex that is cycle-basis invariant and S4-orbit consistent. In particular, degree-two local data are not killed automatically: a two-dimensional overlap stratum carries quadratic rank 3 and several one-dimensional strata carry rank 1.

Therefore neither the Iter074A degree-zero/one cancellation nor the Iter076A Möbius bookkeeping authorizes an `epsilon^-1` cancellation claim. The actual coefficient requires the **source-derived numerator/Jacobian quadratic jet** and an analytically justified overlap/boundary-value treatment.

## Exact next blocker

The current repository/source snapshot defines the full Eq.(4) causal vertex as a four-`SL(2,C)` Haar integral of ten Toller factors and Eq.(7) gives a Cartan/magnetic decomposition, but no validated source-derived map currently identifies the local numerator/Jacobian quadratic jet of the reduced K4 denominator-skeleton coordinates used in Iter068-076. Inventing that jet, choosing a Euclidean metric on cycle coordinates, or treating Möbius coefficients as physical subtraction coefficients is forbidden.

The next coefficient gate is therefore **BLOCKED_OBJECT_DEFINITION** until that map is derived source-faithfully. Analysis/source derivation is preferred over additional denominator-only compute.

## Claim lock

No physical causal-vertex finiteness/divergence theorem; no `epsilon^-1` value or cancellation; no arbitrary counterterm, fitted cancellation or preferred sequential order; no K5/G3/F9/G8 promotion; no complete-QG or new-physics claim.