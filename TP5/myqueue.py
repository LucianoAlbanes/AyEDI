# Queue implementation (FIFO)
# Based on Lists - sequence ADT implementation

from linkedlist import add, length, access, getNode, LinkedList

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
        Extract the element at the end of a queue (sequence ADT).
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
    
    # Store the length of the queue and the element to be extracted.
    _length = length(Q)
    element = access(Q, _length-1)
    
    # Case if only exists one node
    if not queue.head.nextNode:
        queue.head = None
        return element
    
    # Go to the previous node to the last node in the queue.
    previousNode = getNode(Q, _length-2)
    
    # Unlink the last node from the queue.
    previousNode.nextNode = None
    
    # Return the element
    return element
