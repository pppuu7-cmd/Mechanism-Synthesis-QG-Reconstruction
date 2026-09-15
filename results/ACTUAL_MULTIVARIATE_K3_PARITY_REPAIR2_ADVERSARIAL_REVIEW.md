# Independent adversarial review — repaired actual multivariate K3 parity gate

**Date:** 2026-09-15

## Result reviewed

Researcher authority under review:

- scientific parent preregistration `4c4478db20e08387fb7067a55d773fce31d3fc34`;
- control-only repair-2 preregistration `b32fdab248ea8a95bbb716ba30b459a59e4d6b78`;
- repaired implementation `0d9124fd9ef63493cf02c50004c718e443f3e0ed`;
- production head `cec769eb9a379ae26a1ae657130b01618df729f5`;
- Researcher run `34958274852`, job `104345480753`, terminal success;
- artifact `10392590310`;
- artifact ZIP digest `sha256:ba387d6c1a8d72ff4e44f4961cac3f298c36821a0394f89dc86b3fc6b8acead5`;
- production JSON SHA256 `63f372003b01f9cf300969f18340d16017091a5254d37bf52c73bb3ae0ec3014`;
- durable result `results/ACTUAL_MULTIVARIATE_K3_PARITY_CONTROL_REPAIR2_RESULT.md`, commit `c90d26128e5d7b36c012d8285252e7ca91126474`.

Researcher classification:

`K3_PHYSICAL_ORIGIN_POLAR_COEFFICIENT_ZERO_EXACT_BY_NORMAL_INVERSION_PARITY`.

Researcher verdict: `PASS_EXACT_SCOPED`.

A separate Critic contract was frozen before Critic implementation:

- `prereg/ACTUAL_MULTIVARIATE_K3_PARITY_REPAIR2_INDEPENDENT_CRITIC_REVIEW.md`, commit `66cc63813bbcd66909c42b1672f35fab591e65f3`.

Independent Critic implementation / production:

- implementation `4a11025221088dda624a9134b2a15ef71c5733d3`;
- workflow/head `e15a709114fbf003d9d8bdc36e5739660bd60769`;
- run `34961204516`, job `104354954720`, terminal success;
- artifact `10393201960`;
- Critic artifact ZIP digest `sha256:ed37cdf047850692e16ed3d85053a4f5b3a8918465b1cdaa4b4e0afcec827ad9`;
- Critic JSON SHA256 `5e0c2937f1dccd831ebe5cd97b0a4180cb56ff64307d16f9d991cb5612ccac79`.

Independent Critic classification:

`K3_PARITY_REPAIR2_CRITIC_CONFIRMED_SCOPED`.

Mandatory review verdict:

**`CONFIRMED_SCOPED`**.

## Independent source-object and source-order attack

The reviewed object is not a termwise contact-distribution product and not a scalar K4/K5/Hodge surrogate. It is the already-confirmed 16-parameter `q_B`-scheme multivariate meromorphic germ built from the source-ordered all-`j=1/2` K5 object after one-wedge spectral/spinor integration has produced Toller functions, followed by the product of all ten Toller matrices, the complete boundary contraction and the K5 group/distributional object.

The Critic source lock independently verifies the repaired Iter077I leading matrix

`M(v)=[[v_z,-v_x-i v_y],[-v_x+i v_y,-v_z]]`

and the complete 32-dimensional boundary basis. Historical Iter077E/F remain quarantined under `status/ITER077_CONTACT_FORMULA_ERRATUM.md`; the K3 proof does not import their invalid contact transcription.

No exchange of the published spectral limit with termwise ten-distribution multiplication is used. No `beta+i epsilon` replacement is introduced. Fixed source branch signs multiply the K3 leading factors by angle-independent nonzero signs and therefore cannot change the parity conclusion.

## C1 — provenance and chronology

The independent production verifies by Git ancestry that:

- parent scientific preregistration precedes repair-2;
- repair-2 precedes Researcher implementation;
- Researcher implementation precedes production head;
- Researcher production head precedes the independent Critic preregistration;
- the Critic preregistration precedes Critic implementation/production;
- the Critic script did not exist at the Critic preregistration commit.

