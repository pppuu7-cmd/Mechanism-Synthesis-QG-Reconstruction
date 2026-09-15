# Control-only repair 2 — actual multivariate K3 polar parity implementation

Date: 2026-09-15
Status: **PROSPECTIVELY FROZEN BEFORE REPAIR IMPLEMENTATION OR REPAIRED OUTPUT INSPECTION**

## Parent scientific contract

The scientific parent remains unchanged:

`prereg/ACTUAL_SOURCE_ORDERED_MULTIVARIATE_POLAR_NORMAL_JET_ANNIHILATOR.md`, commit `4c4478db20e08387fb7067a55d773fce31d3fc34`.

The proposed K3 theorem remains the unchanged scoped hypothesis from

`sources/ACTUAL_MULTIVARIATE_POLAR_K3_PARITY_DERIVATION.md`, commit `78e63844a8fe0a70af9ac8dc574d358e7ecab927`.

The scientifically usable upstream bridge remains the repaired, independently confirmed 16-parameter source-faithful K5 meromorphic bridge, with corrected nested density powers `(5,8,11)` and face forms `L_C(lambda)`.

No K4/K5 scientific outcome, finite part, selector, regulator-independence claim, candidate version, boundary state, branch convention, source normalization or interpretation ceiling is changed by this repair.

## Why repair 2 is required

Independent Critic review `results/ACTUAL_MULTIVARIATE_K3_PARITY_ADVERSARIAL_IMPLEMENTATION_REVIEW.md`, commit `57e00152548b3ba8ab12c98c9b3145684d115d98`, classified repaired run `34955160116` as `INVALID_IMPLEMENTATION` although no exact scientific counterexample to the K3 parity hypothesis was found.

Repair 1 was prospectively restricted to a provenance-text needle and therefore cannot authorize the broader implementation corrections required below.

The successor implementation must not use hard-coded scientific acceptance booleans for the decisive parity premises.

## Frozen control-only implementation obligations

### R1 — consume the actual 16-parameter bridge object

Mechanically construct the exact divergent-block set consisting of all 10 K3, 5 K4 and 1 K5 blocks. Validate the normal-crossing face-coordinate object against this 16-parameter set. A one-parameter replacement is malformed.

### R2 — explicit K3 normal-coordinate geometry

For each K3 block `B={a,b,c}`, use barycentric incremental boost-normal coordinates

`y_a=u`, `y_b=v`, `y_c=-u-v`,

with six independent real normal coordinates. Mechanically derive:

- the three internal edge differences as nonzero linear forms in those six coordinates;
- the seven external edges as zeroth-order K3-normal Toller matrix factors evaluated at the collapsed block point, hence formal functions of tangential/outer variables but normal degree zero;
- the source quadratic front radius

`q_B/rho_B^2 -> (1/3) sum_(i<j in B) |y_i-y_j|^2`,

and verify its exact invariance under simultaneous inversion `(u,v)->(-u,-v)`.

No fixed-ray external factor may substitute for this derivation.

### R3 — pulled-back Haar/front density

Mechanically construct the linear barycentric normal embedding `R^6 -> {(y_a,y_b,y_c): y_a+y_b+y_c=0}` and its exact Gram matrix. Verify that simultaneous inversion preserves the Gram form and has absolute determinant one. Because the K3 pole uses normal Taylor order zero, the leading pulled-back source Haar/tubular coefficient is the source Haar value on the collapsed stratum times this constant linear normal volume factor; it must therefore be certified angle-independent and inversion-even by the computation rather than an assigned Boolean.

Higher-order Haar corrections are outside the K3 order-zero coefficient and may not be used to infer K4/K5 results.

### R4 — full 32-component symbolic contraction certificate

Using the actual Iter077I node intertwiner options, leg incidence and all ten K5 edges, construct or symbolically certify the K3 order-zero boundary-contracted coefficient for all 32 all-`j=1/2` boundary components.

For each contraction term:

