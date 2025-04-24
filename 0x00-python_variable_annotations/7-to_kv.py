#!/usr/bin/env python3
"""
This module defines a function that returns a key-value tuple
with a squared value.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Return a tuple with the string and the square of the int/float as a float.
    """
    return (k, float(v ** 2))
