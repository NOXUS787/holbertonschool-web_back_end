#!/usr/bin/env python3
"""Provides a type-annotated function that sums a list holding both
integers and floats."""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return the sum of a list of integers and floats.

    Args:
        mxd_lst: the numbers to add together.

    Returns:
        float: the total of every element in the list.
    """
    return float(sum(mxd_lst))
