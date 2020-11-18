from linkedlist import length, getNode, moveNode

def sortLinkedList(linkedList, fromPosition):
    '''
    Explanation:
        Sort a linked list, in increasing order.
    Params:
        linkedList: The list to sort.
        fromPosition: The position of the node from which start to perform the sorting
    Return:
        The sorted linked list.
        Returns 'None' if the linked list is empty or the given position is out of bounds.
    '''
    lengthOfLList = length(linkedList)
    
    # Base case
    if lengthOfLList-1 == fromPosition:
        return linkedList
    
    # Empty list case
    if not linkedList.head:
        return None
    
    # Out of bounds case
    if fromPosition >= lengthOfLList:
        return None

    # General case
    actualNode = getNode(linkedList, fromPosition)
    minValueNode = actualNode
    actualPosition = fromPosition
    minValuePosition = actualPosition

    while actualNode:
        if actualNode.value < minValueNode.value:
            minValueNode = actualNode
            minValuePosition = actualPosition
        actualNode = actualNode.nextNode
        actualPosition += 1
    moveNode(linkedList, minValuePosition, fromPosition)
    
    return sortLinkedList(linkedList, fromPosition + 1)


# Basic interface
from linkedlist import add, access, LinkedList
import random  # Only for testing

# Create and fill the list
print('Generando una lista con 10 valores aleatorios...')

listOfNumbers = LinkedList()
for _ in range(0, 10):
    add(listOfNumbers, random.randint(0, 10))

# Print unsorted list
print('[', end="")
for i in range(0, 10):
    if i != 0:
        print(', ', end="")
    print(str(access(listOfNumbers, i)), end="")
print(']')

# Sort
print('\nOrdenando la lista...')
sortLinkedList(listOfNumbers, 0)

# Print sorted list
print('[', end="")
for i in range(0, 10):
    if i != 0:
        print(', ', end="")
    print(str(access(listOfNumbers, i)), end="")
print(']')
