# Iteration 054 result — exact K4 sign-compatible affine contour chambers

**Status:** terminal

**Classification:** `K4_CAUSAL_SIGN_CHAMBER_CLASS_DEPENDENT`

Authoritative run: `34718445213`

Aggregate artifact: `10305511999`

Artifact digest: `sha256:32f701abd1359ccb60ab22d14edc012f886c47d7225d8088a7337dcb48ae6c42`

## Frozen question

For each factorized K4 causal sign class and each frozen tree/cycle basis, with exact cycle matrix `A` and causal edge-sign vector `s`, define

`M = diag(s) A`.

Ask whether there exists one common affine cycle-contour direction `v` such that

`M v > 0`.

Unlike Iter053, the six induced edge-shift magnitudes need not be equal; only their frozen causal signs and strict positivity are required.

## Terminal aggregate

- exact lanes: **32/32 valid**;
- tree/cycle-basis consistency: **PASS**;
- feasible causal classes: **4/8**;
- feasible in all four bases: `+-+`, `-++`, `-+-`, `--+`;
- infeasible in all four bases: `+++`, `++-`, `+--`, `---`.

Exact integer witnesses for feasible lanes are basis-dependent coordinate representatives of the same strict-chamber property. Examples in `P0`:

- `+-+`: `v=(-2,1,2)`;
- `-++`: `v=(2,1,-2)`;
- `-+-`: `v=(2,-1,2)`;
- `--+`: `v=(-2,3,-2)`.

For the four infeasible classes, exact positive-dependence obstruction certificates are present and basis-stable. Frozen first supports are:

- `+++`: edges `[0,1,2] = [01,02,03]`;
- `++-`: edges `[1,3,5] = [02,12,23]`;
- `+--`: edges `[0,3,4] = [01,12,13]`;
- `---`: edges `[0,1,2] = [01,02,03]`.

## Relation to Iter053

Iter053 proved that **0/8** classes reproduce the original equal-magnitude six-edge shift vector by one common affine translation (`A v=s`). Iter054 is weaker and more general: it asks only for the same sign chamber with unequal positive edge magnitudes. Four classes pass this broader criterion.

Therefore:

- equal-`epsilon` one-vector reconstruction remains excluded for all eight classes;
- a one-vector **sign-compatible** affine tube direction remains available in four classes in the frozen oriented-flow representation.

## Critical covariance hold

The 4/8 partition is **not yet authorized as a physical causal-sector selection**. It must first pass a separate exact vertex-relabeling/S4 covariance audit. A class label can mix graph sign data with the fixed orientation convention of the six edge-flow variables. Iter055 was prospectively preregistered before consuming this terminal result and audits the complete minimal-positive-circuit atlas under tree-basis changes and all 24 K4 vertex permutations.

If that covariance gate fails, Iter054 remains a valid statement about the frozen oriented coordinate representation, but its raw class partition cannot be promoted to a physical invariant without an orientation-corrected reformulation.

## Claim locks

- no physical causal-sector acceptance/rejection yet;
- no physical amplitude finiteness/divergence theorem;
- no general contour no-go theorem;
- no K5 or G3 PASS;
- no F9/G8 promotion;
- no fitted edge-shift magnitudes or post-hoc contour weights.
