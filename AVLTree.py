# Created by: Michael Jung (ID:10680322), Timothy Sanders (ID: 01002147), Megan Ng (ID: 00756276)

# Date: 5/1/25

# Course: Spr25_CS_034 CRN 39575

#--------------------------------------------------------------------------------------------

from typing import Any

from avl_node import AvlNode

class AVLTree:
    """Represents an AVL tree.

    Args:
        root (AvlNode): A reference to the optional root node of the AVL tree

    Attributes:
        root (AvlNode): A reference to the optional root node of the AVL tree
        rotation_count (int): Counter for rotations performed
        log (list): log of operations performed
    """
    def __init__(self, root: AvlNode=None):
        """Initializes an AVL Tree with an optional root node.

        Args:
            root: The root node of the AVL tree. Defaults to `None`
        """
        self.root = root
        self.rotation_count = 0
        self.log = []

    @staticmethod
    def get_height(node: AvlNode) -> int:
        """Gets the height of a node in the AVL tree.

        Args:
            node (AvlNode): The node to get the height of.

        Returns:
            int: The height of the node.
        """
        if not node:          # If the node is None
            return -1         # Conventionally -1 for a null node, 0 for a leaf
        return node.height    # Otherwise, return the node's height

    def update_height(self, node: AvlNode) -> None:
        """Update the height of a node and its ancestors.

        Args:
            node (AvlNode): The node to update the height of.

        Returns:
            None
        """
        while node: # Iterate until reaching the root (which has no parent)
            # Update height based on children's heights
            node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
            node = node.parent  # Move up to the parent node

    def get_balance(self, node: AvlNode) -> int:
        """Get the balance factor of a node in the AVL tree.

        Args:
            node (AvlNode): The node to get the balance factor of.

        Returns:
            int: The balance factor of the node.
        """
        if not node:          # If the node is None
            return 0          # Balance factor is 0 for a null node (leaf node)
        return self.get_height(node.left) - self.get_height(node.right) # Calculate balance factor

    def left_rotate(self, node: AvlNode) -> AvlNode:
        """Perform a left rotation on a node in the AVL tree.

        Args:
            node (AvlNode): The node to rotate.

        Returns:
            AvlNode: The new root of the rotated subtree.
        """
        self.rotation_count += 1
        self.log.append(f"Left rotation on node {node.value}")
        pivot = node.right  # Set the right child of node as new root (pivot)
        node.right = pivot.left  # Set the left child of pivot as node's right child
        if pivot.left:  # If pivot has left child
            pivot.left.parent = node  # Update its parent to be the node being rotated
        pivot.parent = node.parent  # Set pivot's parent as node's parent
        if not node.parent:  # If node was the root
            self.root = pivot  # Set pivot as new root
        elif node == node.parent.left:  # If node was a left child
            node.parent.left = pivot  # pivot replaces node as left child
        else:  # If node was a right child
            node.parent.right = pivot  # pivot replaces node as right child
        pivot.left = node  # Set node as pivot's left child
        node.parent = pivot  # Set node's parent as pivot
        self.update_height(node)  # Update heights after rotation
        self.update_height(pivot)
        return pivot

    def right_rotate(self, node: AvlNode) -> AvlNode:
        """Performs a right rotation on a node in the AVL tree.

        Args:
            node: The node to rotate.

        Returns:
            AvlNode: The new root of the rotated subtree.
        """
        self.rotation_count += 1  # Increment rotation counter
        self.log.append(f"Right rotation on node {node.value}")  # Log the rotation
        pivot = node.left  # Set the left child of node as new root (pivot)
        node.left = pivot.right  # Set the right child of pivot as node's left child
        if pivot.right:  # If pivot has right child
            pivot.right.parent = node  # Update its parent to be the node being rotated
        pivot.parent = node.parent  # Set pivot's parent as node's parent
        if not node.parent:  # If node was the root
            self.root = pivot  # Set pivot as new root
        elif node == node.parent.right:  # If node was a right child
            node.parent.right = pivot  # pivot replaces node as right child
        else:  # If node was a left child
            node.parent.left = pivot  # pivot replaces node as left child
        pivot.right = node  # Set node as pivot's right child
        node.parent = pivot  # Set node's parent as pivot
        self.update_height(node)  # Update heights after rotation
        self.update_height(pivot)
        return pivot  # Return the new subtree root (pivot)

    def update_balance(self, node):
        """Update balance factors and perform rotations if needed."""
        while node:  # Iterate until reaching the root
            balance = self.get_balance(node)  # Get the balance factor
            if balance > 1:  # Left heavy
                if self.get_balance(node.left) < 0:  # Left-Right case
                    node.left = self.left_rotate(node.left)  # Perform left rotation on the left child
                node = self.right_rotate(node)  # Perform right rotation on node
            elif balance < -1:  # Right heavy
                if self.get_balance(node.right) > 0:  # Right-Left case
                    node.right = self.right_rotate(node.right)  # Perform right rotation on right child
                node = self.left_rotate(node)  # Perform left rotation on node
            else:
                node = node.parent  # Move up to the parent node

    def insert(self, value: Any):
        """Inserts a value into the AVL Tree, maintaining the AVL property.

        Args:
            value: The value to insert.
        """
        new_node = AvlNode(value)  # Create a new node
        if not self.root:  # If the tree is empty
            self.root = new_node  # The new node becomes the root
            self.log.append(f"Inserted {value}, tree height: {self.get_height(self.root)}")  # Log the insertion
            return
        parent, current = None, self.root  # Start at the root
        while current:  # Traverse the tree
            parent = current  # keep track of the parent
            if value < current.value:  # Go left
                current = current.left
            elif value > current.value:  # Go right
                current = current.right
            else:
                self.log.append(f"Duplicated key {value} ignored.")
                return  # Duplicate, do nothing
        new_node.parent = parent  # Set parent of the new node
        if value < parent.value:  # Insert as left child
            parent.left = new_node
        else:  # Insert as right child
            parent.right = new_node
        self.update_height(new_node)  # Update heights after insertion
        self.update_balance(new_node)  # Update balance factors and rotate if needed
        self.log.append(f"Inserted {value}, tree height: {self.get_height(self.root)}")  # Log the insertion

    def print_tree(self, node: AvlNode=None, level: int=0, prefix: str='Root:', visited=None) -> None:
        """Prints the AVL tree in a visually appealing format.

        Args:
            node: The starting node for printing. Defaults to the root of the tree.
            level: The current level of the tree. Defaults to 0 (used for indentation).
            prefix: The prefix for indicating the position of the node (e.g. "Root:", "L----", "R----").
            visited
        """
        # Ensure get_balance is called on the correct object (self)
        if node:    # If the current node is not None
            balance = self.get_balance(node)  # Get the balance factor of the node
            print(' ' * (5 * level) + prefix + f"{node.value} (BF={balance})") # Print node value and balance factor
            # Recursively call print_tree on left and right, passing self
            self.print_tree(node.left, level + 1, 'L----', visited) # Print left subtree
            self.print_tree(node.right, level + 1, 'R----', visited) # Print right subtree

    def print_log(self):
        print("\n--- AVL Tree Log ---")
        for entry in self.log:  # Print each entry in the log
            print(entry)
        print(f"Total Rotations: {self.rotation_count}")  # Print total rotations performed
        print(f"Final Tree Height: {self.get_height(self.root)}")  # Print final height of the tree


