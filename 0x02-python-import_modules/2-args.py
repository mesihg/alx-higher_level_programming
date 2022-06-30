#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg_len = len(sys.argv)
    if arg_len == 1:
        print("1 argument:")
    elif arg_len == 0:
        print("0 arguments.")
    else:
        print("{} arguments".format(arg_len - 1))
    for item in range(1, arg_len):
        print("{}: {}".format(item, sys.argv[item]))
