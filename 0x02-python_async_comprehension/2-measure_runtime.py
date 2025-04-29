#!/usr/bin/env python3
"""Measure runtime of four parallel async comprehensions"""

import asyncio
import time
from typing import Callable
from 1-async_comprehension import async_comprehension


async def measure_runtime() -> float:
    """
    Executes async_comprehension 4 times in parallel and measures total runtime.
    Returns:
        float: total runtime in seconds.
    """
    start_time = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.perf_counter()
    return end_time - start_time

