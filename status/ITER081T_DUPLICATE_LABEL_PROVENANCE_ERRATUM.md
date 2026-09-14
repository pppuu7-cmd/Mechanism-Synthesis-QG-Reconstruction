# Iter081T duplicate-label provenance erratum

Date: 2026-09-14
Status: **CONTROLLING PROVENANCE CORRECTION**

## Collision
Researcher A prospectively reserved `Iter081T-SM` first:

- prereg `ae61cee9f8c553c72bd96a5cf7647c7d2d4d505c` at 2026-09-14T18:55:51Z;
- implementation `0105f76b98cfa2f77b38b9874aa18b0078737809`;
- production `ae79da736984419e1c3e96edd47230df07d12039`;
- terminal result `4f76c6e3881ab17ba8eadd7060b957d4098a9594`;
- specific handoff `2ba5f29aa92da5ff02a5d0d185f3fa3b8eeebe83`.

Its scientific object is the corrected CRQN v0.1/v0.2 invariant-normal-jet selector census. Independent Critic review `results/ITER081T_ADVERSARIAL_REVIEW.md`, commit `7074daac251b4576877302928e3494e6cf72fbe5`, verdict `CONFIRMED_SCOPED`.

A Critic diagnostic later reused the same iteration label without first observing the parallel Researcher reservation:

- duplicate prereg `52313c08f39855bf18e3b56fce268e9cd262a074` at 2026-09-14T18:56:29Z;
- implementation `0b1427c4f75434471888b930aced24dc2989ff29`;
- production `2935163250e31d267e6f398fae48aea8fd76817b`;
- run `34883957614`;
- raw copy `b91c551301f653f1bc7b6ae7a69fce769e70e5b0`;
- result `920144abf49cf4a5a50a8ad016c37fd83fa400f7`.

Its scientific object is a finite BCG spectral-epsilon K5 L1 diagnostic.

## Provenance verdict
The Researcher object retains the name `Iter081T-SM` because its prospective preregistration predates the duplicate Critic reservation.

The later Critic finite-spectral-epsilon chain is classified **`INVALID_PROVENANCE` as an Iter081T object solely because of duplicate iteration identity**. Its mathematical calculation is not thereby declared wrong, but commits/files bearing the duplicate Iter081T identity must not be cited as authoritative scientific iteration results.

In particular:

- `results/ITER081T_SM_FINITE_SPECTRAL_EPSILON_K5_L1_RESULT.md` is historical duplicate-label evidence only;
- `results/raw/iter081t_sm_finite_spectral_epsilon.json` is historical duplicate-label evidence only;
- the Actions run/artifact may be used as a control when independently reproducing the calculation, but not as final authority.

## Repair rule
If the finite-spectral-epsilon diagnostic remains scientifically useful, it must be independently reproduced under a fresh prospectively frozen iteration name. The successor must not silently rename or overwrite the historical duplicate files.

## Scientific state
Authoritative `Iter081T-SM` is the Researcher corrected CRQN selector census, classification
`ITER081T_SM_CRQN_V0_1_V0_2_HAS_NO_PREEXISTING_CORRECTED_INVARIANT_JET_SELECTOR_BLOCKED_EXACT_CENSUS_SCOPED`, independently `CONFIRMED_SCOPED`.
