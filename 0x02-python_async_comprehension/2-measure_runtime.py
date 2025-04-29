#!/usr/bin/env python3
"""
2-measure_runtime module.

This module defines a coroutine to measure the total runtime of four
parallel executions of async_comprehension.
"""

import asyncio
import time
from typing import Coroutine

# Import the async_comprehension coroutine from the previous task module
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure the total execution time of four parallel calls to
    async_comprehension.

    Returns:
        float: Total runtime in seconds.
    """
    start: float = time.time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end: float = time.time()
    return end - start

