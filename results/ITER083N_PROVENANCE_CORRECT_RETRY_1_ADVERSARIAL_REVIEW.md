# Iter083N provenance-correct retry 1 — independent adversarial review

Date: 2026-09-15

## Reviewed authority

Reviewed Researcher result: `results/ITER083N_PROVENANCE_CORRECT_RETRY_1_RESULT.md`, commit `7e194bd7d6e074e03f4393a6357d06824aedc745`.

Frozen chain:

- parent scientific prereg `c29ba0ddbaa4d6e1581db558b792565a7916a0cd`;
- source lock `cf9d17cc8dae087f2c59ff0adb9f8aeff8ef7533`;
- theorem derivation `70a756c9c7c66f822d0e5933e9522b2d359dafe8`;
- repaired Iter083M controlling Critic authority `e7623cb5303ea49894e480e2fc4a884df44e7713`;
- fresh retry prereg `d9edb0fd2a5c522ddec021f2b4f8e1a964ee3d96`;
- first retry run `34925091322` permanently `INVALID_IMPLEMENTATION`;
- prospective control-only repair prereg `74ec4edd547d07503e70a0a972a500df70c7c60a`;
- repaired validator / production head `15472a83a6fc5e73c10b050649578822b65558cf`;
- authoritative run `34925157771`, job `104241540969`, terminal success;
- artifact `10379901560`, ZIP digest `sha256:ac44a7a209847a097902904bb7114ffafa40edc8d40d8f15324b0c66204f0384`;
- production JSON SHA256 `b5e1f14e728c1ee9342a5433084b6c1d122faad4af360ffbcd627f60a76cd9ec`.

Historical original Iter083N remains permanently `INVALID_PROVENANCE` under `fbff993fc920e707d0ff885b73549f3204d208c5` and is not rehabilitated.

## Contract / provenance audit

The fresh retry preregistration preserved the parent hypothesis, object, positive/negative controls, PASS/FAIL semantics and interpretation ceiling. The first retry failed only an authority-text implementation lock. The control-only repair was committed before the repaired validator and is an actual ancestor of production head `15472a83...`; compare state is `ahead_by=1` with only `scripts/iter083n_provenance_correct_retry.py` changed after the repair preregistration.

The authoritative workflow fetched full history, checked out exactly `15472a83a6fc5e73c10b050649578822b65558cf`, verified ancestry of the scientific prereg/source/theorem/controlling-Critic/retry commits, executed the repaired validator, obtained all P0-P7 and all controls true, hashed the exact JSON and uploaded the artifact. Artifact metadata independently reports the same head and ZIP digest. No post-hoc scientific threshold, residue order, boundary state, finite coefficient, scale or branch choice was introduced.

The workflow ancestry shell did not explicitly list the later control-repair prereg SHA `74ec4edd...`; however repository ancestry independently verifies that `74ec4edd...` is the direct base of production head `15472a83...`. This is not a provenance defect.

## Independent mathematical attack

The formal Laurent identity is exact for the frozen simple-pole family. For

`U_rho(z)=A_-1/z+A_0+O(z)` and `rho'=exp(phi)rho`,

`exp(z phi)=1+z phi+O(z^2)` gives

`Res_rho'=A_-1`,

`FP_rho' u-FP_rho u=phi A_-1`.

No Felder–Kazhdan applicability assumption is needed for this algebra.

The universal supported-jet threshold is also correct. If a distribution is supported on `N` with normal order at most `omega`, then `I_N^(omega+1)` annihilates it. Conversely, if the first nonzero normal Taylor term of `phi` has multi-degree `alpha` with `|alpha|=q<=omega`, the matching normal derivative `partial^alpha delta_N` gives a nonzero product. Therefore the sharp universal thresholds over the whole allowed supported-residue class are exactly K3 `I_N^1`, K4 `I_N^4`, K5 `I_N^9`.

The CI's 90 one-normal-coordinate identities are not by themselves a complete multidimensional proof, but the frozen derivation states the correct multi-index ideal-filtration theorem and the independent argument above closes that scope. Thus the one-dimensional executable control is a representative exact control, not a scalar-surrogate replacement of the theorem.

## Counterexample-first witness against the forbidden rescue

Take one normal coordinate `x_1` inside any positive-dimensional collision normal fiber and a local Morse–Bott radius

`rho=|x|^2`, `rho'=exp(x_1) rho`.

The two functions have the same quadratic Hessian on `N` because `phi=x_1` vanishes on `N`. Choose an allowed order-one supported residue

