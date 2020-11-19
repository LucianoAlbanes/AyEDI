from linkedlist import moveNode, getNode

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
        
        # Move the min value node to the first position of the current lap
        moveNode(linkedList, minValuePosition, lap)
        lap += 1
        # Reassign first node
        actualFirstNode = getNode(linkedList, lap)
    return 1