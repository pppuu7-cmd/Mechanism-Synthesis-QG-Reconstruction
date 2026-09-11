#!/usr/bin/env bash
# Build the public sl2cfoam-next backend on a clean GitHub Ubuntu runner and,
# if compilation succeeds, attempt one minimal shell-0 Lorentzian full-tensor vertex.
# Every failure is recorded as evidence rather than hidden; the script exits 0 so the
# diagnostic artifact survives for inspection.
set -u
ROOT="${GITHUB_WORKSPACE:-$PWD}"
mkdir -p "$ROOT/results"
WORK="${RUNNER_TEMP:-/tmp}/msqgr-sl2cfoam-smoke"
rm -rf "$WORK"; mkdir -p "$WORK"
STAGE=init; DETAIL=""; BUILT=false; VERTEX=false
finish(){
  MSQGR_ROOT="$ROOT" python3 - "$STAGE" "$DETAIL" "$BUILT" "$VERTEX" <<'PY'
import json,sys,os
stage,detail,built,vertex=sys.argv[1:]
out={"stage_reached":stage,"detail":detail,"library_built":built.lower()=="true","minimal_vertex_completed":vertex.lower()=="true","backend":"qg-cpt-marseille/sl2cfoam-next","blas":"system/openblas","omp":False,"vertex_target":{"gamma":1.2,"twice_spins":[1]*10,"Dl":0},"scope":"build/compute smoke only; no Toller projector and no F9 credit"}
out["verdict"]="MINIMAL_LORENTZIAN_EPRL_VERTEX_COMPUTED" if out["minimal_vertex_completed"] else ("SL2CFOAM_LIBRARY_BUILT_VERTEX_PENDING" if out["library_built"] else "SL2CFOAM_BUILD_SMOKE_BLOCKED")
root=os.environ.get('MSQGR_ROOT','.')
os.makedirs(os.path.join(root,'results'),exist_ok=True)
open(os.path.join(root,'results','sl2cfoam_build_smoke.json'),'w').write(json.dumps(out,indent=2))
print(json.dumps(out,indent=2))
PY
}
trap finish EXIT

STAGE=apt
if ! sudo apt-get update -qq; then DETAIL="apt update failed"; exit 0; fi
if ! sudo apt-get install -y -qq git curl wget build-essential m4 lzip libgmp-dev libmpfr-dev libmpc-dev libgsl-dev libopenblas-dev libomp-dev gfortran; then DETAIL="dependency install failed"; exit 0; fi

cd "$WORK"
STAGE=clone
if ! git clone --depth 1 https://github.com/qg-cpt-marseille/sl2cfoam-next.git; then DETAIL="sl2cfoam clone failed"; exit 0; fi
cd sl2cfoam-next
mkdir -p ext
cd ext
STAGE=wigxjpf
if ! curl -fsSL -o wigxjpf.tar.gz https://fy.chalmers.se/subatom/wigxjpf/wigxjpf-1.13.tar.gz; then DETAIL="wigxjpf download failed"; exit 0; fi
if ! tar -xzf wigxjpf.tar.gz; then DETAIL="wigxjpf extract failed"; exit 0; fi
mv wigxjpf-1.13 wigxjpf
if ! make -C wigxjpf -j2; then DETAIL="wigxjpf build failed"; exit 0; fi

STAGE=fastwigxj
if ! curl -fsSL -o fastwigxj.tar.gz https://fy.chalmers.se/subatom/fastwigxj/fastwigxj-1.4.1.tar.gz; then DETAIL="fastwigxj download failed"; exit 0; fi
if ! tar -xzf fastwigxj.tar.gz; then DETAIL="fastwigxj extract failed"; exit 0; fi
mv fastwigxj-1.4.1 fastwigxj
if ! make -C fastwigxj -j2; then DETAIL="fastwigxj build failed on current GitHub runner compiler; inspect log before patching upstream source"; exit 0; fi

cd ..
STAGE=library
if ! make -j2 BLAS=system OMP=0; then DETAIL="sl2cfoam-next build failed"; exit 0; fi
BUILT=true

STAGE=tables
mkdir -p data_sl2cfoam
if ! ./ext/fastwigxj/bin/hash_js --max-E-3j=16 /dev/null data_sl2cfoam/table_16.3j; then DETAIL="3j table generation failed"; exit 0; fi
if ! ./ext/fastwigxj/bin/hash_js --max-E-6j=16 /dev/null data_sl2cfoam/table_16.6j; then DETAIL="6j table generation failed"; exit 0; fi

STAGE=vertex
export LD_LIBRARY_PATH="$PWD/lib:${LD_LIBRARY_PATH:-}"
# Minimal nontrivial gamma-simple Lorentzian EPRL full tensor, shell cutoff Dl=0.
if timeout 8m ./bin/vertex-fulltensor -V -h -m 2000 "$PWD/data_sl2cfoam" 1.2 1,1,1,1,1,1,1,1,1,1 0 > results_vertex.log 2>&1; then
  VERTEX=true; DETAIL="clean hosted-runner source build and shell-0 vertex completed"
else
  DETAIL="library built but minimal vertex command failed or exceeded 8m; inspect results_vertex.log"
fi
cp results_vertex.log "$ROOT/results/sl2cfoam_vertex.log" 2>/dev/null || true
cd "$ROOT"
