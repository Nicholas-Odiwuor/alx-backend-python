#!/usr/bin/env python3
"""
Test script for 0-async_generator.py
"""

import asyncio

async_generator = __import__('0-async_generator').async_generator

async def print_yielded_values() -> None:
    """
    Collect and print values yielded by async_generator.
    """
    result = []
    async for val in async_generator():
        result.append(val)
    print(result)

if __name__ == '__main__':
    asyncio.run(print_yielded_values())