# --- Command Line Interface ---
# Demonstrate the structure of a sample Binary Tree
# Demonstrate the structure of a sample BST
# Demonstrate the structure of a sample AVL Tree with balance factor (BF)

if __name__ == "__main__":
    print("--- Running Example Usage ---")


    # Demo of AVL (insert() without rotation)
    #--------------------------------------------
    #      50
    #    /   \
    #   30    70
    #  /  \   /  \
    # 20  40 60  80
    print("\n\n------- Demo of AVLTree: insert() with balancing (show balance factors) ------")
    avl1 = AVLTree()
    print("\n\n------Balanced AVL Tree without Rotation------")
    for value in [50, 30, 70, 20, 40, 60, 80]:
        print(f"\nInserting {value} into AVL Tree:")
        avl1.insert(value)
        avl1.print_tree(avl1.root)
        print()

    # Demo of AVL (insert() with rotation)
    #--------------------------------------------
    #      40
    #    /   \
    #   20    60
    #  /  \   /  \
    # 10  30 50  70

    print("\n\n------- Demo of AVLTree: insert() with balancing (show balance factors) ------")
    avl2 = AVLTree()
    for value in [10, 20, 30, 40, 50, 60, 70]:
        print(f"\nInserting {value} into AVL Tree:")
        avl2.insert(value)
        avl2.print_tree(avl2.root)
        print()
    print("\n\n------ End of AVLTree Demo ------")
    print("---------------------------------------------------")
