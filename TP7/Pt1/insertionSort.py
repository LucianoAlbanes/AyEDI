from linkedlist import length, moveNode, getNode

def insertionSort(linkedList):
    # Case empty list
    if not linkedList.head:
        return None

    # Case only one node
    if not linkedList.head.nextNode:
        return 1

    # Define useful variables
    
    nodeToInsert = linkedList.head.nextNode
    nodeToInsertPos = 1
    while nodeToInsert:
        actualNode = linkedList.head
        counter = 0
        tempNode = None
        while actualNode is not nodeToInsert:
            if nodeToInsert.value < actualNode.value:
                tempNode = nodeToInsert.nextNode
                moveNode(linkedList, nodeToInsertPos, counter)
                break
            counter += 1
            actualNode = actualNode.nextNode
        if tempNode:
            nodeToInsert = tempNode
        else:
            nodeToInsert = nodeToInsert.nextNode
        nodeToInsertPos += 1