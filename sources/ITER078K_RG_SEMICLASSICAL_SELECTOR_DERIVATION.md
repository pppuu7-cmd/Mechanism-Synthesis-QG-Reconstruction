# Iter078K-RG derivation — large-spin causal rigidity cannot select a finite-support low-spin extension

**Date:** 2026-09-14

Prospective contract: `prereg/ITER078K_RG_SEMICLASSICAL_SELECTOR_FINITE_SPIN_EXTENSION.md`, commit `9fc2e38be7593ed3923aad06aab47fdc7232b35a`.

## Primary asymptotic authority

Bianchi-Chen-Gamonal derive the large-spin asymptotics of the fixed-causal vertex for a coherent boundary state peaked on a nondegenerate Lorentzian Regge 4-simplex.

The boundary spins are uniformly rescaled

`j_ab -> lambda j_ab`, `lambda -> infinity`,

and the causal amplitude has, in the compatible causal class, a single Regge exponential with the source prefactor/scaling, while incompatible causal data are suppressed faster than any power. The source also stresses that for nondegenerate Lorentzian data the saddle points have nonzero boosts `beta_ab != 0`; the distributional boundary at `B=0` does not contain these ordinary saddle points.

This is an asymptotic theorem on a large-spin ray in the discrete spin labels. It does not state an exact recurrence or analyticity condition determining every finite-spin amplitude from the asymptotic tail.

## Exact finite-support counterexample

Iter078G establishes that in the all-ten-spins-`j=1/2` fixed-causal sector the integrated order-zero extension ambiguity saturates the 32-dimensional boundary dual.

Choose any nonzero `ell in H_B^*`. Define a new exact amplitude family by

`A'_j = A_j + ell` if every one of the ten spins equals `1/2`,

and

`A'_j = A_j`

for every other spin assignment.

Locally the change is realized by the same supported distribution `ell(Psi) delta_N`, so the exact off-collision source-ordered Toller object is unchanged.

Now fix any nonzero Regge spin pattern `j_ab^0` entering the source asymptotic theorem. Along the uniformly scaled sequence

`j_ab(lambda)=lambda j_ab^0`,

the equality `j_ab(lambda)=1/2` for all ten wedges can hold, at most, at isolated finite values of `lambda`. For all sufficiently large `lambda`, the extension shift is exactly zero.

Therefore

`A'_(lambda j^0) = A_(lambda j^0)`

identically for the entire asymptotic tail.

The leading phase, power, Hessian prefactor, causal-rigidity selection and all subleading terms computed from sufficiently large `lambda` are unchanged because the exact amplitude values in that regime are unchanged.

## Source-condition audit

The primary asymptotic construction treats the spin labels as discrete representation labels and performs a uniform large-spin scaling. The frozen source does not provide an exact finite-difference recurrence, spin analyticity postulate, or cross-spin normalization theorem that forbids a finite-support change at `j=1/2`.

The exact identity `T+ + T-=D` is a wedge-sign relation at fixed representation labels, not a relation between different spin magnitudes. Iter078I separately proves that the EPRL sector sum does not select an individual causal extension even at fixed spin.

## Scientific consequence

The published semiclassical causal-rigidity theorem is a necessary downstream test for a completed causal amplitude family, but it is not an exact finite-spin extension selector.

In particular, preserving the correct `exp(+i S_Regge/hbar)` large-spin behavior does not remove the already-proven finite-spin all-`j=1/2` ambiguity.