# Source-faithful joint K5 meromorphic bridge authority gate — Researcher result

Date: 2026-09-15

Status: **PASS_EXACT_SCOPED**

Classification:

`BRIDGE_AUTHORITY_CONFIRMED_SCOPED`

## Prospective provenance

Scientific preregistration was frozen before the substantive construction:

- `prereg/SOURCE_FAITHFUL_JOINT_K5_BRIDGE_AUTHORITY_GATE.md`, commit `4151c02452edd3e5e2c49952686e42e64c6dc180`.

The positive construction was then derived and locked before production:

- derivation `sources/SOURCE_FAITHFUL_JOINT_K5_BRIDGE_DERIVATION.md`, commit `15c19a67f10f6cd26e522649bd41b3d9f1cadd8a`;
- machine-readable source/geometry lock `sources/raw/source_faithful_joint_k5_bridge_lock.json`, commit `221c91c5846cc60d1841ac432a542871a712ddba`;
- validator `scripts/source_faithful_joint_k5_bridge_gate.py`, commit `61926d293dca424e23c348b2f7b5de0b7d94441e`;
- workflow/production head `13a73422493b7e66964883b91ff01b5c670601d7`.

Production authority:

- GitHub Actions run `34952663240`, terminal `success`;
- job `104326933193`, terminal `success`;
- artifact `10389024952`, `source-faithful-joint-k5-bridge-gate`;
- artifact ZIP digest `sha256:83770a227f00d36c4608a1c33e517ffa4af0ca3de6894555097cc7d71bd88327`;
- production JSON SHA256 `84f433176d571a7d19e0e5280201024fc3dc85c8c4976b53643de1e03b2edc02`.

The exact production JSON was downloaded from the terminal artifact and persisted as `results/raw/source_faithful_joint_k5_bridge_gate.json`.

## Recovered-authority ordering

A later same-scope audit workflow, run `34952709428` on head `3889de168d1705ac57bdd8c022c49548cad26417`, terminated `failure`/`INVALID_IMPLEMENTATION` because its supersession guard detected the already-created positive bridge derivation and raw lock but had not ingested them. It produced no competing scientific verdict and no artifact.

`prereg/ITER083Q_CONTROL_ONLY_REPAIR_1.md`, commit `19697881b766a3d64c544c6696f2dba4bb4f0ea6`, was prospectively frozen only to repair that later audit. No repaired duplicate production is run because the earlier authoritative same-object gate `34952663240` is already terminal and complete.

## Exact source-faithful construction

The source object remains ordered as

`one-wedge spectral/spinor integration -> Toller function -> product of ten Toller matrices -> full 32-component boundary contraction -> K5 group integration / distributional extension`.

For a relative Lorentz element `h`, use the exact source Cartan rapidity and define

`q(h)=beta(h)^2 = arcosh(Tr(h h^dagger)/2)^2`.

Near the compact locus, with `s=Tr(h h^dagger)/2-1`,

`q=2s-(1/3)s^2+(1/30)s^3+...`.

Thus `q` is real analytic near `SU(2)`, nonnegative, vanishes exactly on the compact locus, and has the source-normal nondegenerate boost-normal Hessian.

For each collision block `B`, define

`q_B=(1/|B|) sum_{a<b in B} beta(g_b^-1 g_a)^2`.

This is source-derived, gauge/relabel/reversal covariant and agrees at quadratic order with the repaired Iter083M source-normal radial form.

The complete local collision arrangement contains 26 nontrivial blocks: 10 K2, 10 K3, 5 K4, 1 K5. The divergent family contains 16 blocks: 10 K3, 5 K4, 1 K5. The exact nested K3-K4-K5 normal ranks are `(6,3,3)`, so the resolved Haar-density radial powers are `(5,2,2)`.

On the iterated real blow-up of the clean polydiagonal arrangement, the frozen all-`j=1/2` Toller matrices lift to polyhomogeneous conormal matrix-valued functions. Multiplication of all ten source Toller matrices and contraction with all 32 frozen boundary components preserve that class.

