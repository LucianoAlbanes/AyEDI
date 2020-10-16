from algo1 import *

# Ask length of inupt matrix and vector, and declare them
inputMatrix = Array(
    input_int('Ingrese la dimensión (n) de la matriz: '), Array(
        input_int('Ingrese la dimensión (m) de la matriz: '), 0.0))

# Fill matrix
print('--LLENANDO MATRIZ--')
for i in range(0, len(inputMatrix)):
    for j in range(0, len(inputMatrix[i])):
        inputMatrix[i][j] = input_real(f'({i+1}/{j+1}) = ')

# Check if the input matrix is valid
isValid = True
if len(inputMatrix) != len(inputMatrix[0]):
    isValid = False
    print('No es posible comprobar si la matriz ingresada es traingular superior ya que no es una matriz cuadrada (nxn).')
elif len(inputMatrix) == 1:
    isValid = False
    print('No es posible comprobar si la matriz ingresada es traingular superior ya que es una matriz de 1x1.')

# Continue if is valid
if isValid:
    # Check if the matrix are a upper triangular matrix (UTM)
    isUTM = True
    
    for i in range(1, len(inputMatrix)): # Start with 1 because the first row dont need to start with a 0
        for j in range(i):
            if (inputMatrix[i][j] != 0):
                isUTM = False
                break
        if not isUTM:
            break

    if isUTM:
        # Calc the determinant
        # Info: The determinant of a triangular matrix is the product of the elements of the diagonal.
        determinant = float(1)
        for i in range(len(inputMatrix)):
            determinant *= inputMatrix[i][i]

        # Output text
        print('La matriz ingresada es traingular superior!')
        print(f'El determinante es = {determinant}')
    else:
        print('La matriz ingresada no es traingular superior.')
