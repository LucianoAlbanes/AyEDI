from linkedlist import getNode, swapNodes


def selectionSort(linkedList):
    # Case empty list
    if not linkedList.head:
        return None

    # Case only one node
    if not linkedList.head.nextNode:
        return 1

    # Define useful variables
    lap = 0
    actualFirstNode = linkedList.head

    # Sort
    while actualFirstNode:
        actualNode = actualFirstNode
        actualPosition = lap
        minValueNode = actualNode
        minValuePosition = actualPosition

        # Search the lowest value from lap
        while actualNode:
            if minValueNode.value > actualNode.value:
                minValueNode = actualNode
                minValuePosition = actualPosition
            actualNode = actualNode.nextNode
            actualPosition += 1

        # Swap the min value node with the first node of the lap
        swapNodes(linkedList, lap, minValuePosition)
        lap += 1
        # Reassign first node
        actualFirstNode = getNode(linkedList, lap)
    return 1
