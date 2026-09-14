# Iter080J-SM preregistration — independently motivated microlocal WF-only selector power

Date: 2026-09-14

## Why this gate is admissible before seeing its result

This gate does **not** invent CRQN v0.3 and does not add a post-hoc selector to rescue CRQN v0.2. The candidate principle is independently motivated by:

1. the repository's pre-existing Iter029 exact microlocal cycle/wavefront audit (`results/ITER029_MICROLOCAL_CYCLE_WAVEFRONT_AUDIT.md`), which used the standard Hörmander wavefront/transversality criterion before Iter077Q existed;
2. Brunetti--Fredenhagen, *Microlocal Analysis and Interacting Quantum Field Theories: Renormalization on Physical Backgrounds*, Commun. Math. Phys. 208 (2000), arXiv:math-ph/9903028, which develops extension/renormalization methods using microlocal analysis and scaling degree;
3. N. V. Dang, *The extension of distributions on manifolds, a microlocal approach*, Ann. Henri Poincaré 17 (2016), arXiv:1412.2808, which studies extension across a closed embedded submanifold with explicit microlocal control of the extension wavefront set.

Thus `WF/conormal admissibility` is a mathematically standard, pre-test candidate restriction on distributional extensions. This prereg freezes the question of its **selection power** on the already authoritative Iter077Q ambiguity; it is not introduced because a desired numerical answer was observed.

## Frozen authority

- `status/CURRENT.md` newest main at prereg time.
- `results/ITER077Q_SM_INVARIANT_TANGENTIAL_AMBIGUITY_RESULT.md`, blob SHA `26aa90965ccfe495f55df2f4c190f7bbe09093f4`.
- Iter077Q authoritative run `34792482045`, aggregate artifact `10328598487`, digest `sha256:58e3cb389a985838942a4d0181e6e680cdd75480cfc24e0ec7bb07d73b199a96`.
- External theorem sources frozen above: arXiv:math-ph/9903028 and arXiv:1412.2808.

## Frozen object

Iter077Q gives the common-collision embedded submanifold

`N = SU(2)^4 subset SL(2,C)^4`

and an actual nonzero smooth tangential boundary coefficient `F(y)=F_SU2(y;Psi_0)` together with the countably linearly independent supported family

`u_n = Q(y)^n F(y) delta_N`,  n = 0,1,2,...,

where `Q` is smooth/real analytic, source common-left invariant, S5 invariant, nonconstant, and `Q(t)=12+8 cos(t)` on the frozen path.

## Frozen candidate selector class M_WF

`M_WF` means **wavefront/conormal admissibility alone**:

- an allowed supported ambiguity `u` must satisfy `supp(u) subset N`;
- `WF(u) subset N^*N \ 0` (the conormal bundle with zero section removed);
- no additional coefficient equation, differential equation, spectral recurrence, normalization functional, RG/cylindrical law, analyticity boundary-value prescription, positivity condition, or many-vertex composition law is silently included.

A transverse scaling-degree upper bound may be reported as a compatibility control because Iter077Q already freezes it, but the scientific classification of this gate must not depend on a new scaling-degree assumption.

## Frozen mathematical implication to test

Use the standard microlocal facts:

1. `WF(delta_N) = N^*N \ 0` for a smooth embedded submanifold `N` (locally the delta distribution in normal coordinates);
2. for smooth `f`, `WF(f u) subset WF(u)`.

Therefore, if every Iter077Q coefficient `f_n=Q^n F` is smooth on `N`, then

`WF(f_n delta_N) subset N^*N \ 0`

for every `n`.

Because Iter077Q independently proves `{u_n}` linearly independent, `M_WF` cannot select a unique extension if the theorem hypotheses and provenance checks are valid.

## Frozen lanes

### Lane A — provenance

PASS iff the checked-out Iter077Q result has blob SHA exactly `26aa90965ccfe495f55df2f4c190f7bbe09093f4` and contains the frozen objects `N=SU(2)^4`, `Q^n F delta_N`, smooth tangential multiplier statement, and the exact infinite-dimensional classification.

### Lane B — independent motivation/source lock

PASS iff all three pre-test motivation legs are present: repository Iter029 plus frozen Brunetti--Fredenhagen and Dang identifiers. This lane establishes motivation only; it does not infer a physical CRQN selector from QFT literature.

### Lane C — exact selector-power theorem

PASS iff the proof certificate verifies:

- `u_n=f_n delta_N` with smooth `f_n=Q^n F`;
- smooth multiplication cannot enlarge WF;
- `delta_N` is conormal;
- hence every `u_n` obeys `M_WF`;
- Iter077Q linear independence is imported only from its exact theorem/provenance, not inferred from a finite sample;
- therefore an infinite-dimensional subspace survives `M_WF`.

### Lane D — adversarial scope controls

PASS iff the implementation rejects all of these invalid promotions:

- `all microlocal selectors fail`;
- `all differential selectors fail`;
- `all spectral selectors fail`;
- `no future selector can work`;
- `CRQN v0.3 is defined`;
- `unique K5 extension obtained`;
- `NEW_PHYSICS_FOUND`;
- `G3 PASS` or `F9/G8/K5 promotion`.

A negative control representing `WF + an additional tangential coefficient equation` must be classified as **outside M_WF scope**, not as a counterexample to the theorem.

## Frozen outputs

If all lanes pass:

`ITER080J_SM_WAVEFRONT_CONORMAL_ADMISSIBILITY_ALONE_CANNOT_SELECT_ITER077Q_INFINITE_SMOOTH_TANGENTIAL_AMBIGUITY_EXACT_THEOREM_SCOPED`

Scientific verdict: `PASS_EXACT_SCOPED`.

If the theorem hypotheses fail but execution/provenance is valid:

`ITER080J_SM_WF_ONLY_SELECTOR_POWER_NOT_ESTABLISHED_SCIENTIFIC_FAIL_SCOPED`.

If provenance/source locks fail:

`INVALID_PROVENANCE`.

Infrastructure/numerical failures must remain distinct from scientific FAIL.

## Interpretation ceiling

Even on PASS, this gate rules out only `M_WF` as a **standalone unique selector**. It does not rule out a stronger microlocal principle involving a specific differential equation, boundary-value analyticity, spectral condition, positivity, composition/RG law, or function-valued constraint. It does not define a successor model. CRQN v0.2 remains blocked unless a separately prospectively motivated/source-derived selector is established.
