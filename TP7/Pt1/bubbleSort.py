from linkedlist import length, getNode, moveNode

def bubbleSort(linkedList):
    # Case empty list
    if not linkedList.head:
        return None
    
    # Case only one node
    if not linkedList.head.nextNode:
        return 1
    
    # Define useful variables
    lengthOfLList = length(linkedList)
    lap = 0
    flagChanges = True # to make a do-while
    
    # Sort
    while flagChanges:
        flagChanges = False
        position = 0
        actualNode = linkedList.head
        # Check from head to last node - lap
        for _ in range(0, lengthOfLList-lap):
            # Check if next node of node has minor value.
            if actualNode.value > actualNode.nextNode.value:
                # Save the real actual node
                actualNode = actualNode.nextNode
                
                # Move the nodes and update the flag
                moveNode(linkedList, position+1, position)
                flagChanges = True
                
            # Check if exist two nodes ahead. else break the current lap
            if not (actualNode.nextNode and actualNode.nextNode.nextNode):
                break
            
            actualNode = actualNode.nextNode
            position += 1
        lap += 1
    return 1