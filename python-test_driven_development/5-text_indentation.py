#!/usr/bin/python3
"""
Function to print a text with 2 new lines after each '.', '?', and ':'.
"""

def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?', and ':'.
    
    Args:
        text (str): The input text to format and print.
    
    Raises:
        TypeError: If `text` is not a string.
    
    Example:
        >>> text_indentation("Hello. How are you? I'm fine: thank you.")
        Hello.
        
        How are you?
        
        I'm fine:
        
        thank you.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    i = 0
    while i < len(text):
        if text[i] in ".?:":
            print(text[i])
            print()  # print two new lines after ., ? or :
            i += 1
            # Skip any extra spaces that follow these characters
            while i < len(text) and text[i] == ' ':
                i += 1
        else:
            print(text[i], end="")  # print the character without a newline
            i += 1
