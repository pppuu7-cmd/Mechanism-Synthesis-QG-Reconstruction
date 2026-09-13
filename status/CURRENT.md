# Current MSQGR research state

**Date:** 2026-09-13

- Candidate: `CRQN v0.2` (`CARRIER_SELECTED`)
- Established/source-backed mechanism union: `F1-F8`
- Physical F9 (`CAUSAL_ANALYTICITY_RG_INVARIANT`): `BLOCKED`
- G3 quantum dynamics: `OPEN`
- G8 novelty: `BLOCKED_CONVERGENCE_ONLY`
- K5 distributional/vertex extension: `BLOCKED_CORRELATED_EXTENSION_OBJECT_MISSING`
- Active front: `FINITE_EPSILON_TEMPERED_FAMILY / EPSILON_TO_ZERO_DISTRIBUTIONAL_BOUNDARY_VALUE`

## Controlling source/direct chain

- Primary source snapshot commit `7df82d28dd6426aa7aaac353a1e0abf795e6fdee`: Bianchi-Chen-Gamonal arXiv `2601.23162`, DOI `10.1103/fwql-t4yr`; pins Eq.(3) spectral Feynman `i epsilon`, Eq.(4) direct ten-wedge fixed-causal vertex, Eq.(5) `T+ + T-=D`, Eq.(6) unconstrained independent-wedge EPRL sum, Eq.(7) Cartan/magnetic representation.
- Iter063C run `34732046499`, artifact `10309351521`: `ITER063C_PRIMARY_SOURCE_VERTEX_CONTROL_PINNED`.
- Iter064A run `34732198011`, artifact `10309427622`: `ITER064A_DIRECT_CAUSAL_POINTWISE_EPRL_CONTROL_PASS`.
- Iter064B run `34732360103`, artifact `10310016825`: `ITER064B_K4_SOURCE_PREREQUISITES_CLOSED_FOR_K5_QUALIFICATION`.
- Iter065A run `34732545131`, artifact `10310465490`: `ITER065A_K5_BLOCKED_CORRELATED_EXTENSION_OBJECT_MISSING`.
- Iter066A run `34734333416`, artifact `10309673723`: `ITER066A_GENERIC_MULTIVARIATE_FRAMEWORK_AVAILABLE_SOURCE_SELECTOR_STILL_MISSING`.
- Iter067A run `34736725079`, artifact `10310499751`: `ITER067A_THEOREM_ROUTE_EXISTS_PHYSICAL_HYPOTHESES_UNPROVEN`.
- Iter068A run `34739048517`, aggregate job `103675510433`, artifact `10311807799`, digest `sha256:cb4713dde51dbfb390f6c5276b1d33aaa92b7129d2fbbb2716d6c5c61a701268`: `ITER068A_K4_MICROLOCAL_SKELETON_MIXED_8_OBSTRUCTED_8_COMPATIBLE_CONVENTION_INVARIANT`. This is denominator-skeleton microlocal classification only, not a full Toller wavefront theorem or physical sector selector.
- Iter068C authoritative repaired run `34740924423`, aggregate job `103680419357`, artifact `10312555350`, digest `sha256:69786e4ecd550ba25f2329cae9b904d0dab8fba18326115db606f972f3014b2f`: `ITER068C_PREPULLBACK_CONTROL_CONVERGENCE_REVIEW_1_OF_3`. Exact pre-pullback Eq.(5)/(6) algebra passes; gamma `0.2` missed the frozen finite-epsilon error threshold despite monotone convergence.
- Iter069A prereg `50a73e7e95d68d17c8d419998ae3d691dbc61417`, run `34741379013`, aggregate job `103681570964`, artifact `10313315251`, digest `sha256:0a90750582acf1d5a66dc69db22a1fb0454266ded110e3b08b62be46e6262fb3`: `ITER069A_K4_JOINT_SPECTRAL_HOMOGENEOUS_GROWTH_PLUS6_EXACT`. All four exact tree/cycle-basis lanes prove generic source radial degree `+6`, no-contact control degree `-6`, and source leading coefficient `(c2/2)^6 prod_e L_e(v)`, independent of causal signs, finite epsilon and external flow.
- Iter069B prereg `cdcbf58d59f9d610b38a1ed1996b54c175fe9897`, run `34741408690`, aggregate job `103681654751`, artifact `10313135598`, digest `sha256:034d4438e84a963252e71a722292ee79ed00cbc8c37cbf795d182b5baf04ef59`: `ITER069B_K4_JOINT_SPECTRAL_HELDOUT_GENERIC_GROWTH_PLUS6_CAUSAL_SIGN_INDEPENDENT`. `192/192` held-out exact cases pass over H6/H7, eight physical sigma classes, four bases and three radial directions. This closes the naive ordinary improper real-cycle integral route for the reduced rational family only; it is not a physical causal-vertex divergence theorem.
- Iter070C prereg `5d8f184f4c8b52a936bdf88b188b0f070e8e0c6f`, implementation `558f7a52810dcb48b4c1bf42e2eeb2bb50ff00dd`, head `2655c05ce4a91a6b21a88a899fc2a94eee5ee7e1`, run `34741632282`, raw job `103682199101`, aggregate job `103682249488`, raw artifact `10312646506`, aggregate artifact `10313090332`, aggregate digest `sha256:75750b8efdbd3e053151e64defec5d798eb189c0e9c94dd3f03fd3c59cfa9f84`: `ITER070C_LOW_GAMMA_PREPULLBACK_SMALLER_EPS_CONVERGENCE_SUPPORTED`. For gamma `0.2`, all three held-out tests converge strictly on epsilon `0.0125 -> 0.0015625`; final errors are approximately `0.00342`, `0.00707`, `0.00935`. Iter068C remains terminal REVIEW; this does not prove correlated K4/K5 pullback inheritance.

