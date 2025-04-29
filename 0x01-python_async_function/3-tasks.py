#!/usr/bin/env python3
"""
This module creates and returns an asyncio.Task from wait_random.
"""
import asyncio
from typing import Any
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Returns an asyncio.Task that wraps the coroutine wait_random.

    Args:
        max_delay (int): Maximum delay in seconds.

    Returns:
        asyncio.Task: Task object created from wait_random coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))
