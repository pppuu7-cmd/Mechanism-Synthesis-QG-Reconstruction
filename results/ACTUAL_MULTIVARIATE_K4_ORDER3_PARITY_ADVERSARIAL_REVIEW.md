# AUTOMATION B adversarial review — actual multivariate K4 order-3 parity

Date: 2026-09-15
Reviewed Researcher authority: `results/ACTUAL_MULTIVARIATE_K4_ORDER3_PARITY_RESULT.md`
Reviewed production: run `34994467079`, job `104467110732`, artifact `10407455156`, head `cd57b6d0a9c7c48c17ffea7ac3c978e77107c95f`, ZIP digest `sha256:1021b31937956cf2ff3e84c0a98bd8d3f2abac2ce021f087fd19e8cb39d40486`, production JSON SHA256 `dd93d6bfe0151a3f72b2dc3bcee3ac530108e5f7966f919021e165edd2981934`.

Mandatory Critic verdict: **`INVALID_IMPLEMENTATION`**.

## Why the green production is not a scientific PASS

Operational provenance is internally consistent: the scientific preregistration `4f306f3eda9d5ff71a77580c9c192eb7b8a323d0` precedes implementation/production, the authoritative run and job are terminal-successful, and the artifact digest agrees with the durable ledger. This review therefore does not issue `INVALID_PROVENANCE`.

The failure is inside the frozen P1-P6 scientific implementation contract.

### Witness 1 — frozen hard-coded parity acceptance booleans

The preregistration explicitly makes `hard-coded acceptance booleans in place of computed degree/parity certificates` a malformed negative control and says hard-coded verdict booleans imply `INVALID_IMPLEMENTATION`.

But `scripts/actual_multivariate_polar_k4_order3_parity_gate.py` defines `geometry()` with literal values

- `inversion_preserves_gram=True`,
- `positive_front_measure_invariant=True`,
- `antipodal_domain_invariant=True`.

Those literals feed `front_inversion_symmetric`, P1 and P5 directly. The code computes the Gram determinant, but it does not compute the pulled-back source-Haar/front-density transformation or the actual resolved front-domain invariance. The production negative-control dictionary contains only twelve mutations and does **not** execute the prospectively frozen thirteenth malformed control against hard-coded acceptance booleans.

This alone satisfies the frozen `INVALID_IMPLEMENTATION` condition.

### Witness 2 — P2 does not test source Toller leading degree

Frozen P2 requires verifying that every K4-internal pole-removed source Toller matrix entry has the required leading normal behavior and that no omitted degree-zero/nonanalytic term invalidates the parity count.

Production sets

`P2_six_internal_baseline_degree6 = (bad==0 and all block edge censuses complete)`.

The `census()` routine never evaluates a Toller matrix jet. It only enumerates Iter077I intertwiner choices, labels each graph edge `I` or `E`, hashes row/column skeletons, and confirms that a K4 block has six internal and four external edges. Thus `500000` reported raw terms are an **edge-incidence census**, not a computation of the K4 source coefficient or its internal matrix degrees.

Changing the actual source Toller cubic jet while preserving the same six-internal/four-external incidence would leave P2 unchanged. Therefore the predicate cannot certify the frozen P2 statement.

### Witness 3 — P3/P4 enumerate integer partitions, not the actual cubic source coefficient

`parts=list(comps(3,12))` correctly produces the combinatorial number `364`, but the production never maps those partitions to the actual six internal Toller jets, four external Toller jets, Haar/Jacobian jet, sixteen `q_B` pullbacks/cross-couplings and contraction coefficients from the confirmed bridge.

P4 is only a lexical authority check for phrases in the bridge document. No source jet is multiplied, no homogeneous component is extracted, and no coefficient-level parity certificate is produced. Hence the statement that **every complete contribution** has total odd degree is not established by the executable.

### Witness 4 — P6 does not execute S5 transport

The production P6 test is satisfied in part by

`len(list(itertools.permutations(V))) == 120`.

This counts permutations but does not construct the true induced 32-dimensional boundary action, transport a coefficient tensor, or test orientation/branch compatibility. This is materially weaker than the frozen P6 requirement.

## Counterexample-first analytic attack on the parity bookkeeping

