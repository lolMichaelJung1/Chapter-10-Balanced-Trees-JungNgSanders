# Created by: Michael Jung (ID:10680322), Timothy Sanders (ID: 01002147), Megan Ng (ID: 00756276)
from bst_node import BstNode
from red_black_node import RedBlackTreeNode


class RedBlackTree:
    def __init__(self):
        self.root = None

    def __len__(self):
        return self.root.count() if self.root else 0

    def insert(self, key):
        new_node = RBTNode(key)
        if not self.root:
            new_node.color = "black"
            self.root = new_node
        else:
            self._bst_insert(new_node)
            self._fix_insert(new_node)

    def _bst_insert(self, node):
        current = self.root
        while current:
            if node.key < current.key:
                if not current.left:
                    current.set_child("left", node)
                    break
                current = current.left
            else:
                if not current.right:
                    current.set_child("right", node)
                    break
                current = current.right

    def _fix_insert(self, node):
        while node.parent and node.parent.is_red():
            parent = node.parent
            grandparent = node.get_grandparent()
            uncle = node.get_uncle()

            if uncle and uncle.is_red():
                parent.color = uncle.color = "black"
                grandparent.color = "red"
                node = grandparent
            else:
                if parent == grandparent.left:
                    if node == parent.right:
                        self._rotate_left(parent)
                        node = parent
                    parent.color = "black"
                    grandparent.color = "red"
                    self._rotate_right(grandparent)
                else:
                    if node == parent.left:
                        self._rotate_right(parent)
                        node = parent
                    parent.color = "black"
                    grandparent.color = "red"
                    self._rotate_left(grandparent)
        self.root.color = "black"

    def _rotate_left(self, node):
        pivot = node.right
        node.right = pivot.left
        if pivot.left:
            pivot.left.parent = node
        pivot.parent = node.parent
        if not node.parent:
            self.root = pivot
        elif node == node.parent.left:
            node.parent.left = pivot
        else:
            node.parent.right = pivot
        pivot.left = node
        node.parent = pivot

    def _rotate_right(self, node):
        pivot = node.left
        node.left = pivot.right
        if pivot.right:
            pivot.right.parent = node
        pivot.parent = node.parent
        if not node.parent:
            self.root = pivot
        elif node == node.parent.right:
            node.parent.right = pivot
        else:
            node.parent.left = pivot
        pivot.right = node
        node.parent = pivot
