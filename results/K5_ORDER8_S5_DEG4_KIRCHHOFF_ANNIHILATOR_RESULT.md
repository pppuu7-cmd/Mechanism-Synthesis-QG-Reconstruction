# K5 S5-equivariant component-degree-four Kirchhoff annihilator — terminal result

Date: 2026-09-16

## Authority chain

Parent terminal results:

- invariant-dual projective object/reachability: `results/K5_ORDER8_INVARIANT_DUAL_PROJECTIVE_IBP_REACHABILITY_RESULT.md`, commit `e9ed372a91ac1bd219dc7671a916c70405e9cd43`;
- degree-two S5 logarithmic radial-only theorem: commit `ee965976e0af8f3b569407e917b0046f02b79649`;
- repaired degree-three S5 logarithmic radial-only theorem: `results/K5_ORDER8_S5_DEG3_FACE_TANGENT_LOG_IBP_SYZYGY_REPAIRED_RESULT.md`, commit `ed7a2aa05e0fa6bb75d63fa5328665059d0a012b`.

Prospective preregistration:

`prereg/K5_ORDER8_S5_DEG4_KIRCHHOFF_ANNIHILATOR.md`, commit `00b5ddf78474179281380606fbc3f62ca260e337`.

Implementation:

`scripts/k5_order8_s5_deg4_kirchhoff_annihilator.py`, commit `55cfdf27e616befaf39b5f3ec0d1c04d7e083669`.

Workflow/head:

`.github/workflows/k5_order8_s5_deg4_kirchhoff_annihilator.yml`, head `53bdd4d6adb5e470192292d7ef2616a57e15fc6e`.

## Production

- run `35043883583`, terminal `success`;
- job `104629427085`, terminal `success`;
- artifact `10426228492`;
- artifact ZIP digest `sha256:37f52650a70c11f7969302294b726e611ecc74a1adbf44889699daba788db5ca`;
- production JSON SHA256 `7fe9fb47da97a5c396c69d7153d8c25c4cef2f4b95c6f4cb1850cba889bffca4`;
- production summary materialized at `results/raw/k5_order8_s5_deg4_kirchhoff_annihilator_production_summary.json`, commit `2db15ad006b4e14e97e7ae0834d793ff8b387e50`;
- status `PASS_EXACT_SCOPED`;
- classification `K5_S5_DEG4_NONRADIAL_ANNIHILATOR_EXISTS_EXACT_SCOPED`.

All frozen structural checks and all adversarial controls passed. No invariant-dual period verdict was emitted.

## Exact complete degree-four module

Use all 220 homogeneous cubic monomials in ten edge variables.

The fixed-edge stabilizer in `S5` has order 12 and partitions these monomials into exactly 33 orbits. Their sizes are

`(3,6,1,12,6,12,6,12,6,6,6,12,12,2,6,3,6,6,12,12,12,6,3,3,12,6,6,6,3,6,3,6,1)`.

Transporting these fixed-edge orbits to all ten edge components gives the complete regular face-tangent S5-equivariant component-degree-four vector-field space.

The complete S5-invariant cubic logarithmic quotient space has dimension seven, with global orbit sizes

`(10,60,10,20,60,30,30)`.

The exact polynomial coefficient system for

`sum_e v_e d_e Psi_K5 = H_3 Psi_K5`

has

- `7180` rows;
- `40 = 33 + 7` columns;
- exact rank `32`;
- exact nullity `8`.

The full invariant-cubic polynomial-Euler subspace `F_3(alpha) E` has exact dimension `7` and lies inside the logarithmic nullspace. Therefore the exact non-radial quotient dimension is

`8 - 7 = 1`.

Thus component degree four is the first established S5-equivariant regular face-tangent degree in this chain with a genuinely non-radial logarithmic class.

## Exact zero-quotient annihilator

Independently setting all logarithmic-quotient coordinates to zero gives the vector-only matrix. It has exact rank `32` on the 33 vector coefficients and therefore a one-dimensional kernel.

Hence the unique non-radial quotient can be represented by a genuine Kirchhoff annihilator

`v(Psi_K5)=0`.

A deterministic primitive integer representative in the frozen 33-dimensional fixed-edge-orbit basis is

`(0,0,0,0,3,3,0,0,0,0,0,3,0,3,-1,-1,0,-1,-3,-1,0,-3,0,5,-1,-1,0,-1,0,-1,0,0,0)`.

Its nonzero coefficients occur at orbit indices

`4:+3, 5:+3, 11:+3, 13:+3, 14:-1, 15:-1, 17:-1, 18:-3, 19:-1, 21:-3, 23:+5, 24:-1, 25:-1, 27:-1, 29:-1`.

The validator substitutes the complete representative back into the full polynomial identity coefficient-by-coefficient and obtains exact zero. It also proves the representative lies outside the seven-dimensional radial Euler span.

## Adversarial controls

The same decision path rejects:

- an explicit non-face-tangent field;
- an explicit face-tangent but S5-breaking field;
- a fake logarithmic relation;
- a fake annihilator.

The synthetic fixture `Psi_syn=prod_e alpha_e` is sent through the same engine. It gives

- system `220 x 40`;
- exact rank `7`;
- nullity `33`;
- radial dimension `7`;
- non-radial quotient dimension `26`;
- annihilator dimension `26`.

The known synthetic annihilator

`Q_e = 9 alpha_e^3 - sum_(f != e) alpha_f^3`, `v_e=alpha_e Q_e`

is verified exactly. This demonstrates that the annihilator branch is genuinely reachable and not hard-coded.

## Scientific meaning

The exact K5 Kirchhoff denominator admits a unique S5-equivariant non-radial regular face-tangent logarithmic class at component degree four, and that class can be chosen to annihilate the denominator exactly.

This is a structural denominator-preserving projective-IBP direction. It is not yet a relation between the two physical invariant-dual periods, because the actual degree-27 numerators have not yet been materialized as reusable exact coefficient objects and because the projective `(n-2)`-form/boundary terms still have to be treated correctly.

The outcome-independent object audit `sources/K5_INVARIANT_DUAL_DEG27_NUMERATOR_MATERIALIZATION_AUDIT.md`, commit `ecebc3670c63fe877e2ec5eddd84bc36252b3430`, identifies this exact next bottleneck.

## Authorized successor

Do not continue blind higher-degree logarithmic searches.

The highest-information successor is:

1. materialize both actual full-all-32 invariant-dual degree-27 numerator channels from the authoritative weighted-Laplacian/adjugate/Wick/source contraction;
2. reproduce the frozen uniform dual coordinates as an independent control;
3. construct the correct projective-form IBP action of the confirmed degree-four annihilator on each numerator, retaining `prod_e alpha_e^(1/2)`;
4. audit all Schwinger-simplex boundary terms explicitly;
5. classify whether the resulting exact relations are trivial, close on a finite numerator module, generate a reducible recurrence family, or yield a noncancellation/zero certificate for either invariant-dual period.

An independently preregistered Critic for this degree-four theorem already exists at `prereg/K5_ORDER8_S5_DEG4_KIRCHHOFF_ANNIHILATOR_INDEPENDENT_CRITIC.md`, commit `7cde5bd6838e40b7d10fe7dd9707f04cc3198662`, frozen while the Researcher run was still queued.

## Interpretation ceiling

No invariant-dual integrated period zero/nonzero theorem, no full 217-dimensional tensor/annihilator theorem, no reduction of the 377-dimensional supported-extension ambiguity, no physical finite-part selector, no regulator-independence theorem, no G3/F9/G8 promotion, no `NEW_PHYSICS_FOUND`, and no complete-QG claim follows from this result.
