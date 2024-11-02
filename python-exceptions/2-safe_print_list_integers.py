#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in range(0, int(x)):
            if str(my_list[i]).isdigit():
                print("{:d}".format(my_list[i]), end="")
                count += 1
            else:
                continue
    except:
        pass
    print()
    return count
