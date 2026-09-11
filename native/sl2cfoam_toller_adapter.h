#ifndef MSQGR_SL2CFOAM_TOLLER_ADAPTER_H
#define MSQGR_SL2CFOAM_TOLLER_ADAPTER_H

#include <quadmath.h>
#include "common.h"

/* Drop-in additive Toller reconstruction for the raw sl2cfoam dsmall layer.
 * Returns t+ + t- in Ruhl convention.  The normal booster-level Speziale phase
 * must remain downstream exactly where upstream b4_qagp.c applies it.
 */
void msqgr_toller_dsmall_sum(__complex128 ds[], __float128 xs[], size_t N,
                             double rho, dspin two_k, dspin two_j,
                             dspin two_l, dspin two_p);

#endif
