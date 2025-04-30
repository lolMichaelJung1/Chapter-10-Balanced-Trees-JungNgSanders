# Group Members: Michael Jung (ID:10680322), Timothy Sanders (01002147), Megan Ng (ID: 00756276)

# Date: 4/21/25

# Course: Spr25_CS_034 CRN 39575

#--------------------------------------------------------------------------------------------


# ---- File: red_black_node.py ----

from bst_node import BstNode

class RedBlackNode(BstNode): # Inherit from parent node BstNode
    def __init__(self, value):
        print(f"DEBUG: RedBlackNode.__init__({value}) calling super()") # Added for demo
        super().__init__(value) # Call parent node BstNode constructor
        self.color = 'R' # Default color


# ---- Example Usage  ----
# Demonstrate instantiation calls __init__ chain
print("\nCreating RedBlackNode:")
rb_node = RedBlackNode(20)


print(f"RedBlackNode value: {rb_node.value}, color: {rb_node.color}")
print(str(rd_node) + "(" + rd_node.color + ")")
