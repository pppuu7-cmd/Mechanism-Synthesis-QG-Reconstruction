# Source-faithful joint K5 bridge — provenance ledger

Date: 2026-09-15

## Scientific contract

- gate: `SOURCE_FAITHFUL_JOINT_K5_MEROMORPHIC_OR_MULTIVARIABLE_BOUNDARY_VALUE_BRIDGE_AUTHORITY_GATE`;
- prospective scientific preregistration: `prereg/SOURCE_FAITHFUL_JOINT_K5_BRIDGE_AUTHORITY_GATE.md`, commit `4151c02452edd3e5e2c49952686e42e64c6dc180`;
- final Researcher classification: `BRIDGE_AUTHORITY_CONFIRMED_SCOPED`;
- final Researcher verdict: `PASS_EXACT_SCOPED`.

## Positive construction chronology

1. `4151c02452edd3e5e2c49952686e42e64c6dc180` — scientific bridge preregistration.
2. `15c19a67f10f6cd26e522649bd41b3d9f1cadd8a` — source-faithful multivariate meromorphic bridge derivation.
3. `221c91c5846cc60d1841ac432a542871a712ddba` — machine-readable source/geometry lock.
4. `61926d293dca424e23c348b2f7b5de0b7d94441e` — initial validator.
5. `13a73422493b7e66964883b91ff01b5c670601d7` — initial workflow/head.

The scientific derivation and lock predate all production output.

## Initial production — pre-repair evidence only

Run `34952663240` on head `13a73422493b7e66964883b91ff01b5c670601d7` completed successfully and returned B1-B9 true with all malformed controls rejected. Before durable promotion, an implementation-only diagnostic defect was found in the exact formal inversion of

`cosh(sqrt(q))=1+s`.

The diagnostic printed cubic coefficient `1/30`; exact inversion gives `4/45`. The initial scientific predicates had used only coefficients `2` and `-1/3`, so their truth values were unaffected, but the diagnostic was not accepted as durable production authority.

Initial run metadata retained only as history:

- run `34952663240`;
- job `104326933193`;
- artifact `10389024952`;
- ZIP digest `sha256:83770a227f00d36c4608a1c33e517ffa4af0ca3de6894555097cc7d71bd88327`;
- JSON SHA256 `84f433176d571a7d19e0e5280201024fc3dc85c8c4976b53643de1e03b2edc02`.

## Prospective control-only repair

The diagnostic repair was frozen before code modification:

- `prereg/SOURCE_FAITHFUL_JOINT_K5_BRIDGE_CONTROL_ONLY_REPAIR_1.md`, commit `a7157dd0a5a896db9a26e4036cd754934ed852f6`.

Frozen repair scope allowed only correction/assertion of the exact cubic series. B1-B9, source object, source order, geometry, authority, controls, verdict taxonomy and interpretation ceiling were locked unchanged.

Implementation-only repair:

- commit/head `87e732bab75e3d60f1df1390561fc584f667526f`;
- exact diagnostic corrected to `(2,-1/3,4/45)`;
- geometry validator strengthened to require the full corrected cubic tuple.

## Authoritative repaired production

The repaired production is the only scientific production authority for this bridge gate:

- workflow `Source-faithful joint K5 bridge authority gate`;
- head `87e732bab75e3d60f1df1390561fc584f667526f`;
- run `34953022566`, terminal `success`;
- job `104328280379`, terminal `success`;
- artifact `10389449925`, `source-faithful-joint-k5-bridge-gate`;
- artifact size `2208` bytes;
- artifact ZIP digest `sha256:abf75fdd1d1bfe97a0913cdcddb723b9c9fec6ca075dd47cc414fff593769d1b`;
- production JSON SHA256 `3a66499afb5c16b4fd0643ab3796f7da827d5ec09d3e03359fba2a5ba6c56011`.

Repaired production reports:

- `geometry_ok=true`;
- no provenance missing;
- B1-B9 all true;
- all nine malformed controls rejected;
- exact total block count `26`;
- exact divergent K3/K4/K5 block count `16`;
- 20 maximal divergent chains;
- physical incremental normal ranks `(6,3,3)`;
- resolved Haar-density powers `(5,2,2)`;
- 120 S5 relabelings with zero closure failures;
- exact source-radius inversion coefficients `(2,-1/3,4/45)` through cubic order.

The corrected durable raw JSON replaced the pre-repair raw at

`results/raw/source_faithful_joint_k5_bridge_gate.json`, replacement commit `b3f09df77af61a09fec425ce18e7d73d52d66ebe`.

The durable result was reconciled to repaired production in commit `79d166fdf89a9e42a653ed3bbb4b0cac426820da`.

## Scientific content locked by repaired production

- exact source-derived analytic pair radius `q(h)=beta(h)^2`;
- exact block radii `q_B=(1/|B|) sum_(a<b in B) beta(g_b^-1 g_a)^2`;
- complete collision-block arrangement and nested normal geometry;
- full 32-component source boundary structure retained;
- original product Haar density retained;
- multivariate family `U(lambda)=product_B q_B^(lambda_B/2) A_source` over the 16 divergent blocks;
- no modification of the published one-wedge spectral prescription;
- no `beta+i epsilon`, auxiliary regulator-space Q, representative boundary state, finite-part projection, fitted subtraction, preferred label/chain or sequential specialization;
- output object: actual full-boundary-contracted source-ordered multivariate meromorphic polar germ in the frozen local all-`j=1/2` sector.

## Parallel Iter083Q audit lane

A separate same-scope audit implementation was opened after the positive bridge files already existed:

- audit derivation `b94aafa1b30e75d2bc93b2e7b0c349fd4a7f3648`;
- audit implementation `019704d0566f0c055961c9a4ccd3b5097fe42b92`;
- audit head `3889de168d1705ac57bdd8c022c49548cad26417`;
- run `34952709428`, terminal failure / `INVALID_IMPLEMENTATION` before any scientific classification;
- no artifact.

Its supersession guard correctly detected that the new positive bridge derivation and raw lock were not ingested. This audit is a historical implementation control only and never supplied a competing BLOCKED verdict.

`prereg/ITER083Q_CONTROL_ONLY_REPAIR_1.md`, commit `19697881b766a3d64c544c6696f2dba4bb4f0ea6`, prospectively froze a possible ingestion repair. It is not a second scientific contract and no duplicate production is needed because the repaired positive bridge production is terminal authoritative.

## Durable Researcher state

- corrected raw replacement `b3f09df77af61a09fec425ce18e7d73d52d66ebe`;
- repaired result reconciliation `79d166fdf89a9e42a653ed3bbb4b0cac426820da`;
- this ledger is updated after both reconciliations;
- `status/CURRENT.md` and `status/MSQGR_RESEARCHER_HANDOFF.md` must cite repaired run `34953022566`, not the historical pre-repair run.

## Interpretation ceiling

This gate promotes only existence/definition of the scoped multivariate meromorphic polar germ. It does not promote a one-parameter `A_-1`, physical finite part, unique K5 extension, regulator dependence/independence, causal-vertex finiteness/divergence, F9/G3, RG, continuum, or later quantum-gravity layers. Independent Critic review of the repaired bridge remains mandatory before downstream promotion.
