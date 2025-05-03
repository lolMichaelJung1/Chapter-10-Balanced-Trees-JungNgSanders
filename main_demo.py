# Created by: Michael Jung (ID:10680322), Timothy Sanders (ID: 01002147), Megan Ng (ID: 00756276)

# Date: 5/1/25

# Course: Spr25_CS_034 CRN 39575

#--------------------------------------------------------------------------------------------
import random
from io import StringIO
import sys
from bst_node import BstNode
from avl_node import AvlNode
from red_black_node import RedBlackTreeNode
from AVLTree import AVLTree
from RedBlackTree import RedBlackTree
from avl_inventory_manager import InventoryManager
from rbt_flight_manager import FlightManager

# === Unified Demo with avl_inventory_manager & rbt_flight_manager ===
def demo_all():
    """
    Demonstrates AVL and Red-Black Trees, including:
    - AVL random insert
    - AVL-based InventoryManager
    - Red-Black random insert
    - Red-Black-based FlightManager
    """

    # === AVL Tree Demo ===
    print("\n--- AVL Tree Random Insert Test ---")
    random_avl_tree = AVLTree()
    random_values = random.sample(range(1, 100), 15)
    for v in random_values:
        random_avl_tree.insert(v)
    random_avl_tree.print_tree(random_avl_tree.root)
    random_avl_tree.print_log()

    # === AVL Inventory Manager ===
    print("\n>>> AVL Inventory Demo")
    inv = InventoryManager()
    for id in random.sample(range(1000, 1100), 10):
        inv.add_item(id)
    inv.show_inventory(random_avl_tree.root)
    inv.show_log()

    # === Red-Black Tree Demo ===
    print("\n--- Red-Black Tree Random Insert Test ---")
    random_rb_tree = RedBlackTree()
    for v in random_values:
        random_rb_tree.insert(v)
    random_rb_tree.print_tree(random_rb_tree.root)
    random_rb_tree.print_log()

    # === Red-Black Flight Manager ===
    print("\n>>> Red-Black Flight Demo")
    flights = FlightManager()
    for id in random.sample(range(2000, 2100), 10):
        flights.schedule_flight(id)
    flights.display_flight_schedule()
    flights.print_operations_log()

if __name__ == "__main__":
    demo_all()


'''
if __name__ == "__main__":
    random.seed(10)
    random_values = random.sample(range(1,101), 20)
    print('20 random integers from 1 to 100: ', random_values)
    values_to_insert = [10, 20, 30, 15, 25, 5, 1, 8, 18, 28]

    print("\n\n------- Demo of AVLTree ------")
    avl = AVLTree()
    for value in values_to_insert:
        print(f"\nInserting {value} in AVLTree...")
        avl.insert(value)
        avl.print_tree(avl.root)
        print()
    print("\nFinal AVLTree Root:", avl.root)
    print()

    print("\n\n------- Demo of Red-Black Tree ------")
    rbt = RedBlackTree()
    for value in values_to_insert:
        print(f"\nInserting {value} in Red-Black Tree...")
        rbt.insert(value)
        print("Inorder Traversal (key, color):", rbt.inorder_traversal())
        # You would typically add more checks here to verify RBT properties

    print("\nFinal Tree Root:", rbt.root)
    print("Final Red-Black Tree Height:", rbt.get_red_black_tree_height(rbt.root))
    print("Final Inorder Traversal (key, color):", rbt.inorder_traversal())
'''
