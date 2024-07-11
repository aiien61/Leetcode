from __future__ import annotations
from base import Stack

def reverse_string(string: str) -> str:
    """Return a new string with the letters in reverse order.

    Args:
        string: string to be reversed

    Returns:
        new string with letters in reverse order
    """
    stack: Stack = Stack()

    for letter in string:
        stack.push(letter)
    
    reversed_string: str = ""
    while not stack.is_empty():
        reversed_string += stack.pop()

    return reversed_string