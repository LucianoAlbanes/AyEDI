## The purpose of the following code is to have certain functions
## that python provides, but they are restricted in the course.
from algo1 import *

# Absolute Value (Aka 'abs()')
def abs(number):
    if number < 0: return number*-1
    else: return number

# Add a element to an array (Aka append()) [type sensitive]
def append(inputArray, elementToAdd):
    length = len(inputArray)
    outputArray = Array(length+1, )
    
    for i in range(0, (length)):
        outputArray[i] = inputArray[i]
    outputArray[length] = elementToAdd
    return outputArray