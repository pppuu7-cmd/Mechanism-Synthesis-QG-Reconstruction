#include "toller_kernel.h"

#include <math.h>
#include <stddef.h>

static int imax(int a, int b) { return a > b ? a : b; }
static int imin(int a, int b) { return a < b ? a : b; }

static long double facti(int n) {
    if (n < 0) return 0.0L;
    long double r = 1.0L;
    for (int k = 2; k <= n; ++k) r *= (long double)k;
    return r;
}

static long double binomi(int n, int r) {
    if (r < 0 || r > n || n < 0) return 0.0L;
    if (r > n - r) r = n - r;
    long double v = 1.0L;
    for (int k = 1; k <= r; ++k) {
        v *= (long double)(n - r + k) / (long double)k;
    }
    return v;
}

static long double sign_int(int n) { return (n & 1) ? -1.0L : 1.0L; }

/* Gamma(B+d)/Gamma(B) for integer d, evaluated only by recurrence. */
static long double complex gamma_ratio_integer_shift(long double complex B, int d) {
    long double complex r = 1.0L + 0.0Li;
    if (d > 0) {
        for (int q = 0; q < d; ++q) r *= B + (long double)q;
    } else if (d < 0) {
        for (int q = 1; q <= -d; ++q) r /= B - (long double)q;
    }
    return r;
}

/* Direct Gauss series on 0 <= z < 1. */
static long double complex h2f1_unitdisk(
    long double a,
    long double complex b,
    long double complex c,
    long double z)
{
    const long double tol = 2.0e-18L;
    const int max_terms = 200000;
    long double complex term = 1.0L + 0.0Li;
    long double complex sum = term;
    for (int n = 1; n <= max_terms; ++n) {
        long double nn = (long double)n;
        term *= ((a + nn - 1.0L) * (b + nn - 1.0L) /
                 ((c + nn - 1.0L) * nn)) * z;
        long double complex next = sum + term;
        if (cabsl(term) < tol * fmaxl(1.0L, cabsl(next))) return next;
        sum = next;
    }
    return NAN + NAN * I;
}

static long double prefactor(int tj, int tl, int tm, int tk) {
    int jmk = (tj - tk) / 2;
    int jpk = (tj + tk) / 2;
    int lmk = (tl - tk) / 2;
    int lpk = (tl + tk) / 2;
    int jmm = (tj - tm) / 2;
    int jpm = (tj + tm) / 2;
    int lmm = (tl - tm) / 2;
    int lpm = (tl + tm) / 2;
    long double num = facti(jmk) * facti(jpk) * facti(lmk) * facti(lpk);
    long double den = facti(jmm) * facti(jpm) * facti(lmm) * facti(lpm);
    return sqrtl((1.0L + (long double)tj) * (1.0L + (long double)tl)) * sqrtl(num / den);
}

long double complex msqgr_toller_plus(
    int tj, int tl, int tm, int tk,
    long double rho, long double beta)
{
    long double z = expl(-2.0L * beta);
    long double P = prefactor(tj, tl, tm, tk);
    long double complex total = 0.0L + 0.0Li;

    int mkp = (tm + tk) / 2;
    int a1 = imax(0, mkp);
    int b1 = imin((tj + tm) / 2, (tj + tk) / 2);
    int a2 = imax(0, mkp);
    int b2 = imin((tl + tm) / 2, (tl + tk) / 2);

    long double j = 0.5L * (long double)tj;
    long double l = 0.5L * (long double)tl;
    long double complex Bgamma = (1.0L + j) + I * rho;

    for (int n1 = a1; n1 <= b1; ++n1) {
        for (int n2 = a2; n2 <= b2; ++n2) {
            int dgamma = (tk + tm) / 2 - n1 - n2 - 1;
            long double complex q = gamma_ratio_integer_shift(Bgamma, dgamma);

            q *= facti(-(tk + tm) / 2 + n1 + n2);
            q *= binomi((tj - tm) / 2, -(tk + tm) / 2 + n1);
            q *= binomi((tl - tm) / 2, -(tk + tm) / 2 + n2);
            q *= binomi((tj + tm) / 2, n1);
            q *= binomi((tl + tm) / 2, n2);
            q *= sign_int((tj - tl) / 2 + n1 + n2);

            long double er = -1.0L + 0.5L * (long double)(tk + tm) - 2.0L * (long double)n2;
            q *= cexpl(beta * (er + I * rho));

            long double a = 1.0L - 0.5L * (long double)(tk + tm) + (long double)(n1 + n2);
            long double complex b = (1.0L + l) - I * rho;
            long double complex c =
                (1.0L - 0.5L * (long double)(tj + tk + tm) + (long double)(n1 + n2)) - I * rho;
            q *= h2f1_unitdisk(a, b, c, z);
            total += q;
        }
    }
    return P * total;
}

long double complex msqgr_toller_minus(
    int tj, int tl, int tm, int tk,
    long double rho, long double beta)
{
    long double z = expl(-2.0L * beta);
    long double P = prefactor(tj, tl, tm, tk);
    long double complex total = 0.0L + 0.0Li;

    int mmk = (tm - tk) / 2;
    int a1 = imax(0, mmk);
    int b1 = imin((tl + tm) / 2, (tl - tk) / 2);
    int a2 = imax(0, mmk);
    int b2 = imin((tj + tm) / 2, (tj - tk) / 2);

    long double j = 0.5L * (long double)tj;
    long double l = 0.5L * (long double)tl;
    long double complex Bgamma = (1.0L + l) - I * rho;

    for (int n1 = a1; n1 <= b1; ++n1) {
        for (int n2 = a2; n2 <= b2; ++n2) {
            int dgamma = (-tk + tm) / 2 - n1 - n2 - 1;
            long double complex q = gamma_ratio_integer_shift(Bgamma, dgamma);

            q *= facti((tk - tm) / 2 + n1 + n2);
            q *= binomi((tl - tm) / 2, (tk - tm) / 2 + n1);
            q *= binomi((tj - tm) / 2, (tk - tm) / 2 + n2);
            q *= binomi((tl + tm) / 2, n1);
            q *= binomi((tj + tm) / 2, n2);
            q *= sign_int(n1 + n2);

            long double er = -1.0L + 0.5L * (long double)(-tk + tm) - 2.0L * (long double)n2;
            q *= cexpl(beta * (er - I * rho));

            long double a = 1.0L + 0.5L * (long double)(tk - tm) + (long double)(n1 + n2);
            long double complex b = (1.0L + j) + I * rho;
            long double complex c =
                (1.0L - l + 0.5L * (long double)(tk - tm) + (long double)(n1 + n2)) + I * rho;
            q *= h2f1_unitdisk(a, b, c, z);
            total += q;
        }
    }
    return P * total;
}
