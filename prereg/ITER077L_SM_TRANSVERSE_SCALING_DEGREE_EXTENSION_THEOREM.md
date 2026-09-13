# Iter077L-SM preregistration — transverse scaling-degree extension theorem at the K5 common collision

**Date:** 2026-09-14

## Scientific question

Does an established external distribution-extension theorem, applied to the actual source-ordered all-`j=1/2` K5 common-collision singularity already isolated by Iter077I-SM, make the fixed-causal vertex a **unique** local distributional functional without adding a new normalization/regulator prescription?

## External theorem authority

Frozen authorities:

1. R. Brunetti and K. Fredenhagen, *Microlocal Analysis and Interacting Quantum Field Theories: Renormalization on Physical Backgrounds*, Commun. Math. Phys. 208 (2000) 623-661, arXiv:math-ph/9903028, especially the scaling-degree extension results of Sec. 5 and their submanifold/microlocal generalization in Sec. 6.
2. N. V. Dang, *Extension of distributions, scalings and renormalization of QFT on Riemannian manifolds*, arXiv:1411.3670, for extension along closed submanifolds / moderate-growth and weak-homogeneity framework.

Frozen theorem content to test:

- finite scaling degree implies existence of extensions with controlled scaling degree;
- uniqueness at a point holds only when scaling degree is strictly below the dimension of the scaled normal variables;
- at or above the threshold, minimal-scaling-degree extension is not selected uniquely by scaling alone and local terms supported on the singular set remain possible;
- for a smooth singular submanifold the relevant threshold is the transverse codimension, with ambiguity supported on that submanifold and involving normal derivatives of delta up to the superficial degree of divergence.

No theorem may be strengthened beyond its hypotheses.

## Frozen CRQN object

Use only the source-ordered object already closed by Iter077I-SM:

`one-wedge source construction -> Toller function -> K5 product -> full boundary contraction -> group integration`.

Frozen minimal sector:

- all ten spins `j_ab=1/2`;
- all 32 boundary-intertwiner basis components;
- fixed factorized causal structure, no causal-sector sum;
- published one-wedge spectral `i epsilon` prescription retained;
- no termwise contact-distribution product imported.

At a generic common-collision point, use the 12 normal boost coordinates of the four gauge-fixed non-root group variables. Compact/SU(2) directions are tangential to the `beta=0` singular set and are not counted as transverse regularizing dimensions.

Localize to a conic angular patch around an Iter077I exact nonzero witness where all ten relative boost directions stay nonzero. On that patch there are no additional partial-edge collision singularities and the leading angular coefficient is smooth/analytic.

## Frozen input from Iter077I-SM

For every one of the 32 basis components, Iter077I established an exact nonzero leading coefficient at the frozen angular witness and therefore on an open angular neighborhood.

Each wedge has leading transverse radial degree `-2`; ten wedges give

`u(r,omega) = r^-20 a(omega) + O(r^-19)`

on the localized patch, with `a(omega)` nonzero for the tested component. Hence the candidate transverse scaling degree is exactly

`sd_perp = 20`.

Frozen transverse codimension:

`q = 12`.

Frozen superficial transverse degree of divergence:

`omega = sd_perp - q = 8`.

## Positive controls

1. A localized toy distribution with identical smooth angular structure but radial degree `r^-11` in 12 normal dimensions must fall in the unique-extension regime `sd=11<12`.
2. A localized toy distribution `r^-12 a(omega)` must sit exactly at threshold and require at least a delta-supported normalization freedom.

## Negative / invalid controls

- If the exact source-ordered K5 component has transverse scaling degree `<12`, the nonuniqueness hypothesis fails.
- If the common singular set is not a smooth codimension-12 submanifold in the localized patch, theorem application is BLOCKED.
- If the angular patch necessarily intersects an additional singular sub-stratum, do not use the simple single-submanifold theorem there; shrink/localize prospectively or classify BLOCKED.
- If an external theorem supplies uniqueness only after adding extra normalization, covariance, analyticity, contour, or renormalization conditions not already source-selected, that is **not** uniqueness of the published CRQN object.

## PASS

PASS iff the frozen external theorem applies on the localized source-faithful patch with `sd_perp=20`, `q=12`, and therefore establishes:

- extension existence in the theorem's sense;
- absence of uniqueness from scaling degree alone;
- local ambiguity supported on the common-collision submanifold involving normal derivatives through order at most `8` (subject to the exact theorem formulation);
- hence the theorem does not by itself supply the missing source-selected K5 boundary value.

Classification:

`ITER077L_SM_TRANSVERSE_SD20_CODIM12_EXTENSION_EXISTS_BUT_SCALING_ALONE_NONUNIQUE_ORDER8_LOCAL_FREEDOM_THEOREM_SCOPED`

## FAIL

FAIL iff the theorem applies but uniquely selects the extension for the frozen source object without additional conditions beyond those already supplied by the published causal-Toller construction.

## BLOCKED

BLOCKED iff theorem hypotheses cannot be established for the actual source-ordered local object.

## INVALID

INVALID if the argument substitutes a pure radial toy for the source object, counts the full ambient group dimension instead of the transverse codimension without theorem, imports termwise contact products, or infers physical vertex nonexistence from extension nonuniqueness.

## Interpretation ceiling

A PASS does **not** prove that no physically preferred extension exists. It proves only that standard finite-scaling-degree extension theory guarantees extendibility but leaves local normalization freedom because the transverse scaling degree exceeds the codimension. A unique physical vertex would still require additional source-selected conditions and a separate proof that they fix the allowed local terms consistently with gluing, covariance, causal prescription and regulator independence.

No full causal-vertex divergence/nonexistence theorem; no generic-spin theorem; no regulator-independence theorem; no G3/F9/G8/K5 promotion; no complete-QG claim.