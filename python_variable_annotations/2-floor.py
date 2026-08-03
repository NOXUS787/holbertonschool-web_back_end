#!/usr/bin/env python3
"""Provides a type-annotated function that floors a float."""
import math


def floor(n: float) -> int:
    """Return the floor of a float as an integer.

    Args:
        n: the number to round down.

    Returns:
        int: the largest integer less than or equal to n.
    """
    return math.floor(n)
