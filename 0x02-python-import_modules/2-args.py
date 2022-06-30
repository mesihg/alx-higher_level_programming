#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg_list = sys.argv
    arg_len = len(arg_list) - 1
    if arg_len == 1:
        print("1 argument:")
    elif arg_len == 0:
        print("0 arguments.")
    else:
        print("{} arguments".format(arg_len))
    for item in range(1, arg_len + 1):
        print("{}: {}".format(item, arg_list[item]))
