# Iteration 043 — finite-epsilon contact persistence and source-basis localization

Status: **PREREGISTERED / THREE INDEPENDENT LANES**

Date: 2026-09-12

## Closed prerequisites

- Iter025A validates the published j=1/2 Appendix-D boundary primitive `delta^(rho,1/2) = -i*c1*delta - (c2/2)*delta_prime` and `Theta_+ + Theta_- = 1`.
- Iter028/029 show that naive multi-wedge products are non-transverse on cyclic collision strata.
- Iter039/040 show that S5 symmetry alone leaves higher primitive local jets; q2 descendants do not generate the invariant ring.
- Iter041 run `34695499357` closes the source scaling census: for K5, `omega=6..16`, so the actual Appendix-D source reaches higher local-extension orders.
- Iter042A run `34695777621` shows that the edge-local j=1/2 derivative budget spans all three degree-4 primitive directions but only 3/5 at degree 6, and rapidly loses higher primitive directions. Iter042B run `34695777605` confirms a nontrivial S5 invariant-ring fingerprint with first relation-like plethystic coefficients at degree 12.

## Iter043A — exact finite-epsilon one-wedge contact identity

Use the published spectral Feynman denominator itself, not `beta+i*epsilon`. For j=1/2, Appendix D makes the spectral numerator a quadratic polynomial. Polynomial division therefore gives an exact finite-epsilon distribution identity

`Theta_{sigma,epsilon}(x) = A theta(sigma x) exp(-epsilon |x|) + B delta(x) - sigma*c2/2 delta_prime(x)`,

with

`A = 1 + i epsilon sigma c1 - epsilon^2 c2/2`,

`B = -i sigma c1 + epsilon c2/2`.

The key preregistered discriminator is whether the `delta_prime` coefficient remains exactly epsilon-independent. Validate the closed action directly against the original finite-epsilon spectral integral on independent Schwartz test functions for gamma `{0.2,1.2,2.0}` and epsilon `{0.4,0.2,0.1,0.05}`.

Interpretation lock: if PASS, this proves only that keeping the published i-epsilon finite on each wedge separately does not erase the contact layer after the exact spectral transform. It does not rule out a jointly correlated multi-wedge spectral/Feynman extension performed before multiplying boundary distributions.

## Iter043B — unlabeled source-orbit basis at d=4 and d=6

Resolve the Iter042 square-free source span into S5 edge-subgraph orbits. For degrees 4 and 6 and independent seeds 41/83, determine:

- number and descriptors of unlabeled K5 edge-subgraph orbits;
- source primitive quotient rank;
- which individual source orbits are essential;
- smallest source-orbit subsets spanning the observed source-compatible primitive quotient.

This is basis compression for later Feynman coefficient selection; it does not select any coefficient.

## Iter043C — K3 cyclic all-delta mollifier path audit

For the simplest overconstrained source product `delta(x) delta(y) delta(y-x)`, compare normalized Gaussian mollification paths with width ratios `(a,b,c)`. The preregistered leading coefficient is

`I_eta ~ C(a,b,c)/eta`,

`C = 1/[sqrt(pi) a b c sqrt(det M)]`,

where `M=[[a^-2+c^-2,-c^-2],[-c^-2,b^-2+c^-2]]`.

The transverse tree control `delta(x) delta(y)` has unit leading coefficient independent of widths. A nontrivial spread in `C(a,b,c)` is classified as regulator-path dependence of naive independent mollification, not as a no-go for the physical correlated Feynman prescription.

## Frozen guardrails

- no arbitrary finite part/counterterm is authorized;
- no full causal-vertex divergence/nonexistence claim;
- no G3/F9/G8 promotion;
- one-wedge finite-epsilon identities cannot be multiplied naively across non-transverse cyclic strata;
- the next route after PASS is a **joint multi-wedge spectral/Feynman test beginning with K3**, before attempting K5.
