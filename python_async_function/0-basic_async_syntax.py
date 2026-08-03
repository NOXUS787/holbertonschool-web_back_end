#!/usr/bin/env python3
"""Provides an asynchronous coroutine that waits for a random delay."""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Wait for a random delay and return how long it waited.

    Args:
        max_delay: the upper bound of the random delay, in seconds.

    Returns:
        float: the number of seconds actually waited.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
