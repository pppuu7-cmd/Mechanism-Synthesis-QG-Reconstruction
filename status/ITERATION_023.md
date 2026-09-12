# Iteration 023 — Collision scaling of summed causal sectors

Status: **COMPLETED / NO MULTI-COLLISION SOFTENING FROM CAUSAL-SECTOR SUMS**

Workflow: `Causal Sector Sum Collision Power`

- 6/6 GitHub jobs completed successfully.
- gamma = 0.2, 1.2, 2.0; seeds 17 and 41.
- collision clusters k = 2,3,4,5.
- compared the 16 inequivalent factorized causal structures `Cplus16`, their co-causal partners `Cminus16`, the combined `Cboth32`, a fixed all-plus causal structure, and EPRL control.

## Aggregate result

The causal-sector sums do **not** remove the multi-collision pole powers found in Iteration 022.

### k = 2

`Cboth32` slope range: **-2.01145 ... -1.99064**.

All 6/6 first-moment classifications PASS; ordinary second moment remains FAIL.

### k = 3

`Cboth32` slope range: **-6.02699 ... -5.95477**.

All 6/6 classifications remain `BORDERLINE_LOG`; the causal plus/co-causal sum does not remove the logarithmic boundary.

### k = 4

`Cboth32` slope range: **-11.98451 ... -11.93956**.

All 6/6 first-moment classifications FAIL.

### k = 5

`Cboth32` slope range: **-19.99929 ... -19.94116**.

All 6/6 first-moment classifications FAIL.

The separate `Cplus16` and `Cminus16` ranges track the same powers. EPRL remains regular in every run, with slopes close to zero and both first/second moments classified PASS.

## Interpretation

The leading Toller residues do not cancel merely by summing the 16 factorized causal structures or by adding their co-causal partners. Therefore the finiteness issue cannot be solved by a simple causal-sector sum at the level of the tested magnetic-basis carrier.

This is not yet a final divergence verdict for the physical vertex, because the physical boundary spin-network state contracts all boundary magnetic indices with intertwiners, and the Toller matrices are distributions defined by a Feynman `i epsilon` prescription. Those two structures have not yet been included in the multi-collision power test.

## Next target

Iteration 024 performs the complete `j=1/2` five-node boundary-intertwiner contraction **before** measuring multi-collision powers. If the same k=3/4/5 powers survive, the remaining physically plausible rescue mechanism is the genuinely distributional `i epsilon` integration / boundary-of-region contribution rather than ordinary-function cancellation.
