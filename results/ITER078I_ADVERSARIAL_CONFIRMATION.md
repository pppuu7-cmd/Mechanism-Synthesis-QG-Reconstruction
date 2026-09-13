# Iter078I-RG adversarial confirmation — EPRL recovery is an underdetermined sum constraint, not an individual causal-extension selector

**Date:** 2026-09-14

## Reviewed authority

- preregistration `prereg/ITER078I_RG_EPRL_SUM_EXTENSION_SELECTOR.md`, commit `37a9a49e1b0e6cd26241b7595f71e36f86a22323`;
- result `results/ITER078I_RG_EPRL_SUM_EXTENSION_SELECTOR_RESULT.md`, commit `f424d440abecfd8b65b5b3fc483b4777a64cbbc1`;
- primary source identities frozen in the repository: `T^+ + T^- = D` and EPRL recovery by the unconstrained ten-wedge sign sum.

## Adversarial issue 1 — arbitrary `ell` is too broad after the Iter078E stabilizer audit

The Iter078I result phrases the compensating deformation using arbitrary nonzero gauge-invariant `ell in H_B^*`. The critic's exact Iter078E causal-label stabilizer audit shows that gauge invariance alone is not the complete source-compatibility condition in a fixed causal sector: node permutations preserving the causal sign partition act nontrivially on the 32-dimensional boundary basis and reduce the constant order-zero invariant subspace to dimension `2/3/5` depending on causal partition type.

Therefore Iter078G's full-32 **source-compatible** ambiguity interpretation is over-broad and may not be imported unchanged into Iter078I.

This does not invalidate the Iter078I nonselection theorem, because the counterexample needs only one nonzero supported source-compatible direction, not all 32. The already established compact direction

`L = F_SU2 delta_N`

is sufficient: it is gauge-invariant, built from the complete K5 boundary spin network, nonzero on the frozen boundary space, and compatible with the fixed-causal source constraints in Iter077M/N.

## Adversarial issue 2 — the two-sector shift does not by itself preserve every one-wedge additive identity

The preregistered Iter078I question asks whether the **full unconstrained EPRL sector sum** can select an individual causal extension. For that frozen question the two-sector deformation

`Pbar_s -> Pbar_s + L`,

`Pbar_t -> Pbar_t - L`

is enough: it leaves the total `2^10` sum unchanged while changing the chosen causal sector.

However, that two-sector construction alone does not prove the stronger sentence that every pairwise one-wedge identity `T^+ + T^- = D` can simultaneously be imposed after extension. A generic two-sector shift will spoil some fixed-nine-sign pair sums.

The stronger statement nevertheless survives independent adversarial testing because it was already established by the exact branch-cube construction in `results/ITER077N_ADVERSARIAL_BRANCH_CUBE_CONTROL.md`:

`Delta A_kappa = C [prod_e kappa_e] L`.

For any chosen wedge `e0`, summing the two values of `kappa_e0` cancels exactly, so every one-edge `T^+ + T^- = D` additive control is preserved. The complete `2^10` EPRL sum also cancels. Yet for every factorized causal K5 pattern `kappa_ab=sigma_a sigma_b`,

`prod_(a<b) kappa_ab = prod_a sigma_a^4 = +1`,

so every causal sector receives the same nonzero supported deformation `C L`.

Thus the exact source algebra has a nontrivial supported kernel even under the stronger family of one-wedge additive constraints.

## Source-ordering firewall

This review does not replace the causal-Toller source ordering by a termwise contact product. The deformation acts only on the supported extension freedom at the common collision after the source-ordered sector products have been defined off the collision set. No interchange of one-wedge spectral limits and K5 products is assumed.

## Boundary completeness

The witness `L` is not a representative scalar boundary component. It is the complete K5 compact boundary functional previously checked on all 32 frozen all-`j=1/2` intertwiner basis states; `16/32` components are nonzero in the exact critic control.

## Verdict

`CONFIRMED_SCOPED`

The frozen Iter078I scientific claim is correct: exact EPRL recovery of the unconstrained `2^10` sector sum does not uniquely select an individual factorized causal-sector extension.

The proof should be read with the known source-compatible witness `L`, not arbitrary unconstrained `ell in H_B^*`. The simple two-sector construction proves the preregistered full-sum nonselection; the stronger branch-cube construction independently proves nonselection even while preserving every one-wedge additive identity.

## Claim ceiling

No full classification of the 1024-sector ambiguity space follows. No generic-spin theorem follows. The result does not prove that all possible coupled cross-sector conditions fail, and it does not supply the missing causal refinement/RG map, unique K5 extension, regulator independence, G3, continuum limit or complete quantum gravity.