# Concepts and fundamentals

## What Spec Driven Development means

Spec Driven Development (SDD) begins with an explicit description of intended
behavior, then uses it to guide design, implementation, and verification. A
**specification** is a reviewable agreement about what a system should do:
its purpose, rules, boundaries, and representative examples. Code is checked
against that agreement. A spec may be prose, structured scenarios, a machine
readable contract, or a combination.

GitHub's [Spec Kit methodology](https://github.com/github/spec-kit/blob/main/spec-driven.md)
describes a spec-first, agent-assisted process. Its
[quickstart](https://github.github.com/spec-kit/quickstart) separates the
feature specification from planning, tasks, implementation, and convergence.
This Lab borrows the small sequence, without requiring Spec Kit or an AI agent.

## Essential vocabulary

- **Intent and scope:** Why the feature exists and what belongs in it. Here,
  the goal is a shipping quote; taxes and discounts are excluded.
- **Requirement:** A rule that people can review and check. FR-1 says shipping
  costs 5 below a subtotal of 50 and zero at or above 50.
- **Acceptance example:** A concrete input and expected observation. The
  examples 49 → shipping 5 and 50 → shipping 0 expose the exact boundary.
  Examples illustrate a rule; they do not define every possible input.
- **Plan:** Technical decisions for meeting the requirement. This Lab chooses
  Python and a CLI in its plan, after specifying user-visible behavior.
- **Task:** A bounded implementation step derived from the plan.
- **Verification:** Evidence that observed behavior matches the spec. A
  passing test covers its asserted cases, not necessarily every requirement.
- **Traceability:** A link from requirement to check and implementation. Test
  names here include the relevant requirement identifiers.
- **Convergence:** Reviewing the complete result against the spec and fixing
  remaining gaps. A green test suite is one input to that review.

## The workflow

```text
Need → specification → plan → tasks → implementation
          │                           │
          └──── acceptance checks ────┘
                    ↓
             compare and revise
```

This is a loop. When an acceptance check fails, ask whether the code is wrong,
the test misread the spec, or the spec is ambiguous. When desired behavior
changes, revise the spec first, then affected checks and implementation. Revise
the plan as well if the new requirement changes the design. Natural-language
specifications do not become executable automatically; humans must review
meaning, coverage, and trade-offs.

## The Lab's concrete slice

[The feature spec](../specs/001-shipping-quote/spec.md) defines three rules.
[The plan](../specs/001-shipping-quote/plan.md) maps those rules to CLI checks.
[The tasks](../specs/001-shipping-quote/tasks.md) record the baseline sequence.
[The tests](../tests/test_quote.py) run [the CLI](../quote.py) and check output,
errors, and exit status. Changing the fee in the spec and test exposes a gap
until the implementation changes.

Larger work may need multiple features, stakeholder sign-off, service
contracts, nonfunctional requirements, version control, and risk analysis.
The Lab demonstrates a single rule change, not proof that one test suite can
validate an entire product.

## Nearby practices

Test Driven Development (TDD) often begins a code change with a failing test,
then implements and refactors. SDD starts with agreed behavior and can use TDD
to translate that behavior into code. Behavior Driven Development (BDD) uses
shared examples, sometimes in a structured language such as
[Gherkin](https://cucumber.io/docs/gherkin/reference/). These approaches can
work together. A Markdown spec is not automatically an executable Gherkin
scenario, and an API contract covers only part of a feature's intent.
