# Iter075B preregistration — Toller wedge-order reversal source-authority audit

**Frozen before implementation/production.**

## Scientific question

Does the cited 2026 Toller/casual-spinfoam source material explicitly authorize a full branch transformation under group inversion / wedge-order reversal for the source object `T^(kappa)(g_b^-1 g_a)` that is strong enough to propagate causal pole-sign data through edge reversal?

## Source authority frozen for this gate

1. Bianchi, Chen, Gamonal, *Toller matrices and the Feynman i-epsilon in spinfoams*, arXiv:2604.24945 / Phys. Rev. D 114, 046014 (2026).
2. Bianchi, Chen, Gamonal, *Causal spinfoam vertex for 4D Lorentzian quantum gravity*, arXiv:2601.23162 / Phys. Rev. D 113, 126020 (2026).

The audit must preserve the distinction explicitly stated in arXiv:2604.24945 Eq. (14): Toller `T^(±)` are functions on `SL(2,C)` and are **not** representations, so ordinary representation composition/inversion may not be imported. Eq. (15), `T^(+)+T^(-)=D`, and the Wigner-D inverse identity by themselves are not sufficient to infer a branchwise Toller inversion law.

## Frozen evidence requirements

A source-authorized branch/order-reversal law is `QUALIFIED` only if the source explicitly gives, or a line-by-line algebraic derivation from source equations uniquely fixes, all of:

- which branch `kappa` maps to under `g -> g^-1` / wedge order reversal;
- any swap of matrix indices;
- complex conjugation, representation-label changes, and phase factors;
- compatibility with `T^(+)+T^(-)=D` and the Wigner-D inverse identity;
- a reduced pure-boost control consistent with the general full-group statement.

The gate is `BLOCKED_SOURCE_LAW_NOT_ESTABLISHED` if only Wigner-D inversion, additive branch sum, pure-boost asymptotics, or nonrepresentation warnings are source-explicit but the full branchwise inversion/order-reversal law is not uniquely established.

## Frozen interpretation rule

Allowed terminal classifications:

- `ITER075B_TOLLER_ORDER_REVERSAL_SOURCE_LAW_QUALIFIED_SCOPED`
- `ITER075B_TOLLER_ORDER_REVERSAL_BLOCKED_SOURCE_LAW_NOT_ESTABLISHED`
- `ITER075B_SOURCE_AUDIT_INVALID`

No tournament/positive-circulation result may be promoted to a physical causal-sector statement from this gate alone. No K5/G3/F9/G8 promotion. No `NEW_PHYSICS_FOUND`, complete-QG, finiteness/divergence theorem, fitted phase, or assumed representation law.

## Frozen control

The audit must explicitly reject the deliberately invalid inference

`T^(kappa)(g^-1) = [T^(kappa)(g)]^†`

when its only justification is that the Wigner matrix `D` is unitary. This is a negative control because the source explicitly states that Toller branches are not representations.
