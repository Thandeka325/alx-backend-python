#!/usr/bin/env python3
"""
This module safely retrieves a value from a mapping, with an optional default.
"""
from typing import Mapping, Any, TypeVar, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    Return the value for a key in a mapping or a default
    if the key is not found.
    """
    if key in dct:
        return dct[key]
    else:
        return default
