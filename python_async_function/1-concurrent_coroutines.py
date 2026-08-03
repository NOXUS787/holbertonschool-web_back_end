#!/usr/bin/env python3
"""Runs several wait_random coroutines concurrently and collects their
delays in the order they complete."""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """Spawn wait_random n times and return every delay in ascending
    order.

    Args:
        n: how many coroutines to spawn.
        max_delay: the upper bound passed to each coroutine.

    Returns:
        list: the delays, ordered from shortest to longest.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays: List[float] = []

    for completed in asyncio.as_completed(tasks):
        delays.append(await completed)

    return delays
