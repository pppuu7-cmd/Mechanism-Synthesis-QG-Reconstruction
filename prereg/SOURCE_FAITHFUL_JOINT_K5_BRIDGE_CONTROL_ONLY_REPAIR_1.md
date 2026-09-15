# Source-faithful joint K5 bridge gate — control-only repair 1

Date: 2026-09-15
Status: **PROSPECTIVELY FROZEN BEFORE REPAIR IMPLEMENTATION**

Parent scientific contract: `prereg/SOURCE_FAITHFUL_JOINT_K5_BRIDGE_AUTHORITY_GATE.md`, commit `4151c02452edd3e5e2c49952686e42e64c6dc180`.

Initial positive-bridge derivation: `15c19a67f10f6cd26e522649bd41b3d9f1cadd8a`.
Initial structured lock: `221c91c5846cc60d1841ac432a542871a712ddba`.
Initial validator: `61926d293dca424e23c348b2f7b5de0b7d94441e`.
Initial workflow/head: `13a73422493b7e66964883b91ff01b5c670601d7`.
Initial production: run `34952663240`, job `104326933193`, terminal success; scientific output `BRIDGE_AUTHORITY_CONFIRMED_SCOPED` with B1-B9 true and all malformed controls rejected.

## Defect found before durable result promotion

The diagnostic exact inversion of

`cosh(sqrt(q)) = 1+s`

was implemented correctly through quadratic order but incorrectly at cubic order. The validator printed

`q(s)=2s-(1/3)s^2+(1/30)s^3+...`

whereas exact formal inversion gives

`q(s)=2s-(1/3)s^2+(4/45)s^3+...`.

The frozen geometry predicate used only the first two coefficients `2` and `-1/3`; therefore the initial B1-B9 scientific verdict and all negative-control outcomes were not conditional on the erroneous cubic diagnostic. Nevertheless the diagnostic must be repaired and production repeated before durable promotion.

## Frozen repair scope

The repair may change only the exact rational cubic-series calculation and, if necessary, its explicit assertion/output. It must not change:

- any B1-B9 wording or truth criterion;
- the source-derived definition `q=beta^2` or `q_B`;
- source ordering;
- collision block sets/counts;
- nested normal ranks/Jacobian powers;
- source/theorem authority;
- malformed negative controls;
- PASS/BLOCKED/FAIL/INVALID taxonomy;
- interpretation ceiling.

## Repair predicates

R1. Exact symbolic inversion returns coefficients `(2,-1/3,4/45)` through cubic order.

R2. All original geometry/provenance predicates and B1-B9 are recomputed unchanged.

R3. All original malformed controls remain rejected by the same candidate validator.

R4. The repeated production result is classified independently from the corrected cubic diagnostic; a scientific BLOCKED outcome remains allowed if any unchanged B predicate fails.

## Interpretation ceiling

This is an implementation/diagnostic repair only. It does not strengthen the scientific bridge claim and does not authorize durable downstream promotion without a fresh terminal production and independent adversarial review.