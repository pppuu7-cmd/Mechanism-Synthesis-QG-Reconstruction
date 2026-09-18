# Provenance — independent Critic review of repaired component-1 diagnostic

- Reviewed run: `35363610618`
- Reviewed head: `a5a9ae44569532bab7e352b12675d8eb152026ea`
- Reviewed job: `105660606466`
- Reviewed artifact: `10555382872`
- Reviewed artifact ZIP SHA256: `ffc28d87f50691e77bcf196b7db364214bdd31643f7fb092696b93f5796f0d64`
- Reviewed result SHA256: `e77e42f20db72960ee3d5d81faea4082763979265bbeafe8bc474b2a8a832a9a`

Independent Critic:

- prereg commit: `bc7a63a50a2fff36f931e03b5f26d4563ca29607`
- implementation commit: `6b140a14bcd679ad5594f29b7d50e83d6b6d88e8`
- workflow head: `0ebf4037e727a36e091e6153227269cc072015c3`
- run: `35402998823`
- job: `105786745616`
- artifact: `10571337475`
- artifact ZIP SHA256: `4d0cd5dd8c8ec42787d5bd6b22b006655ec237924d6241c96ecbabb10260e5b2`
- result JSON SHA256: `31a222b88fac3fa5a2daffdb8ae55096760d0a6f8da1a212419ecbc5408cb4db`

Classification: `CONFIRMED_SCOPED_COMPONENT1_SUPPORT_SET_MISMATCH`.

The Critic used source blob `2a3e3390556b337eccb6b917979961981f913deb` and standard-library exact Fraction arithmetic. Researcher result/support dictionaries were not imported into the reconstruction. They were compared only after the independent terminal result existed.

q18 partials used: false.

Resolver repair-2: authorized to be prospectively frozen, not yet frozen or run.
