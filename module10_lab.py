# Created by: Michael Jung (ID:10680322), Timothy Sanders (ID: 01002147), Megan Ng (ID: 00756276)

# Date: 4/21/25

# Course: Spr25_CS_034 CRN 39575

#--------------------------------------------------------------------------------------------
import random

from avl_inventory_manager import InventoryManager
from AVLTree import AVLTree
from rbt_flight_manager import FlightManager
from RedBlackTree import RedBlackTree


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
    random_values = random.sample(range(1, 100), 20)
    for v in random_values:
        random_avl_tree.insert(v)
    random_avl_tree.print_tree(random_avl_tree.root)
    random_avl_tree.print_log()

    # === AVL Inventory Manager ===
    print("\n>>> AVL Inventory Demo")
    inv = InventoryManager()
    for id in random.sample(range(1000, 1100), 10):
        inv.add_item(id)
    inv.show_inventory()
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
