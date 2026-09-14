# Iter081K Critic exact corollary — summing both Beltran causal signature sectors still retains the K5 r^-20 non-L1 leading term

Date: 2026-09-14
Status: **EXACT MINIMAL-SECTOR SOURCE-ORDERED COROLLARY; NOT A FULL VERTEX DIVERGENCE THEOREM**

## Source motivation
Beltran `arXiv:2603.22661v2` decomposes the EPRL-KKL orientation sum into three classes: proper causal assignments with `eta=+1`, proper causal assignments with `eta=-1`, and non-causal assignments (Eq. 23). The paper also discusses the interpretation of the two signature conventions and the possibility of retaining causal configurations while excluding non-causal ones.

For a K5 vertex the proper causal assignments have

`epsilon_ab = eta sigma_a sigma_b`,

modulo global reversal of all five `sigma_a`. Hence there are 16 distinct assignments for each fixed `eta`, 32 proper causal assignments total when both signatures are included.

## Authoritative leading-sign input
Iter077I preregistration `c30f1556ad5d0bc92fac3be91b31c052f789cb63` prospectively froze the exact `j=1/2` source-Toller small-collision branch transport:

- `T^+` leading matrix shape `+M(v_ab)`;
- `T^-` leading matrix shape `-M(v_ab)`;
- common nonzero scalar factor identical in magnitude.

For eta=+1 patterns `kappa_ab=sigma_a sigma_b`, Iter077I run `34786586785` proved that all 16 assignments and all 32 boundary components have the same nonzero leading contraction `C_alpha` as the all-plus assignment.

## eta=-1 parity
Changing `eta=+1` to `eta=-1` reverses every wedge sign:

`epsilon_ab^- = - epsilon_ab^+`.

At the frozen leading `j=1/2` source-Toller order, this multiplies each of the ten wedge matrices by `-1`. K5 has ten wedges, so the full contracted leading tensor gains

`(-1)^10 = +1`.

Therefore, for every eta=-1 causal assignment paired with its eta=+1 assignment and for every frozen boundary component,

`C_alpha^(eta=-1,sigma) = C_alpha^(eta=+1,sigma) = C_alpha != 0`.

No new numerical assumption enters this step; it is exact parity applied to the already validated Iter077I leading branch transport.

## Sum over all proper causal assignments
Define the causal-only orientation sum that retains both proper signature sectors and excludes non-causal assignments:

`I_alpha^(causal-only) = sum_(eta=+-1) sum_([epsilon],proper eta) I_alpha^epsilon`.

There are 16 assignments in each sector and every leading coefficient equals `C_alpha`. Hence on the authoritative Iter077I collision ray,

`I_alpha^(causal-only)(r,Omega_0) = 32 C_alpha r^-20 + O(r^-19)`

for every one of the 32 frozen all-`j=1/2` boundary basis components.

Thus the eta=+ and eta=- causal signature sectors add **coherently** at leading order; they do not cancel the K5 common-collision singularity.

## Local L1 consequence
The transverse dimension remains `d=12`. Therefore

`q=-20`, `q+d=-8`, `d-1+q=-9`.

Since `32 C_alpha != 0`, the causal-only summed source-ordered integrand is not locally absolutely `L1` on an open angular neighborhood of the frozen common-collision witness for every minimal boundary component.

Classification:

`ITER081K_SM_BELTRAN_BOTH_PROPER_CAUSAL_SIGNATURE_SECTORS_RETAIN_NONZERO_R_MINUS20_LEADING_TERM_ALL_32_COMPONENTS_NOT_LOCALLY_L1_EXACT_COROLLARY_SCOPED`.

## Relation to Iter081G
Iter081G found algebraically

`C_+ + C_- = 32 sum_(S Eulerian, |S| even) b_S a_(E\S)`.

The present result supplies source-ordered physical leading information on the frozen K5 collision patch: the combined proper-causal sum has a nonzero `r^-20` contraction. In particular, keeping both signatures does not reproduce the unrestricted EPRL branch cancellation, because the non-causal orientation sectors are still absent.

## Extension ambiguity
Exactly as in Iter081I, any supported Iter077Q ambiguity `Q^n F delta_N` is invisible off `N` and can be added to an extension of this causal-only summed object without changing the source-defined off-collision sum or increasing the maximal scaling degree. Thus including both proper causal signature sectors also does not, by itself, provide an extension selector.

## Scope ceiling
This proves neither divergence nor nonexistence of the generalized causal vertex as a distributional/oscillatory/source-selected object. It is minimal-sector, local and absolute-integrability scoped. It does not include the non-causal orientation sectors; the unrestricted `2^10` branch sum is a different object and reconstructs ordinary EPRL-KKL. No generic-spin, regulator, multivertex, RG, G3, F9/G8/K5, `NEW_PHYSICS_FOUND` or complete-QG claim follows.

## Research consequence
Neither of the two source-natural finite causal orientation sums resolves the local obstruction:

1. eta=+ only: leading coefficient `16 C_alpha` (Iter081H);
2. eta=+ plus eta=- proper causal sectors: leading coefficient `32 C_alpha` (this corollary).

The only source-known branch sum that restores the ordinary Wigner/EPRL cancellation is the unrestricted sum over all wedge assignments, which also includes non-causal configurations and therefore is not a causal-sector rescue.
