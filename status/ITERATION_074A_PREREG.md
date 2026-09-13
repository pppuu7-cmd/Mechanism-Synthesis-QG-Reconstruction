# Iter074A preregistration — independent-wedge common-epsilon leading-power cancellation

Date: 2026-09-13

This gate is frozen before production.

## Objective

For the reduced K4 denominator family, sum the common-`epsilon` kernel over all `2^6=64` **independent wedge signs** before taking the collision scaling limit, as required by the Eq.(5)/(6)-type EPRL-control analogue. Determine exactly whether the leading full-collision `epsilon^-3` and first Taylor `epsilon^-2` coefficients survive this independent-sign sum.

## Scope

This is a reduced denominator-skeleton theorem gate. It does not claim the source Toller numerator/group object, distributional Eq.(5)/(6), or K5.

## Frozen kernel

For a cycle basis `L` and `x=L y`,

`K_s(y,epsilon)=prod_e 1/(x_e-i epsilon s_e)`, `s_e=±1` independently.

The independent-sign sum is

`K_sum = sum_s K_s`.

The gate must verify algebraically, not assume, the factorization

`K_sum = prod_e [1/(x_e-i epsilon)+1/(x_e+i epsilon)] = prod_e 2 x_e/(x_e^2+epsilon^2)`.

Under the full-collision scaling `y=epsilon z`, define

`F_L(z)=prod_e 2 (Lz)_e / ((Lz)_e^2+1)`.

Then a smooth local amplitude/test factor has expansion `H(epsilon z)=H_0 + epsilon H_1(z) + epsilon^2 H_2(z)+...`; the nominal full-collision powers are `epsilon^-3`, `epsilon^-2`, `epsilon^-1`, ... .

## Frozen exact tests

Use all four unimodular cycle bases `S0,S1,P0,P1` and all 24 vertex permutations.

P1. Verify the one-edge identity and a direct exact 64-term assembly identity on a frozen set of non-singular rational samples.

P2. For every vertex permutation construct the exact induced `3x3` cycle-space matrix `M_g` satisfying the signed edge relabelling identity `Q_g L = L M_g`; require integer entries and `|det M_g|=1`.

P3. Verify exactly that

`F_L(M_g z) = chi(g) F_L(z)`,

where `chi(g)` is the product of the six canonical edge-orientation signs. Require `chi=+1` for even and `chi=-1` for odd vertex permutations.

P4. Compute the exact alternating Reynolds projection `R[q]=sum_g chi(g) q(M_g z)` for the monomial basis of total degree `0` and `1`. Require it to vanish identically for every such monomial and all four bases.

P5. Independently enumerate the linear-form arrangement flats. Apply the frozen power-count criterion: for a flat with dimension `q`, `N_grow` edge forms grow generically; a degree-`d` moment is absolutely integrable at infinity only if `N_grow > d+q` for every positive-dimensional flat. Require degrees `d=0,1` to pass.

P6. Degree `d=2` is a prospective boundary/overlap diagnostic: report whether the same absolute-integrability criterion passes or fails and identify the first obstructing flat(s). Do not infer its coefficient by symmetric prescription if it fails.

P7. Negative control: the alternating Reynolds projection of the exact degree-six edge product `prod_e (Lz)_e` must be nonzero, proving the alternating projector is not identically zero.

## Frozen interpretation

If P1-P5 and P7 pass, then the reduced independent-sign full-collision `epsilon^-3` and `epsilon^-2` coefficients vanish exactly for smooth local amplitude data because their absolutely convergent moment functionals transform in a nontrivial alternating S4 character.

If P6 fails, the nominal `epsilon^-1` full-collision term remains **overlap-open** and must be treated jointly with proper strata/forest subtraction; no symmetric cutoff may be promoted to a canonical value.

Allowed PASS classification:

`ITER074A_64SIGN_EPSM3_EPSM2_CANCEL_EXACT_EPSM1_OVERLAP_OPEN_SCOPED`

If the exact cancellation tests fail:

`ITER074A_64SIGN_LEADING_CANCELLATION_FAIL`

## Claim lock

No physical EPRL/causal-vertex finiteness theorem, no distributional Eq.(5)/(6), no K5/G3/F9/G8 promotion, complete QG or new physics follows from this reduced fixed-`epsilon` sign-sum theorem.
