# Iter083P-SM preregistration — actual source-ordered residue object definition

Date: 2026-09-15
Status: **PROSPECTIVELY FROZEN BEFORE SUBSTANTIVE SOURCE AUDIT / RESULT**

## HYPOTHESIS

The controlling post-Iter083N question is more primitive than computing a residue annihilator: the repository/source authority may or may not define a canonical **actual source-ordered meromorphic residue object** whose residue can be tested against the remaining normal-jet freedom. This gate tests object definition before any residue algebra is promoted.

## exact OBJECT

Frozen target object:

`A_-1^SOURCE(K3/K4/K5; boundary component)`

meaning the residue at the first meromorphic pole of a source-authorized analytic family constructed from the **actual source-ordered causal/Toller object** in the frozen all-`j=1/2` sector, with ordering

`one-wedge spectral/spinor integration -> Toller function -> product of ten Toller matrices -> full boundary contraction -> K5 group integration / distributional extension`.

For this gate an object counts as defined only if repository authority supplies, or derives without changing source order, all of:

1. the analytic/meromorphic deformation parameter and deformed full source object;
2. the exact map from source Toller/group variables to that deformation;
3. the full boundary contraction on all 32 all-spin-half components or an exact theorem reducing it;
4. actual Haar/group measure and normalization conventions;
5. branch/sign and published spectral prescription compatibility;
6. a theorem that the deformed full K5 object is defined off the collision and admits the relevant Laurent expansion near the collision stratum;
7. a unique identification of the coefficient called `A_-1` independent of an auxiliary scalar/Hodge/Q surrogate or an unauthorized exchange of source ordering.

## DEPENDENCY

This is the immediate object-definition dependency required before `ACTUAL_SOURCE_ORDERED_RESIDUE_NORMAL_JET_ANNIHILATOR_GATE` can perform substantive residue calculations. It tests the arrow

`confirmed Iter083N universal finite-part theorem -> actual physical residue object`.

If this arrow is absent, no annihilator verdict may be inferred from the universal supported-residue space.

## SOURCE AUTHORITY

Frozen repository authority at prereg time:

- `status/CURRENT.md` at main `b0eaa4da04b186f9976b7aa1b78fbc15619ca46e`;
- `status/MSQGR_ADVERSARIAL_CRITIC_HANDOFF.md`, Iter083N `CONFIRMED_SCOPED`;
- repaired Iter083M controlling authority;
- provenance-correct Iter083N retry and its Critic review;
- Iter083L source-authority audit;
- Iter083E/F one-wedge Toller/Feynman source-order audits;
- Iter077I repaired source-order authority and `status/ITER077_CONTACT_FORMULA_ERRATUM.md`.

No external web/source material may be introduced in this gate. GitHub repository authority is the only source of truth.

## FROZEN INPUTS

- candidate `CRQN v0.2` unchanged;
- frozen all-`j=1/2` common-K5-collision sector;
- true K5 incidence/source map only;
- all ten wedges;
- all 32 all-spin-half boundary components unless an already-authoritative exact reduction exists;
- actual source measure/normalization/branch conventions/published one-wedge spectral `i epsilon`;
- no new boundary state;
- no fitted subtraction scale or finite part;
- no auxiliary ten-edge Q as physical source object;
- no scalar K4/K5/Hodge surrogate;
- no termwise `theta/delta/delta' -> product -> pullback` substitution;
- no exchange of one-wedge source integration with K5 product/group integration without theorem;
- no use of Iter083N's formal `rho^z` family as physical source authority unless an existing repository bridge explicitly derives it from the source object.

## POSITIVE CONTROLS

A source/object-definition PASS requires exact repository citations for every item 1-7 in `exact OBJECT`, including the full-order bridge from published/source-defined Toller data to a meromorphic K5 family and Laurent residue.

The audit must separately identify one-wedge analytic/spectral formulas, full ten-wedge product/boundary contraction formulas, group measure, and any extension/meromorphic-family theorem; mere coexistence of these ingredients is not a bridge theorem.

## NEGATIVE CONTROLS

The gate must reject as insufficient:

1. treating the one-wedge Feynman `i epsilon` as the K5 meromorphic residue parameter;
2. treating Iter083N's formal local `rho^z u` family as already source-authorized;
3. inferring a full K5 residue from a representative scalar/component;
4. using auxiliary Q, Hodge/cycle incidence, or scalar K4/K5 controls as the physical source family;
5. termwise multiplication/pullback of contact distributions in place of source ordering;
6. choosing a finite part, defining function, subtraction scale, boundary state, or regulator post hoc;
7. declaring object existence merely because a generic distribution-extension theorem could in principle construct some extension.

## PASS

`PASS_OBJECT_DEFINED_SCOPED` only if repository authority defines the exact actual source-ordered meromorphic family and residue coefficient `A_-1^SOURCE` with all frozen requirements above, without new physical assumptions.

A PASS does **not** mean the residue is nonzero, maximal-order, jet-sensitive, unique as a finite part, or sufficient to select the K5 amplitude. It only unlocks a subsequent actual-residue annihilator computation.

## FAIL

`FAIL_EXACT_SCOPED` only if an already-defined actual source-ordered residue object exists and an exact source-authority contradiction proves that it cannot satisfy the required source ordering/covariance/composition or that its definition is internally inconsistent. Absence of the defining bridge is not FAIL.

## BLOCKED

`BLOCKED_OBJECT_DEFINITION` if any indispensable ingredient 1-7 is absent, only surrogate-defined, only one-wedge-defined, only formal/generic rather than source-derived, or would require an unauthorized ordering exchange/new normalization law.

This is the default classification for a missing physical bridge; no surrogate may be invented to avoid it.

## INVALID

`INVALID_IMPLEMENTATION` for incomplete corpus coverage, stale authority, wrong source version/sign/normalization/branch transcription, unexecuted negative controls, or provenance defects.

## INTERPRETATION CEILING

Even a PASS cannot promote F9/G3, unique K5 extension, regulator independence, global multistratum patching, causal composition, RG, continuum, spin-2, GR, matter/QFT or predictions. A BLOCKED result establishes only that the current repository authority does not define the actual meromorphic residue object needed by the Iter083N successor calculation; it is not a theorem that no such source-faithful construction exists in principle.
