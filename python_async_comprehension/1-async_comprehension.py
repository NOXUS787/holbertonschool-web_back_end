#!/usr/bin/env python3
"""Collects values from an asynchronous generator using an async
comprehension."""
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collect ten random numbers from async_generator.

    Returns:
        list: the ten floats produced by the generator.
    """
    return [number async for number in async_generator()]
