# Fresh-reader review

Use this for important artifacts after the writer's normal review. Independence matters more than the identity of the reviewer.

## Context boundary

Give the reviewer only:

- the finished document;
- necessary source material available to the real reader;
- the intended audience;
- the intended reader outcome.

Do not provide the writer's hidden reasoning, drafting conversation, intended fixes, or explanations of ambiguous passages. If a separate agent is unavailable, simulate the same boundary by starting a context-clean review and refusing to fill gaps from memory.

## Reviewer prompt

```text
Review this as a fresh member of the intended audience.

Identify:
- what is unclear or context-dependent;
- assumptions that are not stated;
- questions the reader would still have;
- claims that appear unsupported;
- missing information needed for the stated goal;
- duplicated or misplaced information;
- contradictions within the document or supplied sources;
- whether the reader could actually act or decide.

Do not infer the author's unstated intent. Cite the relevant section for each finding and rank findings by impact.
```

## Acceptance

The review passes when no high-impact gap blocks the reader's primary task, consequential claims are supported or labeled, and remaining questions are intentionally out of scope. The author should revise from findings, then recheck affected sections; repeated full fresh-reader passes are unnecessary for minor edits.
