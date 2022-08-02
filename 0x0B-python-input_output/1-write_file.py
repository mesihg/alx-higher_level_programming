#!/usr/bin/python3

"""A function that writes to a file"""


def write_file(filename="", text=""):
    """Write contents of text to a file

    Args:
       filename (str): name of the file
       text (str): contents to be written

    Returns:
       the number of characters printed
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
