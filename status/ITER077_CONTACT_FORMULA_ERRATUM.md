# Iter077 contact-formula provenance erratum

**Date:** 2026-09-14

## Purpose

This note quarantines a source-transcription error discovered after parallel `Iter077E-SM` / `Iter077F-SM` execution began. Historical files, preregistrations, workflow labels and artifacts are retained unchanged for provenance. Their source-dependent verdicts must not be promoted as authoritative where they rely on the incorrect formula below.

## Correct primary-source formula

Primary authority: E. Bianchi, C. Chen, M. Gamonal, **“Causal spinfoam vertex for 4d Lorentzian quantum gravity”**, arXiv:2601.23162, Appendix D Eqs. (37)-(39).

The contact distribution is

`delta^(rho,j)(x) = sum_{n=0}^{2j} [c_{n+1}^(rho,j)/(n+1)!] (-i)^(n+1) d^n/dx^n delta(x)`.

The coefficients `c_n^(rho,j)` are the `n`th derivatives, at equal spectral parameters, of the gamma-ratio polynomial `F_j`, and Eq. (39) expands

`F_j(rho+sigma q,rho) = 1 + sum_{n=1}^{2j+1} c_n^(rho,j) (sigma q)^n/n!`.

Therefore the contact formula uses `c_{n+1}` and the complex factors `(-i)^(n+1)`. It does **not** use `c_n (-1)^(n+1)`.

## Exact `j=1/2` correction

For `j=1/2`, the exact polynomial is

`F_(1/2)(rho+q,rho) = ((rho+q)^2 + 1/4)/(rho^2+1/4)`.

Let `D=rho^2+1/4`. Then

`c_1 = 2 rho/D`,

`c_2 = 2/D`,

and the primary-source Eq. (37) gives

`delta^(rho,1/2)(x) = -(2 i rho/D) delta(x) - (1/D) delta'(x)`.

In the gamma-simple all-spin-half sector, `rho=gamma/2`,

`delta^(gamma/2,1/2)(x) = -[4 i gamma/(1+gamma^2)] delta(x) - [4/(1+gamma^2)] delta'(x)`.

For the frozen `gamma=6/5` control this is

`delta^(3/5,1/2)(x) = -(120 i/61) delta(x) - (100/61) delta'(x)`.

The delta-prime coefficient is nonzero for every finite real `gamma`; the ordinary delta coefficient is nonzero for finite real `gamma != 0`.

## Historical gates affected

### `Iter077E-SM` microlocal wavefront sibling

The source supplement `sources/CAUSAL_SPINFOAM_VERTEX_2026_CONTACT_PULLBACK_MICROLOCAL_SUPPLEMENT.md`, preregistration `prereg/ITER077E_SM_CONTACT_WAVEFRONT_PULLBACK_CRITERION.md`, implementation and run `34785411389` used the incorrect transcription `c_n (-1)^(n+1)` and the derived claim `c_0=1 -> -delta`.

The run is therefore **NON_AUTHORITATIVE_SOURCE_LOCK_INVALID**, even though its qualitative microlocal conclusion may survive after correction. Result commit `7267a852f7a055be521ceba1eda0512570702bc2` must be read only as historical evidence pending a corrected gate.

### `Iter077F-SM` rank-9 contact-scaling sibling

The source supplement `sources/CAUSAL_SPINFOAM_VERTEX_2026_RANK9_CONTACT_SCALING_SUPPLEMENT.md`, preregistration `prereg/ITER077F_SM_RANK9_CONTACT_SCALING_EXTENSION.md`, implementation and its workflow froze the same incorrect coefficient formula and explicit wrong `j=1/2` coefficients. Therefore any resulting `Iter077F-SM` source-dependent PASS is **NON_AUTHORITATIVE_SOURCE_LOCK_INVALID** and may not be promoted by status/recovery.

The scaling-degree table itself can be independently re-tested, but its combination with the source contact coefficients must be prospectively repeated.

### `Iter077E-SM` source-contact BLOCKED sibling

The earlier scaling gate that returned `BLOCKED_OBJECT_DEFINITION` because the then-frozen repository snapshots lacked an explicit local formula remains a valid historical statement about those frozen snapshots. The primary source has since been re-inspected and provides the explicit Eq. (37)-(39), so that blocker is now resolved as a source-acquisition issue and should not remain the active frontier.

## Corrected forward gate

The next authoritative source-map gate is `Iter077G-SM`. It must prospectively verify the exact Eq. (37)-(39) `j=1/2` coefficients, reconstruct the contact Fourier polynomial, re-test the rank-9 self-stress wavefront collision without relying on the false `-delta` normalization, and independently re-test the six-dimensional scaling-degree threshold.

## Claim firewall

This erratum does not assert cancellation or survival of the full correlated contact channel after smooth phases, `CP^1` measures, intertwiners and all source integrations. It establishes only that the historical source lock was wrong and must be prospectively corrected before any further physical claim.