# Iter082C-SM prereg — K5 analytic stratified forest extension operator gate

Status: **PROSPECTIVE GATE — frozen before Iter082C implementation/production**  
Date: 2026-09-14

## Purpose
Construct and audit an actual local **distribution-extension operator class** for the source-ordered K5 Toller amplitude on the physically active K3/K4/K5 collision strata, using the exact Iter082B 72-forest architecture. This gate is not a selector gate and must not choose finite subtraction constants, scales, invariant-jet coefficients, or preferred physical normalization.

The mathematical motivation is position-space extension/forest theory (Epstein–Glaser scaling-degree extension; diagonal-arrangement / forest constructions). These sources motivate the extension mechanism only. They are not authority that the resulting finite parts are the physical spin-foam amplitude.

## Authoritative input locks
Use exactly the current MSQGR authority:

- source order: `one-wedge spectral/spinor integration -> Toller function -> ten-wedge product -> full boundary contraction -> K5 group integration / extension`;
- Iter082A physical partial-stratum witnesses;
- Iter082B exact divergent blocks and forests;
- K3: codim `d_3=6`, scaling degree `sd_3=6`, divergence degree `omega_3=0`;
- K4: codim `d_4=9`, scaling degree `sd_4=12`, divergence degree `omega_4=3`;
- K5: codim `d_5=12`, scaling degree `sd_5=20`, divergence degree `omega_5=8`;
- 16 divergent blocks = 10 K3 + 5 K4 + 1 K5;
- 72 compatible forests; 20 maximal chains `K3 subset K4 subset K5`;
- node-wise compact right-SU2 covariance, S5 covariance and true boundary linearity;
- historical Iter077Q physical infinite tangential `W` is `INVALID_SOURCE_LOCK`;
- deepest demonstrated scalar invariant jet subspace is a lower bound `dim J_inv=28`, not the full extension-space dimension;
- CDSR T4 firewall: same-graph reassociation is selector-blind;
- CDSR T5 diagnostic: context-jet distinguishability is not selection.

## Local extension operator to construct
For each divergent collision block `B`, choose an equivariant tubular chart with normal variables `x_B` and tangential/co-graph variables `y_B`. Let `Delta_B={x_B=0}`.

For an S5/right-SU2-covariant smooth cutoff/weight `chi_B` satisfying

- `chi_B=1` on a neighborhood of `Delta_B`;
- all choices for permuted blocks are related by covariance, not by independent fitted constants;

freeze the weighted Taylor projector on test functions

`T_B^(omega) phi = chi_B(x_B,y_B) * sum_{|alpha|<=omega_B} x_B^alpha/alpha! * (partial_x^alpha phi)(0,y_B)`

and the subtraction operator

`W_B = 1 - T_B^(omega)`.

For a distribution `t_B^0` defined away from `Delta_B`, define the minimal local extension functional class by

`<R_B^chi t_B^0, phi> := <t_B^0, W_B phi> + sum_{|alpha|<=omega_B} <c_{B,alpha}(y_B), (partial_x^alpha phi)(0,y_B)>`.

The coefficients `c_{B,alpha}` remain symbolic and are restricted only by established source symmetries / normal-jet representation theory. They are **not selected** in this gate.

## Forest recursion to audit
Because the exact K5 divergent forests contain nested chains but no two disjoint divergent blocks, define the recursive extension along every maximal chain

`B3 subset B4 subset B5`

by applying local subtraction to the smallest unresolved stratum first, then to the induced quotient singularity, while carrying all finite local coefficients symbolically.

The implementation must construct both nested descriptions associated with a maximal chain and compare them only modulo the allowed supported counterterm space. Literal equality of different subtraction orders is **not** a frozen requirement unless it follows algebraically; a difference confined to allowed local jets is classified as scheme dependence, not as a failure or a selector.

## Required exact tasks

### A. Single-block jet annihilation
For each `omega in {0,3,8}`, verify symbolically that `W_B phi` has vanishing normal derivatives through order `omega` at `x_B=0` for a generic polynomial test jet through order `omega+2`.

