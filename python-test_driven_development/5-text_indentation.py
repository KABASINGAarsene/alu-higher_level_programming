#!/usr/bin/python3
"""
Defines a function that prints a text with 2 new lines
after each '.', '?', and ':'.
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
    for char in text:
        result += char
        if char in ".?:":
            result += "\n\n"

    # Remove extra spaces before and after lines
    lines = result.splitlines()
    trimmed_lines = [line.strip() for line in lines]
    print("\n".join(trimmed_lines))
