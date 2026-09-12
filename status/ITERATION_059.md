# Iteration 059 — source-backed equal-spin Toller wedge-reversal law

**Status:** prospectively preregistered before implementation/production

## Scientific question

After Iter058, the K4 signed-normal surrogate has an exact graph-flow characterization, but it cannot be used as physical analyticity input until the actual Toller branch law under wedge-order reversal / group inversion is established.

The causal vertex source uses equal boundary spins on each wedge and the object

`T^(kappa, rho, j)_{j m, j n}(g_b^-1 g_a)`

with `kappa = +/-` fixed by wedge causal data. The 2026 causal-vertex paper defines the branches by the Feynman spectral integral, and the companion Toller paper stresses that `T^(+/-)` are functions on `SL(2,C)`, not representations. Therefore no branchwise composition/inversion rule may be assumed from Wigner-D representation theory alone.

## Source authority frozen before computation

Primary source objects:

1. Bianchi–Chen–Gamonal, *Causal spinfoam vertex for 4d Lorentzian quantum gravity* (2026), causal vertex Eq. (3)/(4):

`T^(±) = lim eps->0+ int_R d rho_tilde/(2 pi i) [±1/(rho_tilde-rho ∓ i eps)] P_jl(rho_tilde;rho) D^(rho_tilde,k)(g)`

and the wedge uses `j=l=j_ab`, `g_ab=g_b^-1 g_a`.

2. Bianchi–Chen–Gamonal, *Toller matrices and the Feynman i-epsilon in spinfoams* (2026), equal source formula and explicit warning that Toller matrices are functions rather than group representations.

3. Standard unitary-principal-series identity for real spectral labels:

`D_{jm,ln}(g^-1) = conjugate(D_{ln,jm}(g))`.

No `beta+i epsilon` rule is introduced.

## Exact proposed transformation frozen before implementation

For the **equal-spin wedge sector only**, `j=l`, real `rho`, real integration variable `rho_tilde`, and `eps>0`, test/derive

`T^(+,rho,k)_{j m,j n}(g^-1) = conjugate(T^(-,rho,k)_{j n,j m}(g))`

and

`T^(-,rho,k)_{j m,j n}(g^-1) = conjugate(T^(+,rho,k)_{j n,j m}(g))`.

Equivalently, wedge-order reversal swaps the two Toller branches and transposes/conjugates magnetic indices. This is a proposed law to be audited, not an assumed result.

## Frozen derivation obligations

The gate must establish all of the following without numerical fitting:

A. **Equal-spin kernel reality:** for `j=l`, the source Toller polynomial kernel `P_jj(rho_tilde;rho)` is invariant under complex conjugation on real `rho_tilde,rho`, by exact pairing of the root set `{-j,-j+1,...,+j}` under `r -> -r`.

B. **Feynman-kernel branch swap:** including the conjugation of the measure factor `1/(2 pi i)`, the complex conjugate of the minus-branch spectral kernel is exactly the plus-branch kernel, and vice versa.

C. **Wigner inverse control:** only the ordinary unitary Wigner-D inverse relation is used to turn `g^-1` into transpose/conjugation. No Toller representation composition law is assumed.

D. **Additive control compatibility:** applying the two proposed identities to `T^+ + T^- = D` must reproduce the Wigner inverse identity exactly.

E. **Unequal-spin negative control:** the audit must explicitly check that the simple kernel-reality step is not silently generalized to arbitrary `j != l`; if `P_jl` is not self-conjugate in the same form, the result remains scoped to the equal-spin causal-wedge sector.

## Exact computational checks

Use symbolic rational-polynomial algebra over `x=rho_tilde` and `r=rho` for doubled spins `2j = 0..12` in the equal-spin sector. Check the kernel identity exactly after clearing denominators. In a separate negative-control matrix, use all `(2j,2l)` with `0<=2j,2l<=8`, `j!=l`, and record whether the same self-conjugacy identity holds; no failure of the negative control invalidates the equal-spin proof, but accidental broad equality must be reported rather than hidden.

Also evaluate held-out high-precision numerical points only as implementation controls, not as the proof: `rho in {0.37,1.13,2.41}`, `rho_tilde in {-3.2,-0.7,0.4,2.6}`, `eps in {1e-3,3e-5}`, with non-pole denominators.

## Frozen classifiers

- `ITER059_SOURCE_OR_IMPLEMENTATION_INVALID`
- `K4_TOLLER_EQUAL_SPIN_WEDGE_REVERSAL_LAW_FAIL`
- `K4_TOLLER_EQUAL_SPIN_WEDGE_REVERSAL_BRANCH_SWAP_SOURCE_DERIVED`

PASS requires A–D exactly and a valid E negative-control report. Numerical tolerance is `1e-40` at 100-digit precision for implementation-control points; numerical checks cannot rescue an exact symbolic failure.

## Interpretation lock

A PASS authorizes only the equal-spin branch/order-reversal transformation actually used on causal EPRL wedges. It does **not** prove contour existence, absolute integrability, a physical sector selection, K4 order independence, K5 validity, vertex finiteness, F9, G3, G8, or new physics. Only after PASS may tournament/positive-circulation geometry be tested against the source branch law as a candidate analyticity input.
