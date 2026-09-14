# Iter078O-RG result — exact causal-stabilizer symmetry reduction of the labelled all-j=1/2 boundary dual

**Date:** 2026-09-14

## Provenance

- Prospective preregistration: `prereg/ITER078O_RG_CAUSAL_STABILIZER_SYMMETRY_REDUCTION.md`, commit `2ee924df68d020485fbd40644c30b7bff0ff0832`.
- Implementation: `distributional/iter078o_rg_causal_stabilizer_symmetry.py`, commit `5681a304a24b748490d0eec7c1a56d4d7fa19fc3`.
- Workflow/production head: `.github/workflows/iter078o_rg_causal_stabilizer_symmetry.yml`, commit `5c8151157e98ca2044c40d9e23e68ae074592f03`.
- Authoritative terminal run: `34791393789`.
- Aggregate artifact: `10327823415`, digest `sha256:a79e55117f8b8347f65dd0e11693b182a260a8068c0c710e9786e5b125e51864`.
- Lane artifacts:
  - A `10328701621`, digest `sha256:5930769466a95dd54fd63b2044097fe6574c91c2f3621004b5525b7629a09ea8`;
  - B `10328378826`, digest `sha256:fa3a637c4155cf41ec485b0fd244b6470b8674a0d17427b3d171b3081890bcec`;
  - C `10328437628`, digest `sha256:1f78ac4a4939297b0eb3fd61987b5dbf74fbc670dbd756553b30ec47743e1169`;
  - D `10328432409`, digest `sha256:7d24ddd5139f6df37dae37cc53e39df24834f2d548df947ec648db40660dde5e`.

## Classification

`ITER078O_RG_CAUSAL_STABILIZER_RECOUPLING_SYMMETRY_REDUCES_LABELLED_FULL32_BOUNDARY_DUAL_EXACT_CONTROL_SCOPED`

Verdict: **CONTROL_RESULT**.

## Exact findings

Using the frozen normalized four-valent `j=1/2` intertwiner basis and deriving every local leg-permutation matrix from exact tensor permutations, the induced labelled five-node boundary representation has exact fixed-subspace dimensions:

- causal class `0<->5`, stabilizer size `120` (`S5`): `dim Fix = 2`;
- causal class `1<->4`, stabilizer size `24` (`S1 x S4`): `dim Fix = 3`;
- causal class `2<->3`, stabilizer size `12` (`S2 x S3`): `dim Fix = 5`.

There are `6` distinct local `S4` recoupling matrices in the frozen representation. Exact fixed-subspace ranks and independent character averages agree in every causal class.

## Scientific interpretation

The labelled 32-dimensional all-`j=1/2` control space is strongly reduced if one **imposes invariance** under the stabilizer of a fixed causal sign class. This is useful control information: the equal-spin boundary dual has substantial exact symmetry structure.

However, the preregistered ceiling is essential. This calculation does **not** establish that the physical causal-Toller extension functional must be invariant, rather than transform covariantly, under the same labelled action. It also does not select a unique element even in the smallest fixed space (`dim=2`). Therefore it does not cure the physical K5 extension ambiguity.

The stronger physical Iter077Q result is logically independent: it exhibits an infinite-dimensional smooth tangential coefficient family built from fully relabeling-invariant scalar `Q`, so graph-stabilizer invariance alone cannot remove that tangential function-space ambiguity.

## Claim ceiling

Control-sector result only. No unique physical extension, no physical RG map/fixed point, no generic-spin coupling count, no regulator independence, no G3/F9/G8/K5 promotion, no new physics and no complete-QG claim.