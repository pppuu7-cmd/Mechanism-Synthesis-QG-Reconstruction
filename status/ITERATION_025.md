# Iteration 025A — j=1/2 Appendix-D distributional primitive

Status: **COMPLETED / PASS**

Workflow: `Jhalf Appendix-D Distribution Validation`

- 3/3 GitHub jobs completed successfully.
- rho = 0.1, 0.6, 1.0.
- j = 1/2.

For j=1/2 the Appendix-D polynomial was reduced to

`F = 1 + c1 sigma q + (c2/2)(sigma q)^2`,

with

- `c1 = 2 rho/(rho^2+1/4)`,
- `c2 = 2/(rho^2+1/4)`,

and therefore

`delta^(rho,1/2) = -i c1 delta - (c2/2) delta'`.

The implementation validates:

1. the exact product-polynomial form against the closed c1,c2 expansion at high precision;
2. the action of `theta(sigma x)+sigma delta^(rho,1/2)(x)` on several Gaussian-polynomial Schwartz test functions using a shrinking Gaussian mollifier;
3. the exact complementary identity `Theta_+ + Theta_- = 1` on the test-function space.

Representative numerical results:

- rho=1.0: polynomial identity error `2.90e-70`, exact complement error `0`, smallest-eta worst action error `1.97e-3`;
- rho=0.1: polynomial identity error `5.80e-70`, exact complement error `1.81e-71`, smallest-eta worst action error `4.68e-3`.

All jobs return `JHALF_APPENDIX_D_DISTRIBUTION_PASS`.

## Interpretation

The boundary-supported distribution required by the published Feynman i-epsilon construction is now an explicit, tested computational primitive in the repository. The implementation deliberately does **not** replace the spectral prescription by an ad-hoc `beta+i epsilon` substitution.

This does not yet resolve the multi-collision finiteness problem. Products/intersections of multiple wedge boundary distributions and possible angular/principal-value cancellations remain separate questions.

## Next target

Iteration 026 tests the cheapest remaining conditional-convergence mechanism: antipodal/angular cancellation of the leading homogeneous multi-collision residue after the full boundary-intertwiner contraction and causal+co-causal sector sum.
