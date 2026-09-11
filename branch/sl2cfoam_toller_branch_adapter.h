#ifndef MSQGR_SL2CFOAM_TOLLER_BRANCH_ADAPTER_H
#define MSQGR_SL2CFOAM_TOLLER_BRANCH_ADAPTER_H

#include <quadmath.h>
#include "common.h"

/* Return one analytic Toller branch for a raw reduced-Wigner dsmall leg.
 * branch > 0 selects t^(+), branch < 0 selects t^(-).
 * All values are in the same Ruhl convention as upstream sl2cfoam_dsmall.
 */
void msqgr_toller_dsmall_branch(__complex128 ds[], __float128 xs[], size_t N,
                                double rho, dspin two_k, dspin two_j,
                                dspin two_l, dspin two_p, int branch);

/* Four-bit branch mask used by a B4 integrand. Bit leg=1 -> plus, 0 -> minus.
 * The mask is read once from MSQGR_TOLLER_MASK in each fresh probe process.
 */
int msqgr_toller_branch_for_leg(int leg);

#endif
