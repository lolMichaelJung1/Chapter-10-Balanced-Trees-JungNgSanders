# Group Members: Michael Jung (ID:10680322), Timothy Sanders (01002147), Megan Ng (ID: 00756276)

# Date: 4/21/25

# Course: Spr25_CS_034 CRN 39575

#--------------------------------------------------------------------------------------------
from bst_node import BstNode


class AvlNode(BstNode): # Inherit from BstNode class
    def __init__(self, key):
        print(f"DEBUG: AvlNode.__init__({key}) calling super()") # Added for demo
        super().__init__(key)  # Call BstNode constructor
        self.height = 1        # Height of the node

# --------- Example Use ---------
# Demonstrate instantiatioin calls __init__ chain
print("Creating AvlNode:")
avl_node = AvlNode(10)

print(f"\nAvlNode key: {avl_node.value}, height: {avl_node.height}")
