#!/usr/bin/env python3
"""Provides an asynchronous generator that yields random numbers."""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Yield ten random floats, waiting one second before each.

    Returns:
        AsyncGenerator: a stream of ten floats between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
