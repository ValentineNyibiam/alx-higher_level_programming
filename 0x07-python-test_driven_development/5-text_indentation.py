#!/usr/bin/python3
"""
Defines a text_indentation function
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines
    after each of these characters: ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # replace .
    replaced = text.replace(". ", ".\n\n")
    # replace ?
    replaced = replaced.replace("? ", "?\n\n")
    # replace :
    replaced = replaced.replace(": ", ":\n\n")

    print(replaced, end="")
