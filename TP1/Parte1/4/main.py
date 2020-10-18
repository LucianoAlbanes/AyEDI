from algo1 import *

# Ask length of the matrices and declare them
minuendMatrix = Array(
    input_int('Ingrese la dimensión (n) de las matrices: '), Array(
        input_int('Ingrese la dimensión (m) de las matrices: '), 0.0))

subtrahendMatrix = copy.deepcopy(minuendMatrix) # Copy is part of algo1 ¯\_(ツ)_/¯

# Define a function to fill matrices
def fillMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = input_real(f'({i+1}/{j+1}) = ')


# Fill matrices
print('--LLENANDO MATRIZ MINUENDO--')
fillMatrix(minuendMatrix)
print('--LLENANDO MATRIZ SUSTRAENDO--')
fillMatrix(subtrahendMatrix)

# Define differenceMatrix and calc the subtraction
differenceMatrix = Array(len(minuendMatrix), Array(len(minuendMatrix[0]), 0.0))

for i in range(len(differenceMatrix)):
    for j in range(len(differenceMatrix[i])):
        differenceMatrix[i][j] = minuendMatrix[i][j] - subtrahendMatrix[i][j]

# Show the difference
print("La diferencia entre las matrices introducidas es la siguiente:")
for i in range(len(differenceMatrix)):  # Print each row of the differenceMatrix
    print(differenceMatrix[i])
