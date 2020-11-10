# Priority Queue implementation (FIFO).
# Based on Lists - sequence ADT implementation.

# Define classes.
class PriorityQueue:
    head = None

class PriorityNode:
    value = None
    nextNode = None
    priority = None

# Define operations.

def enqueue_priority(queue, element, priority):
    """
    Explanation: 
        Add an element at the queue, with the given priority.
    Params:
        queue: The queue on which you want to add the element.
        element: The element to add.
        priority: The priority of the element.
    Return:
        The position in the queue of the added element.
    """
    # Create the new node and store the element.
    newNode = PriorityNode()
    newNode.value = element
    newNode.priority = priority

    # Assign the head node to be the second node.
    newNode.nextNode = queue.head

    # Assign the new node as the first node.
    queue.head = newNode

    # Return the position of the element.
    # Always 0 because the node is stored as head.
    return 0

def dequeue_priority(queue):
    """
    Explanation: 
        Extract the element with the highest priority of a queue (sequence ADT).
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

    # Case if only exists one node.
    if not queue.head.nextNode:
        # Store the element.
        element = queue.head.value

        # Unlink node.
        queue.head = None

        # Return element.
        return element
    
    # Navigate all the nodes of the queue.
    previousNode = queue.head # Previous to the highest priority node.
    actualNode = queue.head
    while actualNode.nextNode: 
        if actualNode.nextNode.priority >= previousNode.nextNode.priority:
            previousNode = actualNode
        actualNode = actualNode.nextNode

    # Store the element of the node.
    element = previousNode.nextNode.value

    # Unlink the the node from the queue.
    previousNode.nextNode = previousNode.nextNode.nextNode

    # Return the element.
    return element