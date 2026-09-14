# Iter083D-SM control-only P4 dependency-lock repair preregistration

Date: 2026-09-15

## Scope

This is an implementation/dependency-lock repair only. It does **not** alter the scientific hypothesis, frozen gate, classification target, causal sums, numerical factors, ambiguity dimension, or any claim ceiling of Iter083D-SM.

The first production run `34910997659` terminated `INVALID_IMPLEMENTATION` because predicate P4 searched `results/ITER081H_CRITIC_BELTRAN_CAUSAL_SUM_L1_COROLLARY.md` for the literal phrase `transverse scaling degree`. The authoritative Iter081H result instead records the same frozen scientific content explicitly as:

- `q=-20` / total homogeneous power `q=-20`;
- transverse dimension `d=12`;
- the same 16 eta=+1 assignments;
- `I^+_alpha(r,Omega_0) = 16 C_alpha r^(-20) + O(r^(-19))` with nonzero leading coefficient.

Therefore the failed predicate was a brittle string-lock mismatch, not a scientific failure and not a numerical failure.

## Frozen repair

Repair P4 only by replacing the missing prose-token lock with exact evidence tokens already present in the authoritative dependency:

1. `16 C_alpha r^(-20)`
2. `q=-20`
3. `d=12`
4. `16` eta=+1 source assignments, using the existing literal `16`/`eta=+1` wording in the dependency.

The repaired P4 still means exactly what the original preregistered P4 meant: the Beltran unit-weight causal sum retains a nonzero `r^-20` common-collision leading term in the same transverse dimension and source-defined 16-pattern family, hence the same transverse scaling-degree class relevant to Iter083B.

No result from a repaired production run has been inspected at the time of this preregistration.

## Frozen outputs

- If all original Iter083D predicates and controls pass after this dependency-lock repair: retain the original classification target `ITER083D_SM_CAUSAL_SUM_RETAINS_EXACT_377_DIMENSIONAL_K5_SUPPORTED_AMBIGUITY_REPAIRED_SCOPED` with verdict `PASS_EXACT_SCOPED`.
- Otherwise: do not reinterpret a failed scientific predicate as success. Record the exact failure and classify implementation vs scientific dependency according to the frozen predicates.

Claim locks remain unchanged: no unique K5 extension, no physical selector, no generic-spin theorem, no global distributional patching theorem, no G3/F9/G8/K5 promotion, no `NEW_PHYSICS_FOUND`, and no complete-QG claim.
