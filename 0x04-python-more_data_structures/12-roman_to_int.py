#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if not roman_string:
        return 0
    sum = 0
    i = 0
    while i < len(roman_string):
        s1 = roman[roman_string[i]]
        if (i + 1 < len(roman_string)):
            s2 = roman[roman_string[i + 1]]
            if (s1 >= s2):
                sum += s1
                i += 1
            else:
                sum -= s1
                i += 1
        else:
            sum += s1
            i += 1
    return sum
