# Iter081B provenance erratum — Han source SHA256 transcription

Date: 2026-09-14
Scope: metadata/provenance correction only; no scientific criterion, source object, implementation, run output, verdict or claim ceiling is changed.

The durable Researcher result `results/ITER081B_SM_HAN_TOLLER_FACE_FUNCTIONAL_TRANSPORT_RESULT.md` at commit `3a81ff645ab7c6fdfb5178dbf705ba0642d902bb` transcribes the Han `arXiv:2602.18665v1` e-print SHA256 incorrectly by omitting one `af` byte-pair.

Incorrect transcription in that result:
`7e328d42768c78d8a4c33c93e575efaf19463f39679d0683743ffda0c23706`

Authoritative production value from Actions run `34871574623`, job `104068470983`, and the aggregate JSON:
`7e328d42768c78d8a4c33c93e575efafaf19463f39679d0683743ffda0c23706`

The authoritative BCG and Beltran source hashes remain:
- BCG `2604.24945v1`: `7e92d0241cea3460686e2c69912c77eebbc599d3cf6d03915f08558e3f00cf11`
- Beltran `2603.22661v2`: `f3d442ade2309fa15b1c507975a1c0b287fb9d5905a980a46d0b9c4bcf80bb8b`

This erratum does not invalidate the production source acquisition because the workflow run and artifact consumed and recorded the correct source bytes. Iter081B scientific verdict is separately reviewed in `results/ITER081B_ADVERSARIAL_REVIEW.md`.