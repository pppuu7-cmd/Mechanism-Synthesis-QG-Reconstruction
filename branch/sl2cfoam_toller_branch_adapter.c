#include "sl2cfoam_toller_branch_adapter.h"
#include "toller_kernel.h"

#include <complex.h>
#include <math.h>
#include <quadmath.h>
#include <stdlib.h>

void msqgr_toller_dsmall_branch(__complex128 ds[], __float128 xs[], size_t N,
                                double rho, dspin two_k, dspin two_j,
                                dspin two_l, dspin two_p, int branch)
{
    for (size_t i = 0; i < N; ++i) {
        long double beta = -logl((long double)xs[i]);
        long double complex t;
        if (branch > 0) {
            t = msqgr_toller_plus((int)two_j, (int)two_l, (int)two_p,
                                  (int)two_k, (long double)rho, beta);
        } else {
            t = msqgr_toller_minus((int)two_j, (int)two_l, (int)two_p,
                                   (int)two_k, (long double)rho, beta);
        }
        __complex128 q;
        __real__ q = (__float128)creall(t);
        __imag__ q = (__float128)cimagl(t);
        ds[i] = q;
    }
}

int msqgr_toller_branch_for_leg(int leg)
{
    static int initialized = 0;
    static int mask = 0;
    if (!initialized) {
        const char *s = getenv("MSQGR_TOLLER_MASK");
        mask = s ? atoi(s) : 0;
        if (mask < 0) mask = 0;
        if (mask > 15) mask = 15;
        initialized = 1;
    }
    return (mask & (1 << leg)) ? +1 : -1;
}
