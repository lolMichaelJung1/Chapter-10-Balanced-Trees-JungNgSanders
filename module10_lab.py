# Created by: Michael Jung (ID:10680322), Timothy Sanders (ID: 01002147), Megan Ng (ID: 00756276)

# Date: 4/21/25

# Course: Spr25_CS_034 CRN 39575

#--------------------------------------------------------------------------------------------
import random

# === Shared Base Node ===
class BstNode:
    """
    Base node for Binary Search Tree.
    """
    def __init__(self, value, parent=None):
        self.value = value 
        self.left = None   
        self.right = None
        self.parent = parent  # Pointer to the parent node

# === AVL Tree ===
class AvlNode(BstNode):
    """
    Node for AVL Tree, inheriting from BstNode.
    Adds a 'height' attribute for balancing.
    """
    def __init__(self, value):
        super().__init__(value)
        self.height = 1   # Initial height of the node


class AVLTree:
    """
    Implementation of an AVL Tree.
    """
    def __init__(self):
        self.root = None
        self.rotation_count = 0   # Counter for rotations performed
        self.log = []             # Log of operations

    def get_height(self, node):
        """Get the height of a node."""
        return -1 if not node else node.height  # Height is -1 if node is None, otherwise node.height

    def update_height(self, node):
        """Update the height of a node and its ancestors."""
        while node: # Iterate until reaching the root (which has no parent)
            # Update height based on children's heights
            node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
            node = node.parent  # Move up to the parent node

    def get_balance(self, node):
        # Balance factor = height(left) - height(right)       
        return 0 if not node else self.get_height(node.left) - self.get_height(node.right)

    def _rotate_left(self, node):
        self.rotation_count += 1                               # Increment rotation counter
        self.log.append(f"Left rotation on node {node.value}") # Log the rotation
        pivot = node.right  # Set the right child of node as new root (pivot)                                   
        node.right = pivot.left # Set the left child of pivot as node's right child
        if pivot.left:  # If pivot has left child
            pivot.left.parent = node  # Update its parent to be the node being retated
        pivot.parent = node.parent  # Set pivot's parent as node's parent
        if not node.parent: # If node was the root
            self.root = pivot # Set pivot as new root
        elif node == node.parent.left:  # If node was a left child
            node.parent.left = pivot    # pivot replaces node as left child
        else: # If node was a right child
            node.parent.right = pivot   # pivot replaces node as right child
        pivot.left = node # Set node as pivot's left child
        node.parent = pivot # Set node's parent as pivot
        self.update_height(node)  # Update heights after rotation
        self.update_height(pivot) 
        return pivot  # Return the new subtree root (pivot)

    def _rotate_right(self, node):
        self.rotation_count += 1                               # Increment rotation counter
        self.log.append(f"Right rotation on node {node.value}")# Log the rotation
        pivot = node.left  # Set the left child of node as new root (pivot)  
        node.left = pivot.right # Set the right child of pivot as node's left child
        if pivot.right:  # If pivot has right child
            pivot.right.parent = node # Update its parent to be the node being rotated
        pivot.parent = node.parent  # Set pivot's parent as node's parent
        if not node.parent: # If node was the root
            self.root = pivot # Set pivot as new root
        elif node == node.parent.right: # If node was a right child
            node.parent.right = pivot # pivot replaces node as right child
        else: # If node was a left child
            node.parent.left = pivot # pivot replaces node as left child
        pivot.right = node  # Set node as pivot's right child
        node.parent = pivot # Set node's parent as pivot
        self.update_height(node)  # Update heights after rotation
        self.update_height(pivot)
        return pivot    # Return the new subtree root (pivot)

    def update_balance(self, node):
        """Update balance factors and perform rotations if needed."""
        while node: # Iterate until reaching the root
            balance = self.get_balance(node) # Get the balance factor
            if balance > 1: # Left heavy
                if self.get_balance(node.left) < 0: # Left-Right case
                    node.left = self._rotate_left(node.left) # Perform left rotation on the left child
                node = self._rotate_right(node) # Perform right rotation on node
            elif balance < -1: # Right heavy
                if self.get_balance(node.right) > 0: # Right-Left case
                    node.right = self._rotate_right(node.right) # Perform right rotation on right child
                node = self._rotate_left(node) # Perform left rotation on node
            else:
                node = node.parent # Move up to the parent node

    def insert(self, value):
        """Insert a new value into the AVL Tree."""
        new_node = AvlNode(value) # Create a new node
        if not self.root: # If the tree is empty
            self.root = new_node # The new node becomes the root
            self.log.append(f"Inserted {value}, tree height: {self.get_height(self.root)}") # Log the insertion
            return
        parent, current = None, self.root # Start at the root
        while current:  #Traverse the tree
            parent = current # keep track of the parent
            if value < current.value: # Go left
                current = current.left
            elif value > current.value: # Go right
                current = current.right
            else:
                return # Duplicate, do nothing
        new_node.parent = parent # Set parent of the new node
        if value < parent.value: # Insert as left child
            parent.left = new_node
        else: # Insert as right child
            parent.right = new_node
        self.update_height(new_node) # Update heights after insertion
        self.update_balance(new_node) # Update balance factors and rotate if needed
        self.log.append(f"Inserted {value}, tree height: {self.get_height(self.root)}") # Log the insertion

    def print_tree(self, node=None, level=0, prefix='Root:', visited=None):
        if node:
            print(' ' * (5 * level) + prefix + f"{node.value} (BF={self.get_balance(node)})") # Print node value and BF
            self.print_tree(node.left, level + 1, 'L----', visited) # Recursively print left subtree
            self.print_tree(node.right, level + 1, 'R----', visited) # Recursively print right subtree

    def print_log(self):
        print("\n--- AVL Tree Log ---")
        for entry in self.log:  # Print each entry in the log
            print(entry)
        print(f"Total Rotations: {self.rotation_count}") # Print total rotations performed
        print(f"Final Tree Height: {self.get_height(self.root)}") # Print final height of the tree

