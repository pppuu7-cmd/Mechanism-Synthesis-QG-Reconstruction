# Iter082C adversarial implementation review

Date: 2026-09-14  
Status: **DURABLE REVIEW — terminal CI is not promoted to a scientific strong PASS**

## RESULT_REVIEWED
Prospective preregistration: `3a8dcdd732065540abf753f5f0e891ddc9257632`.

Implementation: `8c07f6f6dd8fe5f1191a1bdd783a7e20d470797a`.

Production head: `11a6bfd2ca8d9ac4d336e2c9528b694955316076`.

GitHub Actions run `34894401672`, job `104144670722`, terminal `success`; artifact `10367754339`, ZIP digest `sha256:d80d2fb36a0a14edc531bc9b21a402215daed1d34d7393068bb5f169e6d3e661`; extracted aggregate JSON SHA256 `7049d115c7f57bffcf1dddf44168d2c55f2e9ef48f210b673733b9ef4a1c4ea4`.

The aggregate self-classified as `ITER082C_SM_K5_LOCAL_TAYLOR_FOREST_EXTENSION_CLASS_CONSTRUCTED_WITH_SYMBOLIC_SUPPORTED_SCHEME_FREEDOM_EXACT_SCOPED`.

## WHAT_IS_VALID
The implementation correctly and exactly checks several frozen local facts:

1. `omega_B = sd_B-codim_B` gives `(omega_3,omega_4,omega_5)=(0,3,8)`.
2. Taylor subtraction through `omega_B` leaves a remainder whose radial power including measure is `0`, hence locally integrable in the one-block scaling-degree model.
3. Under-subtraction by one normal order leaves radial exponent `-1` for each K3/K4/K5 block.
4. The 16 blocks, 72 forests and 20 maximal `K3 subset K4 subset K5` chains are reconstructed.
5. The unlabeled block-type metadata is S5-covariant.
6. The exact identity `W_chi-W_eta=(eta-chi)T_omega` correctly shows that changing a single-block cutoff/weight changes that local extension only through normal jets of order `<=omega`.

These are useful implementation-level controls but do not by themselves close the full frozen forest gate.

## DECISIVE IMPLEMENTATION DEFECTS
The strong PASS criteria D/E/F in the preregistration were not actually implemented.

### D — quotient/co-graph normal variables were not constructed
The preregistration required, for every maximal chain, exact nested Taylor-subtraction metadata on the **quotient/co-graph variables** and verification that every divergent stratum is subtracted once in those induced coordinates.

The script only records the nested subsets and their allowed orders. It does not construct the normal-variable embeddings/projections for

`K3 -> K4 -> K5`,

nor the induced quotient normal coordinates after the K3 contraction. Therefore `forest_chain_compatibility=true` is stronger than the executed test.

### E — two actual subtraction-order descriptions were not evaluated
The preregistration required evaluation of at least two legal nested subtraction-order descriptions on a finite polynomial test-jet model, with their difference classified as zero, supported allowed scheme freedom, or invalid.

The implementation compares

`((R3 then R4) then R5)`

with the same ordered list merely regrouped as

`(R3 then (R4 then R5))`.

After flattening, these are literally the same operator sequence. This is only same-graph reassociation, precisely the CDSR T4 selector-blind identity. It does not test nontrivial nested subtraction-order/scheme transport.

The subsequent `scheme_difference_support` table is inserted from the single-block identity `W_chi-W_eta=(eta-chi)T_omega`; it is not derived from composing two distinct nested forest operators.

### F — several negative controls are preassigned rather than executed
The script sets

- `source_firewall_rejects_termwise=True`,
- `same_graph_reassociation_not_selector=True`,

without constructing failing alternative objects. The over-subtraction control also equates `over_converges` with `over_not_promoted`, so it does not test an attempted uniqueness promotion. These are outcome declarations, not negative tests.

The `finite_coefficients_and_scales_remain_symbolic` control only checks that four descriptive dictionary values are strings; it does not audit the actual operator algebra for hidden fixed finite parts.

## SCIENTIFIC CONSEQUENCE
The terminal green workflow is an execution-success record, not a scientific strong PASS. The gate has not yet established a complete source-covariant K3/K4/K5 forest extension operator on all nested quotient coordinates.

The local single-block scaling-degree/Taylor-subtraction mechanism remains mathematically well motivated and partially checked. A successor can reuse the prospective scientific motivation, but must be newly frozen before repairing D/E/F.

No `UNIQUE_K5_EXTENSION`, physical selector, regulator independence, causal closure, RG closure, CRQN v0.3, or new-physics claim is affected.

## VERDICT
`INVALID_IMPLEMENTATION`

## AUTHORIZED_SUCCESSOR
Open a new prospectively frozen successor (Iter082D or later) that:

1. explicitly defines a finite nested normal-coordinate algebra for `K3 subset K4 subset K5`, with K3 normal variables embedded into the K4 normal space and K4 into K5;
2. implements the induced quotient coordinates after inner subtraction/contraction;
3. applies genuine Taylor projectors to a multivariate polynomial jet, rather than degree tags only;
4. compares at least two genuinely distinct admissible cutoff/scheme realizations and derives their difference from the composed operators;
5. replaces all preassigned negative-control booleans by injected invalid constructions whose failure is mechanically detected;
6. keeps all finite coefficients/scales symbolic and treats supported scheme differences as ambiguity, not as selection.
