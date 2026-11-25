# Representative use cases

SDD helps when implementing the wrong behavior costs more than clarifying it
first. The amount of specification should fit the risk and the number of
people involved. Only the shipping CLI is implemented in this Lab.

## Small business rules

Fees, eligibility rules, and discounts often have boundaries that developers
can misread. A spec can state the general rule and show examples just below,
at, and above each boundary. Tests check the examples. This Lab is such a
case: 49 and 50 distinguish the two sides of free shipping. A few examples do
not prove every input, so reviewers must inspect the general rule too.

## API contracts across teams

When a client and service are built separately, a written contract can define
request fields, responses, and error cases. An
[OpenAPI description](https://spec.openapis.org/oas/latest.html) can express
HTTP interface details, while a feature spec explains purpose and business
rules. Contracts reduce integration guesswork but can drift unless tests
compare them with deployed behavior. The CLI output in this Lab is a small
analogue of a public interface; it does not implement HTTP.

## Auditable calculations

When a calculation affects money or eligibility, reviewers need to understand
the rule before trusting code. Requirement identifiers and linked tests help
explain why each case exists. The trade-off is more review work. A real
financial calculation may also need rounding, effective dates, data sources,
and approvals. This Lab avoids those complications with whole-dollar values
and one fixed fee.

## Interfaces with multiple user paths

An onboarding or checkout spec can describe the goal, normal path, empty
state, invalid input, and accessibility expectations. Automated checks cover
important interactions; visual and human review cover aspects that tests
express poorly. A screen-by-screen script can overconstrain design, so focus
on outcomes and essential constraints. This Lab demonstrates observable
behavior but has no graphical interface.

## AI-assisted implementation

An AI coding agent can turn a reviewed spec into a plan, tasks, code, and
checks. [Spec Kit's agentic SDD reference](https://github.github.com/spec-kit/reference/agentic-sdd.html)
describes that process. Explicit examples make boundary mistakes easier for a
human to catch. Agent output still needs review and execution: generated code
and generated tests can share the same misunderstanding. The Lab works
without an agent so every artifact is inspectable.

## A bounded change in an existing system

A team can specify one new feature without trying to document the entire
codebase first. The spec should state the new behavior and compatibility
constraints. Planning should respect existing architecture, and verification
should cover affected old behavior. The
[Spec Kit existing-project guide](https://github.github.com/spec-kit/how-to/existing-projects.html)
describes this approach. This Lab starts with a tiny CLI and does not verify
migration or compatibility with existing clients.
