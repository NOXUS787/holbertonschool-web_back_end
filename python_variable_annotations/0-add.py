#!/usr/bin/env python3
"""Provides a type-annotated function that adds two floats."""


def add(a: float, b: float) -> float:
    """Return the sum of two floats.

    Args:
        a: the first number to add.
        b: the second number to add.

    Returns:
        float: the sum of a and b.
    """
    return a + b
