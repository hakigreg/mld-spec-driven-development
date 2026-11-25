# Tutorial: follow a requirement into running code

## 1. Read and predict

Open [the feature spec](../specs/001-shipping-quote/spec.md). Read FR-1 before
looking at code. Predict shipping 5 and total 54 for a subtotal of 49. Predict
free shipping at 50. These two examples test the exact boundary; a single
example below the boundary would leave the meaning of “at 50” uncertain. FR-3
describes an invalid negative subtotal.

The spec says **what** a user should observe. It does not prescribe a language
or function. [The plan](../specs/001-shipping-quote/plan.md) makes those
technical choices, and [the tasks](../specs/001-shipping-quote/tasks.md)
record the implementation sequence.

## 2. Run the deployment

From the project root, use Python 3.11 or later:

```sh
python3 --version
python3 quote.py 49
python3 quote.py 50
```

The first quote should print:

```text
shipping=5
total=54
```

The second should print `shipping=0` and `total=50`. The deployment is
just a local command that exits after printing. No server must be stopped.

## 3. Check acceptance

```sh
python3 -m unittest discover -s tests -v
python3 quote.py -1
```

Expect three passing tests. The negative input deliberately exits with status
2, prints an error on standard error, and prints no quote. Run that command
separately if your shell stops on a nonzero status.

[The tests](../tests/test_quote.py) launch the program as a separate process.
That checks the same public interface the learner uses, including output and
exit status. Their names connect observations to FR-1, FR-2, and FR-3.

## 4. Change the requirement and expose the gap

Change one business rule: below-minimum shipping becomes 7 instead of 5.
In the spec, change FR-1 and its row for 49 to shipping 7 and total 56.
Predict the new result before editing code.

Then change the expected output in `test_below_minimum_fr1_fr2` in
[test_quote.py](../tests/test_quote.py) to `shipping=7\ntotal=56\n`.
Run:

```sh
python3 -m unittest discover -s tests -v
```

That test should fail: the new expected result is 7 and 56, while the program
still prints 5 and 54. The boundary and invalid-input tests should pass.
The failure exposes the gap between the revised requirement and the code.

## 5. Restore agreement

Change `SHIPPING_FEE = 5` to `SHIPPING_FEE = 7` in
[quote.py](../quote.py). Run:

```sh
python3 -m unittest discover -s tests -v
python3 quote.py 49
```

Expect all three tests to pass and the CLI to print `shipping=7` and
`total=56`. Review the spec and test together to confirm they express the
same rule. The design in the plan did not change. Restore the three edited
files to their original values after the exercise.

## Apply the idea elsewhere

The same sequence can guide an API, interface, or data pipeline: clarify the
observable outcome, write representative scenarios and edge cases, choose a
technical plan, implement, and compare the result to the spec. Those other
deployments are illustrative; this Lab verifies only the CLI. Spec Kit's
[quickstart](https://github.github.com/spec-kit/quickstart) offers an agentic
version of the workflow and asks for review between steps.
