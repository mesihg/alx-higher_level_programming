#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    all_keys = list(a_dictionary.keys())
    for ky in all_keys:
        if value == a_dictionary.get(ky):
            del a_dictionary[ky]
    return a_dictionary
