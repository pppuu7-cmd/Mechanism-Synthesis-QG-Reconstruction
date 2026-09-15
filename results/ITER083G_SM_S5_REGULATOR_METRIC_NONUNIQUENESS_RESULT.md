# Iter083G-SM — S5 symmetry does not uniquely fix the ten-edge multivariate regulator metric

Date: 2026-09-15
Status: **PASS_EXACT_SCOPED**

## Prospective provenance

- preregistration: `prereg/ITER083G_SM_MULTIVARIATE_REGULATOR_METRIC_S5_NONUNIQUENESS.md`, commit `e1312b7c59641e53f978130a506d0f4a3dd0bd1d`;
- framework/source lock: `sources/ITER083G_MULTIVARIATE_RENORMALIZATION_Q_SOURCE_LOCK.md`, initial commit `2218aa4af96767854e58fb2091c666041d44ac6a`, wording-only repair commit `fb8920529777129cc6ac32ecf65c5cd8727ffc80`;
- validator: `scripts/iter083g_s5_regulator_metric_nonuniqueness.py`, commit `ba67d16d4f3b0c49083630bde2231aa998dc2386`;
- workflow: `.github/workflows/iter083g_s5_regulator_metric_nonuniqueness.yml`, commit `78c1b9f7dda47f2cf6f7436aa2c1b49cf32aa2f3`.

The first production run `34915017574` failed only P6 because the validator required a literal lowercase source-authority phrase absent from the manifest. All mathematical predicates P1–P5, P7 and their controls already passed. Commit `fb892052...` added only the exact wording to the manifest; no preregistered scientific criterion, matrix, representation, expected dimension, or control changed.

Authoritative repaired production:

- head `fb8920529777129cc6ac32ecf65c5cd8727ffc80`;
- run `34915066408`, terminal success;
- job `104210816198`, terminal success;
- artifact `10375064212`, `iter083g-s5-regulator-metric-nonuniqueness`;
- artifact ZIP digest `sha256:5500b76dbe73b8ae88cfa6a0f33d855396d968d2260273f4ee577902c5ecfbef`;
- production JSON SHA256 `29d0d849746e33641c363cfeea6826af5c5dd85774648ebb6ccc53ee6872ce00`.

## Classification

`ITER083G_SM_S5_INVARIANT_TEN_EDGE_REGULATOR_METRIC_HAS_THREE_SECTORS_SO_Q_BASED_MULTIVARIATE_PROJECTION_NOT_SYMMETRY_UNIQUE_SCOPED`

Verdict: **`PASS_EXACT_SCOPED`**.

## Mathematical framework being tested

Dang–Zhang construct multivariate analytic renormalization by a projection `pi_p` from meromorphic germs with linear poles to holomorphic germs followed by evaluation. Their Remark 6.8 states that the projection is determined by the polar-germ subspace, which in turn is determined by the quadratic form `Q` fixed on regulator-parameter space.

This is used here only as a candidate mathematical repair class. It is not source authority for the Lorentzian K5 amplitude.

## Ten-edge regulator representation

Attach one regulator parameter to each unordered K5 edge. The real parameter space is

`E = R^10`.

S5 acts by vertex relabeling and hence by permutation of the ten edges.

Production enumerated all 120 permutations and obtained a faithful complete ten-edge action.

The character on cycle classes

`(1^5), (2,1^3), (2^2,1), (3,1^2), (3,2), (4,1), (5)`

is

`chi_E = (10,4,2,1,1,0,0)`.

Subtracting the trivial representation and the standard representation gives

`(5,1,1,-1,1,-1,0)`,

whose exact class inner product has norm one and is orthogonal to the first two pieces. Thus

`E = [5] + [4,1] + [3,2]`

with dimensions

`10 = 1 + 4 + 5`.

## Exact S5-invariant symmetric forms

A symmetric 10x10 matrix has 55 independent entries. The invariance equations

`P_sigma^T Q P_sigma = Q`

for all 120 permutations identify entries precisely along the three S5 orbits of unordered edge pairs:

1. the same edge;
2. two distinct adjacent edges;
3. two disjoint edges.

The orbit sizes are

`10, 30, 15`

