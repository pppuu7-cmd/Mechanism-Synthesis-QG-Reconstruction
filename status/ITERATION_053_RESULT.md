# Iteration 053 result — exact K4 global uniform contour compatibility

**Status:** terminal

**Classification:** `K4_CAUSAL_SHIFTS_NO_GLOBAL_UNIFORM_CONTOUR_TRANSLATION`

Authoritative production run: `34718231048`

Aggregate artifact: `10305646600`

Artifact digest: `sha256:3aa44b8f4d65f096120c299c303c20e5e20061e1b084761d82e3fda9fedcfd6f`

## Frozen question

For each factorized K4 causal sign class and each of four frozen tree/cycle bases, write the six edge variables as

`x_e = b_e + a_e · y`

with exact 6×3 matrix `A`, and ask whether all six equal-magnitude causal shifts can come from one common affine cycle-variable translation

`y -> y - i epsilon v`,

so that exactly

`A v = s`.

The preregistered independent graph criterion is the equivalent cycle-space condition `B s = 0`.

## Terminal aggregate

- lanes: **32/32 valid**;
- tree/cycle-basis consistency: **PASS**;
- compatible causal sign classes: **0/8**;
- every class is incompatible in all four frozen bases `P0`, `P1`, `S0`, `S1`;
- the graph cycle-space control agrees: `B s` is nonzero for all eight classes.

Per-class `B s` vectors from the frozen aggregate:

- `+++`: `(-3,-1,1,3)`;
- `++-`: `(-1,1,3,-3)`;
- `+-+`: `(-1,1,-1,1)`;
- `+--`: `(1,3,-3,-1)`;
- `-++`: `(-1,1,-1,1)`;
- `-+-`: `(1,-1,1,-1)`;
- `--+`: `(1,-1,1,-1)`;
- `---`: `(3,-3,-1,1)`.

## Interpretation

The original six equal-`epsilon` causal edge shifts **cannot** be represented as one common uniform affine translation of the three K4 cycle variables for any of the eight factorized causal sign classes.

This is stronger than an integration-order observation: the obstruction already occurs at exact linear contour geometry and is independent of the four tested tree/cycle coordinate bases.

It is deliberately **not** a no-go theorem for causal EPRL/Toller amplitudes. In particular it does not exclude:

- one common affine direction with unequal positive edge-shift magnitudes;
- correlated or edge-dependent multivariate contour deformations;
- nonlinear contours;
- a source-defined multivariate residue/boundary-value prescription.

Those broader possibilities require separate prospective gates. Iter054 is the preregistered next affine sign-chamber test and must be consumed independently.

## Claim locks

- no physical amplitude finiteness/divergence claim;
- no general contour no-go theorem;
- no G3 PASS;
- no F9/G8 promotion;
- no fitted contour weights or post-hoc deformation coefficients.
