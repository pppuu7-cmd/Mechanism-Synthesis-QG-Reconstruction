#!/usr/bin/env bash
# Build one clean sl2cfoam-next checkout, instrument the complex QAGP tensor,
# and either compute the ordinary baseline or four of the 16 Toller branch masks.
set -u
MODE="${1:-}"
ROOT="${GITHUB_WORKSPACE:-$PWD}"
OUT="$ROOT/results"
mkdir -p "$OUT"
WORK="${RUNNER_TEMP:-/tmp}/msqgr-branch-b4-${MODE}"
rm -rf "$WORK"; mkdir -p "$WORK"; cd "$WORK"

STAGE=init; DETAIL=""; COMPLETED=0
finish(){
  MSQGR_ROOT="$ROOT" python3 - "$MODE" "$STAGE" "$DETAIL" "$COMPLETED" <<'PY'
import json,os,sys
mode,stage,detail,n=sys.argv[1:]
out={"mode":mode,"stage_reached":stage,"detail":detail,"completed_probe_processes":int(n),"scope":"complex branch-resolved accurate-B4 integration building block; not yet a full causal vertex or F9"}
root=os.environ.get('MSQGR_ROOT','.')
os.makedirs(os.path.join(root,'results'),exist_ok=True)
open(os.path.join(root,'results',f'branch_b4_status_{mode}.json'),'w').write(json.dumps(out,indent=2))
print(json.dumps(out,indent=2))
PY
}
trap finish EXIT

STAGE=apt
sudo apt-get update -qq || { DETAIL="apt update failed"; exit 0; }
sudo apt-get install -y -qq git curl build-essential libgmp-dev libmpfr-dev libmpc-dev libgsl-dev libopenblas-dev libomp-dev gfortran || { DETAIL="dependency install failed"; exit 0; }

STAGE=clone
git clone --depth 1 https://github.com/qg-cpt-marseille/sl2cfoam-next.git || { DETAIL="clone failed"; exit 0; }
cd sl2cfoam-next
mkdir -p ext; cd ext
curl -fsSL -o wigxjpf.tar.gz https://fy.chalmers.se/subatom/wigxjpf/wigxjpf-1.13.tar.gz || { DETAIL="wigxjpf download failed"; exit 0; }
tar -xzf wigxjpf.tar.gz; mv wigxjpf-1.13 wigxjpf
make -C wigxjpf -j2 || { DETAIL="wigxjpf build failed"; exit 0; }
curl -fsSL -o fastwigxj.tar.gz https://fy.chalmers.se/subatom/fastwigxj/fastwigxj-1.4.1.tar.gz || { DETAIL="fastwigxj download failed"; exit 0; }
tar -xzf fastwigxj.tar.gz; mv fastwigxj-1.4.1 fastwigxj
make -C fastwigxj -j2 || { DETAIL="fastwigxj build failed"; exit 0; }
cd ..

STAGE=instrument
python3 - "$MODE" <<'PY'
from pathlib import Path
import sys
mode=sys.argv[1]
p=Path('src/b4_qagp.c');s=p.read_text()
if '#include <stdio.h>' not in s:
    s=s.replace('#include <math.h>','#include <math.h>\n#include <stdio.h>\n#include <stdlib.h>',1)
anchor='        __complex128 integ_p = res_qagp * phase_p;\n'
logger=r'''
        const char *msqgr_dump = getenv("MSQGR_BRANCH_DUMP");
        if (msqgr_dump && *msqgr_dump) {
            FILE *msqgr_fp = fopen(msqgr_dump, "a");
            if (msqgr_fp) {
                char msqgr_re[96], msqgr_im[96], msqgr_err[96];
                quadmath_snprintf(msqgr_re, sizeof(msqgr_re), "%.36Qg", crealq(integ_p));
                quadmath_snprintf(msqgr_im, sizeof(msqgr_im), "%.36Qg", cimagq(integ_p));
                quadmath_snprintf(msqgr_err, sizeof(msqgr_err), "%.36Qg", abserr_qagp);
                fprintf(msqgr_fp, "%d\t%d\t%d\t%d\t%s\t%s\t%s\t%d\n",
                        two_p1,two_p2,two_p3,two_p4,
                        msqgr_re,msqgr_im,msqgr_err,(int)rcode);
                fclose(msqgr_fp);
            }
        }
'''.replace('\\"','"')
if anchor not in s: raise SystemExit('complex integral anchor not found')
s=s.replace(anchor,anchor+logger,1)
if mode != 'baseline':
    inc='#include "dsmall.h"'
    if inc not in s: raise SystemExit('dsmall include anchor missing')
    s=s.replace(inc,inc+'\n#include "sl2cfoam_toller_branch_adapter.h"',1)
    for n in range(1,5):
        old=f'''sl2cfoam_dsmall(d{n}, xs, N, p{n}->prec, p{n}->Ym, p{n}->Yn, NULL,\n                    p{n}->rho, p{n}->two_j, p{n}->two_j, p{n}->two_l, p{n}->two_p);'''
        new=f'''msqgr_toller_dsmall_branch(d{n}, xs, N, p{n}->rho,\n                                p{n}->two_j, p{n}->two_j, p{n}->two_l, p{n}->two_p,\n                                msqgr_toller_branch_for_leg({n-1}));'''
        if old not in s: raise SystemExit(f'dsmall call {n} not found')
        s=s.replace(old,new,1)
