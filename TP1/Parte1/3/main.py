from algo1 import *

# Ask length of inupt matrix and vector, and declare them
n = int(0)
m = int(0)
while (n < 1):
    n = input_int('Ingrese la dimensión (n) de la matriz: ')
while (m < 1):
    m = input_int('Ingrese la dimensión (m) de la matriz: ')
inputMatrix = Array(n, Array(m, 0.0))

n = int(0)
while (n < 1):
    n = input_int('Ingrese la dimensión (n) del vector: ')
inputVector = Array(n, 0.0)

# Check if can multiply (matrix's m should be equal to vector's n)
if len(inputMatrix[0]) != len(inputVector):
    print('ERROR: Dimensiones incorrectas.')
else:
    # Fill matrix
    print('--LLENANDO MATRIZ--')
    for i in range(0, len(inputMatrix)):
        for j in range(0, len(inputMatrix[i])):
            inputMatrix[i][j] = input_real(f'({i+1}/{j+1}) = ')

    # Fill vector
    print('--LLENANDO VECTOR--')
    for i in range(0, len(inputVector)):
        inputVector[i] = input_real(f'({i+1}) = ')
        
    # Create a new resultVector and initialize it
    resultVector = Array(len(inputMatrix), 0.0)  # (n = matrix's n)
    for i in range(0, len(resultVector)):
        resultVector[i] = 0.0

    # Multiply
    for i in range(0, len(resultVector)):
        for j in range(0, len(inputMatrix[i])):
            resultVector[i] += inputMatrix[i][j] * inputVector[j]

    # Print the multiplication results
    print('El producto de la matriz anterior por el vector es el siguiente:')
    for i in range(0, len(resultVector)): # vector is nx1 (column vector)
        print(f'[{resultVector[i]}]')
