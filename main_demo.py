# Created by: Michael Jung (ID:10680322), Timothy Sanders (ID: 01002147), Megan Ng (ID: 00756276)

from io import StringIO
import sys
from bst_node import BstNode
from avl_node import AvlNode
from red_black_node import RedBlackTreeNode


if __name__ == "__main__":
    values_to_insert = [10, 20, 30, 15, 25, 5, 1, 8, 18, 28]

    print("\n\n------- Demo of AVLTree ------")
    avl = AVLTree()
    for value in values_to_insert:
        print(f"\nInserting {value} in AVLTree...")
        avl.insert(value)
        avl1.print_tree(avl1.root)
        print()
    print("\nFinal AVLTree Root:", avl.root)
    print()

    
    print("\n\n------- Demo of Red-Black Tree ------")  
    rbt = RedBlackTree()
    for value in values_to_insert:
        print(f"\nInserting {key} in Red-Black Tree...")
        rbt.insert(key)
        print("Inorder Traversal (key, color):", rbt.inorder_traversal())
        # You would typically add more checks here to verify RBT properties

    print("\nFinal Tree Root:", rbt.root)
    print("Final Inorder Traversal (key, color):", rbt.inorder_traversal())
