#!/usr/bin/env python3

# 0x03. Unittests and Integration Tests

This project is about writing unit and integration tests in Python.

## Requirements

- Ubuntu 18.04 LTS
- Python 3.7
- pycodestyle (version 2.5)

## Project Structure

- `utils.py`: Utility functions
- `client.py`: Client code interacting with external APIs
- `fixtures.py`: Mock data for testing
- `tests/`: Unit and integration test files

## How to Run Tests

```bash
python3 -m unittest tests/test_utils.py
python3 -m unittest tests/test_client.py
python3 -m unittest tests/test_integration.py

