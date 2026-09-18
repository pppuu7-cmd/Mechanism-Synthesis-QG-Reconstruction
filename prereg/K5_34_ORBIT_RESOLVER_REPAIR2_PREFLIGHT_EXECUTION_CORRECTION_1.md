# Repair-2 preflight execution correction 1

Date: 2026-09-19

Status: FROZEN AFTER TERMINAL PREFLIGHT INVALID, BEFORE IMPLEMENTATION CHANGE.

Parent repair-2 prereg: `beadf232a89331f62a3e129e83e23576e2a33021`.

Terminal preflight run `35403849670`, head `56eb043f402475f93787726073496e977e248453`, artifact `10572140519`, ZIP SHA256 `2f60c5619d50fa1f95da02447c346b3c32b4a0794804f43b98bf6136ac586fff`, is `INVALID_IMPLEMENTATION`. No heavy science was executed and no N/B value was consumed.

## Frozen implementation defects

Two implementation defects are corrected; no scientific condition is changed.

1. The repair-2 module defines the component-1 Critic authority path before re-exporting repair-1 globals. The re-export overwrites that name with the historical Boundary-S5 Critic path. Therefore checks intended to read the terminal component-1 Critic authority read the wrong JSON object.

   Correction: bind the component-1 Critic authority path only after repair-1 re-export, under a unique non-colliding name.

2. The repair-2 module constructs only the forward endpoint/orientation-transported 32-vector and then selects component 1 directly. The frozen parent repair-2 prereg explicitly requires reproduction of the independent Critic route-2 object. That object is defined by **full forward endpoint/orientation transport followed by exact target boundary contragredient projection/mixing of the full 32-component vector**.

   Correction: after forward old-edge -> target-edge transport, reconstruct the target boundary action from source tensors and apply the exact inverse-transpose target projection to the full 32-vector before component selection and invariant-dual/Wick matching collapse.

This correction is mandated by the already-frozen component-1 hash/cardinality control; it does not use any N/B coefficient/order and does not alter the repair-2 hypothesis after seeing a physical result.

## Controls unchanged

All parent repair-2 preflight controls remain mandatory, including:
- independent Critic route-2 dictionary/support hashes and support cardinality 1536;
- exactly 16 contributor authority;
- 32 / 100000 / 945 locks;
- exact rational arithmetic;
- historical repair-1 malformed-object rejection;
- no q18 partials;
- no invalid resolver coefficient payload.

If the corrected preflight does not pass all frozen controls, heavy resolver repair-2 remains forbidden.

Interpretation ceiling is unchanged.
