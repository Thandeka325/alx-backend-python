#!/usr/bin/env python3
"""
This modeule safely retrieves the first element of a sequence, if available.
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Return the first element of a sequence or None if the sequence is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
