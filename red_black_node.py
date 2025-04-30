


# ---- File: red_black_node.py ----

from bst_node import BstNode

class RedBlackNode(BstNode): # Inherit from parent node BstNode
    def __init__(self, key):
        print(f"DEBUG: RedBlackNode.__init__({key}) calling super()") # Added for demo
        super().__init__(key) # Call parent node BstNode constructor
        self.color = 'RED' # Default color


# ---- Example Usage  ----
# Demonstrate instantiation calls __init__ chain
print("\nCreating RedBlackNode:")
rb_n = RedBlackNode(20)


print(f"RedBlackNode key: {rb_n.key}, color: {rb_n.color}")
