#!/usr/bin/env python3

"""
Module demonstrating asynchronous comprehensions for collecting data from an async generator.
"""

from typing import List
from 0-async_generator import async_generator

async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers using an async comprehension over async_generator.
    """
    return [i async for i in async_generator()]
