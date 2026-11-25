# Essential links

These authoritative links were opened and checked on 2026-11-24. SDD is a
practice rather than a single mandatory product; the first links show one
concrete implementation of the process, and the others cover adjacent formats
and the test runner used in this Lab.

- [Spec Kit: understanding SDD](https://github.com/github/spec-kit/blob/main/spec-driven.md)
  explains why the specification can be the central development artifact.
  Read it for the broader philosophy, not as a claim that this Lab uses its
  CLI.
- [Spec Kit quickstart](https://github.github.com/spec-kit/quickstart)
  shows the sequence from specification through plan, tasks, implementation,
  and convergence. Compare that sequence with this Lab's three feature
  documents and CLI tests.
- [Spec Kit agentic SDD reference](https://github.github.com/spec-kit/reference/agentic-sdd.html)
  details the roles of each phase and optional quality checks. Use it when a
  small manual workflow is no longer enough.
- [Spec Kit existing-project guide](https://github.github.com/spec-kit/how-to/existing-projects.html)
  explains how to specify one bounded change in an established codebase.
- [Cucumber Gherkin reference](https://cucumber.io/docs/gherkin/reference/)
  describes a structured format for executable behavior examples. This Lab
  uses Markdown and `unittest`, not Gherkin.
- [Python `unittest` documentation](https://docs.python.org/3/library/unittest.html)
  explains the standard-library test runner used for the acceptance checks.
- [OpenAPI specification](https://spec.openapis.org/oas/latest.html)
  is a starting point for machine-readable HTTP contracts in larger SDD
  examples. No OpenAPI file or HTTP service exists in this Lab.
