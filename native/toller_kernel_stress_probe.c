#include "toller_kernel.h"

#include <complex.h>
#include <stdio.h>

int main(void) {
    puts("two_j\ttwo_l\ttwo_m\tgamma\tbeta\ttp_re\ttp_im\ttm_re\ttm_im");
    const long double gammas[] = {0.1L, 0.4L, 1.0L, 1.2L};
    const long double betas[] = {0.1L, 0.2L, 0.4L, 0.8L};
    for (int tj = 1; tj <= 4; ++tj) {
        int tk = tj;
        long double j = 0.5L * (long double)tj;
        for (int dl = 0; dl <= 4; ++dl) {
            int tl = tj + 2 * dl;
            for (int tm = -tj; tm <= tj; tm += 2) {
                for (int ig = 0; ig < 4; ++ig) {
                    long double gamma = gammas[ig];
                    long double rho = gamma * j;
                    for (int ib = 0; ib < 4; ++ib) {
                        long double beta = betas[ib];
                        long double complex tp = msqgr_toller_plus(tj, tl, tm, tk, rho, beta);
                        long double complex tmin = msqgr_toller_minus(tj, tl, tm, tk, rho, beta);
                        printf("%d\t%d\t%d\t%.18Lg\t%.18Lg\t%.21Lg\t%.21Lg\t%.21Lg\t%.21Lg\n",
                               tj, tl, tm, gamma, beta,
                               creall(tp), cimagl(tp), creall(tmin), cimagl(tmin));
                    }
                }
            }
        }
    }
    return 0;
}
