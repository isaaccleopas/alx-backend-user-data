#!/usr/bin/env python3
"""Filtered Logger Module"""
import os
import re
import logging
from typing import List


def filter_datum(
        fields: List[str], redaction: str, message: str, separator: str
        ) -> str:
    """Filters log line"""
    for field in fields:
        pattern = f'{field}=[^;]+'
    return (re.sub(pattern, f'{field}={redaction}', message))
