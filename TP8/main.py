# Some testing for binary tree adt implementation
from mybinarytree import *

# function to print a tree
COUNT = [10]
def printTree(actualNode, space):
    # Base case.
    if not actualNode:
        return None

    # Increase distance between levels.
    space += COUNT[0]

    # Process right child first.
    printTree(actualNode.rightnode, space)

    # Print current node after space.
    print()
    for i in range(COUNT[0], space):
        print(end=" ")
    print(actualNode.key)

    # Process left child.
    printTree(actualNode.leftnode, space)

# TEST CODE

tree = BinaryTree()

insert(tree, 'Integral', 100)
insert(tree, 'Guille', 60)
insert(tree, 'Humber', 21)
insert(tree, 'Ale', 19)
insert(tree, 'Cristian', 22)
insert(tree, 'Ecogas', 110)
insert(tree, 'Enargas', 111)

printTree(tree.root, 0)
