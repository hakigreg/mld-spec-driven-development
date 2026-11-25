"""A small shipping quote CLI driven by specs/001-shipping-quote/spec.md."""

import argparse


FREE_SHIPPING_MINIMUM = 50
SHIPPING_FEE = 5


def quote(subtotal: int) -> tuple[int, int]:
    """Return (shipping, total) for a nonnegative whole-dollar subtotal."""
    if subtotal < 0:
        raise ValueError("subtotal must be nonnegative")
    shipping = 0 if subtotal >= FREE_SHIPPING_MINIMUM else SHIPPING_FEE
    return shipping, subtotal + shipping


def main() -> None:
    parser = argparse.ArgumentParser(description="Quote shipping for a whole-dollar subtotal.")
    parser.add_argument("subtotal", type=int, help="nonnegative whole-dollar subtotal")
    args = parser.parse_args()
    if args.subtotal < 0:
        parser.error("subtotal must be nonnegative")
    shipping, total = quote(args.subtotal)
    print(f"shipping={shipping}")
    print(f"total={total}")


if __name__ == "__main__":
    main()
