#!/usr/bin/env python3
"""Provides a type-annotated function that sums a list of floats."""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Return the sum of a list of floats.

    Args:
        input_list: the floats to add together.

    Returns:
        float: the total of every element in the list.
    """
    return sum(input_list)
