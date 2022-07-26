#!/usr/bin/python3
"""An addition function module """


def add_integer(a, b=98):
    """Return sum of a and b.

    Args:
       a (int): first input number
       b (int): second input number

    Returns:
        The sum of the given args.

    Raises:
       TypeError: if either of a or b is not integer or not float
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
