# Iter077N adversarial control — exact wedge-branch cube preserves EPRL additive identities while retaining causal ambiguity

**Date:** 2026-09-14

## Purpose

Attack the Iter077M/N ambiguity with the strongest exact one-wedge source identity available in the repository: source Eq. (5) `T^+ + T^- = D` and the consequent Eq. (6) unconstrained sum over all `2^10` independent wedge branches reproducing the EPRL vertex.

This is an independent critic control. It does not alter the frozen Iter077M/N scientific contract.

## Construction

Let the ten independent wedge signs be `kappa_e in {+1,-1}` and let

`L = F_SU2 delta_N`

be the supported boundary functional from Iter077M/N. Define a branch-cube supported deformation

`Delta A_kappa = C [prod_e kappa_e] L`

for one common coefficient `C`.

## Exact one-edge cancellation

Fix the signs of the other nine wedges and sum over the two branches of one chosen edge `e0`:

`sum_(kappa_e0=+-1) Delta A_kappa = C [prod_(e != e0) kappa_e] [(+1)+(-1)] L = 0`.

Therefore the supported deformation disappears under `T^+ + T^- = D` on **any chosen wedge**. The same argument survives repeated partial sums, so every additive one-wedge control obtained by replacing any subset of Toller pairs with Wigner matrices is unchanged.

## Exact full EPRL sum

Summing all ten independent signs gives

`sum_kappa Delta A_kappa = C L prod_e [sum_(kappa_e=+-1) kappa_e] = 0`.

Hence the exact source Eq. (6) EPRL control sum is unchanged.

## Restriction to the source causal image

For a causal K5 pattern

`kappa_ab = sigma_a sigma_b`,

`prod_(a<b) kappa_ab = prod_a sigma_a^4 = +1`,

because every K5 vertex has degree four. Thus on **every one of the 16 distinct source-factorizable causal wedge patterns**,

`Delta A_(sigma_a sigma_b) = C L`.

The full exact EPRL branch-cube cancellation therefore does not force the fixed-causal supported coefficient to vanish.

## Conjugation / branch flip check

The repository source snapshot for the Toller conjugation identity shows that complex conjugation flips every wedge branch. Ten simultaneous sign flips leave `prod_e kappa_e` unchanged because ten is even. Moreover the all-wedge-flipped pattern lies outside the factorizable causal K5 image. Thus that identity does not produce a same-causal cancellation selecting `C=0`; at most additional reality/conjugation conditions could restrict the phase of `C`.

## Verdict of this control

The exact source additive identities Eq. (5)/(6) do **not** remove the supported local/integrated ambiguity. There exists an explicit deformation of the complete independent-sign branch cube that preserves every one-wedge additive control and the full EPRL sum while inducing the same nonzero ambiguity coefficient on every fixed causal K5 sector.

This strengthens only the scoped non-selection result. It does not prove that refinement, cylindrical consistency, RG, transfer-matrix positivity, regulator independence, or another future physical condition cannot select the extension.