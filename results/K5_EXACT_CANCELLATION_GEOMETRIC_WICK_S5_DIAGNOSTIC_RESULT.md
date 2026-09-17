# K5 exact cancellation geometric/Wick S5 diagnostic — terminal result

Date: 2026-09-17

Classification: **`PROJECTED_WICK_CHANNEL_S5_COVARIANCE_FAIL_EXACT`**.

This is an exact implementation/control result. It is not a physical corner, local integrability/flux, global Stokes/IBP, period, finite-part, regulator-independence, or downstream-QG verdict.

## Prospective authority

- Parent scientific gate: `d6b0e805101c8590eafac71398cc2b1466691752`.
- Diagnostic preregistration: `4262e9b55308ba9128eeca2cd195ae0672772bed`.
- Implementation: `9fd0a6d63a0e99a9adaf9d1943e2b9a672589d07`.
- Workflow/head: `bed8ec8538712c15a7cb3dfface1b09834fe5dec`.
- Production run: `35174909771`.
- Job: `105054343705`.
- Artifact: `10478097780`.
- Artifact ZIP SHA256: `0ef60634d4c0e72c5aacb947cc1bf4c42b1cffb58540e1b6bf9ec014c32d4bf8`.
- Production JSON SHA256: `8bbdbfeeec6e82b20b5259d00ffdb0082d154b6c2f0aaaaac30353fe355f8b4a`.

## Exact result

For both frozen asymmetric witnesses `W1,W2`, for the frozen K5 cycle and its inverse, and for every edge pair and every inverse-series order `n=0,...,4`, the exact rational reduced-Laplacian covariance identity

`C'_{p(i),p(j),n} = s_i s_j C_{i,j,n}`

holds identically. There are no geometric covariance mismatch witnesses.

The already-confirmed orientation-transpose source-entry transport/recompression control also passes exactly in every lane.

Nevertheless, after contracting the exact covariances with the two current compressed physical channel coordinate functionals, the projected channel series fail coefficient-by-coefficient covariance for both channels and all tested witnesses/directions, beginning already at series order zero.

Thus the remaining S5 failure is not in:

- reduced K5 Laplacian / root-gauge covariance;
- inverse-series geometry;
- edge orientation signs;
- source-entry row/column transpose transport;
- source compression to 945 matching keys.

It is localized to the interpretation/transport of the two invariant-dual **coordinate channels** used by the projection.

## Consequence

No fitted channel matrix is authorized. The next admissible diagnostic must reconstruct the exact dual/contragredient coordinate transport directly from the authoritative 32-dimensional S5 representation and Reynolds projector, distinguishing invariant vectors from coordinate functionals / dual basis elements. Only that source-derived transport may be used to repair the resolver S5 certificate.

The historical resolver remains `INVALID_IMPLEMENTATION` for S5 certification; its exact primary/independent coefficient agreement and its exact U-lane remain useful diagnostics but cannot yet promote N/B physical corner orders.
