# K5 exact cancellation resolver — compressed-source S5 diagnostic

Status: **PROSPECTIVELY FROZEN BEFORE DIAGNOSTIC OUTPUT**.

Parent scientific gate: `d6b0e805101c8590eafac71398cc2b1466691752`.
Current invalid-covariance production head: `051659255b1b1e7a5315f2b8dc2ec485615a0cfd`.
Frozen cycle: `(1,2,3,4,0)`.

## Objective

Test the already-authoritative compressed all-32 invariant-dual source/Wick coefficient dictionary `MATCH_COEFF` itself for exact S5 covariance, without using any physical corner coefficient, interpolation result, or cancellation depth.

For every perfect-matching key `((e1,e2),...)` in `MATCH_COEFF`:

1. transport each edge index by the frozen induced K5 edge permutation;
2. canonicalize each transported pair and the five-pair matching key;
3. derive the incidence-orientation sign `s_e` from whether the ordered edge orientation reverses under the vertex permutation;
4. multiply the Wick matching coefficient by `prod_e s_e`, because each of the ten edge incidence rows appears exactly once in a perfect matching;
5. compare the complete two-channel complex rational coefficient exactly to the transported dictionary entry.

Also verify the inverse-cycle round trip exactly.

No fit, threshold, random witness, physical numerator/action coefficient, or post-outcome convention change is allowed.

## Classifier

- `COMPRESSED_SOURCE_S5_COVARIANCE_EXACT`: all matching keys and both channel coefficients transform exactly and inverse-cycle round trip is exact.
- `COMPRESSED_SOURCE_S5_COVARIANCE_FAIL_EXACT`: at least one exact source coefficient mismatch exists under the frozen transport.
- `INVALID_IMPLEMENTATION`: key coverage, edge permutation, orientation-sign construction, or round trip is malformed.

A FAIL here is an implementation/control diagnosis for the current resolver S5 lane; it is not a physical K5 falsification and does not alter any frozen N/B/U support or scientific classifier.