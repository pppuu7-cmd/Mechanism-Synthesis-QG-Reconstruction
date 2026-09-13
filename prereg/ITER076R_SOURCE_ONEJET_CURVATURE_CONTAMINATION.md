# Iter076R preregistration — source one-jet versus nonlinear-map curvature contamination

**Date:** 2026-09-13

**Status:** `PREREGISTERED / EXACT_REPRESENTATION_GATE`

## Motivation

Iter076Q proves that the global sign of the exact linear Hodge line `{+H,-H}` disappears after passing to homogeneous quadratic transport. Therefore the Hodge sign itself no longer blocks the degree-two layer.

However, for a nonlinear source-to-cycle coordinate map

`y = X x + (1/2) K(x,x) + O(x^3)`,

a nonzero source one-jet can feed the degree-two coefficient through the quadratic curvature `K`. The next question is whether this contamination is automatically absent from source geometry/symmetry or whether an allowed channel exists and the physical one-jet must be derived explicitly.

## Frozen inputs

Use only:

- the exact K4 cut/cycle representations and Hodge line from Iter076H/Q;
- the exact source-domain Haar/KAK local jet from Iter076D;
- the exact Toller conjugation obstruction from Iter076P;
- the frozen degree-two monomial basis from Iter076Q.

No physical source-to-K4 nonlinear map may be invented. No coefficient may be fitted.

## Lane A — source Haar one-jet

Reproduce the exact local radial Haar/KAK factor from Iter076D:

`(sinh beta / beta)^2 = 1 + beta^2/3 + 2 beta^4/45 + ...`

PASS-A requires the first derivative at `beta=0` to vanish exactly. This establishes only that the Haar density itself contributes no radial one-jet in the frozen local coordinate.

## Lane B — symmetry-allowed quadratic curvature channel

Let `C(pi)` and `Z(pi)` be the frozen 3-dimensional cut and cycle representations. A quadratic curvature tensor compatible with the same sign-twisted cut-to-cycle transformation law as the Hodge line is a `3 x 6` matrix `K` satisfying, for every `pi in S4`,

`Z(pi) K = sgn(pi) K Sym2(C(pi))`.

Solve this exact rational linear system.

PASS-B requires the dimension of this intertwiner space to be determined exactly. The key discriminator is:

- dimension `0`: symmetry forbids quadratic curvature contamination;
- dimension `>0`: symmetry permits it, so one-jet vanishing/provenance remains physically relevant.

No numerical tolerance is allowed.

## Lane C — explicit contamination witness

If Lane B finds a nonzero curvature channel, construct an exact nonzero basis element `K0`. For a generic symbolic covector `ell=(l0,l1,l2)` on the cycle output, compute

`q_ell(x) = ell K0 m_2(x)`

on the frozen six-dimensional degree-two monomial vector `m_2(x)`.

PASS-C requires an exact nonzero polynomial witness for generic `ell`, proving that symmetry alone does not annihilate all possible one-jet/curvature contamination.

If Lane B finds dimension zero, Lane C instead verifies the null result.

## Lane D — source-faithfulness firewall

The implementation must preserve all of the following facts:

1. Iter076D establishes zero Haar radial one-jet, but not zero one-jet of the full Toller/intertwiner numerator.
2. Iter076P shows that known exact Toller complex conjugation exits the source causal K5 image; it cannot be used as a same-causal evenness symmetry to set the full numerator one-jet to zero.
3. Iter076Q establishes sign-independent homogeneous quadratic linear transport, not the nonlinear curvature tensor of the physical pushforward.
4. No `epsilon^-1` coefficient, generic finite-spin signed P3, physical finiteness/divergence theorem, G3, F9, G8 or K5 promotion is emitted.

## Frozen classifications

If Haar one-jet is zero but the twisted quadratic curvature space is nonzero and has an explicit contamination witness:

`ITER076R_HAAR_ONEJET_ZERO_BUT_SYMMETRY_ALLOWS_NONLINEAR_QUADRATIC_CURVATURE_SOURCE_NUMERATOR_ONEJET_STILL_REQUIRED_EXACT_SCOPED`

If the curvature space is exactly zero:

`ITER076R_SYMMETRY_FORBIDS_QUADRATIC_CURVATURE_CONTAMINATION_EXACT_SCOPED`

Any frozen algebra/evidence predicate fails:

`ITER076R_SOURCE_ONEJET_CURVATURE_GATE_FAIL`

## Scientific interpretation

A nonzero curvature channel does not prove that the physical source-to-K4 map has such curvature. It proves only that S4/twisted-Hodge symmetry cannot be used to dismiss the contamination. The next admissible task would then be a source-faithful derivation/audit of the full Toller/intertwiner numerator one-jet and/or the actual nonlinear pushforward curvature.

## Claim locks

No `NEW_PHYSICS_FOUND`; no complete-QG claim; no generic finite-spin signed P3; no physical causal-vertex finiteness/divergence theorem; no nominal `epsilon^-1` coefficient; no G3/F9/G8/K5 promotion; retain the published spectral `i epsilon` prescription.
