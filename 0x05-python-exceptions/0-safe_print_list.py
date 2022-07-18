#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    count_num = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            count_num += 1
        except IndexError:
            break
    print()
    return count_num
