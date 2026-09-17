# Prospective control-only repair 1 — K5 34-orbit exact leading-coefficient cancellation resolver

Date: 2026-09-17

## Historical invalid production

Parent scientific preregistration is immutable:

`prereg/K5_34_ORBIT_EXACT_LEADING_COEFFICIENT_CANCELLATION_RESOLUTION.md`

commit `d6b0e805101c8590eafac71398cc2b1466691752`.

Historical production run `35268238924`, head `25f646baa8b427d7f52ec3d1a5fadc31cd80fca1`, completed all eight deterministic shards and aggregate job `105366477161`, but its own aggregate classifier returned `INVALID_IMPLEMENTATION`.

No substantive N/B coefficient, first-nonzero order, zero/nonzero state or 64-component row from that run is authority and none may be used to tune this repair.

## Frozen defects

### R1 — structural polynomial equality control

The exact polynomial wrapper `P` stores coefficients in dictionary `P.d` but defines no structural `__eq__`. Route controls currently evaluate expressions such as

`psi.v == tree`,

`Ds[0].v == psi.v`,

`Ds[0].d == psi.d`,

which therefore test Python object identity rather than exact polynomial equality.

Allowed repair: implement exact structural equality `P.__eq__` by coefficient dictionaries, or replace only these equality controls with explicit `.d` equality. Arithmetic and scientific objects must not change.

### R2 — source-fixed S5 validation object

The historical shard forms `S5_W1/S5_W2` by permuting only the Schwinger mask/weights and re-evaluating the fixed source-projection coefficient object. That is not the physical coefficient-level S5 object required by the parent preregistration.

Independent Critic authority is now terminal:

`results/raw/k5_full_source_boundary_s5_independent_critic_authoritative.json`, classification `CONFIRMED_EXACT_SCOPED`, run `35267432939`, with `q18_values_used=false`.

It independently establishes exact simultaneous source endpoint/orientation transport plus boundary contragredient transport for the full 32-component/100000-source-term object. The repaired resolver must therefore transport the source coefficient object consistently before comparing the permuted coefficient polynomials.

Allowed repair: construct the transported source coefficient / perfect-matching coefficients exactly from the frozen source patterns and invariant-dual projection using the confirmed source endpoint/orientation transport. The covariance side must retain its own canonical incidence/orientation transport. For a permutation `p`, source and covariance orientation characters are separately mandatory and their product is the already-confirmed complete trivial residual character. No fitted sign, phase or channel-mixing matrix is permitted.

The repaired S5 control must compare the actual physical coefficient polynomials after simultaneous transport, not a source-fixed surrogate.

## Immutable scientific contract

This repair MUST NOT alter:

- CRQN version or claim ceiling;
- 32 proper S5 orbit representatives;
- two physical invariant-dual channels;
- W1, W2 or their frozen S5-permuted weights;
- canonical ten-edge ordering;
- all-32/100000-term source contraction;
- 945 exact retained perfect matchings;
- degree ceilings `N<=27`, `B<=31`, `U<=5`;
- canonical degree-27 DAG and source radius `Q`;
- confirmed projective-normal U authority;
- confirmed mask-511 parent authority;
- exact rational arithmetic;
- independent interpolation-route classes;
- PASS/PARTIAL/INVALID classifier meanings;
- interpretation ceiling;
- published spectral `i epsilon`.

No invalid-run provisional coefficient value may select or modify any implementation choice.

## Required positive controls after repair

1. Parent prereg commit lock remains exact.
2. Independent Boundary-S5 Critic authority is exactly `CONFIRMED_EXACT_SCOPED`, run `35267432939`, and `q18_values_used=false`.
3. `P` structural equality accepts independent exact copies and rejects an altered coefficient.
4. All original route internal exact controls pass.
5. Full source/boundary transport uses all 32 components and exactly 100000 source terms.
6. Source-projected transported perfect-matching construction retains deterministic exact rational arithmetic and complete matching support.
7. S5 CYCLE transport compares actual simultaneously transported physical coefficient polynomials for both channels and both W1/W2, for N and B.
8. The S5 source-fixed object remains a mandatory rejected malformed control on at least one nontrivial frozen validation instance; it may not silently become the repaired object.
9. All eight deterministic orbit shards complete with the same 32-orbit exhaustive coverage and no overlap.
10. Independent interpolation route remains exact on the same frozen `(orbit_size,k)` representative classes.
11. Projective-normal 32-orbit authority is recomputed and exact.
12. Mask-511 `r_N=19,r_B=21` parent witness is reproduced exactly.

## Negative controls

- omit endpoint transpose on reversed canonical edges -> reject;
- omit source reversal orientation character -> reject;
- use source-fixed source coefficients under nontrivial S5 permutation -> reject;
- alter one source coefficient -> reject;
- alter one matching assignment -> reject;
- structural polynomial equality with one changed coefficient -> reject.

## Terminal taxonomy

### PASS_EXACT_SCOPED
Only if every frozen implementation/source/control check passes, all 64 physical channel-orbit coefficient rows are exact and W1/W2 state/order checks agree under the unchanged parent contract.

### PASS_EXACT_PARTIAL_BLOCKED_SCOPED
Only if implementation is valid but at least one frozen component remains uncertified under the unchanged parent contract.

### INVALID_IMPLEMENTATION
Any failure of source locks, exact structural equality controls, simultaneous S5 source/boundary transport, coverage, matching support, independent route, U authority, mask-511 reproduction or mandatory malformed controls. INVALID carries no scientific coefficient verdict.

Scientific FAIL/PASS meanings of the parent contract are not otherwise changed.

## Interpretation ceiling

Even a valid terminal exact resolver only closes the frozen 64 physical N/B leading-order table needed by the 34-orbit physical N/action/flux audit. It does not itself prove global Stokes/IBP, a K5 period, a physical finite-part/joint selector, reduce `dim_C F_8=377`, prove regulator independence, promote F9/G3/G8/K5, establish `NEW_PHYSICS_FOUND` or complete quantum gravity.