p.write_text(s)
PY

if [[ "$MODE" != "baseline" ]]; then
  cp "$ROOT/native/toller_kernel.c" src/toller_kernel.c
  cp "$ROOT/native/toller_kernel.h" src/toller_kernel.h
  cp "$ROOT/branch/sl2cfoam_toller_branch_adapter.c" src/sl2cfoam_toller_branch_adapter.c
  cp "$ROOT/branch/sl2cfoam_toller_branch_adapter.h" src/sl2cfoam_toller_branch_adapter.h
  python3 - <<'PY'
from pathlib import Path
p=Path('Makefile');s=p.read_text();old='b4.o b4_qagp.o cgamma.o';new='b4.o b4_qagp.o cgamma.o toller_kernel.o sl2cfoam_toller_branch_adapter.o'
if old not in s: raise SystemExit('Makefile object anchor missing')
p.write_text(s.replace(old,new,1))
PY
fi

STAGE=build
make lib BLAS=system OMP=0 || { DETAIL="instrumented sl2cfoam build failed"; exit 0; }
mkdir -p data_sl2cfoam
./ext/fastwigxj/bin/hash_js --max-E-3j=16 /dev/null data_sl2cfoam/table_16.3j || { DETAIL="3j table failed"; exit 0; }
./ext/fastwigxj/bin/hash_js --max-E-6j=16 /dev/null data_sl2cfoam/table_16.6j || { DETAIL="6j table failed"; exit 0; }
export LD_LIBRARY_PATH="$PWD/lib:$PWD/ext/fastwigxj/lib:$PWD/ext/wigxjpf/lib:${LD_LIBRARY_PATH:-}"

gcc -std=gnu11 -O2 -I"$PWD/inc" -I"$PWD/src" -I"$PWD/ext/wigxjpf/inc" -I"$PWD/ext/fastwigxj/inc" -I"$PWD/ext" \
  "$ROOT/branch/sl2cfoam_b4_branch_probe.c" \
  -L"$PWD/lib" -L"$PWD/ext/wigxjpf/lib" -L"$PWD/ext/fastwigxj/lib" \
  -Wl,-rpath,"$PWD/lib" -Wl,-rpath,"$PWD/ext/wigxjpf/lib" -Wl,-rpath,"$PWD/ext/fastwigxj/lib" \
  -lsl2cfoam -lopenblas -lblas -lpthread -lmpc -lmpfr -lgmp -lfastwigxj -lwigxjpf -lwigxjpf_quadmath -lquadmath -lm \
  -o /tmp/msqgr_branch_b4_probe || { DETAIL="branch B4 probe compile failed"; exit 0; }

STAGE=compute
if [[ "$MODE" == "baseline" ]]; then
  if timeout 12m /tmp/msqgr_branch_b4_probe "$PWD/data_sl2cfoam" "$OUT" baseline > "$OUT/matrix_baseline.tsv" 2> "$OUT/baseline.log"; then
    COMPLETED=1; DETAIL="ordinary complex QAGP baseline dumped for two small-spin B4 cases"
  else
    DETAIL="ordinary baseline B4 failed or timed out"
  fi
else
  SHARD="$MODE"
  if ! [[ "$SHARD" =~ ^[0-3]$ ]]; then DETAIL="expected shard 0..3 or baseline"; exit 0; fi
  START=$((SHARD*4)); END=$((START+3))
  for MASK in $(seq "$START" "$END"); do
    LABEL="mask${MASK}"
    if timeout 12m /tmp/msqgr_branch_b4_probe "$PWD/data_sl2cfoam" "$OUT" "$LABEL" "$MASK" > "$OUT/matrix_${LABEL}.tsv" 2> "$OUT/${LABEL}.log"; then
      COMPLETED=$((COMPLETED+1))
    else
      DETAIL="branch mask ${MASK} failed or timed out after ${COMPLETED} completed masks"
      exit 0
    fi
  done
  DETAIL="branch masks ${START}..${END} completed with full complex pre-projection QAGP tensors"
fi