### B. Scaling-degree extension criterion
Encode the exact condition `omega_B = sd_B - codim_B` for K3/K4/K5 and verify that Taylor subtraction through `omega_B` raises test-function vanishing sufficiently for the standard scaling-degree extension theorem to apply locally. This is a mathematical extension-theory use, not a new spin-foam source claim.

### C. Symmetry covariance
Reconstruct all 16 blocks and all 120 S5 permutations. Verify that one unlabeled cutoff/projector template transported by permutation gives

`pi T_B pi^-1 = T_{pi(B)}`

and the same for `W_B`. No vertex-label-dependent finite coefficient is permitted.

For the deepest K5 normal fiber, verify compatibility with the established `SO(3) x S5` scalar invariant jet grading `(1,0,1,0,3,0,7,0,16)` through order 8, without asserting exhaustiveness.

### D. Forest-chain construction
Reconstruct all 20 maximal `K3 subset K4 subset K5` chains independently from subsets. For each chain, build the exact nested Taylor-subtraction metadata on the quotient/co-graph variables and verify that every divergent stratum is subtracted once at its allowed normal order.

### E. Order/scheme comparison
For a generic finite polynomial test-jet model adapted to a maximal chain, evaluate at least two legal nested subtraction order descriptions. Classify their difference:

- `IDENTICAL` if exactly zero;
- `SUPPORTED_ALLOWED_SCHEME_DIFFERENCE` if it is expressible entirely by allowed normal jets on K3/K4/K5 strata with orders bounded by `0/3/8` respectively;
- `INVALID_FOREST_OPERATOR` if a nonlocal/off-stratum difference survives or an allowed order is exceeded.

Do **not** set supported differences to zero by fitted constants.

### F. Negative controls
Must reject:

1. under-subtraction (`omega_B-1`) for each nonzero omega block;
2. over-subtraction promoted as source-required uniqueness;
3. a vertex-label-dependent cutoff/coefficient tag that breaks S5 covariance;
4. termwise contact-distribution multiplication before the ten-Toller product/full boundary contraction;
5. treating same-graph reassociation identity as an independent selector equation;
6. inserting numerical values for symbolic finite coefficients/scales.

## Frozen classifications

### Strong PASS
`ITER082C_SM_K5_LOCAL_TAYLOR_FOREST_EXTENSION_CLASS_CONSTRUCTED_WITH_SYMBOLIC_SUPPORTED_SCHEME_FREEDOM_EXACT_SCOPED`

iff A-F pass, every active K3/K4/K5 stratum receives a valid local extension operator, all 20 chains are covered, and all order dependence is zero or confined to the allowed supported counterterm space.

### Partial / blocked
`ITER082C_SM_LOCAL_BLOCK_EXTENSIONS_EXIST_BUT_FOREST_CHAIN_COMPATIBILITY_NOT_ESTABLISHED_SCOPED`

if A-C pass but D/E fail without a source/provenance error.

### Failure
`ITER082C_SM_CANDIDATE_FOREST_EXTENSION_OPERATOR_INVALID_EXACT_SCOPED`

if subtraction leaves an off-stratum/nonlocal remainder, violates source order/symmetry, or exceeds the allowed scaling-degree jet bounds.

`INVALID_IMPLEMENTATION_OR_PROVENANCE` for chronology, hard-coded PASS outcomes, missing controls, or post-hoc criterion changes.

## Interpretation ceiling
A strong PASS constructs a **mathematically valid source-covariant local extension class**, not a unique physical amplitude. It would prove neither that the chosen Taylor/weight scheme is source-derived nor that different symbolic finite parts are physically equivalent. It does not select K3/K4 coefficient functions, deepest 28/16 jets, scales, or subtraction constants.

No claim of:

- `UNIQUE_K5_EXTENSION`;
- `PHYSICAL_SELECTOR_DERIVED`;
- exact total ambiguity dimension;
- `28 CONDITIONS SUFFICE`;
- regulator independence;
- causal E3/E4/E6 closure;
- RG closure;
- CRQN v0.3;
- `NEW_PHYSICS_FOUND`;
- complete quantum gravity.

If strong PASS is obtained, the next interface to CDSR is the symbolic coefficient domain plus the actual physical insertion/context maps; CDSR then audits rank/residual ambiguity/no-smuggling independently.