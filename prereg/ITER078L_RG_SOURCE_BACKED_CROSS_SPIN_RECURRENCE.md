# Iter078L-RG preregistration — is there a source-backed exact cross-spin recurrence that can select the finite-spin extension?

**Date:** 2026-09-14

## Scientific question

Iter078K proves that the published large-spin asymptotic theorem does not determine the exact all-`j=1/2` extension. A stronger exact selector could exist if the causal-Toller construction satisfied a source-backed recurrence/difference equation relating physical vertex amplitudes at different boundary spins.

Does the frozen primary/companion source actually provide such a cross-spin law?

## Frozen source authority

1. Bianchi-Chen-Gamonal, *Causal spinfoam vertex for 4d Lorentzian quantum gravity*, arXiv:2601.23162.
2. Bianchi-Chen-Gamonal, *Toller matrices and the Feynman i epsilon in spinfoams*, arXiv:2604.24945.

## Required law

A qualifying selector must relate the **physical gamma-simple causal vertex** at different boundary-spin assignments. It must be an exact identity of the form schematically

`sum_r C_r(j,...) A_causal(j + Delta_r, ...) = 0`

or an equivalent exact transfer/recurrence, with coefficients and domain fixed independently of the unresolved K5 extension.

It must be strong enough that a finite-support change in the all-`j=1/2` sector is not automatically invisible.

## Invalid substitutes

The following do not qualify by themselves:

- the fixed-spin wedge identity `T+ + T- = D`;
- uniqueness of Toller splitting in the complex continuous representation parameter `rho` at fixed matrix labels;
- SU(2) recoupling identities that only change intertwiner bases within one spin sector;
- hypergeometric contiguous relations for a single reduced matrix element unless they are explicitly shown to induce an exact relation among the gamma-simple full K5 vertex amplitudes, including the source ordering and distributional extension;
- large-spin saddle asymptotics;
- a recurrence valid only for the EPRL sum over all wedge-sign sectors.

## Frozen audit

Search the two source papers for:

- recurrence / recursion / difference equation;
- contiguous relations used as physical spin recurrences;
- exact relations shifting `j_ab`;
- representation-theoretic ladder identities claimed to constrain the causal vertex across spin sectors;
- a transfer equation connecting finite spin to the asymptotic regime.

For every candidate, record whether it acts on:

1. one reduced Toller matrix;
2. representation labels at fixed physical spin;
3. SU(2) basis indices;
4. the full gamma-simple K5 causal vertex.

## PASS

PASS iff a frozen source law satisfying the required physical cross-spin scope is found and its hypotheses are sufficient to test the Iter078K finite-support ambiguity.

Classification:
`ITER078L_RG_SOURCE_BACKED_EXACT_CROSS_SPIN_CAUSAL_VERTEX_RECURRENCE_FOUND_SELECTOR_GATE_OPEN`.

## BLOCKED / negative audit

If no such law is supplied by the frozen sources:

`ITER078L_RG_NO_SOURCE_BACKED_EXACT_CROSS_SPIN_CAUSAL_VERTEX_RECURRENCE_FINITE_SPIN_SELECTOR_UNAVAILABLE`

Verdict `BLOCKED_SELECTOR_NOT_IN_SOURCE`.

This is not a proof that no recurrence can be derived mathematically. It means any new recurrence derivation is new structure and must be prospectively validated on the full source-ordered K5 object before it can act as a selector.

## Interpretation ceiling

No statement about the existence/nonexistence of all possible hypergeometric or representation-theoretic recurrences outside the frozen source. No RG fixed point, unique extension or complete-QG claim.