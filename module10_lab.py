# Created by: Michael Jung (ID:10680322), Timothy Sanders (ID: 01002147), Megan Ng (ID: 00756276)

# Date: 4/21/25

# Course: Spr25_CS_034 CRN 39575

#--------------------------------------------------------------------------------------------
import random
from typing import Any

# === Shared Base Node ===
class BstNode:
    """
    Base node for Binary Search Tree.
    """
    # Constructor for the Node class
    def __init__(self, value, parent=None, debug=False):
        """
        Initializes a new node with a given value.

        Args:
            value: The data to be stored in the node. Defaults to None.
        """
        self.debug = debug
        if self.debug:
            print(f"DEBUG: BstNode.__init__({value}) called") # Added for demo
        self.value = value  # Store data in the node
        self.left = None    # Pointer to the left child node
        self.right = None   # Pointer to the right child node
        self.parent = parent # Assign parent to the current node (default value: None)

    # String representation of the Node
    def __str__(self):
        """
        Returns the string representation of the node's value.
        """
        return str(self.value)

# === AVL Tree Node ===
class AvlNode(BstNode): # Inherit from BstNode class
    """
    Node for AVL tree, inheriting from BstNode.
    Adds a 'height' attribute for balancing.
    """
    def __init__(self, value, debug=False):
        super().__init__(value)  # Call BstNode constructor to initialize basic node properties
        self.debug = debug
        if self.debug:
            print(f"DEBUG: AvlNode.__init__({value}) calling super()") # Added for demo
        self.height = 1        # Initialize the height of the AVL node to 1

    def __str__(self):
        """
        Returns a string representation of the AVL node in the format "value (height: height)".
        """
        return f"{str(self.value)} (height: {self.height})"


# === AVL Tree ===
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

# === Inventory Manager ===
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


# === Red-Black Tree ===
class RedBlackTreeNode(BstNode):  # This class inherits from BstNode (a basic Binary Search Tree node class)
    def __init__(self, value, parent=None, is_red=True, debug=False):
        """
        Initializes a new Red-Black Tree Node.

        Args:
            value: The value to be stored in the node.
            parent: The parent node of this node (default: None).
            is_red: True if the node should be colored red initially, otherwise black (default: True).
            debug: Whether to print debugging messages for the node.
        """
        super().__init__(value)  # Call the parent class's __init__ to initialize common attributes like value, left, right, parent
        # Set the color of the node based on the 'is_red' parameter:
        # 'R' for red if is_red is True, 'B' for black otherwise
        self.color = 'R' if is_red else 'B'
        self.debug = debug
        if self.debug:
            print(f"DEBUG: RedBlackTreeNode.__init__({value}) calling super()")  # Added for demo

    def __str__(self) -> str:
        """
        Returns a string representation of the node's value and color.
        """
        return f"{self.value}({self.color})"

    def is_red(self) -> bool:
        """
        Checks if the node is red.

        Returns:
            True if the node is red, False otherwise.
        """
        return self.color == 'R'

    def is_black(self) -> bool:
        """
        Checks if the node is black.

        Returns:
            True if the node is black, False otherwise.
        """
        return self.color == 'B'

    def get_grandparent(self):
        """
        Gets the grandparent of the current node.

        Returns:
            The grandparent node, or None if the current node has no grandparent.
        """
        return self.parent.parent if self.parent and self.parent.parent else None

    def get_uncle(self):
        """
        Gets the uncle of the current node.
        The uncle is the sibling of the current node's parent.

        Returns:
            The uncle node, or None if the current node has no uncle.
        """
        grandparent = self.get_grandparent() # Get the grandparent of the current node
        if not grandparent:                  # If there is no grandparent, there's no uncle
            return None                      # So return None
        # If there is a grandparent, check if the current node's parent is the left child
        # If so, the uncle is the right child of the grandparent, otherwise it's the left child
        return grandparent.right if self.parent == grandparent.left else grandparent.left

    def get_sibling(self):
        """
        Gets the sibling of the current node.
        The sibling is the node on the opposite side of the current node's parent.

        Returns:
            The sibling node, or None if the current node has no sibling.
        """
        if not self.parent:  # If there is no parent, there's no sibling
            return None      # So return None
        # If there is a parent, check if the current node is the left child
        # If so, the sibling is the right child of the parent, otherwise it's the left child
        return self.parent.right if self == self.parent.left else self.parent.left

    def get_height(self):
        """Get the height of the node."""
        l = self.left.get_height() if self.left else -1
        r = self.right.get_height() if self.right else -1
        return 1 + max(l, r)


