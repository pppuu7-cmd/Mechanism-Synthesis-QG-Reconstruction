# Iteration 006B — EPRL cutoff / backend readiness

**Date:** 2026-09-12  
**MSQGR Actions run:** `34654915609`  
**Parallel matrix:** **19/19 jobs + aggregate = success**.  
**Independent sl2cfoam smoke run:** `34654915552`.

## Cutoff result

The empirical three-step shell criterion finds only the published `gamma=1.2, j=1.0, Dl=25` series reaches 0.2% observed stability in every available column. The shallower `j=0.5, Dl=15` series do not.

## Important precision correction

The last shell increment is not the total unresolved truncation error. Across all nine published tails, a power law fits the last eight increments better than an exponential (`POWER: 9`, `EXPONENTIAL: 0`), with fitted powers roughly `p=2.4..3.0`.

Therefore geometric/Aitken extrapolators validated against the finite `Dl=25` endpoint are not accepted as precision estimators: no method/cutoff passed all columns at the tested sustained thresholds.

A direct power-tail estimate is introduced in Iteration 006C. Preliminary calculation gives remaining fractions near 1.9%, 0.83%, and 1.15% for the three `gamma=1.2, j=1.0` columns. Thus `Dl=25` is suitable for a ~2% **prototype**, but not yet a <1% precision claim.

## sl2cfoam build smoke

The clean Ubuntu 24.04 runner successfully built `wigxjpf` and `fastwigxj`. The first sl2cfoam invocation failed at the library/test stage because upstream parallel `make -j2` started `lib_test` while `libsl2cfoam.so` was still being built; the linker then reported missing `sl2cfoam_init_conf` and `sl2cfoam_vertex_fullrange` symbols.

This is treated as a build-order race, not a physics/backend failure. Iteration 006C switches to sequential `make lib` followed by `make tools` and reruns the physical smoke.

## F9

Still `BLOCKED`. No cutoff result, extrapolator, or successful ordinary EPRL vertex gives F9 credit. The decisive calculation remains a same-realization causal amplitude / boundary map after inserting the Toller split at the reduced Wigner-d / booster level.