respectively. Equivalently the exact constraint rank is

`55 - 3 = 52`.

Therefore

`dim_R Sym^2(E*)^S5 = 3`.

An explicit invariant basis is

- `I`, the identity;
- `A`, the adjacency matrix of the line graph `L(K5)` (two edges share one vertex);
- `B`, the disjointness matrix, `B=J-I-A`.

Hence every S5-invariant symmetric regulator metric has the form

`Q = a I + b A + c B`.

## Exact irreducible eigen-sectors

The line-graph adjacency eigenvalues are

- `6` on `[5]`;
- `1` on `[4,1]`;
- `-2` on `[3,2]`.

The disjointness eigenvalues are

- `3` on `[5]`;
- `-2` on `[4,1]`;
- `1` on `[3,2]`.

Therefore the three eigenvalues of general invariant `Q` are

`lambda_[5]   = a + 6b + 3c`,

`lambda_[4,1] = a + b - 2c`,

`lambda_[3,2] = a - 2b + c`.

Positive definiteness is exactly the conjunction that all three are positive.

## Explicit inequivalent positive metrics

Take

`Q1 = I`,

`Q2 = I + (1/10) A`.

Production verifies exact eigenvalues of `Q2`:

`(8/5, 11/10, 4/5)`

on `[5]`, `[4,1]`, `[3,2]` respectively.

All are positive, so `Q2` is positive definite. Since its three eigenvalues are unequal, `Q2` is not a scalar multiple of `Q1`.

Thus exact S5 covariance does not select a unique positive regulator metric even modulo an overall scale. The positive invariant cone has three sector parameters, or two independent shape parameters after quotienting by common scale.

## Consequence for Q-based multivariate holomorphic projection

For the Dang–Zhang-style class, the holomorphic projection depends on the regulator-space quadratic form used to define the polar complement. Since the currently validated K5 source/symmetry data do not select a unique invariant `Q`, they do not by themselves select a unique member of this Q-based projection family.

Choosing the Euclidean `Q=I` is mathematically natural and is the convention used in the cited construction, but in the present MSQGR source scope it is an extra renormalization-scheme convention rather than a consequence of K5 S5 symmetry.

## Relation to the exact 377-dimensional ambiguity

Iter083B proves that every pair of admissible same-off-collision, same-source-symmetry, same-scaling-degree common-collision extensions differs by an element of

`F_8`, `dim_C F_8 = 377`.

Therefore, **if** two Q-based schemes produce different admissible K5 extensions, their difference is automatically a vector in the already classified 377-dimensional affine ambiguity space.

This statement is one-way. Iter083G does **not** prove that varying Q produces a nonzero vector in F8. The actual K5 meromorphic germ might lie in a subspace on which all admissible Q-projections agree.

That possibility is the next required falsifier.

## Production controls

All P0–P7 and all eight controls passed in authoritative run `34915066408`.

The gate explicitly rejects:

- preferred edge labels;
- the false claim that S5-invariant Q is unique up to scale;
- identifying three Q-sectors with three physical counterterms;
- using `dim F8=377` as evidence that Q-dependence is nonzero;
- treating the external Euclidean renormalization theorem as Lorentzian spinfoam source authority;
- reinterpreting the one-wedge spectral epsilon as Q;
- excluding future source laws that could fix Q or bypass this scheme.

## Exact research consequence

A generic statement of the form

`use multivariate analytic minimal subtraction and impose S5, therefore the K5 extension is canonical`

is not justified.

The next nonredundant calculation must act on the **actual or a source-faithful leading K5 multivariate meromorphic germ** and test projection independence across at least two inequivalent positive S5-invariant choices such as `Q1` and `Q2`.

A Q-independent result would be a genuine positive simplification. A Q-dependent result would explicitly locate renormalization-scheme freedom inside F8.

## Interpretation ceiling

No claim of actual Q-dependence of the physical K5 amplitude; no generic-spin theorem; no all-strata global renormalization theorem; no causal-vertex distributional nonexistence theorem; no regulator independence; no unique-extension impossibility against future physical laws; no G3/F9/G8/K5 promotion; no NEW_PHYSICS_FOUND; no complete-QG claim.