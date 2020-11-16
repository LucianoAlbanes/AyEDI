# Calc the summation from 2 to n, in even steps

def summationEven(n):
    '''
    Explanation:
        This function calcs the summation from 2 to a given number, in even steps.
    Params:
        n: The last number of the summation.
    Return:
        The summation.
        Returns 'None' if the given number is negative or non even.
    '''
    # Base cases
    if n == 2:
        return n

    # Case if negative or non a even number
    if (n < 0) or (n % 2):
        return None

    # General case
    return n + summationEven(n-2)


# Basic interface
from algo1 import input_real

result = None
while result == None:
    result = summationEven(input_real(
        'Ingrese el numero N del que desea obtener la suma de los enteros positivos pares desde N hasta 2: '))
    if result == None:
        print('El número ingresado no es válido. (Debe ser un número par positivo).')

print(
    f'La sumatoria de los pares desde el número ingresado hasta 2 es : {int(result)}')
