/* Drive sl2cfoam_b4_accurate for one fresh Toller branch mask while the
 * patched upstream implementation dumps the full complex QAGP tensor before
 * its ordinary-EPRL real projection.  The real B4 matrix is printed too, but
 * the complex integral dump is the authoritative branch-resolved object.
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "sl2cfoam.h"
#include "common.h"

static void prepare_dump(const char *dir, const char *label, const char *name) {
    char path[1024];
    snprintf(path, sizeof(path), "%s/integrals_%s_%s.tsv", dir, label, name);
    FILE *f = fopen(path, "w");
    if (!f) { perror("fopen branch dump"); exit(3); }
    fprintf(f, "two_p1\ttwo_p2\ttwo_p3\ttwo_p4\tre\tim\tabserr\trcode\n");
    fclose(f);
    setenv("MSQGR_BRANCH_DUMP", path, 1);
}

static void run_case(const char *dir, const char *label, const char *name, dspin tj, dspin tl) {
    dspin imin = 0, imax = 2 * tj;
    dspin kmin = 0, kmax = 2 * tl;
    int dimi = DIV2(imax - imin) + 1;
    prepare_dump(dir, label, name);
    sl2cfoam_dmatrix b = sl2cfoam_b4_accurate(
        tj,tj,tj,tj, tl,tl,tl,tl, imin,imax,kmin,kmax);
    for (dspin ti=imin; ti<=imax; ti+=2) {
        for (dspin tk=kmin; tk<=kmax; tk+=2) {
            double v = matrix_get(b, dimi, DIV2(ti-imin), DIV2(tk-kmin));
            printf("%s\t%s\t%d\t%d\t%d\t%d\t%.17g\n",
                   label,name,(int)tj,(int)tl,(int)ti,(int)tk,v);
        }
    }
    free(b);
}

int main(int argc, char **argv) {
    if (argc < 4) {
        fprintf(stderr, "usage: %s DATA_ROOT DUMP_DIR LABEL [MASK]\n", argv[0]);
        return 2;
    }
    char *data = argv[1];
    const char *dir = argv[2];
    const char *label = argv[3];
    if (argc >= 5) setenv("MSQGR_TOLLER_MASK", argv[4], 1);

    struct sl2cfoam_config conf;
    conf.verbosity = SL2CFOAM_VERBOSE_OFF;
    conf.accuracy = SL2CFOAM_ACCURACY_NORMAL;
    conf.max_two_spin = 20;
    conf.max_MB_mem_per_thread = 0;
    sl2cfoam_init_conf(data, 1.2, &conf);

    printf("label\tcase\ttwo_j\ttwo_l\ttwo_i\ttwo_k\tvalue\n");
    run_case(dir,label,"jhalf_lhalf",1,1);
    run_case(dir,label,"jhalf_lthreehalf",1,3);

    sl2cfoam_free();
    return 0;
}
