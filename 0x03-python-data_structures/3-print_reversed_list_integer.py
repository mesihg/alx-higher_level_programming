#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list == None:
        return None
    for item in my_liset[::-1]:
        print("{:d}".format(item))
