# Iter078E-RG preregistration — minimal integrated extension-coupling space in the full 32-component j=1/2 boundary sector

**Date:** 2026-09-14

## Scientific question

Before constructing an RG/refinement truncation, what is the **minimum** dimension of the supported extension freedom that must be carried by the controlling all-`j=1/2` boundary amplitude?

Iter077M/N exhibited one explicit scalar direction `c L`, but Iter077L's extension theorem permits a much larger order-8 supported-jet space. It is invalid to build an RG flow on one scalar `c` unless a reduction theorem exists.

## Frozen object

Boundary Hilbert space in the controlling minimal sector:

`H_B = Inv[(1/2)^⊗4]^{⊗5}`

with the same five recoupling labels `k_a in {0,1}` and complete basis size

`dim H_B = 2^5 = 32`.

For each basis state `|alpha>` let

`u_alpha(g)`

be the scalar source-ordered fixed-causal vertex distribution off the common-collision set `N=SU(2)^4`, after contraction with that boundary basis state.

Iter077L guarantees local same-scaling-degree extensions componentwise and allows supported differences with normal derivative order up to 8. This gate tests only the **order-zero** subspace proportional to `delta_N`; higher normal derivatives can only enlarge the ambiguity.

## Prospective construction

Choose any one reference extension `bar u_alpha` for every `alpha`. For a frozen vector of complex constants

`c = (c_1,...,c_32) in C^32`,

define

`bar u_alpha^(c) = bar u_alpha + c_alpha delta_N`.

Equivalently, for an arbitrary boundary state `Psi=sum_alpha psi_alpha |alpha>`,

`A_c(Psi) = A_ref(Psi) + delta_N * sum_alpha c_alpha psi_alpha`.

The supported term must be checked against the source-backed symmetry/boundary structure; no basis component may be selected post hoc.

## Frozen checks

### Lane A — componentwise extension theorem

Verify that:

- `delta_N` has transverse scaling degree 12;
- adding it to any component does not raise the maximal source scaling degree 20;
- all 32 coefficients are independent at the level of finite-dimensional boundary dual space unless an explicit source symmetry relates them.

### Lane B — true boundary/gauge covariance

Verify that the `|alpha>` basis consists of genuine SU(2)-invariant five-node boundary spin-network states, not scalar K4/K5 surrogates. The coefficient functional

`ell_c(Psi)=sum_alpha c_alpha psi_alpha`

is a linear functional on the actual gauge-invariant boundary Hilbert space.

The pre-gauge supported distribution is placed on the same invariant common-collision set used in Iter077M. Global `SL(2,C)` gauge invariance acts on group variables, not on the already gauge-invariant boundary coefficients, so it does not by itself identify distinct `c_alpha`.

### Lane C — relabeling/causal-symmetry audit

Audit the primary causal-vertex source for an explicit condition forcing the 32 coefficients to one common number or to a lower-dimensional fixed subspace for a **fixed labelled causal boundary graph**.

Covariance under simultaneous relabeling of the graph, boundary state and causal labels is not the same as invariance of `c_alpha` under holding labels fixed. Do not use permutation covariance to collapse the coupling space unless the source states the required identification.

## PASS

PASS iff the order-zero supported ambiguity contains an injective copy of the full boundary dual `H_B^*`, giving the exact lower bound

`dim_C ambiguity_image >= 32`

in the frozen minimal sector.

Classification:

`ITER078E_RG_INTEGRATED_EXTENSION_THEORY_SPACE_HAS_AT_LEAST_FULL32_ORDERZERO_BOUNDARY_DUAL_DIRECTIONS_EXACT_THEOREM_SCOPED`

## FAIL

FAIL iff a frozen source-backed symmetry/theorem identifies enough component coefficients that the full 32-dimensional order-zero construction is not admissible.

## BLOCKED

BLOCKED iff componentwise extension or gauge covariance of the supported basis functionals cannot be established.

## Interpretation ceiling

PASS is a lower bound only. Order-1 through order-8 normal derivatives and nonconstant/distributional coefficient data along `N` may enlarge the space substantially or make it infinite-dimensional before further symmetry conditions.

PASS does not say all 32 directions survive the fully integrated vertex with nonzero values under one particular compact coefficient choice; it says there are at least 32 independent admissible supported extension directions as linear functionals on the 32-dimensional boundary sector before an external selector is imposed.

No RG fixed point, no regulator independence, no generic-spin theorem, no unique extension, no G3 or complete-QG claim.