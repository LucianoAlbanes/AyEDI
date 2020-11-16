# Calc the n-th number of the Fibonacci sequence

from linkedlist import LinkedList
from mystack import push, pop


def fibonacci(n):
    '''
    Explanation:
        This function calcs and return the number at a given position of the fibonacci sequence.
    Params:
        n: The position of the number on the fibonacci sequence.
    Return:
        The number at the given position of the fibonacci sequence.
        Returns 'None' if the given position is negative or non a integer.
    '''
    # Base cases
    if (n == 0) or (n == 1):
        return n

    # Case if negative or non integer
    if (n < 0) or (n % 1):
        return None

    # Calc using a stack
    stack = LinkedList()
    push(stack, 1)
    push(stack, 1)

    for _ in range(2, int(n)):
        a = pop(stack)
        b = pop(stack)
        summation = a + b
        push(stack, a)
        push(stack, summation)

    return pop(stack)


# Basic interface
from algo1 import input_real

result = None
while result == None:
    result = fibonacci(input_real(
        'Ingrese la posición del número a obtener en la secuencia de fibonacci: '))
    if result == None:
        print('El número ingresado no es válido. (Debe ser un número entero positivo).')

print(
    f'El número de fibonacci que corresponde a la posición dada es: {int(result)}')
