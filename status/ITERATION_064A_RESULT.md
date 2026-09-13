# Iteration 064A terminal result — source-defined direct causal pointwise / exact EPRL control

Date: 2026-09-13

## Frozen authority

Preregistration: `3f3c8fa03ab5d35e2a70784924502eb653894bf5`  
Primary-source snapshot: `7df82d28dd6426aa7aaac353a1e0abf795e6fdee`  
Authoritative repaired production head: `ec3c0ed213b7c53d2a546c1a9fbf7c83385dc620`  
Authoritative run: `34732198011`  
Aggregate job: `103656960238`  
Aggregate artifact: `10309427622`  
Aggregate digest: `sha256:2cb05aa6b626f23256a0ba1fcd3502404ecc3387a8521baece660ab238a9f161`

## Initial production authority note

Initial head `a11a686988a5eeab7b04ca8269417f3fb5b41cc7`, run `34732114933` failed identically in all six lanes before any scientific output with:

`ModuleNotFoundError: No module named 'regulated'`

The same carrier had previously been run with repository-root `PYTHONPATH=.` and the stable-hyp2f1 wrapper. Therefore this was classified as a runtime/infrastructure implementation defect, not a scientific result. No lane artifact was produced and the aggregate was structurally invalid.

Workflow-only repair commit `ec3c0ed213b7c53d2a546c1a9fbf7c83385dc620` restored `PYTHONPATH=.`, pinned the already-used `mpmath==1.3.0`, used `regulated/run_with_stable_hyp2f1.py`, and made artifact upload unconditional. Frozen gamma values, seeds, witnesses, thresholds, source object and interpretation were unchanged.

## Terminal classification

`ITER064A_DIRECT_CAUSAL_POINTWISE_EPRL_CONTROL_PASS`

All 6/6 frozen lanes pass for `gamma={0.4,1.2}` × `seed={1701,1702,1703}`.

## Raw lane provenance

- `gamma=0.4, seed=1701`: artifact `10309936002`, digest `sha256:ed8ac328720f9946b876f3b555503b6c01e67853a14f93e3cc04b3ed9a022be3`
- `gamma=0.4, seed=1702`: artifact `10309482468`, digest `sha256:fbd448f8764bc87e8b1c936267495361b20f9e4e21ee048a5eaa86b757f55c7d`
- `gamma=0.4, seed=1703`: artifact `10309756971`, digest `sha256:5a2488892aa7f0b16813be032d323fc1f3fec153963a1e4f3f47b4de17df53f9`
- `gamma=1.2, seed=1701`: artifact `10309986609`, digest `sha256:6a064e79d855d735ca31ee60629d0896de2937232bfc13946a7e36e2aeeb4082`
- `gamma=1.2, seed=1702`: artifact `10310255586`, digest `sha256:0f63536e8f786457ff14a26341e45295efe7de51ba6e8a3ada7a619d8786221a`
- `gamma=1.2, seed=1703`: artifact `10309362794`, digest `sha256:d309195270f2e5f9570d4bde84c980d00be366455db543ee3858dd4aa982ab20`

All six raw artifacts were consumed before terminal classification.

## Worst frozen metrics across raw lanes

- worst KAK reconstruction error: `1.94617110678392e-15` < `1e-10`
- minimum pair boost: `0.44133896410388834` >= `0.12`
- worst edge additive `T+ + T- = D` relative residual: `5.230227719508377531641e-64` < `1e-35`
- worst explicit `2^10` independent-wedge-sign sum vs direct EPRL pointwise integrand residual: `5.663006161342366652884e-64` < `1e-35`
- worst global sigma-flip duplication residual: `1.105326424628305392268e-80` < `1e-60`

The constrained 16-class causal sum was intentionally **not** equated to the EPRL object. Its causal-vs-EPRL relative difference varies strongly over the panel (including values much larger than one), exactly preserving the primary-source distinction between constrained causal sigma data and the unconstrained independent-wedge Eq.(6) control.

## Scope

This is a generic separated, small-spin **pointwise direct ten-wedge carrier** certificate with exact source Eq.(5)/(6) EPRL control. It is not a four-group Haar integration, not an integrated causal vertex, not a boundary-intertwiner-complete convergence theorem, not a proof of absolute integrability or distributional uniqueness, and it does not promote K5/F9/G3/G8 or establish new physics.

## Next allowed step

Do not repeat pointwise branch-sum tests. Prefer analysis-only reuse of validated earlier S5 boundary-carrier covariance evidence where it remains compatible with the now source-pinned inversion law. Any genuinely new production gate should target an unresolved layer: source-consistent boundary contraction/permutation audit not already covered, or a separately preregistered integrated/quadrature convergence qualification with explicit regulator and EPRL controls. K5 remains blocked until the K4/source-selection prerequisites are explicitly closed in `status/CURRENT.md`.
