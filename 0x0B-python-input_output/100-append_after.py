#!/usr/bin/python3

"""A function that inserts a line of text to a file"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file

    Args:
       filename (str): name of the file
       search_string (str): search parameter
       new_string (str): contents to be updated
    """
    new_text_content = ""
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f.readlines():
            new_text_content += line
            if search_string in line:
                new_text_content += new_string

    with open(filename, 'w', encoding='utf-8') as wr:
        wr.write(new_text_content)
