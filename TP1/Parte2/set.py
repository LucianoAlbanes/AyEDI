# Return a ADT set and remove duplicates
def Create_Set(Array):
    outputArray = []
    for element in Array:
        if element not in outputArray:
            outputArray.append(element)
    return outputArray

# Return the union between two arrays, iff the arrays not contain duplicated elements
def Union(ArrayS, ArrayT):
    if (check_duplicates(ArrayS) or check_duplicates(ArrayT)):
        print('ERROR: Alguno de los arrays ingresados posee elementos duplicados.')
    else:
        outputArray = Create_Set(ArrayS + ArrayT) #Remove duplicates 
        return outputArray

# Return the intersection between two arrays, iff the arrays not contain duplicated elements
def Intersection(ArrayS, ArrayT):
    if (check_duplicates(ArrayS) or check_duplicates(ArrayT)):
        print('ERROR: Alguno de los arrays ingresados posee elementos duplicados.')
    else:
        outputArray = []
        for element in ArrayS:
            if element in ArrayT:
                outputArray.append(element)
        return outputArray

# Return the difference between two arrays, iff the arrays not contain duplicated elements
def Difference(ArrayS, ArrayT):
    if (check_duplicates(ArrayS) or check_duplicates(ArrayT)):
        print('ERROR: Alguno de los arrays ingresados posee elementos duplicados.')
    else:
        outputArray = []
        for element in ArrayS:
            if element not in ArrayT:
                outputArray.append(element)
        return outputArray

# Check if exist any duplicate element is the array, return a boolean value
def check_duplicates(Array):
    haveDuplicates = False
    tempArray = []
    for element in Array:
        if element not in tempArray:
            tempArray.append(element)
        else:
            haveDuplicates = True
            break
    return haveDuplicates
