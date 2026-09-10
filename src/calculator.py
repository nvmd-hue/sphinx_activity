"""A simple calculator module for Sphinx documentation testing.

This module provides basic arithmetic operations and serves as a demonstration
of Google-style docstrings being parsed by Sphinx and Napoleon.
"""

from typing import Union

# Custom type alias for numbers
Numeric = Union[int, float]


def add(a: Numeric, b: Numeric) -> Numeric:
    """Calculate the sum of two numbers.

    This is a simple one-line description followed by a detailed explanation.
    You can add multiple paragraphs here to explain the behavior of your function.

    Args:
        a: The first number to add.
        b: The second number to add.

    Returns:
        The arithmetic sum of `a` and `b`.

    Examples:
        >>> add(2, 3)
        5
        >>> add(5.5, 4.5)
        10.0
    """
    return a + b


def divide(dividend: Numeric, divisor: Numeric) -> float:
    """Divide a number by another number.

    Demonstrates how to document exceptions (`Raises`) in Google style.

    Args:
        dividend: The number to be divided.
        divisor: The number to divide by.

    Returns:
        The float result of the division.

    Raises:
        ValueError: If `divisor` is equal to 0, since division by zero
            is mathematically undefined.
    """
    if divisor == 0:
        raise ValueError("The divisor cannot be zero.")

    return float(dividend / divisor)
