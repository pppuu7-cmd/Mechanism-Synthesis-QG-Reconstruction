# Prospective preregistration — independent Critic review of K5 projective constant-2x2 closure

Date: 2026-09-16

## Scope

Review only the Researcher result `K5_PROJECTIVE_CONSTANT2X2_CLOSURE_FALSIFIED_EXACT_SCOPED` from run `35140030858`, job `104941953222`, artifact `10464124390`.

The reviewed object is the corrected projective degree-27 action

`P_v[N]=B_v[N]/s1^4`

on the two actual full-all-32 invariant-dual channels. This review does not reopen the historical raw `B=MN` object and does not assign an integrated-period/Stokes verdict.

## Frozen acceptance criteria

The Critic must independently establish:

1. Prospective chronology: Researcher prereg commit `4f1e49f9d850fa7834dd189228d0787f84406f84` precedes the parent-point lock, implementation and production.
2. Production provenance: run/job/head/artifact/digest/production-JSON identity agree with durable records and are terminal-successful.
3. Parent-point provenance: all four locked `N_c` and `B_c` values match the downloaded authoritative parent artifact `10461780450`, not merely metadata copied into a new file.
4. Object correctness: `P=B/s1^4`, `deg N=deg P=27`, `deg B=31`; no representative boundary component or scalar/Hodge surrogate replaces the two invariant-dual channels.
5. Frozen representatives and edge ordering are unchanged: fit_A, fit_B, validation_U, validation_G exactly as preregistered.
6. The fit numerator matrix is exactly invertible and the Critic independently recomputes the unique rational constant `2x2` matrix from fit_A/fit_B.
7. The same matrix has at least one exact nonzero residual on the prospectively frozen validation representatives. A single nonzero exact validation component suffices to falsify the global constant-matrix identity.
8. Projective representative scaling cannot create/remove the counterexample: because N and P have the same homogeneous degree, residuals scale covariantly. The Critic must distinguish this from the historical heterogeneous raw-B test.
9. Basis robustness: constant closure/nonclosure must be invariant under any fixed invertible constant change of the two invariant-dual channel basis.
10. Interpretation ceiling: no promotion to failure of polynomial/rational modules, integrated periods, Stokes, full 217D K5 tensor, finite-part selection, regulator independence, F9/G3/G8, new physics or complete QG.

## Frozen adversarial controls

The review must actively test/flag at least:

- swapped fit/validation roles;
- post-hoc replacement of any frozen representative;
- singular fit matrix;
- use of `B` instead of `P`;
- denominator powers `s1^3` and `s1^5`;
- representative rescaling of one validation point;
- constant invertible channel-basis change;
- alteration of one parent exact N/B value;
- use of only one channel or one boundary component;
- promotion of finite-point falsification to a stronger module/period theorem.

## Terminal verdict mapping

- `CONFIRMED_SCOPED` if provenance, exact arithmetic, object identity and counterexample all survive.
- `QUALIFIED` if the exact constant-closure falsification survives but a nonessential implementation/provenance statement must be narrowed.
- `INVALID_PROVENANCE` if exact parent values cannot be bound to the authoritative artifact.
- `INVALID_IMPLEMENTATION` for circular/hard-coded arithmetic or malformed-control failure.
- `REQUIRES_NEW_PREREGISTERED_GATE` if the tested object differs materially from the frozen Researcher object.

No criteria may be changed after Critic computation.
