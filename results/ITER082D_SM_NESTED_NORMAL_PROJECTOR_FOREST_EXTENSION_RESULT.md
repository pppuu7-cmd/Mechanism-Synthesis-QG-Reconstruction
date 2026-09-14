# Iter082D-SM — repaired nested-normal-projector forest extension RESULT

Date: 2026-09-14

## Provenance

- predecessor Iter082C implementation review: `974bb1c9d1c1d0dd3ff4078aed199e7d1691226f`, verdict `INVALID_IMPLEMENTATION`;
- prospective preregistration: `09b1affb5489e0dfcbe01b0100e0fc8a44aded98`;
- implementation: `ed15c5436a3d83b0119faea9a94e9f7a74b76189`;
- production head: `6b60bdeb6497883b92429719988b4869cd552e5b`;
- GitHub Actions run: `34894909845`, terminal `success`;
- job: `104146361380`, terminal `success`;
- artifact: `10368183868`, name `iter082d-sm-aggregate`;
- artifact ZIP digest: `sha256:9d53b4e491e3b9698acb7f1a4880413ea123c0f4508d3b9296328226175e930e`;
- extracted aggregate JSON SHA256: `59da0938b82730bf51c6ed98f3da838216732a279a4559fee7e48ba8c867c35f`;
- downloaded aggregate independently matched the local prerelease exact output byte-for-JSON-content.

## Classification

`ITER082D_SM_K5_NESTED_NORMAL_PROJECTOR_TAYLOR_FOREST_SCHEME_CLASS_CONSTRUCTED_EXACT_SCOPED`

Verdict: **PASS_EXACT_SCOPED**.

## Exact nested normal geometry

For every collision block `B`, the label-free barycentric projector

`P_B[i,j] = delta_ij - 1/|B|` for `i,j in B`

was constructed with exact rational arithmetic.

Across all 16 divergent blocks:

- `P_B` is symmetric;
- `P_B^2=P_B`;
- `rank(P_B)=|B|-1`;
- the common translation vector is annihilated.

For all 20 maximal chains `B3 subset B4 subset B5`, the exact increments

`A=P_B3`,

`B=P_B4-P_B3`,

`C=P_B5-P_B4`

satisfy:

- one-component ranks `(2,1,1)`;
- pairwise orthogonality;
- idempotence;
- `A+B+C=P_B5`.

After tensoring with the physical three boost-vector components this gives the nested transverse decomposition

`6 + 3 + 3 = 12`.

Thus the K3/K4/K5 chain now has an explicit label-free quotient-normal algebra rather than only subset metadata.

## Exact S5 covariance

All 120 permutations were checked.

- block-projector covariance checks: **1920/1920**;
- chain-increment covariance checks: **7200/7200**.

For permutation matrix `U_pi`:

`U_pi P_B U_pi^-1 = P_{pi(B)}`

and the three increment projectors transport to the corresponding permuted chain exactly.

A deliberately label-dependent min/base-vertex projector was injected and mechanically rejected by the same covariance test.

## Taylor / scaling-degree scheme

The polynomial control uses degree triples `(a,b,c)` in the orthogonal normal groups `(A,B,C)`, representing the full nested normal polynomial algebra with multiplicities suppressed. All **286** degree triples with total degree `<=10` were included with nonzero exact rational coefficients.

Frozen Taylor visibility:

- K3: `a<=0`, `omega_3=0`;
- K4: `a+b<=3`, `omega_4=3`;
- K5: `a+b+c<=8`, `omega_5=8`.

For K3/K4/K5, subtraction through the authoritative `omega=(0,3,8)` gives radial remainder exponent including measure exactly `0`, while one-order under-subtraction gives exactly `-1` in every case.

Thus the local scaling-degree/Taylor mechanism is explicitly realized in the repaired nested normal coordinates.

## Distinct scheme comparison

Two mechanically distinct weight-jet families `chi` and `eta` were constructed. Each equals one through the required normal Taylor order and differs only beginning at normal order `omega_B+1`.

Both full inner-to-outer operators

`W5 o W4 o W3`

were evaluated exactly.

Results on the complete degree-triple control space:

- scheme difference is nonzero, so the comparison is not a trivial duplicate;
- **198** input degree classes affect the scheme difference;
- **88** input degree classes lie in the common kernel of all allowed Taylor-jet maps;
- scheme difference annihilates **88/88** common-kernel classes;
- invisible-input violations: **0**.

Hence, in this finite exact nested polynomial control, changing the admissible weight scheme changes the operator only through data visible to at least one allowed K3/K4/K5 normal-jet map. No off-jet remainder was found.

This result holds for all 20 geometrically distinct maximal chains.

## Sequential / forest-expansion check

The ordered operator

`(I-T5)(I-T4)(I-T3)`

was expanded without commuting the Taylor operators and compared with direct sequential application for both scheme families.

Exact result: **identical**.

This is explicitly classified as a same-graph consistency identity, not a selector equation, in accordance with the imported CDSR T4 firewall.

## Negative controls

All six frozen invalid constructions were injected and rejected mechanically:

1. label-dependent projector fails S5 transport;
2. under-subtraction leaves nonintegrable exponent `<=-1`;
3. bad weight with a forbidden low-order normal term fails the unit-jet validator;
4. termwise contact multiplication before the ten-Toller/full-boundary source object fails the source-order validator;
5. a numeric finite coefficient fails the symbolic-finite-data validator;
6. promoting same-graph reassociation to a selector equation fails the selector firewall.

No negative-control PASS was assigned by a literal predeclared boolean.

## Scientific meaning

Iter082D repairs the implementation defect of Iter082C and establishes an explicit, label-free, S5-covariant **linearized/tubular local forest-extension scheme class** for the nested K3/K4/K5 collision geometry.

The result is stronger than Iter082B's combinatorial architecture: quotient-normal spaces and exact Taylor operators are now constructed, and nontrivial admissible scheme changes are shown in the finite polynomial control to remain within jet-visible data.

However the scheme freedom is real. The result does not select any subtraction constants, scales, K3/K4 tangential coefficient functions, or deepest K5 invariant-jet coefficients.

`finite_parts_selected = false`.

`physical_selector_derived = false`.

`unique_k5_extension = false`.

`nonlinear_chart_independence_established = false`.

## Interpretation ceiling

This is **not yet** a global analytic extension theorem for the full nonlinear `SL(2,C)^4` K5 group manifold.

Not established:

- overlap compatibility of different nonlinear tubular/group charts;
- independence from exponential/KAK/local-coordinate choice;
- physical equivalence of different symbolic weight schemes;
- a source-derived finite-part selector;
- exact total physical ambiguity dimension;
- sufficiency of 28 conditions;
- regulator independence;
- causal E3/E4/E6 closure;
- RG closure;
- CRQN v0.3;
- `NEW_PHYSICS_FOUND`;
- complete quantum gravity.

The demonstrated deepest `J_inv` dimension 28 remains a lower bound/subspace result only.

## Updated blocker

The combinatorial forest blocker and the **linearized nested-normal operator construction** are now closed in their stated scopes.

The next analytic blocker is:

`K5_NONLINEAR_TUBULAR_CHART_OVERLAP_AND_EXTENSION_CLASS_INDEPENDENCE`.

A successor gate must compare prospectively frozen nonlinear local charts on `SL(2,C)^4`, transport the nested normal projectors/Taylor jets through their transition maps, and determine whether chart changes alter the extension only by the already-allowed supported jet data. It must keep all finite coefficients symbolic and must not treat chart compatibility as a selector law.
