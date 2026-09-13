# Iter075D — Toller branch-flip kernel held-out certificate

Date: 2026-09-13

## Authority

- preregistration: `c7166bdeeb0f5dc2adb65b1a3d28b4d664bf2f31`
- implementation: `e613ffa8b4a10f82b99733149e26d79fc1b649fd`
- production head: `d8b24077897a89ca40efa5f1ee2e00e2eba58adc`
- workflow run: `34755617861`

Jobs / artifacts:

- `103719363992` (`two_one`) — artifact `10317590592`, digest `sha256:c7f8f12eaa122e5f9690c702c1134679563989770d09bd4f54023c5a92ef0c2b`
- `103719364004` (`h_h`) — artifact `10317655444`, digest `sha256:0c7dfdb7630283875166af32bb4f52ddab6caed796be29935f53fb23ba190c2b`
- `103719364021` (`three_four`) — artifact `10317461437`, digest `sha256:decd8d26b6f96c90eb31d7facab36054ec059d01d1d79c559868efe3a01aaf0f`
- `103719364027` (`one_two`) — artifact `10317800972`, digest `sha256:3da03d93001aacfa978ff7fd5b74205a3e3c8c2e1daafe92d80b275af8ced772`
- `103719364071` (`threehalf_fivehalf`) — artifact `10316866930`, digest `sha256:db810c0e6b3a8e36e00019849fae8cff5c1785ed1025c3e6e6c707018834bb4c`
- `103719364073` (`fivehalf_half`) — artifact `10316967325`, digest `sha256:39fe82114ed13f7ad425cfc0c02766665cc4527eb0e3d236373bf6113cf560c3`

## Frozen scientific classification

`ITER075D_BRANCH_FLIP_KERNEL_RECURRENCE_CERTIFICATE_SUPPORTED_SCOPED`

All six prospectively frozen held-out lanes passed. Across `648/648` records:

- all source coefficients were finite and nonzero;
- the branch-flipped comparison
  `K_s(j,l;rho,rtilde,epsilon) = -conj(K_-s(l,j;rho,rtilde,epsilon))`
  satisfied the frozen relative tolerance `1e-40` in every record;
- observed residuals were at approximately `1e-101` numerical scale at 100-digit arithmetic;
- the ratio to the conjugated branch-flipped coefficient was compatible with the frozen constant `-1` throughout;
- changing epsilon over `1e-2, 3e-4, 1e-6` did not alter the result;
- the same-branch negative control failed the candidate identity on 100% of records in every lane (`negative_fraction = 1.0`), safely above the frozen 90% requirement.

## Interpretation

The published Feynman-kernel coefficient therefore has a highly stable held-out branch-flip/index-swap/conjugation relation on the frozen real-spectral domain. This materially strengthens Iter075C by excluding a narrow-panel coincidence.

The result remains **kernel-level**. It is not a formal symbolic proof of the gamma-function identity, is not the full group-function relation for `T^(kappa)(g^{-1})`, and does not establish how all Toller phases, magnetic indices, group coordinates or wedge-ordering data transform. Ordinary representation inversion must still not be transferred branchwise without a source-derived full Toller law.

## Claim locks

No G3/F9/G8/K5 promotion; no physical sector selection; no causal-vertex finiteness/divergence theorem; no new-physics or complete-QG claim.

## Next allowed gate

Audit the existing source-backed full-group/order-reversal machinery (Iter059/060/061/062 and source snapshot) against the now-qualified kernel relation. Only if it supplies an explicit branch/index/phase transformation may a new, prospectively frozen full-group Toller inversion certificate be launched. Otherwise the full-group law remains BLOCKED rather than inferred from this kernel result.
