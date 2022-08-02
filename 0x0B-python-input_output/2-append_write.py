#!/usr/bin/python3

"""A function that appends a string to a file"""


def append_write(filename="", text=""):
    """Append contents of text to a file

    Args:
       filename (str): name of the file
       text (str): contents to be appended

    Returns:
       the number of characters added
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