The exact bridge itself shows why simple radial-order counting needs a real coefficient-level proof. For the plus branch, after the common `beta^-2/(2D)` pole is factored, let `z=i rho`, `R=beta^2/sinh(beta)^2`, and use the bridge formulas

`a_+ = -exp(z beta) R`,

`a_- = exp(z beta)[cosh(beta)-2z sinh(beta)]R`,

`t3_reg=(a_+-a_-)/2`.

Exact Taylor expansion gives the cubic coefficient

`[beta^3] t3_reg = -z/12 + z^3/3`.

At the frozen gamma-simple value `rho=gamma/2=3/5`, this is

`-61 i / 500 != 0`.

The full-matrix bridge writes the corresponding channel as `t3(beta) N(h)`, with

`N(h)=[h-h^{-dagger}]/[2 sinh(beta/2)]`.

For an internal relative element `h(X)=exp(-X_b)exp(X_a)`, simultaneous inversion gives exactly `h(-X)=h(X)^{-dagger}` and therefore `N(-X)=-N(X)` while `beta(-X)=beta(X)`. The nonzero cubic scalar correction therefore preserves the odd inversion parity of this individual `N` channel rather than being certified solely by the Researcher integer-partition count.

This is an explicit omitted channel that the production does not inspect. It shows that the claimed implication `relative Taylor order 3 -> automatic parity flip of the full internal factor` cannot be accepted from the present validator.

This review does **not** promote that channel to `SCIENTIFIC_FAIL_CONFIRMED`, because a prospectively valid full-32 source contraction/front pairing of the channel has not yet been executed. It is a concrete adversarial witness against the implementation/proof path, not yet a terminal nonzero K4 residue theorem.

## Source/order/surrogate audit

The intended object is correct in scope: source-ordered one-wedge construction -> Toller functions -> ten-factor product -> full boundary contraction -> K5 group/distributional object, inside the independently confirmed 16-parameter `q_B` germ. No termwise theta/delta/delta-prime product is promoted and no scalar/Hodge surrogate is used in the declared object.

`status/ITER077_CONTACT_FORMULA_ERRATUM.md` remains controlling; historical Iter077E/F stay quarantined. The published one-wedge spectral `i epsilon` remains locked. The defect found here does not reopen the independently confirmed K3 result or the independently confirmed K4 cubic object-definition bridge; it invalidates only the downstream Researcher K4 zero certification.

## Verdict and authority consequence

**`INVALID_IMPLEMENTATION`**.

The Researcher statement `Res_(L_K4=0) U = 0` from run `34994467079` is not downstream-usable authority. The current K4 simple-face coefficient returns to `?`; no K5 order-8 gate may consume the K4 zero.

The parity hypothesis itself remains scientifically unresolved by this review. It may still be true after a source-faithful coefficient-level calculation, but green CI and incidence/partition counts do not establish it.

## Authorized next gate

Only a **control-only repair/retry of `ACTUAL_MULTIVARIATE_K4_ORDER3_PARITY_GATE` under the unchanged scientific preregistration** is authorized.

The repaired implementation must:

1. derive front measure/domain inversion from the actual pulled-back source geometry, with no literal acceptance booleans;
2. mechanically reconstruct the internal Toller radial/front expansion through relative order 3 for both branches and all matrix entries, including the nonzero cubic `t3_reg` channel above;
3. build the actual coefficient contributions from the six internal jets, four external jets, Haar/Jacobian jet and all relevant `q_B` pullback factors in the one confirmed chart, rather than enumerating unlabeled weak compositions only;
4. execute the complete all-32 boundary contraction for each contribution or provide an exact symbolic parity theorem that consumes the real coefficient objects;
5. execute the true induced-leg S5 transport, not merely count 120 permutations;
6. run every prospectively frozen malformed control, including the missing hard-coded-boolean control, through the same validator;
7. if an inversion-even contribution survives the full source contraction/front pairing, retain it as the frozen FAIL result rather than repairing it away.

Until repaired production is terminal-valid and independently reviewed, K5 order 8, finite-part selection, global patching, causal E3/E4/E6, G3, regulator removal/independence, RG, continuum, spin-2, GR, matter/QFT and prediction remain locked.
