# ~~ I miss you, membership operators :c ~~

# Return a ADT set and remove duplicates
def Create_Set(Array):
    outputArray = []
    for i in range(0, len(Array)):
        areInside = False
        for j in range(0, len(outputArray)):
            if Array[i] == outputArray[j]:
                areInside = True
                break
        if not areInside:
            outputArray.append(Array[i])
    return outputArray

# Return the union between two arrays, iff the arrays not contain duplicated elements
def Union(ArrayS, ArrayT):
    # Overwrite the input array without duplicates
    if not check_duplicates(ArrayS):
        check_duplicates(ArrayT)
    ArrayS = Create_Set(ArrayS)
    ArrayT = Create_Set(ArrayT)

    return Create_Set(ArrayS + ArrayT)  # Remove duplicates

# Return the intersection between two arrays, iff the arrays not contain duplicated elements
def Intersection(ArrayS, ArrayT):
    # Overwrite the input array without duplicates
    if not check_duplicates(ArrayS):
        check_duplicates(ArrayT)
    ArrayS = Create_Set(ArrayS)
    ArrayT = Create_Set(ArrayT)

    # Create an outputArray and store the elements if match
    outputArray = []
    for i in range(0, len(ArrayS)):
        areInside = False
        for j in range(0, len(ArrayT)):
            if ArrayS[i] == ArrayT[j]:
                areInside = True
                break
        if areInside:
            outputArray.append(ArrayS[i])
    return outputArray

# Return the difference between two arrays, iff the arrays not contain duplicated elements
def Difference(ArrayS, ArrayT):
    # Overwrite the input array without duplicates
    if not check_duplicates(ArrayS):
        check_duplicates(ArrayT)
    ArrayS = Create_Set(ArrayS)
    ArrayT = Create_Set(ArrayT)

    # Create an outputArray and store the elements if match
    outputArray = []
    for i in range(0, len(ArrayS)):
        areInside = False
        for j in range(0, len(ArrayT)):
            if ArrayS[i] == ArrayT[j]:
                areInside = True
                break
        if not areInside:
            outputArray.append(ArrayS[i])
    return outputArray

# Check if exist any duplicate element is the array, return a boolean value
def check_duplicates(Array):
    tempArray = []
    haveDuplicates = False
    for i in range(0, len(Array)):
        for j in range(0, len(tempArray)):
            if Array[i] == tempArray[j]:
                haveDuplicates = True
                break
        if not haveDuplicates:
            tempArray.append(Array[i])
        else:
            print('INFO: Alguno de los arrays ingresados posee elementos duplicados. Fueron eliminados.')
            break
    return haveDuplicates
