# Implementation plan

This plan derives from [the feature specification](spec.md). Use Python 3.11+
and its standard library so the learner can run the example locally without
installing packages. A single CLI accepts the subtotal as one positional
integer, calculates shipping and total, and prints the specified lines.

Keep the threshold and fee as named constants so the rule is easy to find.
Use `argparse` for command-line parsing and validation. Use `unittest` with
subprocess calls for acceptance checks: this verifies the public CLI, output,
error stream, and exit status rather than only an internal function.

Traceability: FR-1 and FR-2 map to `test_below_minimum_fr1_fr2` and
`test_at_minimum_fr1_fr2`; FR-3 maps to `test_negative_subtotal_fr3`.
No server, database, external package, or deployment infrastructure is needed
for this behavior.
