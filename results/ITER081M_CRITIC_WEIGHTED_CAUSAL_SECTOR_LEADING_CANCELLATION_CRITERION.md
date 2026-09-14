# Iter081M Critic exact theorem — weighted proper-causal K5 sector sums cancel the frozen r^-20 leading term iff their total weight is zero

Date: 2026-09-14
Status: **EXACT MINIMAL-SECTOR LEADING-ORDER CLASSIFICATION; WEIGHTED MODELS ARE NOT SOURCE-AUTHORIZED BY THIS NOTE**

## Authoritative input
Iter077I proves that on the frozen source-ordered all-`j=1/2` K5 common-collision ray, for each of the 32 boundary basis components `alpha`, every proper eta=+1 causal assignment has exactly the same nonzero leading contraction `C_alpha`.

Iter081K extends this by exact ten-edge parity to eta=-1: every proper causal assignment in both signature sectors has the same leading coefficient `C_alpha`.

Thus the result below uses no new numerical data.

## Eta=+1 weighted sum
Let `Sigma_+` be the 16 proper eta=+1 K5 orientation classes and assign arbitrary complex coefficients `w_sigma` independent of the collision radius `r`.

Define the weighted fixed-orientation sum

`I_alpha[w](r,Omega) := sum_(sigma in Sigma_+) w_sigma I_(alpha,sigma)(r,Omega)`.

At the authoritative Iter077I ray,

`I_(alpha,sigma)(r,Omega_0) = C_alpha r^-20 + O(r^-19)`

for every `sigma`. Hence exactly

`I_alpha[w](r,Omega_0) = C_alpha (sum_sigma w_sigma) r^-20 + O(r^-19)`.

Since `C_alpha != 0`, the `r^-20` coefficient vanishes **iff**

`sum_sigma w_sigma = 0`.

This condition is independent of `alpha`; the same scalar condition is necessary and sufficient to cancel the leading term simultaneously in all 32 frozen boundary components.

## Both proper causal signature sectors
Let `Sigma_causal=Sigma_+ union Sigma_-` contain all 32 proper causal assignments and assign arbitrary complex weights `w_(eta,sigma)`. Iter081K gives the same coefficient `C_alpha` for every element. Therefore

`I_alpha^causal[w] = C_alpha (sum_(eta,sigma) w_(eta,sigma)) r^-20 + O(r^-19)`,

and again the exact leading-cancellation criterion is

`sum_(eta,sigma) w_(eta,sigma) = 0`.

## Consequences

### Source weights
Beltran Eq. (36) uses unit weights in the eta=+ sector, so the total weight is `16`, not zero. The causal-only sum over both proper signature sectors with unit weights has total weight `32`, not zero. These source-defined sums therefore cannot cancel the frozen leading term, reproducing Iter081H/K.

### Nonnegative weights
For any weighting with real `w_sigma >= 0` and not all weights zero,

`sum_sigma w_sigma > 0`.

Therefore **no nontrivial nonnegative reweighting of the proper causal sectors can cancel the frozen `r^-20` leading singularity**.

This includes normalized probabilistic weights and positive symmetry averages.

### Signed or complex weights
Leading cancellation is algebraically possible only with a zero-sum signed/complex weighting. Such weights are not supplied by the audited BCG/Beltran causal source definitions and would constitute new model content unless independently motivated.

Moreover zero total weight removes only the leading `r^-20` coefficient. It says nothing about `r^-19`, lower singular orders, other collision strata, generic spins, or distributional extension uniqueness.

## Extension-selector independence
Even if a prospectively motivated zero-sum weighting cancelled the frozen leading coefficient, the act of choosing finite orientation weights does not by itself define values of a distribution supported on the common collision set. Any residual non-L1 summed object would still require extension analysis, and finite weighting is not a function-space selector for the already established Iter077Q tangential ambiguity.

In the currently source-defined unit-weight objects the stronger Iter081I result already applies directly: the infinite-dimensional `Q^n F delta_N` ambiguity survives.

## Classification
`ITER081M_SM_WEIGHTED_PROPER_CAUSAL_K5_R_MINUS20_LEADING_CANCELLATION_IFF_TOTAL_WEIGHT_ZERO_EXACT_THEOREM_SCOPED`.

## Claim ceiling
This theorem does not prohibit a future independently motivated signed/complex causal weighting, subtraction, analytic renormalization, or correlated boundary-value prescription. It states the exact necessary and sufficient condition for cancelling **only the frozen Iter077I leading coefficient** by radius-independent finite orientation weights. No full-vertex finiteness/divergence, generic-spin, regulator, multivertex, RG or complete-QG claim follows.
