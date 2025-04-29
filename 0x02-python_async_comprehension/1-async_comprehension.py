#!/usr/bin/env python3
"""
1-async_comprehension module.

Provides a coroutine to collect random numbers from async_generator
using an async comprehension.
"""

from typing import List

# Import the async_generator coroutine from the previous task
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collect 10 random numbers from async_generator into a list.

    Returns:
        List[float]: list of 10 randomly generated floats.
    """
    result: List[float] = [
        number async for number in async_generator()
    ]
    return result

