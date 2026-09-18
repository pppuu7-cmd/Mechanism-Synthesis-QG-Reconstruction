# Provenance — repaired component-1 support-mixing diagnostic

Date: 2026-09-18

- parent diagnostic prereg: `ea49bb0cc67887659bb92c8a68b616f6b7e52513`
- original implementation: `e22c272425a624b80802d4ef7e295bcfd381f77c`
- original run: `35359497526`
- independent Critic invalidation: `65d8b04e874a29a8b6ce13d3d7d1a419e5e62801`
- repair-1 prereg: `aab70cd2ffbc9bf52fdd83f8caa78bc3d8b220ec`
- repaired implementation initial commit: `f92612da651cac91fe466f6aee2550242c55baeb`
- repaired workflow creation: `ef82324d05e46f474cebd2a14ea089c801b24ab6`
- initial repaired run: `35363408523`; operational success but `INVALID_IMPLEMENTATION_OR_PROVENANCE` solely because of a self-referential prereg-content SHA lock
- control repair-2 prereg: `7bc6f76fe8d183a38e944f096f93a9f0b6b0ab37`
- execution-only prereg-lock fix/head: `a5a9ae44569532bab7e352b12675d8eb152026ea`
- authoritative repaired run: `35363610618`
- job: `105660606466`
- artifact: `10555382872`
- artifact ZIP SHA256: `ffc28d87f50691e77bcf196b7db364214bdd31643f7fb092696b93f5796f0d64`
- result JSON SHA256: `e77e42f20db72960ee3d5d81faea4082763979265bbeafe8bc474b2a8a832a9a`
- terminal classification: `K5_S5_COMPONENT1_DEFECT_SUPPORT_INDEX_MISSING_OR_SPURIOUS`
- scientific_verdict: `null`
- invalid resolver values consumed: false
- q18 values consumed: false
- resolver physical authority after this diagnostic: `0/64`

All mandatory repaired validity controls pass, including independent raw-tensor boundary matrix reconstruction, 16-source contribution mixing for target component 1, dropped-contributor rejection, endpoint/orientation roundtrip, wrong-transpose discrimination and coefficient-mutation sensitivity.

The duplicate preparation commits `7d22ea4e5af4c3143317734afe4fecffd704f2a2`, `905908c2d7838fa7feae2c0b031ddeee8e07a8a9`, `8435881e6b5cfb200b57c13e8ab8a9a8a145e7cf` are non-authoritative.

Next dependency: independent Automation-B adversarial review of the repaired diagnostic. No heavy resolver rerun is authorized before that review.
