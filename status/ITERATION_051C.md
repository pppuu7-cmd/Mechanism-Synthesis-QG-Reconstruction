# Iteration 051C — preregistration: held-out range validation of factorized causal-sign RR masks

**Preregistered before implementation and production.**

## Motivation

Iter051A classified the frozen H1/H2 census as `K4_RR_SIGN_CLASS_NUISANCE_STABLE`: all eight factorized causal-sign classes retained identical 12-bit RR masks at two held-out nuisance points. This is scoped evidence only. Iter051C tests whether those exact masks survive two additional, wider and independently frozen nuisance points without refitting or changing the reference masks.

## Frozen held-out nuisance points

All values are exact rationals and the four external-flow components sum to zero.

- `H4`: `gamma=31/100`, `epsilon=31/1000`, `k=(41/100,-37/100,12/100,-16/100)`.
- `H5`: `gamma=245/100`, `epsilon=163/1000`, `k=(-22/100,47/100,-31/100,6/100)`.

These points are fixed in this preregistration before implementation/output inspection.

## Frozen reference masks from terminal Iter051A

Coordinates are the 12 ordered positions `tree/pair` with trees `S0,S1,P0,P1` and pairs `01,02,12`. The expected active positions are frozen as:

- `+++`: `P1/01`, `P1/02`, `P1/12`, `S0/01`.
- `++-`: `P0/12`, `P1/01`, `P1/02`, `P1/12`, `S0/01`, `S0/12`, `S1/12`.
- `+-+`: `P0/01`, `P0/02`, `P0/12`, `P1/01`, `S0/01`.
- `+--`: `P0/01`, `P0/02`, `P0/12`, `P1/01`, `P1/12`, `S0/01`, `S0/12`, `S1/12`.
- `-++`: `P0/01`, `P0/02`, `P0/12`, `P1/12`, `S1/01`, `S1/12`.
- `-+-`: `P0/01`, `P0/02`, `P0/12`, `S0/12`, `S1/01`.
- `--+`: `P0/01`, `P0/12`, `P1/01`, `P1/02`, `P1/12`, `S1/01`, `S1/12`.
- `---`: `P0/01`, `P1/01`, `P1/02`, `P1/12`, `S0/12`, `S1/01`.

No reference position or coefficient may be changed after production results are visible.

## Frozen matrix

`2 points × 8 sign classes × 4 trees × 3 pairs = 192 exact source lanes`, each with the existing identical F=1/EPRL control.

For every lane use the unchanged Iter051A sequential K4 RR diagnostic and unchanged factorized sign map `kappa_ab=sigma_a sigma_b`.

## Frozen validity gates

Every lane must satisfy:

1. source reconstruction validity;
2. control reconstruction validity;
3. exact zero control total and all control channels;
4. exact factorized-sign consistency;
5. no missing/duplicate matrix lane.

If any validity gate fails, aggregate classification is `ITER051C_CONTROL_OR_RECONSTRUCTION_INVALID` and no scientific stability claim is allowed.

## Frozen primary classification

`K4_RR_SIGN_CLASS_RANGE_STABLE` iff all validity gates pass **and**, for every sign class, both H4 and H5 12-bit RR masks exactly equal the corresponding frozen Iter051A reference mask.

Otherwise, if validity gates pass but at least one bit differs, classification is `K4_RR_SIGN_CLASS_RANGE_DEPENDENT`.

The aggregate must report, for each sign class and each point, the exact RR mask, active count, Hamming distance to the frozen reference, and changed positions. It must also report H4↔H5 Hamming distance.

## Claim locks

- This is a held-out range validation of a **sequential diagnostic**, not a proof of global sign universality.
- No fitted selector, threshold, counterterm or preferred order is allowed.
- No physical multivariate K4 amplitude is defined.
- K5 remains blocked regardless of a PASS here until a genuinely multivariate source/analyticity-selected K4 prescription passes its own covariance/control gates.
- No G3, physical F9 or G8 promotion follows from this gate.
