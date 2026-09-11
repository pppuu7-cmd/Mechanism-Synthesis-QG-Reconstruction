#!/usr/bin/env bash
# Build public sl2cfoam-next, compute a minimal Lorentzian vertex, then probe the
# actual upstream reduced Wigner dsmall for an empirical Ruhl/spinfoam phase audit.
# Failures are recorded as artifacts rather than hidden.
set -u
ROOT="${GITHUB_WORKSPACE:-$PWD}"
mkdir -p "$ROOT/results"
WORK="${RUNNER_TEMP:-/tmp}/msqgr-sl2cfoam-smoke"
rm -rf "$WORK"; mkdir -p "$WORK"
STAGE=init; DETAIL=""; BUILT=false; VERTEX=false; PHASE=false
finish(){
  MSQGR_ROOT="$ROOT" python3 - "$STAGE" "$DETAIL" "$BUILT" "$VERTEX" "$PHASE" <<'PY'
import json,sys,os
stage,detail,built,vertex,phase=sys.argv[1:]
out={"stage_reached":stage,"detail":detail,"library_built":built.lower()=="true","minimal_vertex_completed":vertex.lower()=="true","phase_audit_passed":phase.lower()=="true","backend":"qg-cpt-marseille/sl2cfoam-next","blas":"system/openblas","omp":False,"vertex_target":{"gamma":1.2,"twice_spins":[1]*10,"Dl":0},"scope":"backend + convention smoke only; no causal booster and no F9 credit"}
if out['minimal_vertex_completed'] and out['phase_audit_passed']: out['verdict']='LORENTZIAN_VERTEX_AND_DSMALL_PHASE_AUDIT_COMPLETE'
elif out['minimal_vertex_completed']: out['verdict']='MINIMAL_LORENTZIAN_EPRL_VERTEX_COMPUTED__PHASE_AUDIT_OPEN'
elif out['library_built']: out['verdict']='SL2CFOAM_LIBRARY_BUILT_VERTEX_PENDING'
else: out['verdict']='SL2CFOAM_BUILD_SMOKE_BLOCKED'
root=os.environ.get('MSQGR_ROOT','.')
os.makedirs(os.path.join(root,'results'),exist_ok=True)
open(os.path.join(root,'results','sl2cfoam_build_smoke.json'),'w').write(json.dumps(out,indent=2))
print(json.dumps(out,indent=2))
PY
}
trap finish EXIT

STAGE=apt
if ! sudo apt-get update -qq; then DETAIL="apt update failed"; exit 0; fi
if ! sudo apt-get install -y -qq git curl wget build-essential m4 lzip libgmp-dev libmpfr-dev libmpc-dev libgsl-dev libopenblas-dev libomp-dev gfortran python3-pip; then DETAIL="dependency install failed"; exit 0; fi

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
if ! make -C fastwigxj -j2; then DETAIL="fastwigxj build failed"; exit 0; fi

cd ..
STAGE=library
if ! make lib BLAS=system OMP=0; then DETAIL="sl2cfoam-next shared-library build failed"; exit 0; fi
BUILT=true
STAGE=tools
if ! make tools BLAS=system OMP=0; then DETAIL="sl2cfoam-next tools build failed after library success"; exit 0; fi

STAGE=tables
mkdir -p data_sl2cfoam
if ! ./ext/fastwigxj/bin/hash_js --max-E-3j=16 /dev/null data_sl2cfoam/table_16.3j; then DETAIL="3j table generation failed"; exit 0; fi
if ! ./ext/fastwigxj/bin/hash_js --max-E-6j=16 /dev/null data_sl2cfoam/table_16.6j; then DETAIL="6j table generation failed"; exit 0; fi

export LD_LIBRARY_PATH="$PWD/lib:$PWD/ext/fastwigxj/lib:$PWD/ext/wigxjpf/lib:${LD_LIBRARY_PATH:-}"
STAGE=vertex
if timeout 8m ./bin/vertex-fulltensor -V -h -m 2000 "$PWD/data_sl2cfoam" 1.2 1,1,1,1,1,1,1,1,1,1 0 > results_vertex.log 2>&1; then
  VERTEX=true; DETAIL="shell-0 Lorentzian vertex completed"
else
  DETAIL="library/tools built but minimal vertex failed or exceeded 8m"
fi
cp results_vertex.log "$ROOT/results/sl2cfoam_vertex.log" 2>/dev/null || true

STAGE=dsmall_probe
# libsl2cfoam.so references quad-precision Wigner symbols (e.g. wig6jj_float128)
# that live in libwigxjpf_quadmath.a rather than the ordinary libwigxjpf archive.
if ! gcc -std=gnu11 -O2 -I"$PWD/inc" -I"$PWD/src" -I"$PWD/ext/wigxjpf/inc" -I"$PWD/ext/fastwigxj/inc" -I"$PWD/ext" \
  "$ROOT/scripts/sl2cfoam_dsmall_probe.c" -L"$PWD/lib" -L"$PWD/ext/wigxjpf/lib" -L"$PWD/ext/fastwigxj/lib" \
  -Wl,-rpath,"$PWD/lib" -Wl,-rpath,"$PWD/ext/wigxjpf/lib" -Wl,-rpath,"$PWD/ext/fastwigxj/lib" \
  -lsl2cfoam -lopenblas -lblas -lpthread -lmpc -lmpfr -lgmp -lquadmath -lfastwigxj -lwigxjpf -lwigxjpf_quadmath -lm \
  -o /tmp/sl2cfoam_dsmall_probe; then DETAIL="vertex backend works but dsmall probe compilation failed"; cd "$ROOT"; exit 0; fi
if ! /tmp/sl2cfoam_dsmall_probe > "$ROOT/results/sl2cfoam_dsmall_probe.tsv"; then DETAIL="dsmall probe runtime failed"; cd "$ROOT"; exit 0; fi

STAGE=phase_audit
cd "$ROOT"
python3 -m pip install -q mpmath
if python3 convention/sl2cfoam_phase_convention_audit.py --probe results/sl2cfoam_dsmall_probe.tsv --output results/sl2cfoam_phase_convention_audit.json; then
  PHASE=true; DETAIL="Lorentzian vertex and pointwise dsmall/Ruhl convention map completed"
else
  DETAIL="dsmall values obtained but Ruhl/spinfoam convention map not resolved at target tolerance"
fi
