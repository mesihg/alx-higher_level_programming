#!/usr/bin/python3
"""A function that prints some indentation module"""


def text_indentation(text):
    """Prints a text with 2 new lines after some character group: ., ? and :.

    Args:
       text (str): input string

    Raises:
       TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    c = 0
    while c < len(text) and text[c] == ' ':
        c += 1

    while c < len(text):
        print(text[c], end="")
        if text[c] == "\n" or text[c] in ".?:":
            if text[c] in ".?:":
                print("\n")
            c += 1
            while c < len(text) and text[c] == ' ':
                c += 1
            continue
        c += 1
