# Best practices

These practices apply to SDD beyond the shipping CLI. Spec Kit's
[quickstart](https://github.github.com/spec-kit/quickstart) and
[agentic reference](https://github.github.com/spec-kit/reference/agentic-sdd.html)
provide one tool-supported workflow; the principles below also work without
that tool.

## Specify outcomes before implementation choices

State who needs the behavior and what they can observe. A rule such as “a
subtotal of 50 receives free shipping” leaves room to choose a CLI, API, or
UI later. Put language, architecture, and storage choices in the plan. This
separation makes it easier to review product behavior without debating
implementation details at the same time. If a technical constraint is truly
part of the contract, state it explicitly as a constraint.

## Make ambiguity visible with boundaries and errors

Words like “over,” “near,” and “valid” hide decisions. Give examples at
important boundaries and state invalid-input behavior. The Lab tests 49,
50, and -1 because those values distinguish the two fee branches and the
error path. For a date rule, include the exact cutoff and timezone; for an
API, include missing-field and malformed-field responses.

## Keep requirements and checks traceable

Use stable, simple identifiers and connect each important requirement to an
acceptance check. In the Lab, FR-1 and FR-2 appear in two test names and FR-3
appears in a third. This makes missing coverage easier to spot when a
requirement changes. Avoid turning IDs into bureaucracy: one meaningful
requirement may have several checks, and one end-to-end scenario may exercise
several requirements.

## Verify the public behavior

Check the interface users or downstream systems actually consume. The Lab's
tests launch the CLI and inspect standard output, standard error, and exit
status. A unit test of the `quote()` function would be useful for a larger
calculation, but it alone would miss command-line parsing and formatting
errors. For web services, test representative HTTP exchanges; for interfaces,
test meaningful user actions and review the rendered result.

## Treat change as a loop

When a requirement changes, revise the spec, then its acceptance checks,
then the implementation. Review whether the plan and tasks are still valid.
The Lab exercise deliberately creates one failing test before changing the
fee constant. That failure is evidence of the gap to close. Once checks pass,
inspect the complete diff or changed files for accidental behavior changes.

## Choose a proportionate level of detail

Write enough to remove meaningful uncertainty, then stop. A two-line
shipping rule needs a short spec; a payment workflow needs more cases,
security constraints, and review. Long documents with repeated statements
can contradict each other. Keep one authoritative behavior rule and use
examples to clarify it.

## Review generated artifacts as independent evidence

An agent can draft specs, plans, tasks, code, and tests, but a shared mistake
can pass from one artifact to the next. A human should validate intent and
important examples, and the actual program must be run. Spec Kit's
[convergence step](https://github.github.com/spec-kit/quickstart) encourages
checking the final codebase against the specification and adding work for
remaining gaps. Passing tests support that review; they do not replace it.
