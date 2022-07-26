#!/usr/bin/python3
"""A module for locked class."""


class LockedClass:
    """Prevents from creating a new instance except first_name attr"""

    __slots__ = ["first_name"]
