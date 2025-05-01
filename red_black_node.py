# Group Members: Michael Jung (ID:10680322), Timothy Sanders (01002147), Megan Ng (ID: 00756276)

# Date: 4/21/25

# Course: Spr25_CS_034 CRN 39575

#--------------------------------------------------------------------------------------------
from bst_node import BstNode

class RedBlackTreeNode(BstNode):  # This class inherits from BstNode (a basic Binary Search Tree node class)
    def __init__(self, value, parent=None, is_red=True):
        """
        Initializes a new Red-Black Tree Node.

        Args:
            value: The value to be stored in the node.
            parent: The parent node of this node (default: None).
            is_red: True if the node should be colored red initially, otherwise black (default: True).
        """
        super().__init__(value)  # Call the parent class's __init__ to initialize common attributes like value, left, right, parent
        # Set the color of the node based on the 'is_red' parameter:
        # 'R' for red if is_red is True, 'B' for black otherwise
        self.color = 'R' if is_red else 'B'

    def __str__(self):
        """
        Returns a string representation of the node's value and color.
        """
        return f"{self.value}({self.color})"

    def is_red(self):
        """
        Checks if the node is red.

        Returns:
            True if the node is red, False otherwise.
        """
        return self.color == 'R'

    def is_black(self):
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
        return self.parent.parent if self.parent else None

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


# ---- Example Usage  ----
if __name__ == "__main__":
    # Demonstrate instantiation calls __init__ chain
    rbt_node = RedBlackTreeNode(10)
    print(rbt_node)