The repair-2 note explicitly freezes a control-only repair and leaves the parent hypothesis, physical object, verdict taxonomy and interpretation ceiling unchanged.

## C2/C3 — complete coefficient reconstruction and parity

The Critic independently reconstructs all ten K3 blocks using the actual Iter077I node intertwiner options and leg-incidence convention. The seven external collapsed Toller matrices are never evaluated at a representative angular ray: every external matrix entry is kept as an arbitrary formal degree-zero coefficient in the outer/tangential coefficient ring.

For each of the ten K3 blocks and each of all 32 boundary basis components, the Critic enumerates the raw node-contraction terms. Total independent census:

- 10 K3 blocks;
- 32 boundary components per block;
- 100,000 raw contraction terms per block;
- 1,000,000 raw contraction terms total.

Every raw monomial contains exactly three internal K3 matrix entries and seven external degree-zero matrix entries. Every internal leading entry is independently reconstructed as a nonzero linear form in the six barycentric K3 normal coordinates. Therefore every raw monomial has exact K3 normal degree three and changes sign under simultaneous normal inversion.

Possible cancellation among odd monomials can only produce another odd polynomial or zero; it cannot create an even part. Thus the complete contracted coefficient vector is odd in every one of all 32 boundary components, without representative-state selection and without choosing values for the seven external matrices.

## C4/C5 — Haar/front geometry and singular subfaces

The independent Critic derives the barycentric one-axis embedding

`(u,v) -> (u,v,-u-v)`

and obtains

`G=[[2,1],[1,2]]`.

Across three Cartesian axes the six-dimensional Gram determinant is exactly `27`. Simultaneous inversion is `-I_6`, has determinant `+1`, and preserves the Gram form exactly. The normal-order-zero coefficient of a smooth pulled-back source Haar density is therefore independent of the K3 front direction and is inversion-even.

Independently,

`(1/3)[|u-v|^2+|2u+v|^2+|u+2v|^2]`

has the same quadratic matrix `G`, so the `q_B` front is even and antipodally invariant.

The only K2 singular subfaces on the K3 front have local radial exponent

`(3-1)-2=0>-1`.

Two distinct K2 equalities would force all three K3 normal points to coincide, which is the excluded origin rather than a point on the unit K3 front. Thus there is no hidden overlapping nonintegrable K2 corner on the K3 front. Antipodal angular pairing is legitimate.

## C6 — true boundary S5 transport

A weakness in the Researcher helper was attacked directly: its S5 routine transports block labels and the tuple of two local intertwiner labels, which is coarser than the true induced incident-leg action on the 32-dimensional boundary space.

The independent Critic therefore reconstructs the two-dimensional four-spin singlet action under every local leg permutation from the actual Iter077I intertwiner tensors, assembles the full 32-dimensional K5 boundary action for all 120 vertex permutations and verifies every matrix has rank 32. The resulting class character is exactly

`(32,0,8,2,0,0,2)`,

matching the independently confirmed Iter083A boundary representation.

All 120 permutations also map the ten K3 blocks into the same ten-block orbit. Since the complete coefficient is the zero vector in all 32 components for every K3 block, the true induced-leg S5 action maps zero to zero. The scientific zero theorem is therefore genuinely S5 covariant even though the Researcher S5 helper alone was not a full boundary-representation transport proof.

## C7 — nested residues

The external Toller factors were kept as arbitrary outer/tangential degree-zero coefficients throughout the independent coefficient ring calculation. Hence the K3 angular pairing is the zero element of that coefficient ring, not merely zero at one outer configuration.

The vanishing occurs before any later K4/K5 Laurent extraction. Therefore any multiresidue containing that K3 face residue vanishes within the same frozen local meromorphic germ. This does not classify K4-only or K5-only polar coefficients.

## C8 — defining-function gauge

The confirmed joint bridge has a simple normal-crossing K3 face pole at the physical K3 hyperplane. For a holomorphic defining-function multiplier

`H(L)=h_0+h_1 L+h_2 L^2+...`,

and

`U=R/L+F_0+F_1 L+...`,

the only exponent pair contributing to the transformed `L^-1` coefficient is `(0,-1)`. Thus

