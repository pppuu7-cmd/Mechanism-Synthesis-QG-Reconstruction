# Iteration 063B authority record — source-control qualification

Date: 2026-09-13

## Frozen gate

Prospective preregistration remains `75fb19ed4644ca422a3954ef8e231d8e35c92fc4` (`status/ITERATION_063B_PREREG.md`). No scientific requirement, output class, target, threshold, or interpretation rule has been weakened after observing production output.

## Initial production is diagnostic / non-authoritative

Initial head: `11c6823e00473650f63ca7ed7464718e1049ae7b`  
Run: `34729216381`  
Job: `103648792303`  
Artifact: `10308837692`  
Digest: `sha256:46ea46cc0c0b9e7882252c7dfc359719856813b1c62cb07569bae25ab079a5ff`

The workflow completed green and emitted `ITER063B_SOURCE_CONTROL_QUALIFIED`, but raw artifact inspection showed that the only `qualified_files` were:

- `status/ITERATION_063B_PREREG.md`
- `scripts/iter063b_source_control_qualification.py`

This violates the frozen requirement that qualification come from repository-tracked **source-backed material**. The implementation scanned the preregistration/audit code itself and allowed generic source-related tokens inside those files to satisfy its regex predicates. Therefore the initial run is classified:

`ITER063B_IMPLEMENTATION_INVALID_SELF_REFERENCE`

It is not a scientific PASS and cannot authorize a direct-vertex/EPRL production gate.

## Minimal repair

Implementation-only repair commit: `ecc99cb078dd2f41007cac429c5cb080bf79d145`.

The repair excludes self-generated audit/status/workflow/code roots from source authority and restricts candidate authority to literature/source-backed `docs/` and `bridges/` text. It also requires a concrete DOI/arXiv identifier rather than generic words such as `source snapshot`. The original stronger same-file qualification rule is retained; it was not weakened.

Workflow retrigger commit / repaired authoritative head: `6102be4255016b43aa49af9f8ee6293abc6a3090`.

Authoritative retry run: `34731891190`.

## Interpretation lock

Until the repaired retry is terminal and its raw artifact is consumed, Iter063B remains **OPEN / implementation repair in progress**. K5 remains BLOCKED; G3 remains OPEN; F9 remains BLOCKED; G8 remains BLOCKED_CONVERGENCE_ONLY. No physical causal-sector, finiteness/divergence, universal no-go, or new-physics claim is authorized.