## Active production

### Iter070A — finite-epsilon K4 joint-spectral tempered-family qualification

- Preregistration: `026f1ee074a0961b464226bfdb305f14fbc1bde0`
- Implementation: `5944d57f68a4275203a852c1d45fa171cb66787e`
- Authoritative launch/head: `b72e0b70eab70ebf1a47eb24a195e6039e354d49`
- Production run: `34741624207`
- Frozen matrix: `8` physical sigma classes x `4` K4 tree/cycle bases = `32` jobs, each evaluating exact source points T1 and T2 (`64` exact cases total).
- Frozen target: `ITER070A_K4_FINITE_EPSILON_JOINT_SPECTRAL_TEMPERED_FAMILY_QUALIFIED` only if every fixed-epsilon member is real-affine in edge flows, has nonzero constant denominator imaginary parts on real cycle space, is smooth there, retains exact generic degree `+6`, and admits a finite global polynomial bound sufficient for a tempered distribution.
- Scope: fixed `epsilon>0` only. It cannot prove existence/uniqueness of the `epsilon->0+` boundary value.

## Exact K5 blocker after Iter070C / Iter069

The reduced K4 finite-spectral family is now known to have generic polynomial growth rather than ordinary real-cycle integrability, while the independent branch-sum pre-pullback Eq.(5)/(6) control has strong small-epsilon convergence evidence. The remaining physical K5 bridge is still missing.

Unresolved requirements:

1. qualify the fixed-`epsilon>0` joint family as a well-defined tempered/analytic family (Iter070A active);
2. prove a source-selected correlated `epsilon->0+` boundary value in `S'` or an equivalent canonical tube/wavefront construction for the physical Toller family;
3. establish uniqueness without arbitrary local counterterms or preferred tree/cycle/integration order;
4. prove that Eq.(5)/(6) survives the non-transverse correlated K4/K5 boundary value/pullback, not merely the independent-edge pre-pullback tensor product;
5. only after those steps may a K5 direct causal-vertex construction be qualified.

This remains `BLOCKED`, not a theorem of physical vertex divergence or nonexistence.

## Historical distributional localization retained

- Iter039: `S5_SYMMETRY_ONLY_EXTENSION_UNIQUE_THROUGH_16 = FALSE`; first non-unique invariant degree 4.
- Iter040: primitive S5 extension directions begin at degree 4.
- Iter041: complete K5 all-delta sector has superficial extension degree `omega=6`.
- Iter042: Appendix-D edge-local source span strongly reduces but does not uniquely select the primitive extension ambiguity.
- Iter044: source-faithful joint finite-spectral-`i epsilon` K3 kernel has a common-cycle polynomial obstruction.
- Iter045: exact correlated finite part is coordinate-covariant on held-out K3 data and is a viable K3 candidate extension only.
- Iter046: the corresponding sequential one-dimensional K4 rule is order/forest dependent; preferred order/tree is forbidden.
- Iter058: exact K4 strict-chamber feasibility iff strong tournament connectivity.
- Iter059: source-backed equal-spin Toller wedge reversal gives branch swap under group inversion.
- Iter060: K4 tournament/positive-circulation analyticity surrogate is covariant under that reversal law.
- Iter061: orientation-blind identification of physical kappa with ordered spectral sign is obstructed.
- Iter062: minimal ordered bridge `s(a,b)=c eta(a,b) kappa_ab` is covariant but has an unfixed global convention.

## Next admissible step

Consume Iter070A raw artifacts and frozen aggregate when terminal. If it passes, the next physics-critical gate is a prospectively frozen **correlated epsilon-to-zero tempered-distribution boundary-value qualification**, using the source-defined finite-spectral family and held-out Schwartz test functions, with basis/permutation/order covariance controls and no fitted subtraction. Iter070C may be used only as a pre-pullback Eq.(5)/(6) control; it cannot substitute for the correlated collision gate.

Do not return to ordinary improper real-cycle integration or a preferred sequential finite part: Iter069 and Iter046 have already closed those routes for the reduced K4 family.

## Claim locks

- no `NEW_PHYSICS_FOUND` or complete-QG claim;
- no physical causal-vertex finiteness/divergence theorem;
- no universal causal-EPRL or contour no-go theorem;
- no physical causal-sector selection from tournament or microlocal-skeleton results;
- no G3 PASS or F9/G8 promotion;
- no arbitrary counterterm, fitted cancellation coefficient, or preferred sequential order/tree;
- do not replace the published spectral `i epsilon` prescription with `beta+i epsilon`;
- keep ordinary/absolute integrability, conditional/PV finite part, fixed-epsilon tempered distribution, source-defined distributional boundary value, and microlocal product existence distinct.