class InventoryManager:
    def __init__(self):
        self.tree = AVLTree()

    def add_item(self, item_id):
        print(f"Adding inventory item: {item_id}")
        self.tree.insert(item_id)

    def show_inventory(self, node=None, level=0, prefix='Root:', visited=None):
        print("\n--- Inventory Tree ---")
        self.tree.print_tree(node or self.tree.root, level, prefix, visited)

    def show_log(self):
        self.tree.print_log()


# === Red-Black Tree ===
class RedBlackTreeNode(BstNode):
    """
    Node for Red-Black Tree, inheriting from BstNode.
    Adds a 'color' attribute for balancing.
    """
    def __init__(self, value, parent=None, is_red=True):
        super().__init__(value, parent)
        self.color = 'R' if is_red else 'B'  # Node color (Red or Black)

    def is_red(self): 
        """Check if the node is red."""
        return self.color == 'R'

    def is_black(self): 
        """Check if the node is black."""
        return self.color == 'B'

    def get_grandparent(self): 
        """Get the grandparent of the node."""
        return self.parent.parent if self.parent and self.parent.parent else None

    def get_uncle(self):
        """Get the uncle of the node."""
        gp = self.get_grandparent()
        return gp.right if self.parent == gp.left else gp.left if gp else None

    def get_sibling(self): 
        """Get the sibling of the node."""
        return self.parent.right if self == self.parent.left else self.parent.left if self.parent else None

    def get_height(self):
        """Get the height of the node."""
        l = self.left.get_height() if self.left else -1
        r = self.right.get_height() if self.right else -1
        return 1 + max(l, r)

class RedBlackTree:
    """
    Implementation of a Red-Black Tree.
    """
    def __init__(self):
        self.root = None  # Root of the tree
        self.rotation_count = 0  # Counter for rotations performed
        self.log = []  # Log of operations

    def insert(self, value):
        """Insert a new value into the Red-Black Tree."""
        new_node = RedBlackTreeNode(value)
        if not self.root:
            self.root = new_node
            new_node.color = 'B'  # Root is always black
            return
        parent, current = None, self.root
        while current:
            parent = current
            if value < current.value:
                current = current.left
            else:
                current = current.right
        new_node.parent = parent
        if value < parent.value:
            parent.left = new_node
        else:
            parent.right = new_node
        self._fix_insert(new_node)

    def _fix_insert(self, node):
        """Fix the tree after insertion to maintain Red-Black properties."""
        while node != self.root and node.parent.is_red():
            p, gp, u = node.parent, node.get_grandparent(), node.get_uncle()
            if u and u.is_red():  # Case 1: Uncle is red
                self.log.append(f"Recoloring: {p.value}, {u.value}, {gp.value}")
                p.color = 'B'; u.color = 'B'; gp.color = 'R'; node = gp
            else:  # Case 2: Uncle is black
                if p == gp.left:  # Parent is left child of grandparent
                    if node == p.right:  # Node is right child of parent (Left-Right case)
                        self._rotate_left(p); node = p
                    node.parent.color = 'B'; gp.color = 'R'; self._rotate_right(gp) # Left-Left case
                else:  # Parent is right child of grandparent
                    if node == p.left:  # Node is left child of parent (Right-Left case)
                        self._rotate_right(p); node = p
                    node.parent.color = 'B'; gp.color = 'R'; self._rotate_left(gp) # Right-Right case
                self.rotation_count += 1
        self.root.color = 'B'  # Ensure root is black

    def _rotate_left(self, node):
        """Perform a left rotation on a node."""
        self.log.append(f"Left rotation on node {node.value}")
        pivot = node.right
        node.right = pivot.left
        if pivot.left: pivot.left.parent = node
        pivot.parent = node.parent
        if not node.parent: self.root = pivot
        elif node == node.parent.left: node.parent.left = pivot
        else: node.parent.right = pivot
        pivot.left = node; node.parent = pivot

    def _rotate_right(self, node):
        """Perform a right rotation on a node."""
        self.log.append(f"Right rotation on node {node.value}")
        pivot = node.left
        node.left = pivot.right
        if pivot.right: pivot.right.parent = node
        pivot.parent = node.parent
        if not node.parent: self.root = pivot
        elif node == node.parent.right: node.parent.right = pivot
        else: node.parent.left = pivot
        pivot.right = node; node.parent = pivot

    def print_tree(self, node=None, level=0, prefix='Root:'):
        """Print the tree structure."""
        #node = node or self.root
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

# === Unified Demo Script ===
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
    random_avl_tree.print_tree(random_avl_tree.root)  # use default = safest
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
    random_rb_tree.print_tree(random_rb_tree.root)  # safest call
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
