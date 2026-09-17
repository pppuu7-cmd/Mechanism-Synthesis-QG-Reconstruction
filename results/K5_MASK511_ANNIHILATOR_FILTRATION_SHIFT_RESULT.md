# K5 mask-511 annihilator filtration-shift result

Date: 2026-09-17

## Gate

`K5_MASK511_ANNIHILATOR_FILTRATION_SHIFT`

Prospective preregistration: `prereg/K5_MASK511_ANNIHILATOR_FILTRATION_SHIFT.md`, commit `1377d3944765b4aedbc512264cf73b75c45b96ad`.

Implementation: `scripts/k5_mask511_annihilator_filtration_shift.py`, commit `1450820c5ac25510d2f34a090c9a1fc1774e58ff`.

Workflow/head: `.github/workflows/k5_mask511_annihilator_filtration_shift.yml`, commit `0f3fc3d5dcd1b4e9a15dadad5dfb421dd4daa14e`.

## Production authority

Run `35250988892`, job `105302991242`, terminal `success`.

Artifact `10509478970`, `k5-mask511-annihilator-filtration-shift`, ZIP digest `sha256:4c095f158c6659d434d75eeb8b284174296920a06a187ffbd6c6630cfd59ec66`.

Production JSON SHA256 `2145dbdff1d06a002aa6cc9801bbeb1ce79f32203b2ac38c8ea18c55aa2139e8`.

Durable raw authority: `results/raw/k5_mask511_annihilator_filtration_shift_authoritative.json`.

## Exact result

For the labeled mask-511 filtration `F^r` by total degree in `alpha_0,...,alpha_8`, with `alpha_9` unscaled, the confirmed degree-four annihilator has exact cubic polynomials `q_i` whose minimum mask degree is two for every edge.

The exact reconstructed bounds are:

- `min_t(q_i)=2` for all ten edges;
- `min_t(v_i)=3` for edges `0,...,8` and `min_t(v_9)=2`;
- every transport term `s1 * v_i * partial_i` raises the filtration by at least two;
- `div(v)`, `sum_i q_i`, and `S=sum_i v_i` lie in `F^2`;
- `s1` has filtration degree zero because the unscaled tenth edge is present;
- the multiplication term `K=s1(div(v)+(1/2)sum_i q_i)-3S` lies in `F^2`.

Therefore, exactly and for every polynomial `N`,

`B_v(F^r) subset F^(r+2)`.

In particular, conditional on a separate proof that the physical numerator satisfies `N in F^19`, one obtains `B_v[N] in F^21` without a separate action-polynomial expansion.

The malformed control `q_9 -> q_9 + alpha_9^3` lowers the exact operator filtration shift to zero and is rejected as required.

All source/coefficient/blob locks, canonical edge order, cubic-degree checks, exact `v(Psi_K5)=0`, 125-tree `Psi_K5`, no-boundary-S5-consumption lock, no-numerical-identity lock and all frozen controls passed.

## Classification

`K5_MASK511_ANNIHILATOR_RAISES_FILTRATION_BY2_EXACT_SCOPED`

Status: `PASS_EXACT_SCOPED`.

## Interpretation ceiling

This result is an exact algebraic theorem about the frozen labeled mask-511 annihilator operator. It does **not** prove the physical membership `N_c in F^19`; `physical_numerator_membership_verdict` remains `null`. It does not establish angular-uniform mask-511 integrability, any other mask/orbit, boundary-S5 transport, global Stokes/IBP, an integrated K5 period, a finite-part selector, regulator independence, F9/G3/G8/K5 promotion, `NEW_PHYSICS_FOUND`, or complete quantum gravity.

The full structural-divisibility repair-1 run `35246991631` remains the sole authoritative production for the broader numerator/action angular-polynomial theorem while it is non-terminal. This operator theorem must not be used to consume partial values from that run or to launch a competing structural verdict.
