# Queue implementation (FIFO)
# Based on Lists - sequence ADT implementation

from linkedlist import add

# Define operations


def enqueue(queue, element):
    """
    Explanation: 
        Add an element at the beginning of a queue (sequence ADT).
    Params:
        queue: The queue on which you want to add the element.
        element: The element to add.
    """
    # Add the element to the beginning of the stack. add() equivalent.
    add(queue, element)


def dequeue(queue):
    """
    Explanation: 
        Extract the first element added to the queue (sequence ADT).
    Info:
        The extracted element will be removed from the queue.
    Params:
        queue: The queue on which you want perform the extraction.
    Return:
        The extracted element.
        Returns 'None' if the queue is empty.
    """
    # Case if the queue is empty.
    if not queue.head:
        return None

    # Case if only exists one node
    if not queue.head.nextNode:
        # Store the element
        element = queue.head.value

        # Unlink node
        queue.head = None

        # Return element
        return element

    # Go to the previous node to the last node in the queue.
    previousNode = queue.head
    while previousNode.nextNode.nextNode:
        previousNode = previousNode.nextNode

    # Store the element of the last node.
    element = previousNode.nextNode.value

    # Unlink the last node from the queue.
    previousNode.nextNode = None

    # Return the element
    return element