class RedBlackTree:
    """Represents a Red-Black Tree structure.

    Attributes:
        root (RedBlackTreeNode): A reference to the optional root node of the Red-Black tree
        rotation_count
        log
    """

    def __init__(self):
        """
        Initializes an empty Red-Black Tree.
        """
        # The root node of the tree, initially None (empty tree)
        self.root = None
        self.rotation_count = 0
        self.log = []

    def insert(self, value: Any) -> None:
        """Inserts a new node with the given key into the Red-Black Tree.

        Args:
            value (Any): The value to be inserted into the tree.
        """
        # Step 1: Perform standard BST insertion and color the new node red.
        new_node = RedBlackTreeNode(value)  # New nodes are always initially red

        # Handle the case of an empty tree
        if not self.root:
            # If the tree is empty, the new node becomes the root
            self.root = new_node
            new_node.color = "B"  # Root node is always black
            return
        # Find the correct position for the new node using BST logic
        current = self.root
        parent = None
        while current:
            parent = current  # Keep track of the parent
            if value < current.value:
                current = current.left  # Go left
            elif value > current.value:
                current = current.right  # Go right
            else:
                # Optional: Handle duplicate keys (e.g., ignore, update, raise error)
                # In this version, we simply don't insert duplicates.
                print(f"value {value} already exists. Insertion skipped.")
                return

        # Link the new node to its parent
        new_node.parent = parent
        if value < parent.value:
            parent.left = new_node  # Insert as left child
        else:
            parent.right = new_node  # Insert as right child

        # Step 2: Fix any Red-Black Tree violations caused by the insertion.
        self._fix_insert(new_node)

        # Step 3: Ensure the root is always black (final enforcement).
        # This handles the case where the root was initially inserted or
        # became red during balancing.
        if self.root.is_red():
            self.root.color = "B"

    def _fix_insert(self, node: RedBlackTreeNode) -> None:
        """Fixes the Red-Black Tree properties (violations) after insertion.

        This method handles the balancing operations (recoloring and rotations)
        required to maintain the Red-Black Tree invariants.

        Args:
            node (RedBlackTreeNode): The newly inserted node (which is initially red).
        """
        # Continue fixing as long as the current node is red and has a red parent
        # (violating the "no consecutive red nodes" property).
        # We stop if the node becomes the root (node.parent is None) or its parent is black.
        while node != self.root and node.parent.is_red():
            parent = node.parent
            grandparent = node.get_grandparent()
            uncle = node.get_uncle()

            # If grandparent is None, it means parent is the root.
            # Since the loop condition requires parent to be red, and we ensure
            # the root is black *after* _fix_insert, this case shouldn't
            # strictly happen within the loop if called correctly from insert().
            # However, having the check prevents potential errors.
            if grandparent is None:
                break  # Should not happen if parent is red

            # Determine the cases based on the parent's position relative to the grandparent
            if parent == grandparent.left:
                # --- Parent is the LEFT child ---

                # Case 1: Uncle is RED
                if uncle and uncle.is_red():
                    # Recolor parent, uncle, and grandparent
                    self.log.append(f"Recoloring: {parent.value}, {uncle.value}, {grandparent.value}")
                    parent.color = "B"
                    uncle.color = "B"
                    grandparent.color = "R"
                    # Move up the tree: continue checking from the grandparent
                    node = grandparent
                else:
                    # Case 2: Uncle is BLACK or None - Node is RIGHT child (LR triangle)
                    if node == parent.right:
                        # Perform a left rotation at the parent
                        self._rotate_left(parent)
                        self.rotation_count += 1
                        # After rotation, the original parent becomes the node
                        # for the next step (which is now an LL case)
                        node = parent  # node now points to the original parent
                        parent = node.parent  # update parent reference (original grandparent)
                        # Grandparent remains the same for the next step

                    # Case 3: Uncle is BLACK or None - Node is LEFT child (LL line)
                    # This case also handles the situation after Case 2's rotation
                    # Recolor parent and grandparent
                    parent.color = "B"
                    grandparent.color = "R"
                    # Perform a right rotation at the grandparent
                    self._rotate_right(grandparent)
                    self.rotation_count += 1
                    # After rotation and recoloring, the subtree is balanced locally.
                    # The loop condition will re-evaluate.

            else:  # parent == grandparent.right
                # --- Parent is the RIGHT child (Mirror cases) ---

                # Case 1: Uncle is RED
                if uncle and uncle.is_red():
                    # Recolor parent, uncle, and grandparent
                    parent.color = "B"
                    uncle.color = "B"
                    grandparent.color = "R"
                    # Move up the tree: continue checking from the grandparent
                    node = grandparent
                else:
                    # Case 2: Uncle is BLACK or None - Node is LEFT child (RL triangle)
                    if node == parent.left:
                        # Perform a right rotation at the parent
                        self._rotate_right(parent)
                        self.rotation_count += 1
                        # After rotation, the original parent becomes the node
                        # for the next step (which is now an RR case)
                        node = parent  # node now points to the original parent
                        parent = node.parent  # update parent reference (original grandparent)
                        # Grandparent remains the same for the next step

                    # Case 3: Uncle is BLACK or None - Node is RIGHT child (RR line)
                    # This case also handles the situation after Case 2's rotation
                    # Recolor parent and grandparent
                    parent.color = "B"
                    grandparent.color = "R"
                    # Perform a left rotation at the grandparent
                    self._rotate_left(grandparent)
                    self.rotation_count += 1
                    # After rotation and recoloring, the subtree is balanced locally.
                    # The loop condition will re-evaluate.

        # Final check: Ensure the root node is always black after all adjustments.
        # This covers the case where the inserted node was the first node,
        # or if recoloring propagated up to the root.
        self.root.color = "B"

    def _rotate_left(self, node: RedBlackTreeNode) -> None:
        """Performs a left rotation around the given node.

        Args:
            node (RedBlackTreeNode): The node around which the rotation is performed (becomes the child).
        """
        self.log.append(f"Left rotation on node {node.value}")
        # Identify the pivot (node's right child) which will move up
        pivot = node.right
        if not pivot:  # Cannot rotate left if there's no right child
            return

        # Step 1: Update node's right child
        # The pivot's left subtree becomes the node's right subtree
        node.right = pivot.left
        if pivot.left:
            pivot.left.parent = node  # Update parent pointer of the moved subtree

        # Step 2: Update pivot's parent
        # The pivot takes the place of the original node
        pivot.parent = node.parent
        if not node.parent:
            # If the node was the root, the pivot becomes the new root
            self.root = pivot
        elif node == node.parent.left:
            # If the node was a left child, update its parent's left child
            node.parent.left = pivot
        else:
            # If the node was a right child, update its parent's right child
            node.parent.right = pivot

        # Step 3: Update pivot's left child and node's parent
        # The original node becomes the left child of the pivot
        pivot.left = node
        node.parent = pivot  # Update the original node's parent pointer

    def _rotate_right(self, node: RedBlackTreeNode) -> None:
        """Performs a right rotation around the given node.

        Args:
            node: The node around which the rotation is performed (becomes the child).
        """
        self.log.append(f"Right rotation on node {node.value}")
        # Identify the pivot (node's left child) which will move up
        pivot = node.left
        if not pivot:  # Cannot rotate right if there's no left child
            return

        # Step 1: Update node's left child
        # The pivot's right subtree becomes the node's left subtree
        node.left = pivot.right
        if pivot.right:
            pivot.right.parent = node  # Update parent pointer of the moved subtree

        # Step 2: Update pivot's parent
        # The pivot takes the place of the original node
        pivot.parent = node.parent
        if not node.parent:
            # If the node was the root, the pivot becomes the new root
            self.root = pivot
        elif node == node.parent.right:
            # If the node was a right child, update its parent's right child
            node.parent.right = pivot
        else:
            # If the node was a left child, update its parent's left child
            node.parent.left = pivot

        # Step 3: Update pivot's right child and node's parent
        # The original node becomes the right child of the pivot
        pivot.right = node
        node.parent = pivot  # Update the original node's parent pointer

    def print_tree(self, node=None, level=0, prefix='Root:'):
        """Print the tree structure."""
        # node = node or self.root
        if node:
            print(' ' * (5 * level) + prefix + f"{node.value}({node.color})")
            self.print_tree(node.left, level + 1, 'L----')
            self.print_tree(node.right, level + 1, 'R----')

    def print_log(self):
        """Print the operation log."""
        print("\n--- Red-Black Tree Log ---")
        for entry in self.log:
            print(entry)
        print(f"Total Rotations: {self.rotation_count}")
        print(f"Final Tree Height: {self.root.get_height() if self.root else -1}")

    # --- Helper methods for traversal/visualization (Optional) ---
    def inorder_traversal(self) -> list:
        """Performs an inorder traversal and returns a list of values."""
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node: RedBlackTreeNode, result: list) -> None:
        if node:
            self._inorder_recursive(node.left, result)
            result.append((node.value, node.color))  # Include color for verification
            self._inorder_recursive(node.right, result)

    def get_red_black_tree_height(self, node: RedBlackTreeNode):
        """Returns the height of the Red-Black Tree by calculating it recursively.

        Args:
            node (RedBlackTreeNode): The node which is used to calculate the height of the Red-Black tree.
        """
        if node is None:
            return -1
        return 1 + max(self.get_red_black_tree_height(node.left), self.get_red_black_tree_height(node.right))


class FlightManager:
    """
    Manages flight schedules using a Red-Black Tree.
    """
    def __init__(self):
        self.tree = RedBlackTree()

    def schedule_flight(self, flight_id):
        """Schedule a flight."""
        print(f"Scheduling flight {flight_id}")
        self.tree.insert(flight_id)

    def display_flight_schedule(self, node=None, level=0, prefix='Root:'):
        """Display the flight schedule tree."""
        print("\n--- Flight Schedule Tree ---")
        self.tree.print_tree(node or self.tree.root, level, prefix)

    def print_operations_log(self):
        """Print the operation log."""
        self.tree.print_log()

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
