# Iter083G provenance ledger

**Date:** 2026-09-15

## Scientific contract

Iter083G tests only whether exact K5 vertex-relabeling symmetry `S5` uniquely determines the positive quadratic form `Q` on the ten-edge regulator-parameter space used by a Dang-Zhang-style multivariate holomorphic-projection class. It is a candidate mathematical renormalization framework, not Lorentzian K5 source authority and not a physical selector.

Prospective scientific preregistration:

- `prereg/ITER083G_SM_MULTIVARIATE_REGULATOR_METRIC_S5_NONUNIQUENESS.md`
- commit `e1312b7c59641e53f978130a506d0f4a3dd0bd1d`.

Initial framework/source lock:

- `sources/ITER083G_MULTIVARIATE_RENORMALIZATION_Q_SOURCE_LOCK.md`
- commit `2218aa4af96767854e58fb2091c666041d44ac6a`.

Validator:

- `scripts/iter083g_s5_regulator_metric_nonuniqueness.py`
- commit `ba67d16d4f3b0c49083630bde2231aa998dc2386`.

Workflow / first production head:

- `.github/workflows/iter083g_s5_regulator_metric_nonuniqueness.yml`
- commit `78c1b9f7dda47f2cf6f7436aa2c1b49cf32aa2f3`.

## First production attempt

Run `34915017574`, job `104210672296`, terminal `failure`.

The mathematical predicates had already produced the frozen three-sector result and the explicit positive non-proportional metrics. The failure was the P6 source-authority lexical guard: the source-lock document already said that the framework was not MSQGR physical authority, but the validator required a particular literal lowercase phrase. No artifact was produced for this failed run.

This run is retained as a non-authoritative implementation/control failure. It must not be rewritten as a scientific FAIL.

## Wording-only repair

Commit `fb8920529777129cc6ac32ecf65c5cd8727ffc80` changed only the source-lock wording so the existing semantic authority ceiling matched the frozen lexical validator. It did not change:

- the hypothesis;
- the ten-edge `S5` representation;
- the invariant-form equations;
- the expected dimension;
- `Q1`, `Q2`, or positivity criteria;
- PASS/FAIL/BLOCKED criteria;
- the interpretation ceiling.

Because the same substantive source-authority limitation was already present before the first run, this repair is treated as control-only wording alignment, not outcome-dependent scientific redefinition.

## Authoritative repaired production

Head `fb8920529777129cc6ac32ecf65c5cd8727ffc80`.

- run `34915066408`, terminal `success`;
- job `104210816198`, terminal `success`;
- artifact `10375064212`, name `iter083g-s5-regulator-metric-nonuniqueness`;
- artifact ZIP digest `sha256:5500b76dbe73b8ae88cfa6a0f33d855396d968d2260273f4ee577902c5ecfbef`;
- production JSON SHA256 `29d0d849746e33641c363cfeea6826af5c5dd85774648ebb6ccc53ee6872ce00`.

Durable Researcher result:

- `results/ITER083G_SM_S5_REGULATOR_METRIC_NONUNIQUENESS_RESULT.md`;
- commit `f36977255fd1695860b11f49245e5f7a15c51e58`;
- Researcher classification `ITER083G_SM_S5_INVARIANT_TEN_EDGE_REGULATOR_METRIC_HAS_THREE_SECTORS_SO_Q_BASED_MULTIVARIATE_PROJECTION_NOT_SYMMETRY_UNIQUE_SCOPED`;
- Researcher verdict `PASS_EXACT_SCOPED`.

Independent adversarial review:

- `results/ITER083G_ADVERSARIAL_REVIEW.md`;
- commit `1d4e5984710ba88a50fbbfcb606c6a9687c25e39`;
- Critic verdict `CONFIRMED_SCOPED`.

## Exact verified scoped fact

For the ten unordered K5 edges, symmetric `S5`-invariant forms have exactly three orbit sectors: same edge, adjacent distinct edges, and disjoint edges, with orbit sizes `10,30,15`. Hence

`dim_R Sym^2((R^10)^*)^S5 = 3`.

Equivalently the edge permutation representation decomposes as

`R^10 = [5] + [4,1] + [3,2]`.

The explicit positive metrics

`Q1 = I`,

`Q2 = I + (1/10) A_L(K5)`

are both `S5` invariant and are not proportional; `Q2` has exact sector eigenvalues `(8/5, 11/10, 4/5)`. Therefore `S5` relabeling symmetry alone does not uniquely determine `Q`, even modulo overall scale.

## Preserved loopholes / ceiling

Iter083G does not prove that two allowed `Q` choices yield different renormalized K5 amplitudes. The actual source-faithful K5 polar/meromorphic germ might lie in a `Q`-independent subspace.

Iter083G also does not test whether stronger source-derived locality, factorization, forest restriction, deletion/contraction, gluing, or multivertex functoriality imposes additional orthogonality conditions that reduce or fix the three-sector positive cone.

The Dang-Zhang framework is external mathematical motivation only. Its Euclidean analytic-continuation theorem is not automatically a theorem for the Lorentzian Toller K5 source object.

No unique K5 extension, physical finite-part selector, actual regulator-dependence theorem, regulator independence, generic-spin theorem, causal E3/E4/E6 closure, G3/F9/G8/K5 promotion, `NEW_PHYSICS_FOUND`, or complete-QG claim follows.

`status/ITER077_CONTACT_FORMULA_ERRATUM.md`, blob `63356e5099929f2b21d9d7296ab97f15ff163dba`, remains controlling and historical source-lock-invalid Iter077E/F siblings remain quarantined.