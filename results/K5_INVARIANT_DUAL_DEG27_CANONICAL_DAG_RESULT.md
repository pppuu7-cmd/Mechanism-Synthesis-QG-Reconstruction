# K5 invariant-dual degree-27 canonical numerator DAG — terminal result

Date: 2026-09-16

## Authority

Parent full-all-32 projective-object authority:

`results/K5_ORDER8_INVARIANT_DUAL_PROJECTIVE_IBP_REACHABILITY_RESULT.md`, commit `e9ed372a91ac1bd219dc7671a916c70405e9cd43`.

Outcome-independent object audit:

`sources/K5_INVARIANT_DUAL_DEG27_NUMERATOR_MATERIALIZATION_AUDIT.md`, commit `ecebc3670c63fe877e2ec5eddd84bc36252b3430`.

Prospective preregistration:

`prereg/K5_INVARIANT_DUAL_DEG27_CANONICAL_DAG_MATERIALIZATION.md`, commit `faa436e10301ecb92f2e4558411f0d1af6f4594f`.

Exact implementation:

`scripts/k5_invariant_dual_deg27_canonical_dag.py`, commit `ce6aa550f706c1f1980787b9e6ab455e9749b5f6`.

Workflow/head:

`.github/workflows/k5_invariant_dual_deg27_canonical_dag.yml`, head `d094ee6204845592ac395a67b94501461e98e4ff`.

## Production

- run `35044686796`, terminal `success`;
- job `104631868911`, terminal `success`;
- artifact `10426617568`;
- artifact ZIP digest `sha256:6da2c3346b14aaa2d8d3dd342f6305dcf4896391a3f4ac9153ed86d1dc1b1b45`;
- production JSON SHA256 `47eaa12719abb2a0ce8a090374e759b62678041d468b11e77f242c64e869d331`;
- canonical DAG SHA256 `f8eaaa5c7923497a67f0354a2d59475f4b6d82022e032fc005c1d9d2add69992`;
- production summary `results/raw/k5_invariant_dual_deg27_canonical_dag_production_summary.json`, commit `46386f64ce54c7c76957ba4d659950455c07e3ed`;
- status `PASS_EXACT_SCOPED`;
- classification `K5_INVARIANT_DUAL_DEG27_CANONICAL_DAG_MATERIALIZED_EXACT_SCOPED`.

All frozen exact checks and all eight malformed controls passed.

## Exact reusable numerator object

The two physical invariant-dual numerator channels are now represented by a deterministic exact polynomial DAG, not merely by a structural symbol `N_c` or one-point value.

The DAG fixes:

- the ten-edge order and reduced incidence rows;
- the 125-term coefficient-one K5 Kirchhoff polynomial `Psi_K5`;
- the complete polynomial adjugate of the reduced weighted Laplacian;
- all edge-pair covariance numerator polynomials;
- the source radius matrix `Q=L_uniform/5`;
- the authoritative leading source matrix-entry coefficients;
- the full 32D boundary S5 action and exact dual/covector Reynolds data;
- inverse-series recursion for `(L+sQ)^(-1)` through order four;
- determinant-ratio series through order four;
- the exact ten-factor source Wick recursion;
- the order-eight rule `J_4=4! [s^4](...)`;
- the exact numerator clearing rule `N_c=Psi^9 J_{4,c}`.

The algebraic derivation `sources/K5_DEG27_CANONICAL_POLYNOMIAL_DAG_DERIVATION.md`, commit `18944fdeb1ceef08f2920ad90cf2a3d6104203d8`, proves term-by-term that this DAG is an exact homogeneous degree-27 polynomial representation.

## Exact validation controls

### Full source / dual object

The production retains:

- all 32 boundary components;
- exactly `100000` source node-choice terms;
- boundary character `(32,0,8,2,0,0,2)`;
- Reynolds rank two;
- dual RREF pivots `(1,4)`;
- dual projection distinct from vector projection in the stripped basis.

### Uniform point

The new generic evaluator reproduces the previously validated full all-32 boundary vector exactly.

Invariant-dual coordinates are exactly

`(-9225216/9765625, -7175168/9765625)`.

The corresponding exact numerator values are

`N_1(1,...,1)=-7038281250000000000`,

`N_2(1,...,1)=-5474218750000000000`.

### Two independent nonuniform controls

At

`edge01_2=(2,1,1,1,1,1,1,1,1,1)`,

the new all-32 evaluator's `00000` component equals the independent legacy nonuniform evaluator exactly:

`70286827392/9191328125`.

At

`mixed_small=(1,2,1,3,1,2,1,1,2,1)`,

the same independent equality holds:

`3287903397106539/7710244864000000`.

The direct rational evaluator and canonical-DAG evaluator agree exactly on the complete boundary vector at all three frozen points.

### Degree-27 homogeneity

Under the prospectively frozen control rescaling `alpha -> 2 alpha` at `edge01_2`, both numerator channels scale exactly by `2^27`.

Thus the reusable object has the correct homogeneous degree 27.

## Scientific meaning

The previous object-definition bottleneck is closed: the confirmed degree-four K5 Kirchhoff annihilator can now act on the two **actual full-all-32 invariant-dual source numerators** without substituting a representative boundary component or arbitrary polynomial.

This is still not an integrated-period theorem. No value, sign, zero, or nonzero verdict has been assigned to either 9D projective period.

## Authorized successor

The highest-information successor is the already-derived annihilator action on both exact numerator DAGs.

Using `sources/K5_DEG4_ANNIHILATOR_PROJECTIVE_GAUGE_ACTION_DERIVATION.md`, define

`B_v[N]=s1 v(N)+{s1[div v +(1/2)sum_i q_i]-3S}N`,

where `v_i=alpha_i q_i`, `S=sum_i v_i`, `s1=sum_i alpha_i`, and the confirmed structural theorem gives `v(Psi_K5)=0`.

A prospective successor should first determine exactly whether `B_v[N_1]` and `B_v[N_2]` are zero/nonzero and whether the action closes on the two-dimensional physical numerator span with constant coefficients. This is useful even before global Stokes authority: a single exact nonzero witness disproves algebraic annihilation, and a frozen out-of-sample exact point can falsify constant 2x2 closure.

Only after that algebraic action is known should the separate higher-codimension Schwinger-corner boundary audit decide whether the total derivative may be integrated to zero globally.

## Interpretation ceiling

No invariant-dual integrated-period zero/nonzero theorem, no full 217-dimensional tensor theorem, no reduction of `dim_C F_8=377`, no physical finite-part selector, no regulator-independence theorem, no G3/F9/G8 promotion, no `NEW_PHYSICS_FOUND`, and no complete-QG claim follows.
