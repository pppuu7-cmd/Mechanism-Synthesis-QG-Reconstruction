# Iter077Q-SM preregistration — invariant tangential extension-ambiguity dimension

**Date:** 2026-09-14

## HYPOTHESIS

The source-compatible same-scaling-degree K5 extension freedom exposed by Iter077L/M is not merely a one-parameter constant ambiguity. After imposing the source-backed constraints already frozen in Iter077M (common left `SL(2,C)` gauge covariance, true spin-network boundary object, fixed causal labels, source ordering, and relabeling covariance), the supported `delta_N` sector still contains an infinite-dimensional smooth tangential coefficient space.

## EXACT OBJECT

The actual K5 common-collision submanifold

`N = SU(2)^4 subset SL(2,C)^4`

after the source gauge `g_1=1`, together with the supported extension family

`A_ext + h(y) F_SU2(y;Psi) delta_N(x)`

where `F_SU2` is the true compact restriction of the source spin-network boundary functional from Iter077M and `h` is a smooth tangential scalar built only from relative compact group elements.

No scalar K4/K5 surrogate is allowed.

## DEPENDENCY TESTED

Whether the remaining local-amplitude ambiguity can reasonably be represented by one/finitely many source-selected couplings, or whether the already-authorized extension theorem plus source symmetries leave a functional ambiguity before any new renormalization/composition principle is added.

## SOURCE / THEOREM AUTHORITY

- `results/ITER077L_SM_TRANSVERSE_SCALING_DEGREE_EXTENSION_THEOREM_RESULT.md`: codim `12`, transverse scaling degree `20`, supported normal-jet freedom through order `8`, with coefficient data along `N` subject to separately imposed conditions.
- `sources/ITER077M_SM_SOURCE_SYMMETRY_SELECTOR_DERIVATION.md` and `results/ITER077M_SM_SOURCE_SYMMETRY_EXTENSION_SELECTOR_RESULT.md`: `F_SU2 delta_N` is compatible with the frozen source object, common left gauge symmetry, true boundary representation, fixed causal sector and source ordering.
- `results/ITER077M_ADVERSARIAL_COMPACT_BOUNDARY_CONTROL.json`: at least one true minimal-sector boundary functional has nonzero compact restriction (the previous exhaustive control found 16/32 nonzero).
- Primary causal-vertex source remains Bianchi–Chen–Gamonal, arXiv:2601.23162; no new physical selector is imported.

## FROZEN INVARIANT FAMILY

Before gauge fixing use five group variables on the common-collision set with all relative elements in `SU(2)`. Define the permutation-symmetric tangential scalar

`Q(g) = sum_(1<=a<b<=5) tr_1/2(g_b^-1 g_a)`.

On the gauge slice `g_1=I`, define

`h_n(y)=Q(y)^n`, `n=0,1,2,...`.

The trace is the fundamental `SU(2)` trace. No coefficient/function may be changed after calculation.

## POSITIVE CONTROLS

1. Common-left gauge: every relative element is unchanged under `g_a -> H g_a`, so `Q` must be unchanged.
2. Vertex relabeling: because `Q` sums over all unordered pairs, every permutation of the five labels must leave `Q` unchanged.
3. Nonconstancy path: on `N`, freeze
   `g_1=g_3=g_4=g_5=I`, `g_2=diag(e^{it},e^{-it})`.
   The exact target is `Q(t)=12+8 cos(t)`, hence `Q` is nonconstant.
4. Scaling: multiplying `F_SU2 delta_N` by any smooth `h_n` must retain transverse scaling degree `12`, hence remain inside the Iter077L same-scaling-degree class with total maximum `20` when added to `A_ext`.

## NEGATIVE CONTROLS

1. A function of an absolute group variable rather than relative elements must fail the common-left gauge lock and is inadmissible.
2. A non-symmetrized edge-labelled coefficient may fail full relabeling covariance and cannot be used for the invariant-subspace theorem.
3. Normal-coordinate singular coefficients are inadmissible in this gate; `h_n` must be smooth tangential functions only.

## PARALLEL LANES

### Lane A — provenance/source locks
Verify the Iter077L/M authority, actual `N=SU(2)^4` object, scaling-degree allowance for smooth tangential coefficients, and existence of at least one nonzero `F_SU2` boundary functional.

### Lane B — exact symmetry theorem
Verify symbolically/combinatorially that `Q` is common-left invariant and invariant under all `5!` vertex relabelings.

### Lane C — exact nonconstancy / infinite-family theorem
Derive exactly `Q(t)=12+8 cos(t)` on the frozen one-parameter compact path. Use the theorem that powers of a nonconstant continuous function whose image contains an interval are linearly independent as functions. Record an exact finite Vandermonde check at frozen distinct rational/cyclotomic controls only as an independent control, not as the proof of infinite dimension.

### Lane D — adversarial distributional/scope audit
Check that multiplying the nonzero true boundary functional by `Q^n` preserves support, source ordering, fixed causal labels, linearity in `Psi`, common-left gauge symmetry and relabeling covariance; search for any already-published source condition that forces all nonconstant tangential coefficients to vanish. Do not introduce new RG, finite-part or normalization rules.

## PASS

PASS iff all lanes establish that there exists a countably infinite linearly independent family

`{ Q^n F_SU2 delta_N : n>=0 }`

inside the source-compatible same-scaling-degree supported ambiguity space for at least one actual nonzero boundary functional, with all frozen source symmetries preserved.

Classification target:

`ITER077Q_SM_SOURCE_COMPATIBLE_K5_EXTENSION_AMBIGUITY_CONTAINS_INFINITE_DIMENSIONAL_TANGENTIAL_SUBSPACE_EXACT_THEOREM_SCOPED`.

## FAIL

FAIL iff a frozen source-backed condition already present before this gate forces `h` to be constant (or otherwise reduces the displayed invariant family to a finite-dimensional space), or the exact `Q` family fails one of the frozen gauge/relabeling/source-order/boundary locks.

## BLOCKED

BLOCKED if the Iter077L theorem does not actually permit smooth coefficient data along `N`, or no nonzero true boundary compact functional is available in repository authority.

## INVALID

INVALID for wrong source object, surrogate replacement, post-hoc change of `Q`, use of partial nonterminal Actions evidence, source-lock conflict, or any new physical selector introduced after seeing the result.

## INTERPRETATION CEILING

A PASS proves only an infinite-dimensional **mathematical/source-compatible local extension ambiguity** under the constraints already present in CRQN v0.2. It does not prove that no future independently motivated renormalization/composition/covariance principle can reduce this freedom, does not prove full vertex nonexistence/divergence, and does not establish generic-spin behavior, regulator independence, RG closure, G3, F9/G8/K5 promotion, new physics or complete quantum gravity.

A PASS would mean that treating Iter077M's constant `c` as the whole local ambiguity is scientifically insufficient: a predictive continuation must supply a new prospectively motivated selector/theory-space restriction strong enough to control tangential coefficient functions, not merely fit one scalar counterterm.