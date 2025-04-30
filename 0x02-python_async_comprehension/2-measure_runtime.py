#!/usr/bin/env python3
"""
This module is for coroutine that measures runtime of async_comprehension,
runs 4 times in parallel.
"""

import asyncio
import time
from importlib import import_module as using

async_comprehension = using('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure the total runtime of running async_comprehension in parallel.

    Returns:
        float: Total elapsed time in seconds.
    """
    start_time = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    total_time = time.perf_counter() - start_time
    return total_time
