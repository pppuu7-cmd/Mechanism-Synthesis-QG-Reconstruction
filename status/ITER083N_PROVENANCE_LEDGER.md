# Iter083N provenance ledger

**Date:** 2026-09-15

## Reviewed terminal chain

- preregistration: `c29ba0ddbaa4d6e1581db558b792565a7916a0cd`;
- actual source-lock commit: `cf9d17cc8dae087f2c59ff0adb9f8aeff8ef7533`;
- actual theorem-derivation commit: `70a756c9c7c66f822d0e5933e9522b2d359dafe8`;
- implementation: `3d93d82009ed22dceceda4e71e28a94331475b02`;
- syntax-only repair: `095e1c98af085ad54fadb1cde2e38b2d2d6d18cd`;
- wording-only repair / authoritative production head: `d35c1c3eb92456c053b27fa46a8783f28c76879b`;
- terminal run: `34917739247`;
- job: `104218935908`;
- artifact: `10376728965`;
- artifact ZIP digest: `sha256:da3a81a693797975ade1823d5e7554d9445358852029c926bc209281b10815d3`;
- production JSON SHA256: `9cc509a84714ff18e6687eda9b5f8e94c3ba7df1786f8cfb63866f9a8bd04553`;
- Researcher result: `d90be70dce0c820ba0a574a7d82e46737187f541`.

## Controlling Critic classification

`INVALID_PROVENANCE`

Controlling review: `results/ITER083N_ADVERSARIAL_PROVENANCE_REVIEW.md`, commit `fbff993fc920e707d0ff885b73549f3204d208c5`.

## Dependency chronology defect

The controlling Iter083M invalidation `063087c5dfcf0cca9e2565cf75ef82c8ea640f6f` predates Iter083N preregistration `c29ba0dd...`.

Iter083N froze P0 to consume Iter083M radial geometry even though Iter083M was already non-authoritative. The executable later checked only that the old Iter083M Researcher result contained PASS/status strings and did not consult the later Critic invalidation or CURRENT authority. Therefore the terminal green run does not satisfy frozen dependency authority.

## Durable provenance transcription defect

The Iter083N Researcher result records two identifiers as provenance commits:

- `9883aed83057ff6850dab605201bccddb7c92254` for the source lock;
- `f0a1d59956e76f135b9dac6a31d6cdf8bcbca578` for the theorem derivation.

Neither resolves as a commit or blob in the repository. The actual commits are `cf9d17cc...` and `70a756c9...` respectively.

## Authority consequence

The Iter083N terminal numerical/symbolic output may be retained historically but may not be used downstream. The standalone finite-part algebra is not scientifically refuted; authority can only be recovered after Iter083M becomes valid and Iter083N is then re-run under a dependency-valid contract, or through a newly preregistered gate if the dependency is changed.

Iter083O preregistration `2b0ef9969cc07f70a0d9d22819f17973e2ee67c6` is preparation only and is downstream-quarantined from substantive production until the Iter083M -> Iter083N chain is authoritative.
