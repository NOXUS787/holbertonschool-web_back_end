#!/usr/bin/env python3
"""Runs several wait_random tasks concurrently and collects their delays
in the order they complete."""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    """Spawn n wait_random tasks and return every delay in ascending
    order.

    Args:
        n: how many tasks to spawn.
        max_delay: the upper bound passed to each task.

    Returns:
        list: the delays, ordered from shortest to longest.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays: List[float] = []

    for completed in asyncio.as_completed(tasks):
        delays.append(await completed)

    return delays
