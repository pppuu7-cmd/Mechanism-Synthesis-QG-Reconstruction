# K5 34-orbit physical numerator/action-flux audit — control repair 1 preregistration

Status: **PROSPECTIVELY FROZEN BEFORE REPAIR-1 PRODUCTION OUTCOME**.

Parent scientific gate: `K5_34_ORBIT_PHYSICAL_NUMERATOR_ACTION_FLUX_AUDIT`, preregistration commit `9c42a26350e547eb02649c6ee44f8dd2477100d0`.

Failed implementation run: GitHub Actions run `35150430183`, job `104977054981`. The run terminated in the t-adic matrix inverse with `ZeroDivisionError: ('leading denominator unresolved', 0, 0, 0)` after exact cancellation of the stored leading coefficient. This is an **implementation failure only**; it is not a scientific FAIL, not a divergence verdict, and does not change any frozen physical hypothesis.

## Frozen scientific inputs — unchanged

- the same 34 S5 edge-subset orbits (32 proper physical orbits plus empty/full controls);
- the same lexicographically canonical representatives and orbit sizes;
- the same two physical all-32 invariant-dual channels;
- the same degree-27 numerator authority and degree-31 annihilator action authority;
- the same corrected projective-tangent geometry;
- primes `1000003`, `1000033`;
- weights `W1=(2,3,5,7,11,13,17,19,23,29)` and `W2=(31,37,41,43,47,53,59,61,67,71)`;
- the same K5/S5 cyclic permutation control;
- the same formulas for `g`, `rPsi`, `m`, `I`, `F`, and `A`;
- the same interpretation ceiling: no global Stokes/IBP, integrated-period, finite-part, regulator-independence, complete-amplitude, or downstream-QG verdict.

## Repair-1 execution algebra — frozen now

The one-leading-term `LT` representation is replaced only for execution by a cancellation-capable exact finite-field probe of the *same algebra*.

1. Freeze interpolation nodes to the 32 integers
   `t = 1,2,...,32`.
2. For every frozen witness lane, evaluate the same compressed exact all-32 source algebra and its directional AD action simultaneously over the appropriate frozen prime.
3. Reconstruct coefficients in `GF(p)[t]` from the fixed 32-node Vandermonde system.
4. Frozen degree ceilings are:
   - `Psi`: degree <= 4;
   - each physical numerator `N_c`: degree <= 27;
   - annihilator action `B_c`: degree <= 31;
   - the polynomial numerator of the projective normal component
     `U_Z = s1*sum_{e in Z} v_e - S*sum_{e in Z} alpha_e`: degree <= 31 (deliberately loose; only its lowest order is used).
5. In parallel, every algebra element carries a tropical/order lower bound propagated through the same canonical recurrence (`min` for addition, sum for products, sign reversal for inversion). This is the frozen **structural DAG lower bound**.
6. A component is certified only if all of the following hold:
   - every one of the 32 frozen interpolation nodes is denominator-invertible in both frozen primes for both asymmetric witnesses and their S5-permuted controls;
   - reconstructed coefficients above the frozen degree ceiling vanish;
   - both primes and both asymmetric witnesses give the same lowest nonzero order;
   - that order equals the structural DAG lower bound;
   - the corresponding S5-permuted lane gives the same order and the same leading coefficient after frozen weight transport.
7. Exact/modular cancellation that raises the actual lowest order above the structural DAG lower bound is **not repaired away**. It is classified exactly as the parent preregistration requires: `BLOCKED_CANCELLATION_RESOLUTION` for that component.
8. A frozen interpolation denominator failure does not crash the run. It makes the affected certification false and is recorded machine-readably.

No node, prime, weight, orbit, channel, threshold, basis, exponent formula, or scientific classifier may be changed after observing repair-1 production output.

## Terminal classification rule — unchanged in substance

- `INVALID_IMPLEMENTATION` if coverage, frozen authority, degree checks, controls, or execution/provenance requirements fail.
- `K5_34_ORBIT_PHYSICAL_NUMERATOR_ACTION_FLUX_PARTIAL_BLOCKED_SCOPED` if implementation is valid but at least one physical channel/orbit component fails frozen cancellation certification.
- `K5_34_ORBIT_PHYSICAL_NUMERATOR_ACTION_FLUX_AUDIT_EXACT_SCOPED` only if all 64 physical channel-orbit components are certified.

Any local integrability/divergence labels are scoped data for the certified component only. No global Stokes or integrated-period inference is authorized by this repair.
