
# Group Members: Michael Jung (ID:10680322), Timothy Sanders (01002147), Megan Ng (ID: 00756276)

# Date: 4/21/25

# Course: Spr25_CS_034 CRN 39575

#--------------------------------------------------------------------------------------------

class BstNode:
    # Constructor for the Node class   
    def __init__(self, value, parent=None):
        """
        Initializes a new node with a given value.

        Args:
            value: The data to be stored in the node. Defaults to None.
        """      
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

# ---- Example Usage  ----
if __name__ == "__main__":
    # Demonstrate instantiation calls __init__ chain
    print("\nCreating BST Node:")
    bst_node = BstNode(20)
    print(f"BST Node value: {bst_node.value}")
    print(f"{str(bst_node)} Left: ({bst_node.left}) Right: ({bst_node.right})")
