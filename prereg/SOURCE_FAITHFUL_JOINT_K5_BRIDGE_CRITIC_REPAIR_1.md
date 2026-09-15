# Critic control/scientific repair preregistration — nested blow-up Jacobian correction

Date: 2026-09-15
Status: **PROSPECTIVELY FROZEN BEFORE ALTERING THE CRITIC VERDICT OR RESEARCHER DERIVATION**

Parent bridge preregistration: `4151c02452edd3e5e2c49952686e42e64c6dc180`.
Researcher repaired result: `79d166fdf89a9e42a653ed3bbb4b0cac426820da`.
Initial Critic review: `results/SOURCE_FAITHFUL_JOINT_K5_BRIDGE_ADVERSARIAL_REVIEW.md`, commit `d22ee01756a59f7e31e9fe643d3679e02c4850f6`.

## Newly found defect

The Researcher derivation/lock/validator and initial Critic review identified the orthogonal incremental normal dimensions along a maximal chain `K3 subset K4 subset K5` as `(6,3,3)` and then incorrectly converted these directly to resolved boundary-density powers `(5,2,2)`.

For the actual nested real blow-up, the boundary defining functions are hierarchical scales, not independent absolute polar radii for the three orthogonal summands.

Write the orthogonal normal decomposition as

- `u3 in R^6` for the K3 internal normal;
- `u4 in R^3` for the K4/K3 added normal;
- `u5 in R^3` for the K5/K4 added normal.

At the maximal nested corner the blow-up coordinates have leading scaling

`u5 = rho5 * angular`,

`u4 = rho5 rho4 * angular`,

`u3 = rho5 rho4 rho3 * angular`.

Therefore the Euclidean/Haar leading density scales as

`rho5^(12-1) rho4^(9-1) rho3^(6-1)`

or, ordered inner-to-outer,

`(rho3^5, rho4^8, rho5^11)`.

The previous `(5,2,2)` powers are the powers of independent polar coordinates on the orthogonal summands, not the boundary Jacobian powers of the nested blow-up used by the Mellin continuation argument.

## Immediate scientific consequence

The frozen B4 predicate required the transformed density/Jacobian to be derived explicitly. The currently promoted B4 PASS is therefore not scientifically established.

The initial Critic verdict `CONFIRMED_SCOPED` must be superseded by `REJECTED_SCIENTIFIC_PENDING_REPAIR` unless a prospectively frozen Researcher repair re-derives B4/B6 correctly and obtains fresh production.

## Repair target already implied by authoritative scaling data

The correction is structurally consistent with authoritative K3/K4/K5 divergence orders. In hierarchical coordinates the ten `j=1/2` wedge singularities scale as

- K3 internal edges: `rho3^-6 rho4^-6 rho5^-6`;
- all K4 internal edges: `rho4^-12 rho5^-12` cumulatively;
- all K5 internal edges: `rho5^-20` cumulatively.

Multiplying by the corrected density gives

`rho3^(5-6)=rho3^-1`,

`rho4^(8-12)=rho4^-4`,

`rho5^(11-20)=rho5^-9`,

which reproduces the already-authoritative superficial divergence degrees

`omega_K3=0`, `omega_K4=3`, `omega_K5=8`.

## Frozen repair discipline

A valid scientific repair must:

1. replace `(5,2,2)` by the hierarchical cumulative powers `(5,8,11)` in every B4/B6 derivation/lock/validator/result/provenance field;
2. mechanically derive those powers from cumulative normal dimensions `(6,9,12)`, not hard-code them as a target;
3. verify the source ten-wedge scaling gives radial exponents `(-1,-4,-9)` on every maximal nested chain;
4. derive the regulator hyperplane forms at a chain from the actual block inclusion incidence;
5. re-establish a nonempty convergence chamber and meromorphic continuation with the corrected exponents;
6. rerun all unchanged B1-B9 and malformed controls;
7. preserve the existing defining-function scheme firewall and finite-part interpretation ceiling.

No B1-B9 wording or classification taxonomy may be changed by the repair.