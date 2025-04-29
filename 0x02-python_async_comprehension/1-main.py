#!/usr/bin/env python3
"""
Test script for 1-async_comprehension.py
"""

import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension

async def main() -> None:
    """
    Invoke async_comprehension and print its returned list.
    """
    result = await async_comprehension()
    print(result)

if __name__ == '__main__':
    asyncio.run(main())
