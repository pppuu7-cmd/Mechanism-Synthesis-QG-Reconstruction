# Dependency reconciliation after Iter077Q right-SU(2) source-lock invalidation

Date: 2026-09-14
Controlling correction: `results/ITER077Q_ADVERSARIAL_RIGHT_SU2_SOURCE_LOCK_REVIEW.md`, commit `c0ae0ef208a3eccef4ece7960cdf5337e7d5fa2e`, verdict `INVALID_SOURCE_LOCK`.
Repair authority: `results/ITER081R_SM_RIGHT_SU2_S5_INVARIANT_JET_CLASSIFICATION_RESULT.md`, commit `5fe42e766aab2660b36c654502a029930db28890`.
Repaired consequences: `results/ITER081S_CRITIC_REPAIRED_SELECTOR_CONSEQUENCES.md`, commit `8c2fc23084e89c39f624853ac0d445e3103850d1`.

## Controlling repaired fact
Historical Iter077Q's mathematical family `{Q^n F delta_N}` is linearly independent but is not source-compatible because `Q` violates the exact node-wise compact gauge symmetry of the fully boundary-contracted source object.

The corrected scalar source-symmetry-compatible normal-jet lower bound through order 8 is finite-dimensional:

`d_k=(1,0,1,0,3,0,7,0,16)`, total `28`.

This is a lower-bound subspace, not the exact total extension-space dimension.

## Historical dependency statuses

### Iter077Q
**Status:** `INVALID_SOURCE_LOCK` as a physical/source-compatible infinite-dimensional ambiguity theorem.

Retain only the narrower algebraic linear-independence theorem for the non-source-compatible multipliers. Do not use `W=span{Q^nFdelta_N}` as physical authority.

### Iter080A — finite K5 permutation covariance
**Status:** `QUALIFIED` / historical infinite-dimensional witness superseded.

The specific nonconstant tangential multiplier used by Iter080A has the same omitted right-SU(2) defect. Its claim of an infinite-dimensional source-compatible S5-invariant tangential sector is not authoritative. However the qualitative conclusion `S5 covariance alone does not uniquely select` is repaired independently and more physically by Iter081R: the corrected space already imposes S5 and still contains at least 28 scalar invariant jets.

### Iter080D — every fixed finite scalar-linear selector family fails
**Status:** `INVALID_SOURCE_LOCK` for physical application to the K5 ambiguity.

Its rank-nullity theorem is mathematically correct conditional on an infinite-dimensional vector space `W`, but that source-compatible premise is invalid. In the repaired scalar subspace, only `m<28` conditions are guaranteed insufficient; `m>=28` may be injective algebraically. Do not cite Iter080D as a universal finite-condition no-go for the physical K5 extension problem.

### Iter080E — frozen BCG/Beltran source-selector census
**Status:** `QUALIFIED`.

The target phrase `selector acting on full Iter077Q W` is obsolete. The source audit nevertheless retains the narrower conclusion that the frozen BCG/Beltran corpus contains no explicit correlated joint-K5 boundary-value/extension prescription satisfying the P1-P5 completeness requirements. Right-SU(2) covariance is an exact source constraint, but Iter081R proves it is not a complete selector: 28 scalar invariant jet directions survive.

### Iter080H — pre-Iter077Q CRQN v0.1/v0.2 selector census
**Status:** `REQUIRES_NEW_PREREGISTERED_GATE` before reuse as a theorem about the corrected ambiguity.

A2/A3 were explicitly frozen against the old infinite `W`/arbitrary extension-function target. The exhaustive corpus work remains useful evidence, but its selector-completeness verdict must not be transferred automatically to the repaired normal-jet coefficient problem. A corrected candidate-corpus census must target the 28-dimensional scalar jet lower bound / complete right-SU2-covariant jet space.

### Iter080I — current-candidate local-amplitude survival decision
**Status:** historical dependency proof `INVALID_SOURCE_LOCK`; present high-level conclusion independently re-established.

The historical gate materially consumed Iter077Q and Iter080D as authorities, so its exact dependency proof is no longer valid. However `BLOCKED_CURRENT_CANDIDATE_LOCAL_AMPLITUDE` remains correct after Iter081R because at least 28 source-symmetry-compatible scalar jet coefficients remain unselected. Cite Iter081R/S, not the old infinite-W dependency chain, for the current blocker.

### Iter080J — ordinary conormal/WF admissibility alone
**Status:** `QUALIFIED`, qualitative conclusion repaired.

The historical `Q^n` witnesses are not source-compatible. Nevertheless every invariant normal derivative of `delta_N` counted by Iter081R has support on `N` and wavefront contained in `N^*N\0`. Thus weak support+conormal/WF admissibility still leaves at least 28 scalar source-compatible directions and is not a unique selector. Cite Iter081S for the repaired conclusion.

### Iter081I — causal eta=+ sum retains infinite-dimensional ambiguity
**Status:** `INVALID_SOURCE_LOCK` for the infinite-dimensional statement; qualitative nonselection repaired.

The old surviving `Q^n` family is invalid. However the source-defined causal orientation sum changes only the off-collision finite combination and does not assign values to distributions supported on `N`. The 28-dimensional invariant scalar jet lower bound can still be added to a causal-summed extension without changing the off-collision causal object. Cite Iter081S for the repaired `>=28` persistence statement.

### Iter080K
Historical `INVALID_PROVENANCE` remains unchanged.

## Results unaffected by the Iter077Q correction
The following do not require the invalid tangential family and remain in their established scopes:

- Iter077I minimal all-j=1/2 source-ordered common-collision non-L1 obstruction;
- Iter077K one-wedge i-epsilon not a correlated joint-K5 boundary value;
- Iter077L scaling degree 20 / codimension 12 / normal derivative order <=8 extension theorem;
- Iter077M nonzero order-zero compact-boundary `F_SU2 delta_N` ambiguity;
- Iter080B causal E3/E4/E6 source-bridge obstruction;
- Iter081B direct Han/Toller source-inheritance blocker;
- Iter081E actual selected-Toller Han-bound counterexamples;
- Iter081G/H/K/L/M causal orientation-sum leading-sign/noncancellation results, insofar as they rely on Iter077I rather than Iter077Q;
- Iter081N/O/P generic-spin one-wedge/full-block/uncontracted carrier sign theorems, within their stated pre-boundary scopes.

## New controlling local chain
`source-ordered K5 non-L1 (Iter077I)`
`-> sd20/codim12 extension freedom (Iter077L)`
`-> nonzero constant ambiguity (Iter077M)`
`-> old infinite tangential W INVALID_SOURCE_LOCK (Iter077Q re-review)`
`-> exact node-wise compact gauge quotient`
`-> >=28-dimensional SO(3)xS5 invariant scalar normal-jet ambiguity (Iter081R)`
`-> coefficient selector / correlated boundary value ?`.

## Operational rule
Any future gate that references `full W`, `infinite-dimensional tangential ambiguity`, `Q^nFdelta_N` as source-compatible, or the universal Iter080D finite-condition obstruction is stale and must stop/recover before execution.

Use the corrected blocker:

`RIGHT_SU2_COVARIANT_K5_INVARIANT_NORMAL_JET_COEFFICIENT_SELECTOR`.
