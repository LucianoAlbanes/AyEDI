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
            break
    return haveDuplicates

# Check if two arrays have a duplicate elements, print an info message and overwrite as a set
def preConditions(ArrayS, ArrayT):
    # Check if haveDuplicates; if true, remove them
    haveDuplicates = False
    if check_duplicates(ArrayS):
        ArrayS = Create_Set(ArrayS)
        haveDuplicates = True
    if check_duplicates(ArrayT):
        ArrayT = Create_Set(ArrayT)
        haveDuplicates = True

    # Print the info message
    if haveDuplicates:
        print('INFO: Alguno de los arrays ingresados posee elementos duplicados. Estos fueron eliminados.')

# Return the union between two arrays
def Union(ArrayS, ArrayT):
    # Verify Conditions
    preConditions(ArrayS, ArrayT)

    # Do the union, if the result array have duplicates, remove them
    outputArray = ArrayS + ArrayT
    if check_duplicates(outputArray):
        outputArray = Create_Set(outputArray)
    return outputArray

# Return the intersection between two arrays
def Intersection(ArrayS, ArrayT):
    # Verify Conditions
    preConditions(ArrayS, ArrayT)

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

# Return the difference between two arrays
def Difference(ArrayS, ArrayT):
    # Verify Conditions
    preConditions(ArrayS, ArrayT)

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
