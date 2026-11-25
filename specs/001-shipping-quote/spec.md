# Feature specification: shipping quote

## Why

A shopper needs to know the shipping charge and order total before checkout.
This feature provides one predictable quote for a whole-dollar subtotal.

## Scope and vocabulary

The **subtotal** is a nonnegative integer number of US dollars before
shipping. **Shipping** is the flat charge. **Total** is subtotal plus shipping.
Taxes, discounts, currencies other than USD, and persistence are outside this
feature.

## Requirements

- **FR-1:** Given a subtotal below 50, charge 5 for shipping. Given a subtotal
  of 50 or more, charge 0. The boundary is inclusive: 50 receives free shipping.
- **FR-2:** Print exactly two lines to standard output: `shipping=<amount>` and
  `total=<amount>`, with integer amounts and a trailing newline. Total equals
  subtotal plus shipping.
- **FR-3:** Reject a negative subtotal with a nonzero exit status, an error
  message containing `subtotal must be nonnegative` on standard error, and no
  standard output.

## Acceptance examples

| Input subtotal | Expected shipping | Expected total | Requirement |
| ---: | ---: | ---: | --- |
| 49 | 5 | 54 | FR-1, FR-2 |
| 50 | 0 | 50 | FR-1, FR-2 |
| -1 | Error | No output | FR-3 |

The acceptance examples specify observable behavior. They do not prescribe a
programming language, file layout, or internal algorithm.
