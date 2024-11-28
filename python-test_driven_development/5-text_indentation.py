#!/usr/bin/python3
"""
Defines a function that prints a text with 2 new lines
after each of these characters: '.', '?', and ':'.
"""

def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?', and ':'.

    Args:
        text (str): The input text to format and print.

    Raises:
        TypeError: If `text` is not a string.

    Example:
        >>> text_indentation("Hello. How are you? I'm fine: thanks.")
        Hello.

        How are you?

        I'm fine:

        thanks.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    result = ""
    skip_space = False
    for char in text:
        if skip_space and char == " ":
            continue
        skip_space = False
        result += char
        if char in ".?:":
            result += "\n\n"
            skip_space = True

    print(result.strip())
