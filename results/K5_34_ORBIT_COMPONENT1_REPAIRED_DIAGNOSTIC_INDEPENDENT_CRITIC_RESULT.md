# Independent Critic result — repaired component-1 support-mixing diagnostic

Date: 2026-09-19

## Terminal verdict

**CONFIRMED_SCOPED_COMPONENT1_SUPPORT_SET_MISMATCH**

Independent Critic run `35402998823`, job `105786745616`, artifact `10571337475`.

The Critic reconstructed the reviewed object independently from corrected Iter077I source tensors and did not import the Researcher diagnostic implementation or result payload as a computational premise.

## Exact reconstruction

- 32 boundary components reconstructed directly from source.
- Exactly 100000 source-choice terms.
- 945 perfect matchings independently enumerated as provenance control.
- Exact Fraction arithmetic throughout.
- Global cycle action and inverse compose exactly.
- Endpoint/orientation roundtrip passes on all 32 components.
- Wrong-transpose malformed control is rejected.
- Target component 1 has exactly 16 nonzero source-component contributors:
  `[0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30]`.
- Dropping one nonzero contributor changes the direct target dictionary and is rejected.

The independent target dictionaries both have support cardinality 1536, but their exact support sets differ.

Route 1 dictionary SHA256:
`6eca3bbe1e0abef16daa0c62bbf1f1bb1097d07783e5687e07f67ddbe7f713e1`

Route 2 dictionary SHA256:
`76fba3334777ba180b8aea2da1a592463b1c62c389dcf70df448fb7aeec9dc85`

These exactly match the terminal Researcher run only after the independent reconstruction had already completed.

First missing support key:
`((0, 0), (0, 0), (0, 1), (0, 1), (0, 0), (0, 1), (1, 1), (1, 1), (0, 1), (1, 1))`

First spurious support key:
`((0, 0), (0, 1), (0, 0), (0, 1), (1, 1), (1, 0), (0, 1), (0, 0), (1, 1), (1, 1))`

## Provenance

Reviewed Researcher run: `35363610618`.
Reviewed artifact: `10555382872`.
Reviewed result JSON SHA256: `e77e42f20db72960ee3d5d81faea4082763979265bbeafe8bc474b2a8a832a9a`.

Critic prereg: `bc7a63a50a2fff36f931e03b5f26d4563ca29607`.
Critic implementation: `6b140a14bcd679ad5594f29b7d50e83d6b6d88e8`.
Critic workflow head: `0ebf4037e727a36e091e6153227269cc072015c3`.
Critic artifact ZIP SHA256: `4d0cd5dd8c8ec42787d5bd6b22b006655ec237924d6241c96ecbabb10260e5b2`.
Critic result JSON SHA256: `31a222b88fac3fa5a2daffdb8ae55096760d0a6f8da1a212419ecbc5408cb4db`.

No q18 partial value was consumed.

## Consequence

The repaired component-1 Researcher diagnostic is independently confirmed in its implementation-diagnostic scope. This authorizes prospectively freezing heavy-resolver repair-2, but does not itself freeze or execute that repair.

Heavy resolver remains 0/64 authoritative until a separately frozen repair-2 is run and terminally classified.

No global Stokes/IBP, K5 period, finite-part selector, regulator independence, G3/composition, NEW_PHYSICS_FOUND, or complete-QG claim is authorized.
