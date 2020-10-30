## Sequence ADT implementation

# Define the needed classes
class LinkedList:
    head = None

class Node:
    value = None
    nextNode = None

# Define operations
def add(linkedList, element):
    """
    Explanation: 
        Add an element at the beginning of a LinkedList (sequence ADT).
    Params:
        linkedList: The list on which you want to add the element.
        element: The element to add.
    """
    # Create the new node and store the element.
    newNode = Node()
    newNode.value = element
    
    # Assign the head node to be the second node, if exists
    if linkedList.head:
        newNode.nextNode = linkedList.head
    
    # Assign the new node as the first node
    linkedList.head = newNode

def search(linkedList, element):
    """
    Explanation: 
        Searches for an element in the given list.
    Params:
        linkedList: The list on which you want to perform the search.
        element: The element to search in the given list.
    Return:
        The index where is the element.
        If the element is found multiple times, returns the first index where appears.
        Returns 'None' if the element is not in the array.
    """ 
    # Define the head of the linked list as the actualNode
    actualNode = linkedList.head
    
    # Perform the search
    i = -1 # To start with 0
    while actualNode:
        i += 1
        if actualNode.value == element:
            return i
        actualNode = actualNode.nextNode
    return None

def insert(linkedList, element, position):
    """
    Explanation:
        Inserts an element in a given position on a list.
    Params:
        linkedList: The list on which you want to perform the insert.
        element: The element to insert in the given list.
        position: The position of the element to insert.
    Return:
        The index where was inserted the element.
        Returns 'None' if the given position is out of bounds of the list.
    """
    # Go to the node previous to the given position.
    previousNode = getNode(linkedList, position-1)
    
    # Check if don't exist a previous node (out of bounds).
    if not previousNode:
        return None
    
    # Create the new node and store the element.
    newNode = Node()
    newNode.value = element
    
    # Asign new pointers (.nextNode)
    newNode.nextNode = previousNode.nextNode
    previousNode.nextNode = newNode
    
    # Return the position of the inserted element.
    return position

def delete(linkedList, element):
    """
    Explanation:
        Delete an element on an list.
    Info:
        If exist more than one element, only the first one will be deleted.
    Params:
        linkedList: The list on which you want to perform the delete.
        element: The element to delete in the given list.
    Return:
        The index where was located the deleted element.
        Returns 'None' if the element don't exist on the list.
    """
    # Search and store the position of the element
    position = search(linkedList, element)
    
    # Case if the element was not found.
    if not position:
        return None
    
    # Go to the node previous to the position of the element.
    previousNode = getNode(linkedList, position-1)
    
    # Reasign pointers (.nextNode)
    previousNode.nextNode = previousNode.nextNode.nextNode
    
    # Return the position where was located the deleted element.
    return position

def length(linkedList):
    """
    Explanation: 
        Count the number of elements of the given list.
    Params:
        linkedList: The list on which you want to perform the count.
    Return:
        The number of elements.
    """
    # Define the head of the linked list as the actualNode
    actualNode = linkedList.head
    
    # Perform the count
    count = 0
    while actualNode:
        actualNode = actualNode.nextNode
        count += 1
    return count

def access(linkedList, position):
    """
    Explanation: 
        Access to an element in the given position of the list.
    Params:
        linkedList: The list where is located the element to access.
        position: The position of the element in the list.
    Return:
        The value of the element at the given position.
        Returns 'None' if there is no element for that position.
    """
    # Store the node
    actualNode = getNode(linkedList, position)
    
    # Case if the position is out of bounds.
    if not actualNode:
        return None
    else: # Return the element
        return actualNode.value
    
def getNode(linkedList, position):
    """
    Explanation:
        Go to the node at the given position.
    Params:
        linkedList: The list where is located the node.
        position: The node's position.
    Return:
        The pointer of the node.
        Returns 'None' if the given position is out of bounds of the list.
    """
    # Case if the position is out of bounds.
    if position > length(linkedList):
        return None
    
    # Go to the node with the given position.
    actualNode = linkedList.head
    actualPosition = 0 
    while (actualPosition != position):
        actualNode = actualNode.nextNode
        actualPosition += 1
    
    # Return the pointer.
    return actualNode






Listita = LinkedList()
add(Listita, 'O')
add(Listita, 'N')
add(Listita, 'A')
add(Listita, 'I')
add(Listita, 'C')
add(Listita, 'U')
add(Listita, 'L')

print(access(Listita,0))

"""
print(delete(Listita,'C'))

print('-------')
print(length(Listita))
print(search(Listita, 'I'))
print('---1234123----')
print(search(Listita, 'U'))
print(search(Listita, 'C'))
"""
