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
    Return:
        The position in the queue of the added element.
    """
    # Create the new node and store the attributes.
    newNode = PriorityNode()
    newNode.value = element
    newNode.priority = priority

    # Case if queue is empty.
    if not queue.head:
        queue.head = newNode
        return 0

    # Define actualNode as head of the queue.
    actualNode = queue.head

    # Navigate until find a Node with major priority.
    previousNode = None  # Will be used if exist a node with same priority.
    position = 0
    while priority > actualNode.priority:
        position += 1
        if not actualNode.nextNode:
            break
        if priority == actualNode.nextNode.priority:
            previousNode = actualNode
        actualNode = actualNode.nextNode

    # Assign new pointers (.nextNode)
    if queue.head.priority >= priority:  # Case lowest priority
        newNode.nextNode = actualNode
        queue.head = newNode
    elif actualNode.priority == priority:  # Case with existing priority.
        newNode.nextNode = actualNode
        previousNode.nextNode = newNode
    else:  # Case with new priority.
        newNode.nextNode = actualNode.nextNode
        actualNode.nextNode = newNode

    # Return the position.
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
enqueue_priority(PQ, 'El Pepe', 2)
enqueue_priority(PQ, 'El Sabroson', 0)
enqueue_priority(PQ, 'El Onur', 1)
enqueue_priority(PQ, 'El Sech', 3)
enqueue_priority(PQ, 'El Mamahuevaso', 4)
enqueue_priority(PQ, 'El Culiao', 3)
enqueue_priority(PQ, 'El Loquito', 2)
enqueue_priority(PQ, 'El Loquito2', 2)

for i in range(0, 7):
    print(dequeue_priority(PQ))