`A_-1=partial_(x_1) delta_N`.

Then

`phi A_-1 = x_1 partial_(x_1) delta_N = -delta_N != 0`.

So equal tangent quadratic geometry does **not** universally fix the finite part as soon as order-one residues are allowed. This directly defeats the strongest possible tangent-metric rescue for the frozen K4/K5 universal classes. For K3, where only order-zero residues are allowed, `phi|_N=0` does annihilate every residue, exactly as claimed.

Higher-degree sharpness follows similarly with `phi=x^alpha` and `A_-1=partial^alpha delta_N` for `|alpha|<=omega`.

## Scope attacks that survive as qualifications

1. The theorem is only for a **simple pole**. Higher-order meromorphic poles would produce additional powers of `phi` in finite-part transformations and require a new preregistered gate.
2. The theorem compares **conformally related** regularizers `rho'=exp(phi)rho`. Two arbitrary Morse–Bott functions with the same Hessian need not have a smooth conformal ratio across `N`; no arbitrary-same-Hessian equivalence theorem follows.
3. The thresholds are universal over the whole allowed supported-distribution space. They do not prove the actual source-ordered Toller residue reaches order 3 or 8, is nonzero, or couples to the unfixed jets.
4. The result is local to one collision stratum. It does not solve nested-forest compatibility, partition-of-unity patching, inter-stratum transport or composition/gluing.
5. No physical regularization prescription has been source-authorized. Published spectral `i epsilon` remains one-wedge source data and is not identified with `rho^z`.

## Source / ordering / boundary audit

The reviewed object is deliberately not a full source amplitude. It is a local formal meromorphic extension class applied after the source-ordered Toller object has been formed. Nothing in the gate exchanges spectral/spinor integration with termwise `theta/delta/delta'` products, and no scalar K4/K5 incidence object is substituted for a true source Jacobian.

No representative boundary state is selected. The normal-order ceilings are inherited from the frozen all-`j=1/2` common-collision scope, but Iter083N does not establish that any of the 32 boundary components carries a nonzero physical residue of maximal order. Boundary activation remains an actual-residue question.

`status/ITER077_CONTACT_FORMULA_ERRATUM.md` remains controlling and historical Iter077E/F source-lock-invalid siblings remain quarantined.

## Verdict

`CONFIRMED_SCOPED`

Critic classification: `ITER083N_PROVENANCE_CORRECT_RETRY_CRITIC_CONFIRMED_SCOPED`.

The Researcher theorem is correct exactly as a local, conformal, simple-pole, universal-supported-residue-class statement. It does not constitute a physical finite-part scheme-dependence theorem or a selector.

## Authorized next gate

Do **not** spend the next authoritative production on another generic radial candidate merely because one can be written down. The already-prepared Iter083O sum-of-squared-Cartan-rapidities gate can at most establish a source-native geometric candidate while its own P7 admits that the audited causal/Toller source does not mandate that candidate as the renormalization defining function. Its downstream-unlock value is therefore lower than the remaining physical question.

The highest-value next gate is a prospectively frozen **`ACTUAL_SOURCE_ORDERED_RESIDUE_NORMAL_JET_ANNIHILATOR_GATE`** (or an equivalent source-faithful residue gate). It must target the actual fully boundary-contracted source-ordered K3/K4/K5 residue data in the frozen minimal sector and ask whether the residue is zero, has lower normal order, or annihilates all defining-function changes left free by Iter083M. It must preserve source ordering, all relevant boundary components, exact source normalization/branch conventions and the published spectral prescription. If the actual residue object cannot yet be defined without exchanging limits or substituting a surrogate, return `BLOCKED_OBJECT_DEFINITION`.

A cheaper source-authority audit for an exact nonlinear defining function is admissible only if it can establish that the primary causal/Toller construction **mandates** the function for analytic extension; merely proving that a smooth source-native candidate exists is not a selector and should not displace the actual-residue front.

## Claim locks

Unchanged: no `NEW_PHYSICS_FOUND`; no complete-QG claim; no unique physical K5 extension; no source-authorized finite-part selector; no actual nonzero physical finite-part scheme dependence; no generic finite-spin signed P3; no exact full-amplitude cancellation/non-cancellation theorem; no causal-vertex finiteness/divergence theorem; no physical regulator-independence theorem; no physical source->K4 pushforward; no nominal epsilon^-1 coefficient; no G3 PASS; no F9/G8/K5 promotion; retain published spectral `i epsilon` in its source scope.