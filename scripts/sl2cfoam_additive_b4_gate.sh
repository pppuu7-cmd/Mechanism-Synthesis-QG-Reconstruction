#!/usr/bin/env bash
# Full integration-plumbing test: compare upstream sl2cfoam_b4_accurate with a
# controlled build in which the four raw dsmall calls inside dsmall_prod_qagp
# are replaced by native Toller (t+ + t-). Everything downstream is unchanged.
set -u
ROOT="${GITHUB_WORKSPACE:-$PWD}"
mkdir -p "$ROOT/results"
WORK="${RUNNER_TEMP:-/tmp}/msqgr-additive-b4"
rm -rf "$WORK"; mkdir -p "$WORK"; cd "$WORK"
STAGE=init; DETAIL=""; BASE=false; PATCH=false; TOLLER=false
finish(){
  MSQGR_ROOT="$ROOT" python3 - "$STAGE" "$DETAIL" "$BASE" "$PATCH" "$TOLLER" <<'PY'
import json,os,sys
stage,detail,base,patch,toller=sys.argv[1:]
out={"stage_reached":stage,"detail":detail,"baseline_b4_completed":base.lower()=="true","toller_integrand_patch_built":patch.lower()=="true","toller_sum_b4_completed":toller.lower()=="true","scope":"full sl2cfoam_b4_accurate additive plumbing gate; no branch-resolved causal B4 and no F9 credit"}
if out['toller_sum_b4_completed']:out['verdict']='ADDITIVE_B4_RESULTS_READY_FOR_COMPARISON'
elif out['toller_integrand_patch_built']:out['verdict']='TOLLER_PATCH_BUILT_B4_RUNTIME_OPEN'
elif out['baseline_b4_completed']:out['verdict']='BASELINE_B4_READY_TOLLER_PATCH_OPEN'
else:out['verdict']='ADDITIVE_B4_INFRASTRUCTURE_BLOCKED'
root=os.environ.get('MSQGR_ROOT','.')
os.makedirs(os.path.join(root,'results'),exist_ok=True)
open(os.path.join(root,'results','additive_b4_smoke.json'),'w').write(json.dumps(out,indent=2))
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

STAGE=baseline_build
make lib BLAS=system OMP=0 || { DETAIL="baseline sl2cfoam lib build failed"; exit 0; }
mkdir -p data_sl2cfoam
./ext/fastwigxj/bin/hash_js --max-E-3j=16 /dev/null data_sl2cfoam/table_16.3j || { DETAIL="3j table failed"; exit 0; }
./ext/fastwigxj/bin/hash_js --max-E-6j=16 /dev/null data_sl2cfoam/table_16.6j || { DETAIL="6j table failed"; exit 0; }
export LD_LIBRARY_PATH="$PWD/lib:$PWD/ext/fastwigxj/lib:$PWD/ext/wigxjpf/lib:${LD_LIBRARY_PATH:-}"

compile_probe(){
  gcc -std=gnu11 -O2 -I"$PWD/inc" -I"$PWD/src" -I"$PWD/ext/wigxjpf/inc" -I"$PWD/ext/fastwigxj/inc" -I"$PWD/ext" \
    "$ROOT/scripts/sl2cfoam_b4_accurate_probe.c" \
    -L"$PWD/lib" -L"$PWD/ext/wigxjpf/lib" -L"$PWD/ext/fastwigxj/lib" \
    -Wl,-rpath,"$PWD/lib" -Wl,-rpath,"$PWD/ext/wigxjpf/lib" -Wl,-rpath,"$PWD/ext/fastwigxj/lib" \
    -lsl2cfoam -lopenblas -lblas -lpthread -lmpc -lmpfr -lgmp -lquadmath -lfastwigxj -lwigxjpf -lwigxjpf_quadmath -lm \
    -o /tmp/msqgr_b4_probe
}

STAGE=baseline_b4
compile_probe || { DETAIL="baseline B4 probe compile failed"; exit 0; }
if timeout 10m /tmp/msqgr_b4_probe "$PWD/data_sl2cfoam" > "$ROOT/results/b4_baseline.tsv" 2> "$ROOT/results/b4_baseline.log"; then
  BASE=true
else
  DETAIL="baseline accurate B4 failed or timed out"; exit 0
fi

STAGE=patch_toller
cp "$ROOT/native/toller_kernel.c" src/toller_kernel.c
cp "$ROOT/native/toller_kernel.h" src/toller_kernel.h
cp "$ROOT/native/sl2cfoam_toller_adapter.c" src/sl2cfoam_toller_adapter.c
cp "$ROOT/native/sl2cfoam_toller_adapter.h" src/sl2cfoam_toller_adapter.h
python3 - <<'PY'
from pathlib import Path
m=Path('Makefile');s=m.read_text()
old='b4.o b4_qagp.o cgamma.o'
new='b4.o b4_qagp.o cgamma.o toller_kernel.o sl2cfoam_toller_adapter.o'
if old not in s: raise SystemExit('Makefile object anchor not found')
m.write_text(s.replace(old,new,1))
p=Path('src/b4_qagp.c');s=p.read_text()
anchor='#include "dsmall.h"'
if anchor not in s: raise SystemExit('include anchor not found')
s=s.replace(anchor,anchor+'\n#include "sl2cfoam_toller_adapter.h"',1)
for n in range(1,5):
    old=f'''sl2cfoam_dsmall(d{n}, xs, N, p{n}->prec, p{n}->Ym, p{n}->Yn, NULL,\n                    p{n}->rho, p{n}->two_j, p{n}->two_j, p{n}->two_l, p{n}->two_p);'''
    new=f'''msqgr_toller_dsmall_sum(d{n}, xs, N, p{n}->rho,\n                             p{n}->two_j, p{n}->two_j, p{n}->two_l, p{n}->two_p);'''
    if old not in s: raise SystemExit(f'dsmall call {n} anchor not found')
    s=s.replace(old,new,1)
p.write_text(s)
PY
rm -rf obj lib bin
if make lib BLAS=system OMP=0; then PATCH=true; else DETAIL="Toller-patched sl2cfoam build failed"; exit 0; fi

STAGE=toller_b4
compile_probe || { DETAIL="Toller B4 probe compile failed"; exit 0; }
if timeout 15m /tmp/msqgr_b4_probe "$PWD/data_sl2cfoam" > "$ROOT/results/b4_toller_sum.tsv" 2> "$ROOT/results/b4_toller_sum.log"; then
  TOLLER=true
else
  DETAIL="Toller-sum accurate B4 failed or timed out; likely endpoint/hypergeometric precision-performance blocker"; exit 0
fi

STAGE=compare
cd "$ROOT"
if python3 convention/compare_additive_b4.py --baseline results/b4_baseline.tsv --toller results/b4_toller_sum.tsv --output results/additive_b4_comparison.json --threshold 1e-4; then
  DETAIL="full accurate B4 additive reconstruction passed at NORMAL integration tolerance"
else
  DETAIL="both B4 calculations completed but additive comparison missed tolerance; inspect precision/cancellation by matrix entry"
fi
