#!/usr/bin/python3
for item in range(0, 100):
    if item == 99:
        print("{:d}".format(item))
    else:
        print("{:02d}".format(item), end=", ")
