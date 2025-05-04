# Group Members: Michael Jung (ID:10680322), Timothy Sanders (01002147), Megan Ng (ID: 00756276)

# Date: 4/21/25

# Course: Spr25_CS_034 CRN 39575

#--------------------------------------------------------------------------------------------
from bst_node import BstNode


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

# --------- Example Use ---------
# Demonstrate instantiation calls __init__ chain
if __name__ == "__main__":
    # Demonstrate instantiation calls __init__ chain
    print("Creating AvlNode:")
    avl_node = AvlNode(10, debug=True)  # Instantiate an object of AvlNode with value 10
    print(avl_node)  # Print the node (call the __str__ for a user-friendly output)
