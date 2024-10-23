#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    cmd_args = len(argv) - 1

    if cmd_args == 0:
        print("{} arguments.".format(cmd_args))
    elif cmd_args == 1:
        print("{} argument:".format(cmd_args))
        print("{}: {}".format(cmd_args, argv[1]))
    else:
        print("{} arguments:".format(cmd_args))
        for indx, i in enumerate(argv[1:], start=1):
            print("{}: {}".format(indx, i))
