#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    """
    safe_print_list_integers - Prints the first x elements
    of a list and only integers
    Parameters:
    my_list - List to be printed
    x - Number of elements of the list to be printed

    Return:
    The real number of integers printed
    """
    i = 0
    int_count = 0
    for item in range(x):
        try:
            if type(my_list[i]) is int:
                print("{:d}".format(my_list[i]), end="")
                int_count += 1
                i += 1
            else:
                i += 1
                continue
        except IndexError:
            break
    print()
    return int_count
