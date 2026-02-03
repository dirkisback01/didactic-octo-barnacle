"""
A simple calculator module for learning Claude Code.
"""


def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Subtract b from a."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b


def divide(a: float, b: float) -> float:
    """Divide a by b.

    Raises:
        ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(base: float, exponent: float) -> float:
    """Raise base to the power of exponent.

    Args:
        base: The base number.
        exponent: The exponent to raise the base to.

    Returns:
        base raised to the power of exponent.
    """
    return base ** exponent


def sqrt(n: float) -> float:
    """Calculate the square root of a number.

    Args:
        n: The number to find the square root of.

    Returns:
        The square root of n.

    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return n ** 0.5


def main():
    """Run some example calculations."""
    print("Calculator Examples:")
    print(f"  5 + 3 = {add(5, 3)}")
    print(f"  10 - 4 = {subtract(10, 4)}")
    print(f"  6 * 7 = {multiply(6, 7)}")
    print(f"  15 / 3 = {divide(15, 3)}")
    print(f"  2 ^ 3 = {power(2, 3)}")
    print(f"  sqrt(16) = {sqrt(16)}")


if __name__ == "__main__":
    main()
