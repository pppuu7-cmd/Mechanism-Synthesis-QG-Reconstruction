#ifndef MSQGR_TOLLER_KERNEL_H
#define MSQGR_TOLLER_KERNEL_H

#include <complex.h>

/*
 * Standalone long-double implementation of the general Lorentzian Toller
 * split in Ruhl phase convention.  Spins are supplied doubled (2j,2l,2m,2k)
 * so all combinatorial bounds remain exact integers.
 *
 * This is a validation kernel, not yet wired into sl2cfoam boosters.
 */
long double complex msqgr_toller_plus(
    int two_j, int two_l, int two_m, int two_k,
    long double rho, long double beta);

long double complex msqgr_toller_minus(
    int two_j, int two_l, int two_m, int two_k,
    long double rho, long double beta);

#endif