`Res(HU)=h_0 Res(U)`.

An identically zero K3 residue stays zero. No invariance of finite parts or of all Laurent coefficients follows.

## C9 — malformed and counterexample controls

The independent Critic passes a valid candidate and rejects all ten frozen malformed classes through the same validator:

1. one-parameter `rho^z` replacement;
2. representative boundary component only;
3. omitted external wedges;
4. historical `(5,2,2)` nested density;
5. one angular point without front pairing;
6. representation multiplicity promoted to a source nonzero statement;
7. all Laurent coefficients falsely declared scheme invariant;
8. sequential finite part called the source residue;
9. omitted Haar/Jacobian;
10. imported invalid Iter077Q tangential family.

Two additional counterexample-first controls are rejected: a first-order external Taylor term misclassified as K3 order zero, and an odd leading Haar term.

Alternative boundary intertwiners do not rescue a nonzero channel because the complete 32-component coefficient vector vanishes; every linear combination therefore vanishes. A fixed alternative causal branch sign cannot change the angular oddness. No representative component or post-hoc state choice is used.

## C10 — overclaim firewall

Confirmation is strictly limited to the frozen all-`j=1/2`, local source-ordered, full-32-boundary, 16-parameter `q_B`-scheme meromorphic germ and to K3 face residues at the physical regulator origin.

It does not establish a K4 or K5 zero, a unique K5 extension, a physical finite part, regulator independence, global multistratum patching, generic-spin completion, causal E3/E4/E6 closure, G3/F9/G8/K5 promotion, RG closure, continuum geometry, spin-2, GR, matter/QFT, a normalized prediction, `NEW_PHYSICS_FOUND`, or complete quantum gravity.

The exact 377-dimensional supported extension-selection space remains a separate authority and is not removed by the K3 zero.

## Qualification on Researcher implementation

The Researcher script retains one literal `K3_11_no_k4_k5_overreach=True`. This is a non-substantive interpretation-ceiling flag, not a premise of the independent parity proof; the durable Researcher output also explicitly sets `k4_or_k5_conclusion=null`. The Critic production does not consume that boolean and independently enforces the no-overreach ceiling.

The coarse Researcher S5 helper similarly cannot by itself certify the true induced-leg representation, but the independent Critic closes that gap by reconstructing the full rank-32 S5 action.

Neither issue invalidates the independently established K3 zero.

## Verdict

`CONFIRMED_SCOPED`

The exact statement

`Res_(L_K3=0) U = 0`

is independently confirmed for every K3 block and every boundary component in the frozen local all-`j=1/2` source-ordered 16-parameter meromorphic germ. Every later multiresidue containing that K3 residue also vanishes in the same scope, and this zero is stable under the allowed holomorphic defining-function gauge.

## Authorized next gate

Do not repeat K3 parity, nearby Hodge tests or another order-zero surrogate. The next highest-information gate is a prospectively frozen

`ACTUAL_SOURCE_ORDERED_MULTIVARIATE_POLAR_NORMAL_JET_ANNIHILATOR_K4_LANE`.

It must extract the actual K4 normal-order-3 polar tensor under the already-confirmed 16-parameter source family, retaining:

- all ten source Toller wedges;
- source ordering and published spectral prescription;
- all 32 boundary components and the true induced-leg S5 action;
- exact K4 normal coordinates and nested K3/K4/K5 incidence;
- nonlinear/BCH group geometry;
- pulled-back source Haar density through total K4 normal order three;
- Toller Taylor data through the required order;
- all angular/subface singularities and exact distributional pairing;
- finite coefficients/scales symbolic;
- no sequential finite-part prescription promoted to a physical selector.

Counterexample-first targets should include an explicit nonzero K4 channel, boundary-intertwiner dependence, branch dependence, exceptional/rank-deficient strata, odd/even mixing from order-one to order-three external/Haar/BCH corrections and incompatible nested gluing. If the exact order-three source coefficient cannot be defined or computed without a surrogate or an unauthorized exchange of distributional limits, the successor must return the appropriate blocker rather than infer a K4 verdict. K5 order eight remains downstream of an independently reviewed K4 lane.
