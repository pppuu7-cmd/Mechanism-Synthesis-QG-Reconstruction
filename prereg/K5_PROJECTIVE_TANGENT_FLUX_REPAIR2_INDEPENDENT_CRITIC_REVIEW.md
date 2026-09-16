# Independent Critic review — K5 projective tangent-flux repair2

Date: 2026-09-16
Status: PROSPECTIVELY FROZEN BEFORE CRITIC IMPLEMENTATION / OUTPUT

## RESULT_REVIEWED

Researcher result: `K5_PROJECTIVE_TANGENT_NORMAL_FLUX_SCALING_EXACT_SCOPED`.
Researcher durable result: `results/K5_PROJECTIVE_TANGENT_NORMAL_FLUX_SCALING_REPAIR2_RESULT.md`, commit `aa8baf37f4beaadf341f2cc6cf3b31415282cc5d`.
Frozen Researcher repair2 prereg: `prereg/K5_SCHWINGER_PROJECTIVE_TANGENT_NORMAL_FLUX_SCALING_CONTROL_REPAIR_2.md`, commit `d482b58d8d2640752ea9840eecf05bf444ded4cc`.
Researcher production: run `35146728850`, job `104964596683`, head `90dc54e8568b77675cd6dfee4e9d8dbcec645fef`, artifact `10466668706`, ZIP SHA256 `3c6d2894b184bd8177a6d0c5eaced31c62c49b3b813710e9e9f118eeffd52b3e`, result JSON SHA256 `017f25d431bbf137aefd9f375ddbefbff45d551bfda4fd46a0a55a825aa91fe3`.

## HYPOTHESIS / OBJECT

Independently test whether the terminal Researcher repair2 actually establishes the scoped local projective blow-up/tangent-flux geometry for

`Vol=dalpha_0 wedge ... wedge dalpha_9`, `Omega_9=i_E Vol`, `E=sum_i alpha_i partial_i`,

`v_i=alpha_i q_i(alpha)`, `S=sum_i v_i`, `s1=sum_i alpha_i`, `u=v-(S/s1)E`.

This review does not consume or classify the 34 physical corner orbits.

## FROZEN CRITIC INPUTS

1. Exact parent artifact identity above; the Critic workflow must download the artifact ZIP itself, verify ZIP SHA256, unpack it, and verify `result.json` SHA256 before scientific review.
2. Researcher source file `scripts/k5_projective_tangent_normal_flux_exact.py` is inspected only for coverage/hard-code audit; the independent reconstruction MUST NOT import or execute that module.
3. Independent generic field:
   `q_i=(i+3)+2 alpha_{i+2 mod 10}-alpha_{i+5 mod 10}`.
4. Independent exceptional field at `Z={0}`:
   `q_i=2+(i+1)^2 alpha_0`.
5. Proper faces: one frozen representative `Z={0,...,k-1}` for every `k=1,...,9`, plus its image under K5 vertex cycle `(0,1,2,3,4)->(1,2,3,4,0)`.
6. Two genuine simplex/projective charts per k, differing by dependent beta and/or eliminated outside coordinate; edge relabeling is not a second chart.

## REQUIRED INDEPENDENT CHECKS

The Critic implementation must independently reconstruct, without importing Researcher code:

1. exact antisymmetric `Omega_9`, `i_E Omega_9`, `i_v Omega_9`, `i_u Omega_9`;
2. exact `u(s1)=0`, `i_E Omega_9=0`, `i_v Omega_9=i_u Omega_9`, and contracted-form invariance under `v->v+f(alpha)E`;
3. for every k=1..9 and both frozen charts: actual blow-up pullback, lowest nonzero scalar and flux t-valuations, exact leading coefficients, and the face identity `PB(i_u Omega_9)|dt=0 = PB(Omega_9)_(dt wedge ...) * u(t)`;
4. for every k=1..9: exact chart-transition map, scalar and flux transition determinants, and equality of the full pulled-back coefficients after transport, not merely valuation agreement;
5. for every k=1..9: independent K5/S5-induced permutation push-forward of the field and face, with mechanically reconstructed scalar/flux valuations;
6. exceptional nonradial control with finite nonzero flux whose valuation strictly exceeds the generic valuation at the same face;
7. code audit that no scalar valuation is assigned by a literal `k-1`/`jac_exp=k-1` acceptance shortcut; extracted valuations must arise from symbolic pullback/valuation logic;
8. artifact coverage: exactly 18 Researcher chart witnesses, 9 chart relations, 9 permutation witnesses, nonphysical `Z=empty` and full-edge firewalls, and no physical verdict attached to those firewalls.

## FROZEN VERDICT RULE

- `CONFIRMED_SCOPED` only if provenance, implementation coverage, all independent exact identities, both-chart/full-form relations, S5 controls, and exceptional control all pass.
- `SCIENTIFIC_FAIL_CONFIRMED` if provenance and implementation coverage are complete but an independently reconstructed mathematical identity/scaling/chart relation required by the Researcher claim is exactly false.
- `INVALID_IMPLEMENTATION` if the Researcher decision path lacks a frozen obligation, contains forbidden hard-coded acceptance, or artifact witness coverage is insufficient.
- `INVALID_PROVENANCE` if artifact/run/hash identity cannot be independently reproduced.
- `QUALIFIED` only for a precise scope restriction that leaves a valid smaller result.

No criteria, q-family, face, chart, tolerance, or verdict rule may change after Critic output is seen.

## INTERPRETATION CEILING

Even `CONFIRMED_SCOPED` only unlocks prospective execution of the 34-orbit physical numerator/action-flux audit. It does not establish that audit, global Stokes/IBP, any integrated K5 period statement, any reduction of `dim_C F_8=377`, a physical finite-part selector, regulator independence, F9/G3/G8, `NEW_PHYSICS_FOUND`, or complete QG.
