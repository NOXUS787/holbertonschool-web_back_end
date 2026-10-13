#!/usr/bin/env python3
"""Simple helper function module for computing pagination index ranges."""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Return a tuple with the start and end indexes for a given page.

    Page numbers are 1-indexed, so page 1 starts at index 0. The end index
    is exclusive, matching Python list slicing semantics.
    """
    start: int = (page - 1) * page_size
    end: int = start + page_size
    return (start, end)
