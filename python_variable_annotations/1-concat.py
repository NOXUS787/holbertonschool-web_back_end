#!/usr/bin/env python3
"""Provides a type-annotated function that concatenates two strings."""


def concat(str1: str, str2: str) -> str:
    """Return the concatenation of two strings.

    Args:
        str1: the string that comes first.
        str2: the string appended to the first.

    Returns:
        str: the two strings joined together.
    """
    return str1 + str2
