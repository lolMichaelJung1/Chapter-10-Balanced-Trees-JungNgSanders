# Created by: Michael Jung (ID:10680322), Timothy Sanders (ID: 01002147), Megan Ng (ID: 00756276)

# Date: 5/1/25

# Course: Spr25_CS_034 CRN 39575

#--------------------------------------------------------------------------------------------
import random
from AVLTree import AVLTree


class InventoryManager:
    """
    Manages an inventory of items using an AVL tree for efficient storage and retrieval.
    """
    def __init__(self):
        """
        Initializes an empty inventory by creating an AVL tree to store items.
        """
        self.avl_tree = AVLTree()  # Create an instance of the AVLTree class to store inventory items

    def add_item(self, item_id):
        """
        Adds an item to the inventory.

        Args:
            item_id: The ID of the item to add.
        """
        print(f"Adding item ID: {item_id}")  # Print a message indicating the item being added
        self.avl_tree.insert(item_id)  # Insert the item ID into the AVL tree

    def remove_item(self, item_id):
        """
        Removes an item from the inventory.

        Args:
            item_id: The ID of the item to remove.
        """
        pass
        #print(f"Removing item ID: {item_id}")  # Print a message indicating the item being removed
        #self.avl_tree.delete(item_id)  # Delete the item ID from the AVL tree

    def show_inventory(self, node=None, level=0, prefix='Root:', visited=None):
        """
        Displays the current inventory by printing the AVL tree structure.

        Args:
            node: The starting node for printing. Defaults to the root of the tree.
            level: The current level of the tree. Defaults to 0 (used for indentation).
            prefix: The prefix for indicating the position of the node (e.g. "Root:", "L----", "R----").
            visited: Used to avoid reprinting nodes
        """
        print("\n--- Inventory AVL Tree ---")  # Print a header for the inventory display
        self.avl_tree.print_tree(node or self.avl_tree.root, level, prefix, visited)  # Print the AVL tree structure

    def show_log(self):
        """
        Displays the log of rotations performed during insertions and deletions.
        """
        self.avl_tree.print_log()  # Print the rotation log


# === Inventory Manager Demo ===
manager = InventoryManager()  # Create an instance of the InventoryManager
for item in random.sample(range(1, 50), 10):  # Generate 10 random, unique item IDs
    manager.add_item(item)  # Add each item to the inventory

manager.show_inventory()  # Display the final inventory tree
