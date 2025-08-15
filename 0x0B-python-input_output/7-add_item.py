#!/usr/bin/python3
"""
This is a script that adds all arguments to a Python list, 
and then save them to a file.
"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


# check if the file already exist with content, then load
list_to_save = load_from_json_file("add_item.json")

# extract list from command line input
index = 0
while index < len(sys.argv):
    if index > 0:
        list_to_save.append(sys.argv[index])
    index += 1

# save to file
save_to_json_file(list_to_save, "add_item.json")

# print(list_to_save)
