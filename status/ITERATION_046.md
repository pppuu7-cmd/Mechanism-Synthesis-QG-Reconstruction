# Iteration 046 — K4 forest / cycle-basis / integration-order consistency

Date: 2026-09-12

## Motivation
Iter045 established, on 40 held-out K3 parameter points, that the exact polynomial-subtraction plus residue/PV finite-part rule is invariant under choosing q1, q2, or q3 as the redundant common-cycle coordinate. K3 has only one independent cycle. A genuine extension candidate must survive graphs with more than one cycle, where a new ambiguity appears: the result could depend on the spanning tree / fundamental-cycle basis or on the order in which cycle variables are extended.

A development-only implementation probe used `(gamma,epsilon,signs,k)=(0.7,0.07,++++++,(0.17,-0.29,0.41,-0.29))` and is excluded from production acceptance below. No production parameter point below was inspected before this preregistration.

## Frozen K4 source object
Use the complete graph K4 with vertices `{0,1,2,3}` and oriented edges

`01, 02, 03, 12, 13, 23`.

Introduce real edge-flow variables `x_e = sigma_e q_e`. The three independent reduced incidence constraints are

`B_red x = k_red`, with `sum_v k_v = 0`.

For branch sign `sigma_e = +/-1`, the source-faithful j=1/2 edge factor is

`[1 + c1*x_e + (c2/2)*x_e^2] / [x_e - i*sigma_e*epsilon]`,

because the sign transformation from q to x has unit absolute Jacobian. The K4 source kernel is the product of the six edge factors.

For a spanning tree T, solve the three tree-edge flows from the incidence constraints and use the three chord flows as fundamental cycle coordinates. For K4 incidence minors, `|det B_T|=1`; this must be checked in every job, so no tree-dependent measure factor is hidden.

## Frozen one-dimensional operator
At every sequential integration step, apply **exactly the Iter045 operator without retuning**:

1. exact polynomial division in the current real cycle variable `u`, `K=Q+r`;
2. retain only the proper rational remainder `r=O(1/u)`;
3. define

`FP_u[K] = 2*pi*i*sum Res(r, upper-half-plane poles) - i*pi*a_minus1`,

where `a_minus1 = lim_{u->infinity} u*r(u)`.

No fitted subtraction, extra finite counterterm, order-dependent adjustment, or post-result tolerance change is allowed.

## Forest / basis set
Freeze four labeled spanning trees covering both K4 tree isomorphism classes and different label placements:

- `S0 = {01,02,03}` (star at 0)
- `S1 = {01,12,13}` (star at 1)
- `P0 = {01,12,23}` (path 0-1-2-3)
- `P1 = {02,12,13}` (path 0-2-1-3)

For each tree test all six orders of its three chord variables: `012,021,102,120,201,210`.

## Held-out production cases
Case A:
- gamma `0.83`
- epsilon `0.06`
- signs `++++++`
- external vertex flow `k=(0.19,-0.31,0.27,-0.15)`

Case B:
- gamma `1.43`
- epsilon `0.12`
- signs `-++-++`
- external vertex flow `k=(-0.22,0.37,-0.28,0.13)`

Both satisfy `sum k=0` exactly.

This gives 2 cases x 4 trees x 6 orders = **48 independent source jobs**.

## Ordinary EPRL / no-contact control
In every job, repeat the same constrained K4 calculation with numerator `F_e=1` on every edge while keeping the same Feynman pole locations. This control has no contact-generating polynomial numerator. The aggregate is scientifically interpretable only if the control is invariant across all tested trees and orders to exact symbolic equality when simplification succeeds, or numerical relative spread `<1e-10` otherwise.

## Prospective classification
For each production case:

- `K4_FINITE_PART_FOREST_ORDER_COVARIANT` only if all 24 source results (4 trees x 6 orders) are exactly equal after simplification, with numerical relative spread `<1e-10`, and the EPRL control also passes.
- `K4_FINITE_PART_ORDER_OR_FOREST_DEPENDENT` if the EPRL control passes but the source finite part differs between any frozen tree/order by relative spread `>=1e-10` or exact symbolic inequality.
- `K4_CONTROL_INVALID` if the EPRL/no-contact control itself fails invariance; this blocks scientific interpretation and triggers numerical/implementation diagnosis rather than a source-physics conclusion.

A negative source result is a scientific result and must not be repaired by changing subtraction rules or choosing a preferred forest/order after inspection.

## Claim lock
Even a full K4 PASS would establish only consistency of this particular sequential correlated finite-part prescription on the frozen K4 source representation. It would not yet prove K5 consistency, equality to the physical causal spinfoam vertex, RG closure, G3, F9, G8, continuum recovery, or a new quantum-gravity theory. A K4 PASS authorizes K5; a K4 source FAIL with valid control localizes the obstruction to multi-cycle extension consistency.

## Terminal result — 2026-09-12

**Scientific classification:** `K4_FINITE_PART_ORDER_OR_FOREST_DEPENDENT`.

The frozen sequential K3 finite-part rule does not extend consistently to the frozen K4 multi-cycle problem. The source result depends on integration order / fundamental-cycle basis while the ordinary EPRL/no-contact control remains invariant.

Authoritative repaired Case-B production:

- launch/repaired commit: `d9f1b29489dfe7a72e44e950da3374c1e956aee5`
- workflow run: `34703606792`
- aggregate job: `103579919585`
- Case-B lanes: `24/24`
- `source_exact_equal = false`
- `source_relative_spread = 0.5903762046739115`
- `control_exact_equal = true`
- `control_relative_spread = 0.0`
- maximum source discrepancy: `231.10329057111215`

Maximum-discrepancy witness:

- `P0 / order 210`: `148.3411417653609952967291 + 178.1028830014885424045242 i`
- `S0 / order 120`: `372.2794601126873799933901 + 121.0033165533324625781631 i`

Case A independently showed the same source order/basis dependence with exact control invariance before the Case-B metadata repair. The repair changed only serialization/metadata handling and did not alter the frozen finite-part algebra.

### Terminal interpretation

This is a controlled negative result for the **sequential one-dimensional extension prescription** on a multi-cycle K4 source. It is not a theorem that the physical causal vertex diverges or is undefined. It forbids promoting the K3 prescription by choosing a preferred order/tree after inspection.

`K5` is therefore **BLOCKED**. The next permitted gate is exact localization of the K4 obstruction through pairwise commutators of the unchanged finite-part operators (Iter047), followed—if noncommutativity is confirmed—by a preregistered genuinely multivariate correlated extension rather than order selection or post-hoc counterterms.
