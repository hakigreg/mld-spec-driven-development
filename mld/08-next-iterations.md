# Next iterations

These are suggestions, not implemented Lab behavior. Make one change at a
time and return to the spec → check → code loop.

1. **Add the zero subtotal example.** Add an acceptance example for 0 and
   check that it prints shipping 5 and total 5. This teaches how an edge case
   extends coverage without changing the rule.
2. **Change the free-shipping threshold.** Change 50 to 60, revise boundary
   examples at 59 and 60, then implement. Observe the old test at 50 fail
   until expectations and code agree. This teaches boundary-driven revision.
3. **Accept cents.** Specify decimal input and a precise rounding rule before
   changing parsing. Observe how a seemingly small input change forces a
   design decision that the whole-dollar Lab avoided.
4. **Expose an HTTP quote endpoint.** Specify the request, response, and
   errors before adding a small server. Observe the same business rule
   through a new public interface. This teaches the distinction between a
   feature rule and an interface contract.
