
# Group Members: Michael Jung (ID:10680322), Timothy Sanders (01002147), Megan Ng (ID: 00756276)

# Date: 4/21/25

# Course: Spr25_CS_034 CRN 39575

#--------------------------------------------------------------------------------------------

class BstNode:
    # Constructor for the Node class   
    def __init__(self, value=None):
        """
        Initializes a new node with a given value.

        Args:
            value: The data to be stored in the node. Defaults to None.
        """      
        print(f"DEBUG: BstNode.__init__(value}) called") # Added for demo   
        self.value = value  # Store data in the node
        self.left = None    # Pointer to the left child node
        self.right = None   # Pointer to the right child node

    # String representation of the Node
    def __str__(self):
        """
        Returns the string representation of the node's value.
        """
        return str(self.value)

