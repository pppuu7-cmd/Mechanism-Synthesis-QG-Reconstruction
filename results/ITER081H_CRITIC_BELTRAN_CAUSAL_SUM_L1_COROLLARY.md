# Iter081H Critic exact corollary — Beltran eta=+1 K5 causal-sector sum retains the Iter077I non-L1 leading term

Date: 2026-09-14
Status: **EXACT COROLLARY FROM EXISTING AUTHORITATIVE SOURCE-ORDERED DATA; NOT A FULL VERTEX DIVERGENCE THEOREM**

## Inputs already independently established

### Beltran v2 source definition
Carlos E. Beltran, `arXiv:2603.22661v2`, defines orientation-dependent EPRL-KKL amplitudes `A_v^{epsilon}` and the positive-signature causal vertex

`A_{gamma_v}^{+} := sum_{[epsilon_ab], eta=+1} A_v^{epsilon_ab}`

with unit coefficient for every globally admissible `eta=+1` orientation assignment (Eq. 36). For a K5/4-simplex vertex the causal sign condition is, in the `eta=+1` convention,

`epsilon_ab = sigma_a sigma_b`,

modulo the global reversal `sigma_a -> -sigma_a`. Thus there are `2^(5-1)=16` distinct eta=+1 wedge-sign assignments.

Beltran Eqs. (25)-(27) also make clear that the ordinary EPRL-KKL amplitude is recovered only by the unrestricted sum over all wedge assignments, while each fixed assignment is realized by the corresponding product of Toller matrices.

### Iter077I authoritative source-ordered K5 theorem
`results/ITER077I_SM_SOURCE_ORDERED_JHALF_K5_L1_RESULT.md`, authoritative run `34786586785`, result commit `6e1dd1e6bb5e26d607e2c249ff6f8978f0df922a`.

The prospective Iter077I preregistration `c30f1556ad5d0bc92fac3be91b31c052f789cb63` froze exactly:

- all ten `j_ab=1/2`;
- the complete 32-dimensional five-node boundary-intertwiner basis;
- one source-ordered Toller K5 integrand at a time;
- the 16 factorized causal patterns `kappa_ab=sigma_a sigma_b`, with one `sigma` gauge-fixed by global reversal;
- an exact nondegenerate common-collision ray;
- source order `one-wedge Toller construction -> ten-wedge K5 product -> full boundary contraction -> group integration`.

Lane C then proved for all `32*16=512` component/assignment pairs that the leading contraction is nonzero and, more strongly, **exactly equal to the all-plus leading coefficient for the same boundary component**. The algebraic reason frozen before execution was

`prod_(a<b) kappa_ab = prod_a sigma_a^4 = +1`

on K5.

Iter077I also proved wedge power `beta^-2`, total homogeneous power `q=-20`, transverse boost dimension `d=12`, and nonzero leading coefficient on an open angular neighborhood for all 32 components.

## Exact identification of the two 16-element sets
Beltran `eta=+1` K5 assignments and Iter077I Lane-C assignments are the same sign set:

`epsilon_ab = sigma_a sigma_b = kappa_ab`,

with the same global reversal redundancy. No extra local branch patterns are introduced and no admissible eta=+1 pattern is omitted.

Therefore Iter077I did not merely sample 16 convenient signs: it exhaustively evaluated the leading term for every source-defined eta=+1 K5 causal orientation class relevant to Beltran Eq. (36).

## Finite-sum leading coefficient
Fix one of the 32 boundary components `alpha`. Let its all-plus Iter077I leading coefficient on the frozen collision ray be `C_alpha`, with `C_alpha != 0`.

Iter077I proves for every one of the 16 eta=+1 assignments `sigma`:

`I_{alpha,sigma}(r,Omega_0) = C_alpha r^(-20) + O(r^(-19))`

in the frozen source-ordered leading expansion (up to the already-frozen common nonzero normalizations).

Beltran Eq. (36) uses a finite unit-weight sum, hence off the collision the sum can be taken at integrand level by linearity:

`I^+_alpha = sum_sigma I_{alpha,sigma}`.

Consequently,

`I^+_alpha(r,Omega_0) = 16 C_alpha r^(-20) + O(r^(-19))`,

and the leading coefficient is nonzero for every `alpha=1,...,32`.

Because the individual exact leading contractions are equal, there is no orientation-sector cancellation at order `r^-20` in the eta=+1 causal sum on this frozen ray.

## Local absolute-integrability corollary
The same Iter077I transverse dimension `d=12` applies. Therefore the radial absolute-integrand exponent of the eta=+1 summed leading term is

`d-1+q = 12-1-20 = -9`,

and the first-moment margin is

`q+d = -8 < 0`.

Since `16 C_alpha != 0`, continuity of the ordinary off-collision leading angular coefficient gives an open angular neighborhood with the same nonzero leading behavior.

Thus, for every one of the 32 frozen all-j=1/2 boundary basis components, the **Beltran eta=+1 causally summed source-ordered K5 integrand is not locally absolutely L1 at the common collision**.

Classification of this Critic corollary:

`ITER081H_SM_BELTRAN_ETA_PLUS_CAUSAL_K5_ORIENTATION_SUM_RETAINS_NONZERO_R_MINUS20_LEADING_TERM_ALL_32_COMPONENTS_NOT_LOCALLY_L1_EXACT_COROLLARY_SCOPED`.

## Relation to Iter081G cycle-space identity
Iter081G independently rewrites the same eta=+1 16-sector sum as 64 Eulerian/cycle-space channels in `a=(T^++T^-)/2` and `b=(T^+-T^-)/2`. The present corollary supplies the missing physical source-ordered information on the frozen Iter077I ray: after actual K5 incidence and full frozen boundary contraction, the complete eta=+1 sum has a nonzero `r^-20` coefficient.

No separate all-edge-channel survival theorem is needed to establish the summed leading non-cancellation on this ray; Iter077I's exhaustive 16-assignment equality is already stronger for that purpose. A channel-resolved statement would be additional structure, not a prerequisite for the L1 corollary.

## Important scope ceiling
This result is **only a local absolute-integrability obstruction** for the all-j=1/2 source-ordered eta=+1 causal sum on the validated Iter077I collision geometry.

It does NOT prove:

- that the Beltran causal vertex does not exist as a distributional, oscillatory, principal-value, Hadamard-finite-part, or source-selected correlated boundary value;
- that the group integral is divergent in every admissible sense;
- generic-spin failure;
- regulator dependence or regulator independence;
- absence of cancellations in subleading terms or after a separately defined correlated extension prescription;
- a unique K5 extension selector;
- causal multivertex E3/E4/E6 closure;
- Han-stack boundedness or RG closure;
- `NEW_PHYSICS_FOUND`, F9, G3, G8, or complete quantum gravity.

Beltran v2 itself states that finiteness of the generalized causal vertex remains an open question; this corollary narrows that question by establishing a source-ordered local `L1` obstruction in the frozen minimal-spin sector, without answering distributional existence.

## Research consequence
Do **not** spend a new production gate merely asking whether the 16 eta=+1 orientations cancel the Iter077I `r^-20` term: existing authoritative data plus the source definition already answer that question exactly — they do not cancel.

The next nonredundant causal-K5 question is instead whether a source-motivated correlated boundary-value/extension prescription acts on this summed non-L1 object and, if so, whether it selects a unique element of the Iter077Q extension space `W`. Any such prescription must be prospectively frozen before computation and must respect the source-order firewall.
