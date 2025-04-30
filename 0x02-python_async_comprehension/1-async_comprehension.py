#!/usr/bin/env python3
"""
This module is for a coroutine that collects 10 random numbers,
using an async comprehension
"""

from typing import List
from importlib import import_module as using

async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random float numbers from async_generator,
    using async comprehension.

    Returns:
        List[float]: A list of 10 random floats between 0 and 10.
    """
    return [i async for i in async_generator()]
