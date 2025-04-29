#!/usr/bin/env python3
"""
A module for asynchronous random delay.

This module provides a coroutine that waits for a random amount of time up to max_delay seconds
and returns the actual delay.
"""

import asyncio
import random
from typing import Union


def wait_random(max_delay: int = 10) -> float:
    """
    Wait for a random delay between 0 and max_delay seconds and return the delay.

    Args:
        max_delay (int): Maximum delay in seconds (inclusive). Defaults to 10.

    Returns:
        float: The actual delay waited.
    """
    delay: float = random.uniform(0, max_delay)
    return asyncio.sleep(delay, result=delay)

