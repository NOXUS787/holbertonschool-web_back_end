#!/usr/bin/env python3
"""Provides a type-annotated function that builds a multiplier
function."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies a float by a fixed factor.

    Args:
        multiplier: the factor the returned function multiplies by.

    Returns:
        Callable: a function taking one float and returning a float.
    """
    def multiply(value: float) -> float:
        """Multiply the given value by the captured multiplier."""
        return value * multiplier

    return multiply
