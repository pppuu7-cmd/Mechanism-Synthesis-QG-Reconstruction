# Iteration 014 — Toller endpoint pole/cancellation map

## Status

`PASS / STRUCTURAL_POLE_CANCELLATION_CONFIRMED`

## Campaign

Four independent high-precision GitHub jobs scanned

- `gamma = 0.2, 0.5, 1.2, 2.0`;
- `j = 1/2, 1, 3/2, 2`;
- `l = j, j+1, j+2`;
- all allowed magnetic `p` values;
- six endpoint scales down to `beta = 5e-4`.

This gives 42 EPRL sectors per gamma and 168 sectors total.

For each sector the scan fitted the local powers

- `|t+| ~ beta^q_plus`;
- `|t-| ~ beta^q_minus`;
- `|t+ + t-| ~ beta^q_sum`;
- cancellation ratio `|t+ + t-|/(|t+|+|t-|)`.

The exactly integer-degenerate hypergeometric continuation was evaluated by a symmetric high-precision analytic limit in the numerical backend; the Toller formula itself was not altered.

## Result

Across all four gamma values:

- finite sectors: `168 / 168`;
- sectors with an individual Toller branch pole: `168 / 168`;
- sectors with cancellation gain greater than one-half power: `168 / 168`.

Observed branch powers were approximately

`q_plus ~= q_minus in [-7, -2]`.

After addition, the Wigner/EPRL combination was regular:

`q_sum ~= 0, 1, or 2`

(up to the small finite-grid fitting error).

The cancellation gain ranged approximately from two to nine powers of `beta`. In the strongest scanned sectors, the endpoint ratio

`|t+ + t-|/(|t+|+|t-|)`

fell to order `1e-29`--`1e-33` on the smallest beta point.

The pattern is essentially unchanged over the tested gamma range: the endpoint pole order is controlled mainly by the representation/spin sector rather than by a special choice of Immirzi parameter.

## Small-spin cross-check

For `j=1/2`:

- `l=1/2`: each single branch scales approximately as `beta^-2`, while `t+ + t-` scales as `beta^0`;
- `l=3/2`: each branch scales approximately as `beta^-3`, while `t+ + t-` scales as `beta^1`.

Including the radial `sinh^2(beta)` measure but no magnetic recoupling, four fixed branches scale approximately as

- `beta^-6` for `l=1/2`;
- `beta^-10` for `l=3/2`;

whereas the additive four-leg products scale approximately as `beta^2` and `beta^6`, respectively.

Thus none of the 16 uncontracted branch masks is real-axis endpoint-integrable in these test sectors, while the additive EPRL combination is.

## Interpretation

The numerical obstruction found in Iteration 011 is structural, not a random precision failure. The Toller split exposes singular components whose poles cancel in the ordinary Wigner/EPRL sum.

Therefore a finite causal implementation must respect the analytic Feynman `i epsilon` definition and/or demonstrate cancellation at a larger correlated contraction level before taking the regulator away. It is not legitimate to assign ordinary real-axis B4 integrals independently to the singular branches.

## Gate impact

- existence and order of separate-branch endpoint poles: `CONFIRMED`;
- `T+ + T- = D` pole cancellation: `CONFIRMED_NUMERICALLY` over 168 sectors;
- ordinary integrate-first branch B4: `REJECTED` as generic causal building block;
- precontract-before-integrate possibility: pending Iteration 013 heavy stream;
- Feynman `i epsilon` vertex implementation: next mandatory route if precontraction remains non-integrable.
