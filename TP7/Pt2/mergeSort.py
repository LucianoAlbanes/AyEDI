from linkedlist import LinkedList, length, getNode, add, Node, insert, delete


def mergeSort(linkedList):
    '''
    Explanation:
        Sort a linked list using merge sort algorithm, in increasing order.
    Params:
        linkedList: The list to sort.
    Return:
        The sorted linked list.
        Retruns 'None' if the list is empty.
    '''
    # Case empty list
    if not linkedList.head:
        return None
    
    # Base case
    if not linkedList.head.nextNode:
        return linkedList

    # Divide the linked list in two parts
    lengthOfLList = length(linkedList)
    leftPart = copyLinkedList(linkedList, 0, int(lengthOfLList/2))
    rightPart = copyLinkedList(linkedList, int(lengthOfLList/2), lengthOfLList)

    # Recursively divide and sort the two parts, until base case
    leftPart = mergeSort(leftPart)
    rightPart = mergeSort(rightPart)

    # Return the merge of the parts
    return mergeSortAux(leftPart, rightPart)


def mergeSortAux(leftPart, rightPart):
    # Create the output List and counter of the q elements
    outputLList = LinkedList()
    outputLListCounter = 0

    # Compare the numbers if two parts have values
    while leftPart.head and rightPart.head:
        if leftPart.head.value > rightPart.head.value:
            insert(outputLList, rightPart.head.value, outputLListCounter)
            delete(rightPart, rightPart.head.value)
        else:
            insert(outputLList, leftPart.head.value, outputLListCounter)
            delete(leftPart, leftPart.head.value)
        outputLListCounter += 1

    # Add residue values
    while leftPart.head:
        insert(outputLList, leftPart.head.value, outputLListCounter)
        delete(leftPart, leftPart.head.value)
        outputLListCounter += 1

    while rightPart.head:
        insert(outputLList, rightPart.head.value, outputLListCounter)
        delete(rightPart, rightPart.head.value)
        outputLListCounter += 1

    # Return the sorted list
    return outputLList


def copyLinkedList(originalLinkedList, fromPosition, toPosition):
    # Return a section of a list.
    outputLList = LinkedList()
    actualNodeInput = getNode(originalLinkedList, fromPosition)
    actualNodeOutput = None
    for i in range(fromPosition, toPosition):
        if i == fromPosition:  # case if head
            add(outputLList, actualNodeInput.value)
            actualNodeOutput = outputLList.head
        else:
            newNode = Node()
            newNode.value = actualNodeInput.value
            actualNodeOutput.nextNode = newNode
            actualNodeOutput = actualNodeOutput.nextNode
        actualNodeInput = actualNodeInput.nextNode
    return outputLList
