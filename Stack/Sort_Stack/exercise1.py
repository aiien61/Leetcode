from base import Stack

def sort_stack(stack: Stack) -> None:
    """Sort the stack in ascending order

    Args:
        stack: stack to be sorted
    """
    if stack.is_empty():
        return None
    
    sorted_stack: Stack = Stack()

    temp: int | None = stack.pop()

    while True:
        if stack.is_empty() and temp is None:
            break

        if sorted_stack.is_empty():
            sorted_stack.push(temp)
            temp = stack.pop()
            continue
        
        if temp < sorted_stack.peek():
            stack.push(sorted_stack.pop())
            continue

        sorted_stack.push(temp)
        temp = stack.pop()
    
    while not sorted_stack.is_empty():
        stack.push(sorted_stack.pop())
    
    return None
