# AUTOMATION B adversarial review — component-1 S5 support-mixing diagnostic

Date: 2026-09-18
Role: independent MSQGR Adversarial Critic
Reviewed gate: `K5_34_ORBIT_COMPONENT1_SUPPORT_MIXING_DEFECT_DIAGNOSTIC`
Researcher prereg: `ea49bb0cc67887659bb92c8a68b616f6b7e52513`
Implementation: `e22c272425a624b80802d4ef7e295bcfd381f77c`
Workflow trigger/head: `7dac2c885c88cd2b9875bae021a129782b4d14ea`
Run: `35359497526`
Job: `105646962045`
Artifact: `10553332576`
Artifact ZIP SHA256: `f2b9b3303ca53438479c3215ebb9918b6031027f81c4cb7cd42b883a7f764e80`
Raw JSON SHA256: `42b3930e3fc9055e92d816e3e8278d2a1e8e03955978127e6ceb71db02d84884`

Mandatory Critic verdict: **INVALID_IMPLEMENTATION**

## Result reviewed

The terminal workflow is operationally valid and the artifact is internally consistent. It reports
`K5_S5_COMPONENT1_DEFECT_SUPPORT_INDEX_MISSING_OR_SPURIOUS` with equal cardinalities 1536/1536 but distinct exact support hashes and explicit missing/spurious keys. Those values are diagnostic-only and no N/B order was consumed.

The reported support mismatch is not scientific authority because the "direct target" route does not implement the direct target-component projection frozen by the preregistration.

## Decisive wrong-object witness

The preregistration freezes two independent constructions of **target component 1**:

1. canonical source support propagated through exact boundary contragredient `A^{-T}` component mixing;
2. direct endpoint/orientation transport of the underlying source terms **followed by target component projection**.

The implementation computes route 1 correctly as:

`predicted = s5.transform_dictvec(ATi, base)`
`pred = predicted[1]`

which forms target component 1 as the relevant linear combination of the full 32-component source vector.

But route 2 is implemented as:

`target = [transport_one(d) for d in base]`
`direct = target[1]`

That transports only the source dictionary that was already component 1. It never applies the target boundary-basis/component mixing to the transported source-term vector. Therefore it compares a mixed target component against an unmixed transported source component.

This is exactly the support-mixing mechanism the gate is supposed to diagnose, so the comparator is circularly biased toward producing missing/spurious support whenever the physical boundary action mixes components.

## Why the controls do not cure this defect

- all-32 and 100000-term cardinality controls only show the input vector is present;
- endpoint/orientation roundtrip only validates edge/type relabeling;
- the wrong-transpose control compares `A^{-1}` against `A^{-T}`, but does not test whether the direct route performs the target component projection at all;
- coefficient mutation sensitivity perturbs the already mixed `pred` dictionary and therefore does not validate the missing direct projection step;
- equal support cardinalities (1536/1536) do not imply equality of the correct objects.

The raw artifact's exact missing/spurious support keys are therefore witnesses to disagreement between two different objects, not a validated localization of the resolver defect.

## Source/order/erratum firewall

No source lock is changed by this review. The independently confirmed full-source Boundary-S5 coefficient transport remains authoritative. Canonical ten-edge order, all-32/100000 source contraction, 945 matchings, corrected Iter077 source ordering, published one-wedge spectral `i epsilon`, and the Iter077 contact-formula erratum remain controlling. Historical Iter077E/F remain quarantined.

No q18 partial payload or provisional q18 value was inspected or consumed.

## Consequence

The Researcher classification
`K5_S5_COMPONENT1_DEFECT_SUPPORT_INDEX_MISSING_OR_SPURIOUS`
from run `35359497526` is **not authoritative**. It cannot justify repair-2 of the heavy 34-orbit resolver.

The broader resolver state remains: repair-1 is `INVALID_IMPLEMENTATION`, 0/64 N/B components are authoritative, and the exact location of the S5 comparison defect remains unresolved.

## Authorized next gate

Only a prospectively frozen **implementation-only repair of the component-1 support-mixing diagnostic** is authorized.

The repaired direct route must start from the full transported 32-component source-term vector and independently project/mix it into target component 1 using the source-defined permuted node/intertwiner tensors (or an algebraically independent construction proven equivalent to the target boundary projection), rather than selecting transported `base[1]`.

It must include a positive mixing control where target component 1 provably receives at least two nonzero source-component contributions and a malformed control that deliberately drops one contributing source component and is rejected.

No heavy 34-orbit resolver rerun, no N/B order promotion, and no global Stokes/IBP or K5-period gate is authorized until that repaired diagnostic terminalizes and is independently reviewed.
