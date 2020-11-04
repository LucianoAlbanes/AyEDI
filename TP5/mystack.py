# Stack implementation (LIFO)
# Based on Lists - sequence ADT implementation

from linkedlist import add, delete

# Define operations

def push(stack, element):
    """
    Explanation: 
        Add an element at the beginning of a stack (sequence ADT).
    Params:
        stack: The stack on which you want to add the element.
        element: The element to add.
    """
    # Add the element to the beginning of the stack. add() equivalent.
    add(stack, element)


def pop(stack):
    """
    Explanation: 
        Extract the element at the beginning of a stack (sequence ADT).
    Info:
        The extracted element will be removed from the stack.
    Params:
        stack: The stack on which you want perform the extraction.
    Return:
        The extracted element.
        Returns 'None' if the stack is empty.
    """
    # Store the element if exists, otherwise store 'None'
    if stack.head:
        element = stack.head.value
    else:
        element = None

    # Delete the element from the stack.
    delete(stack, element)

    # Return the element
    return element
