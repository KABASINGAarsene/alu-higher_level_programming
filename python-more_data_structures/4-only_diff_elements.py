#!/usr/bin/python3


def only_diff_elements(set_1, set_2):
    set_3 = set()
    for element1 in set_1:
        for element2 in set_2:
            if element1 == element2:
                set_3.add(element1)
    set_1 = set_1.difference(set_3)
    set_2 = set_2.difference(set_3)
    diff_set = set_1.union(set_2)
    return diff_set
