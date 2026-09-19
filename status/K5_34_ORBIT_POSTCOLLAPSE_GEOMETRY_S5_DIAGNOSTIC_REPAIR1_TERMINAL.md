# Corrected post-collapse S5 geometry/covariance diagnostic — terminal

Date: 2026-09-19

The original implementation was superseded for classifier authority by implementation-only repair prereg `cd4dcf9f3b88b142d5413da0c8d17b24acd40074`.

Corrected production:
- run `35407837027`, attempt 1
- head `47d2aef09e7f42bc412f7304310a59c3bd60df6a`
- job `105801164758`
- artifact `10574116412`
- ZIP SHA256 `26a0c67083346072a2f63e4fd22af934847f9be4f7556b31a20a7115e7c3d5b4`
- raw JSON SHA256 `ab2fcb05236337dfbd4fde346d2c0840ca8821e27c436290811be49cbdb53ed3`

Terminal classification:

`K5_S5_POSTCOLLAPSE_DEFECT_MATCHING_COVARIANCE_COMPOSITION`.

All validity and malformed controls pass. Corrected stage vector is exactly G1–G7 PASS, G8 FAIL, G9 FAIL downstream. G5 explicitly includes the full dual-jet Laplacian congruence and passes. The first failing matching remains `((0,1),(2,3),(4,5),(6,7),(8,9))`.

Thus the implementation-only G3/G5 correction does not change the localization. The pre-existing G8-only prereg `a9781b3c6b61ecaa1940ae796ae0a68b9b29c9b6`, frozen before this corrected output was available, is revalidated without changing its lane, H1–H7 stages, controls, classifier, or claim ceiling.

Resolver authority remains `0/64`. Heavy resolver and global Stokes/IBP remain unauthorized.
