#!/usr/bin/python3

"""A function that reads a file"""


def read_file(filename=""):
    """Read the contents of a file

    Args:
       filename (str): name of the file
    """
    with open(filename, 'r', encoding="utf-8") as f:
        text = f.read()
        print(text, end="")
