# Bad practices and their consequences

These are recurring SDD mistakes in small scripts and larger projects. The
shipping Lab helps expose several of them, but it does not simulate a full
team or production system.

## Writing the spec after the code and treating it as proof

A retroactive description can simply repeat current behavior, including
mistakes. It gives little independent evidence of what was wanted. Start with
the user outcome and acceptance examples, review them, and then compare code
to them. In this Lab, the exercise changes FR-1 before changing `quote.py`,
so a mismatch can be observed.

## Hiding design decisions inside a behavior requirement

“Use Python and an if statement” tells an implementer how to code but not
what a shopper should receive at 50. It can also block a valid alternative
implementation. Specify the observable rule, then document Python and the
CLI in the plan. State true platform constraints separately.

## Using vague or only happy-path examples

“Shipping is free for large orders” does not define “large.” A test at 49
alone cannot tell whether 50 is free. The result is disagreement among
reviewers and inconsistent implementations. State the inclusive boundary and
test at it. Include invalid inputs when they change the public outcome.

## Letting spec, tests, and code drift

Changing the shipping fee in code alone could leave a test failing or,
worse, leave a stale spec that misleads the next change. Changing only the
test can make the suite appear current while the intended rule remains
unreviewed. Update the authoritative spec, affected tests, and implementation
as one change; review their agreement after execution.

## Confusing passing tests with complete correctness

Tests check only what they assert. A suite can pass even when the spec omits
taxes, rounding, accessibility, or a critical error case. Generated tests
can share the same incorrect assumption as generated code. Review coverage
against requirements and inspect behavior beyond automated checks when risk
warrants it. The Lab explicitly limits input to whole-dollar subtotals and
excludes taxes and discounts.

## Overspecifying a tiny feature

Large templates, complex infrastructure, and many optional quality gates can
bury the core rule. They increase maintenance cost and make contradictions
more likely. Use the smallest set of artifacts that keeps intent, design,
work, and evidence clear. The Lab uses one spec, one plan, one task list, one
CLI, and three acceptance tests.

## Treating an agent's plan as authorization

An AI agent may make a plausible but unsupported product decision. For
example, it might choose free shipping above 50 rather than at 50. Review
business rules and acceptance examples before implementation. The human
owns the intended outcome; the agent can help draft and implement it. The
[Spec Kit quickstart](https://github.github.com/spec-kit/quickstart) also
places review between phases.
