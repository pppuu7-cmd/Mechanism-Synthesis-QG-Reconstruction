# Iter076N preregistration — exact amplitude orientation-selector provenance

**Date:** 2026-09-13

**Status:** `PREREGISTERED / FAIL_CLOSED`

**Source supplement:** `sources/CAUSAL_VERTEX_EXACT_ORIENTATION_PROVENANCE_SUPPLEMENT.md`

## Question

Does the exact source causal-vertex amplitude of Bianchi-Chen-Gamonal, including Eq. (4), Eq. (7), the boundary intertwiner/magnetic contractions and source-defined ordering/orientation data, contain or uniquely force a canonical orientation-odd selector equivalent on the non-degenerate locus to

`Omega_sigma(g)=sgn det([1; sigma_a F_a])`, `F_a=ghat_a T`,

so that the unique Iter076H Hodge line can be promoted from `{+H,-H}` to a physical signed `SOURCE_TO_K4_PUSHFORWARD`?

Mere constructibility from exact integration variables is not sufficient.

## Frozen target character

Any admissible exact selector `Omega` must satisfy simultaneously:

1. proper-Lorentz gauge invariance;
2. invariance under global causal reversal `sigma -> -sigma`;
3. odd `S5` covariance `Omega(pi.x)=sgn(pi) Omega(x)` under simultaneous relabeling;
4. root/gauge-fixing independence after transport;
5. no externally chosen vertex ordering, Levi-Civita convention or fitted sign;
6. agreement with the Iter076L Regge 4-volume orientation on non-degenerate Lorentzian Regge saddles, up to one frozen global convention.

## Exact source skeleton under audit

The source Eq. (4) uses

- `kappa_ab=sigma_a sigma_b`;
- `g_ab=g_b^-1 g_a`;
- a scalar product over all ten unordered wedges `a<b`;
- product Haar measure after one group gauge fixing;
- boundary magnetic/intertwiner contractions.

Eq. (7) is only the Cartan decomposition of each Toller function and may not be treated as new physical orientation input.

## Lane A — exact permutation character of the Eq. (4) skeleton

Enumerate all `120` permutations of five tetrahedron labels and verify the simultaneous relabeling action on:

- the ten unordered wedge slots;
- `kappa_ab`;
- the ten relative-element slots;
- the product measure/gauge-root transport.

PASS-A requires the computation to determine the scalar character carried by the source skeleton without inserting any extra orientation object.

Expected discriminator:
- trivial character `+1` for all permutations means no source-level alternating scalar is present in the displayed kernel;
- an intrinsic `sgn(pi)` character would be evidence for an exact selector source.

## Lane B — causal-data alternating-character no-go control

For each causal orbit represented by `sigma` Hamming classes `0/5`, `1/4`, `2/3`, compute stabilizers under `S5` and test whether each contains an odd permutation.

If every orbit has an odd stabilizer, any sign-equivariant scalar depending only on `sigma` or `kappa` is forced to vanish. This lane is a control/reproduction of the Iter076K obstruction and must not be promoted beyond that scope.

## Lane C — availability-versus-selection witness

Construct non-degenerate exact group-variable controls for which `Omega_sigma(g)!=0`. For every `pi in S5`, compare:

- `Omega_sigma(pi.x)/Omega_sigma(x)`;
- the character of the exact Eq. (4) slot/product skeleton under the same simultaneous relabeling.

PASS-C requires the expected separation to be explicit: the candidate may carry `sgn(pi)` while the source product skeleton carries the trivial scalar character. This lane proves a character mismatch, not amplitude non-existence.

## Lane D — boundary/intertwiner provenance firewall

Audit the source specification for any source-fixed contraction that supplies a five-tetrahedron alternating one-dimensional character independently of the chosen boundary state/basis.

The following do **not** count as exact provenance:

- a sign obtained only after choosing an ordered intertwiner recoupling basis;
- a boundary state deliberately chosen in the sign representation;
- the Iter076L semiclassical Regge orientation;
- importing the Engle proper-vertex orientation projector;
- manually inserting `Omega_sigma` into Eq. (4).

PASS-D requires the audit to classify whether such a source-fixed alternating contraction is present, absent in the published formula, or genuinely unresolved.

## Frozen terminal classifications

### Exact selector source-provenanced

Allowed only if A-D jointly identify a source-defined alternating object with the target covariance and no extra convention:

`ITER076N_EXACT_CAUSAL_VERTEX_SOURCES_CANONICAL_ORIENTATION_SELECTOR_REVIEW_SIGNED_P3_SCOPED`

### Exact source no-selector / semiclassical only

Use if the exact Eq. (4)/(7) structure has trivial scalar relabeling character, causal data cannot provide the sign character, and no source-fixed intertwiner contraction supplies it, while Iter076L/M remain valid:

`ITER076N_EQ4_EQ7_HAVE_NO_CANONICAL_S5_ODD_SELECTOR_EXACT_SIGNED_P3_BLOCKED_SEMICLASSICAL_ONLY_SCOPED`

### Unresolved boundary-contraction provenance

Use if A-C close but the source specification leaves an exact boundary/intertwiner sign character genuinely undecidable:

`ITER076N_BOUNDARY_INTERTWINER_ORIENTATION_CHARACTER_UNRESOLVED_EXACT_SIGNED_P3_BLOCKED_SCOPED`

## Promotion rule

Only the first classification permits Iter076O signed-P3 promotion.

Either blocked classification is terminal for the **source-native exact signed-P3 lane** and must be carried into the DSIR exit manifest as a no-go/blocker rather than repaired by convention.

## Claim locks

No `NEW_PHYSICS_FOUND`; no complete-QG claim; no G3/F9/G8/K5 promotion; no physical finiteness/divergence theorem; no replacement of the published spectral `i epsilon`; no arbitrary orientation insertion; no reinterpretation of semiclassical 4-volume orientation as an exact source factor.
