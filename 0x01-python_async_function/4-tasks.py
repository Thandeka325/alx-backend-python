#!/usr/bin/env python3
"""
This module spawns multiple tasks using task_wait_random
and collects the results.
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random n times with max_delay
    and returns list of delays in ascending order.

    Args:
        n (int): Number of times to spawn the task.
        max_delay (int): Maximum delay in seconds.

    Returns:
        List[float]: List of delays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = []

    for task in asyncio.as_completed(tasks):
        result = await task
        delays.append(result)

    return delays
