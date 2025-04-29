#!/usr/bin/env python3
"""
Measure the average runtime of executing wait_n concurrently.

This module provides a function to measure how long, on average,
it takes to run wait_n(n, max_delay) by timing the total execution
and dividing by the number of tasks.
"""

import time
import asyncio
from typing import Union

# Import wait_n from the previous async module
from 1-concurrent_coroutines import wait_n  # adjust module name if different


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time of wait_n(n, max_delay) and return the average per task.

    Args:
        n (int): Number of concurrent coroutines to run.
        max_delay (int): Maximum delay for each coroutine.

    Returns:
        float: Average runtime per coroutine (total_time / n).
    """
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    total_time = time.time() - start
    return total_time / n

