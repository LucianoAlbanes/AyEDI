from algo1 import *
import restrictions

# Ask length and declare vector (numbers)
length = int(0)
while (length < 1):
    length = input_int('Ingrese la cantidad de elementos a analizar: ')
numbers = Array(length, 0)

# Ask element's values
for i in range(0, length):
    numbers[i] = input_int(f'Ingrese el valor ({i+1}/{length}) = ')
    
# Find biggest absolute number
biggestAbsNum = int(0)
for i in range(0, length):
    actualAbsNum = restrictions.abs(numbers[i])
    biggestAbsNum = restrictions.abs(biggestAbsNum)  
    if actualAbsNum > biggestAbsNum:
        biggestAbsNum = numbers[i]
    
# Output phrase
print(f'El elemento con mayor valor absoluto ingresado previamente es: {biggestAbsNum}')
