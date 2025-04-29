#!/usr/bin/env python3
"""
This module runs multiple asynchronous wait_random coroutines concurrently.
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with the specified max_delay.

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): Maximum number of seconds to wait in each coroutine.

    Returns:
        List[float]: A list of delays returned by wait_random
        in ascending order.
    """
    delays = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    return sorted(delays)
