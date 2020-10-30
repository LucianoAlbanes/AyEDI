# Some operations to do with arrays.

# Search for an element on an array.
def search(array, element): #3 OE (9+5n, n=Cant de elementos a comparar hasta la aparicion, peor caso)
    """
    Explanation: 
        Searches for an element in the given array.
    Params:
        array: The array on which you want to perform the search.
        element: The element to search in the given array.
    Return:
        The index where is the element.
        If the element is found multiple times, returns the first index where appears.
        Returns 'None' if the element is not in the array.
    """
    index = None #1 OE
    i = 0 #1 OE
    while (i < len(array)): #3 OE
        if array[i] == element: #2 OE
            index = i #1 OE
            break
        i += 1 #1 OE
    return index #2 OE

# Insert an element on an array
def insert(array, element, position): #4 OE (13+4n, n=Lugares despues de position, peor caso)
    """
    Explanation:
        Inserts an element in a given position on an array.
    Info:
        All other elements are moved one position down.
        The last element will be lost.
    Params:
        array: The array on which you want to perform the insert.
        element: The element to insert in the given array.
        position: The position of the element to insert.
    Return:
        The index where was inserted the element.
        Returns None' if the element can't be inserted.
    """
    # Store the length of the array.
    length = len(array) #3 OE

    # Case if the position is out of bounds.
    if position >= length: #1 OE
        return None #2 OE

    # Moving the rest of the elements one position.
    i = length-1 #1 OE
    while (i > position): #1 OE
        array[i] = array[i-1] #2 OE
        i -= 1 #1 OE

    # Assing the element to the given position.
    array[position] = element #1 OE

    # Return the element position.
    return position #2 OE

# Delete an element on an array.
def delete(array, element): # 3 OE ()
    """
    Explanation:
        Delete an element on an array.
    Info:
        All other elements are moved one position up.
        The last element will be 'None'.
        If exist more than one element, only the first one will be deleted.
    Params:
        array: The array on which you want to perform the delete.
        element: The element to delete in the given array.
    Return:
        The index where was located the deleted element.
        Returns 'None' if the element don't exist on the array.
    """
    # Store the length of the array.
    length = len(array) #1 OE

    # Search for the index of the element.
    index = search(array, element) #10+5n OE

    # Check if none, and end. Otherwise do the deletion.
    if index == None: #1 OE
        return None #1 OE
    else:
        # Move one position up from the index of the element deleted.
        i = 0 #1 OE
        while (i < length-1): # 1
            array[i] = array[i+1] #2 OE
            i +=1 #1 OE
            
        # Assign the last element of the array to 'None'.
        array[length-1] = None #1 OE
        # Return the index where was located the deleted element.
        return index #2 OE

# Count the lenght of the array (without empty elements)
def length(array):
    """
    Explanation: 
        Count the number of active elements in the array.
    Params:
        array: The array on which you want to perform the count.
    Return:
        The number of items that are not 'None'.
    """
    count = 0
    for i in range(0, len(array)):
        if array[i] != None:
            count += 1
    return count

arr = ['P', 'e', 'l', 'o']
delete(arr, arr[2])
print(arr)