# Prospective preregistration — exact physical N/B corner witness at labeled K5 mask 511

Date: 2026-09-17

Status: **PROSPECTIVELY FROZEN BEFORE SUBSTANTIVE N/B OUTPUT**.

## HYPOTHESIS

The maximally collapsed proper labeled K5 Schwinger corner

`Z_511={0,1,2,3,4,5,6,7,8}`

(`k=9`, one non-collapsing canonical edge) may already supply an exact obstruction to ordinary local integrability of one or both physical invariant-dual projective channels, without using any S5 transport theorem. If an exact frozen angular witness gives first nonzero numerator order `r_N <= 18`, then the physical interior radial exponent is `-19+r_N <= -1`; because the corresponding angular leading-coefficient polynomial is nonzero at that exact witness, it is nonzero on an angular neighbourhood and ordinary local integrability fails on this labeled corner in that channel.

This gate tests that proposition directly. It does **not** infer any other orbit from mask 511.

## exact OBJECT

Use the terminal canonical full-all-32/100000-source-term physical invariant-dual numerator channels `N_1,N_2`, degree 27, and the confirmed degree-four Kirchhoff annihilator action polynomial

`B_v[N]=s1 v(N)+{s1[div v +(1/2)sum_i q_i]-3S}N`,

of degree 31, with the corrected raw-homogeneous normalization.

For each frozen angular weight vector `W`, use the labeled corner path

`alpha_e(t)=W_e t` for `e in Z_511`,

`alpha_9(t)=W_9`.

No S5 permutation, orbit transport, fitted phase, fitted channel mixing or boundary-state change is used.

## DEPENDENCY

Consumes only independently established authorities that do not depend on the pending symbolic boundary-S5 Critic:

1. full physical all-32 invariant-dual K5 projective object;
2. terminal degree-27 canonical numerator DAG;
3. independently confirmed degree-four annihilator with `v(Psi_K5)=0`;
4. independently confirmed corrected projective-tangent geometry;
5. exact denominator valuation `ord_Z Psi_K5=c(K5\\Z)-1`;
6. terminal projective-normal mask-511 result `r_U=3`.

It does not consume the Researcher-only coefficient-level full-source S5 theorem and does not execute the frozen 64-component resolver `d6b0e805101c8590eafac71398cc2b1466691752`.

## SOURCE AUTHORITY

Source ordering remains

`one-wedge spectral/spinor integration -> Toller function -> product of ten Toller matrices -> full boundary contraction -> K5 group/distributional object`.

Use the published one-wedge spectral `i epsilon`, all source signs/branches encoded by the terminal full-all-32 numerator DAG, dual/covector projection (not vector projection), exact K5 incidence and the corrected raw-homogeneous action formula.

## FROZEN INPUTS

Canonical K5 edge order is the repository-authoritative ten-edge order.

Frozen labeled corner:

`mask=511`, bits `[0,1,2,3,4,5,6,7,8]`, `k=9`.

Frozen angular witnesses:

- `W1=(2,3,5,7,11,13,17,19,23,29)`;
- `W2=(31,37,41,43,47,53,59,61,67,71)`.

Exact rational arithmetic only.

Complete polynomial degree ceilings are frozen before output:

- `deg_t N_c <= 27`;
- `deg_t B_v[N_c] <= 31`.

Exact interpolation/evaluation schedule is frozen:

- evaluate exact full point object at every integer `t=1,...,34` for W1 and W2;
- reconstruct each `N_c(t)` from exactly `t=1,...,28` (28 points for degree <=27);
- validate reconstructed `N_c` exactly at `t=29,...,34`;
- reconstruct each `B_v[N_c](t)` from exactly `t=1,...,32` (32 points for degree <=31);
- validate reconstructed `B` exactly at `t=33,34`.

Interpolation must be exact rational Vandermonde/Newton algebra. No floating point, modular-only zero test, adaptive sample, changed weight, changed degree, or post-output extra witness is permitted.

Authoritative geometric values frozen before N/B output:

- `r_Psi=3` for mask 511, since `K5\\Z_511` has four connected components;
- scalar blow-up factor exponent `g=k-1=8`;
- half-density/denominator factor `m=k/2-(21/2)r_Psi=9/2-63/2=-27`;
- therefore physical interior exponent is `I=-19+r_N`;
- terminal projective-normal order is `r_U=3`, hence flux exponent `F=-16+r_N`;
- action exponent is `A=-19+r_B`.

## POSITIVE CONTROLS

1. Reconstruct the terminal dual projector/all-32 source object and exactly reproduce parent numerator locks at raw uniform and `fit_A`.
2. Reproduce corrected raw-uniform `B=-1500N` for both channels.
3. Verify `v(Psi_K5)=0` exactly.
4. Verify degree-27 Euler identity for `N` and degree accounting 31 for `B`.
5. Verify interpolation reconstructions against all frozen holdout points exactly.
6. W1 and W2 must each be processed independently with the same frozen schedule.
7. `Psi(alpha(t))` must have exact first nonzero order 3 on both W1 and W2.
8. Import the already-terminal mask-511 `r_U=3` only as fixed geometry authority; do not recompute it to change the gate.

## NEGATIVE CONTROLS

The validator must reject/detect:

- vector Reynolds projection substituted for dual projection;
- historical raw-uniform `s1=1` mistake;
- one altered annihilator coefficient;
- degree-26 truncation for N;
- degree-30 truncation for B;
- one corrupted interpolation sample;
- replacing mask 511 by another mask;
- changing W1/W2 after output;
- claiming another S5 orbit from this labeled result;
- claiming full-amplitude or global Stokes conclusions from one corner.

## PASS / FAIL / BLOCKED / INVALID

`FAIL_ORDINARY_LOCAL_INTEGRABILITY_MASK511_PHYSICAL_CHANNEL_EXACT_SCOPED` if all implementation/provenance controls pass and at least one physical channel has an exact frozen-witness nonzero coefficient at `r_N<=18`. This is a scientific failure of **ordinary local integrability of that full contracted physical channel at this labeled corner**, not a failure of existence as a renormalized/boundary-value distribution and not a complete-QG verdict.

`K5_MASK511_ACTION_OR_FLUX_OBSTRUCTION_EXACT_SCOPED` if no interior failure witness occurs but an exact action or flux exponent is `<=-1` on at least one channel/witness.

`K5_MASK511_NO_OBSTRUCTION_WITNESS_ON_FROZEN_RAYS_INCONCLUSIVE_SCOPED` if all frozen exact interior/action/flux exponents are `>-1`. This does not prove angular-uniform integrability.

`BLOCKED_OBJECT_DEFINITION` if the terminal full physical N/B object cannot be reconstructed without importing the pending S5 transport theorem.

`INVALID_IMPLEMENTATION` or `INVALID_PROVENANCE` for failed locks, interpolation validation, degree/support violation, wrong source object, wrong normalization or malformed-control failure.

## INTERPRETATION CEILING

A nonzero exact coefficient at one frozen angular point proves the corresponding angular coefficient polynomial is not identically zero and hence is nonzero on an angular neighbourhood. Thus a radial exponent `<=-1` at that coefficient is sufficient to disprove ordinary local integrability at this labeled corner in that channel.

No result from this gate may be promoted to all 32 orbit representatives, all 1022 labeled subsets, the full 217-dimensional tensor, a global Stokes/IBP theorem, either integrated K5 period, a physical finite-part selector, reduction of the `dim_C F_8=377` extension freedom, regulator independence, F9/G3/G8/K5 promotion, `NEW_PHYSICS_FOUND`, or complete quantum gravity.
