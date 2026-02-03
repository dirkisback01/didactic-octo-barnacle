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


def main():
    """Run some example calculations."""
    print("Calculator Examples:")
    print(f"  5 + 3 = {add(5, 3)}")
    print(f"  10 - 4 = {subtract(10, 4)}")
    print(f"  6 * 7 = {multiply(6, 7)}")
    print(f"  15 / 3 = {divide(15, 3)}")


if __name__ == "__main__":
    main()
