# Iteration 048 — terminal result

## Frozen gate
Exact decomposition of the unchanged sequential K4 finite-part commutator into the diagnostic channels

`FP_u = R_u + A_u`,

with `R_u = 2*pi*i*(upper-half-plane residues of the same proper rational remainder)` and `A_u = -i*pi*a_-1`. The discarded polynomial quotient remains metadata only. No counterterm or preferred order was introduced.

Frozen matrix: cases A/B × trees S0,S1,P0,P1 × pairs 01,02,12 = 24 lanes, with ordinary EPRL/no-contact `F=1` controls.

## Authoritative provenance
- main implementation commit: `ad7e10d8a3083ee84b72037b2d035e7c365cb024`
- workflow run: `34708541480`
- aggregate job: `103593666033`
- aggregate artifact: `iter048-aggregate`, artifact ID `10302632044`
- artifact digest: `sha256:8557404d30df06358fca43d2fa702c5b9e57e746f3c02077370475a670080f3c`

## Terminal machine result
Classification: `K4_FP_OBSTRUCTION_MIXED_CHANNELS`.

All 24/24 lanes are valid. All 24/24 source totals are nonzero. All 24/24 control totals are exactly zero. All one-step, ordered and channel reconstructions are exact.

Overall source-channel counts:
- `RR` nonzero: 8/24
- `RA` nonzero: 24/24
- `AR` nonzero: 24/24
- `AA` nonzero: 24/24

Pattern counts:
- `RESIDUE_ONLY`: 0
- `INFINITY_ONLY`: 16
- `MIXED`: 8
- `SOURCE_TOTAL_ZERO`: 0
- `UNRESOLVED`: 0

The split is identical at the count level in held-out cases A and B: each has 8 `INFINITY_ONLY` and 4 `MIXED` lanes. Controls show no channel cancellation: every control channel commutator is itself exactly zero.

Representative raw lanes confirm that pair `01` can be `MIXED` in both cases, e.g. A/S0/01 and B/S1/01, while previously inspected pair `02` examples are `INFINITY_ONLY`. The aggregate does not by itself prove that the RR selector is exactly pair `01`; that becomes the next prospective gate.

## Scientific interpretation
The K4 sequential-FP obstruction is not reducible to a universal single `a_-1`/infinity channel: a residue-residue commutator contributes in a strict subset of lanes, while A-containing channels contribute in every source lane. Conversely, the residue sector is not universally obstructed either, because 16/24 lanes have exactly zero `RR` commutator.

This is a structural localization result inside the frozen sequential 1D finite-part algebra. It is **not** a theorem of physical causal-vertex divergence or ill-definition, does not define a multivariate amplitude, and does not authorize K5, G3, F9 or G8 promotion.

## Next gate
Before constructing a multivariate subtraction/forest prescription, test whether the 8-lane `RR` activation is covariant under cycle-coordinate relabeling or merely tied to positional labels in the implementation. Iter049 is therefore a preregistered cycle-coordinate permutation covariance audit of the `RR` selector.
