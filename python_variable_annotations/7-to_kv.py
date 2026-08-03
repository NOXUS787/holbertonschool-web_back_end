#!/usr/bin/env python3
"""Provides a type-annotated function that pairs a string with the
square of a number."""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple of a string and the square of a number.

    Args:
        k: the string placed first in the tuple.
        v: the number whose square is placed second.

    Returns:
        tuple: the string k and the square of v.
    """
    return (k, v * v)
