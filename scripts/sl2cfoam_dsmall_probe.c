/* Pointwise probe of the upstream sl2cfoam reduced Wigner d-matrix.
 * Built only inside the physical-backend workflow against an unmodified
 * sl2cfoam-next checkout.  Outputs TSV rows for phase-convention comparison.
 */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <quadmath.h>
#include <complex.h>
#include <mpc.h>
#include "common.h"
#include "dsmall.h"

typedef struct { int tj, tl, tp; double gamma, beta; } probe_case;

static void one(const probe_case *c) {
    const int two_j=c->tj, two_l=c->tl, two_p=c->tp;
    const double j=0.5*(double)two_j;
    const double rho=c->gamma*j;
    const int Jmp=abs(two_j-two_p)/2;
    const int Jpp=abs(two_j+two_p)/2;
    const int m_max=(two_j+two_l)/2-Jmp;
    const int n_max=(two_j+two_l)/2-Jpp;
    const int precision=192;
    mpc_ptr *Ym=calloc((size_t)m_max+1,sizeof(mpc_ptr));
    mpc_ptr *Yn=calloc((size_t)n_max+1,sizeof(mpc_ptr));
    if(!Ym||!Yn){fprintf(stderr,"alloc failed\n");exit(2);}
    for(int m=0;m<=m_max;m++){Ym[m]=malloc(sizeof(mpc_t));mpc_init2(Ym[m],precision);}
    for(int n=0;n<=n_max;n++){Yn[n]=malloc(sizeof(mpc_t));mpc_init2(Yn[n],precision);}
    sl2cfoam_dsmall_Yc(Ym,precision, rho,two_j,two_l,two_j, two_p);
    sl2cfoam_dsmall_Yc(Yn,precision,-rho,two_j,two_j,two_l,-two_p);
    __float128 x[1]; __complex128 d[1];
    x[0]=expq(-(__float128)c->beta);
    sl2cfoam_dsmall(d,x,1,precision,Ym,Yn,NULL,rho,two_j,two_j,two_l,two_p);
    printf("%d\t%d\t%d\t%.17g\t%.17g\t%.17g\t%.17g\n",two_j,two_l,two_p,c->gamma,c->beta,(double)crealq(d[0]),(double)cimagq(d[0]));
    for(int m=0;m<=m_max;m++){mpc_clear(Ym[m]);free(Ym[m]);}
    for(int n=0;n<=n_max;n++){mpc_clear(Yn[n]);free(Yn[n]);}
    free(Ym);free(Yn);
}

int main(void){
    probe_case cs[]={
      {1,1, 1,1.2,0.3},{1,1,-1,1.2,0.8},
      {1,3, 1,1.2,0.3},{1,3,-1,1.2,0.8},
      {1,5, 1,1.2,0.8},{1,5,-1,0.4,1.7},
      {2,2, 0,1.2,0.3},{2,4, 0,1.2,0.8},
      {2,4, 2,0.4,1.7},{2,6,-2,1.2,0.8}
    };
    printf("two_j\ttwo_l\ttwo_m\tgamma\tbeta\tre\tim\n");
    for(size_t i=0;i<sizeof(cs)/sizeof(cs[0]);i++) one(&cs[i]);
    return 0;
}