- every one of the three internal K3 edge entries must be an explicit homogeneous normal-linear form derived from the Iter077I leading matrix `M(v)`;
- every one of the seven external edge entries must be represented as an arbitrary formal collapsed Toller matrix entry of normal degree zero;
- the implementation must enumerate the actual boundary contraction terms and certify that every nonzero term has total K3 normal degree exactly three.

The resulting 32 component coefficients must therefore be certified odd under K3 inversion without evaluating a single frozen angular ray. A fixed-ray `exact_full32()` checksum alone is insufficient.

### R5 — angular zero and K2 integrability

The zero certificate must be derived from the computed facts:

- full 32-component coefficient odd under inversion;
- K3 quadratic front and leading source-Haar density even;
- inversion preserves the angular domain;
- each internal K2 singularity has relative three-dimensional radial exponent `(3-1)-2=0>-1`, so the front-face angular pairing is locally integrable.

Only then may the implementation classify the K3 face residue as exact zero.

### R6 — coefficient-level S5 transport

Mechanically transport the K3 block class through all 120 permutations. It is sufficient for the zero theorem to certify that every permuted K3 block is mapped to one of the ten K3 blocks, that the 32 boundary labels are permuted bijectively, and that the full symbolic contraction certificate for the image block remains odd in all 32 components. A mere internal-edge-count check is insufficient.

### R7 — nested multiresidue and defining-function gauge

Derive, not assign, that the K3 residue coefficient vanishes as a formal function/meromorphic coefficient of all outer variables before K4/K5 extraction. Therefore any later coefficient extraction containing the K3 face is zero.

For an allowed holomorphic defining-function gauge multiplier, mechanically verify the simple-face Laurent convolution rule

`Res_L(HU)=H|_(L=0) Res_L(U)`

for the K3 simple pole. Hence an identically zero K3 residue remains zero. Do not claim all Laurent coefficients are scheme invariant.

### R8 — execute the ten parent malformed controls through the same validator

The repaired implementation must instantiate and reject all ten malformed constructions frozen in the parent preregistration:

1. one-parameter `rho^z u` replacement;
2. representative boundary component only;
3. omission of external smooth wedge factors;
4. old nested-density tuple `(5,2,2)`;
5. one angular point used as a nonzero residue certificate without angular pairing;
6. positive representation multiplicity promoted to source nonzero;
7. all Laurent coefficients declared scheme invariant;
8. sequential finite-part ordering called the source residue;
9. omission of Haar/Jacobian factors;
10. import of the invalid historical Iter077Q tangential family.

Each malformed object must be fed through the same structural/scientific validator used for the positive object. Additional controls are allowed but do not replace these ten.

## Frozen verdict taxonomy

If the repaired implementation is execution-valid and the full coefficient-level parity certificate succeeds, retain the parent scoped scientific classification

`K3_PHYSICAL_ORIGIN_POLAR_COEFFICIENT_ZERO_EXACT_BY_NORMAL_INVERSION_PARITY`

with verdict `PASS_EXACT_SCOPED`.

If an exact computation contradicts the frozen K3 parity prediction, return `FAIL_EXACT_SCOPED`.

If the required source coefficient cannot be constructed exactly, return the appropriate parent blocked classification rather than inventing a surrogate.

Implementation/provenance defects remain `INVALID_IMPLEMENTATION`.

## Interpretation ceiling

A repaired K3 PASS would establish only the actual K3-face polar coefficient zero in the frozen all-`j=1/2` local 16-parameter source-faithful meromorphic germ, plus the algebraic consequences for multiresidues containing a K3 factor and the zero's defining-function-gauge stability. It would not classify K4 or K5 polar coefficients, choose a finite part, remove the exact 377-dimensional physical extension-selection ambiguity, prove regulator independence, global patching, causal multivertex closure, G3/F9/G8/K5 promotion, RG/continuum/spin-2/GR/matter/prediction results, `NEW_PHYSICS_FOUND`, or complete quantum gravity.
