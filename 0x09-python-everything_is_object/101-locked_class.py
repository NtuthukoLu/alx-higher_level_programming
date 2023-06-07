#!/usr/bin/python3
"""A locked class Module"""


class LockedClass:
    """Stops User from instanting new locked class"""
    __slots__ = ["first_name"]
    