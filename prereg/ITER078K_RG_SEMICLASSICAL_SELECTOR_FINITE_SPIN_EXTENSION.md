# Iter078K-RG preregistration — can published large-spin causal rigidity select the finite-spin K5 extension?

**Date:** 2026-09-14

## Scientific question

The causal-Toller source proves a large-spin asymptotic selection rule for nondegenerate Lorentzian coherent boundary data, with causal rigidity selecting the compatible Regge saddle and a single `exp(+i S_Regge/hbar)` contribution.

Can this semiclassical theorem uniquely select the exact finite-spin distributional extension that is underdetermined in Iter077L-M / Iter078E-G?

## Frozen source authority

Primary source: Bianchi-Chen-Gamonal causal vertex, especially the large-spin asymptotic analysis and causal-rigidity condition.

The asymptotic regime scales a fixed nondegenerate boundary geometry to large spins; schematically `j_ab -> lambda j_ab` with `lambda -> infinity`.

No additional analyticity in the discrete spin labels or recurrence relation connecting all finite-spin sectors is stated as part of the asymptotic theorem.

## Frozen counterexample construction

Use the already-authoritative all-`j=1/2` fixed-causal extension freedom.

Choose any nonzero admissible integrated order-zero shift

`Delta A_(1/2)(Psi) = ell(Psi)`

in the all-ten-spins-`1/2` sector, with `ell in H_B^*` nonzero, realized locally by `ell(Psi) delta_N` as in Iter078E/G.

Define a modified exact amplitude family across spin sectors by

- adding this shift only when every `j_ab=1/2`;
- adding zero extension shift in every other spin sector.

This is a finite-support modification in the discrete spin labels.

## Frozen checks

1. **Exact finite-spin difference:** at least one all-`j=1/2` boundary state changes by a nonzero amount.
2. **Off-collision source preservation:** the local modification is supported on `N`, so the source Toller object off the collision set is unchanged.
3. **Large-spin invisibility:** for every fixed nonzero Regge spin pattern `j_ab^0`, the uniformly scaled sequence `lambda j_ab^0` eventually leaves the single all-`1/2` sector permanently as `lambda -> infinity`; the modification is therefore identically zero along the asymptotic tail.
4. **Causal-rigidity preservation:** because the amplitude sequence is exactly unchanged for all sufficiently large `lambda`, the published leading saddle/phase and causal-rigidity statement are unchanged, not merely approximately unchanged.
5. **No hidden spin-analyticity condition:** audit the frozen source for a theorem requiring the finite-spin extension coefficients to be analytic/polynomial/recursively determined functions of the discrete spins in a way that forbids finite-support changes.

## PASS

PASS iff all checks hold.

Classification:

`ITER078K_RG_PUBLISHED_LARGE_SPIN_CAUSAL_RIGIDITY_DOES_NOT_SELECT_EXACT_FINITE_SPIN_K5_EXTENSION_COUNTEREXAMPLE_SCOPED`

Scientific consequence: the semiclassical causal result cannot be used as the missing exact finite-spin normalization/extension selector. It remains an important downstream constraint on any completed amplitude family but leaves finite-spin freedom unless supplemented by an exact cross-spin law.

## FAIL

FAIL iff the published asymptotic/source construction contains an exact finite-to-large-spin relation that forbids the finite-support modification and uniquely determines the `j=1/2` sector.

## Interpretation ceiling

PASS does not show that arbitrary extension choices can be made independently at all spins while retaining a global theory. It proves only that the published large-spin asymptotic theorem alone is insufficient to select the already-established minimal finite-spin ambiguity.

No statement about generic-spin ambiguity dimension, RG fixed points, continuum limit, Einstein recovery, G3 or complete QG.