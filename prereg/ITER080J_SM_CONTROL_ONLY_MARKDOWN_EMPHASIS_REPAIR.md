# Iter080J-SM control-only repair preregistration — markdown-emphasis normalization

Date: 2026-09-14

## Historical runs preserved

Historical production run `34859269730` remains `INVALID_IMPLEMENTATION_LEXICAL_CONTROL`: Lane B failed on the authoritative Iter029 `Hormander` ASCII spelling before aggregate authority.

Historical repaired run `34859501380` also remains implementation-invalid for scientific classification. In that run lanes A/C/D passed, while Lane B failed only because the executable searched for the literal plain-text substring `does not invent CRQN v0.3`, whereas the prospectively frozen preregistration contains the semantically identical Markdown-emphasized sentence `does **not** invent CRQN v0.3`. Aggregate therefore lacked all four lane artifacts and failed. No scientific PASS/FAIL is assigned to that run.

## Exact implementation defect

The frozen Lane B scientific criterion is unchanged: the candidate `M_WF` gate must be independently motivated and must not construct a successor model merely because CRQN v0.2 is blocked.

The second repaired executable correctly accepts both `Hormander` and `Hörmander` for the Iter029 motivation, but its `no_successor_construction` check is a brittle raw substring match that ignores Markdown emphasis. The authoritative preregistration itself supplies the required negative statement; only presentation markup separates `does` from `not` in the raw bytes.

## Frozen repair

Only the Lane B textual control for the already-frozen no-successor statement may change:

- normalize Markdown emphasis markers before checking the exact semantic phrase `does not invent CRQN v0.3`, or equivalently accept the exact authoritative emphasized spelling `does **not** invent CRQN v0.3`;
- keep the original Iter080J preregistration, `M_WF` object, frozen authority, Brunetti--Fredenhagen/Dang identifiers, Iter029 motivation requirement, theorem implication, PASS/FAIL criteria, interpretation ceiling, and all other lanes unchanged;
- do not add a selector, coefficient equation, spectral condition, regulator prescription, composition law, new candidate definition, or any substantive scientific hypothesis.

## Frozen classification handling

- Runs `34859269730` and `34859501380`: historical implementation-invalid controls only; neither has scientific authority.
- A new repaired production run may receive the original Iter080J preregistered classification only if lanes A/B/C/D and aggregate all complete under the unchanged scientific contract.
- Green CI is execution evidence only; the durable result must separately state the exact theorem used: smooth multiplication does not enlarge wavefront set, `delta_N` is conormal, and the exact Iter077Q linearly independent family therefore survives `M_WF`.
