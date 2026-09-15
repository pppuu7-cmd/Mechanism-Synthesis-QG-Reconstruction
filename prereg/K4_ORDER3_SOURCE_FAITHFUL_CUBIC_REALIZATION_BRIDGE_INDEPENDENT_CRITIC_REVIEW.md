# K4 order-3 source-faithful cubic realization bridge — independent Critic preregistration

Date: 2026-09-15
Role: independent adversarial Critic gate

## Prospective order lock

This preregistration is committed before Critic implementation or production. Frozen criteria below must not be changed after inspection of Critic production output.

Researcher authority under review: `K4_ORDER3_SOURCE_FAITHFUL_CUBIC_REALIZATION_BRIDGE_DEFINED_EXACT_SCOPED`, Researcher run 34976334040 / artifact 10399632086. The Researcher PASS is not independently confirmed authority until this gate is terminal and valid.

## Frozen scope

Audit only whether the Researcher has defined a mutually compatible, source-faithful cubic object sufficient to make a subsequent actual K4 order-3 polar-coefficient gate well-defined. Do not evaluate or classify the K4 polar coefficient itself.

## Frozen required checks

C1 provenance: preregistration precedes Researcher derivation/implementation/production; authoritative run/artifact/durable bytes and recorded digests agree.

C2 exact gauge-free Toller identity: independently verify algebraically that for `h=U1 exp(beta sigma_3/2) U2`, with `t0=(t_++t_-)/2`, `t3=(t_+-t_-)/2`,
`T^kappa(h)=t0(beta)(h+h^{-dagger})/(2 cosh(beta/2))+t3(beta)(h-h^{-dagger})/(2 sinh(beta/2))`
reconstructs `U1 diag(t_+,t_-) U2`, with removable beta=0 behavior treated by the source reduced-function jets rather than by choosing a KAK angular section.

C3 source conventions: verify matrix/basis conventions and branch normalization are consistent with the retained Toller/source authority and preserve the published one-wedge spectral `i epsilon`; reject `beta+i*epsilon` substitution.

C4 common chart compatibility: internal six K4 wedges and all four external-to-K4 wedges must be jets of the same source group variables/chart, not independently fitted or representative-component surrogates.

C5 exact defining functions: independently verify `q(h)=arcosh((1/2)Tr(hh^dagger))^2`, all 16 simultaneous `q_B`, and the cubic scalar expansion `q=2s-(1/3)s^2+(4/45)s^3+O(s^4)` for `s=(1/2)Tr(hh^dagger)-1`; nested/cross couplings may not be dropped.

C6 original measure: retain original Haar/Jacobian structure through the cubic object definition; reject flat/frozen-measure replacement unless exactly derived as the relevant jet.

C7 resolved-front pairing and full boundary: retain the source-ordered full-32 boundary contraction and resolved-front/distributional pairing. Reject representative boundary component, scalar/Hodge surrogate, or termwise contact-product substitution.

C8 permutation covariance: independently check all five K4 blocks and all 120 S5 transports at object-definition level, including six internal plus four external wedges per K4 block.

C9 negative controls: run malformed candidates through the same validator. At minimum reject: commuting-BCH surrogate; missing external jets; representative boundary only; frozen angular ray/KAK section; one-parameter regulator replacing the 16-parameter germ; termwise theta/delta/delta-prime source-order replacement; post-hoc finite-part/fitted cancellation; `beta+i*epsilon`; dropped nested q_B cross-couplings; flat-Haar surrogate; scalar/Hodge replacement; preferred sequential continuation.

C10 interpretation ceiling: a Critic confirmation establishes only exact scoped object-definition sufficiency for a future K4 order-3 coefficient computation. It does not establish coefficient zero/nonzero, a physical finite part, regulator independence, unique K5 extension, F9/G8/G3, or new physics.

## Frozen terminal classifications

- `K4_CUBIC_REALIZATION_BRIDGE_CRITIC_CONFIRMED_SCOPED`: C1-C10 all pass and all malformed controls are rejected.
- `SCIENTIFIC_FAIL_SCOPED`: a source/mathematical claim required by the frozen bridge is independently false while implementation/provenance are valid.
- `INVALID_IMPLEMENTATION`: Critic or Researcher validator does not actually test the frozen predicates, is circular, or malformed controls do not traverse the same validation path.
- `INVALID_PROVENANCE`: prospective/durable-byte/run-artifact provenance is invalid or inconsistent.
- `BLOCKED`: required source/durable artifact is unavailable so the frozen audit cannot be completed.

Infrastructure/numerical failures are not scientific failures and must be reported separately.

## Dependency lock

Only a terminal valid `K4_CUBIC_REALIZATION_BRIDGE_CRITIC_CONFIRMED_SCOPED` authorizes prospective preregistration/implementation of the actual all-32 K4 order-3 polar coefficient/tensor and annihilator gate. K5 order-8 remains locked until that K4 coefficient gate is terminal and independently reviewed.
