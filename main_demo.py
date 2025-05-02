# Created by: Michael Jung (ID:10680322), Timothy Sanders (ID: 01002147), Megan Ng (ID: 00756276)


from bst_node import BstNode
from avl_node import AvlNode
from red_black_node import RedBlackTreeNode


if __name__ == "__main__":
    avl = AvlTree()
  
    rbt = RedBlackTree()
    keys_to_insert = [10, 20, 30, 15, 25, 5, 1, 8, 18, 28]

    print("Inserting keys:", keys_to_insert)
    for key in keys_to_insert:
        print(f"\nInserting {key}...")
        rbt.insert(key)
        print("Inorder Traversal (key, color):", rbt.inorder_traversal())
        # You would typically add more checks here to verify RBT properties

    print("\nFinal Tree Root:", rbt.root)
    print("Final Inorder Traversal (key, color):", rbt.inorder_traversal())
