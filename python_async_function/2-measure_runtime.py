#!/usr/bin/env python3
"""Measures the average execution time of the wait_n coroutine."""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Return the average time taken per coroutine by wait_n.

    Args:
        n: how many coroutines wait_n should spawn.
        max_delay: the upper bound passed to each coroutine.

    Returns:
        float: the total elapsed time divided by n.
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    elapsed = time.time() - start

    return elapsed / n
