from algo1 import *

# Declare function for filling vector
def askForValues(vector):
    for i in range(0, len(vector)):
        vector[i] = input_real(f'({i+1}/{len(vector)}) = ')

# Ask length of each inputVector and declare them
length1 = int(0)
length2 = int(0)

while (length1 < 1):
    length1 = input_int('Ingrese la dimensión del primer vector: ')
while (length2 < 1):
    length2 = input_int('Ingrese la dimensión del segundo vector: ')

inputVector1 = Array(length1, 0.0)
inputVector2 = Array(length2, 0.0)


# Check if dimensions are the same
if len(inputVector1) != len(inputVector2):
    print('ERROR: Las dimensiones no son iguales, por lo que no se podrá continuar.')
else:    
    # Ask for the element´s values of each vector
    print('INGRESANDO LOS VALORES DEL PRIMER VECTOR')
    askForValues(inputVector1)
    print('INGRESANDO LOS VALORES DEL SEGUNDO VECTOR')
    askForValues(inputVector2)

    # Declare sumVector and calc the sum
    sumVector = Array(len(inputVector1), 0.0)
    for i in range(0, len(sumVector)):
        sumVector[i] = inputVector1[i] + inputVector2[i]

    # Declare and calc the norm
    summatory = float(0)
    for i in range(0, len(sumVector)):
        summatory += sumVector[i]**2
    norm = summatory**0.5  # sqrt equivalent

    # Show results
    print(f'Vector suma: {sumVector}')
    print(f'Norma: {norm}')
