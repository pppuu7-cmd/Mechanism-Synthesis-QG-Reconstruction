# Iter075C — Toller Feynman-kernel inversion candidate audit

Date: 2026-09-13

## Authority

- preregistration: `0106e9b658aa37171e60262352810be48e6b674f`
- implementation: `8498324cb5c6838a0e4f53d036c98ecad524d3d6`
- production head: `f0d9b7fda85e4a05c9d2dbca100c59104abf835f`
- workflow run: `34753274168`
- job: `103713294964`
- artifact: `10316637744`
- artifact digest: `sha256:095e3057b03d2eb2d0ff5863b708c91bb0c708e1cac7d4cd059f3ee050107163`

## Frozen result

Scientific classification: `ITER075C_SIMPLE_TOLLER_INVERSION_CANDIDATE_SURVIVES_KERNEL_GATE_SCOPED`.

On the frozen real-tilde-rho panel, the branch-flipped candidate comparing the published Feynman-i-epsilon kernel coefficient for `(s,j,l)` with the conjugated coefficient for `(-s,l,j)` is compatible in every lane. The normalized ratio is constant to roughly `1e-91` and has unit magnitude with phase `pi` modulo branch convention, i.e. the observed kernel-level relation is consistent with an overall minus sign. The same-branch candidate fails systematically, with normalized deviations of order `4.5e-4` to `6.0e-4`, far above the frozen `1e-20` tolerance. The synthetic constant-factor control passes exactly.

## Scope

This is a necessary same-real-axis Feynman-kernel identity check only. It does **not** establish the full Toller function inversion law on `SL(2,C)`, does not prove the transformation of all labels/phases/indices under wedge-order reversal, and does not authorize using tournament/positive-circulation geometry as a physical analyticity selector. It does not promote G3, F9, G8 or K5 and does not imply causal-vertex finiteness/divergence.

## Next allowed gate

Prospectively test whether the surviving branch-flip/minus-sign relation is stable under independent epsilon, rho, tilde-rho and admissible `(j,l)` hold-outs and whether it can be reduced to a finite gamma-recurrence identity rather than a pointwise numerical coincidence. Only after that may a full-group Toller inversion/order-reversal gate be attempted.
