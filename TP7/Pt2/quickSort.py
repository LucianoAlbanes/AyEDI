from linkedlist import length, getNode, swapNodes


def quickSort(linkedList):
    '''
    Explanation:
        Sort a linked list using quick sort algorithm, in increasing order.
    Params:
        linkedList: The list to sort.
    Return:
        '1' if the sort was successful.
        Retruns 'None' if the list is empty.
    '''
    # Case empty list
    if not linkedList.head:
        return None

    # Case only one node
    if not linkedList.head.nextNode:
        return 1

    # Store length and call aux function
    lengthOfLList = length(linkedList)
    quickSortAux(linkedList, 0, lengthOfLList-1)
    return 1


def quickSortAux(linkedList, fromPosition, toPosition):
    if fromPosition < toPosition:
        # Find pivot position (Median of three)
        a = getNode(linkedList, fromPosition)
        b = getNode(linkedList, int((fromPosition+toPosition)/2))
        c = getNode(linkedList, toPosition)
        pivot = None
        pivotPosition = None

        if (a.value <= b.value <= c.value) or (c.value <= b.value <= a.value):
            pivot = b
            pivotPosition = int((fromPosition+toPosition)/2)
        elif (b.value <= a.value <= c.value) or (c.value <= a.value <= b.value):
            pivot = a
            pivotPosition = fromPosition
        else:
            pivot = c
            pivotPosition = toPosition

        # Sorting Part
        # Move pivot to the beginning of the section of the list
        swapNodes(linkedList, pivotPosition, fromPosition)

        # Define useful counters and nodes
        borderNode = pivot
        borderNodePosition = fromPosition
        actualNode = borderNode

        # Swap the nodes with lower value than the pivot
        for actualNodePosition in range(fromPosition, toPosition+1):
            if actualNode.value < pivot.value:
                borderNodePosition += 1
                swapNodes(linkedList, actualNodePosition, borderNodePosition)
                actualNode = getNode(linkedList, actualNodePosition)
            actualNode = actualNode.nextNode

        # Move the pivot to the correct position
        swapNodes(linkedList, fromPosition, borderNodePosition)

        # Recursive part
        quickSortAux(linkedList, fromPosition, borderNodePosition-1)
        quickSortAux(linkedList, borderNodePosition+1, toPosition)
