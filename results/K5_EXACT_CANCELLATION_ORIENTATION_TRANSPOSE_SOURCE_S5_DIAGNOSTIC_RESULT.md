# K5 exact cancellation orientation-transpose source S5 diagnostic — terminal result

Date: 2026-09-17

Classification: **`ORIENTATION_TRANSPOSE_SOURCE_S5_EXACT`**.

This is an exact implementation/control result for the S5 lane of the K5 exact-cancellation resolver. It is not by itself a physical corner, Stokes/IBP, period, finite-part, regulator-independence, or downstream-QG verdict.

## Prospective authority

- Parent scientific gate: `d6b0e805101c8590eafac71398cc2b1466691752`.
- Diagnostic preregistration: `3090c19b968edc7a34e6b6e08c65e8a00465971e`.
- Implementation: `b6e517c729a635d877188e275cd4301dd3aecade`.
- Workflow/head: `2fc8cfc982e9fd0fea8563a27517e1b70e385901`.
- Production run: `35174669582`.
- Job: `105053613749`.
- Artifact: `10477199026`.
- Artifact ZIP SHA256: `90a54d2b4e96aa371e30d9c1bab8814bb1e53dc0babadf73cd2dd2155a4dc3a9`.
- Production JSON SHA256: `dcd93e55270dc7421f9f83b21ccfae7fdd7f27e5d2abe1138ef6fab77abb3242`.

## Exact result

All frozen implementation controls pass. The frozen K5 cycle and inverse each reverse the canonical orientation of exactly four of the ten edges.

Under the prospectively frozen full source-entry transport

- orientation preserved: `(row,col) -> (row,col)`;
- orientation reversed: `(row,col) -> (col,row)`;

at the permuted edge position, the complete weighted source-type dictionary is exactly S5 covariant:

- `tcw_keys = 7776`;
- transported TCW key set exact: true;
- transported TCW rational coefficients exact: true;
- inverse round trip exact: true;
- no key collisions.

Independent exact recompression of the transported source-type dictionary through the authoritative entry metric / Wick matching map reproduces the full compressed dictionary exactly:

- authoritative matching keys: `945`;
- recompressed matching key set exact: true;
- recompressed two-channel rational coefficients exact: true;
- mismatch samples: empty.

The base recompression also exactly reproduces the authoritative `MATCH_COEFF` dictionary, so the diagnostic does not rely on a new compression convention.

## Diagnosis

The previous `COMPRESSED_SOURCE_S5_COVARIANCE_FAIL_EXACT` result is therefore localized as an implementation defect in the **naive post-compression transport**, which permuted matching edge indices and applied only a global orientation sign after the source-entry row/column data had already been eliminated.

The physical source itself and the exact compression map are not falsified by that control. Exact covariance is restored by the prospectively frozen orientation-sensitive source-entry transpose action.

This is also consistent with the independently established source-vector result `A_cycle W = W I_2`: no nontrivial post-hoc constant two-channel mixing matrix is needed or allowed.

## Consequence

The exact-cancellation resolver may now receive an execution-only S5 repair that transports the full source-entry object using the frozen orientation-transpose rule before compression. The resolver must then be rerun over all 32 proper orbits and both physical channels. The historical invalid resolver payload may not be promoted automatically.

No local physical exponent or global Stokes/IBP claim is authorized until the repaired resolver terminalizes under its original scientific classifier.
