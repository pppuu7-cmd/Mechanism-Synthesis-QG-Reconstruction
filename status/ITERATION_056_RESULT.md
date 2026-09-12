# Iteration 056 result — orientation-cocycle covariance of K4 signed normals

**Status:** terminal

**Classification:** `K4_ORIENTATION_COCYCLE_RESTORES_COVARIANCE_FACTOR_CLASS_NOT_CLOSED`

Authoritative run: `34719504197`

Artifact: `10306082820`

Artifact digest: `sha256:72ca7c70d08a93264c2caface34397326a54185bcb53d8dbcd9e80d1c1eacc9c`

Preregistration commit: `dfd78f896ec4f0d10b727ff71551aacd32bf637d` before implementation/output.

## Exact result

For each of 8 source factorized causal classes, all 24 K4 vertex permutations, all 4 source cycle bases and all 4 target cycle bases, Iter056 used only the prospectively frozen orientation cocycle

`q_e=+1` if the permuted old oriented edge agrees with the canonical target orientation, and `q_e=-1` otherwise,

so that the effective oriented pole sign is

`s_eff,new = q_e s_old`.

The exact signed-normal covariance identity

`diag(s_eff) A_target C = E diag(s_source) A_source`

passes in **3072/3072** source/permutation/source-basis/target-basis checks.

Other exact totals:

- all audit validity checks: PASS;
- orientation-cocycle covariance: exact;
- class/permutation actions: 192;
- actions whose effective oriented sign vector remains in the original 8 factorized `tau_a tau_b` set: **32/192**;
- nonfactorized actions: **160/192**;
- each source factorized class remains factorized under exactly 4 of 24 vertex permutations;
- distinct effective oriented six-edge sign vectors generated from the original 8 classes: **48**.

There are no covariance failures.

## Interpretation

Iter055's naive S4 noncovariance is explained exactly by omission of the canonical edge-orientation reversal sign. Once the algebraically forced orientation cocycle is included, the frozen denominator/signed-normal geometry is exactly covariant.

However, the eight physical factorized wedge-sign vectors `kappa_ab=sigma_a sigma_b` are **not a closed state space for the orientation-dependent pole-sign vector** used by this surrogate. Under vertex relabeling plus restoration of canonical edge orientation, the effective spectral pole signs explore a 48-vector subset of `{+,-}^6`.

This does not mean that physical causal sectors cease to be factorized. It means two different data must not be conflated:

1. physical wedge causal data `kappa_ab=sigma_a sigma_b`;
2. orientation-dependent pole signs after expressing every edge variable in a fixed canonical orientation.

The latter acquires the cocycle `q`.

## Scope lock

This is an exact transformation law for the frozen oriented-flow denominator/signed-normal surrogate. It is **not** yet a full Toller-vertex permutation law: Toller branches are functions rather than representations, and group-element inversion/index transformations require a separate source-backed derivation.

No physical amplitude, K5, G3, F9, G8, complete-QG or new-physics claim follows.
