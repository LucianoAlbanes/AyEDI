from linkedlist import length, getNode, swapNodes, moveNode
from linkedlist import LinkedList, add, access  # TESTING


def quickSort(linkedList):
    # Case empty list
    if not linkedList.head:
        return None

    # Case only one node
    if not linkedList.head.nextNode:
        return 1

    # Store length and call aux function
    lengthOfLList = length(linkedList)
    quickSortAux(linkedList, 0, lengthOfLList-1)


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
        
        # Order 
        swapNodes(linkedList, pivotPosition, fromPosition)
        
        borderNode = pivot.nextNode
        borderNodePosition = fromPosition + 1
        actualNode = borderNode.nextNode
        
        for actualNodePosition in range(fromPosition+2, toPosition+1):
            if actualNode.value < pivot.value:
                swapNodes(linkedList, actualNodePosition, borderNodePosition)
                borderNodePosition += 1
                actualNode = getNode(linkedList, actualNodePosition)
            actualNode = actualNode.nextNode
        
        # Move the pivot to the correct position
        
        borderNode = getNode(linkedList, borderNodePosition)
        if borderNode.value < pivot.value:
            swapNodes(linkedList, fromPosition, borderNodePosition)
        else:
            moveNode(linkedList, fromPosition, borderNodePosition-1)
            borderNodePosition -=1
        
        # Recursive part
        quickSortAux(linkedList, fromPosition, borderNodePosition-1)
        quickSortAux(linkedList, borderNodePosition+1, toPosition)



LL = LinkedList()
add(LL, 2)
add(LL, 0)
add(LL, 1)
add(LL, 0)
add(LL, 1)

def printList(linkedList):
    print('[', end="")
    for i in range(0, length(linkedList)):
        if i != 0:
            print(', ', end="")
        print(str(access(linkedList, i)), end="")
    print(']')

printList(LL)
    
quickSort(LL)

printList(LL)