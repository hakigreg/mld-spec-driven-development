# Minimum Lab Deployment: Spec Driven Development

This Lab demonstrates one fundamental behavior of Spec Driven Development
(SDD): a written, reviewable requirement drives an acceptance check and the
code that satisfies it. The example is a shipping quote CLI. It charges 5 USD
below a 50 USD subtotal and gives free shipping at 50 USD or more.

## Mental model

`spec.md` defines **what** must happen; `plan.md` selects **how** to build it;
`tasks.md` records the small implementation steps; acceptance tests check the
observable behavior; `quote.py` implements it. A change begins at the spec,
then moves through the test to the code. The human reviews the intended
behavior and the observed result. An AI coding agent can do the translation,
but no agent or SDD toolkit is required to run this Lab.

## Prerequisite

Python 3.11 or later. There are no external packages or secrets. Run all
commands from this project directory.

## Run and verify

```sh
python3 --version
python3 quote.py 49
python3 quote.py 50
python3 -m unittest discover -s tests -v
```

Expected CLI output for `49` is:

```text
shipping=5
total=54
```

For `50`, expect `shipping=0` and `total=50`. The tests should report three
passing cases. `python3 quote.py -1` should exit with status 2 and explain
that the subtotal must be nonnegative.

## Exercise: run → change → observe

1. Run `python3 quote.py 49` and the test command above. Predict the result.
2. Change the below-minimum shipping fee in
   [the specification](specs/001-shipping-quote/spec.md) from 5 to 7, including
   its acceptance example (49 → shipping 7, total 56).
3. Change the expected output in `test_below_minimum_fr1_fr2` in
   [the acceptance test](tests/test_quote.py) to `shipping=7` and `total=56`.
   Run `python3 -m unittest discover -s tests -v`. That test should fail because
   the code still charges 5. This failure makes the spec/code gap visible.
4. Change `SHIPPING_FEE` in [quote.py](quote.py) to 7. Run the tests and
   `python3 quote.py 49` again. Expect all three tests to pass and the CLI to
   print `shipping=7` and `total=56`. Update the plan if the design changes;
   this fee change does not change the design.
5. Restore the three edited files to their original values when finished.

There is no server to stop; each command exits after printing its result.

## Essential files

| File | Purpose |
| --- | --- |
| [spec.md](specs/001-shipping-quote/spec.md) | Requirements and acceptance examples |
| [plan.md](specs/001-shipping-quote/plan.md) | Technical choice and requirement-to-test map |
| [tasks.md](specs/001-shipping-quote/tasks.md) | Baseline work and verification checklist |
| [quote.py](quote.py) | Runnable behavior |
| [test_quote.py](tests/test_quote.py) | Checks the CLI against the spec |

## Learning guide

Read in order or jump to the topic you need:

1. [Concepts and fundamentals](mld/01-concepts-and-fundamentals.md)
2. [Tutorial](mld/02-tutorial.md)
3. [Use cases](mld/03-use-cases.md)
4. [Essential links](mld/04-essential-links.md)
5. [GitHub repositories](mld/05-github-repositories.md)
6. [Best practices](mld/06-best-practices.md)
7. [Bad practices](mld/07-bad-practices.md)
8. [Next iterations](mld/08-next-iterations.md)
