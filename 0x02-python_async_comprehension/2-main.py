#!/usr/bin/env python3
"""
Test script for 2-measure_runtime.py
"""

import asyncio

measure_runtime = __import__('2-measure_runtime').measure_runtime

async def main() -> None:
    """
    Measure and print runtime of four parallel async_comprehension calls.
    """
    runtime = await measure_runtime()
    print(runtime)

if __name__ == '__main__':
    asyncio.run(main())
