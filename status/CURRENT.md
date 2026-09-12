# Current MSQGR research state

**Date:** 2026-09-13

- Candidate: `CRQN v0.2` (`CARRIER_SELECTED`)
- Established/source-backed mechanism union: `F1-F8`
- Physical F9 (`CAUSAL_ANALYTICITY_RG_INVARIANT`): `BLOCKED`
- G3 quantum dynamics: `OPEN`
- G8 novelty: `BLOCKED_CONVERGENCE_ONLY`
- K5 distributional/vertex extension: `BLOCKED`
- Active front: `ITERATION_058 / STRONG_TOURNAMENT_POSITIVE_CIRCULATION_THEOREM`

## Closed results controlling the front

The Lorentzian EPRL/Toller carrier, exact `T+ + T- = D` control, native general Toller kernel, residue-series pure-boost kernel and direct ten-wedge topology are validated. Ordinary EPRL booster factorization is not a valid fixed-Toller-branch causal carrier; direct relative-group causal integration remains the selected architecture.

Key K4 chain:

- Iter046 `K4_FINITE_PART_ORDER_OR_FOREST_DEPENDENT`.
- Iter047 `K4_PAIRWISE_FP_COMMUTATOR_OBSTRUCTION_LOCALIZED`.
- Iter048 `K4_FP_OBSTRUCTION_MIXED_CHANNELS`.
- Iter049 `K4_RR_SELECTOR_NONCOVARIANT`.
- Iter050 `K4_RR_FACTOR_DEPENDENT_BEYOND_POLE_COUNT`; denominator control `DENOMINATOR_POLE_TOPOLOGY_SIGN_GEOMETRY_STABLE`.
- Iter051 `K4_RR_EXACT_RESIDUE_GEOMETRY_SEPARATION` + `K4_RR_CANCELLATION_DOMINATED_SUBSET`.
- Iter051A `K4_RR_SIGN_CLASS_NUISANCE_STABLE` on H1/H2.
- Iter051B `K4_RR_BEYOND_PREREG_RESIDUE_STRUCTURE`.
- **Iter051C terminal `K4_RR_SIGN_CLASS_RANGE_STABLE`**; run `34717183041`, artifact `10306111279`, digest `sha256:8828bbe7b2d46a58072d4b4c9e486f2902a206a1c964efa15882e0bc44383b6f`. 192/192 exact H4/H5 lanes valid, controls exact zero, total reference Hamming distance 0 and H4↔H5 Hamming distance 0. This is wider frozen range stability, not a global sign theorem.
- Iter052 `K4_RRR_CANONICAL_ANTISYMMETRY_OBSTRUCTION_NONZERO`; run `34716166419`, artifact `10305101542`; 36/36 valid, controls exact zero, source full-S3 antisymmetrizer nonzero 9/36. No coefficient refitting.
- Iter053 `K4_CAUSAL_SHIFTS_NO_GLOBAL_UNIFORM_CONTOUR_TRANSLATION`; run `34718231048`, artifact `10305646600`. Exact equal-magnitude `A v=s` fails for all 8 factorized classes in all four bases.
- Iter054 `K4_CAUSAL_SIGN_CHAMBER_CLASS_DEPENDENT`; run `34718445213`, artifact `10305511999`. Strict `diag(s)A v>0` with unequal positive magnitudes is feasible for factorized representatives `+-+,-++,-+-,--+` and obstructed for `+++,++-,+--,---`; all 32/32 lanes valid and basis-consistent.
- Iter055 `K4_SIGNED_NORMAL_CIRCUIT_ATLAS_S4_NONCOVARIANT`; run `34719188955`, artifact `10305313738`. Complete minimal-positive-circuit atlas is basis-invariant but not covariant under naive class-only S4 relabeling. Raw 4/8 split is therefore not a physical sector statement.
- **Iter056 terminal `K4_ORIENTATION_COCYCLE_RESTORES_COVARIANCE_FACTOR_CLASS_NOT_CLOSED`**; run `34719504197`, artifact `10306082820`, digest `sha256:72ca7c70d08a93264c2caface34397326a54185bcb53d8dbcd9e80d1c1eacc9c`. The algebraically forced oriented-edge reversal cocycle restores exact signed-normal covariance in **3072/3072** checks. Only 32/192 class/permutation actions remain inside the original eight factorized pole-sign vectors; the effective oriented pole-sign closure contains 48 distinct vectors.
- **Iter057 terminal `K4_ORIENTED_SIGN_SPACE_EXACT_BASIS_AND_S4_COVARIANT`**; run `34719626599`, artifact `10305747534`, digest `sha256:53cb834063b722aed716ad524ec79de76c25d6a63087456c227db84264c380c4`. Complete `{+,-}^6` domain: 64 sign vectors, 256 basis lanes, **14,336** exact support tests, **1,536/1,536** orientation-aware S4 actions covariant. There are exactly four S4 orbits of sizes 8,8,24,24; only one 24-orbit is strict-chamber feasible (24 vectors), the other 40 vectors are obstructed. The original factorized subset intersects the two 24-orbits and has orientation-aware closure size 48.

