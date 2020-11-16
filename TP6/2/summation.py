# Calc the summation from 0 to n

def summation(n):
    '''
    Explanation:
        This function calcs the summation from 0 to a given number.
    Params:
        n: The last number of the summation.
    Return:
        The summation.
        Returns 'None' if the given number is negative or non a integer.
    '''
    # Base cases
    if (n == 0) or (n == 1):
        return n
    
    # Case if negative or non integer
    if (n < 0) or (n % 1):
        return None

    # General case
    return n + summation(n-1)


# Basic interface
from algo1 import input_real

result = None
while result == None:
    result = summation(input_real(
        'Ingrese el numero N del cual quiera obtener la suma de los primeros N enteros: '))
    if result == None:
        print('El número ingresado no es válido. (Debe ser un número entero positivo).')

print(
    f'La sumatoria desde 0 hasta el número dado es : {int(result)}')