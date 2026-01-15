#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# ///
"""Fibonacci number calculator using inline uv dependencies."""


def fibonacci(n: int) -> int:
    """Return the nth Fibonacci number (0-indexed).

    F(0) = 0, F(1) = 1, F(n) = F(n-1) + F(n-2)
    """
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 0
    if n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        n = int(sys.argv[1])
        print(f"fibonacci({n}) = {fibonacci(n)}")
    else:
        # Demo first 10 fibonacci numbers
        for i in range(10):
            print(f"fibonacci({i}) = {fibonacci(i)}")
