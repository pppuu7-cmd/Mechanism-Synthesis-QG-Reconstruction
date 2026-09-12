# Iteration 055 result — K4 signed-normal positive-circuit atlas and S4 covariance

**Status:** terminal

**Classification:** `K4_SIGNED_NORMAL_CIRCUIT_ATLAS_S4_NONCOVARIANT`

Authoritative run: `34719188955`

Artifact: `10305313738`

Artifact digest: `sha256:bbc7834a7db83d214d45e7f65b180d5102707e641327c1ca88c6148ba64266af`

Preregistration commit: `5ef00a72f034d2dbf943ccd5e0c7ab5662bb8d21` before implementation/output.

## Exact audit

For every one of 8 factorized causal sign classes and all four frozen K4 tree/cycle bases, Iter055 exhaustively tested all 56 edge supports of size 1..4 for exact support-minimal positive dependences of

`M = diag(s) A`.

Totals:

- 32/32 signed-normal lanes valid;
- 56 support tests per lane;
- **1792 exact support tests** total;
- complete minimal-positive-circuit atlas is **basis-invariant**;
- all 192 class × vertex-permutation maps have valid edge bijections and valid naive factorized sign-class maps;
- nevertheless the circuit atlas is **not S4 covariant** under that naive class-only relabeling.

## Exact S4 class orbits under naive factorized sigma relabeling

- `{+++}`;
- `{+--, -+-, --+}`;
- `{++-, +-+, -++, ---}`.

But circuit counts are not constant on the nontrivial orbits:

- `+++`: 3 circuits;
- `+--`: 3, while `-+-` and `--+`: 0;
- `++-` and `---`: 3, while `+-+` and `-++`: 0.

For each obstructed class the atlas contains exactly 3 minimal positive circuits with size histogram `2 × size-3 + 1 × size-4`; feasible classes have zero positive circuits, matching the Iter054 strict-chamber taxonomy.

## Structural consequence

The Iter054 4/8 partition is exact and basis-independent **in the frozen oriented edge-flow representation**, but the raw class label `s_e = sigma_a sigma_b` is not sufficient to transport that signed-normal geometry under arbitrary vertex relabeling.

The likely missing datum is the orientation reversal of the canonical edge-flow variable. If an old oriented edge `(a,b)` maps to a new canonically oriented edge in the opposite direction, then `x_old = -x_new`; algebraically

`x_old - i s_old epsilon = -(x_new - i (-s_old) epsilon)`.

Therefore the effective pole sign in the new oriented-flow coordinate acquires an orientation cocycle. This is a precise hypothesis for the next preregistered gate; it is not retroactively inserted into Iter055.

## Interpretation lock

- do not promote the raw Iter054 feasible classes to physical causal sectors;
- do not interpret Iter055 as a failure of physical permutation covariance of the causal vertex;
- the demonstrated failure is for the **naive factorized-class-only action on the frozen oriented-flow surrogate**;
- an orientation-aware denominator/signed-normal covariance audit is required next.

## Claim locks

No physical amplitude, K5, G3, F9, G8, new-physics, or general causal-EPRL no-go claim follows from this result.
