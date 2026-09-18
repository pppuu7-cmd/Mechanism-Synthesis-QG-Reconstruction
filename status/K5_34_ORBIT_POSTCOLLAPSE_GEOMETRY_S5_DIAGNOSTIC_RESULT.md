# K5 34-orbit post-collapse S5 geometry diagnostic — terminal

Date: 2026-09-19

Prospective preregistration: `b7495db85844111b947bc902e5df2a496bf614ad`.
Implementation: `b47198b9f4fa9d4b9726b2fd76971a76a29992c5`.
Workflow/head: `ebf328ebede611c830fcb9c0f598e51630e32d37`.
Run: `35404490633` (`completed/success`).
Artifact: `10571294546`.
Artifact ZIP digest: `sha256:77521688df988cadccab13fef1cf12d080d9027cbd7ab4720731f8687fd64c24`.

Frozen classification:

`K5_S5_POSTCOLLAPSE_DEFECT_MATCHING_COVARIANCE_COMPOSITION`

This is implementation diagnosis only. It is not a scientific N/B verdict and does not authorize the heavy resolver or global Stokes/IBP.

Exact stage vector:

- G1 ray permutation: PASS
- G2 incidence-basis transport: PASS (all 10 row relations)
- G3 Laplacian congruence: PASS
- G4 Q invariance: PASS
- G5 annihilator/tangent transport: PASS (`q_edge`, `v_edge`, divergence invariant)
- G6 covariance-series transport: PASS
- G7 determinant-factor transport: PASS
- G8 matching-covariance composition: FAIL
- G9 full N/B polynomial equality: FAIL in both channels and N/B objects

The first G8 failure occurs at the first frozen matching `((0,1),(2,3),(4,5),(6,7),(8,9))`. All mandatory validity controls pass, including component-1 Critic confirmation, exact rational matching arithmetic, parent prereg lock, 945 matchings on both repair routes, 100000 source terms, post-collapse matching-object equality, and q18 non-use. Deliberate malformed controls are rejected, including altered covariance, identity-G Laplacian, and omitted orientation sign.

Interpretation ceiling: upstream post-collapse geometry transport through determinant factors is exact for this frozen lane; the remaining implementation defect is localized to composition of matching covariance with the transported geometry. The final N/B polynomial mismatch is downstream of that G8 defect and is not scientific authority.

Resolver authority remains `0/64`; heavy resolver rerun remains unauthorized. `NEW_PHYSICS_FOUND`, F9/G3/G8 promotion, global Stokes/IBP, K5 periods, regulator independence, and complete-QG claims remain locked.

Highest-information next step: prospectively freeze a minimal G8-only exact diagnostic on the first failed matching, decomposing the matching covariance composition into edge-pair permutation, orientation cocycle/sign, covariance-entry pullback/pushforward convention, and product assembly. Do not inspect or fit N/B leading coefficients in that diagnostic.