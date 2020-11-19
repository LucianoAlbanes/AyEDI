# ~~ Test ~~

from linkedlist import add, access, LinkedList, length
from bubbleSort import bubbleSort
from selectionSort import selectionSort
'''from insertionSort import insertionSort'''
import random  # Only for testing

def printList(linkedList):
    print('[', end="")
    for i in range(0, length(linkedList)):
        if i != 0:
            print(', ', end="")
        print(str(access(linkedList, i)), end="")
    print(']')

def testSort(sorterFn):
    # Print current sort method
    print(f'\n~~~ {sorterFn.__name__} ~~~')
    
    # Create and fill the list
    print('Generando una lista con 10 valores aleatorios...')

    listOfNumbers = LinkedList()
    for _ in range(0, 10):
        add(listOfNumbers, random.randint(0, 10))

    # Print unsorted list
    printList(listOfNumbers)

    # Sort
    print('\nOrdenando la lista...')
    sorterFn(listOfNumbers)

    # Print sorted list
    printList(listOfNumbers)

## TESTS
testSort(selectionSort)
testSort(bubbleSort)