# Created by: Michael Jung (ID:10680322), Timothy Sanders (ID: 01002147), Megan Ng (ID: 00756276)

# Date: 4/21/25

# Course: Spr25_CS_034 CRN 39575

#--------------------------------------------------------------------------------------------

from io import StringIO
import sys
import unittest

from binarysearchtree import BST
from bst_node import BstNode
from avl_node import AvlNode

# --- AVLTree Class ---
# Represents a AVL Tree, inheriting basic tree operations from BST.
class AVLTree(BST):
    def __init__(self, root=None):
        """
        Initializes an AVL Tree with an optional root node.

        Args:
            root: The root node of the AVL tree.
        """
        super().__init__(root)    # Inherit from BST


    def get_height(self, node):
        """
        Gets the height of a node in the AVL tree.

        Args:
            node: The node to get the height of.

        Returns:
            int: The height of the node.
        """
        if not node:          # If the node is None
            return -1         # Conventionally -1 for a null node, 0 for a leaf
        return node.height    # Otherwise, return the node's height

    def get_balance(self, node):
        """
        Gets the balance factor of a node in the AVL tree.

        Args:
            node: The node to get the balance factor of.

        Returns:
            int: The balance factor of the node.
        """
        if not node:          # If the node is None
            return 0.         # Balance factor is 0 for a null node (leaf node)
        return self.get_height(node.left) - self.get_height(node.right) # Calculate balance factor

    def left_rotate(self, z):
        """
        Performs a left rotation on a node in the AVL tree.

        Args:
            z: The node to rotate.

        Returns:
            Node: The new root of the rotated subtree.
        """
        # Initialize the nodes needed
        y = z.right
        T2 = y.left

        # Rotate
        y.left = z
        z.right = T2

        # Update heights AFTER rotation
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y   # Return the new root of the subtree (y)

    def right_rotate(self, z):
        """
        Performs a right rotation on a node in the AVL tree.

        Args:
            z: The node to rotate.

        Returns:
            Node: The new root of the rotated subtree.
        """
        # Initialize the nodes needed
        y = z.left
        T3 = y.right

        # Rotate
        y.right = z
        z.left = T3

        # Update heights AFTER rotation
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y   # Return the new root of the subtree (y)

    # Override insert from BST
    def insert(self, value):
        """
        Inserts a value into the AVL Tree, maintaining the AVL property.

        Args:
            value: The value to insert.
        """
        def _insert(node, value):
            """
            Recursive helper for insertion.

            Args:
                node: The current node being examined.
                value: The value to insert.

            Returns:
                Node: The root of the subtree after insertion.
            """
            # Standard BST insertion
            if not node:   # If the current node is None (empty subree)
                return AvlNode(value)    # Create a new node with the value and return it
            if value < node.value:    # If the value is less than the current node's value
                node.left = _insert(node.left, value) # Insert into the left subtree
            elif value > node.value:  # If the value is greater than the current node's value
                node.right = _insert(node.right, value) # Insert into the right subtree
            else:
                print(f"Duplicated key {value} ignored.") # Suppress during insertion if not testing output
                return node # Value already exists, return the current node

            # Update height of current node after insertion into subtree
            node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

            # Get balance factor
            balance = self.get_balance(node)

            # Perform rotations if unbalanced
            # ----------------------------------
            # Left Left Case
            if balance > 1 and value < node.left.value:
                return self.right_rotate(node)

            # Right Right Case
            if balance < -1 and value > node.right.value:
                return self.left_rotate(node)

            # Left Right Case
            if balance > 1 and value > node.left.value:
                node.left = self.left_rotate(node.left)
                return self.right_rotate(node)

            # Right Left Case
            if balance < -1 and value < node.right.value:
                node.right = self.right_rotate(node.right)
                return self.left_rotate(node)

            # Return the (potentially new) root of the subtree
            return node

        self.root = _insert(self.root, value)  # Start the insertion from the root


    # Override print_tree from BinaryTree to include balance factor (already done)
    def print_tree(self, node=None, level=0, prefix='Root:'):
        """
        Prints the AVL tree in a visually appealing format.

        Args:
            node: The starting node for printing. Defaults to the root of the tree.
            level: The current level of the tree. Defaults to 0 (used for indentation).
            prefix: The prefix for indiicate the position of the node (e.g. "Root:", "L----", "R----").
        """
        # Ensure get_balance is called on the correct object (self)
        if node:    # If the current node is not None
            balance = self.get_balance(node)  # Get the balance factor of the node
            print(' ' * (5 * level) + prefix + f"{node.value} (BF={balance})") # Print node value and balance factor
            # Recursively call print_tree on left and right, passing self
            self.print_tree(node.left, level + 1, 'L----') # Print left subtree
            self.print_tree(node.right, level + 1, 'R----') # Print right subtree



# --- Helper function to capture print output ---
# Useful for unit testing methods that print to stdout.
def capture_print_output(func, *args, **kwargs):
    """
    Captures the standard output (stdout) produced by a function call.

    Args:
        func: The function to call.
        *args: Positional arguments to pass to the function.
        **kwargs: Keyword arguments to pass to the function.

    Returns:
        str: The captured output as a string.
    """
    old_stdout = sys.stdout
    sys.stdout = captured_output = StringIO()
    try:
        # Call the function with provided arguments
        func(*args, **kwargs)
    finally:
        # Restore standard output regardless of exceptions
        sys.stdout = old_stdout
    # Return the value captured in the StringIO buffer
    return captured_output.getvalue()


# --- AVLTree Tests ---
# ---------------------
class TestAVLTree(unittest.TestCase):
    def setUp(self):
        self.avl = AVLTree()
        self.values = [50, 30, 70, 20, 40, 60, 80]

    def build_avl_tree(self):
        for value in self.values:
            self.avl.insert(value)

    def test_insert_balancing(self):
        self.build_avl_tree()
        self.assertIsNotNone(self.avl.root, "AVL Tree root should not be None")
        self.assertEqual(self.avl.root.value, 50, "Root should be 50")

    def test_search_inserted_values(self):
        self.build_avl_tree()
        for value in self.values:
            found_node = self.avl.root
            stack = [found_node]
            found = False
            while stack:
                current = stack.pop()
                if current:
                    if current.value == value:
                        found = True
                        break
                    stack.append(current.left)
                    stack.append(current.right)
            self.assertTrue(found, f"Value {value} should be found in AVL Tree")

    def test_insert_duplicate(self):
        self.build_avl_tree()
        captured = StringIO()
        sys.stdout = captured
        self.avl.insert(50)
        sys.stdout = sys.__stdout__
        output = captured.getvalue()
        self.assertIn("Duplicated key 50 ignored.", output)


# --- Command Line Interface ---
# Demonstrate the structure of a sample Binary Tree
# Demonstrate the structure of a sample BST
# Demonstrate the structure of a sample AVL Tree with balance factor (BF)

if __name__ == "__main__":
    # Control whether to run demos or unit tests
    run_tests = False  # <-- Set to True if you want to run unit tests
    if not run_tests:
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
    
    else:
        print("--- Running Unit Tests ---\n")
        unittest.main(argv=['first-arg-is-ignored'], exit=False)
