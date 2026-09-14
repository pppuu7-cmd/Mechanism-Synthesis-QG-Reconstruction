# Iter082D-SM prereg — repaired nested-normal-projector forest extension gate

Status: **PROSPECTIVE REPAIR GATE — frozen before Iter082D implementation/production**  
Date: 2026-09-14

## Trigger
Iter082C preregistration was prospective, but its implementation was rejected by `results/ITER082C_ADVERSARIAL_IMPLEMENTATION_REVIEW.md` with verdict `INVALID_IMPLEMENTATION`: it did not construct quotient-normal coordinates, did not evaluate genuinely distinct scheme realizations, and preassigned several negative-control outcomes.

Iter082D is a fresh repair. Historical Iter082C must not be patched or rerun into authority.

## Scope
Construct and test an explicit **linearized/tubular local nested-normal extension scheme class** for every maximal `K3 subset K4 subset K5` chain. This gate remains below a full nonlinear global `SL(2,C)^4` forest-extension theorem and below any physical selector.

## Exact collision-normal geometry
Work first in one spatial component on vertex-coordinate space `R^5`, with common translation as gauge direction. For each collision block `B subset {0,1,2,3,4}`, define the label-free barycentric orthogonal projector

`P_B[i,j] = delta_ij - 1/|B|` for `i,j in B`, and `0` otherwise.

Thus `im(P_B)` is the `( |B|-1 )`-dimensional internal difference space of the block and `P_B * 1 = 0`.

For every maximal chain `B3 subset B4 subset B5`, define exact nested normal increments

`A = P_B3`,

`B = P_B4 - P_B3`,

`C = P_B5 - P_B4`.

Required one-component ranks are

`rank(A)=2`, `rank(B)=1`, `rank(C)=1`,

with exact pairwise orthogonality/idempotence and

`A+B+C=P_B5`.

Tensoring with the physical three boost-vector components gives transverse dimensions `6+3+3=12` and identifies the nested normal-degree groups used below.

## S5 covariance
For every permutation matrix `U_pi`, require exact rational-matrix covariance

`U_pi P_B U_pi^-1 = P_{pi(B)}`

for every K3/K4/K5 block. The increment projectors of every maximal chain must transform into those of the permuted chain. No base vertex, minimum-label normal coordinate or label-dependent constant is allowed in the authoritative construction.

## Exact nested polynomial jet algebra
Represent a monomial by its total degrees `(a,b,c)` in the three orthogonal normal groups `(A,B,C)`. This degree algebra stands for the full `6+3+3` normal-variable polynomial algebra with multiplicities suppressed; Taylor eligibility depends only on these total degrees.

Freeze the Taylor projectors:

- K3: `T3` keeps monomials with `a <= omega3=0`;
- K4: `T4` keeps monomials with `a+b <= omega4=3`;
- K5: `T5` keeps monomials with `a+b+c <= omega5=8`.

Use an exact generic finite polynomial containing **all degree triples with total degree <=10**, with nonzero rational coefficients assigned deterministically from `(a,b,c)`.

## Two genuinely distinct admissible scheme realizations
Define two weight-jet families `chi` and `eta`. For each block size k, the weight must equal `1` through normal Taylor order `omega_k`; equivalently `weight-1` begins at normal degree `omega_k+1` in that block's normal variables.

The two families must be mechanically distinct. Example admissible shifts may differ in how degree `omega+1` is distributed across the nested normal groups, but both must pass the unit-jet condition.

For a polynomial `phi`, define exactly

`T_B^w phi = w_B * Taylor_B^(omega_B)(phi)`

and

`W_B^w = I - T_B^w`.

The authoritative inner-to-outer chain operator is

`W5^w o W4^w o W3^w`.

Do not introduce outer-first recursion as physically equivalent unless separately proved.

## Required tasks

### A. Projector geometry
For all 16 blocks verify exact rational:

- symmetry and idempotence of `P_B`;
- `rank(P_B)=|B|-1`;
- common-translation annihilation.

For all 20 maximal chains verify:

- ranks `(2,1,1)` for `(A,B,C)`;
- pairwise orthogonality;
- sum `A+B+C=P_B5`;
- tensor-with-R3 dimensions `(6,3,3)`.

### B. Full S5 transport
Check all 120 permutations on every block projector and all 20 chain increment triples.

### C. Multivariate Taylor action
On the complete degree-triple polynomial through total degree 10, verify mechanically that each `Wk` removes precisely the Taylor-eligible monomials at unit weight and that subtraction through `(0,3,8)` yields the scaling-degree remainder threshold. Under-subtraction by one order must exhibit the critical `-1` radial exponent.

### D. Distinct weight-scheme comparison
Construct two distinct admissible weight families `chi != eta`, run the full inner-to-outer chain operator for every one of the 20 chains, and compute the exact polynomial difference.

The difference is accepted as `SUPPORTED_ALLOWED_SCHEME_DIFFERENCE` only if the operator difference annihilates the common kernel of all allowed Taylor-jet maps and every input monomial on which it depends is visible to at least one permitted jet condition:

`a=0` or `a+b<=3` or `a+b+c<=8`.

Any dependence on a monomial invisible to all three allowed jet maps is an off-jet/nonlocal remainder and fails the gate.

### E. Sequential-vs-expanded operator identity
Mechanically expand the noncommutative ordered product

`(I-T5)(I-T4)(I-T3)`

without commuting the `Tk`, evaluate it on the polynomial model and verify equality with sequential application. This is a consistency check only and must be explicitly tagged `SAME_GRAPH_REASSOCIATION_NOT_SELECTOR`.

### F. Injected negative controls — no preassigned booleans
The implementation must construct and reject each of the following by the same validation functions used on the positive object:

1. **label-dependent projector:** a base/min-label difference coordinate that fails some S5 transport test;
2. **under-subtraction:** lower one nonzero omega and exhibit a nonintegrable radial exponent `<=-1`;
3. **bad weight jet:** inject `weight-1` at degree `<=omega` and require the unit-jet validator to reject it;
4. **source-order violation:** instantiate an object tagged as termwise contact multiplication before the ten-Toller product/full contraction and require the source-object validator to reject it;
5. **numeric finite-part smuggling:** insert a numeric finite coefficient/scale in the scheme configuration and require the symbolic-data validator to reject it;
6. **reassociation-as-selector smuggling:** mark the expanded/sequential identity as a selector equation and require the selector-firewall validator to reject that promotion.

No negative-control status may be assigned by a literal `True`/`False` without constructing the invalid object and running the validator.

## Frozen classification

### PASS
`ITER082D_SM_K5_NESTED_NORMAL_PROJECTOR_TAYLOR_FOREST_SCHEME_CLASS_CONSTRUCTED_EXACT_SCOPED`

iff A-F pass for all 20 chains and all 120 S5 permutations.

### FAIL
`ITER082D_SM_NESTED_NORMAL_FOREST_SCHEME_CONSTRUCTION_FAILS_EXACT_SCOPED`

if the positive construction fails an exact geometry/Taylor/scheme-support test.

`INVALID_IMPLEMENTATION_OR_PROVENANCE` for missing chronology, preassigned controls, incomplete chain/permutation coverage, hard-coded PASS labels, or post-hoc criterion changes.

## Interpretation ceiling
A PASS would establish an explicit **linearized/tubular local** source-covariant forest-extension scheme class with exact nested quotient-normal geometry and with scheme dependence confined, in the finite polynomial control, to allowed jet-visible data.

It would **not** yet prove:

- chart independence on the full nonlinear `SL(2,C)^4` group manifold;
- a global Toller forest extension;
- that the symbolic scheme freedom is physically equivalent;
- a physical selector;
- exact total ambiguity dimension;
- sufficiency of 28 conditions;
- regulator independence;
- causal E3/E4/E6 closure;
- RG closure;
- CRQN v0.3;
- `NEW_PHYSICS_FOUND`;
- complete QG.

If PASS, the next scientific gate is nonlinear tubular-chart overlap / chart-independence of the local extension class before any coefficient selection.