Durable result notes include `status/ITERATION_051C_RESULT.md` and `status/ITERATION_052_RESULT.md` through `status/ITERATION_057_RESULT.md` where applicable.

## Structural interpretation now established for the surrogate

Physical causal wedge data `kappa_ab=sigma_a sigma_b` and the orientation-dependent spectral pole-sign vector must not be identified. Under vertex relabeling, rewriting every edge flow in canonical orientation introduces an exact orientation cocycle `q`; the effective pole signs transform as `s_eff=q*s` after edge permutation. This fully explains the Iter055 naive noncovariance at the signed-normal level.

The complete 64-vector pole-sign domain is naturally the set of orientations of K4, i.e. four-vertex tournaments. Iter057's four exact S4 orbits coincide with the four unlabeled tournament types. The feasible 24-orbit has score sequence `[2,2,1,1]`; the obstructed 24-orbit is transitive `[3,2,1,0]`; the two size-8 obstructed orbits have `[3,1,1,1]` and `[2,2,2,0]`.

This suggests a graph-flow theorem: a strict sign-compatible cycle-space direction exists exactly when the tournament is strongly connected. That claim is being tested prospectively in Iter058 rather than retroactively promoted from Iter057.

## Active Iter058 — strict chamber iff strongly connected tournament

Preregistered **before implementation/output** at commit `51c3e04da81652060a3bc76c2bad5c9825faecca`; implementation `11513a2554ad26ef5320091eedd04337cab5454f`; workflow `fe135f1aa2befdb959a2c40238ee98b9b54373de`; PR #60 merged as `dff2803ca240760861233c766b447e026fea16ae`; run `34719879504`.

Frozen theorem gate over all 64 oriented K4 sign vectors:

`exists x in ker(B) with s_e x_e>0 on every edge`

iff the tournament defined by `s` is strongly connected.

Strong cases receive a deterministic constructive positive circulation formed by summing directed cycles, with exact reconstruction in all four cycle bases. Non-strong cases receive an exact one-way directed-cut conservation obstruction. The complete positive-circuit criterion is independently recomputed, and orientation-aware S4 orbit invariants are checked again.

Frozen classifiers: `ITER058_GRAPH_FLOW_AUDIT_INVALID`; `K4_STRICT_CHAMBER_STRONG_TOURNAMENT_EQUIVALENCE_FAIL`; or `K4_STRICT_CHAMBER_IFF_STRONGLY_CONNECTED_TOURNAMENT`.

## Next allowed decisions

1. Consume Iter058 only from its terminal artifact and record a durable result.
2. If Iter058 passes, elevate the K4 affine-surrogate statement from a 64-vector enumeration to a graph-flow characterization: feasibility = strongly connected tournament / strictly positive circulation. Do **not** promote that to a physical Toller-sector selection.
3. The next physics-critical front must be source-backed: derive/test the actual Toller branch transformation under group inversion / wedge-order reversal for `T^(kappa)(g_b^-1 g_a)`. Toller branches are functions, not representations, so denominator-surrogate covariance cannot substitute for the full vertex law.
4. Only after a full branch/order-reversal law is established may the graph-flow chamber criterion be tested as a candidate analyticity input for the direct causal vertex.
5. Do not fit residue selectors, cancellation coefficients, counterterms, or preferred orders. K5 remains blocked until a source/analyticity-selected K4 construction passes tree/cycle-basis/permutation/order independence and exact EPRL control.

## Claim locks

- no `NEW_PHYSICS_FOUND` or complete-QG claim;
- no physical causal-vertex finiteness/divergence theorem;
- no universal causal-EPRL or contour no-go theorem;
- no physical causal-sector selection from tournament/chamber results;
- no G3 PASS or F9/G8 promotion;
- no arbitrary counterterm, fitted cancellation coefficient, or preferred sequential order;
- do not replace the published spectral `i epsilon` prescription with an unproved `beta+i epsilon` rule;
- keep absolute integrability, conditional/PV finite part and source-defined distributional amplitude distinct.
