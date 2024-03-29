#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """
    Prints all integers of a list in reverse order
    Parameters:
    - my_list: The list to be printed
    """
    if my_list:
        i = len(my_list) - 1
        while i >= 0:
            print("{:d}".format(my_list[i]))
            i -= 1
