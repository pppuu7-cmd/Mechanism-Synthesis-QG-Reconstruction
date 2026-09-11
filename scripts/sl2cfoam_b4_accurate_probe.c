/* Small-spin accurate B4 probe used to compare the unmodified upstream
 * integrand with the additive Toller reconstruction t+ + t-.
 */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "sl2cfoam.h"
#include "common.h"

static void run_case(const char *name, dspin tj, dspin tl) {
    dspin imin = 0;
    dspin imax = 2 * tj;
    dspin kmin = 0;
    dspin kmax = 2 * tl;
    int dimi = DIV2(imax - imin) + 1;
    int dimk = DIV2(kmax - kmin) + 1;

    sl2cfoam_dmatrix b = sl2cfoam_b4_accurate(
        tj,tj,tj,tj, tl,tl,tl,tl,
        imin,imax,kmin,kmax);

    for (dspin ti=imin; ti<=imax; ti+=2) {
        for (dspin tk=kmin; tk<=kmax; tk+=2) {
            double v = matrix_get(b, dimi, DIV2(ti-imin), DIV2(tk-kmin));
            printf("%s\t%d\t%d\t%d\t%d\t%.17g\n",
                   name,(int)tj,(int)tl,(int)ti,(int)tk,v);
        }
    }
    free(b);
    (void)dimk;
}

int main(int argc, char **argv) {
    const char *data = argc > 1 ? argv[1] : "data_sl2cfoam";
    struct sl2cfoam_config conf;
    conf.verbosity = SL2CFOAM_VERBOSE_OFF;
    conf.accuracy = SL2CFOAM_ACCURACY_NORMAL;
    conf.max_two_spin = 20;
    conf.max_MB_mem_per_thread = 0;
    sl2cfoam_init_conf(data, 1.2, &conf);

    printf("case\ttwo_j\ttwo_l\ttwo_i\ttwo_k\tvalue\n");
    run_case("jhalf_lhalf", 1, 1);
    run_case("jhalf_lthreehalf", 1, 3);

    sl2cfoam_free();
    return 0;
}
