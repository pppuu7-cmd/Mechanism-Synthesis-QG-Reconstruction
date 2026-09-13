# Iteration 070A result — finite-epsilon K4 joint-spectral tempered-family qualification

Date: 2026-09-13

## Authoritative provenance

- Preregistration: `026f1ee074a0961b464226bfdb305f14fbc1bde0`
- Implementation: `5944d57f68a4275203a852c1d45fa171cb66787e`
- Launch/head: `b72e0b70eab70ebf1a47eb24a195e6039e354d49`
- Workflow run: `34741624207`
- Aggregate job: `103682359416`
- Aggregate artifact: `10312736337`
- Aggregate digest: `sha256:1ecf4d89943a0685c80ec2737ed50f0cf2dad2af2c9c4c8c48f801e5d64879c8`

The production matrix contained `32` raw jobs (`8` physical sigma classes x `4` K4 tree/cycle bases), each evaluating the two frozen exact source points T1 and T2, for `64` exact cases total. All 32 raw jobs completed successfully and the frozen aggregate consumed all raw JSON artifacts before terminal classification.

## Frozen terminal result

Terminal classification:

`ITER070A_K4_FINITE_EPSILON_JOINT_SPECTRAL_TEMPERED_FAMILY_QUALIFIED`

The frozen aggregate reports:

- `32/32` job lanes valid;
- `64/64` exact source cases valid;
- exact generic radial degree set `{+6}`;
- explicit global polynomial-bound degree set `{12}`.

For every frozen tree/sign/source case:

1. the six edge flows are real affine functions on real cycle space;
2. each denominator has nonzero constant imaginary part `-s_e epsilon`, so there are no real-cycle poles for fixed `epsilon>0`;
3. the rational kernel is smooth on real cycle space;
4. its generic radial growth remains exactly `+6`, consistently with Iter069;
5. the numerator-degree/finite-epsilon denominator lower bounds give a finite global polynomial bound, hence each fixed-`epsilon>0` member defines a tempered distribution by pairing with Schwartz test functions.

## Scientific interpretation

This closes a useful prerequisite: the reduced source-backed K4 finite-spectral family is a well-defined tempered-distribution family at each fixed positive epsilon, despite not being ordinarily integrable at spectral infinity.

It does **not** prove that the family has a unique, finite, or path-independent `epsilon -> 0+` limit in `S'`. It also does not prove a common Toller tube domain, a canonical correlated K4/K5 collision boundary value, or a physical causal-vertex finiteness/divergence theorem.

The next admissible physics-critical step is therefore a prospectively frozen correlated `epsilon -> 0+` distributional boundary-value/path audit, with basis/permutation/order covariance controls and no fitted subtraction or preferred sequential finite part.

No K5/G3/F9/G8 promotion is authorized.
