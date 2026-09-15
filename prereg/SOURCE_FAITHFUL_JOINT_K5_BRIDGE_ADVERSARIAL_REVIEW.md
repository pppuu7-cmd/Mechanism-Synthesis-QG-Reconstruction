# Independent adversarial review preregistration — source-faithful joint K5 meromorphic bridge

Date: 2026-09-15
Status: **PROSPECTIVELY FROZEN BEFORE REVIEW VERDICT**

Researcher result under review: `results/SOURCE_FAITHFUL_JOINT_K5_BRIDGE_AUTHORITY_RESULT.md`, repaired result commit `79d166fdf89a9e42a653ed3bbb4b0cac426820da`.
Parent scientific preregistration: `4151c02452edd3e5e2c49952686e42e64c6dc180`.
Authoritative repaired production: run `34953022566`, job `104328280379`, head `87e732bab75e3d60f1df1390561fc584f667526f`, artifact `10389449925`, artifact digest `sha256:abf75fdd1d1bfe97a0913cdcddb723b9c9fec6ca075dd47cc414fff593769d1b`, JSON SHA256 `3a66499afb5c16b4fd0643ab3796f7da827d5ec09d3e03359fba2a5ba6c56011`.

## Review question

Does the repaired Researcher result actually satisfy the frozen B1-B9 bridge contract for the frozen local all-`j=1/2` K5 sector, without silently turning a mathematically convenient analytic regularization into a physical finite-part selector?

## Frozen adversarial attacks

A1. **Cartan-radius analyticity.** Re-derive from the source convention `K_z=i sigma_z/2` that `Tr(h h^dagger)/2=cosh beta`; verify exact inversion `beta^2=2s-(1/3)s^2+(4/45)s^3+...`, zero locus, nondegenerate normal Hessian and inversion/compact covariance.

A2. **Block-radius authority.** Check whether `q_B=(1/|B|)sum beta_ab^2` is sufficiently source/mathematically fixed for bridge existence. Distinguish exact nonlinear defining-function choice from tangent-only Iter083M authority. If nonlinear freedom `q_B -> q_B(1+O(q_B))` can alter the meromorphic **polar germ** rather than only finite/holomorphic parts, B7 must be qualified or rejected.

A3. **Full arrangement / blow-up.** Check that resolving all 10 K2, 10 K3, 5 K4 and 1 K5 polydiagonals is a legitimate clean/wonderful arrangement and that divergent K3/K4/K5 blocks have the claimed 20 maximal chains and normal ranks `(6,3,3)`.

A4. **KAK angular degeneracy.** The compact factors in KAK are nonunique at `beta=0`. Verify that the actual `j=1/2` Toller matrix as a function of the group variable nevertheless lifts polyhomogeneously/conormally after real blow-up; rejecting a derivation that assumes `U1,U2` separately smooth at the compact locus.

A5. **Full 32-component object.** Verify finite matrix multiplication and complete boundary contraction preserve the required conormal/polyhomogeneous class and that no representative-component reduction is hidden.

A6. **Continuation theorem matching.** Verify the Mellin/complex-power theorem actually applies to the resolved vector/matrix-valued polyhomogeneous object and original Haar density, with a nonempty convergence chamber. Separate existence/uniqueness of meromorphic continuation from uniqueness of any renormalized value at `lambda=0`.

A7. **Branch/spectral firewall.** Verify the regulator is applied after source Toller construction, is branch-blind/reversal-even, and does not alter the one-wedge spectral `i epsilon` or invoke a false Toller representation/composition law.

A8. **Multivariate residue firewall.** Verify the result defines only a 16-parameter meromorphic germ/polar coefficients. Any claim of a unique one-parameter `A_-1`, finite part, or physical extension without new prospective authority is an automatic overclaim failure.

A9. **Scheme dependence.** Test transformations of defining functions `q_B' = exp(phi_B) q_B`. Determine which part of the multivariate Laurent germ changes. If negative polar data transform nontrivially, record that fact explicitly and limit the bridge claim accordingly; do not confuse meromorphic-family existence with regulator independence.

A10. **Production/provenance.** Confirm repaired run/head/artifact/JSON and that historical run1 / persisted pre-repair `1/30` evidence is superseded, not mixed into authority.

## Verdict taxonomy

- `CONFIRMED_SCOPED`: all bridge-existence obligations survive, with explicit finite-part/regulator-independence ceilings.
- `QUALIFIED`: a genuine multivariate meromorphic family exists, but one or more Researcher B predicates require narrower wording (for example defining-function/scheme dependence).
- `REJECTED_SCIENTIFIC`: a frozen B predicate needed for bridge existence fails.
- `INVALID_REVIEW`: provenance or attack implementation is defective.

The review must not modify the parent B1-B9 criteria after inspecting evidence.