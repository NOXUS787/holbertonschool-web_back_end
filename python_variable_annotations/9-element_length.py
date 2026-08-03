#!/usr/bin/env python3
"""Provides a duck-typed function that pairs each element of an iterable
with its length."""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return each element of an iterable paired with its length.

    Args:
        lst: an iterable of sequences that each support len().

    Returns:
        list: tuples of each element and its length.
    """
    return [(i, len(i)) for i in lst]
