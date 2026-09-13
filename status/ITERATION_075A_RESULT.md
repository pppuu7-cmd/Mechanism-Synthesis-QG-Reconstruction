# Iter075A — Nontransitive positive-real L1 coercivity

**Scientific classification:** `ITER075A_NONTRANSITIVE_POSITIVE_REAL_L1_COERCIVITY_EXACT_SCOPED`

## Authority

- Preregistration: `56eae289eeaffc11f71b33dd25a664d6e5ffb63d`
- Implementation: `47d62950d0a12c46d759e7520b4bf98094f46859`
- Production head: `57d263d9cc5ab3e2bd2d1875c49dd8da75d7820c`
- Run: `34750595140`
- Job: `103706458814`
- Artifact: `10315304394` (`iter075a-aggregate`)
- Digest: `sha256:e76003536c5dec1a9b7a02c9d22765d6237233a56040020b0dde98ca62bb4c2d`

## Frozen gate outcome

All `1008/1008` frozen nontransitive `(source class, cycle basis, nonempty edge subset)` cases possess exact strict dual certificates and satisfy the exact positive-real coercive estimate

`||A_S t||_1 >= kappa_1 ||t||_1` for all `t >= 0`.

All frozen predicates P1–P6 passed.  The exact coefficient histogram is:

- `kappa_1 = 1`: 581 cases;
- `kappa_1 = 1/2`: 363 cases;
- `kappa_1 = 1/3`: 64 cases.

Hence the actual global exact minimum is `1/3`, stronger than the preregistered conservative floor `1/7`.  Basis/S4 status is invariant, and the transitive positive control retains a kernel witness and correctly has no strict dual certificate.

## Scope

This proves a reduced **positive-real cone coercivity** statement only.  It is not an `epsilon -> 0` convergence theorem, does not establish a complex/distributional correlated boundary value, and does not imply physical causal-vertex finiteness.  It gives no G3/F9/G8/K5 promotion and no complete-QG or new-physics claim.

## Next use

The nontransitive positive-real escape directions are now quantitatively controlled.  Remaining decisive work is concentrated on transitive proper-stratum coefficients/overlap subtraction, especially the nominal `epsilon^-1` layer, and on the source-backed correlated Toller/group boundary value.
