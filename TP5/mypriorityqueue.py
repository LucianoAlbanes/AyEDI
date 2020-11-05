# Priority Queue implementation (FIFO)
# Based on Lists - sequence ADT implementation, with priority attribute

# Define classes
class PriorityQueue:
    head = None


class PriorityNode:
    value = None
    nextNode = None
    priority = None

# Define operations


def enqueue_priority(queue, element, priority):
    """
    Explanation: 
        Add an element at the queue, with the given priority.
    Params:
        queue: The queue on which you want to add the element.
        element: The element to add.
        priority: The priority of the element.
    """
    # Create the new node and store the attributes.
    newNode = PriorityNode()
    newNode.value = element
    newNode.priority = priority

    # Define actualNode
    actualNode = queue.head

    # Case if the queue is empty.
    if not actualNode:
        # Assign newNode as head of the queue
        queue.head = newNode
        # Return with the position 0.
        return 0

    # Iterate the queue until appears an node with the same priority.
    position = 0
    while actualNode.nextNode and actualNode.priority < priority:
        position =+ 1
        actualNode = actualNode.nextNode
    
    # Case if position is 0 / Assign head of the queue
    if position == 0 and actualNode.priority > priority:
        newNode.nextNode = queue.head
        queue.head = newNode
    else:
        if actualNode.nextNode:
            newNode.nextNode = actualNode.nextNode
        actualNode.nextNode = newNode
        
    # Return the position in the queue of the inserted element
    return position


def dequeue_priority(queue):
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

PQ = PriorityQueue()

import math, random
for i in range(0,10):
    ran = math.floor(random.random()*10)
    enqueue_priority(PQ, i, 0)

for i in range(0,11):
    print(dequeue_priority(PQ))
