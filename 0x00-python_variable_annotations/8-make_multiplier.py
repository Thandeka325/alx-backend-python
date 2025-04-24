#!/usr/bin/env python3
"""
This module returns a multiplier function for a given float.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Return a function that multiplies a float by the given multiplier.
    """
    return lambda x: x * multiplier
