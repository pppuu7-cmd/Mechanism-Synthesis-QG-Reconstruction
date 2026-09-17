# K5 mask-511 structural divisibility repair-1 — preterminal code audit

Date: 2026-09-17

Scope: outcome-independent AUTOMATION A audit only. Repaired production run `35246991631` was nonterminal when this audit was written. No shard coefficient payload, interim scientific value, result JSON, or classification was inspected or used.

## Frozen authority

Parent scientific contract remains `prereg/K5_MASK511_STRUCTURAL_DIVISIBILITY_LOWER_COEFFICIENTS.md`, commit `bb2fc2636de21d8eed06e3694a128be34e5fede1`.

Prospective execution-only repair remains `prereg/K5_MASK511_STRUCTURAL_DIVISIBILITY_CONTROL_REPAIR_1.md`, commit `16aac0291d9f129b61a3cfecadbab0803e83590a`.

Repaired implementation authority at this cut:

- shard implementation `cd406326b45cfe1a1f881344efa4b5f8a2174d1c`;
- aggregate implementation `1b57c7ff487e660e9a6efa19ee6a564951519937`;
- workflow/head `ef5f365798ab6aa2b9cb53d6b091868d910c9b71`;
- base scientific implementation blob `709904a582210642905ba053b5d622135da1067c`;
- shard blob `a7a8d20d8b170e71995c4cddff3c11c53e222a8f`;
- aggregate blob `6ab50f74ef5d94af6fdf508aa987295e9ce6d3c8`;
- workflow blob `9fdf4fb5c048badfcb3b39e94ac3c57764496709`.

## Static audit findings

1. The ordered retained perfect-matching set is unchanged at 945 matchings. Sharding is deterministic by `global_matching_index mod 8`; the aggregate requires exact coverage `0,...,944` with no duplicates before classification.

2. Each shard locks the parent preregistration, repair preregistration, canonical DAG blob/hash, action blob, all-32/100000-source-term dual object, rank-two dual pivots `[1,4]`, `Psi_K5` tree count 125, and exact `v(Psi_K5)=0`.

3. The restricted numerator materialization window `t^18,...,t^21` is consistent with the frozen exact degree bookkeeping. For each determinant/Wick summand `F_j S_(4-j)`, `min_t(F_j)=2j`, while the five-pair covariance contribution at source order `4-j` has minimum t-degree `10+2(4-j)`. Hence every numerator contribution has minimum t-degree `2j+10+2(4-j)=18`; coefficients below `t^18` are structurally impossible before cancellation.

4. Discarding numerator terms above `t^21` cannot affect the frozen action slices through `t^21`. In `B_v[N]=s1 v(N)+K N`, all polynomial multipliers have nonnegative mask-511 t-degree. For scaled variables, differentiation lowers t-degree by one but the corresponding factor `alpha_i` in `v_i=alpha_i q_i` restores it before multiplication by the nonnegative-degree `q_i`; for the unscaled variable differentiation does not lower mask t-degree. Therefore the action cannot map an omitted `N_{q>21}` term into `B_{q<=21}`.

5. Aggregate scientific classification is impossible until all eight shard summaries/payloads are present, each reports `SHARD_PASS_EXACT_CONTROL_ONLY`, payload hashes match, exact matching coverage is complete, and the summed physical imaginary components cancel exactly.

6. The aggregate reconstructs `B_v[N_c]` only after exact summation of all shard numerator dictionaries. No shard carries scientific classification authority.

7. Parent W1/W2 first coefficients at `N_q19` and `B_q21` are required to reproduce exactly from the aggregate symbolic coefficient polynomials.

8. The malformed retained-source-coefficient control remains exact and must produce a nonzero `N_q18` delta; failure is INVALID rather than scientific BLOCKED/PASS/FAIL.

9. No boundary-S5 transport theorem is consumed. The gate remains strictly labeled mask 511 and cannot be promoted to another mask/orbit.

## Audit conclusion

No outcome-independent contract violation or obvious truncation/sharding error was found in repair-1. This audit is not a scientific verdict and does not predict whether the lower angular-polynomial coefficients vanish. Repaired run `35246991631` remains the sole authoritative execution; no duplicate run is permitted while it is nonterminal.

Claim locks remain unchanged: no angular-uniform mask-511 integrability theorem before terminal aggregate authority; no full K5 cancellation/non-cancellation theorem; no Stokes/IBP theorem; no K5 period theorem; no physical finite-part selector; no regulator-independence theorem; no F9/G3/G8/K5 promotion; no `NEW_PHYSICS_FOUND`; no complete-QG claim; published spectral `i epsilon` retained.
