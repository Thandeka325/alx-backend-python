#!/usr/bin/env python3
"""
This module asynchronous a generator that yields 10 random numbers.
Each number is yielded after a 1-second delay.
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Function yields a random float between 0 and 10 every second, 10 times.

    Returns:
        AsyncGenerator[float, None]: An async generator yielding random floats.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
