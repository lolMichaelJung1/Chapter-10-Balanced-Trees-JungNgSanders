import pytest
from RedBlackTree import RedBlackTree
from red_black_node import RedBlackTreeNode

@pytest.fixture
def rbtree():
    return RedBlackTree()

def insert_values(tree, values):
    for value in values:
        tree.insert(value)

def test_empty_tree_initialization(rbtree):
    assert rbtree.root is None
    assert rbtree.rotation_count == 0
    assert rbtree.log == []

def test_single_insertion_sets_root_black(rbtree):
    rbtree.insert(10)
    assert rbtree.root is not None
    assert rbtree.root.value == 10
    assert rbtree.root.color == "B"

def test_duplicate_insertion_prints_message(rbtree):
    rbtree.insert(10)
    rbtree.insert(10)  # duplicate
    assert any("value 10 already exists" in msg.lower() for msg in rbtree.log)

def test_inorder_traversal_values_only(rbtree):
    values = [20, 10, 30]
    insert_values(rbtree, values)
    inorder = [val for val, _ in rbtree.inorder_traversal()]
    assert inorder == sorted(values)

def test_color_property_preserved(rbtree):
    insert_values(rbtree, [10, 20, 30, 15])
    for val, color in rbtree.inorder_traversal():
        assert color in ("R", "B")

def test_rotation_logging(rbtree):
    insert_values(rbtree, [10, 20, 30])
    assert any("rotation" in msg.lower() for msg in rbtree.log)

def test_get_red_black_tree_height(rbtree):
    insert_values(rbtree, [10, 20, 30, 5])
    height = rbtree.get_red_black_tree_height(rbtree.root)
    assert isinstance(height, int)
    assert height >= 0

def test_root_is_black_after_multiple_insertions(rbtree):
    insert_values(rbtree, [10, 20, 5, 1, 15])
    assert rbtree.root.color == "B"

def test_node_default_color_red():
    node = RedBlackTreeNode(10)
    assert node.color == "R"
    assert node.is_red()
    assert not node.is_black()

def test_node_explicit_color_black():
    node = RedBlackTreeNode(20, is_red=False)
    assert node.color == "B"
    assert node.is_black()
    assert not node.is_red()

def test_str_method_output():
    node = RedBlackTreeNode(30)
    assert str(node) == "30(R)"

def test_grandparent_returned_correctly():
    tree = RedBlackTree()
    tree.insert(10)
    tree.insert(5)
    tree.insert(7)
    tree.insert(1)
    tree.insert(3)
    node = tree.root.left.left
    assert node.get_grandparent() == tree.root

def test_grandparent_none_if_missing():
    node = RedBlackTreeNode(5)
    assert node.get_grandparent() is None

def test_uncle_returns_correct_node():
    tree = RedBlackTree()
    tree.insert(10)
    tree.insert(5)
    tree.insert(15)
    tree.insert(1)
    node = tree.root.left.left
    assert node.get_uncle() == tree.root.right

def test_sibling_returns_correct_node():
    tree = RedBlackTree()
    tree.insert(10)
    tree.insert(5)
    tree.insert(15)
    left = tree.root.left
    right = tree.root.right
    assert left.get_sibling() == right
    assert right.get_sibling() == left

def test_sibling_none_if_no_parent():
    node = RedBlackTreeNode(10)
    assert node.get_sibling() is None

def test_get_height_leaf_node():
    node = RedBlackTreeNode(5)
    assert node.get_height() == 0

def test_get_height_with_children():
    root = RedBlackTreeNode(1)
    root.left = RedBlackTreeNode(2, parent=root)
    root.right = RedBlackTreeNode(3, parent=root)
    root.left.left = RedBlackTreeNode(4, parent=root.left)
    assert root.get_height() == 2