# Iter080F-SM — control-only timezone/provenance repair plan

Run `34836984921` is implementation/provenance-invalid, not scientific authority. Lane A compared ISO-8601 timestamp strings literally. Git renders the same commit instant in the commit's recorded `+03:00` offset, while the prereg ledger recorded the API-equivalent UTC instant. Thus identical instants were falsely marked unequal.

## Frozen science unchanged

The Iter080F preregistration at `382948b3369c3bc2132ff4c2757500fdd7b77ba1`, frozen corpus, blob SHAs, origin commits, A1-A5 predicates, candidate statements, classifier controls, possible outcomes and interpretation ceiling remain unchanged.

## Allowed repair only

Lane A shall normalize commit timestamps to timezone-aware UTC instants (or Unix epoch seconds) before equality/order comparison. It must continue to verify:

- exact candidate blob SHAs;
- exact origin commit IDs;
- origin commit instants equivalent to `2026-09-11T21:52:10Z` and `2026-09-11T21:55:16Z`;
- Iter077Q result commit instant equivalent to `2026-09-14T00:24:24Z`;
- both candidate origins strictly predate Iter077Q.

No Lane B/C/D scientific logic may be altered as part of this repair. The failed run remains preserved as `INVALID_PROVENANCE`.