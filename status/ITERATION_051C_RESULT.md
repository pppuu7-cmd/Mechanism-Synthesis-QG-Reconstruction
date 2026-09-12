# Iteration 051C result — wider held-out RR sign-class range validation

**Status:** terminal

**Classification:** `K4_RR_SIGN_CLASS_RANGE_STABLE`

Authoritative run: `34717183041`

Aggregate artifact: `10306111279`

Artifact digest: `sha256:8828bbe7b2d46a58072d4b4c9e486f2902a206a1c964efa15882e0bc44383b6f`

Preregistration commit: `1d3cd2b28d4f33cb18b89408962628254a2ed920` before implementation/output.

## Frozen held-out audit

Matrix: **192 exact lanes** = H4/H5 × 8 factorized causal sign classes × 4 tree bases × 3 ordered RR pairs, each with identical F=1 control.

Held-out points:

- H4: `gamma=31/100`, `epsilon=31/1000`, `k=(41,-37,12,-16)/100`;
- H5: `gamma=245/100`, `epsilon=163/1000`, `k=(-22,47,-31,6)/100`.

The eight Iter051A H1/H2 12-bit RR masks were frozen as references before H4/H5 production.

## Terminal aggregate

- lanes valid: **192/192**;
- all F=1 control totals and channels: **exactly zero**;
- all factorized-sign checks: **PASS**;
- all lane/reference matches: **PASS**;
- total H4/H5 vs frozen-reference Hamming distance: **0**;
- total H4↔H5 Hamming distance: **0**.

RR nonzero counts per 12-bit class mask remain exactly:

- `+++`: 4;
- `++-`: 7;
- `+-+`: 5;
- `+--`: 8;
- `-++`: 6;
- `-+-`: 5;
- `--+`: 7;
- `---`: 6.

Thus the complete sign-class RR masks found on H1/H2 survive two substantially displaced held-out nuisance points H4/H5 without a single bit transition.

## Interpretation

This upgrades the earlier statement from two-point nuisance stability to a wider four-point frozen range validation. It supports the claim that the observed sequential-RR mask taxonomy is not a fragile accident of the original gamma/epsilon/external-flow choices tested so far.

It does **not** establish global sign universality, a physical contour prescription, or a causal amplitude. In particular Iter055 independently shows that the signed-normal affine-chamber surrogate is not naively S4 covariant under class-only relabeling, so RR range stability and physical permutation covariance remain separate questions.

## Claim locks

- no fitted RR selector;
- no global sign theorem;
- no physical amplitude or K5 claim;
- no G3 PASS;
- no F9/G8 promotion;
- no new-physics claim.
