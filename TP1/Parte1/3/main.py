from algo1 import *

# Ask length of inupt matrix and vector, and declare them
inputMatrix = Array(
    input_int('Ingrese la dimensión (n) de la matriz: '), Array(
        input_int('Ingrese la dimensión (m) de la matriz: '), 0.0))

inputVector = Array(
    input_int('Ingrese la dimensión (n) del vector: '), 0.0)

# Fill matrix
print('--LLENANDO MATRIZ--')
for i in range(0, len(inputMatrix)):
    for j in range(0, len(inputMatrix[i])):
        inputMatrix[i][j] = input_real(
            '(' + str(i+1) + ',' + str(j+1) + ') = '
        )

# Fill vector
print('--LLENANDO VECTOR--')
for i in range(0, len(inputVector)):
    inputVector[i] = input_real('(' + str(i+1) + ') = ')

# Check if can multiply (matrix's m should be equal to vector's n)
if len(inputMatrix[0]) != len(inputVector):
    print('ERROR: Dimensiones incorrectas.')
else:
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
    print(resultVector)
