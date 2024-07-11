from base import Stack


def is_balanced_parentheses(parentheses: str) -> bool:
    """Check to see if a string of parentheses is balanced or not.

    Args:
        parentheses: string of parentheses

    Returns:
        True if the parentheses are balanced, False otherwise
    """
    stack: Stack = Stack()

    for p in parentheses:
        if p == "(":
            stack.push(p)
        elif p == ")":
            if stack.is_empty():
                return False
            stack.pop()

    return stack.is_empty()