The joint family is therefore defined by

`U(lambda) = [product_(B in D) q_B^(lambda_B/2)] A_source`,

where `D` is the 16-block divergent family and `A_source` is the actual source-ordered ten-Toller/full-boundary local integrand paired with the unchanged product Haar density.

The construction is applied **after** the published one-wedge Toller objects have been formed. It does not replace the published spectral `i epsilon`, does not use `beta+i epsilon`, and does not introduce an auxiliary regulator-space metric `Q`.

For sufficiently large real parts of the parameters, the lifted family is locally integrable. The polydiagonal-resolution plus Mellin/complex-power continuation framework gives the corresponding distribution-valued multivariate meromorphic continuation. Uniqueness here is uniqueness of the meromorphic continuation from the nonempty convergent parameter domain.

## B1-B9 result

Production returns all frozen bridge predicates true:

- B1: simultaneous true-K5 multivariate analytic/meromorphic family — PASS;
- B2: exact post-Toller source-to-joint-family map without spectral substitution — PASS;
- B3: full 32-component boundary contraction retained — PASS;
- B4: original Haar/group measure and source order retained, resolved Jacobian derived — PASS;
- B5: branch/sign/reversal and published spectral prescription preserved — PASS;
- B6: applicable resolved polyhomogeneous/Mellin complex-power continuation framework — PASS in the frozen local sector;
- B7: no extra finite-part/holomorphic-projection/subtraction choice is required to define the **polar germ** — PASS for bridge existence only;
- B8: S5 block covariance with no preferred label/chain/basis — PASS;
- B9: enough of the actual full local object is defined to authorize a multivariate polar-coefficient normal-jet gate — PASS.

Mechanical controls also passed: 26/26 block census, 16/16 divergent-block census, 20 maximal divergent chains, exact `(6,3,3)` ranks, exact `(5,2,2)` density powers, all 120 S5 relabelings, Laplacian/projector identities, and exact first source-radius series coefficients. All nine malformed bridge controls were rejected.

## New scientific fact

The Iter083P transition blocker is removed **for existence/definition of a frozen local full-source multivariate meromorphic polar object**.

Current authority now defines, in the frozen all-`j=1/2` local K5 collision sector, an actual full-boundary-contracted source-ordered multivariate meromorphic polar germ. This is stronger than an auxiliary radial/Hodge/Q surrogate and stronger than one-wedge analyticity: all ten wedges, true K5 incidence, the complete 32-component boundary contraction, source Haar density and causal/spectral conventions are retained.

## What is not solved

The result does **not** choose a holomorphic projection, Hadamard finite part, subtraction constant, physical renormalization condition or unique K5 extension. It therefore does not remove the exact frozen `377`-dimensional supported-extension selection problem.

It also does not authorize replacing the 16-parameter germ by a one-parameter family `rho^z u` or naming a unique `A_-1`. Any one-parameter specialization is an additional choice and requires a separate prospective authority test.

The authorized successor object is instead the actual multivariate polar family and its collision-stratum polar coefficients.

## Next dependency

After independent Critic review of this bridge, the next admissible Researcher gate is

`ACTUAL_SOURCE_ORDERED_MULTIVARIATE_POLAR_NORMAL_JET_ANNIHILATOR`.

That gate must determine the actual normal-jet orders/support channels of the full source polar coefficients and whether the source-derived nonlinear defining functions eliminate, preserve, or expose the finite-part freedom identified abstractly by Iter083N. It must not collapse the multivariate object to a one-parameter residue without separate authority.

## Interpretation ceiling

No unique predictive local K5 amplitude yet; no physical finite-part selector; no regulator-independence/dependence theorem; no causal-vertex finiteness/divergence theorem; no generic-spin completeness; no global all-strata patching; no E3/E4/E6 closure; no G3/F9/G8/K5 promotion; no RG/continuum/spin-2/GR/matter/prediction result; no `NEW_PHYSICS_FOUND`; no complete-QG claim.
