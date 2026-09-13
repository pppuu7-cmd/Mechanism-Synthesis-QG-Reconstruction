# Iteration 063C terminal result — primary-source causal-vertex / EPRL-control pinning

Date: 2026-09-13

## Frozen provenance

Preregistration: `66ce9c87bcdf5b08e4c1e5604568766847321d98`  
Primary-source snapshot: `7df82d28dd6426aa7aaac353a1e0abf795e6fdee`  
Authoritative retry head: `1b795ac45e0c6b290b0c196aabea5aace220b00f`  
Authoritative run: `34732046499`  
Aggregate job: `103656528583`  
Aggregate artifact: `10309351521`  
Digest: `sha256:a8fad3edd3e820b849fa0be8fcf0939571fdc65b4919b2369d46efb2f2aa4eac`

## Authority note for first production

Initial production run `34731993670`, artifact `10309686785`, digest `sha256:25123425eeda0028438837c1884693242fc238666df307930a9d897291a786f8` returned 3/4 lanes with `representation_guard` blocked only because the implementation required a literal English phrase absent from the source snapshot despite the snapshot already containing the frozen Eq.(7) Cartan/magnetic statement. This was a matcher-only implementation false negative. Repair commit `41a0a423e9a00a176943194be20ce733f775463c` changed only the matcher to recognize the equation-level content; the frozen criterion was not weakened.

The initial production is diagnostic/non-authoritative for terminal classification.

## Terminal classification

`ITER063C_PRIMARY_SOURCE_VERTEX_CONTROL_PINNED`

All 4/4 frozen source-qualification lanes are valid:

- `vertex_object`: PASS
- `eprl_control`: PASS
- `causal_conventions`: PASS
- `representation_guard`: PASS

## What is now source-pinned

The tracked primary-source snapshot identifies arXiv `2601.23162` / DOI `10.1103/fwql-t4yr` and pins the following source structure:

- edge orientations `sigma_a=±1` and wedge branch `kappa_ab=sigma_a sigma_b`;
- ordered relative element `g_ab=g_b^{-1}g_a`;
- gamma-simple `(rho,k)=(gamma j_ab,j_ab)`;
- source Feynman spectral `i epsilon` Toller definition;
- direct fixed-causal ten-wedge vertex Eq.(4), with `g1=1` and four `SL(2,C)` integrations;
- exact additive relation `T+ + T- = D` Eq.(5);
- ordinary EPRL vertex as the **unconstrained** sum over all independent wedge signs Eq.(6), not the constrained causal sigma sum;
- Cartan/magnetic decomposition Eq.(7) as a representation of the same source Toller object.

## Scope

This is a source/object qualification PASS only. It does not establish the value, finiteness, absolute integrability, distributional meaning, permutation independence of a numerical regulator, physical sector selection, F9, G3, G8, K5, continuum closure, or new physics.

## Next authorized gate

A separately prospectively preregistered direct Eq.(4)-level numerical/symbolic gate may now test the source-defined pointwise integrand/carrier and the exact Eq.(5)/(6) EPRL control. Any later integrated vertex gate must separately control quadrature/cutoff/regulator dependence and boundary-intertwiner contraction.
