# Iteration 063B preregistration — source-backed direct-vertex / EPRL-control qualification

Date: 2026-09-13

Prospective preregistration before implementation/production.

## Question
Does the repository already contain an immutable, source-backed object sufficient to define the next direct-causal K4 amplitude gate with an exact EPRL control, without importing a guessed representation law or fitting a normalization after seeing output?

## Frozen qualification requirements
A source object is `QUALIFIED` only if repository-tracked material contains all of the following, with file/line provenance captured in the artifact:
1. a bibliographic source identifier or immutable source snapshot for the causal/Toller vertex;
2. an explicit mathematical definition of the causal/direct vertex integrand or branch-resolved amplitude object;
3. an explicit relation specifying how the corresponding standard/EPRL control is obtained (e.g. branch sum, orientation sum, or source-stated limit), rather than an inferred analogy;
4. enough convention data to map ordered wedges `(a,b)`, physical `kappa_ab`, and the spectral branch sign used in Iter062;
5. no dependence on a preferred spanning tree/cycle basis or sequential finite-part order.

Repository-wide text search may identify candidates, but qualification requires all five conditions within source-backed tracked material. Mere mentions of `EPRL`, `Toller`, `causal`, or `standard vertex` do not qualify.

## Frozen outputs
- `ITER063B_SOURCE_CONTROL_QUALIFIED`
- `ITER063B_SOURCE_CONTROL_BLOCKED_MISSING_EXPLICIT_RELATION`
- `ITER063B_SOURCE_CONTROL_BLOCKED_MISSING_CONVENTIONS`
- `ITER063B_SOURCE_CONTROL_BLOCKED_NO_IMMUTABLE_SOURCE`
- `ITER063B_IMPLEMENTATION_INVALID`

## Interpretation
PASS only authorizes construction of a later numerical/symbolic direct-vertex gate. BLOCKED means no such gate may be fabricated from structural evidence alone; external/source acquisition or a mathematically explicit derivation must come first. No K5/G3/F9/G8 promotion and no physical finiteness/sector claim is allowed.