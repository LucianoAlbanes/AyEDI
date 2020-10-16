from algo1 import *

# Ask length and declare vector (numbers)
lenght = input_int('Ingrese la cantidad de elementos a analizar: ')
numbers = Array(lenght, 0)

# Ask element's values
for i in range(0, lenght):
    numbers[i] = input_int(f'Ingrese el valor ({i+1}/{lenght}) = ')
    
# Find biggest absolute number
biggestAbsNumPosition = int(0)
for i in range(0, lenght):
    actualAbsNum = abs(numbers[i])
    biggestAbsNum = abs(numbers[biggestAbsNumPosition])
    
    if actualAbsNum > biggestAbsNum:
        biggestAbsNumPosition = i
    
# Output phrase
print(f'El elemento con mayor valor absoluto ingresado previamente es: {numbers[biggestAbsNumPosition]}')

