# Iter078H-RG result — the BF-like ambiguity tensor is not closed under the exact fixed-j=1/2 1-to-5 control map

**Date:** 2026-09-14

## Provenance

- Prospective preregistration: `prereg/ITER078H_RG_FULL32_ORDERZERO_1TO5_TENSOR_MAP.md`, commit `ccf47cb8e3f9e9500d99d7c2c5342fd59be04cb0`.
- Implementation: `distributional/iter078h_rg_full32_orderzero_1to5.py`, commit `6a11820662ff5c655ab39120b3df6c6844f5e6ca`.
- Workflow/production head: `.github/workflows/iter078h_rg_full32_orderzero_1to5.yml`, commit `7c48f183b995291bbe9c449809b275cd94a0f93c`.
- Authoritative terminal run: `34790730688`.
- Lane A artifact `10328082225`, digest `sha256:58867c37a9ed7d109334b7f5ab08f263d96c1c146cf50e21cb02a1ba511d5aa1`.
- Lane B artifact `10327781817`, digest `sha256:af75ba10a87901381a5c3695145e1cd370e2865c0d2ab822050e51b128cde3bd`.
- Lane C artifact `10328401641`, digest `sha256:ff3d7bf16809eafd5e7deef297853106700d6fbba5f6dde6f279768925097f9f`.
- Lane D artifact `10327751803`, digest `sha256:2e27548f8fde4d2df4edc1a68db51ce9ccbbad8b44eddfe858707b237fb79ce3`.
- Aggregate artifact `10327981505`, digest `sha256:c8479371352ad8688a00b079dfca691eb67dc92382371a898333e67fdf366dd1`.

## Classification

`ITER078H_RG_FULL32_FIXED_JHALF_ORDERZERO_MAP_BF_TENSOR_NOT_CLOSED_EXACT_CONTROL_SCOPED`

Scientific verdict: **CONTROL_RESULT / NOT_CLOSED** in the prospectively frozen finite-spin tensor-network control.

## Exact findings

The exact degree-5 map `R_EPRL:C^32->C^32` was evaluated using the versioned Iter078F fixed-spin control measure: all internal and external face spins fixed to `j=1/2`, internal intertwiner labels `k=0,1`, common face factor `2^10`, and internal edge weights `d_k=2k+1`.

### BF-like compact tensor image

The exact compact tensor `L` from Iter077N is **not** an eigen-ray of the EPRL-weighted map.

A decisive exact witness is component index `1`:

- input/base value `L_1 = 0`;
- refined image value `R_EPRL(L)_1 = 12197975556096`.

Therefore no scalar `K` can satisfy

`R_EPRL(L)=K L`.

The one-scalar witness truncation `{t L}` is not closed even in this minimal fixed-spin control.

### Linearized selector rank

The exact `32x32` Jacobian at `L` has

- rank over `Q`: `31`;
- nullity: `1`;
- an exact right-nullspace witness is present and verified.

Thus the control map is sensitive at first order to 31 independent local directions near `L`, with one exact linearized null direction.

### Measure control

Repeating the same diagnostics with deliberately altered unit internal-edge weights gives:

- BF tensor still not an eigen-ray;
- Jacobian rank `31`;
- nullity `1`.

The frozen summary flag `measure_sensitive=false` means only that these coarse diagnostics — closure/eigen-ray status and Jacobian rank/nullity — agree between the two tested measures. It does **not** mean the two full polynomial maps or their exact images are equal.

## New scientific fact

The supported BF-like ambiguity direction does not remain a one-dimensional direction under the simplest exact `1->5` control built from the newly versioned measure skeleton. Refinement generates components outside the span of `L` immediately.

This independently supports the Iter078E/G conclusion that a one-coupling `cL` RG truncation is not scientifically adequate: the minimal integrated ambiguity sector must be treated as a multidimensional theory space unless a prospective reduction theorem is supplied.

## Interpretation ceiling

This is a **fixed all-`j=1/2` pure order-zero ambiguity tensor-network control**. It omits:

- the Lorentzian source-Toller reference extension `A_ref`;
- all higher internal spins;
- sums over compatible causal orientations;
- the full order-1 through order-8 supported-jet ambiguity;
- convergence/regulator analysis of the physical fine amplitude;
- coarse projection/matching to the actual causal vertex.

Therefore it is not a CRQN RG fixed point, not a beta function, not a generic-spin closure theorem, and not a continuum/G3 result.

## Exact next admissible step

Classify the unique exact linearized null direction **prospectively** rather than treating rank 31 as either a defect or a gauge mode. Freeze tests for:

1. its exact component structure;
2. whether the EPRL-weighted and unit-weight null vectors coincide/proportional;
3. whether it is an obvious relabeling/parity/normalization direction;
4. whether `R(L+t n)` is exactly flat or only first-order flat by computing the exact coefficients of `t^2,...,t^5`;
5. whether the first nonzero nonlinear order generates directions outside the null line.

Only after that should selector-rank claims be made.