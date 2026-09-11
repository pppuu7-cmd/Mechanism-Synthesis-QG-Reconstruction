#include "sl2cfoam_toller_adapter.h"
#include "toller_kernel.h"

#include <complex.h>
#include <math.h>
#include <quadmath.h>

void msqgr_toller_dsmall_sum(__complex128 ds[], __float128 xs[], size_t N,
                             double rho, dspin two_k, dspin two_j,
                             dspin two_l, dspin two_p)
{
    for (size_t i = 0; i < N; ++i) {
        long double beta = -logl((long double)xs[i]);
        long double complex tp = msqgr_toller_plus(
            (int)two_j, (int)two_l, (int)two_p, (int)two_k,
            (long double)rho, beta);
        long double complex tm = msqgr_toller_minus(
            (int)two_j, (int)two_l, (int)two_p, (int)two_k,
            (long double)rho, beta);
        long double complex s = tp + tm;
        __complex128 q;
        __real__ q = (__float128)creall(s);
        __imag__ q = (__float128)cimagl(s);
        ds[i] = q;
    }
}
