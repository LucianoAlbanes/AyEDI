from algo1 import *

# Ask lenght of matrix and vector, and declare them
inputMatrix = Array(
    input_int('Ingrese la dimensión (n) de la matriz: '), Array(
        input_int('Ingrese la dimensión (m) de la matriz: '), 0.0)
)

inputVector = Array(
    input_int('Ingrese la dimensión (n) del vector: '), 0.0)

# Fill matrix
print('--LLENANDO MATRIZ--')
for i in range(0, len(inputMatrix)):
    for j in range(0, len(inputMatrix[i])):
        inputMatrix[i][j] = input_real('(' + str(i+1) + ',' + str(j+1) + ') = ')
        

# Fill vector
print('--LLENANDO VECTOR--')
for i in range(0, len(inputVector)):
    inputVector[i] = input_real('(' + str(i+1) + ') = ')
