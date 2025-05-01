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

    def is_red(self):
        """
        Checks if the node is red.

        Returns:
        - True if the node is red, False otherwise.
        """
        return self.color == "red"

    def is_black(self):
        """
        Checks if the node is black.

        Returns:
        - True if the node is black, False otherwise.
        """
        return self.color == "black"

    def get_grandparent(self):
        """
        Gets the grandparent of the current node.

        Returns:
        - The grandparent node, or None if the current node has no grandparent.
        """
        if self.parent:
            return self.parent.parent
        return None

    def get_uncle(self):
        """
        Gets the uncle of the current node.

        Returns:
        - The uncle node, or None if the current node has no uncle.
        """
        grandparent = self.get_grandparent()
        if not grandparent:
            return None
        if self.parent == grandparent.left:
            return grandparent.right
        return grandparent.left

    def get_sibling(self):
        """
        Gets the sibling of the current node.

        Returns:
        - The sibling node, or None if the current node has no sibling.
        """
        if self.parent is None:
            return None
        return self.parent.right if self == self.parent.left else self.parent.left


    def __str__(self):
        """
        Returns a string representation of the node's value and color.
        """
        return f"{self.value}({self.color})"


# ---- Example Usage  ----
if __name__ == "__main__":
    # Demonstrate instantiation calls __init__ chain
    rbt_node = RedBlackTreeNode(10)
    print(f"RBTNode value: {rbt_node.value}, color: {rbt_node.color}")
    print(str(rbt_node) + "(" + rbt_node.color + ")")
