# Created by: Michael Jung (ID:10680322), Timothy Sanders (ID: 01002147), Megan Ng (ID: 00756276)

# Date: 5/1/25

# Course: Spr25_CS_034 CRN 39575

#--------------------------------------------------------------------------------------------
from typing import Any

from bst_node import BstNode
from red_black_node import RedBlackTreeNode


# RedBlackTree class - represents the Red-Black Tree structure
class RedBlackTree:
    """Represents a Red-Black Tree structure.

    Attributes:
        root (RedBlackTreeNode): A reference to the optional root node of the Red-Black tree
    """
    def __init__(self):
        """
        Initializes an empty Red-Black Tree.
        """
        # The root node of the tree, initially None (empty tree)
        self.root = None

    def insert(self, value: Any) -> None:
        """Inserts a new node with the given key into the Red-Black Tree.

        Args:
            value (Any): The value to be inserted into the tree.
        """
        # Step 1: Perform standard BST insertion and color the new node red.
        new_node = RedBlackTreeNode(value) # New nodes are always initially red

        # Handle the case of an empty tree
        if not self.root:
            # If the tree is empty, the new node becomes the root
            self.root = new_node
        else:
            # Find the correct position for the new node using BST logic
            current = self.root
            parent = None
            while current:
                parent = current # Keep track of the parent
                if value < current.value:
                    current = current.left # Go left
                elif value > current.value:
                    current = current.right # Go right
                else:
                    # Optional: Handle duplicate keys (e.g., ignore, update, raise error)
                    # In this version, we simply don't insert duplicates.
                    print(f"value {value} already exists. Insertion skipped.")
                    return

            # Link the new node to its parent
            new_node.parent = parent
            if value < parent.value:
                parent.left = new_node # Insert as left child
            else:
                parent.right = new_node # Insert as right child

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

            # If grandparent is None, it means parent is the root.
            # Since the loop condition requires parent to be red, and we ensure
            # the root is black *after* _fix_insert, this case shouldn't
            # strictly happen within the loop if called correctly from insert().
            # However, having the check prevents potential errors.
            if grandparent is None:
                 break # Should not happen if parent is red

            uncle = node.get_uncle()

            # Determine the cases based on the parent's position relative to the grandparent
            if parent == grandparent.left:
                # --- Parent is the LEFT child ---

                # Case 1: Uncle is RED
                if uncle and uncle.is_red():
                    # Recolor parent, uncle, and grandparent
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
                        # After rotation, the original parent becomes the node
                        # for the next step (which is now an LL case)
                        node = parent # node now points to the original parent
                        parent = node.parent # update parent reference (original grandparent)
                        # Grandparent remains the same for the next step

                    # Case 3: Uncle is BLACK or None - Node is LEFT child (LL line)
                    # This case also handles the situation after Case 2's rotation
                    # Recolor parent and grandparent
                    parent.color = "B"
                    grandparent.color = "R"
                    # Perform a right rotation at the grandparent
                    self._rotate_right(grandparent)
                    # After rotation and recoloring, the subtree is balanced locally.
                    # The loop condition will re-evaluate.

            else: # parent == grandparent.right
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
                        # After rotation, the original parent becomes the node
                        # for the next step (which is now an RR case)
                        node = parent # node now points to the original parent
                        parent = node.parent # update parent reference (original grandparent)
                        # Grandparent remains the same for the next step

                    # Case 3: Uncle is BLACK or None - Node is RIGHT child (RR line)
                    # This case also handles the situation after Case 2's rotation
                    # Recolor parent and grandparent
                    parent.color = "B"
                    grandparent.color = "R"
                    # Perform a left rotation at the grandparent
                    self._rotate_left(grandparent)
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
        # Identify the pivot (node's right child) which will move up
        pivot = node.right
        if not pivot: # Cannot rotate left if there's no right child
             return

        # Step 1: Update node's right child
        # The pivot's left subtree becomes the node's right subtree
        node.right = pivot.left
        if pivot.left:
            pivot.left.parent = node # Update parent pointer of the moved subtree

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
        node.parent = pivot # Update the original node's parent pointer


    def _rotate_right(self, node: RedBlackTreeNode) -> None:
        """Performs a right rotation around the given node.

        Args:
            node: The node around which the rotation is performed (becomes the child).
        """
        # Identify the pivot (node's left child) which will move up
        pivot = node.left
        if not pivot: # Cannot rotate right if there's no left child
            return

        # Step 1: Update node's left child
        # The pivot's right subtree becomes the node's left subtree
        node.left = pivot.right
        if pivot.right:
            pivot.right.parent = node # Update parent pointer of the moved subtree

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
        node.parent = pivot # Update the original node's parent pointer

    # --- Helper methods for traversal/visualization (Optional) ---
    def inorder_traversal(self) -> list:
        """Performs an inorder traversal and returns a list of values."""
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node: RedBlackTreeNode, result: list) -> None:
        if node:
            self._inorder_recursive(node.left, result)
            result.append((node.value, node.color)) # Include color for verification
            self._inorder_recursive(node.right, result)
            
    def get_red_black_tree_height(self, node : RedBlackTreeNode):
        """Returns the height of the Red-Black Tree by calculating it recursively.

        Args:
            node (RedBlackTreeNode): The node which is used to calculate the height of the Red-Black tree.
        """
        if node is None:
            return -1
        return 1 + max(self.get_red_black_tree_height(node.left), self.get_red_black_tree_height(node.right))
        
# --- Example Usage ---
if __name__ == "__main__":
    rbt = RedBlackTree()
    values_to_insert = [10, 20, 30, 15, 25, 5, 1, 8, 18, 28]

    print("Inserting values:", values_to_insert)
    for value in values_to_insert:
        print(f"\nInserting {value}...")
        rbt.insert(value)
        print("Inorder Traversal (value, color):", rbt.inorder_traversal())
        # You would typically add more checks here to verify RBT properties

    print("\nFinal Tree Root:", rbt.root)
    print("Final Inorder Traversal (value, color):", rbt.inorder_traversal())
